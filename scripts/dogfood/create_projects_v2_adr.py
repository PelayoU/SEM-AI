#!/usr/bin/env python3
"""Bootstrap dogfood Part 8: create the Projects v2 partition ADR.

Records the decision to treat Projects v2 as adopter-owned (visual layer
+ operational layer for methodology), with cero duplicación against the
framework's truth (Issues + labels + body). Includes the phased rollout:
v0.4 ships pure visual layer; v0.5+ adds operational passthrough when
adopter demand surfaces.

Parent: C5 #23 — Use GitHub as unified backend with no extra infrastructure.

Idempotent.

Run once:
    SEM_AI_REPO=PelayoU/SEM-AI .venv/bin/python scripts/dogfood/create_projects_v2_adr.py
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from engine.adapters import GitHubAdapter, load_config  # noqa: E402
from engine.core import api  # noqa: E402
from engine.core.catalog import NodeType, Status  # noqa: E402
from engine.core.permissions import Role  # noqa: E402


PARENT_ID = "#23"  # C5 — GitHub as unified backend

ADR_TITLE = "Projects v2 belongs to the adopter; framework writes only Issues + labels + body"

ADR_BODY = """## Map

- Parent: #23 (C5 — Use GitHub as unified backend with no extra infrastructure)
- Related: #2 (ADR-001 — All graph nodes as GitHub Issues; this ADR refines the storage boundary that ADR-001 originally framed); #28 (C10 — Adopter-customizable methodology layer; operational data lives there); #29 (ADR — methodology boundary; same partition principle applied to a different axis)

## Status

accepted

## Context

