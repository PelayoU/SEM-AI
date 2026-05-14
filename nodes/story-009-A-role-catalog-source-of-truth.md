---
category: story
id: story-009-A-role-catalog-source-of-truth
parent: "[[feature-009-role-catalog-design-doc]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 009-A — Single source of truth for the role catalog

> Parent: [[feature-009-role-catalog-design-doc]].

## Cohn statement

As a **framework maintainer**, I want **a single design document (`sem-role-catalog.md`) defining the role catalog (Tier 1–4, BP→skill mapping)**, so that **additions or changes to roles are anchored to one auditable source rather than discovered across multiple files**.

## Conditions of Satisfaction

- `.claude/sem-role-catalog.md` exists and is current.
- Every `.claude/agents/<role>.md` is consistent with the catalog.

## INVEST self-check

✅ I · ✅ N · ✅ V (single point of change for role taxonomy) · ✅ E · ✅ S · ✅ T (cross-check agent files vs catalog).

## Source

- GISF `gisf-delivery-backlog-management.pdf` slides 124, 128, 125.
- Parent feature: [[feature-009-role-catalog-design-doc]].
