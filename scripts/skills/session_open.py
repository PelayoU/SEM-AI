#!/usr/bin/env python3
"""session-open — start a new framework session.

Creates:
  - branch `session/<YYYY-MM-DD>-<slug>` off main
  - doc `sessions/<YYYY-MM-DD>-<slug>.md` with the 3-part scaffold
  - 📍 comments on each Issue listed via --in-play

Usage:
  python scripts/skills/session_open.py <slug> [--context "<one-line>"]
                                               [--in-play "#42,#43"]
                                               [--from-branch main]

Exits 0 on success, non-zero on git/gh failure.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from scripts.skills._common import (  # noqa: E402
    SESSIONS_DIR,
    doc_path_for,
    gh_issue_comment,
    normalize_issue_number,
    slugify,
    today,
)


DOC_TEMPLATE = """---
id: {session_id}
opened: {today}
in-play: {in_play_yaml}
---

## Context

{context}

## Decisions

_(Append-only — record each binding decision as a line: date / role / what was decided / condensed why + alternatives rejected / link to affected Issue.)_

## Handoff

_Active role:_ {role}
_In play:_ {in_play_human}
_Next:_ {next_step}
"""


def main() -> int:
    parser = argparse.ArgumentParser(prog="session-open")
    parser.add_argument("slug", help="Short slug; will be combined with today's date")
    parser.add_argument("--context", default="(write why this session exists)")
    parser.add_argument(
        "--in-play", default="",
        help="Comma-separated Issue refs entering in-play (e.g. '#42,#43')",
    )
    parser.add_argument(
        "--role", default="product-manager",
        help="Active role at session start",
    )
    parser.add_argument(
        "--next", dest="next_step", default="(state the first concrete step)",
    )
    parser.add_argument("--from-branch", default="main")
    args = parser.parse_args()

    slug = slugify(args.slug)
    session_id = f"{today()}-{slug}"
    branch = f"session/{session_id}"
    doc = doc_path_for(session_id)

    # 1. Ensure sessions/ directory exists
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)

    # 2. Create the branch
    try:
        subprocess.run(
            ["git", "checkout", args.from_branch],
            check=True, capture_output=True, text=True, timeout=10,
        )
        subprocess.run(
            ["git", "checkout", "-b", branch],
            check=True, capture_output=True, text=True, timeout=10,
        )
    except subprocess.CalledProcessError as e:
        print(f"FAIL: git operation failed: {e.stderr}", file=sys.stderr)
        return 1

    # 3. Parse in-play list
    in_play_raw = [s.strip() for s in args.in_play.split(",") if s.strip()]
    in_play_normalized = [
        "#" + normalize_issue_number(ref) for ref in in_play_raw
    ]
    in_play_yaml = (
        "[" + ", ".join(f'"{ref}"' for ref in in_play_normalized) + "]"
        if in_play_normalized
        else "[]"
    )
    in_play_human = (
        ", ".join(in_play_normalized) if in_play_normalized else "(none yet)"
    )

    # 4. Write the session doc
    doc_text = DOC_TEMPLATE.format(
        session_id=session_id,
        today=today(),
        in_play_yaml=in_play_yaml,
        context=args.context,
        role=args.role,
        in_play_human=in_play_human,
        next_step=args.next_step,
    )
    doc.write_text(doc_text, encoding="utf-8")

    # 5. Stage + commit the doc
    try:
        subprocess.run(
            ["git", "add", str(doc.relative_to(REPO_ROOT))],
            check=True, capture_output=True, text=True, timeout=5,
        )
        subprocess.run(
            ["git", "commit", "-m", f"session: open {session_id}"],
            check=True, capture_output=True, text=True, timeout=10,
        )
    except subprocess.CalledProcessError as e:
        print(f"WARN: could not commit session doc: {e.stderr}", file=sys.stderr)
        # Continue — branch + doc exist even if commit failed

    # 6. Post 📍 comments on each in-play Issue
    posted = 0
    for ref in in_play_normalized:
        comment_body = (
            f"📍 In play in [session/{session_id}]"
            f"(../../tree/session/{session_id}) — see "
            f"[sessions/{session_id}.md]"
            f"(../../blob/session/{session_id}/sessions/{session_id}.md)"
        )
        if gh_issue_comment(normalize_issue_number(ref), comment_body):
            posted += 1

    print(f"Opened session {session_id}")
    print(f"  Branch: {branch}")
    print(f"  Doc:    sessions/{session_id}.md")
    if in_play_normalized:
        print(
            f"  📍 comments posted: {posted}/{len(in_play_normalized)} "
            f"({', '.join(in_play_normalized)})"
        )
    print()
    print(f"Next: edit sessions/{session_id}.md to refine Context + Handoff.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
