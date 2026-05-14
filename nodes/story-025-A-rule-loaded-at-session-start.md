---
category: story
id: story-025-A-rule-loaded-at-session-start
parent: "[[feature-025-claude-md-subagent-rule]]"
artifacts:
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 025-A — Subagent dispatch rule loaded at session start

> Parent: [[feature-025-claude-md-subagent-rule]].

## Cohn statement

As **any agent considering dispatch**, I want **the "subagent dispatch ≠ authority transfer" rule loaded from CLAUDE.md at session start**, so that **I don't accidentally cede scope when I meant to consult**.

## Conditions of Satisfaction

- CLAUDE.md Layer B section names the rule.
- Loaded by harness at every session start.

## INVEST self-check

✅ I · ✅ N · ✅ V (scope-preservation by default) · ✅ E · ✅ S · ✅ T (read CLAUDE.md).

## Source

- GISF slides 124, 128, 125.
- Parent feature: [[feature-025-claude-md-subagent-rule]].
- [[adr-005-subagent-dispatch-not-authority-transfer]].
