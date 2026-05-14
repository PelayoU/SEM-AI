---
category: feature
id: feature-047-po-project-planning-skill
parent: "[[cap-03-apply-po-discipline]]"
artifacts:
  - "[[.claude/skills/po-project-planning/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 047 — Skill: `po-project-planning`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/po-project-planning/SKILL.md`. Delivers part of [[cap-03-apply-po-discipline]].

## What it delivers

Lets the PO build / maintain the project plan — WBS, activity network, critical path, historical-benchmark calibration, multi-release segmentation, time-allotted for requirements / change handling / inspections / testing / risk reaction — using Jones BP #15's 11 planning best-practice elements and GISF multilevel hierarchical planning horizons.

## Stories (children)

- [[story-047-A-allot-time-for-the-five-skipped]] — As a PO drafting a plan, I want explicit allotments for the 5 most-skipped categories (requirements analysis, change handling, inspections, testing, risk reaction), so the plan doesn't hide them in a 10 % buffer.

## Spec sibling

- [[spec-047-po-project-planning-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Absorbed PM scope per [[adr-006-super-po-fusion]].

## Source

- Anchoring authority: Capers Jones BP #15 (pp. 77–79); multilevel horizons GISF `gisf-delivery-planning.pdf` slide 150; critical-topic Ch 1 p. 19.
- Substrate evidence: `.claude/skills/po-project-planning/SKILL.md`.
