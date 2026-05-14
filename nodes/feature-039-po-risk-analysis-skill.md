---
category: feature
id: feature-039-po-risk-analysis-skill
parent: "[[cap-03-apply-po-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 039 — Skill: `po-risk-analysis`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/po-risk-analysis/SKILL.md`. Delivers part of [[cap-03-apply-po-discipline]].

## What it delivers

Lets the PO identify / classify / mitigate project risks using Jones's 14-category empirical inventory + Cagan four risks lens + size-based escalation rules (optional <1k FP / mandatory >10k FP / malpractice >100k FP).

## Stories (children)

- [[story-039-A-sweep-fourteen-categories]] — As a PO at project start, I want to walk Jones's 14-category inventory, so risks aren't silent until they materialise.

## Spec sibling

- [[spec-039-po-risk-analysis-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]].

## Source

- Anchoring authority: Capers Jones BP #17 (pp. 81–83); Cagan four risks via GISF slide 64; critical-topic status Ch 1 p. 19.
- Substrate evidence: `.claude/skills/po-risk-analysis/SKILL.md`.
