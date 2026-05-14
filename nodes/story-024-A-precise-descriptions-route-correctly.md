---
category: story
id: story-024-A-precise-descriptions-route-correctly
parent: "[[feature-024-agent-description-dispatch-triggers]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 024-A — Precise agent descriptions route work correctly

> Parent: [[feature-024-agent-description-dispatch-triggers]].

## Cohn statement

As a **calling agent describing work to dispatch**, I want **descriptions to be precise trigger phrases rather than vague summaries**, so that **dispatch routes to the right specialist on the first try**.

## Conditions of Satisfaction

- Every `.claude/agents/<role>.md` has a `description:` with concrete trigger phrases.
- Dispatch mis-routing rate negligible in practice.

## INVEST self-check

✅ I · ✅ N · ✅ V (low mis-dispatch rate) · ✅ E · ✅ S · ✅ T (observed routing accuracy).

## Source

- GISF slides 124, 128, 125.
- Parent feature: [[feature-024-agent-description-dispatch-triggers]].
