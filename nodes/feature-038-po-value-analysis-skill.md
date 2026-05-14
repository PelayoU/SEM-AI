---
category: feature
id: feature-038-po-value-analysis-skill
parent: "[[cap-03-apply-po-discipline]]"
artifacts:
  - "[[.claude/skills/po-value-analysis/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 038 — Skill: `po-value-analysis`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/po-value-analysis/SKILL.md`. Delivers part of [[cap-03-apply-po-discipline]].

## What it delivers

Lets the PO assess tangible (10 financial items) and intangible (9 items) value of a capability or feature using Jones BP #18 framework + Cagan four risks lens, with value-point scaling for cross-comparison and ROI computation.

## Stories (children)

- [[story-038-A-prioritise-by-value-not-loudest-voice]] — As a PO with competing capabilities, I want a quantitative value analysis, so prioritisation is value-weighted rather than political.

## Spec sibling

- [[spec-038-po-value-analysis-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]].

## Source

- Anchoring authority: Capers Jones BP #18 (pp. 83–84); Cagan four risks via GISF `gisf-life-cycle.pdf` slide 64.
- Substrate evidence: `.claude/skills/po-value-analysis/SKILL.md`.
