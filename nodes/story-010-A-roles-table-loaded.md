---
category: story
id: story-010-A-roles-table-loaded
parent: "[[feature-010-claude-md-role-scope-section]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 010-A — Roles table loaded at session start

> Parent: [[feature-010-claude-md-role-scope-section]].

## Cohn statement

As **any agent or human in a session**, I want **the CLAUDE.md `## Roles` table loaded at session start**, so that **role boundaries are common knowledge from turn zero, without verbal context transfer**.

## Conditions of Satisfaction

- CLAUDE.md is loaded by the harness automatically at every session start.
- The `## Roles` section enumerates the 5 implemented + 2 planned roles with custody/skills/agent-path/tier.

## INVEST self-check

✅ I · ✅ N · ✅ V (zero-overhead role-context) · ✅ E · ✅ S · ✅ T (start a session; observe roles table available).

## Source

- GISF `gisf-delivery-backlog-management.pdf` slides 124, 128, 125.
- Parent feature: [[feature-010-claude-md-role-scope-section]].
