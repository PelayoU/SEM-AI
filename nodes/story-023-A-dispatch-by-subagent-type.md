---
category: story
id: story-023-A-dispatch-by-subagent-type
parent: "[[feature-023-task-tool-integration]]"
artifacts:
  # No concrete substrate — this node describes an abstract property
  # without a single artefact owner. See CLAUDE.md § Substrate traceability.
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 023-A — Dispatch a specific role-agent by name via `subagent_type`

> Parent: [[feature-023-task-tool-integration]].

## Cohn statement

As a **calling agent**, I want **to dispatch a specific role-agent by name via Task's `subagent_type` parameter**, so that **the right specialist is engaged without ambiguity**.

## Conditions of Satisfaction

- `subagent_type: <role>` resolves to the matching `.claude/agents/<role>.md`.
- Dispatched agent loads its own identity + CLAUDE.md.

## INVEST self-check

✅ I · ✅ N · ✅ V (deterministic routing) · ✅ E · ✅ S · ✅ T (Phase 1 PO→Architect dispatch demonstrated).

## Source

- GISF slides 124, 128, 125.
- Parent feature: [[feature-023-task-tool-integration]].
