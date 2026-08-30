#!/usr/bin/env python3
"""Low-rate PDF backfill for independently confirmed conference papers only."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from verify_all_titles import choose_pdf, evidence_from_semantic_scholar, is_verified_in_range
from publication_lib import write_json, write_review_csv


def main() -> int:
    parser = argparse.ArgumentParser(description="为已确认会议论文补全开放 PDF，不重新判定会议归属")
    parser.add_argument("--input", required=True, type=Path, help="verification-results.json")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--from-year", type=int, default=2024)
    parser.add_argument("--to-year", type=int, default=2026)
    parser.add_argument("--rate-seconds", type=float, default=3.2, help="Semantic Scholar 请求间隔")
    args = parser.parse_args()
    rows = json.loads(args.input.read_text(encoding="utf-8"))
    targets = [row for row in rows if is_verified_in_range(row, args.from_year, args.to_year) and not row.get("pdf_url")]
    for index, row in enumerate(targets, start=1):
        print(f"[{index}/{len(targets)}] {row['title']}", flush=True)
        raw = {"title": row["title"], "source": row.get("scholar_source", "")}
        try:
            evidence = evidence_from_semantic_scholar(raw)
        except Exception as error:
            row["notes"] = row.get("notes", "") + f" PDF 检索失败：{type(error).__name__}。"
            time.sleep(args.rate_seconds)
            continue
        row["evidence"] = [item for item in row.get("evidence", []) if item.get("provider") != "Semantic Scholar"] + [evidence]
        pdf_url = choose_pdf(row["evidence"], row.get("scholar_source", ""))
        if pdf_url:
            row["pdf_url"] = pdf_url
            row["pdf_status"] = "found"
            row["pdf_metadata_source"] = "Semantic Scholar"
        time.sleep(args.rate_seconds)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    verified = [row for row in rows if is_verified_in_range(row, args.from_year, args.to_year)]
    final = [{**row, "decision": "include", "acceptance_confirmed": "yes"} for row in verified if row.get("pdf_url")]
    missing = [row for row in verified if not row.get("pdf_url")]
    write_json(args.output_dir / "verification-results.json", rows)
    write_review_csv(args.output_dir / "review-all.csv", rows)
    write_json(args.output_dir / "verified-conferences.json", final)
    write_review_csv(args.output_dir / "verified-conferences.csv", final)
    write_json(args.output_dir / "verified-missing-pdf.json", missing)
    print(f"PDF 回填完成：最终记录 {len(final)} 篇，仍缺 PDF {len(missing)} 篇。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
