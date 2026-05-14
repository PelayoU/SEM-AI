---
category: story
id: story-018-A-rehydrate-session-state
parent: "[[feature-018-session-context-slash-command]]"
artifacts:
  - "[[.claude/commands/session-context.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 018-A — Re-read session doc into context on demand

> Parent: [[feature-018-session-context-slash-command]].

## Cohn statement

As an **active role in a long session**, I want **`/session-context` to re-read the session doc into my working memory**, so that **my context matches the durable record after drift**.

## Conditions of Satisfaction

- `.claude/commands/session-context.md` defines the command.
- Invocation surfaces the current session doc content into the active turn.

## INVEST self-check

✅ I · ✅ N · ✅ V (drift-resistance) · ✅ E · ✅ S · ✅ T (invoke; observe doc content loaded).

## Source

- GISF slides 124, 128, 125.
- Parent feature: [[feature-018-session-context-slash-command]].
