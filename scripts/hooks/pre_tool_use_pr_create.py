#!/usr/bin/env python3
"""PreToolUse hook on Bash(gh pr create *).

Before the agent opens a PR, run engine/checks/ against the Issues the PR
claims to close (parsed from the PR body the `gh pr create` command would
post). Surfaces findings as additionalContext so the agent can adjust
before pushing the PR.

For v0.3.0 the hook does NOT block on warnings — only emits context. A
future iteration could `permissionDecision=deny` on critical findings if
the team configures it.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from scripts.hooks._common import emit_context, read_input  # noqa: E402

# Match "--body 'text with closes #N'" or "--body \"text\""
_BODY_FLAG_RE = re.compile(r"--body\s+(?:'([^']*)'|\"([^\"]*)\")")
# Match "Closes #42", "Fixes #42", etc.
_CLOSES_RE = re.compile(
    r"(?i)\b(?:close|closes|closed|fix|fixes|fixed|resolve|resolves|resolved)\s+#(\d+)"
)


def _extract_pr_body(command: str) -> str:
    """Extract the --body argument from a `gh pr create ...` command line."""
    m = _BODY_FLAG_RE.search(command)
    if not m:
        return ""
    return m.group(1) or m.group(2) or ""


def main() -> int:
    payload = read_input()

    # Confirm this is the gh pr create matcher
    tool_input = payload.get("tool_input") or {}
    command = tool_input.get("command", "")
    if "gh pr create" not in command:
        return 0

    body = _extract_pr_body(command)
    closed_ids = [f"#{m.group(1)}" for m in _CLOSES_RE.finditer(body)]
    if not closed_ids:
        emit_context(
            "PreToolUse",
            (
                "[sem-ai pre-PR hook] PR body has no 'Closes #N' references — "
                "the merged PR will not auto-derive artifacts to any Issue. "
                "Confirm this is intentional, or add 'Closes #<spec-id>' to "
                "the PR body before pushing."
            ),
        )
        return 0

    # Run engine/checks/ against each closed Issue
    try:
        from engine.adapters import GitHubAdapter, load_config
        from engine.checks import run_all_checks
    except ImportError:
        return 0

    try:
        adapter = GitHubAdapter(load_config())
    except Exception:
        return 0

    all_findings: list[tuple[str, object]] = []
    for issue_id in closed_ids:
        try:
            node = adapter.get_issue(issue_id)
            findings = run_all_checks(node, adapter)
            for f in findings:
                all_findings.append((issue_id, f))
        except Exception:
            continue

    if not all_findings:
        return 0  # quiet — all the Issues being closed look fine

    lines = [
        f"📋 Pre-PR checks across {len(closed_ids)} Issue(s) surfaced "
        f"{len(all_findings)} finding(s):",
        "",
    ]
    for issue_id, f in all_findings:
        sev_emoji = {"info": "ℹ️", "warning": "⚠️", "error": "❌"}.get(
            f.severity, "•"
        )
        lines.append(f"  {sev_emoji} {issue_id} [{f.code}] {f.message}")
    lines.append("")
    lines.append(
        "These are warnings (the hook does not block). Consider addressing "
        "them in the Issue body before the PR mergers."
    )
    emit_context("PreToolUse", "\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
