#!/usr/bin/env python3
"""Validate reviewed records and optionally import them through OpenNLG's protected API."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from publication_lib import author_sequence_complete, clean_authors, clean_text, normalise_title, read_review_csv, write_json


def accepted(value: str) -> bool:
    return clean_text(value).lower() in {"yes", "y", "true", "1", "确认", "是", "已确认"}


def valid_record(record: dict) -> tuple[bool, str]:
    if record.get("decision") and clean_text(record.get("decision", "")).lower() != "include":
        return False, "未标记为 include"
    if record.get("acceptance_confirmed") and not accepted(record.get("acceptance_confirmed", "")):
        return False, "未确认已录取/正式会议论文"
    if not clean_text(record.get("title", "")) or not clean_text(record.get("source", "")):
        return False, "标题或来源为空"
    year = str(record.get("publication_year", ""))
    if not clean_text(record.get("venue_short_name", "")) or not year.isdigit():
        return False, "会议简称或年份无效"
    if not author_sequence_complete(record.get("authors", "")):
        return False, "作者序列为空或仍被截断"
    return True, ""


def request_json(url: str, *, token: str | None = None, payload: dict | None = None) -> dict:
    headers = {"Accept": "application/json"}
    data = None
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = Request(url, data=data, headers=headers, method="POST" if payload is not None else "GET")
    with urlopen(request, timeout=30) as response:  # nosec B310: API base is an explicit operator argument
        return json.loads(response.read().decode("utf-8"))


def existing_records(api_base: str) -> list[dict]:
    existing: list[dict] = []
    page = 1
    while True:
        query = urlencode({"currentPage": page, "size": 100})
        payload = request_json(f"{api_base.rstrip('/')}/reserarch/list?{query}")
        page_data = payload.get("data", {}) if isinstance(payload, dict) else {}
        rows = page_data.get("data", []) if isinstance(page_data, dict) else []
        for row in rows:
            existing.append(row)
        if not rows or page * 100 >= int(page_data.get("total", 0)):
            return existing
        page += 1


def to_payload(record: dict) -> dict:
    return {
        "reserarchTitle": clean_text(record["title"]),
        "reserarchAuthor": clean_authors(record["authors"]),
        "reserarchSource": clean_text(record["source"]),
        "publicationYear": int(record["publication_year"]),
        "publicationType": clean_text(record.get("publication_type", "conference")),
        "venueShortName": clean_text(record["venue_short_name"]),
        "pdfUrl": clean_text(record.get("pdf_url", "")),
        "doiUrl": clean_text(record.get("doi_url", "")),
        "outsideUrl": clean_text(record.get("outside_url") or record.get("metadata_url") or record.get("detail_url", "")),
    }


def input_records(path: Path) -> list[dict]:
    if path.suffix.lower() == ".json":
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, list):
            raise ValueError("JSON 导入清单必须是数组")
        return value
    return read_review_csv(path)


def matching_existing(record: dict, existing: list[dict]) -> tuple[dict | None, str]:
    candidates = [record.get("title", "")] + list(record.get("aliases", []) or [])
    keys = {normalise_title(title) for title in candidates if title}
    matches = [row for row in existing if normalise_title(row.get("reserarchTitle", "")) in keys]
    if len(matches) == 1:
        return matches[0], "标题或受控别名匹配"
    if len(matches) > 1:
        return None, "多个历史记录匹配，拒绝自动更新"
    return None, ""


def main() -> int:
    parser = argparse.ArgumentParser(description="验证论文复核清单；仅在 --apply 时写入 OpenNLG 数据库")
    parser.add_argument("--input", required=True, type=Path, help="JSON 数据清单或人工复核后的 review.csv")
    parser.add_argument("--output", required=True, type=Path, help="import-preview.json 或 import-result.json")
    parser.add_argument("--apply", action="store_true", help="实际调用 /reserarch/create；默认只生成预览")
    parser.add_argument("--api-base", default=os.environ.get("OPENNLG_API_BASE", ""), help="例如 https://opennlg.cn/api")
    parser.add_argument("--token-env", default="OPENNLG_API_TOKEN", help="保存 JWT 的环境变量名")
    args = parser.parse_args()

    approved, skipped = [], []
    for row in input_records(args.input):
        ok, reason = valid_record(row)
        if ok:
            approved.append(row)
        else:
            skipped.append({"title": row.get("title", ""), "reason": reason})
    preview = {"mode": "apply" if args.apply else "dry-run", "approved": [to_payload(row) for row in approved], "skipped": skipped}
    if not args.apply:
        if args.api_base:
            existing = existing_records(args.api_base)
            creates, updates = [], []
            for row in approved:
                payload = to_payload(row)
                previous, reason = matching_existing(row, existing)
                if previous:
                    updates.append({"reserarchId": previous.get("reserarchId"), "reason": reason, "before": previous, "after": payload})
                else:
                    creates.append(payload)
            preview.update({"creates": creates, "updates": updates, "existing_count": len(existing)})
            print(f"dry-run：新增 {len(creates)} 条，更新 {len(updates)} 条，跳过 {len(skipped)} 条。")
        else:
            print(f"dry-run：可导入 {len(approved)} 条，跳过 {len(skipped)} 条。")
        write_json(args.output, preview)
        return 0

    if not args.api_base:
        parser.error("--apply 时必须提供 --api-base 或 OPENNLG_API_BASE")
    token = os.environ.get(args.token_env)
    if not token:
        parser.error(f"--apply 时必须设置环境变量 {args.token_env}")
    existing = existing_records(args.api_base)
    created, updated, duplicates, failures = [], [], [], []
    for row in approved:
        payload = to_payload(row)
        previous, reason = matching_existing(row, existing)
        if previous:
            update_payload = {**payload, "reserarchId": previous.get("reserarchId")}
            try:
                response = request_json(f"{args.api_base.rstrip('/')}/reserarch/update", token=token, payload=update_payload)
                if response.get("code") == 200:
                    updated.append({"reserarchId": previous.get("reserarchId"), "title": payload["reserarchTitle"], "reason": reason})
                else:
                    failures.append({"title": payload["reserarchTitle"], "response": response})
            except Exception as error:
                failures.append({"title": payload["reserarchTitle"], "error": f"{type(error).__name__}: {error}"})
            continue
        try:
            response = request_json(f"{args.api_base.rstrip('/')}/reserarch/create", token=token, payload=payload)
            if response.get("code") == 200:
                created.append(payload)
                existing.append({"reserarchTitle": payload["reserarchTitle"], "reserarchId": None})
            else:
                failures.append({"title": payload["reserarchTitle"], "response": response})
        except Exception as error:
            failures.append({"title": payload["reserarchTitle"], "error": f"{type(error).__name__}: {error}"})
    write_json(args.output, {**preview, "created": created, "updated": updated, "duplicates": duplicates, "failures": failures})
    print(f"已创建 {len(created)} 条，更新 {len(updated)} 条，重复 {len(duplicates)} 条，失败 {len(failures)} 条。")
    return 0 if not failures else 2


if __name__ == "__main__":
    raise SystemExit(main())
