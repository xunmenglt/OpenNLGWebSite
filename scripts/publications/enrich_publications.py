#!/usr/bin/env python3
"""Enrich Scholar candidates with DBLP/Crossref metadata; never writes to the website database."""

from __future__ import annotations

import argparse
import json
import time
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from publication_lib import author_sequence_complete, clean_authors, clean_text, load_json, normalise_title, write_json, write_review_csv

USER_AGENT = "OpenNLG-publication-import/1.0 (metadata verification; contact: website administrator)"


def fetch_json(url: str) -> dict:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(request, timeout=20) as response:  # nosec B310: public metadata endpoints supplied by this script
        return json.loads(response.read().decode("utf-8"))


def score_title(candidate: str, observed: str) -> float:
    return SequenceMatcher(None, normalise_title(candidate), normalise_title(observed)).ratio()


def authors_to_text(authors: object) -> str:
    if isinstance(authors, dict):
        authors = authors.get("author", [])
    if isinstance(authors, dict):
        authors = [authors]
    if not isinstance(authors, list):
        return ""
    names = []
    for author in authors:
        if isinstance(author, dict):
            names.append(clean_text(author.get("text") or author.get("@text") or author.get("family", "")))
        else:
            names.append(clean_text(str(author)))
    return clean_authors(", ".join(name for name in names if name))


def enrich_dblp(record: dict) -> dict | None:
    query = urlencode({"q": f'title:{record["title"]}', "h": 10, "format": "json"})
    payload = fetch_json(f"https://dblp.org/search/publ/api?{query}")
    hits = payload.get("result", {}).get("hits", {}).get("hit", [])
    if isinstance(hits, dict):
        hits = [hits]
    best: tuple[float, dict] | None = None
    for hit in hits if isinstance(hits, list) else []:
        info = hit.get("info", {})
        score = score_title(record["title"], info.get("title", ""))
        if best is None or score > best[0]:
            best = (score, info)
    if not best or best[0] < 0.92:
        return None
    _, info = best
    return {
        "authors": authors_to_text(info.get("authors", {})),
        "source": clean_text(info.get("venue", "")) or record["source"],
        "metadata_source": "DBLP",
        "metadata_url": info.get("url", ""),
        "pdf_url": info.get("ee", "") if str(info.get("ee", "")).lower().endswith(".pdf") else "",
    }


def enrich_crossref(record: dict) -> dict | None:
    query = urlencode({"query.title": record["title"], "rows": 5, "select": "title,author,container-title,URL,link"})
    payload = fetch_json(f"https://api.crossref.org/works?{query}")
    best: tuple[float, dict] | None = None
    for item in payload.get("message", {}).get("items", []):
        title = (item.get("title") or [""])[0]
        score = score_title(record["title"], title)
        if best is None or score > best[0]:
            best = (score, item)
    if not best or best[0] < 0.92:
        return None
    _, item = best
    names = [clean_text(" ".join(filter(None, [author.get("given"), author.get("family")])) ) for author in item.get("author", [])]
    links = item.get("link") or []
    pdf_url = next((link.get("URL", "") for link in links if "pdf" in link.get("content-type", "").lower()), "")
    return {
        "authors": clean_authors(", ".join(name for name in names if name)),
        "source": clean_text((item.get("container-title") or [record["source"]])[0]),
        "metadata_source": "Crossref",
        "metadata_url": item.get("URL", ""),
        "pdf_url": pdf_url,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="使用公开元数据补全作者序列与论文链接")
    parser.add_argument("--input", required=True, type=Path, help="extract_scholar.py 生成的 candidates.json")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--reuse-from", type=Path, help="复用此前 enriched.json 中按标题匹配的元数据")
    parser.add_argument("--offline", action="store_true", help="不访问 DBLP/Crossref，只生成复核文件")
    parser.add_argument("--rate-seconds", type=float, default=1.0, help="公开元数据请求之间的间隔")
    args = parser.parse_args()
    records = load_json(args.input)
    if not isinstance(records, list):
        parser.error("input 必须是 candidates.json 数组")

    cached_by_title = {}
    if args.reuse_from:
        cached = load_json(args.reuse_from)
        if not isinstance(cached, list):
            parser.error("reuse-from 必须是 enriched.json 数组")
        cached_by_title = {
            normalise_title(item.get("title", "")): item
            for item in cached
            if item.get("metadata_source") and item.get("metadata_source") != "Google Scholar (manual HTML export)"
        }

    enriched = []
    for index, record in enumerate(records, start=1):
        item = dict(record)
        metadata = None
        cached_item = cached_by_title.get(normalise_title(item["title"]))
        if cached_item:
            metadata = {
                key: cached_item.get(key, "")
                for key in ("authors", "source", "metadata_source", "metadata_url", "pdf_url")
            }
        elif not args.offline:
            for provider in (enrich_dblp, enrich_crossref):
                try:
                    metadata = provider(item)
                except Exception as error:  # leave the record for review; do not stop a batch
                    item["notes"] = f"元数据查询失败：{type(error).__name__}"
                if metadata:
                    break
                time.sleep(args.rate_seconds)
        if metadata:
            item.update({key: value for key, value in metadata.items() if value})
            item["needs_author_enrichment"] = not author_sequence_complete(item.get("authors", ""))
            item["status"] = "needs_acceptance_review" if author_sequence_complete(item.get("authors", "")) else "needs_author_review"
            item["notes"] = "请确认已录取/正式会议论文，再将 decision 设为 include。"
        elif item.get("status") == "needs_author_enrichment":
            item["notes"] = "未能补全完整作者序列；请人工补充后再导入。"
        enriched.append(item)
        if not args.offline and index < len(records):
            time.sleep(args.rate_seconds)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_json(args.output_dir / "enriched.json", enriched)
    write_review_csv(args.output_dir / "review.csv", enriched)
    print(f"已处理 {len(enriched)} 条候选，复核文件：{args.output_dir / 'review.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
