---
category: feature
id: feature-064-developer-maintenance-skill
parent: "[[cap-06-apply-developer-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 064 — Skill: `developer-maintenance`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/developer-maintenance/SKILL.md`. Delivers part of [[cap-06-apply-developer-discipline]].

## What it delivers

Lets the Developer maintain / enhance legacy code under Jones BP #48's 23-work-type taxonomy (major / minor enhancements, defect repairs, complexity analysis, dead-code removal, error-prone-module surgery, refactoring, renovation, migration, conversion, retirement, etc.) and the 14+ legacy best-practice inventory. Renovate-before-enhance rule; 5 %-of-modules / 50 %-of-defects error-prone surgery.

## Stories (children)

- [[story-064-A-renovate-before-enhance]] — As a Developer about to enhance aging legacy, I want renovation first (complexity + error-prone modules + dead code), so the enhancement doesn't inherit the legacy's debt.

## Spec sibling

- [[spec-064-developer-maintenance-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Maintenance is the dominant expense of the software industry per Jones BP #48 p. 163.

## Source

- Anchoring authority: Capers Jones BP #48 (pp. 161–164); BP #28 practices 12–13; BP #47 cross-link; Ch 5 Table 5-2; Ch 9 Table 9-22.
- Substrate evidence: `.claude/skills/developer-maintenance/SKILL.md`.
