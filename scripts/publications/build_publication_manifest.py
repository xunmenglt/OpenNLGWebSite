#!/usr/bin/env python3
"""Create a database-ready publication manifest from the inclusive audit.

The manifest is deliberately separate from the source audit: it records display
venue abbreviations and legacy title aliases without mutating research evidence.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from publication_lib import clean_text, write_json


JOURNAL_VENUES = {
    "transactions of the association for computational linguistics": "TACL",
    "ieee transactions on audio, speech and language processing": "IEEE TASLP",
    "acm computing surveys": "ACM CSUR",
    "ieee transactions on knowledge and data engineering": "IEEE TKDE",
    "ieee transactions on pattern analysis and machine intelligence": "IEEE TPAMI",
}

# Known production titles that pre-date canonical metadata; this is only used
# by the importer to update the old row instead of creating a duplicate.
LEGACY_ALIASES = {
    "A³: Automatic Alignment Framework for Attributed Text Generation": [
        "A3: Automatic Alignment Framework for Attributed Text Generation"
    ],
    "Unleashing LLM Reasoning Capability via Scalable Question Synthesis from Scratch": [
        "Unleashing Reasoning Capability of LLMs via Scalable Question Synthesis from Scratch"
    ],
    "SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning": [
        "Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning"
    ],
    "Thoughts Are All Over the Place: On the Underthinking of Long Reasoning Models": [
        "Thoughts are all over the place: On the underthinking of o1-like llms"
    ],
}


def venue_for(record: dict) -> str:
    current = clean_text(record.get("venue_short_name", ""))
    if current:
        return current
    source = clean_text(record.get("source", ""))
    return JOURNAL_VENUES.get(source.lower(), source)


def build_record(record: dict) -> dict:
    title = clean_text(record["title"])
    return {
        "title": title,
        "aliases": LEGACY_ALIASES.get(title, []),
        "authors": clean_text(record.get("authors", "")),
        "publication_year": int(record["publication_year"]),
        "publication_type": clean_text(record.get("publication_type", "")),
        "venue_short_name": venue_for(record),
        "source": clean_text(record.get("source", "")),
        "pdf_url": clean_text(record.get("pdf_url", "")),
        "doi_url": clean_text(record.get("metadata_url", "")) if str(record.get("metadata_url", "")).startswith("https://doi.org/") else "",
        "outside_url": clean_text(record.get("metadata_url", "") or record.get("detail_url", "")),
        "metadata_source": clean_text(record.get("metadata_source", "")),
        "formal_status": clean_text(record.get("formal_status", "")),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="构建 OpenNLG 论文数据库导入清单")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    source = json.loads(args.input.read_text(encoding="utf-8"))
    records = [build_record(row) for row in source if row.get("decision") == "include"]
    records.sort(key=lambda row: (-row["publication_year"], row["publication_type"], row["venue_short_name"], row["title"]))
    write_json(args.output, records)
    missing = [row["title"] for row in records if not row["pdf_url"]]
    print(f"已生成 {len(records)} 条数据库清单；缺直接 PDF {len(missing)} 条。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
