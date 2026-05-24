#!/usr/bin/env python3
"""PostToolUse hook on Bash(gh pr merge *).

When a PR mergers, parse 'Closes #N' references from the PR body and post
a comment on each closed Issue listing the files the PR changed. This
materializes the artifacts-derived-from-PRs rule.

The bot comment format: '📦 Artifacts derived: ...' so it's distinct from
the 📍/✅/🏁 session lifecycle markers.

For v0.3.0 the hook uses `gh` CLI directly to read the merged PR's body
and files, then `gh issue comment` to post the artifact list. No engine
adapter needed — this is purely a `gh`-orchestrated side effect.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from scripts.hooks._common import emit, read_input # noqa: E402

# Match `gh pr merge <num>` or `gh pr merge <num> --squash` etc.
_PR_NUM_RE = re.compile(r"gh\s+pr\s+merge\s+(\d+)")


def _gh_pr_view(pr_number: str) -> dict | None:
    """Fetch PR JSON via gh. Returns None on any failure."""
    try:
        result = subprocess.run(
            [
                "gh", "pr", "view", pr_number,
                "--json", "body,files",
            ],
            capture_output=True, text=True, check=True, timeout=10,
        )
        return json.loads(result.stdout)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired,
            FileNotFoundError, json.JSONDecodeError):
        return None


def _gh_issue_comment(issue_number: str, body: str) -> bool:
    """Post a comment on the issue. Returns True on success."""
    try:
        subprocess.run(
            ["gh", "issue", "comment", issue_number, "--body", body],
            capture_output=True, text=True, check=True, timeout=10,
        )
        return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired,
            FileNotFoundError):
        return False


def main() -> int:
    payload = read_input()
    tool_input = payload.get("tool_input") or {}
    command = tool_input.get("command", "")

    m = _PR_NUM_RE.search(command)
    if not m:
        return 0
    pr_number = m.group(1)

    pr_data = _gh_pr_view(pr_number)
    if pr_data is None:
        return 0

    body = pr_data.get("body") or ""
    files_list = pr_data.get("files") or []
    file_paths = tuple(
        f.get("path", "") for f in files_list if isinstance(f, dict)
    )
    file_paths = tuple(p for p in file_paths if p)

    # Parse Closes #N from the body
    from engine.checks.artifacts_derive import parse_closed_issues

    closed_ids = parse_closed_issues(body)
    if not closed_ids:
        emit({"systemMessage": f"PR #{pr_number} merged but has no Closes #N references; no artifacts derived."})
        return 0

    if not file_paths:
        emit({"systemMessage": f"PR #{pr_number} merged but had no changed files."})
        return 0

    # Post a comment on each closed Issue with the artifact list
    files_md = "\n".join(f"- `{p}`" for p in file_paths)
    comment_body = (
        f"📦 Artifacts derived from merged PR #{pr_number}:\n\n"
        f"{files_md}\n\n"
        f"_Posted by SEM-AI post-merge hook._"
    )

    posted = 0
    for issue_id in closed_ids:
        issue_number = issue_id.lstrip("#")
        if _gh_issue_comment(issue_number, comment_body):
            posted += 1

    emit(
        {
            "systemMessage": (
                f"PR #{pr_number} merged. Posted artifact-derivation comment "
                f"on {posted}/{len(closed_ids)} closed Issue(s)."
            )
        }
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
