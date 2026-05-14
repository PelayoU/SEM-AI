---
category: capability
id: cap-03-apply-po-discipline
parent: "[[goal-01-self-bootstrap-validation]]"
status: draft
mvp: go
created: 2026-05-14
updated: 2026-05-14
---

# Capability 03 — Apply audited Product / Business Analysis / Project Management discipline

> Authored via `po-capabilities`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54. MVP filter: slide 69. Cagan four risks: slide 64.

## Statement (slides 97–99 form)

In order to **apply rigorous, citable product, business analysis, and project management discipline to a project without staffing three separate roles** (parent goal [[goal-01-self-bootstrap-validation]] — the current bootstrap is exercising this capability — also enables [[goal-02-tfm-public-artifact]] and [[goal-03-portability-proof]]),
as **anyone running a software engineering effort under SEM-IA in a PO capacity**,
I want **the ability to author the project's vision, goals, capabilities, features, stories, specs; assess value and risk; discover and validate requirements; involve users at appropriate scale; control scope changes; size, estimate, plan, track, and benchmark — each grounded in audited primary sources (Cagan, Capers Jones, GISF UC3M, Cohn, Patton, Cucumber)**.

## Implementation-agnostic test

- **Implementation A** (current): 15 PO skills under `.claude/skills/po-*/SKILL.md`, each with formal criteria + workflow + citations, applied via skill invocation by the PO agent (super-PO model: PM + Product Leader + BA + PM-project absorbed).
- **Implementation B** (alternative): same discipline encoded as a human checklist / textbook chapters / decision-rule database; applied manually by a human PO without an AI agent.

A third plausible: discipline distributed across multiple specialist agents (separate BA, separate PM) rather than a fused super-PO. The capability is *audited PO/BA/PM discipline being available*, not the role-fusion choice (which is SEM-IA's Cagan-empowered implementation per the role catalog).

## MVP Go / No-go

- **Value risk:** Without this capability, project work proceeds on opinion rather than method. Highest-value capability for product-level rigor; the entire G1 bootstrap rests on it.
- **Usability risk:** Moderate — 15 skills is a lot to know about; the agent's workflow (step 2: match-to-skill via description triggers) mitigates this.
- **Viability risk:** Proven — all 15 PO skills implemented, citations audited, super-PO fusion Cagan-consistent per `sem-role-catalog.md`.
- **Business viability risk:** N/A.

**Decision: Go** — foundational to the entire roadmap.

## Non-overlap with sibling capabilities

- Sibling: [[cap-02-role-scoped-agents]] — adjacent. cap-02 is the *property* (role boundaries exist); this is *what the PO role enables*.
- Siblings: [[cap-04-apply-architect-discipline]], [[cap-05-apply-qa-discipline]], [[cap-06-apply-developer-discipline]], [[cap-07-apply-devops-discipline]] — same shape, different role. Together with this capability they cover the 5 implemented role disciplines.

## Non-coverage

- **Not about how the agent reasons internally.** Skill execution is implementation; the capability is *that the discipline is available*.
- **Not about role-fusion design.** Whether PO absorbs BA + PM (Cagan-empowered, SEM-IA's choice) or splits is design decision, not capability. Tier-4 emergence cases are documented separately.
- **Not about applying skills outside software engineering.** Scope is SE.

## Source

- Skill: `po-capabilities`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54, slide 69; `gisf-discovery.pdf` slides 97–99.
- Cagan four risks: `gisf-life-cycle.pdf` slide 64.
- PO agent definition: `.claude/agents/product-owner.md` (super-PO fusion).
- 15 PO skills under `.claude/skills/po-*/SKILL.md` are the features delivering this capability.
- Anchoring sources via skills: Cagan *Inspired/Empowered* (via GISF); Capers Jones BPs #6 / #11 / #12 / #15 / #16 / #17 / #18 / #19 / #31 / #32 / #33; GISF UC3M slides; Cohn (story format via GISF); Patton (story mapping via GISF); Cucumber Gherkin reference.
