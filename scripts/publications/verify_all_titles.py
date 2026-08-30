#!/usr/bin/env python3
"""Re-extract every recent Scholar title and independently verify its conference venue.

The input is a locally saved Scholar HTML/MHTML snapshot. Each title is queried against
DBLP and Crossref; the script never contacts Google Scholar or the OpenNLG database.
"""

from __future__ import annotations

import argparse
import json
import time
from datetime import date
from pathlib import Path
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen

from enrich_publications import enrich_crossref, enrich_dblp
from extract_scholar import conference_year, parse_profile
from publication_lib import (
    author_sequence_complete,
    clean_authors,
    classify_venue,
    clean_text,
    load_venues,
    venue_label,
    write_json,
    write_review_csv,
)

OPENALEX_USER_AGENT = "OpenNLG-publication-import/1.0 (metadata verification)"
SEMANTIC_SCHOLAR_USER_AGENT = "OpenNLG-publication-import/1.0 (open PDF lookup)"


def evidence_from_provider(provider_name: str, record: dict) -> dict:
    provider = enrich_dblp if provider_name == "DBLP" else enrich_crossref
    result = provider(record)
    return {
        "provider": provider_name,
        "authors": clean_text(result.get("authors", "")) if result else "",
        "source": clean_text(result.get("source", "")) if result else "",
        "url": result.get("metadata_url", "") if result else "",
        "pdf_url": result.get("pdf_url", "") if result else "",
        "matched": bool(result),
    }


def evidence_from_openalex(record: dict) -> dict:
    """Second title search: obtain an OA PDF when an exact OpenAlex record exists."""
    from difflib import SequenceMatcher
    from publication_lib import normalise_title

    query = urlencode({"search": record["title"], "per-page": 5})
    request = Request(
        f"https://api.openalex.org/works?{query}",
        headers={"User-Agent": OPENALEX_USER_AGENT, "Accept": "application/json"},
    )
    with urlopen(request, timeout=25) as response:  # nosec B310: fixed public metadata endpoint
        payload = json.loads(response.read().decode("utf-8"))
    best = None
    for item in payload.get("results", []):
        score = SequenceMatcher(None, normalise_title(record["title"]), normalise_title(item.get("display_name", ""))).ratio()
        if best is None or score > best[0]:
            best = (score, item)
    if not best or best[0] < 0.92:
        return {"provider": "OpenAlex", "matched": False, "source": "", "authors": "", "url": "", "pdf_url": ""}
    _, item = best
    primary_location = item.get("primary_location") or {}
    source = ((primary_location.get("source") or {}).get("display_name")) or ""
    authors = ", ".join(
        clean_text((entry.get("author") or {}).get("display_name", ""))
        for entry in item.get("authorships", [])
        if clean_text((entry.get("author") or {}).get("display_name", ""))
    )
    locations = [item.get("best_oa_location") or {}] + list(item.get("locations") or [])
    pdf_url = next((location.get("pdf_url", "") for location in locations if location.get("pdf_url")), "")
    return {
        "provider": "OpenAlex",
        "matched": True,
        "source": clean_text(source),
        "authors": authors,
        "url": primary_location.get("landing_page_url") or item.get("doi") or item.get("id", ""),
        "pdf_url": pdf_url,
    }


def evidence_from_semantic_scholar(record: dict) -> dict:
    """Third title search for an open-access PDF; it never confirms conference status."""
    from difflib import SequenceMatcher
    from publication_lib import normalise_title

    query = urlencode(
        {
            "query": record["title"],
            "limit": 5,
            "fields": "title,venue,authors,openAccessPdf,url,externalIds",
        }
    )
    request = Request(
        f"https://api.semanticscholar.org/graph/v1/paper/search?{query}",
        headers={"User-Agent": SEMANTIC_SCHOLAR_USER_AGENT, "Accept": "application/json"},
    )
    with urlopen(request, timeout=25) as response:  # nosec B310: fixed public metadata endpoint
        payload = json.loads(response.read().decode("utf-8"))
    best = None
    for item in payload.get("data", []):
        score = SequenceMatcher(None, normalise_title(record["title"]), normalise_title(item.get("title", ""))).ratio()
        if best is None or score > best[0]:
            best = (score, item)
    if not best or best[0] < 0.92:
        return {"provider": "Semantic Scholar", "matched": False, "source": "", "authors": "", "url": "", "pdf_url": ""}
    _, item = best
    authors = ", ".join(clean_text(author.get("name", "")) for author in item.get("authors", []) if clean_text(author.get("name", "")))
    arxiv_id = (item.get("externalIds") or {}).get("ArXiv", "")
    pdf_url = (item.get("openAccessPdf") or {}).get("url", "")
    if not pdf_url and arxiv_id:
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
    return {
        "provider": "Semantic Scholar",
        "matched": True,
        "source": clean_text(item.get("venue", "")),
        "authors": authors,
        "url": item.get("url", ""),
        "pdf_url": pdf_url,
    }


