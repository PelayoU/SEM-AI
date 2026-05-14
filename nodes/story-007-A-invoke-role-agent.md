---
category: story
id: story-007-A-invoke-role-agent
parent: "[[feature-007-five-role-agent-identities]]"
artifacts:
  - "[[.claude/agents/product-owner.md]]"
  - "[[.claude/agents/architect.md]]"
  - "[[.claude/agents/qa.md]]"
  - "[[.claude/agents/developer.md]]"
  - "[[.claude/agents/devops.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 007-A — Invoke any of the 5 role-agents

> Parent: [[feature-007-five-role-agent-identities]].

## Cohn statement

As a **human**, I want **to invoke any of the 5 role-agents with `claude --agent <role>`**, so that **I engage role-scoped expertise from the first turn**.

## Conditions of Satisfaction

- 5 `.claude/agents/<role>.md` files exist (PO, Architect, QA, Developer, DevOps).
- `claude --agent product-owner` (or similar) loads the agent's identity + CLAUDE.md.

## INVEST self-check

✅ I · ✅ N · ✅ V (role-scoped reasoning from turn zero) · ✅ E · ✅ S · ✅ T (invoke; observe role-scoped behaviour).

## Source

- GISF `gisf-delivery-backlog-management.pdf` slides 124, 128, 125.
- Parent feature: [[feature-007-five-role-agent-identities]].
