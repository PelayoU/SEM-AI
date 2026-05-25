#!/usr/bin/env python3
"""Migrate `parent:#N` label fallbacks to native sub-issue relationships.

Background: pre-2026-05-25 the GitHubAdapter passed `issue_number` instead
of `database_id` as the `sub_issue_id` parameter to the sub-issues POST API.
The call silently 404'd; the fallback applied a `parent:#N` label. We
misdiagnosed the failure as a personal-account / private-repo limitation
for ~6 months.

The bug is now fixed in the adapter. This script cleans up the historical
state on PelayoU/SEM-AI: for each Issue carrying a `parent:#N` label,
attempt the native sub-issue link with the correct database_id; if the
link succeeds (or already exists), remove the `parent:#N` label.

Idempotent:
  - Skips Issues already linked natively (just removes the label)
  - Skips Issues whose API call still fails (leaves the label as
    defensive fallback)

Run once:
    SEM_AI_REPO=PelayoU/SEM-AI .venv/bin/python scripts/dogfood/migrate_parent_labels_to_subissues.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from engine.adapters import GitHubAdapter, load_config  # noqa: E402
from engine.core.permissions import Role  # noqa: E402


_PARENT_LABEL_RE = re.compile(r"^parent:#(\d+)$")


def _run_gh(args: list[str]) -> str:
    """Run gh with capture; raise on non-zero exit."""
    result = subprocess.run(
        ["gh", *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def _fetch_database_id(repo: str, issue_n: int) -> int:
    """Get the GraphQL/REST database id (integer) of an Issue."""
    out = _run_gh(
        ["api", f"repos/{repo}/issues/{issue_n}", "--jq", ".id"]
    ).strip()
    return int(out)


def _fetch_sub_issue_ids(repo: str, parent_n: int) -> set[int]:
    """Fetch the set of database ids currently linked as sub-issues of parent_n."""
    out = _run_gh(
        ["api", f"repos/{repo}/issues/{parent_n}/sub_issues"]
    ).strip()
    if not out:
        return set()
    data = json.loads(out)
    return {item["id"] for item in data}


def _try_link_sub_issue(
    repo: str, parent_n: int, child_database_id: int
) -> tuple[bool, str]:
    """Attempt native sub-issue link. Returns (success, message)."""
    try:
        _run_gh(
            [
                "api",
                "-X",
                "POST",
                f"repos/{repo}/issues/{parent_n}/sub_issues",
                "-F",
                f"sub_issue_id={child_database_id}",
            ]
        )
        return True, "linked"
    except subprocess.CalledProcessError as e:
        return False, f"api error: {e.stderr.strip()[:120]}"


def main() -> int:
    cfg = load_config()
    adapter = GitHubAdapter(cfg)
    repo = cfg.repo

    print(f"Target repo: {repo}")
    print()

    # Find every Issue carrying a parent:#N label (state=all to catch closed too)
    print("==> Scanning all Issues for parent:#N labels")
    raw = _run_gh(
        [
            "issue",
            "list",
            "--repo",
            repo,
            "--state",
            "all",
            "--limit",
            "1000",
            "--json",
            "number,labels",
        ]
    )
    issues = json.loads(raw)
    candidates: list[tuple[int, int, str]] = []  # (issue_n, parent_n, label_name)
    for issue in issues:
        for label in issue.get("labels", []):
            m = _PARENT_LABEL_RE.match(label["name"])
            if m:
                candidates.append(
                    (issue["number"], int(m.group(1)), label["name"])
                )
                break

    print(f"    {len(candidates)} Issues carry a parent:#N label")
    print()

    if not candidates:
        print("==> Nothing to migrate.")
        return 0

    # Cache sub_issue lists per parent (avoid N round-trips for the same parent)
    sub_cache: dict[int, set[int]] = {}

    linked = 0
    already_linked = 0
    failed = 0
    cleaned_label_count = 0

    for issue_n, parent_n, label_name in candidates:
        try:
            child_db_id = _fetch_database_id(repo, issue_n)
        except subprocess.CalledProcessError as e:
            print(f"  [FAIL] #{issue_n}: could not fetch db id ({e.stderr.strip()[:80]})")
            failed += 1
            continue

        if parent_n not in sub_cache:
            try:
                sub_cache[parent_n] = _fetch_sub_issue_ids(repo, parent_n)
            except subprocess.CalledProcessError as e:
                print(
                    f"  [FAIL] #{issue_n}: could not fetch sub_issues of "
                    f"parent #{parent_n} ({e.stderr.strip()[:80]})"
                )
                failed += 1
                continue

        if child_db_id in sub_cache[parent_n]:
            action = "already-linked"
            already_linked += 1
        else:
            ok, msg = _try_link_sub_issue(repo, parent_n, child_db_id)
            if ok:
                action = "linked"
                linked += 1
                sub_cache[parent_n].add(child_db_id)  # keep cache consistent
            else:
                print(
                    f"  [FAIL] #{issue_n} → parent #{parent_n}: {msg} — "
                    f"leaving label as fallback"
                )
                failed += 1
                continue

        # Action succeeded (linked or already-linked) → remove the label
        try:
            adapter.remove_label(
                f"#{issue_n}", label_name, acting_role=Role.PM
            )
            cleaned_label_count += 1
        except Exception as e:
            print(
                f"  [partial] #{issue_n}: sub-issue {action}, but label "
                f"removal failed ({e})"
            )
            continue

        print(
            f"  [{action:14}] #{issue_n} → parent #{parent_n} (db id={child_db_id})"
        )

    print()
    print("==> Summary")
    print(f"    Newly linked:    {linked}")
    print(f"    Already linked:  {already_linked}")
    print(f"    Labels cleaned:  {cleaned_label_count}")
    print(f"    Failed:          {failed} (label kept as fallback)")
    print(f"    Total processed: {len(candidates)}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
