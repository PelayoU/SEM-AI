---
category: story
id: story-019-A-finalise-session-state
parent: "[[feature-019-session-close-slash-command]]"
artifacts:
  - "[[.claude/commands/session-close.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 019-A — Finalise session with closing summary and merge decision

> Parent: [[feature-019-session-close-slash-command]].

## Cohn statement

As an **active role at the natural end of a thread of work**, I want **`/session-close` to author the `## Closing summary` and surface the merge / PR / discard decision**, so that **the session ends cleanly with a durable outcome record**.

## Conditions of Satisfaction

- `.claude/commands/session-close.md` defines the command.
- Invocation authors Outcome / Pending / Merge-decision sections.
- The human signs the merge decision (no automated merge).

## INVEST self-check

✅ I · ✅ N · ✅ V (clean closure) · ✅ E · ✅ S · ✅ T (invoke at session end; observe closing summary appended).

## Source

- GISF slides 124, 128, 125.
- Parent feature: [[feature-019-session-close-slash-command]].
- [[adr-010-human-directed-ai-maintained]] (merge decision is human's).
