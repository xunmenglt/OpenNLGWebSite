#!/usr/bin/env python3
"""Extract 2025+ conference candidates from a user-saved Google Scholar profile HTML file.

This script intentionally does not request Google Scholar. Save the fully expanded profile
page in a browser, then pass that local HTML file to this program.
"""

from __future__ import annotations

import argparse
from datetime import date
from email import policy
from email.parser import BytesParser
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urljoin

from publication_lib import (
    author_sequence_complete,
    classify_venue,
    clean_text,
    load_venues,
    venue_label,
    write_json,
    write_review_csv,
)


class ScholarWorksParser(HTMLParser):
    """Small parser for Google Scholar's public profile work rows (.gsc_a_tr)."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.records: list[dict[str, str]] = []
        self.current: dict[str, str] | None = None
        self.capture_stack: list[tuple[str, str]] = []

    @staticmethod
    def _classes(attrs: list[tuple[str, str | None]]) -> set[str]:
        return set(dict(attrs).get("class", "").split())

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        classes = self._classes(attrs)
        attrs_map = dict(attrs)
        if tag == "tr" and "gsc_a_tr" in classes:
            self.current = {"title": "", "authors": "", "source": "", "year": "", "href": ""}
            return
        if not self.current:
            return
        field = ""
        if tag == "a" and "gsc_a_at" in classes:
            self.current["href"] = attrs_map.get("href") or ""
            field = "title"
        elif "gs_gray" in classes:
            field = "authors" if not self.current["authors"] else "source"
        elif "gsc_a_y" in classes:
            field = "year"
        if field:
            self.capture_stack.append((tag, field))

    def handle_data(self, data: str) -> None:
        if self.current and self.capture_stack:
            self.current[self.capture_stack[-1][1]] += data

    def handle_endtag(self, tag: str) -> None:
        if self.capture_stack and self.capture_stack[-1][0] == tag:
            self.capture_stack.pop()
        if tag == "tr" and self.current:
            self.records.append({key: clean_text(value) for key, value in self.current.items()})
            self.current = None
            self.capture_stack.clear()


def parse_profile(path: Path) -> list[dict[str, str]]:
    if path.suffix.lower() in {".mht", ".mhtml"}:
        message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
        html_part = next(
            (part for part in message.walk() if part.get_content_type() == "text/html"),
            None,
        )
        if html_part is None:
            raise ValueError("MHTML 文件中未找到 text/html 内容")
        html = html_part.get_content()
    else:
        html = path.read_text(encoding="utf-8", errors="replace")
    parser = ScholarWorksParser()
    parser.feed(html)
    parser.close()
    return [record for record in parser.records if record["title"]]


def conference_year(source: str, short_name: str, scholar_year: int) -> int:
    """Prefer the explicit year adjacent to the venue name over Scholar's list year.

    Scholar may retain a preprint's first-seen year after the work is accepted by a
    later conference. The website groups papers by the conference year instead.
    """
    venue_match = re.search(
        rf"\b{re.escape(short_name)}\s*[-–]?\s*(20\d{{2}})\b",
        source,
        flags=re.IGNORECASE,
    )
    if venue_match:
        return int(venue_match.group(1))
    source_years = [int(value) for value in re.findall(r"\b(20\d{2})\b", source)]
    return source_years[-1] if source_years else scholar_year


def main() -> int:
    parser = argparse.ArgumentParser(description="从本地保存的 Scholar 个人主页提取会议论文候选项")
    parser.add_argument("--input", required=True, type=Path, help="浏览器保存的 Scholar HTML 文件")
    parser.add_argument("--output-dir", required=True, type=Path, help="本次运行的输出目录")
    parser.add_argument("--from-year", type=int, default=2025)
    parser.add_argument("--to-year", type=int, default=date.today().year)
    parser.add_argument("--profile-url", default="https://scholar.google.com/citations?user=sZSygsYAAAAJ")
    parser.add_argument("--venues", type=Path, default=Path(__file__).with_name("venues.json"))
    args = parser.parse_args()
    if args.from_year > args.to_year:
        parser.error("from-year 不能大于 to-year")

    venues = load_venues(args.venues)
    accepted: list[dict[str, object]] = []
    rejected: list[dict[str, str]] = []
    for record in parse_profile(args.input):
        try:
            year = int(record["year"])
        except ValueError:
            rejected.append({**record, "reason": "Scholar 条目没有可解析的年份"})
            continue
        short_name = classify_venue(record["source"], venues)
        if not short_name:
            rejected.append({**record, "reason": "来源未匹配会议白名单，不能确认是正式会议论文"})
            continue
        year = conference_year(record["source"], short_name, year)
        if not args.from_year <= year <= args.to_year:
            rejected.append({**record, "reason": "正式会议年份不在指定范围内"})
            continue
        full_authors_needed = not author_sequence_complete(record["authors"])
        accepted.append({
            "decision": "",
            "acceptance_confirmed": "",
            "notes": "需要人工确认已录取/正式会议论文",
            "title": record["title"],
            "publication_year": year,
            "venue_short_name": short_name,
            "venue_label": venue_label(short_name, year),
            "authors": record["authors"],
            "source": record["source"],
            "detail_url": urljoin("https://scholar.google.com", record["href"]),
            "metadata_source": "Google Scholar (manual HTML export)",
            "metadata_url": "",
            "pdf_url": "",
            "status": "needs_author_enrichment" if full_authors_needed else "needs_acceptance_review",
            "needs_author_enrichment": full_authors_needed,
            "scholar_year": record["year"],
            "scholar_source": record["source"],
        })

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_json(args.output_dir / "candidates.json", accepted)
    write_json(args.output_dir / "rejected.json", rejected)
    write_review_csv(args.output_dir / "review.csv", accepted)
    print(f"已提取候选 {len(accepted)} 条，排除 {len(rejected)} 条。")
    print(f"请先运行 enrich_publications.py，再编辑 {args.output_dir / 'review.csv'}。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
