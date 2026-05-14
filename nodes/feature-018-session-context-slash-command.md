---
category: feature
id: feature-018-session-context-slash-command
parent: "[[cap-09-session-continuity]]"
artifacts:
  - "[[.claude/commands/session-context.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 018 — `/session-context` slash command

> Authored via `po-feature-decomposition`. Delivers part of [[cap-09-session-continuity]].

## What it delivers

`.claude/commands/session-context.md` defines the `/session-context` slash command. Re-reads the current session document into the active conversation's context. Used when context has drifted in a long session (the agent's working memory needs refresh from the durable session doc) or when resuming after a tool failure / mid-flight rollback.

## Story Map position

- **Activity (Epic):** Session ceremony.
- **Task:** This feature (context refresh command).
- **Release slice:** Walking skeleton.

## Stories (children)

- [[story-018-A-rehydrate-session-state]] — As an active role in a long session, I want to re-read the session doc into context, so my working memory matches the durable record.

## Spec sibling

- [[spec-018-session-context-slash-command]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (verifiable by issuing `/session-context` and observing session-doc content in next turn) → Construction → Consequences (drift-resistance in long sessions).

## Notes

Architectural anchor: [[adr-001-sessions-as-git-branch]]. The command is *read-only* — does not modify state. Anti-pattern to invoke instead of `/session-log` (logging is a *write* operation; refreshing context is a *read* operation).

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-001-sessions-as-git-branch]].
- Substrate evidence: `.claude/commands/session-context.md`.
