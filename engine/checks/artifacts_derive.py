"""Artifacts derivation from PR bodies.

Per ADR-001 § 'How it works' (frontmatter equivalent → artifacts):
artifacts of a node are derived post-hoc from PRs that close the Issue
via `Closes #N` markers in the PR body. This module parses the markers
and returns the mapping.

Invoked by:
  - The `PostToolUse on Bash(gh pr merge *)` hook (ADR-004 hook 5) to
    record artifacts the moment a PR mergers, so the agent's next call
    to `get_node` reflects the new evidence.
  - The `sem-ai-artifacts.yml` Action example (per ADR-004 + ADR-009)
    when a PR mergers outside Claude Code.

This is not a check that returns Findings — it's a deriver that returns
the actual mapping. Lives in this package alongside the checks because
both are part of the semantic CI library invoked from the same callers.
"""

from __future__ import annotations

import re

# Matches "Closes #42", "closes #42", "Close #42", "Fixes #42", "Resolves #42"
# Source: GitHub's documented keywords for linking PRs to Issues.
_CLOSE_KEYWORDS = (
    "close",
    "closes",
    "closed",
    "fix",
    "fixes",
    "fixed",
    "resolve",
    "resolves",
    "resolved",
)

_CLOSE_PATTERN = re.compile(
    rf"(?i)\b(?:{'|'.join(_CLOSE_KEYWORDS)})\s+#(\d+)",
)


def parse_closed_issues(pr_body: str) -> tuple[str, ...]:
    """Extract all 'closes #N' references from a PR body.

    Returns a tuple of issue ids (e.g. ('#42', '#88')), deduplicated and
    preserving first-mention order. Returns an empty tuple if no
    references are found.

    Per GitHub's documented behavior, any of these keywords trigger
    automatic linking: close / closes / closed / fix / fixes / fixed /
    resolve / resolves / resolved.
    """
    if not pr_body:
        return ()
    seen: dict[str, None] = {}  # ordered dedupe
    for m in _CLOSE_PATTERN.finditer(pr_body):
        issue_id = f"#{m.group(1)}"
        seen.setdefault(issue_id, None)
    return tuple(seen.keys())


def derive_artifacts_from_pr_body(
    pr_body: str, changed_files: tuple[str, ...]
) -> dict[str, tuple[str, ...]]:
    """Map every closed-Issue id to the files the PR changed.

    Per ADR-001: each PR linked via `Closes #N` contributes its
    `changed_files` to the closed Issue's artifacts. If a PR closes
    multiple Issues, all of them get the same set of changed files.

    Args:
        pr_body: The body of the pull request as a string. The 'closes #N'
            references are typically in the body or in commit messages,
            but this function inspects the body; commit-message parsing
            is left to the caller (which would feed combined text here).
        changed_files: Tuple of file paths changed by the PR.

    Returns:
        A dict mapping each closed Issue id ('#42', '#88', …) to a
        tuple of the changed files. Empty dict if no Issues are closed
        by the PR.
    """
    closed = parse_closed_issues(pr_body)
    if not closed:
        return {}
    files = tuple(changed_files)
    return {issue_id: files for issue_id in closed}
