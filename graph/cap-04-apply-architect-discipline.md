---
category: capability
id: cap-04-apply-architect-discipline
parent: "[[goal-01-self-bootstrap-validation]]"
status: draft
mvp: go
created: 2026-05-14
updated: 2026-05-14
---

# Capability 04 — Apply audited Architect discipline

> Authored via `po-capabilities`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54. MVP filter: slide 69. Cagan four risks: slide 64.

## Statement (slides 97–99 form)

In order to **apply rigorous, citable architecture, methodology, reuse, and performance discipline to a project** (parent goal [[goal-01-self-bootstrap-validation]] — the 5-role-authorship M-criterion requires Architect contribution, particularly for [[cap-11-adr-capture]] — also serves [[goal-03-portability-proof]]),
as **anyone running a software engineering effort under SEM-IA in an Architect capacity**,
I want **the ability to draft or audit architecture against Capers Jones's seven fundamental topics and the Zachman 6×6 schema; select a development methodology against a 5-axis suitability matrix; design a reusability strategy across the 15 reusable artifact types; certify reusable materials against the 11-supporting-practice gate; and run performance analysis with profiling, instrumentation, and the perf↔quality↔security overlap**.

## Implementation-agnostic test

- **Implementation A** (current): 5 Architect skills under `.claude/skills/architect-*/SKILL.md` applied via skill invocation by the Architect agent; ADRs as the artifact class for capturing architectural decisions.
- **Implementation B** (alternative): same discipline as a human architectural-design playbook; ADRs as long-form documents in a corporate wiki; methodology selection via a spreadsheet rubric.

A third plausible: an Enterprise Architect specialization splits off as a Tier-2.5 role for >500-application portfolios per `sem-role-catalog.md`. The capability is *audited Architect discipline being available*, not the specialization level.

## MVP Go / No-go

- **Value risk:** Without this capability, architectural decisions go unrecorded, methodologies are fashion-driven, reuse is uncertified (±300% ROI swing), and performance is treated separately from quality and security (anti-pattern per Jones BP #39).
- **Usability risk:** Moderate — Architect skills are concentrated knowledge requiring careful application; size-tier scaling (Table 7-7) mitigates over-engineering on small projects.
- **Viability risk:** Proven — all 5 Architect skills implemented and cited against Jones BPs #9 / #14 / #26 / #27 / #39 + Ch 7 + Ch 9 Table 9-23.
- **Business viability risk:** N/A.

**Decision: Go** — required for G1 (Architect must contribute) and to feed [[cap-11-adr-capture]].

## Non-overlap with sibling capabilities

- Sibling: [[cap-02-role-scoped-agents]] — adjacent. cap-02 is the role-boundary property; this is what the Architect role enables.
- Siblings: [[cap-03-apply-po-discipline]], [[cap-05-apply-qa-discipline]], [[cap-06-apply-developer-discipline]], [[cap-07-apply-devops-discipline]] — same shape, different role.
- Sibling: [[cap-11-adr-capture]] — closely adjacent. This capability is *the Architect's discipline being applicable*; cap-11 is *the artifact class (ADR) that captures the decisions taken under this discipline*.

## Non-coverage

- **Not about specific architectural choices.** The capability is *the discipline being applicable*; the choices themselves (SOA vs monolith for SEM-IA, etc.) are content authored by Architect at feature/ADR time.
- **Not about Enterprise Architect specialization.** Tier-2.5 emergence for >500-application portfolios is out-of-current-scope.
- **Not about out-of-bibliography frameworks.** Bass / Ford / Ousterhout / Martin / Nygard ADRs are convention pointers per the Architect agent definition, not Jones-anchored authority. The capability respects this flagging.

## Source

- Skill: `po-capabilities`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54, slide 69; `gisf-discovery.pdf` slides 97–99.
- Cagan four risks: `gisf-life-cycle.pdf` slide 64.
- Architect agent definition: `.claude/agents/architect.md`.
- 5 Architect skills under `.claude/skills/architect-*/SKILL.md` are the features delivering this capability.
- Anchoring sources via skills: Capers Jones BPs #9 / #14 / #26 / #27 / #39; Jones Ch 7 § Software Architecture (pp. 470–475, 7 fundamental topics + Table 7-7); Ch 9 Table 9-23 (architect assignment scope + impact).
