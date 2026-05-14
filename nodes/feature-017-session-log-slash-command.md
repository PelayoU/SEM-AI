---
category: feature
id: feature-017-session-log-slash-command
parent: "[[cap-09-session-continuity]]"
artifacts:
  - "[[.claude/commands/session-log.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 017 — `/session-log` slash command

> Authored via `po-feature-decomposition`. Delivers part of [[cap-09-session-continuity]].

## What it delivers

`.claude/commands/session-log.md` defines the `/session-log` slash command. Appends a Log entry to the current session document, datestamped and role-tagged, capturing what was decided, what artifacts were touched, who contributed, what's next. Used at every Log entry trigger (significant decision, artifact created, subagent consultation, before stepping away).

## Story Map position

- **Activity (Epic):** Session ceremony.
- **Task:** This feature (log slash command).
- **Release slice:** Walking skeleton — handoff discipline depends on it.

## Stories (children)

- [[story-017-A-append-log-entry]] — As an active role mid-session, I want `/session-log` to append a structured Log entry to the session doc, so the next contributor inherits state without verbal context transfer.

## Spec sibling

- [[spec-017-session-log-slash-command]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (this very session has used the command's pattern multiple times — even when invoked manually rather than via the slash) → Construction (`.claude/commands/session-log.md`) → Consequences (session doc carries chronological narrative).

## Notes

Architectural anchor: [[adr-001-sessions-as-git-branch]]. Companion to [[feature-018-session-context-slash-command]] (re-read state) and [[feature-019-session-close-slash-command]] (finalise state).

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-001-sessions-as-git-branch]].
- Substrate evidence: `.claude/commands/session-log.md`.
