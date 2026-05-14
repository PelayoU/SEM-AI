---
category: capability
id: cap-06-apply-developer-discipline
parent: "[[goal-01-self-bootstrap-validation]]"
status: draft
mvp: go
created: 2026-05-14
updated: 2026-05-14
---

# Capability 06 — Apply audited Developer discipline (coding, reuse, static analysis, unit testing, maintenance)

> Authored via `po-capabilities`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54. MVP filter: slide 69. Cagan four risks: slide 64.

## Statement (slides 97–99 form)

In order to **write and maintain production code under rigorous, citable practice — language selection, complexity ceilings, certified reuse, static analysis, developer-owned testing, legacy renovation** (parent goal [[goal-01-self-bootstrap-validation]] — 5-role-authorship requires Developer contribution; the code-affecting bottom of the backbone passes through Developer — also serves [[goal-03-portability-proof]]),
as **anyone running a software engineering effort under SEM-IA in a Developer capacity**,
I want **the ability to apply Capers Jones's 13 programming best practices when writing new code; consume certified reusable artifacts from the project's reuse library (curated by Architect); run automated static analysis (~87% DRE on coding defects); write and run subroutine / module / unit tests (25–52% DRE depending on discipline); and maintain legacy code under the 23-work-type taxonomy with the renovate-before-enhance rule and error-prone-module surgery**.

## Implementation-agnostic test

- **Implementation A** (current): 5 Developer skills under `.claude/skills/developer-*/SKILL.md` applied via the Developer agent.
- **Implementation B** (alternative): same discipline encoded as a coding standards document, an IDE plugin set (linting + complexity + test-coverage), and a manual code-review checklist; applied by a human Developer without an AI agent.

A third plausible: discipline distributed via TSP / PSP measurement scaffolding (Watts Humphrey, the PSP/TSP unit-testing form reaches 52% DRE vs plain 25%). The capability is *audited Developer discipline being available*, not the methodology overlay.

## MVP Go / No-go

- **Value risk:** Without this capability, the code-affecting bottom of the backbone (specs → code) is unconstrained. Custom-coding without certification is the most expensive option per Jones BP #28 p. 109.
- **Usability risk:** Moderate — 13 practices is comprehensive; cyclomatic complexity ceilings (<10 safe, >20 dangerous) act as a hard rule that flags problems automatically.
- **Viability risk:** Proven — all 5 Developer skills implemented; bibliography anchored on Jones BPs #26 / #28 / #36 / #37 / #48 + Ch 8 + Ch 9 Table 9-22.
- **Business viability risk:** N/A.

**Decision: Go** — required for G1 (5-role coverage + code-affecting artifacts).

## Non-overlap with sibling capabilities

- Sibling: [[cap-02-role-scoped-agents]] — adjacent. cap-02 is the role-boundary property; this is what Developer enables.
- Siblings: [[cap-03-apply-po-discipline]], [[cap-04-apply-architect-discipline]], [[cap-05-apply-qa-discipline]], [[cap-07-apply-devops-discipline]] — same shape, different role.

## Non-coverage

- **Not about specific code.** The capability is *the discipline being applicable*; the code itself is content authored by Developer at story / spec time.
- **Not about pair programming as the entire quality strategy.** Per Jones BP #28 p. 108: pair programming is *"intrinsically inefficient"*; solo + static analysis + peer review is the empirical best practice.
- **Not about static analysis as a substitute for inspection.** Per Jones BP #36: layered combination (inspection + static analysis + testing) is required for >95% DRE; static analysis alone tops 87% on structural defects only.

## Source

- Skill: `po-capabilities`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54, slide 69; `gisf-discovery.pdf` slides 97–99.
- Cagan four risks: `gisf-life-cycle.pdf` slide 64.
- Developer agent definition: `.claude/agents/developer.md`.
- 5 Developer skills under `.claude/skills/developer-*/SKILL.md` are the features delivering this capability.
- Anchoring sources via skills: Capers Jones BPs #26 / #28 / #36 / #37 / #48; Jones Ch 8 § Forms of Programming Defect Prevention (pp. 519–525); Ch 9 Table 9-22 (DRE values per developer-owned activity); SPR language taxonomy (out-of-biblio convention pointer for >700 languages).
