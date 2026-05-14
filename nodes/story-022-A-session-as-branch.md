---
category: story
id: story-022-A-session-as-branch
parent: "[[feature-022-git-branch-as-session-state]]"
artifacts:
  # No concrete substrate — this node describes an abstract property
  # without a single artefact owner. See CLAUDE.md § Substrate traceability.
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 022-A — Session state carried by git branch

> Parent: [[feature-022-git-branch-as-session-state]].

## Cohn statement

As an **active role**, I want **my session's state carried by a git branch named `session/<id>`**, so that **isolation, durability, and concurrency come from a substrate I already trust (git) rather than a parallel state-tracking layer**.

## Conditions of Satisfaction

- Every session has a matching `session/<id>` branch.
- Switching branches switches session context.

## INVEST self-check

✅ I · ✅ N · ✅ V (zero-tooling state) · ✅ E · ✅ S · ✅ T (this very session: `session/2026-05-14-sem-ia-self-bootstrap`).

## Source

- GISF slides 124, 128, 125.
- Parent feature: [[feature-022-git-branch-as-session-state]].
- [[adr-001-sessions-as-git-branch]].
