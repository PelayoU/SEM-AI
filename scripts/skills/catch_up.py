#!/usr/bin/env python3
"""catch-up — digest of graph changes since the last invocation.

Reads GitHub notifications (or a --since timestamp) and surfaces:
  - Issues that changed state recently
  - New Issues
  - Comments on Issues the agent might have in its working set
  - PRs that mergered

Output is structured markdown suitable for the agent to read at the
start of a session. Persists the last-invocation timestamp in
`.sem-ai/last-catch-up.json` so the next invocation defaults to "since
last time".

Usage:
  python scripts/skills/catch_up.py                # since last invocation
  python scripts/skills/catch_up.py --since 7d     # last 7 days
  python scripts/skills/catch_up.py --since 2026-05-01T00:00:00Z
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

STATE_DIR = REPO_ROOT / ".sem-ai"
STATE_FILE = STATE_DIR / "last-catch-up.json"


# ----- Time parsing ----------------------------------------------------------


_RELATIVE_RE = re.compile(r"^(\d+)([dhmw])$")


def parse_since(value: str | None) -> datetime:
    """Parse the --since argument to a UTC datetime.

    Accepts:
      - ISO 8601 timestamps (e.g. "2026-05-01T00:00:00Z")
      - Relative durations: "7d", "24h", "30m", "2w"
      - None → returns the persisted last-catch-up timestamp, or 24h ago

    Always returns UTC.
    """
    now = datetime.now(timezone.utc)
    if value is None:
        return _load_last_catch_up() or (now - timedelta(hours=24))

    m = _RELATIVE_RE.fullmatch(value.strip())
    if m:
        n = int(m.group(1))
        unit = m.group(2)
        delta = {
            "m": timedelta(minutes=n),
            "h": timedelta(hours=n),
            "d": timedelta(days=n),
            "w": timedelta(weeks=n),
        }[unit]
        return now - delta

    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        dt = datetime.fromisoformat(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError as e:
        print(f"FAIL: could not parse --since value {value!r}: {e}", file=sys.stderr)
        sys.exit(2)


def _load_last_catch_up() -> datetime | None:
    if not STATE_FILE.exists():
        return None
    try:
        data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
        ts = data.get("last_invocation")
        if not ts:
            return None
        if ts.endswith("Z"):
            ts = ts[:-1] + "+00:00"
        return datetime.fromisoformat(ts)
    except (OSError, json.JSONDecodeError, ValueError):
        return None


def _save_last_catch_up(when: datetime) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps(
            {"last_invocation": when.isoformat()},
            indent=2,
        ),
        encoding="utf-8",
    )


# ----- gh queries ------------------------------------------------------------


def _gh_json(args: list[str]) -> object | None:
    try:
        result = subprocess.run(
            ["gh", *args],
            capture_output=True, text=True, check=True, timeout=30,
        )
        return json.loads(result.stdout) if result.stdout else None
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        FileNotFoundError,
        json.JSONDecodeError,
    ):
        return None


def query_recently_updated_issues(since: datetime) -> list[dict]:
    """Issues with updatedAt >= since. Limited to 100 most recent."""
    since_iso = since.strftime("%Y-%m-%dT%H:%M:%SZ")
    data = _gh_json(
        [
            "issue", "list",
            "--state", "all",
            "--limit", "100",
            "--json", "number,title,state,updatedAt,labels,author",
            "--search", f"updated:>={since_iso}",
        ]
    )
    if not isinstance(data, list):
        return []
    return data


def query_recently_merged_prs(since: datetime) -> list[dict]:
    """PRs merged on/after `since`."""
    since_iso = since.strftime("%Y-%m-%dT%H:%M:%SZ")
    data = _gh_json(
        [
            "pr", "list",
            "--state", "merged",
            "--limit", "50",
            "--json", "number,title,mergedAt,author,body",
            "--search", f"merged:>={since_iso}",
        ]
    )
    if not isinstance(data, list):
        return []
    return data


# ----- Render -----------------------------------------------------------------


def _label_names(issue: dict) -> list[str]:
    out = []
    for label in issue.get("labels", []) or []:
        if isinstance(label, dict):
            name = label.get("name")
            if name:
                out.append(name)
        elif isinstance(label, str):
            out.append(label)
    return out


def _classify_issue(issue: dict) -> str:
    """Detect rough category from labels."""
    labels = _label_names(issue)
    for label in labels:
        if label.startswith("type:"):
            return label[len("type:") :]
    if "bug" in labels:
        return "bug"
    return "(untyped)"


def render(
    since: datetime,
    issues: list[dict],
    merged_prs: list[dict],
) -> str:
    """Build the digest markdown."""
    lines = []
    lines.append(f"# Catch-up — changes since {since.strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append("")

    if not issues and not merged_prs:
        lines.append("_No changes detected in this window._")
        return "\n".join(lines)

    # Group issues by category
    if issues:
        by_category: dict[str, list[dict]] = {}
        for issue in issues:
            cat = _classify_issue(issue)
            by_category.setdefault(cat, []).append(issue)
        lines.append(f"## Issues updated ({len(issues)})")
        for cat in sorted(by_category.keys()):
            cat_issues = by_category[cat]
            lines.append("")
            lines.append(f"### {cat} ({len(cat_issues)})")
            for issue in cat_issues:
                state = issue.get("state", "?").lower()
                ts = issue.get("updatedAt", "")[:16].replace("T", " ")
                lines.append(
                    f"- #{issue['number']} [{state}] _{ts}_ — {issue.get('title', '')}"
                )

    if merged_prs:
        lines.append("")
        lines.append(f"## PRs merged ({len(merged_prs)})")
        for pr in merged_prs:
            ts = pr.get("mergedAt", "")[:16].replace("T", " ")
            lines.append(
                f"- PR #{pr['number']} _{ts}_ — {pr.get('title', '')}"
            )

    return "\n".join(lines)


# ----- Main ------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(prog="catch-up")
    parser.add_argument(
        "--since", default=None,
        help=(
            "ISO timestamp or relative (e.g. '7d', '24h'). "
            "Default: since last invocation, or 24h ago."
        ),
    )
    parser.add_argument(
        "--no-state", action="store_true",
        help="Do not update the .sem-ai/last-catch-up.json file",
    )
    args = parser.parse_args()

    since = parse_since(args.since)

    issues = query_recently_updated_issues(since)
    merged_prs = query_recently_merged_prs(since)

    output = render(since, issues, merged_prs)
    print(output)

    if not args.no_state:
        _save_last_catch_up(datetime.now(timezone.utc))

    return 0


if __name__ == "__main__":
    sys.exit(main())
