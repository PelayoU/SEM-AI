---
category: feature
id: feature-021-claude-md-layer-b-section
parent: "[[cap-09-session-continuity]]"
artifacts:
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 021 — CLAUDE.md Layer B section (sessions, bootstrap, slash commands)

> Authored via `po-feature-decomposition`. Delivers part of [[cap-09-session-continuity]].

## What it delivers

`CLAUDE.md` carries the entire *Layer B — operating the framework* section: sessions = git branch + doc; session bootstrap procedure (detect branch → list open sessions → conversational ask → act); writing to the session doc (the 5 sections and who writes them); slash commands; subagent dispatch ≠ authority transfer; direct work on `main`. Loaded into every session start so the operating model is common knowledge.

## Story Map position

- **Activity (Epic):** Session ceremony documentation.
- **Task:** This feature (Layer B contract surface).
- **Release slice:** Walking skeleton.

## Stories (children)

- [[story-021-A-bootstrap-procedure-loaded]] — As any agent starting a new session, I want the bootstrap procedure documented in the universal contract, so resuming a branch or opening a new session is conversational and reliable.

## Spec sibling

- [[spec-021-claude-md-layer-b-section]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (verifiable: open a new session, observe the bootstrap-conversation pattern) → Construction (text in CLAUDE.md) → Consequences (operational model loaded for free at session start).

## Notes

Architectural anchor: [[adr-001-sessions-as-git-branch]]. The Layer B section is the *operating* doc; Layer A (framework definition) is the *what and why*. Both live in CLAUDE.md, deliberately separated by `## Layer A` / `## Layer B` headers.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-001-sessions-as-git-branch]].
- Substrate evidence: `CLAUDE.md` § *Layer B — operating the framework*.
