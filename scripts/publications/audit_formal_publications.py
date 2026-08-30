#!/usr/bin/env python3
"""Build an inclusive audit of formally published conference and journal papers.

This intentionally differs from ``verify_all_titles.py``: venue whitelists are
not admission criteria here.  A record is included only when it has public
publication evidence from DBLP/Crossref, or a curated official proceedings
override.  Preprints and entries that merely *claim* a venue stay in the review
file rather than being silently included.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from publication_lib import normalise_title, write_json, write_review_csv


JOURNAL_PATTERNS = (
    r"\btransactions\b",
    r"\bcomputing surveys\b",
    r"\bcomputational linguistics\b",
    r"\bknowledge and data engineering\b",
    r"\bpattern analysis and machine intelligence\b",
)
PROCEEDINGS_PATTERNS = (r"\bproceedings\b", r"\blecture notes\b", r"\bfrontiers in artificial intelligence and applications\b")
PREPRINT_PATTERNS = (r"\barxiv\b", r"\bpreprint\b", r"\bcorr\b")


def source_kind(source: str) -> str:
    text = source.lower()
    if any(re.search(pattern, text) for pattern in PREPRINT_PATTERNS):
        return "preprint"
    if "transactions of the association for computational linguistics" in text:
        return "journal"
    if any(re.search(pattern, text) for pattern in JOURNAL_PATTERNS):
        # Avoid treating "Association for Computational Linguistics" as a journal.
        if "association for computational linguistics" not in text:
            return "journal"
    if any(re.search(pattern, text) for pattern in PROCEEDINGS_PATTERNS):
        return "conference"
    return "unknown"


def trusted_evidence(row: dict) -> dict | None:
    for item in row.get("evidence", []):
        if item.get("provider") in {"DBLP", "Crossref"} and item.get("matched"):
            kind = source_kind(item.get("source", ""))
            if kind in {"conference", "journal"}:
                return {**item, "publication_type": kind}
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="生成会议与期刊的正式发表审计结果")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--overrides", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    rows = json.loads(args.input.read_text(encoding="utf-8"))
    overrides = json.loads(args.overrides.read_text(encoding="utf-8"))
    output, included, pending = [], [], []
    for original in rows:
        row = dict(original)
        key = normalise_title(row.get("title", ""))
        override = overrides.get(key)
        evidence = trusted_evidence(row)
        if override:
            row.update(override)
        if override and override.get("publication_type"):
            row["formal_status"] = "confirmed_official"
            row["decision"] = "include"
            row["acceptance_confirmed"] = "yes"
        elif row.get("status") == "verified_conference":
            row["publication_type"] = "conference"
            row["formal_status"] = "confirmed_metadata"
            row["decision"] = "include"
            row["acceptance_confirmed"] = "yes"
        elif evidence:
            row["publication_type"] = evidence["publication_type"]
            row["formal_status"] = "confirmed_metadata"
            row["decision"] = "include"
            row["acceptance_confirmed"] = "yes"
            row["metadata_source"] = evidence["provider"]
            row["metadata_url"] = evidence.get("url", "")
            row["source"] = evidence.get("source", "")
        else:
            row["publication_type"] = ""
            row["formal_status"] = "needs_official_confirmation"
            row["decision"] = ""
            row["acceptance_confirmed"] = ""
            row["notes"] = (row.get("notes", "") + " 未取得可纳入的正式发表证据；保留待复核。").strip()
        output.append(row)
        (included if row["decision"] == "include" else pending).append(row)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_json(args.output_dir / "formal-publication-audit.json", output)
    write_review_csv(args.output_dir / "formal-publication-audit.csv", output)
    write_json(args.output_dir / "confirmed-publications.json", included)
    write_review_csv(args.output_dir / "confirmed-publications.csv", included)
    write_json(args.output_dir / "needs-official-confirmation.json", pending)
    print(f"已审计 {len(output)} 篇：确认正式发表 {len(included)} 篇，待官方确认 {len(pending)} 篇。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
