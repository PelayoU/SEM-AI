---
category: story
id: story-054-A-perf-as-architecture-not-tuning
parent: "[[feature-054-architect-performance-analysis-skill]]"
artifacts:
  - "[[.claude/skills/architect-performance-analysis/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 054-A — Performance budgeted at design stage, not patched at code stage

> Parent: [[feature-054-architect-performance-analysis-skill]].

As an **Architect**, I want **performance budgeted at design stage (Jones Ch 7 topic 6: performance attributes)**, so that **optimisation isn't a last-mile code patch order-of-magnitude more expensive**.

## Conditions of Satisfaction

- Performance budget (latency / throughput / memory / MTTF) declared at architecture phase.
- Instrumentation hooks designed in, not bolted on.

## INVEST self-check

✅ I · ✅ N · ✅ V · ✅ E · ✅ S · ✅ T (skill prescribes; architecture-design event applies).

## Source

GISF slides 124, 128, 125. Parent: [[feature-054-architect-performance-analysis-skill]].
