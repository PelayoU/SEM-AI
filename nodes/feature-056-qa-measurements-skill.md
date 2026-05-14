---
category: feature
id: feature-056-qa-measurements-skill
parent: "[[cap-05-apply-qa-discipline]]"
artifacts:
  - "[[.claude/skills/qa-measurements/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 056 — Skill: `qa-measurements`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/qa-measurements/SKILL.md`. Delivers part of [[cap-05-apply-qa-discipline]].

## What it delivers

Lets QA design the project's quality and productivity measurement program per Jones BP #30 (9-measure state-of-the-art inventory) with explicit refusal of the 2 forbidden metrics (lines of code, cost-per-defect) that violate economic assumptions. Defines DRE = dev-found / (dev-found + client-found) with fixed post-release window.

## Stories (children)

- [[story-056-A-no-loc-no-cost-per-defect]] — As QA setting up measures, I want LOC and cost-per-defect explicitly excluded as primary metrics, so I don't inherit the malpractice patterns Jones names.

## Spec sibling

- [[spec-056-qa-measurements-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. DRE bands: U.S. average ~85 %, leaders >95 %, top performers 99 %.

## Source

- Anchoring authority: Capers Jones BP #30 (pp. 110–112); BP #35 (severity, COQ); BP #11 (churn).
- Substrate evidence: `.claude/skills/qa-measurements/SKILL.md`.
