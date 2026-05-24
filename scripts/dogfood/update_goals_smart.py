#!/usr/bin/env python3
"""Bootstrap dogfood Part 4: apply SMART fixes to goals #11-#18.

Two fixes per the slide-driven audit:
  (a) Add a `## Stakeholder` section to every goal body (slotted between
      Outcome statement and Parent vision). Names the WHO of the template
      "In order to [outcome], as [STAKEHOLDER], I want { capabilities }".
  (b) Time-bound the continuous goals (G2, G3, G7) by editing their
      Horizon and Acceptance check sections with concrete checkpoints,
      without renouncing the steady-state nature of the goal.

Idempotent: skips a goal if the `## Stakeholder` section already exists;
skips time-bound updates if the new acceptance-check text is already
present.

Run once:
    SEM_AI_REPO=PelayoU/SEM-AI .venv/bin/python scripts/dogfood/update_goals_smart.py
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from engine.adapters import GitHubAdapter, load_config  # noqa: E402
from engine.core import api  # noqa: E402
from engine.core.catalog import NodeType  # noqa: E402
from engine.core.permissions import Role  # noqa: E402


# ============================================================================
# Patch definitions — keyed by Issue id
# ============================================================================


@dataclass(frozen=True)
class GoalPatch:
    code: str  # "G1"
    issue_id: str  # "#11"
    stakeholder: str  # body of the new ## Stakeholder section
    new_horizon: str | None = None  # replaces ## Horizon body if not None
    new_acceptance: str | None = None  # replaces ## Acceptance check body if not None


PATCHES: list[GoalPatch] = [
    GoalPatch(
        code="G1",
        issue_id="#11",
        stakeholder="Adopter team — developers and PM maintaining a product across years. The framework's value to this stakeholder is preserved investment in AI-generated work: code, decisions, and learning all remain navigable and evolvable, not abandoned to opaque blob status six months after initial generation.",
    ),
    GoalPatch(
        code="G2",
        issue_id="#12",
        stakeholder="Adopter team's PM (sees role-correct, scope-aware work landing in the graph) and developers (operate alongside AI agents that stay in their lane, without policing or rework). Indirectly: anyone reviewing AI-generated PRs — they get structurally sound work, not chaos.",
        new_horizon="Continuous as a steady-state property of the framework. Time-bound checkpoint: **v1.0 release**.",
        new_acceptance="By **v1.0 release**, ≥80% of AI-generated PRs sampled across dogfood + ≥3 adopter projects pass a scope-violation audit at first review (sampled manually until an automated audit ships). Continuous lifetime goal: rates trend toward zero as the framework matures and methodology skills accumulate.",
    ),
    GoalPatch(
        code="G3",
        issue_id="#13",
        stakeholder="Adopter team's QA + developers — QA gains an automated structural-defect screen before manual review; developers receive findings inline in their Claude Code session, before the work is consolidated, so fixes happen in context rather than after a costly review round-trip.",
        new_horizon="Continuous from v0.3.0 onwards; surface area grows as more semantic checks are written. Time-bound checkpoint: **v1.0 release**.",
        new_acceptance="By **v1.0 release**: ≥80% of structural defects (catalogue-violations + missing-required-section + supersede-chain breaks) caught by automated checks before human PR review. Measured by counting findings in CI logs vs findings in PR review comments across dogfood + ≥3 adopter projects.",
    ),
    GoalPatch(
        code="G4",
        issue_id="#14",
        stakeholder="Adopter team's PM and developers — they feel discovery cost directly every cycle (searching for what was decided, who owns what, where the spec lives). If this goal is realized, both segments spend more time validating and less searching, which is the vision's *Why* made operational.",
    ),
    GoalPatch(
        code="G5",
        issue_id="#15",
        stakeholder="Two segments simultaneously: **solo developer / freelancer / 2-3 person team** (gets enterprise-grade discipline as a default — typed graph, role discipline, mechanical CI — without building it themselves), AND **enterprise PM / engineering lead** (injects house methodology via `.claude/skills/` to enforce corporate practice over AI behavior without forking the framework).",
    ),
    GoalPatch(
        code="G6",
        issue_id="#16",
        stakeholder="SEM-AI maintainers (Pelayo + future team) — adoption is the proxy by which the framework's existence is justified; without adoption, G1-G5 cannot be observed in the world. Indirectly: prospective adopters who discover the framework through references / template fork signals / community signals.",
    ),
    GoalPatch(
        code="G7",
        issue_id="#17",
        stakeholder="SEM-AI maintainers — dogfood is both a credibility signal to potential adopters (*they use it themselves*) and a continuous integration test of the framework model (every time we use SEM-AI to build SEM-AI we find friction the model must address).",
        new_horizon="Continuous from v0.3.0 onwards, **audited quarterly starting Q1-2027**. The 2026-05-24 migration of 9 markdown ADRs to Issues #2-#10 is the first major dogfood inflection point; further ones occur each time the framework gains a capability.",
        new_acceptance="**Quarterly dogfood audit starting Q1-2027**. At each audit, the SEM-AI repo's graph is queryable and self-consistent: no orphan artifacts; no decisions stored outside Issues; no role-violations in commit history; every substantive work block has an associated session doc. Checkable via the framework's own validators run against itself.",
    ),
    GoalPatch(
        code="G8",
        issue_id="#18",
        stakeholder="Non-GitHub-using adopter — enterprise teams with compliance / legal / on-prem constraints that prevent GitHub usage, plus organizations on Jira / Linear / GitLab / private backends. The viability of the abstraction is also a credibility signal to vendor-conscious buyers.",
    ),
]


# ============================================================================
# Body manipulation helpers
# ============================================================================


_STAKEHOLDER_HEADING = "## Stakeholder"


def has_stakeholder(body: str) -> bool:
    """Return True if the body already contains a `## Stakeholder` section."""
    return bool(re.search(rf"^{re.escape(_STAKEHOLDER_HEADING)}\b", body, re.MULTILINE))


def insert_stakeholder(body: str, text: str) -> str:
    """Insert a `## Stakeholder` section between Outcome statement and Parent vision."""
    new_section = f"{_STAKEHOLDER_HEADING}\n\n{text}\n\n"
    pattern = re.compile(r"^(## Parent vision\b)", re.MULTILINE)
    new_body, count = pattern.subn(new_section + r"\1", body, count=1)
    if count == 0:
        raise RuntimeError(
            "could not locate '## Parent vision' heading to anchor Stakeholder section"
        )
    return new_body


_SECTION_RE_CACHE: dict[str, re.Pattern[str]] = {}


def _section_re(heading: str) -> re.Pattern[str]:
    if heading not in _SECTION_RE_CACHE:
        _SECTION_RE_CACHE[heading] = re.compile(
            rf"^## {re.escape(heading)}\b[^\n]*\n(.*?)(?=^## |\Z)",
            re.MULTILINE | re.DOTALL,
        )
    return _SECTION_RE_CACHE[heading]


def section_matches(body: str, heading: str, new_content: str) -> bool:
    """True if the section's current content already equals `new_content` (whitespace-trimmed)."""
    m = _section_re(heading).search(body)
    if m is None:
        return False
    return m.group(1).strip() == new_content.strip()


