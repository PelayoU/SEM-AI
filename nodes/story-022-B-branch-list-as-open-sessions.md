---
category: story
id: story-022-B-branch-list-as-open-sessions
parent: "[[feature-022-git-branch-as-session-state]]"
artifacts:
  # No concrete substrate — this node describes an abstract property
  # without a single artefact owner. See CLAUDE.md § Substrate traceability.
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 022-B — Open sessions = `git branch --list 'session/*'`

> Parent: [[feature-022-git-branch-as-session-state]].

## Cohn statement

As a **human between sessions**, I want **the inventory of open sessions to be `git branch --list 'session/*'`**, so that **no parallel status-tracking system is needed**.

## Conditions of Satisfaction

- All open session branches follow `session/<id>` naming.
- Closed sessions = branches merged or deleted.

## INVEST self-check

✅ I · ✅ N · ✅ V (operational simplicity) · ✅ E · ✅ S · ✅ T (run the command; see open sessions).

## Source

- GISF slides 124, 128, 125.
- Parent feature: [[feature-022-git-branch-as-session-state]].
- [[adr-001-sessions-as-git-branch]].
