---
category: feature
id: feature-022-git-branch-as-session-state
parent: "[[cap-09-session-continuity]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 022 — Git branch as the durable session-state carrier

> Authored via `po-feature-decomposition`. Delivers part of [[cap-09-session-continuity]].

## What it delivers

A session lives as a git branch named `session/<id>` (matching the session doc id at `sessions/<id>.md`). Branch state IS session state — there is no separate session-status field. To list open sessions: `git branch --list 'session/*'`. To resume: `git checkout session/<id>`. The git substrate provides durability, isolation, and (via merge / discard) closure semantics with no additional tooling.

## Story Map position

- **Activity (Epic):** Session ceremony substrate.
- **Task:** This feature (branch as state carrier).
- **Release slice:** Walking skeleton — required for any session to exist.

## Stories (children)

- [[story-022-A-session-as-branch]] — As an active role, I want my session's state carried by a git branch, so isolation and durability come from a substrate I already trust.
- [[story-022-B-branch-list-as-open-sessions]] — As a human between sessions, I want `git branch --list 'session/*'` to be the inventory of open sessions, so no parallel status-tracking is needed.

## Spec sibling

- [[spec-022-git-branch-as-session-state]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (verifiable: this session lives on `session/2026-05-14-sem-ia-self-bootstrap`) → Construction (git substrate) → Consequences (zero-tooling state management).

## Notes

Architectural anchor: [[adr-001-sessions-as-git-branch]]. Git is a tier-1 dependency — universal among software-engineering projects; safe to bind to. The decision rules out alternative session implementations (DB row, JSON state file) per ADR 001.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-001-sessions-as-git-branch]].
- Substrate evidence: git itself; this session is the live example.
