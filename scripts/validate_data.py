#!/usr/bin/env python3
"""Validate data/hackathons.json schema and print a concise status summary."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "hackathons.json"

REQUIRED_EVENT_FIELDS = {
    "id",
    "name",
    "region",
    "format",
    "category",
    "url",
    "event_dates",
    "registration_window",
    "registration_status",
    "eligibility",
    "hardware_or_stack",
    "prize_pool",
    "last_verified",
    "notes",
}

ALLOWED_REGIONS = {"China", "North America", "Europe", "Global"}
ALLOWED_FORMATS = {"in-person", "online", "hybrid"}
ALLOWED_STATUSES = {"open", "opening_soon", "closed", "interest_only", "ended", "unverified"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_RE = re.compile(r"^[a-z0-9-]+$")


def validate() -> int:
    if not DATA_PATH.exists():
        print(f"ERROR: Missing {DATA_PATH}", file=sys.stderr)
        return 1

    try:
        payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"ERROR: Invalid JSON in {DATA_PATH}: {exc}", file=sys.stderr)
        return 1

    errors: list[str] = []

    last_updated = payload.get("last_updated", "")
    if not DATE_RE.match(str(last_updated)):
        errors.append(f"Top-level 'last_updated' must be YYYY-MM-DD, got {last_updated!r}")

    events = payload.get("events")
    if not isinstance(events, list) or not events:
        errors.append("Top-level 'events' must be a non-empty list")
        events = []

    seen_ids: set[str] = set()
    status_counts: dict[str, int] = {}

    for idx, event in enumerate(events):
        prefix = f"events[{idx}]"
        if not isinstance(event, dict):
            errors.append(f"{prefix}: expected object")
            continue

        missing = REQUIRED_EVENT_FIELDS - set(event.keys())
        if missing:
            errors.append(f"{prefix} ({event.get('id', '?')}): missing fields {sorted(missing)}")

        eid = str(event.get("id", ""))
        if not ID_RE.match(eid):
            errors.append(f"{prefix}: id {eid!r} must be kebab-case ([a-z0-9-]+)")
        elif eid in seen_ids:
            errors.append(f"{prefix}: duplicate id {eid!r}")
        seen_ids.add(eid)

        if event.get("region") not in ALLOWED_REGIONS:
            errors.append(f"{prefix} ({eid}): invalid region {event.get('region')!r}")

        if event.get("format") not in ALLOWED_FORMATS:
            errors.append(f"{prefix} ({eid}): invalid format {event.get('format')!r}")

        status = event.get("registration_status")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{prefix} ({eid}): invalid registration_status {status!r}")
        else:
            status_counts[status] = status_counts.get(status, 0) + 1

        cats = event.get("category")
        if not isinstance(cats, list) or not cats or not all(isinstance(c, str) and c for c in cats):
            errors.append(f"{prefix} ({eid}): category must be a non-empty list of strings")

        url = str(event.get("url", ""))
        if not (url.startswith("https://") or url.startswith("http://")):
            errors.append(f"{prefix} ({eid}): url must start with http:// or https://, got {url!r}")

        lv = str(event.get("last_verified", ""))
        if not DATE_RE.match(lv):
            errors.append(f"{prefix} ({eid}): last_verified must be YYYY-MM-DD, got {lv!r}")

    if errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"OK: Validated {len(events)} events (last_updated={last_updated})")
    for st in sorted(status_counts):
        print(f"  - {st}: {status_counts[st]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(validate())
