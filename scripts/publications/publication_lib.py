"""Shared helpers for the publication-import workflow. Uses only Python's standard library."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any, Iterable, Optional


REVIEW_COLUMNS = [
    "decision", "acceptance_confirmed", "notes", "title", "publication_year",
    "venue_short_name", "venue_label", "authors", "source", "detail_url",
    "metadata_source", "metadata_url", "pdf_url", "status",
]


def clean_text(value: str) -> str:
    return " ".join((value or "").replace("\xa0", " ").split())


def clean_authors(value: str) -> str:
    """Remove DBLP's erroneous zero-prefixed author-id suffixes.

    Some DBLP search responses append a local author identifier such as ``0005``
    to the displayed name. These suffixes are not part of the author sequence.
    """
    text = clean_text(value)
    return re.sub(r"(?<=\S)\s+0\d{3}(?=\s*(?:,|$))", "", text)


def normalise_title(value: str) -> str:
    value = clean_text(value).lower()
    return re.sub(r"[^a-z0-9]+", "", value)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def load_venues(path: Path) -> list[dict[str, Any]]:
    data = load_json(path)
    venues = data.get("venues", [])
    if not isinstance(venues, list):
        raise ValueError("venues.json 的 venues 必须是数组")
    for venue in venues:
        if not venue.get("short_name") or not venue.get("patterns"):
            raise ValueError("每个会议必须提供 short_name 与 patterns")
    return venues


def classify_venue(source: str, venues: Iterable[dict[str, Any]]) -> Optional[str]:
    source = clean_text(source)
    for venue in venues:
        for pattern in venue["patterns"]:
            if re.search(pattern, source, flags=re.IGNORECASE):
                return venue["short_name"]
    return None


def venue_label(short_name: str, year: int) -> str:
    return f"{short_name}{year}"


def author_sequence_complete(authors: str) -> bool:
    text = clean_text(authors)
    return bool(text) and "…" not in text and "..." not in text


def write_review_csv(path: Path, records: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REVIEW_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for record in records:
            writer.writerow({key: record.get(key, "") for key in REVIEW_COLUMNS})


def read_review_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))
