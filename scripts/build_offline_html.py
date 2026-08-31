#!/usr/bin/env python3
"""Create one self-contained, public OpenNLG website HTML file.

The script reads the public website data from the local MySQL database via the
existing ``opennlg-dev`` login-path, builds a special public-only Vue entry,
and embeds the resulting CSS, JavaScript, fonts, local assets and public image
URLs as data URIs.  It never changes database records or the normal web build.
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLIENT = ROOT / "pageclient"
DIST = CLIENT / "dist-offline"
DEFAULT_OUTPUT = ROOT / "exports" / "opennlg-public-offline.html"
HTTP_IMAGE = re.compile(r"https?://[^\"'\\\s)]+", re.I)


def run_mysql(sql: str) -> list[dict]:
    command = [
        "mysql", "--login-path=opennlg-dev", "opennlg", "--batch", "--raw",
        "--skip-column-names", "-e", sql,
    ]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError("无法读取本地数据库：\n" + result.stderr.strip())
    return [json.loads(line) for line in result.stdout.splitlines() if line.strip()]


def sql_json(name_values: list[tuple[str, str]]) -> str:
    pairs = ", ".join("'%s', %s" % pair for pair in name_values)
    return "JSON_OBJECT(" + pairs + ")"


def database_snapshot() -> dict:
    member_fields = [
        ("ctType", "mc.ct_type"), ("ctZhName", "mc.ct_zh_name"), ("sort", "mc.sort"),
        ("memberId", "m.member_id"), ("cnName", "m.cn_name"), ("enName", "m.en_name"),
        ("memberDesc", "m.member_desc"), ("profession", "m.profession"),
        ("direction", "m.direction"), ("email", "m.email"), ("serialNum", "mcr.serial_num"),
        ("avatarUrl", "m.avatar_url"), ("outsideUrl", "m.outside_url"), ("insideUrl", "m.inside_url"),
        ("createTime", "DATE_FORMAT(m.create_time, '%Y-%m-%d %H:%i:%s')"),
        ("updateTime", "DATE_FORMAT(m.update_time, '%Y-%m-%d %H:%i:%s')"),
        ("cohortYear", "me.cohort_year"), ("cohortLabel", "me.cohort_label"),
        ("programType", "me.program_type"), ("degreeType", "me.degree_type"),
        ("graduationDestination", "me.graduation_destination"),
    ]
    member_sql = f"""
      SELECT {sql_json(member_fields)}
      FROM og_members_category mc
      INNER JOIN og_member_category_rel mcr ON mcr.ct_type = mc.ct_type AND mcr.is_visible = 1
      INNER JOIN og_members m ON m.member_id = mcr.member_id
      LEFT JOIN og_member_education me ON me.member_id = m.member_id
        AND ((mcr.ct_type = 'phd' AND me.degree_type = 'phd')
          OR (mcr.ct_type = 'graduate_student' AND me.degree_type = 'master')
          OR (mcr.ct_type = 'graduate'))
      ORDER BY mc.sort ASC, me.cohort_year ASC, mcr.serial_num ASC, m.serial_num ASC
    """
    member_rows = run_mysql(member_sql)
    categories: dict[str, dict] = {}
    for row in member_rows:
        category = categories.setdefault(row["ctType"], {
            "ctType": row["ctType"], "ctZhName": row["ctZhName"], "sort": row["sort"], "children": []
        })
        category["children"].append({key: value for key, value in row.items() if key not in {"ctZhName", "sort"}})
    members = sorted(categories.values(), key=lambda item: (item["sort"] or 0, item["ctType"]))

    research_fields = [
        ("reserarchId", "reserarch_id"), ("reserarchTitle", "reserarch_title"),
        ("reserarchSource", "reserarch_source"), ("reserarchAuthor", "reserarch_author"),
        ("publicationYear", "publication_year"), ("publicationType", "publication_type"),
        ("researchDirection", "research_direction"), ("venueShortName", "venue_short_name"),
        ("pdfUrl", "pdf_url"), ("doiUrl", "doi_url"), ("codeUrl", "code_url"),
        ("projectUrl", "project_url"), ("reserarchCover", "reserarch_cover"), ("isNew", "is_new"),
        ("outsideUrl", "outside_url"), ("insideUrl", "inside_url"),
        ("createTime", "DATE_FORMAT(create_time, '%Y-%m-%d %H:%i:%s')"),
        ("updateTime", "DATE_FORMAT(update_time, '%Y-%m-%d %H:%i:%s')"),
    ]
    research = run_mysql(
        "SELECT %s FROM og_reserarch ORDER BY COALESCE(publication_year, YEAR(create_time)) DESC, is_new DESC, create_time DESC"
        % sql_json(research_fields)
    )
    news = run_mysql("SELECT %s FROM og_news ORDER BY is_new DESC, create_time DESC" % sql_json([
        ("newsId", "news_id"), ("newsTitle", "news_title"), ("newsSummary", "news_summary"),
        ("newsReadTimes", "news_read_times"), ("outsideUrl", "outside_url"), ("insideUrl", "inside_url"),
        ("createTime", "DATE_FORMAT(create_time, '%Y-%m-%d %H:%i:%s')"),
        ("updateTime", "DATE_FORMAT(update_time, '%Y-%m-%d %H:%i:%s')"), ("isNew", "is_new"),
    ]))
    culture = run_mysql("SELECT %s FROM og_team_culture ORDER BY create_time DESC" % sql_json([
        ("id", "id"), ("image", "image"), ("title", "title"), ("outsideUrl", "outside_url"),
        ("insideUrl", "inside_url"), ("createTime", "DATE_FORMAT(create_time, '%Y-%m-%d %H:%i:%s')"),
    ]))
    return {
        "generatedAt": dt.datetime.now(dt.timezone.utc).isoformat(),
        "members": members, "research": research, "news": news, "culture": culture,
        "researchOptions": {
            "directions": sorted({x["researchDirection"] for x in research if x.get("researchDirection")} ),
            "years": sorted({x["publicationYear"] or int(x["createTime"][:4]) for x in research if x.get("publicationYear") or x.get("createTime")}, reverse=True),
            "types": sorted({x["publicationType"] for x in research if x.get("publicationType")} ),
            "resources": sorted({x["reserarchSource"] for x in research if x.get("reserarchSource")} ),
            "venues": sorted({x["venueShortName"] for x in research if x.get("venueShortName")} ),
        },
    }


def data_uri(content: bytes, mime: str) -> str:
    return "data:%s;base64,%s" % (mime, base64.b64encode(content).decode("ascii"))


def download_image(url: str, warnings: list[str]) -> str:
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "OpenNLG offline exporter/1.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            content = response.read(15 * 1024 * 1024 + 1)
            mime = response.headers.get_content_type()
        if len(content) > 15 * 1024 * 1024 or not mime.startswith("image/"):
            raise ValueError("响应不是 15 MB 以内的图像")
        return data_uri(content, mime)
    except Exception as error:
        warnings.append("未能读取图像 %s：%s；已使用内嵌离线说明图" % (url, error))
        fallback = ("<svg xmlns='http://www.w3.org/2000/svg' width='960' height='540' "
                    "viewBox='0 0 960 540'><rect width='960' height='540' fill='#eaf1f9'/>"
                    "<path d='M0 400L240 190l145 126 115-92 460 176v140H0z' fill='#d6e1ee'/>"
                    "<text x='480' y='282' text-anchor='middle' fill='#43566b' font-family='sans-serif' "
                    "font-size='28'>Image unavailable in offline export</text></svg>")
        return "data:image/svg+xml;base64," + base64.b64encode(fallback.encode("utf-8")).decode("ascii")


def embed_snapshot_media(snapshot: dict, warnings: list[str]) -> None:
    cache: dict[str, str] = {}
    for group in snapshot["members"]:
        for member in group["children"]:
            url = member.get("avatarUrl")
            if url and url.startswith(("http://", "https://")):
                member["avatarUrl"] = cache.setdefault(url, download_image(url, warnings))
    for item in snapshot["culture"] + snapshot["research"]:
        key = "image" if "image" in item else "reserarchCover"
        url = item.get(key)
        if url and url.startswith(("http://", "https://")):
            item[key] = cache.setdefault(url, download_image(url, warnings))


def build_client() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    environment = dict(os.environ, OPENNLG_OFFLINE="1")
    command = ["npm", "run", "build", "--", "--dest", str(DIST)]
    result = subprocess.run(command, cwd=CLIENT, text=True, env=environment)
    if result.returncode:
        raise RuntimeError("离线前端构建失败。")


def local_assets() -> dict[str, str]:
    assets: dict[str, str] = {}
    for path in DIST.rglob("*"):
        if not path.is_file() or path.name == "index.html" or path.suffix.lower() in {".js", ".css", ".map"}:
            continue
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        assets[path.relative_to(DIST).as_posix()] = data_uri(path.read_bytes(), mime)
    return assets


def inline_build(snapshot: dict, output: Path, warnings: list[str]) -> None:
    html = (DIST / "index.html").read_text(encoding="utf-8")
    script_pattern = re.compile(r"<script(?P<attrs>[^>]*?)\s+src=\"(?P<src>[^\"]+)\"(?P<tail>[^>]*)></script>", re.I)
    # Vue CLI writes the two attributes in either order depending on its version.
    style_pattern = re.compile(r"<link[^>]+href=\"(?P<href>[^\"]+\.css(?:\?[^\"]*)?)\"[^>]*>", re.I)

    def file_text(reference: str) -> str:
        if reference.startswith(("http://", "https://", "//")):
            warnings.append("未内嵌第三方样式 %s（已移除；页面会使用本地字体回退）" % reference)
            return ""
        return (DIST / reference.lstrip("./")).read_text(encoding="utf-8")

    html = style_pattern.sub(lambda match: "<style>" + file_text(match.group("href")) + "</style>", html)
    # Remaining HTTP link tags are optional third-party font stylesheets.  The
    # build already embeds the local icon font; remove these so file:// mode
    # never needs a network request.
    def remove_external_link(match: re.Match) -> str:
        warnings.append("未内嵌第三方样式 %s（已移除；页面会使用本地字体回退）" % match.group("href"))
        return ""
    html = re.sub(r'<link[^>]+href="(?P<href>https?://[^\"]+)"[^>]*>', remove_external_link, html, flags=re.I)
    # The Vue CLI entry scripts are normally deferred in <head>.  An inline
    # script ignores ``defer`` and would run before ``#app`` in <body> exists,
    # leaving the offline site blank.  Preserve their order but place them
    # immediately before </body>, after the mount element has been parsed.
    inline_scripts: list[str] = []

    def inline_script(match: re.Match) -> str:
        inline_scripts.append("<script>" + file_text(match.group("src")) + "</script>")
        return ""

    html = script_pattern.sub(inline_script, html)
    snapshot_tag = "<script>window.__OPENNLG_OFFLINE_DATA__=" + json.dumps(snapshot, ensure_ascii=False, separators=(",", ":")) + ";</script>"
    # Vue's entry scripts are emitted in <head>.  Put the snapshot immediately
    # after the opening tag so api.js can read it during module initialization.
    html = html.replace("<head>", "<head>" + snapshot_tag, 1)

    if "</body>" not in html:
        raise RuntimeError("离线前端 HTML 缺少 </body>，无法注入应用脚本。")
    html = html.replace("</body>", "".join(inline_scripts) + "</body>", 1)

    # Apply asset replacement only after the application scripts are back in
    # the document: webpack stores image and font URLs inside those scripts.
    for reference, uri in local_assets().items():
        html = html.replace(reference, uri)

    # Home's four research illustrations are external literals in the source.
    # Only replace URLs that the server proves are image data; PDF/profile links remain links.
    external_urls = sorted(set(HTTP_IMAGE.findall(html)))
    for url in external_urls:
        if "baidu.com/it/" in url:
            replacement = download_image(url, warnings)
            if replacement != url:
                html = html.replace(url, replacement)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="single HTML output path")
    args = parser.parse_args()
    warnings: list[str] = []
    snapshot = database_snapshot()
    embed_snapshot_media(snapshot, warnings)
    build_client()
    inline_build(snapshot, args.output.resolve(), warnings)
    digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
    print("输出文件：%s" % args.output.resolve())
    print("体积：%.1f MiB" % (args.output.stat().st_size / 1024 / 1024))
    print("SHA-256：%s" % digest)
    print("快照数据：%d 个成员分类，%d 篇论文，%d 条消息，%d 组影像" % (
        len(snapshot["members"]), len(snapshot["research"]), len(snapshot["news"]), len(snapshot["culture"])))
    if warnings:
        print("警告（以下资源保留为外部链接）：", file=sys.stderr)
        print("\n".join("- " + message for message in warnings), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
