#!/usr/bin/env python3
"""Resolve PDF URLs from official proceedings using confirmed publication metadata."""

from __future__ import annotations

import argparse
import json
import re
import time
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from verify_all_titles import is_verified_in_range
from publication_lib import write_json, write_review_csv

USER_AGENT = "OpenNLG-publication-import/1.0 (official proceedings PDF lookup)"


class PdfLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href", "")
            if href:
                self.links.append(href)


def fetch_text(url: str) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=25) as response:  # nosec B310: URL is derived from vetted publication metadata
        return response.read().decode("utf-8", errors="replace")


def direct_pdf_from_url(url: str) -> str:
    """Resolve deterministic official PDF URL patterns without guessing an identifier."""
    if not url:
        return ""
    parsed = urlparse(url)
    if url.startswith("https://doi.org/10.18653/v1/"):
        return f"https://aclanthology.org/{url.rsplit('/', 1)[-1]}.pdf"
    if url.startswith("https://doi.org/10.1145/"):
        return f"https://dl.acm.org/doi/pdf/{url.removeprefix('https://doi.org/')}"
    if parsed.netloc == "aclanthology.org" and parsed.path.strip("/"):
        return f"https://aclanthology.org/{parsed.path.strip('/')}.pdf"
    if parsed.netloc.endswith("openreview.net") and parsed.path == "/forum" and "id=" in parsed.query:
        return f"https://openreview.net/pdf?{parsed.query}"
    if "-Abstract-Conference.html" in parsed.path:
        return url.replace("-Abstract-Conference.html", "-Paper-Conference.pdf")
    if "-Abstract-Datasets_and_Benchmarks_Track.html" in parsed.path:
        return url.replace("-Abstract-Datasets_and_Benchmarks_Track.html", "-Paper-Datasets_and_Benchmarks_Track.pdf")
    if parsed.path.lower().endswith(".pdf"):
        return url
    return ""


def dblp_ee(record_url: str) -> str:
    if not record_url.startswith("https://dblp.org/rec/"):
        return ""
    xml = fetch_text(f"{record_url}.xml")
    root = ET.fromstring(xml)
    ee = root.find(".//ee")
    return ee.text.strip() if ee is not None and ee.text else ""


def pdf_from_landing_page(url: str) -> str:
    html = fetch_text(url)
    parser = PdfLinkParser()
    parser.feed(html)
    candidates = [urljoin(url, href) for href in parser.links]
    for candidate in candidates:
        if candidate.lower().endswith(".pdf") or "/pdf?" in candidate.lower() or "download" in candidate.lower() and "pdf" in candidate.lower():
            return candidate
    return ""


def resolve_record(record: dict, overrides: dict[str, str]) -> str:
    if record.get("metadata_url", "") in overrides:
        return overrides[record["metadata_url"]]
    direct = direct_pdf_from_url(record.get("metadata_url", ""))
    if direct:
        return direct
    try:
        ee = dblp_ee(record.get("metadata_url", ""))
    except Exception:
        return ""
    direct = direct_pdf_from_url(ee)
    if direct:
        return direct
    if ee:
        try:
            return pdf_from_landing_page(ee)
        except Exception:
            return ""
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description="从官方会议论文库补全已确认论文的 PDF")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--from-year", type=int, default=2024)
    parser.add_argument("--to-year", type=int, default=2026)
    parser.add_argument("--overrides", type=Path, default=Path(__file__).with_name("official_pdf_overrides.json"))
    parser.add_argument("--rate-seconds", type=float, default=1.0)
    args = parser.parse_args()
    rows = json.loads(args.input.read_text(encoding="utf-8"))
    overrides = json.loads(args.overrides.read_text(encoding="utf-8"))
    targets = [row for row in rows if is_verified_in_range(row, args.from_year, args.to_year) and not row.get("pdf_url")]
    for index, row in enumerate(targets, start=1):
        print(f"[{index}/{len(targets)}] {row['title']}", flush=True)
        pdf_url = resolve_record(row, overrides)
        if pdf_url:
            row["pdf_url"] = pdf_url
            row["pdf_status"] = "found"
            row["pdf_metadata_source"] = "official_proceedings"
        time.sleep(args.rate_seconds)

    verified = [row for row in rows if is_verified_in_range(row, args.from_year, args.to_year)]
    final = [{**row, "decision": "include", "acceptance_confirmed": "yes"} for row in verified if row.get("pdf_url")]
    missing = [row for row in verified if not row.get("pdf_url")]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_json(args.output_dir / "verification-results.json", rows)
    write_review_csv(args.output_dir / "review-all.csv", rows)
    write_json(args.output_dir / "verified-conferences.json", final)
    write_review_csv(args.output_dir / "verified-conferences.csv", final)
    write_json(args.output_dir / "verified-missing-pdf.json", missing)
    print(f"官方论文库解析完成：最终记录 {len(final)} 篇，仍缺 PDF {len(missing)} 篇。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
