# ADR-007 — Holistic dimensions are the risk surface

- **Status**: accepted
- **Date**: 2026-05-24
- **Supersedes**: —
- **Superseded by**: —

## Context

Modern product management literature articulates three principles that elevate a team from "feature factory" to "product organization":

1. **Solve problems, not implement features.** Roadmaps for conventional products are about production; strong teams ensure the solution resolves the underlying problem, and measure by business results, not by features shipped.
2. **Define and design collaboratively, not sequentially.** Product, design, and engineering work hand-in-hand on a "give and take" path; the older model where PM defines, designer designs, engineering implements (each person living with the previous one's constraints) is rejected.
3. **Address risks in advance, not at the end.** Validate value risk (will customers buy it?), usability risk (can users figure out how to use it?), viability risk (can our engineers build it sustainably with the skills and technology we have?), and business viability risk (does it work for sales, marketing, finance, legal, support, …?) before deciding to build.

Two of these three are already covered by decisions already taken:

- **Principle 1** is materialized by the spine encoding outcomes (not outputs) at the goal/capability level (`goal.Outcome statement` is behavioral, not output-shaped; explicit in ADR-005 + recent commit tightening goal template). ADR-005 articulates value vs output explicitly; ADR-006 separates intent (delivery vs experiment) — both are operationalisations of "solve problems, not produce features".

- **Principle 2** is materialized by the `consult` mechanism in every agent.md (a role consults the others when authoring; consult returns information, not authorship — the active role integrates) and by ADR-002 (the graph is not constructed top-down sequentially; it loops, and bottom-up signals refine upper levels via `supersede` and `anchor pending`). Collaboration is the operative norm, not a methodology to opt into.

**Principle 3 is what this ADR records.** And it does so by making explicit a connection that, once seen, is structural: **the four canonical risk classes of the modern approach are a direct projection of the five holistic dimensions of ADR-003**.

## Decision

The five holistic dimensions of ADR-003 (Technology, UX design, Monetization, Acquisition, Offline experience, plus Functionality as the base) are not only the **design lens** of the spine — they are also the **risk surface** of any feature.

**An unvalidated dimension is a risk assumed without knowing.** If the team only looks at the functional / technical dimensions when designing a feature, the team only sees functional / technical risks; the rest are absorbed silently and surface as surprises at launch (or after).

### The mapping

The four canonical risk classes name the same surface from the angle of *what can go wrong*; the five dimensions name it from the angle of *what to design for*. They are two readings of the same structure:

| Risk class (modern approach principle 3) | Holistic dimension(s) (ADR-003) | What goes unvalidated |
|---|---|---|
| **Value risk** — will customers buy / adopt it? | Monetization (primarily) + Functionality | Pricing, willingness-to-pay, value proposition, problem-solution fit |
| **Usability risk** — can users figure out how to use it? | UX design | Flows, interactions, copy, accessibility, trust, recovery from error |
| **Viability risk** — can our engineers build and sustain it? | Technology | Infrastructure, scale, technical stack fit, operational complexity, team skills, technical debt cost |
| **Business viability risk** — does it work for sales, marketing, finance, legal, support, ops? | Acquisition + Offline experience | Channel strategy, sales narrative, support capacity, regulatory compliance, finance modelling, operational absorption |

The mapping is **not the framework's invention**; it is the recognition that two literatures (product holistic + modern risk management) describe the same surface from two angles.

### What this changes operationally

1. **The Holistic dimensions section in spine templates** (vision, goal, capability, feature — per ADR-003) gains a tighter reading: each slot is a **design slot AND a risk-surface slot**. A slot left silent is a risk absorbed; a slot marked `N/A` must explicitly justify why this dimension does not apply at this level.

2. **The Uncertainty addressed slot in the feature template** (per ADR-006) gains a mapping cue: when populated, it names which dimension(s) the experiment tests. An experimental feature *is* a validation instrument against one or more dimensions. A delivery feature implies the dimensions it covers were already validated.

3. **The Value chain section in the feature template** (per ADR-005) gains a complementary reading: Outcomes observed and Benefits measured are read by dimension. Did monetization metrics move? Did usability adoption move? Did operational metrics absorb the rollout? Each dimension has its own evidence trail post-done.

4. **Pre-build coherence check**: before committing to construction of a significant feature, the team can ask, dimension by dimension: *is this validated? if not, is the feature itself the experiment that validates it, or is there an experiment we should run first?* This is the framework's operationalisation of "validate risks before building".

### What the framework does NOT impose

- **The names** "value risk / usability risk / viability risk / business viability risk" are not made into structural labels. They appear in template comments (as the risk-class reading of the dimensions) and in this ADR, but the spine templates' sections continue to use the dimension names (Technology, UX design, etc.) as headers.
- **No "Risks addressed" slot** is added separately. That would duplicate `Uncertainty addressed` (ADR-006). An experimental feature already declares its uncertainty; the dimension(s) it tests *is* the risk class it validates.
- **No required pre-build risk validation step**. The framework recommends the team look at the surface before committing significant build, but does not enforce a gate. Teams that ship deliveries against already-validated dimensions skip the validation step legitimately; teams whose unknowns dominate ship experiments first.
- **No catalogue of experiment forms** (landing page, concierge, wizard of oz, A/B test, dogfooding…). Those are methodology — the project's methodology skill (if any) supplies them. ADR-006 already names this.

## Principles 1 and 2 — coverage record

This ADR also records, for traceability, that the other two principles of the modern approach are already covered by prior decisions:

| Modern approach principle | Where it lives in the framework |
|---|---|
| **(1)** Solve problems, not implement features | Spine encodes outcomes at goal/capability layers (ADR-001 + ADR-005); `goal.Outcome statement` is behavioral, not output (tightened in commit `bc312ef`); ADR-005 articulates value vs output; ADR-006 separates delivery vs experimental intent |
| **(2)** Define and design collaboratively, not sequentially | `consult` mechanism in every agent.md (cross-role input without authorship transfer); ADR-002's hierarchical loop (construction is not top-down sequential); the role-jurisdiction map in framework SKILL § Working as roles |
| **(3)** Address risks in advance, not at the end | **This ADR.** The five holistic dimensions are the risk surface; an unvalidated dimension is an assumed risk; experimental features (ADR-006) are validation instruments against specific dimensions |

This is not a methodology import — it is the recognition that the framework's existing structure already operationalises the modern approach, and this ADR closes the gap on the only principle that was not yet explicit.

## Alternatives considered

- **A new ADR for each of the three principles.** Rejected — principles 1 and 2 are already covered; writing ADRs that simply re-state existing coverage would inflate the catalog. This ADR includes the coverage record as a section, which is enough.
- **A new "Risks addressed" slot in the feature template, separate from "Uncertainty addressed".** Rejected — duplicates ADR-006. The dimension(s) being tested IS the risk class being validated. One slot is enough.
- **A required pre-build validation gate.** Rejected — the framework prefers "infrastructure available; team decides" over imposed gates. Teams can adopt a gate as project methodology if they want.
- **A catalog of canonical experiment forms (landing page, concierge, etc.).** Rejected — methodology, not infrastructure. The project's methodology skills supply experiment forms; the framework supplies only the structural slot.
- **Renaming the Holistic dimensions section to "Risk surface" or "Design + Risk".** Rejected — the dimensions are *primarily* a design lens; risk surface is the secondary reading. Keep the name, refine the comment.

## Consequences

- `framework/SKILL.md` § The graph: the Holistic dimensions paragraph gains a closing line naming dimensions as both design lens and risk surface, with a pointer to this ADR.
- `node-templates/SKILL.md`: the comment header of every `## Holistic dimensions` section (vision, goal, capability, feature) is refined to state: each slot is a design slot AND a risk-surface slot; silent omission = absorbed risk; mark `N/A` only with explicit reason.
- `node-templates/SKILL.md`: the comment of `## Uncertainty addressed` in the feature template (ADR-006) gains a mapping cue: the four canonical risk classes (value / usability / viability / business viability) map to the dimensions (Monetization / UX design / Technology / Acquisition + Offline experience) respectively; an experimental feature names which dimension(s) it tests.
- Coherence checks (mentioned in ADR-002) can include the pre-build dimension scan: which dimensions are validated, which are assumed, is this feature an experiment to close that gap, or are we shipping blind on assumptions?

## Status

Accepted. The five holistic dimensions of ADR-003 are recognised as the risk surface of any feature; an unvalidated dimension is an assumed risk; the modern approach's principle 3 ("address risks in advance") is operationalised in the framework via the holistic-dimensions lens applied before committing significant build. Principles 1 and 2 of the modern approach are documented as already-covered by prior ADRs.