def choose_conference_evidence(evidence: list[dict], venues: list[dict]) -> tuple[dict | None, str | None]:
    """Return a metadata record whose venue independently matches the allowlist."""
    for item in evidence:
        if item.get("provider") not in {"DBLP", "Crossref"}:
            continue
        short_name = classify_venue(item.get("source", ""), venues)
        if item.get("matched") and short_name:
            return item, short_name
    return None, None


def is_verified_in_range(record: dict, from_year: int, to_year: int) -> bool:
    return (
        record.get("status") == "verified_conference"
        and from_year <= int(record["publication_year"]) <= to_year
        and bool(record.get("venue_short_name"))
    )


def choose_pdf(evidence: list[dict], scholar_source: str) -> str:
    for item in evidence:
        pdf_url = item.get("pdf_url", "")
        if isinstance(pdf_url, str) and pdf_url.startswith(("https://", "http://")):
            return pdf_url
    import re

    arxiv_match = re.search(r"arXiv:(\d{4}\.\d{4,5})", scholar_source, flags=re.IGNORECASE)
    return f"https://arxiv.org/pdf/{arxiv_match.group(1)}" if arxiv_match else ""


def verify_record(record: dict[str, str], venues: list[dict], *, delay: float, cached: dict | None = None) -> dict:
    scholar_year = int(record["year"])
    scholar_short = classify_venue(record["source"], venues)
    evidence = []
    errors = []
    cached_evidence = {item.get("provider"): item for item in (cached or {}).get("evidence", [])}
    for provider_name in ("DBLP", "Crossref"):
        if provider_name in cached_evidence:
            evidence.append(cached_evidence[provider_name])
            continue
        try:
            evidence.append(evidence_from_provider(provider_name, record))
        except Exception as error:  # a failed public endpoint must not stop the audit
            errors.append(f"{provider_name}: {type(error).__name__}")
            evidence.append({"provider": provider_name, "matched": False, "source": "", "authors": "", "url": "", "pdf_url": ""})
        time.sleep(delay)
    for provider_name, provider in (("OpenAlex", evidence_from_openalex), ("Semantic Scholar", evidence_from_semantic_scholar)):
        if provider_name in cached_evidence:
            evidence.append(cached_evidence[provider_name])
            continue
        try:
            evidence.append(provider(record))
        except Exception as error:
            errors.append(f"{provider_name}: {type(error).__name__}")
            evidence.append({"provider": provider_name, "matched": False, "source": "", "authors": "", "url": "", "pdf_url": ""})
        time.sleep(delay)

    external, short_name = choose_conference_evidence(evidence, venues)
    if external and short_name:
        year = conference_year(external["source"], short_name, scholar_year)
        status = "verified_conference"
        notes = f"已由 {external['provider']} 的会议元数据独立核验。"
        # DBLP can append a numeric author-id suffix (for example “Li 0005”).
        # Crossref is preferred for author spelling while DBLP still provides
        # the independently verified conference venue.
        author_evidence = next(
            (item for item in evidence if item.get("provider") == "Crossref" and item.get("authors")),
            external,
        )
        authors = clean_authors(author_evidence.get("authors", "") or record["authors"])
        source = external["source"]
        metadata_source = external["provider"]
        metadata_url = external["url"]
        pdf_url = external["pdf_url"]
    else:
        short_name = scholar_short
        year = conference_year(record["source"], short_name, scholar_year) if short_name else scholar_year
        status = "needs_manual_review"
        notes = "未在 DBLP/Crossref 中得到匹配白名单会议的独立证据；请人工核验录取信息。"
        authors = clean_authors(record["authors"])
        source = record["source"]
        metadata_source = "Google Scholar (manual HTML export)"
        metadata_url = ""
        pdf_url = ""

    pdf_url = choose_pdf(evidence, record["source"]) or pdf_url
    secondary = next((item for item in evidence if item.get("provider") == "OpenAlex" and item.get("matched")), None)
    pdf_evidence = next((item for item in evidence if pdf_url and item.get("pdf_url") == pdf_url), None)

    if errors:
        notes += " 查询异常：" + "; ".join(errors)
    return {
        "decision": "",
        "acceptance_confirmed": "",
        "notes": notes,
        "title": record["title"],
        "publication_year": year,
        "venue_short_name": short_name or "",
        "venue_label": venue_label(short_name, year) if short_name else "",
        "authors": authors,
        "source": source,
        "detail_url": urljoin("https://scholar.google.com", record["href"]),
        "metadata_source": metadata_source,
        "metadata_url": metadata_url,
        "pdf_url": pdf_url,
        "status": status,
        "scholar_year": scholar_year,
        "scholar_source": record["source"],
        "authors_complete": author_sequence_complete(authors),
        "pdf_status": "found" if pdf_url else "missing",
        "secondary_metadata_source": "OpenAlex" if secondary else "",
        "secondary_metadata_url": secondary.get("url", "") if secondary else "",
        "pdf_metadata_source": pdf_evidence.get("provider", "") if pdf_evidence else "",
        "evidence": evidence,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="重新提取并复核 Scholar 快照中所有近期论文的会议信息")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--from-year", type=int, default=2025)
    parser.add_argument("--to-year", type=int, default=date.today().year)
    parser.add_argument("--venues", type=Path, default=Path(__file__).with_name("venues.json"))
    parser.add_argument("--reuse-from", type=Path, help="复用此前 verification-results.json 中的 DBLP/Crossref 证据")
    parser.add_argument("--rate-seconds", type=float, default=1.0)
    args = parser.parse_args()
    if args.from_year > args.to_year:
        parser.error("from-year 不能大于 to-year")

    raw = []
    for item in parse_profile(args.input):
        try:
            scholar_year = int(item["year"])
        except ValueError:
            continue
        if args.from_year <= scholar_year <= args.to_year:
            raw.append(item)
    if not raw:
        parser.error("未在快照中找到指定年份范围内的论文")

    venues = load_venues(args.venues)
    cached_by_title = {}
    if args.reuse_from:
        cached_rows = json.loads(args.reuse_from.read_text(encoding="utf-8"))
        cached_by_title = {item.get("title", "").strip().lower(): item for item in cached_rows}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_json(args.output_dir / "all-recent-titles.json", raw)
    results = []
    for index, item in enumerate(raw, start=1):
        print(f"[{index}/{len(raw)}] {item['title']}", flush=True)
        results.append(
            verify_record(
                item,
                venues,
                delay=args.rate_seconds,
                cached=cached_by_title.get(item["title"].strip().lower()),
            )
        )
    write_json(args.output_dir / "verification-results.json", results)
    write_review_csv(args.output_dir / "review-all.csv", results)
    verified_records = [item for item in results if is_verified_in_range(item, args.from_year, args.to_year)]
    final_records = [
        {**item, "decision": "include", "acceptance_confirmed": "yes"}
        for item in verified_records
        if item.get("pdf_url")
    ]
    missing_pdf = [item for item in verified_records if not item.get("pdf_url")]
    write_json(args.output_dir / "verified-conferences.json", final_records)
    write_review_csv(args.output_dir / "verified-conferences.csv", final_records)
    write_json(args.output_dir / "verified-missing-pdf.json", missing_pdf)
    print(
        f"已复核 {len(results)} 篇：独立确认会议 {len(verified_records)} 篇；"
        f"含 PDF 的最终记录 {len(final_records)} 篇；缺 PDF {len(missing_pdf)} 篇。"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
