---
category: story
id: story-056-A-no-loc-no-cost-per-defect
parent: "[[feature-056-qa-measurements-skill]]"
artifacts:
  - "[[.claude/skills/qa-measurements/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 056-A — LOC and cost-per-defect explicitly excluded

> Parent: [[feature-056-qa-measurements-skill]].

As **QA setting up the measurement program**, I want **LOC and cost-per-defect explicitly excluded as primary metrics**, so that **I don't inherit the malpractice patterns Jones names (LOC penalises high-level languages; cost-per-defect makes buggy software look better)**.

## Conditions of Satisfaction

- Primary size metric is function points.
- LOC appears (if at all) only as secondary code-density metric.
- Cost is normalised per FP, not per defect.

## INVEST self-check

✅ I · ✅ N · ✅ V · ✅ E · ✅ S · ✅ T (skill prescribes; metric definitions verify).

## Source

GISF slides 124, 128, 125. Parent: [[feature-056-qa-measurements-skill]].
