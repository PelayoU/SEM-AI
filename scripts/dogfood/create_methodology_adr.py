#!/usr/bin/env python3
"""Bootstrap dogfood Part 5: create the methodology-boundary ADR as an Issue.

Records the boundary between methodology embedded in the framework's
templates + semantic CI library (definitional + mechanically verifiable)
and methodology supplied by the adopter via `.claude/skills/<topic>/SKILL.md`
(procedural + judgement-requiring).

Parent: C10 #28 — Adopter-customizable methodology layer (the spine node
whose scope this decision refines).

Idempotent: skips creation if an ADR with the same title already exists.

Run once:
    SEM_AI_REPO=PelayoU/SEM-AI .venv/bin/python scripts/dogfood/create_methodology_adr.py
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


PARENT_ID = "#28"  # C10 — Adopter-customizable methodology layer

ADR_TITLE = "Framework templates encode definitional product literacy; project methodology layers via skills"

ADR_BODY = """## Map

- Parent: #28 (C10 — Adopter-customizable methodology layer)
- Related: #5 (ADR-004 — invocation model, hooks/MCP/Actions layering) and #9 (ADR-008 — deployable framework, SemVer + extensibility boundary) which already establish the fixed-vs-variable layer split; this ADR refines that split at the methodology layer

## Status

accepted

## Context

The framework's stated position is "ships infrastructure, not methodology": catalog, MCP, hooks, role contracts and semantic CI library are universal; project-specific methodology is supplied by the adopter via `.claude/skills/<topic>/SKILL.md` files (the methodology layer capability, #28).

That position is correct as written but **silently underspecified** at the seam. Several pieces of methodology already live in framework templates today:

- Output / Outcome / Benefit / Value distinction (#6) — embedded in goal & feature templates with negative examples ("Ship feature X" → that's an output)
- Holistic dimensions as design + risk surface (#4 + #8) — embedded in spine templates with 5 slots + 4 risk-class mapping
- Delivery vs experiment intent with sub-type lifecycle (#7) — embedded in feature template via `Uncertainty addressed` slot + per-sub-type expected status
- Probabilistic value chain + learning as guaranteed output (#6) — embedded in feature template's post-done Value chain section

During the 2026-05 dogfood derivation (vision #1 → 8 goals → 10 capabilities) the team applied additional methodology not yet embedded in the framework:

- **SMART** (Specific / Measurable / Achievable / Relevant / Time-bound) — goals had to be retrofitted with Time-bound checkpoints for the continuous ones (G2 / G3 / G7)
- **Patton goal-driven** (what, not how) — friction surfaced when capabilities tilted toward solutions
- **Stakeholder framing** (`In order to [outcome], as [STAKEHOLDER], I want { capabilities }`) — the goal template lacked a `## Stakeholder` section; goals were authored without naming the beneficiary
- **Why-stack** (pop "why?" to distinguish solution from real goal — the "Twitter → talk to users → sell more tickets" example) — applied verbally, not encoded

These four are **not opinionated methodology** like SAFe / LeSS / specific design-sprint protocols. They are **definitional grammar**: SMART (1981) is the de-facto vocabulary across product management literature; the why-stack maps to Toyota's 5-whys (1958); Patton goal-driven is universal product-coaching baseline; stakeholder framing has no school that disputes it.

The seam between framework-embedded and adopter-supplied methodology needs to be made explicit so future framework changes (and adopters) know where to put new methodology.

## Decision

The framework's templates and semantic CI library encode **definitional + mechanically-verifiable** product literacy. The adopter's `.claude/skills/<topic>/SKILL.md` files encode **procedural + judgement-requiring** methodology.

**Boundary test:**
- If a regex / structural / heuristic check in `engine/checks/` can surface the problem reliably → **framework**
- If the problem requires expert judgement, domain context, or methodology school choice → **adopter**

**Inventory of methodology currently embedded in framework templates + checks:**

1. **Output vs outcome distinction** (#6) — goal & feature templates, with negative example
2. **Holistic dimensions as design + risk surface** (#4 + #8) — spine templates, 5 slots + 4 risk-class mapping
3. **Delivery vs experiment intent + sub-type lifecycle** (#7) — feature template, label-slot coherence
4. **Probabilistic value chain + learning as guaranteed output** (#6) — feature template post-done
5. **SMART (Specific / Measurable / Achievable / Relevant / Time-bound)** — *added by this ADR* — goal template Horizon + Acceptance check comments; `engine/checks/goal_smart.py` GS002/GS003 enforce time-bound presence
6. **Stakeholder framing** — *added by this ADR* — goal template `## Stakeholder` section as required slot; `engine/checks/goal_smart.py` GS001 enforces presence
7. **Why-stack / outcome-not-solution test** — *added by this ADR* — goal template Outcome statement comment with the Twitter → tickets example; `engine/checks/goal_smart.py` GS004 detects output-shaped verbs
8. **Capability WHAT vs feature HOW distinction** — *added by this ADR* — capability template Statement comment with coinless trolley vs NFC unlock example; Two implementations section reinforced as anti-solution salvavidas
9. **Anchor-pending pattern + supersede chains** (#3) — graph-level support for bottom-up emergence

**Pieces deliberately NOT embedded** (adopter responsibility):

- Specific value-analysis frameworks (Wardley maps, Lean Canvas, opportunity solution trees)
- Specific story formats (Connextra, INVEST criteria, Jobs to be Done)
- Specific security threat modelling (STRIDE, PASTA, attack trees)
- Specific risk classification methodology beyond the 4 canonical risk classes
- Domain methodology (requirements discovery in fintech vs healthcare vs consumer)
- Estimation / planning techniques (story points, t-shirt sizing, Monte Carlo)
- Specific cycle methodologies (Scrum sprint cadence, Kanban WIP limits, OKR cadence)

## Consequences

**What becomes easier:**
- New methodology candidates have a boundary test: "does it pass the mechanically-verifiable check?" If yes, framework embedding candidate; if no, adopter territory
- Adopters know which methodology gaps they need to fill (anything not in the inventory above)
- Framework contributors know when they're crossing into opinionated territory (proposing STRIDE-based threat modelling in templates would be over the line)
- The PM agent remains methodology-blind in its identity (no behavioural change in `.claude/agents/product-manager.md`), yet a PM operating under the framework cannot silently produce a goal without Stakeholder or without time-bound checkpoint — the template + check do the work

**What becomes harder:**
- The framework is subtly more opinionated than "methodology-blind" suggested. We are opinionated in favour of SMART over NCT, in favour of the why-stack over alternatives, etc. The opinionated stance is defensible (these are the most established / widely-taught baselines) but it is not invisible
- Adopters who use a different framework (e.g. NCT-shaped goals) would need a methodology skill that overrides or extends the embedded literacy

**What is now locked in:**
- The capability `C10 — Adopter-customizable methodology layer` (#28) is the framework's stated extensibility point for procedural methodology; this ADR refines what flows through that capability vs what remains in the framework's templates
- Adding new methodology to framework templates is now an explicit framework-level decision (a new ADR), not an incremental commit
- `engine/checks/` is now an active surface for embedded literacy enforcement; further checks (e.g. capability WHAT-vs-HOW heuristic, vision Value-ambition shape) are framework-level changes that need their own ADRs if they encode new methodology

## Security attributes

N/A — methodology boundary, no security surface.

## Alternatives considered

- **Keep "methodology-blind" as stated, embed nothing methodological in templates.** Rejected: untrue to the current state (output/outcome, Holistic dimensions, delivery/experiment, value chain are all already methodology in templates). Pretending otherwise causes drift between docs and behaviour.

- **Push ALL methodology to adopters' `.claude/skills/`, including the four already-embedded pieces.** Rejected: removes the structural guarantees the framework currently offers (Holistic dimensions as risk surface forces consideration at planning time; Value chain post-done forces learning extraction). Adopters who don't author a methodology skill would lose those guarantees, contradicting C10's "defaults work for solo devs out of the box".

- **Embed more methodology (specific value-analysis framework, specific story format).** Rejected: at this level the framework becomes opinionated about *how to do product work*, which is the line we don't want to cross. SMART / Patton / Stakeholder / why-stack are *definitional*; specific value-analysis methods are *procedural*.

- **Give the PM agent some methodology directly** (modify `.claude/agents/product-manager.md` to teach SMART, Stakeholder framing, etc.). Rejected: violates the role-identity / methodology-blind separation. The right home is the template + check (declarative, persists across agent changes, applies uniformly whether the operator is human-PM or AI-PM).
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
