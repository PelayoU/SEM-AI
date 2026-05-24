#!/usr/bin/env python3
"""session-close — close the current framework session.

Steps:
  1. Verify we're on a session/* branch + the doc exists
  2. Parse the doc's in-play list
  3. Post 🏁 comments on each in-play Issue (the outcome line)
  4. Print summary; the agent decides merge / PR / discard interactively

This script does NOT execute the merge/PR/discard automatically — those
are decisions the human must make. The skill's SKILL.md guides the agent
through the post-close decision.

Usage:
  python scripts/skills/session_close.py [--outcome "<one-line>"]
                                         [--no-comments]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from scripts.skills._common import ( # noqa: E402
    current_branch,
    doc_path_for,
    gh_issue_comment,
    normalize_issue_number,
    session_id_from_branch,
)


# Match the in-play frontmatter line: in-play: ["#42", "#43"]
_IN_PLAY_RE = re.compile(
    r"^in-play:\s*\[(.*?)\]",
    re.MULTILINE,
)


def parse_in_play_from_doc(doc_text: str) -> list[str]:
    """Extract the in-play list from the YAML frontmatter."""
    m = _IN_PLAY_RE.search(doc_text)
    if not m:
        return []
    raw = m.group(1)
    # Split on commas, strip quotes/whitespace
    refs = []
    for part in raw.split(","):
        ref = part.strip().strip('"').strip("'").strip()
        if ref:
            refs.append(ref)
    return refs


def main() -> int:
    parser = argparse.ArgumentParser(prog="session-close")
    parser.add_argument(
        "--outcome", default="(session closing — review the Handoff for the final state)",
        help="One-line summary that goes into the 🏁 comment",
    )
    parser.add_argument(
        "--no-comments", action="store_true",
        help="Skip posting 🏁 comments (useful for sessions that didn't touch Issues)",
    )
    args = parser.parse_args()

    branch = current_branch()
    session_id = session_id_from_branch(branch) if branch else None
    if not session_id:
        print(
            f"FAIL: not on a session/* branch (current: {branch!r}). "
            "session-close only works from inside a session.",
            file=sys.stderr,
        )
        return 1

    doc = doc_path_for(session_id)
    if not doc.exists():
        print(
            f"FAIL: session doc sessions/{session_id}.md not found.",
            file=sys.stderr,
        )
        return 1

    doc_text = doc.read_text(encoding="utf-8")
    in_play_refs = parse_in_play_from_doc(doc_text)

    posted = 0
    if not args.no_comments and in_play_refs:
        for ref in in_play_refs:
            comment_body = (
                f"🏁 Session closed: [session/{session_id}]"
                f"(../../tree/session/{session_id}) — {args.outcome}"
            )
            if gh_issue_comment(normalize_issue_number(ref), comment_body):
                posted += 1

    # Print summary
    print(f"Closing session {session_id}")
    print(f" Branch: {branch}")
    print(f" Doc: sessions/{session_id}.md")
    if in_play_refs:
        print(
            f" 🏁 comments posted: {posted}/{len(in_play_refs)} "
            f"({', '.join(in_play_refs)})"
        )
    print()
    print("Next: decide the disposition of this branch:")
    print(
        " - merge to main: git checkout main && git merge --no-ff "
        f"session/{session_id}"
    )
    print(
        " - open PR for review: gh pr create --base main --head "
        f"session/{session_id}"
    )
    print(
        f" - discard the branch: git checkout main && "
        f"git branch -D session/{session_id}"
    )
    print()
    print(
        "Per dogfood: the disposition is your call. The session doc "
        "is preserved in either case (committed to the branch + visible via "
        "the 🏁 Issue comments)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
