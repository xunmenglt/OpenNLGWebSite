#!/usr/bin/env python3
"""Repair DBLP numeric author-id suffixes in the local publication database."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

from enrich_publications import enrich_crossref
from publication_lib import clean_authors, write_json


def mysql(login_path: str, database: str, sql: str) -> str:
    result = subprocess.run(
        ["mysql", f"--login-path={login_path}", "--database", database, "--batch", "--raw", "--skip-column-names"],
        input=sql, text=True, capture_output=True, check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "mysql failed")
    return result.stdout


def quote(value: str) -> str:
    return "'" + value.replace("\\", "\\\\").replace("'", "''") + "'"


def backup(login_path: str, database: str, output: Path) -> None:
    result = subprocess.run(
        ["mysqldump", f"--login-path={login_path}", "--single-transaction", "--skip-comments", "--no-tablespaces", database, "og_reserarch"],
        capture_output=True, check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace"))
    output.write_bytes(result.stdout)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--login-path", default="opennlg-dev")
    parser.add_argument("--database", default="opennlg")
    parser.add_argument("--run-dir", type=Path, default=None)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    run_dir = args.run_dir or Path("runs/publications") / ("author-repair-" + datetime.now().strftime("%Y-%m-%d-%H%M%S"))
    run_dir.mkdir(parents=True, exist_ok=True)
    rows = mysql(args.login_path, args.database, "SELECT reserarch_id, reserarch_title, reserarch_source, reserarch_author FROM og_reserarch WHERE reserarch_author REGEXP '(^|, )[A-Za-z .-]+ 0[0-9]{3}(,|$)';")
    repairs, unresolved = [], []
    for line in rows.splitlines():
        identifier, title, source, before = line.split("\t", 3)
        try:
            crossref = enrich_crossref({"title": title, "source": source})
        except Exception as error:
            crossref = None
            error_text = type(error).__name__
        else:
            error_text = ""
        after = clean_authors((crossref or {}).get("authors", ""))
        provider = "Crossref"
        metadata_url = (crossref or {}).get("metadata_url", "")
        # A few records have no Crossref author list. Their DBLP name text is
        # still usable once the known zero-prefixed PID tail is stripped.
        if not after:
            after = clean_authors(before)
            provider = "DBLP suffix sanitization"
            metadata_url = ""
        if after and after != before and not re.search(r"(^|, )[A-Za-z .-]+ 0[0-9]{3}(,|$)", after):
            repairs.append({"reserarch_id": int(identifier), "title": title, "before": before, "after": after, "provider": provider, "metadata_url": metadata_url})
        else:
            unresolved.append({"reserarch_id": int(identifier), "title": title, "before": before, "reason": error_text or "Crossref 未提供可用作者序列"})
    report = {"mode": "apply" if args.apply else "dry-run", "repairs": repairs, "unresolved": unresolved}
    write_json(run_dir / "author-repair-report.json", report)
    if args.apply and unresolved:
        raise RuntimeError(f"仍有 {len(unresolved)} 篇无法由 Crossref 独立确认，未写入数据库")
    if args.apply:
        backup(args.login_path, args.database, run_dir / "og_reserarch-before.sql")
        statements = [f"UPDATE og_reserarch SET reserarch_author={quote(item['after'])}, update_time=NOW() WHERE reserarch_id={item['reserarch_id']};" for item in repairs]
        mysql(args.login_path, args.database, "START TRANSACTION;\n" + "\n".join(statements) + "\nCOMMIT;\n")
    print(json.dumps({"mode": report["mode"], "repaired": len(repairs), "unresolved": len(unresolved), "run_dir": str(run_dir)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
