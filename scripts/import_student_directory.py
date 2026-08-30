#!/usr/bin/env python3
"""Import OpenNLG student roster from the approved Excel workbook.

The script is deliberately deterministic: it writes a source-normalised report,
backs up the affected local tables, and only mutates MySQL with --apply.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import openpyxl


NAME_MAP = {
    "王继凯": "王纪凯",
    "施新宇": "施欣宇",
    "周楚粤": "周楚越",
}
SECTION_CATEGORY = {"博士生": "phd", "硕士生": "graduate_student", "毕业生": "graduate"}
SECTION_DEGREE = {"博士生": "phd", "硕士生": "master", "毕业生": None}
TEACHER_ONLY_NAMES = {"梁小波"}


def sql_quote(value: object | None) -> str:
    if value is None:
        return "NULL"
    return "'" + str(value).replace("\\", "\\\\").replace("'", "''") + "'"


def mysql(login_path: str, database: str, sql: str) -> str:
    result = subprocess.run(
        ["mysql", f"--login-path={login_path}", "--database", database, "--batch", "--raw", "--skip-column-names"],
        input=sql,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "mysql failed")
    return result.stdout


def normalized_name(value: object | None) -> str:
    return re.sub(r"\s+", "", str(value or "").strip())


def parse_grade(label: str) -> tuple[int, str | None]:
    match = re.match(r"^(\d{4})(?:级)?(.*)$", label)
    if not match:
        raise ValueError(f"无法解析年级：{label}")
    suffix = match.group(2).strip() or None
    return int(match.group(1)), suffix


def parse_workbook(path: Path) -> list[dict]:
    worksheet = openpyxl.load_workbook(path, data_only=True).active
    section = None
    rows: list[dict] = []
    for row_number, source_row in enumerate(worksheet.iter_rows(values_only=True), 1):
        values = [str(value).strip() if value is not None else "" for value in source_row]
        if values[0] in SECTION_CATEGORY and not any(values[1:]):
            section = values[0]
            continue
        if not section or not values[0] or values[0] == "学历":
            continue
        raw_name = normalized_name(values[1])
        if not raw_name:
            raise ValueError(f"第 {row_number} 行缺少姓名")
        canonical_name = NAME_MAP.get(raw_name, raw_name)
        cohort_year, program_type = parse_grade(values[2])
        degree_type = SECTION_DEGREE[section] or {"本科": "bachelor", "硕士": "master", "博士": "phd"}.get(values[0])
        if not degree_type:
            raise ValueError(f"第 {row_number} 行学历无法识别：{values[0]}")
        destination = values[3] or None
        rows.append(
            {
                "source_row": row_number,
                "section": section,
                "category": SECTION_CATEGORY[section],
                "degree_type": degree_type,
                "source_name": raw_name,
                "cn_name": canonical_name,
                "cohort_year": cohort_year,
                "cohort_label": values[2],
                "program_type": program_type,
                "destination": destination,
            }
        )
    return rows


def current_members(login_path: str, database: str) -> dict[str, dict]:
    output = mysql(login_path, database, "SELECT member_id, cn_name, ct_type, COALESCE(email, '') FROM og_members;")
    members: dict[str, dict] = {}
    for line in output.splitlines():
        member_id, name, category, email = line.split("\t")
        if email.startswith("local-avatar-demo-") and email.endswith("@invalid"):
            continue
        members[normalized_name(name)] = {"member_id": int(member_id), "ct_type": category, "cn_name": name}
    return members


def category_for(row: dict) -> str:
    return row["category"]


def member_description(row: dict) -> str | None:
    if row["section"] != "毕业生":
        return None
    degree_label = {"bachelor": "本科", "master": "硕士", "phd": "博士"}[row["degree_type"]]
    return f"{row['cohort_year']}级{degree_label}"


def sql_for(rows: list[dict], existing: dict[str, dict]) -> tuple[str, dict]:
    by_name: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_name[row["cn_name"]].append(row)
    if any(len(items) > 1 for items in by_name.values()):
        duplicated = [name for name, items in by_name.items() if len(items) > 1]
        raise ValueError(f"Excel 中出现重复规范姓名：{duplicated}")

    for name in TEACHER_ONLY_NAMES.intersection(by_name):
        member = existing.get(name)
        if not member or member["ct_type"] != "teacher":
            raise ValueError(f"仅教师成员不存在或主分类不是 teacher：{name}")

    alumni_names = {
        row["cn_name"]
        for row in rows
        if row["section"] == "毕业生" and row["cn_name"] not in TEACHER_ONLY_NAMES
    }
    statements = ["START TRANSACTION;"]
    statements.append("DELETE FROM og_members WHERE email LIKE 'local-avatar-demo-%@invalid';")

    for name in sorted(TEACHER_ONLY_NAMES.intersection(by_name)):
        statements.append(
            "DELETE rel FROM og_member_category_rel rel JOIN og_members m ON m.member_id = rel.member_id "
            f"WHERE m.cn_name = {sql_quote(name)} AND rel.ct_type <> 'teacher';"
        )
        statements.append(
            "DELETE edu FROM og_member_education edu JOIN og_members m ON m.member_id = edu.member_id "
            f"WHERE m.cn_name = {sql_quote(name)};"
        )

    for name in sorted(alumni_names):
        statements.append(f"UPDATE og_members SET ct_type = 'graduate' WHERE cn_name = {sql_quote(name)};")
        statements.append(
            "DELETE rel FROM og_member_category_rel rel JOIN og_members m ON m.member_id = rel.member_id "
            f"WHERE m.cn_name = {sql_quote(name)} AND rel.ct_type = 'graduate_student';"
        )

    for row in rows:
        name = row["cn_name"]
        if name in TEACHER_ONLY_NAMES:
            continue
        if name not in existing:
            statements.append(
                "INSERT INTO og_members (cn_name, en_name, member_desc, serial_num, ct_type) "
                f"SELECT {sql_quote(name)}, NULL, NULL, 0, {sql_quote(category_for(row))} "
                f"WHERE NOT EXISTS (SELECT 1 FROM og_members WHERE cn_name = {sql_quote(name)});"
            )
        if row["section"] == "毕业生":
            statements.append(
                f"UPDATE og_members SET member_desc = {sql_quote(member_description(row))} WHERE cn_name = {sql_quote(name)};"
            )

        statements.append(
            "INSERT INTO og_member_category_rel (member_id, ct_type, is_primary, is_visible, serial_num) "
            f"SELECT member_id, {sql_quote(category_for(row))}, "
            f"IF(ct_type = {sql_quote(category_for(row))}, 1, 0), 1, serial_num FROM og_members "
            f"WHERE cn_name = {sql_quote(name)} "
            "ON DUPLICATE KEY UPDATE is_visible = VALUES(is_visible), serial_num = VALUES(serial_num);"
        )

        destination = row["destination"] if row["section"] in {"博士生", "毕业生"} else None
        note = None
        statements.append(
            "INSERT INTO og_member_education "
            "(member_id, degree_type, cohort_year, cohort_label, program_type, graduation_destination, education_note, source_name, source_row, display_order) "
            f"SELECT member_id, {sql_quote(row['degree_type'])}, {row['cohort_year']}, {sql_quote(row['cohort_label'])}, "
            f"{sql_quote(row['program_type'])}, {sql_quote(destination)}, {sql_quote(note)}, '学生数据.xlsx', {row['source_row']}, {row['source_row']} "
            f"FROM og_members WHERE cn_name = {sql_quote(name)} "
            "ON DUPLICATE KEY UPDATE cohort_label = VALUES(cohort_label), program_type = VALUES(program_type), "
            "graduation_destination = VALUES(graduation_destination), education_note = VALUES(education_note), "
            "source_name = VALUES(source_name), source_row = VALUES(source_row), display_order = VALUES(display_order);"
        )

    statements.append("COMMIT;")
    report = {
        "excel_rows": len(rows),
        "new_members": sorted(name for name in by_name if name not in existing),
        "existing_members": sorted(name for name in by_name if name in existing),
        "alumni_transitions": sorted(name for name in alumni_names if existing.get(name, {}).get("ct_type") == "graduate_student"),
        "name_mappings": NAME_MAP,
        "retained_unmatched_current_students": sorted(
            member["cn_name"]
            for name, member in existing.items()
            if member["ct_type"] == "graduate_student" and name not in by_name
        ),
        "teacher_only_members": sorted(TEACHER_ONLY_NAMES.intersection(by_name)),
    }
    return "\n".join(statements) + "\n", report


def backup(login_path: str, database: str, target: Path) -> None:
    result = subprocess.run(
        ["mysqldump", f"--login-path={login_path}", "--single-transaction", "--skip-comments", "--no-tablespaces", database,
         "og_members", "og_members_category", "og_member_category_rel", "og_member_education"],
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace"))
    target.write_bytes(result.stdout)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--xlsx", type=Path, default=Path("学生数据.xlsx"))
    parser.add_argument("--login-path", default="opennlg-dev")
    parser.add_argument("--database", default="opennlg")
    parser.add_argument("--run-dir", type=Path, default=None)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    run_dir = args.run_dir or Path("runs/students") / datetime.now().strftime("%Y-%m-%d-%H%M%S")
    run_dir.mkdir(parents=True, exist_ok=True)
    rows = parse_workbook(args.xlsx)
    existing = current_members(args.login_path, args.database)
    sql, report = sql_for(rows, existing)
    (run_dir / "normalized-students.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (run_dir / "match-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (run_dir / "import.sql").write_text(sql, encoding="utf-8")
    if args.apply:
        backup(args.login_path, args.database, run_dir / "members-before.sql")
        mysql(args.login_path, args.database, sql)
    (run_dir / "summary.json").write_text(
        json.dumps({"mode": "apply" if args.apply else "dry-run", **report}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"mode": "apply" if args.apply else "dry-run", "run_dir": str(run_dir), **report}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
