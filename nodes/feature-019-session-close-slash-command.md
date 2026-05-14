---
category: feature
id: feature-019-session-close-slash-command
parent: "[[cap-09-session-continuity]]"
artifacts:
  - "[[.claude/commands/session-close.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 019 — `/session-close` slash command

> Authored via `po-feature-decomposition`. Delivers part of [[cap-09-session-continuity]].

## What it delivers

`.claude/commands/session-close.md` defines the `/session-close` slash command. Appends the `## Closing summary` to the session doc (Outcome / Pending / Merge decision), surfaces the human's decision on the branch (merge to main / open PR / discard), and ends the session as a coherent unit. Until invoked, the session remains *open* (per [[adr-001-sessions-as-git-branch]] *branch state IS session state*).

## Story Map position

- **Activity (Epic):** Session ceremony.
- **Task:** This feature (close command).
- **Release slice:** Walking skeleton — closure ritual completes the session lifecycle.

## Stories (children)

- [[story-019-A-finalise-session-state]] — As an active role at the natural end of a thread of work, I want `/session-close` to finalise the session doc and prompt for a merge decision, so the session's outcome is durable and the branch decision is explicit.

## Spec sibling

- [[spec-019-session-close-slash-command]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (closing summary appears; merge decision recorded) → Construction → Consequences (sessions end cleanly, never hang).

## Notes

Architectural anchor: [[adr-001-sessions-as-git-branch]]. The command does not automatically merge or push — the human signs (per [[adr-010-human-directed-ai-maintained]]). It only authors the closure and surfaces the decision.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-001-sessions-as-git-branch]], [[adr-010-human-directed-ai-maintained]].
- Substrate evidence: `.claude/commands/session-close.md`.
