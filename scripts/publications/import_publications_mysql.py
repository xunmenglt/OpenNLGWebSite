#!/usr/bin/env python3
"""Import a reviewed publication manifest into a local OpenNLG MySQL database.

This intentionally supports only a named ``mysql_config_editor`` login path so
database credentials never need to appear in a command line, source file, or
run artifact.  It is idempotent by normalized title plus declared aliases.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from import_publications import input_records, to_payload, valid_record
from publication_lib import normalise_title, write_json


REQUIRED_COLUMNS = {
    "reserarch_id",
    "reserarch_title",
    "reserarch_source",
    "reserarch_author",
    "publication_year",
    "publication_type",
    "venue_short_name",
    "pdf_url",
    "doi_url",
    "outside_url",
}


def quote(value: object | None) -> str:
    if value is None:
        return "NULL"
    text = str(value)
    return "'" + text.replace("\\", "\\\\").replace("'", "''") + "'"


def mysql(args: argparse.Namespace, sql: str) -> str:
    command = [
        "mysql",
        f"--login-path={args.login_path}",
        "--database",
        args.database,
        "--batch",
        "--raw",
        "--skip-column-names",
    ]
    result = subprocess.run(command, input=sql, text=True, capture_output=True, check=False)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "mysql command failed")
    return result.stdout


def load_existing(args: argparse.Namespace) -> tuple[dict[str, int], set[str]]:
    columns = {
        line.split("\t", 1)[0]
        for line in mysql(args, "SHOW COLUMNS FROM og_reserarch;\n").splitlines()
        if line
    }
    missing = REQUIRED_COLUMNS - columns
    if missing:
        raise RuntimeError("og_reserarch schema is incomplete: " + ", ".join(sorted(missing)))
    rows = mysql(args, "SELECT reserarch_id, reserarch_title FROM og_reserarch;\n")
    return {
        normalise_title(title): int(identifier)
        for line in rows.splitlines()
        if (parts := line.split("\t", 1)) and len(parts) == 2
        for identifier, title in [parts]
    }, columns


def statements(records: list[dict], existing: dict[str, int]) -> tuple[list[str], list[dict], list[dict]]:
    sql, creates, updates = [], [], []
    for record in records:
        payload = to_payload(record)
        keys = [normalise_title(record.get("title", ""))]
        keys.extend(normalise_title(alias) for alias in record.get("aliases", []) or [])
        matched = next((existing[key] for key in keys if key in existing), None)
        if matched is None:
            creates.append(payload)
            sql.append(
                "INSERT INTO og_reserarch "
                "(reserarch_title, reserarch_source, reserarch_author, publication_year, publication_type, "
                "venue_short_name, pdf_url, doi_url, outside_url, is_new, create_time, update_time) VALUES "
                f"({quote(payload['reserarchTitle'])}, {quote(payload['reserarchSource'])}, "
                f"{quote(payload['reserarchAuthor'])}, {int(payload['publicationYear'])}, "
                f"{quote(payload['publicationType'])}, {quote(payload['venueShortName'])}, "
                f"{quote(payload['pdfUrl'])}, {quote(payload['doiUrl'])}, {quote(payload['outsideUrl'])}, "
                "1, NOW(), NOW());"
            )
        else:
            updates.append({"reserarchId": matched, **payload})
            sql.append(
                "UPDATE og_reserarch SET "
                f"reserarch_title={quote(payload['reserarchTitle'])}, "
                f"reserarch_source={quote(payload['reserarchSource'])}, "
                f"reserarch_author={quote(payload['reserarchAuthor'])}, "
                f"publication_year={int(payload['publicationYear'])}, "
                f"publication_type={quote(payload['publicationType'])}, "
                f"venue_short_name={quote(payload['venueShortName'])}, "
                f"pdf_url={quote(payload['pdfUrl'])}, doi_url={quote(payload['doiUrl'])}, "
                f"outside_url={quote(payload['outsideUrl'])}, is_new=1, update_time=NOW() "
                f"WHERE reserarch_id={matched};"
            )
    return sql, creates, updates


def main() -> int:
    parser = argparse.ArgumentParser(description="Import reviewed publications into local MySQL")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--login-path", default="opennlg-dev")
    parser.add_argument("--database", default="opennlg")
    parser.add_argument("--apply", action="store_true", help="write changes; default is dry-run")
    args = parser.parse_args()

    records, skipped = [], []
    for record in input_records(args.input):
        ok, reason = valid_record(record)
        if ok:
            records.append(record)
        else:
            skipped.append({"title": record.get("title", ""), "reason": reason})
    existing, _ = load_existing(args)
    sql, creates, updates = statements(records, existing)
    result = {
        "mode": "apply" if args.apply else "dry-run",
        "approved_count": len(records),
        "creates": creates,
        "updates": updates,
        "skipped": skipped,
    }
    if args.apply:
        mysql(args, "START TRANSACTION;\n" + "\n".join(sql) + "\nCOMMIT;\n")
    write_json(args.output, result)
    print(f"{'已导入' if args.apply else '预览'}：新增 {len(creates)} 条，更新 {len(updates)} 条，跳过 {len(skipped)} 条。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
