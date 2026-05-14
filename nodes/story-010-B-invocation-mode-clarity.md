---
category: story
id: story-010-B-invocation-mode-clarity
parent: "[[feature-010-claude-md-role-scope-section]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 010-B — Invocation modes documented explicitly

> Parent: [[feature-010-claude-md-role-scope-section]].

## Cohn statement

As a **human deciding how to engage SEM-IA**, I want **the two invocation modes (full role as agent vs subagent consultation via Task) explicitly documented**, so that **I don't conflate them**.

## Conditions of Satisfaction

- CLAUDE.md `## Roles` section names both modes.
- Cross-references to ADR 005 (`subagent dispatch ≠ authority transfer`).

## INVEST self-check

✅ I · ✅ N · ✅ V (no role-mode confusion) · ✅ E · ✅ S · ✅ T (read CLAUDE.md; verify both modes named).

## Source

- GISF slides 124, 128, 125.
- Parent feature: [[feature-010-claude-md-role-scope-section]].
- [[adr-005-subagent-dispatch-not-authority-transfer]].