def replace_section_body(body: str, heading: str, new_content: str) -> tuple[str, bool]:
    """Replace the content of a `## {heading}` section, preserving the heading.

    Returns (new_body, changed) where changed=True if a replacement happened.
    """
    replacement_block = f"## {heading}\n\n{new_content}\n\n"
    new_body, count = _section_re(heading).subn(replacement_block, body, count=1)
    if count == 0:
        return body, False
    return new_body, new_body != body


# ============================================================================
# Main
# ============================================================================


def main() -> int:
    cfg = load_config()
    adapter = GitHubAdapter(cfg)

    print(f"Target repo: {cfg.repo}")
    print()

    existing_goals = {g.id: g for g in adapter.query_issues(type=NodeType.GOAL)}
    print(f"Found {len(existing_goals)} goal Issues on the graph")
    print()

    patched = 0
    skipped = 0
    for patch in PATCHES:
        node = existing_goals.get(patch.issue_id)
        if node is None:
            print(f"  [skip] {patch.code} {patch.issue_id} not found on the graph")
            continue

        current_body = node.body or ""
        new_body = current_body
        actions: list[str] = []

        # (a) Stakeholder section
        if has_stakeholder(new_body):
            actions.append("stakeholder=exists")
        else:
            new_body = insert_stakeholder(new_body, patch.stakeholder)
            actions.append("stakeholder=added")

        # (b) Time-bound checkpoints (only goals with these patches set).
        # Compare actual current section content vs the desired new content
        # to decide whether to update — sentinel matching is too brittle when
        # old and new share a common prefix.
        if patch.new_horizon is not None:
            if section_matches(new_body, "Horizon", patch.new_horizon):
                actions.append("horizon=exists")
            else:
                new_body, changed = replace_section_body(
                    new_body, "Horizon", patch.new_horizon
                )
                actions.append(
                    "horizon=updated" if changed else "horizon=not-found"
                )

        if patch.new_acceptance is not None:
            if section_matches(new_body, "Acceptance check", patch.new_acceptance):
                actions.append("acceptance=exists")
            else:
                new_body, changed = replace_section_body(
                    new_body, "Acceptance check", patch.new_acceptance
                )
                actions.append(
                    "acceptance=updated" if changed else "acceptance=not-found"
                )

        if new_body == current_body:
            print(f"  [no-op]  {patch.code} {patch.issue_id} ({', '.join(actions)})")
            skipped += 1
            continue

        try:
            api.update_node(
                adapter,
                node_id=patch.issue_id,
                body=new_body,
                acting_role=Role.PM,
            )
        except Exception as e:
            print(f"  [FAIL]   {patch.code} {patch.issue_id}: {e}")
            return 1

        print(f"  [update] {patch.code} {patch.issue_id} ({', '.join(actions)})")
        patched += 1

    print()
    print(f"==> Done. Patched: {patched}, no-op: {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
