#!/usr/bin/env python3
"""Bootstrap dogfood Part 3: enrich vision #1's Value ambition slot.

Replaces the `## Value ambition` section of vision #1's body with a richer
version that distinguishes aspirational outcome prose (the polar-star
"world where..." paragraph) from concrete success markers (the 4
indicator bullets).

The rest of the body — Why / The future as a context / The future product
story / One-breath narrative / Positioning / Horizon / Adopted trends /
Holistic dimensions — is preserved verbatim.

Idempotent: if the body already contains the new content (detected via a
sentinel phrase), this is a no-op.

Run once, manually:
    SEM_AI_REPO=PelayoU/SEM-AI .venv/bin/python scripts/dogfood/update_vision_value_ambition.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from engine.adapters import GitHubAdapter, load_config  # noqa: E402
from engine.core import api  # noqa: E402
from engine.core.catalog import NodeType  # noqa: E402
from engine.core.permissions import Role  # noqa: E402


NEW_VALUE_AMBITION = """## Value ambition

A world where AI-augmented software development produces **durable, evolvable products** that humans can keep working on for years — where the AI is a role-correct peer that stays inside the project's plan, not a chaotic copilot that hallucinates new ones — where the discipline of typed product intent is available to a freelance developer and to a multinational equally — where the cost of AI participation is measured in **validation**, not in re-discovery — where releases, refactorings, bugfixes and improvements all happen continuously in the same graph that produced the first prototype.

Concretely, the framework will have arrived when:

- **≥10 independent projects** are actively running cycles on SEM-AI within 12 months of v1.0 — not just clicked-the-template, but operating under the model (vision + ≥3 goals + ≥10 features + session evidence).
- **Adopters report a measurable shift** in AI-augmented review labor from discovery ("what was decided, where, by whom") to validation ("is this correct given the context") — honestly tracked, including when it doesn't move.
- **The framework continuously dogfoods itself**: SEM-AI's own development operates under SEM-AI's model without parallel mechanisms (no markdown ADRs, no role-bleed, sessions used for substantial work).
- **A non-GitHub adapter is viable**: a Jira / Linear / GitLab implementation can be contributed without modifying `engine/core/` — validated by a stub adapter or accepted community RFC.

"""


# Sentinel — if the body already contains this phrase, the update has
# already been applied; this script becomes a no-op.
SENTINEL = "A world where AI-augmented software development produces"


# Matches the entire `## Value ambition` section from its heading up to
# (but excluding) the next `## ` heading or end-of-string. MULTILINE so `^`
# matches line starts; DOTALL so `.` matches newlines for the non-greedy
# `.*?` middle.
SECTION_RE = re.compile(
    r"^## Value ambition\n.*?(?=^## |\Z)",
    re.MULTILINE | re.DOTALL,
)


def main() -> int:
    cfg = load_config()
    adapter = GitHubAdapter(cfg)

    print(f"Target repo: {cfg.repo}")
    print()

    visions = adapter.query_issues(type=NodeType.VISION)
    if not visions:
        print("FAIL: no vision Issue found. Run migrate_to_issues.py first.")
        return 1
    vision = visions[0]
    print(f"==> Vision: {vision.id} ({vision.title!r})")

    current = adapter.get_issue(vision.id)
    body = current.body or ""

    if SENTINEL in body:
        print(
            f"    [no-op] vision {vision.id} already has the enriched "
            f"Value ambition section."
        )
        return 0

    match = SECTION_RE.search(body)
    if not match:
        print(
            f"FAIL: could not locate '## Value ambition' section in vision "
            f"{vision.id} body."
        )
        return 1

    new_body = SECTION_RE.sub(NEW_VALUE_AMBITION, body, count=1)

    print(f"==> Replacing Value ambition section")
    print(f"    old: {len(match.group())} chars")
    print(f"    new: {len(NEW_VALUE_AMBITION)} chars")
    print(f"    full body: {len(body)} → {len(new_body)} chars")

    api.update_node(
        adapter,
        node_id=vision.id,
        body=new_body,
        acting_role=Role.PM,
    )

    print(f"==> Vision {vision.id} body updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
