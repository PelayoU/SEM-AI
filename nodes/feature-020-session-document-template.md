---
category: feature
id: feature-020-session-document-template
parent: "[[cap-09-session-continuity]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 020 — Session document template

> Authored via `po-feature-decomposition`. Delivers part of [[cap-09-session-continuity]].

## What it delivers

`_obsidian/templates/session.md` is the canonical structure for every session document: frontmatter (category, id, date, participants, related-nodes) + Context + Log + Artifacts touched + Subagent consultations + Closing summary. Sessions opened in the bootstrap conversation scaffold from this template.

## Story Map position

- **Activity (Epic):** Session ceremony.
- **Task:** This feature (session-doc template).
- **Release slice:** Walking skeleton.

## Stories (children)

- [[story-020-A-session-from-template]] — As a session-opening role, I want a session doc scaffold with all sections present from turn zero, so structure doesn't depend on author memory.

## Spec sibling

- [[spec-020-session-document-template]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (this very session was opened from the template) → Construction → Consequences (sessions are structurally uniform).

## Notes

Architectural anchor: [[adr-001-sessions-as-git-branch]]. Section conventions per CLAUDE.md Layer B `## Writing to the session doc`. The template is also the audit grid: a session that lacks any of the 5 sections is structurally non-conformant.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-001-sessions-as-git-branch]].
- Substrate evidence: `_obsidian/templates/session.md`.
