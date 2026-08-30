#!/usr/bin/env python3
"""Synchronise OpenNLG's public website content into a local MySQL snapshot.

Only publicly readable display resources are included. Authentication, user
accounts, uploaded files, member records, and the independently curated
publication table are deliberately out of scope. Member data is now maintained
locally because it has grade and multi-category relations not available from
the production API.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen


TABLES = (
    "og_article",
    "og_news",
    "og_publication",
    "og_team_culture",
)


def quote(value: object | None) -> str:
    if value is None:
        return "NULL"
    text = str(value)
    return "'" + text.replace("\\", "\\\\").replace("'", "''") + "'"


def mysql(login_path: str, database: str, sql: str) -> str:
    result = subprocess.run(
        ["mysql", f"--login-path={login_path}", "--database", database, "--batch", "--raw", "--skip-column-names"],
        input=sql,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "mysql command failed")
    return result.stdout


def api_list(api_base: str, endpoint: str) -> list[dict]:
    query = urlencode({"currentPage": 1, "size": 200})
    with urlopen(f"{api_base.rstrip('/')}/{endpoint}?{query}", timeout=30) as response:  # nosec B310: explicit operator URL
        payload = json.loads(response.read().decode("utf-8"))
    if payload.get("code") != 200:
        raise RuntimeError(f"{endpoint}: API response code {payload.get('code')}")
    data = payload.get("data")
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        rows = data.get("data")
        if isinstance(rows, list):
            return rows
    raise RuntimeError(f"{endpoint}: unexpected list payload")


def fetch_snapshot(api_base: str) -> dict:
    return {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "source": api_base,
        "articles": api_list(api_base, "article/list"),
        "members": api_list(api_base, "members/list"),
        "member_categories": api_list(api_base, "members-category/list"),
        "news": api_list(api_base, "news/list"),
        "publications": api_list(api_base, "publication/list"),
        "team_culture": api_list(api_base, "team-culture/list"),
    }


def row_values(row: dict, fields: list[str]) -> str:
    return ", ".join(quote(row.get(field)) for field in fields)


def insert(table: str, columns: list[str], values: str) -> str:
    return f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({values});"


def sql_for(snapshot: dict) -> str:
    sql = ["START TRANSACTION;"]
    sql.extend(f"DELETE FROM {table};" for table in TABLES)

    for row in snapshot["articles"]:
        columns = ["id", "article_id", "article_title", "article_summary", "article_content", "article_read_times", "create_time"]
        values = row_values(row, ["id", "articleId", "articleTitle", "articleSummary", "articleContent", "articleReadTimes", "createTime"])
        sql.append(insert("og_article", columns, values))
    for row in snapshot["news"]:
        columns = ["news_id", "news_title", "news_summary", "news_read_times", "outside_url", "inside_url", "create_time", "is_new"]
        values = row_values(row, ["newsId", "newsTitle", "newsSummary", "newsReadTimes", "outsideUrl", "insideUrl", "createTime", "isNew"])
        sql.append(insert("og_news", columns, values))
    for row in snapshot["publications"]:
        columns = ["publication_id", "publication_title", "publication_desc", "publication_cover", "outside_url", "inside_url", "create_time", "update_time"]
        values = row_values(row, ["publicationId", "publicationTitle", "publicationDesc", "publicationCover", "outsideUrl", "insideUrl", "createTime", "updateTime"])
        sql.append(insert("og_publication", columns, values))
    for row in snapshot["team_culture"]:
        columns = ["id", "image", "title", "outside_url", "inside_url", "create_time"]
        values = row_values(row, ["id", "image", "title", "outsideUrl", "insideUrl", "createTime"])
        sql.append(insert("og_team_culture", columns, values))
    sql.append("COMMIT;")
    return "\n".join(sql) + "\n"


def local_backup_sql(login_path: str, database: str) -> str:
    result = subprocess.run(
        [
            "mysqldump",
            f"--login-path={login_path}",
            "--single-transaction",
            "--skip-comments",
            "--no-tablespaces",
            database,
            *TABLES,
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "mysqldump command failed")
    return result.stdout


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync OpenNLG public content to local MySQL")
    parser.add_argument("--api-base", default="https://opennlg.cn/api")
    parser.add_argument("--login-path", default="opennlg-dev")
    parser.add_argument("--database", default="opennlg")
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    snapshot = fetch_snapshot(args.api_base)
    backup_sql = local_backup_sql(args.login_path, args.database)
    write_json(args.run_dir / "remote-public-content.json", snapshot)
    (args.run_dir / "local-public-content-before.sql").write_text(backup_sql, encoding="utf-8")
    counts = {key: len(value) for key, value in snapshot.items() if isinstance(value, list)}
    if args.apply:
        mysql(args.login_path, args.database, sql_for(snapshot))
    write_json(args.run_dir / "summary.json", {"mode": "apply" if args.apply else "dry-run", "counts": counts, "target_tables": TABLES})
    print("同步" if args.apply else "预览", json.dumps(counts, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
