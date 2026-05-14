---
category: feature
id: feature-046-po-cost-estimating-skill
parent: "[[cap-03-apply-po-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 046 — Skill: `po-cost-estimating`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/po-cost-estimating/SKILL.md`. Delivers part of [[cap-03-apply-po-discipline]].

## What it delivers

Lets the PO estimate effort / cost / schedule / quality using FP-driven automated tooling (COCOMO II, KnowledgePlan, SEER, SLIM, Price-S, SoftCost, CHECKPOINT) — mandatory above 10 k FP per BP #16 (manual = malpractice) — with historical benchmarks as defense against politically-driven overrides.

## Stories (children)

- [[story-046-A-automated-tools-above-10kfp]] — As a PO above 10 k FP, I want at least one automated estimator (with manual cross-check), so the estimate is defensible against political pressure.

## Spec sibling

- [[spec-046-po-cost-estimating-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Absorbed PM scope per [[adr-006-super-po-fusion]].

## Source

- Anchoring authority: Capers Jones BP #16 (pp. 79–81); historical benchmarks BP #31; critical-topic Ch 1 p. 19.
- Substrate evidence: `.claude/skills/po-cost-estimating/SKILL.md`.
