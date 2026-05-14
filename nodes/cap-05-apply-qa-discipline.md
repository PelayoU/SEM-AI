---
category: capability
id: cap-05-apply-qa-discipline
parent: "[[goal-01-self-bootstrap-validation]]"
status: draft
mvp: go
created: 2026-05-14
updated: 2026-05-14
---

# Capability 05 — Apply audited QA discipline (independent SQA, inspections, testing, DRE)

> Authored via `po-capabilities`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54. MVP filter: slide 69. Cagan four risks: slide 64.

## Statement (slides 97–99 form)

In order to **apply rigorous, citable quality discipline — measured by defect removal efficiency, anchored in the IBM-model SQA independence imperative — to a project** (parent goal [[goal-01-self-bootstrap-validation]] — 5-role-authorship requires QA contribution and G1-B citation audit method is QA-scope — also serves [[goal-03-portability-proof]]),
as **anyone running a software engineering effort under SEM-IA in a QA capacity**,
I want **the ability to design or audit the SQA program against Jones BP #35 (12-role inventory, independence from dev chain, mandatory >2,500 FP); design the measurement program with the 9 valid measures + refuse the 2 forbidden metrics (LOC, cost-per-defect); plan the inspection cadence (Fagan-origin, 65–85% DRE); compose the testing portfolio (20+ forms, ≥3 typically applied); and assemble the prevention+removal stack to reach >95% cumulative DRE**.

## Implementation-agnostic test

- **Implementation A** (current): 5 QA skills under `.claude/skills/qa-*/SKILL.md` applied via the QA agent (which reports independently per CLAUDE.md, modelling the IBM Ch 5 p. 282 independence imperative).
- **Implementation B** (alternative): same discipline encoded as ISO 9000 / CMMI process documentation; applied by a human SQA group reporting to a senior VP of quality outside dev management.

A third plausible: discipline distributed across an inspection-moderator specialist + a tester specialist + an SQA manager (Jones Table 9-23 split). The capability is *audited QA discipline being available*, not the specialization split.

## MVP Go / No-go

- **Value risk:** Without this capability, quality drops to the U.S. average ~85% DRE band — below the 95% safe minimum. The vision's *"audit becomes inspection of the substrate"* claim depends on this discipline being applicable to the substrate itself.
- **Usability risk:** Moderate — independence imperative is structural, not merely advisory; misimplementation collapses the function (50% test-only / 10% none / 5% figurehead patterns per Jones Ch 5).
- **Viability risk:** Proven — all 5 QA skills implemented; bibliography anchored on Jones BPs #30 / #35 / #36 / #37 + Ch 5 + Ch 9 Tables 9-22 + 9-23.
- **Business viability risk:** N/A.

**Decision: Go** — required for G1 (citation audit, 5-role coverage) and reinforces every other capability that needs verification.

## Non-overlap with sibling capabilities

- Sibling: [[cap-02-role-scoped-agents]] — adjacent. cap-02 is the role-boundary property; this is what QA enables.
- Siblings: [[cap-03-apply-po-discipline]], [[cap-04-apply-architect-discipline]], [[cap-06-apply-developer-discipline]], [[cap-07-apply-devops-discipline]] — same shape, different role.
- Sibling: [[cap-08-citation-discipline]] — adjacent. Citation discipline is *the substrate property*; QA's inspection method (G1-B) is *how that property is verified at audit time*.

## Non-coverage

- **Not about specific quality decisions.** The capability is *the discipline being applicable*; specific inspections / test plans / DRE projections are content authored by QA at feature time.
- **Not about quality-as-testing-only.** The 50%-of-organizations-use-SQA-label-on-testing-org failure pattern is explicitly excluded per Jones Ch 5.
- **Not about appraisals.** Defect data must not feed individual appraisals (Jones BP #36 p. 125).

## Source

- Skill: `po-capabilities`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54, slide 69; `gisf-discovery.pdf` slides 97–99.
- Cagan four risks: `gisf-life-cycle.pdf` slide 64.
- QA agent definition: `.claude/agents/qa.md` (independence imperative quoted from Jones Ch 5 p. 282).
- 5 QA skills under `.claude/skills/qa-*/SKILL.md` are the features delivering this capability.
- Anchoring sources via skills: Capers Jones BPs #30 / #35 / #36 / #37; Jones Ch 5 § SQA Organizations (pp. 342–348) + p. 282; Ch 9 Table 9-22 (80 defect removal activities) + Table 9-23 (role impact).
