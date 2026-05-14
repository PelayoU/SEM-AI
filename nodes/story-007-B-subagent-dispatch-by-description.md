---
category: story
id: story-007-B-subagent-dispatch-by-description
parent: "[[feature-007-five-role-agent-identities]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 007-B — Subagent dispatch routes by description match

> Parent: [[feature-007-five-role-agent-identities]].

## Cohn statement

As a **calling agent**, I want **to dispatch a sibling agent via `Task` and have its `description` field trigger the correct match**, so that **cross-role consultation routes automatically without manual role-name lookup**.

## Conditions of Satisfaction

- Each `.claude/agents/<role>.md` carries a `description:` with concrete trigger phrases.
- Task dispatch with `subagent_type: <role>` reaches the right agent.

## INVEST self-check

✅ I · ✅ N · ✅ V (routing automation) · ✅ E · ✅ S · ✅ T (demonstrated in Phase 1 PO→Architect dispatch).

## Source

- GISF `gisf-delivery-backlog-management.pdf` slides 124, 128, 125.
- Parent feature: [[feature-007-five-role-agent-identities]].