ADR-001 (#2) named Projects v2 custom fields (Related, Supersedes, Superseded by, Acting role, Holistic dimensions) as part of the framework's storage layer. Honest assessment of v0.3 code:

- `set_status` writes only the `status:<value>` label; never touches the Projects v2 Status field
- `set_related` posts a "🔗 Related (set by X)" comment + label; never updates the Projects v2 Related custom field (the adapter's docstring confesses *"deferred to a follow-up commit"*)
- `list_related` returns `()` always
- `supersede` transitions status but doesn't update Projects v2 Supersedes / Superseded by fields
- Acting role lives as `role:<value>` label; never as a Projects v2 field
- Holistic dimensions live as body sections; never as Projects v2 fields
- Issues are NOT auto-added to the Projects v2 board on create_node

In other words: the "Projects v2 custom fields" framing in ADR-001 was *aspirational*; the actual operational truth has always been Issues + labels + body + native sub-issues + Milestones + Releases + PR reviews. Projects v2 in v0.3 is a placeholder board with empty fields.

Beyond visualization, Projects v2 has legitimate scope for **operational data the adopter team manages**: story points / effort estimates, value scoring, sprint / iteration membership, manual backlog ordering, capacity allocation, draft items not yet ready to become Issues. This is methodology-territory per ADR #29 — not framework's to opine on.

Two concerns surfaced during the 2026-05-25 design conversation:

1. **Single source of truth violation risk**. If the framework also writes Projects v2 fields (Status), the Projects v2 default Status column drifts against the framework's `status:<value>` label. Same risk for Related, Supersedes, etc.
2. **Adopter operational layer is unlimited**. Story points / FP / value scoring / sprint cadence vary wildly across teams; the framework cannot bake in a single convention without becoming opinionated methodology (rejected by ADR #29's boundary).

## Decision

**The framework writes ONLY Issues + labels + body content + native sub-issues + Milestones + Releases + PR reviews. That IS the truth of the graph.**

Projects v2 belongs to the adopter and has two complementary sub-layers:

**Visual layer**: kanban / table / roadmap views, configured to filter + group by framework labels (`status:*`, `type:*`, `role:*`, etc.). Views read from the truth; they don't store it. The default Projects v2 "Status" column is not used — kanban columns come from grouping by `status:*` label.

**Operational layer**: adopter custom fields (Story Points, Priority, Iteration, Value Score, etc.) that hold methodology-specific data. Owned by the adopter via their methodology skills (the `.claude/skills/<topic>/SKILL.md` extensibility point of C10).

Cero duplicación: each data point has ONE owner. Their union is the complete planning + execution truth.

**Phased rollout:**

**v0.4 (next release): ship pure visual layer.**

- `setup-github-project.sh` provisions labels (already does) + creates the Projects v2 board + creates 4 recommended views grouping/filtering by framework labels:
  - Discovery — `type:feature label:experiment`, group by parent capability
  - Delivery — `type:feature -label:experiment`, group by parent capability
  - Risk surface — Issues grouped by a derived dimension (from Holistic dimensions sections)
  - Map by parent — Issues grouped by `parent:*` label (the sub-issue tree)
- Adapter cleanup: `set_related` uses labels + body cross-references; the "🔗 Related" comment fallback is deprecated; unused GraphQL plumbing paths that touched custom fields are removed
- Setup script no longer creates Projects v2 custom field placeholders (Related, Supersedes, Superseded by, Acting role, Holistic dimensions) — those were aspirational and never populated; their data lives elsewhere
- README documents the partition explicitly: "Projects v2 is your layer; framework writes labels; views read from labels; delete the default Status column and group by `status:*` label instead"
- Cero new MCP tools, cero new engine surface for operational data — the framework stays minimal

**v0.5+ (demand-driven): add operational layer passthrough when adopters need it.**

When the first adopter requests value-scored backlog / story-point-aware queries / sprint-aware filtering, add to the adapter + MCP:

- `get_project_v2_fields(node_id) -> dict[str, Any]` — opaque read of all custom field values for this Issue on the configured Project board
- `set_project_v2_field(node_id, field_name, value)` — opaque write of a single field value

The passthrough is **opaque** — the framework does not interpret field semantics. The adopter's methodology skill knows what "Story Points" means and how to compute it; the framework just shuttles values.

This is a small addition (~100 LOC + GraphQL plumbing) but worth deferring until: (a) a real adopter requests it, and (b) at least one reference methodology skill exists to consume it. Building the passthrough without a methodology skill ecosystem to use it is premature.

## Consequences

**What becomes easier:**

- Single source of truth: each data point has a clear owner; cero drift risk between Issue labels and Projects v2 fields
- Framework stays minimal in v0.4 — no GraphQL writes runtime, no opinion about story points / value scoring / sprint conventions
- Methodology-blind discipline (ADR #29) extends cleanly: the operational layer IS methodology, lives in adopter skills, framework provides primitives only
- Adopters get a useful Projects v2 board out of `semia init` (4 working views grouping by framework labels) without the framework over-promising operational features it can't deliver
- The deferred passthrough work is small and well-defined; can land in v0.5 once demand surfaces

**What becomes harder:**

- Adopters wanting story points / value scoring / sprint-aware features in v0.4 have to either (a) build their own methodology skill that talks to gh CLI directly, or (b) wait for v0.5+
- The Projects v2 default Status column must be deleted or ignored (the README is the only enforcement); adopters who don't read the README may end up with two Statuses (label + Project field) drifting
- ADR-001 (#2) was implicitly relying on Projects v2 fields that this ADR now removes from framework's scope; that ADR's body should be updated (a follow-up) to remove the aspirational custom fields framing

**What is now locked in:**

- Cero duplicación between Issues and Projects v2 fields for framework-owned data
- Projects v2 default Status field is NOT used by the framework; kanban columns are label-grouped
- Operational fields (story points, value scoring, etc.) are out of framework scope — adopter methodology only
- v0.4 deliverable: pure visual layer; v0.5+ adds operational passthrough when adopter demand pulls

## Security attributes

N/A — partition decision, no security surface. Projects v2 access inherits the adopter's GitHub permissions; no framework-introduced security responsibility.

## Alternatives considered

- **Modelo A: framework doesn't touch Projects v2 at all (no setup automation).** Rejected: gives adopters an empty Projects tab; bad UX for `semia init`; misses the easy win of pre-configured views.

- **Modelo B: framework writes Projects v2 fields runtime (full GraphQL plumbing for Status / Related / Supersedes / etc.).** Rejected: implementation cost (400-600 LOC), ownership confusion (two sources of truth — label vs field), double-truth drift risk, and requires `project` token scope that many adopters lack.

- **Modelo C with full v0.4 scope (visual + operational passthrough in one release).** Rejected pro tem: passthrough is small (~100 LOC) but the methodology skill ecosystem to USE it isn't there yet (no adopters with their own value-scoring / story-point skills); building speculatively risks over-fitting to imagined adopter conventions. Defer to demand.

- **Bake story points / FP / value scoring into the framework directly.** Rejected: same line as ADR #29 (methodology boundary) — these are procedural methodology choices that vary across teams; baking one in alienates teams using another.
"""


def main() -> int:
    cfg = load_config()
    adapter = GitHubAdapter(cfg)

    print(f"Target repo: {cfg.repo}")
    print()

    existing_adrs = adapter.query_issues(type=NodeType.ADR)
    for node in existing_adrs:
        if node.title == ADR_TITLE:
            print(f"[exists] ADR already on the graph: {node.id} ({node.title!r})")
            return 0

    print(f"==> Creating ADR under parent {PARENT_ID}")
    print(f"    title: {ADR_TITLE!r}")

    node = api.create_node(
        adapter,
        type=NodeType.ADR,
        parent_id=PARENT_ID,
        title=ADR_TITLE,
        body=ADR_BODY,
        status=Status.ACCEPTED,
        acting_role=Role.ARCHITECT,
    )
    print(f"==> Created {node.id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
