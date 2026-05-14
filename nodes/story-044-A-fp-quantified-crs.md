---
category: story
id: story-044-A-fp-quantified-crs
parent: "[[feature-044-po-change-control-skill]]"
artifacts:
  - "[[.claude/skills/po-change-control/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 044-A — Every CR quantified in function points

> Parent: [[feature-044-po-change-control-skill]].

As a **PO receiving a "small change" request**, I want **every CR FP-quantified before CCB review**, so that **the 10-FP re-estimation gate is objective rather than political**.

## Conditions of Satisfaction

- CR carries an FP delta.
- Above 10 FP triggers re-estimation (cross-link `po-cost-estimating`).

## INVEST self-check

✅ I · ✅ N · ✅ V · ✅ E · ✅ S · ✅ T (skill prescribes; project enforces at CR intake).

## Source

GISF slides 124, 128, 125. Parent: [[feature-044-po-change-control-skill]].
