---
category: feature
id: feature-016-claude-md-citation-mandate
parent: "[[cap-08-citation-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 016 — CLAUDE.md citation-mandate rule + out-of-bibliography flagging

> Authored via `po-feature-decomposition`. Delivers part of [[cap-08-citation-discipline]].

## What it delivers

`CLAUDE.md` carries the operating principle *"Citation is mandatory. Every authoritative claim traces to a primary source."* and the corollary *"Out-of-bibliography is named, not borrowed silently."* These rules are loaded into every session at start, so every agent (and the human) operates under citation discipline from turn zero.

## Story Map position

- **Activity (Epic):** Bibliographic infrastructure.
- **Task:** This feature (citation mandate as contract).
- **Release slice:** Walking skeleton — the rule must exist before any skill can cite.

## Stories (children)

- [[story-016-A-citation-mandate-loaded]] — As any agent or human, I want the citation rule loaded at session start, so no claim escapes the discipline by oversight.
- [[story-016-B-out-of-biblio-flagged]] — As a skill author considering a framework not in `bibliography/sources/`, I want the flagging rule explicit, so I add a disclaimer rather than treat the framework as authority.

## Spec sibling

- [[spec-016-claude-md-citation-mandate]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (rule present in CLAUDE.md operating principles) → Construction (text added to the contract) → Consequences (citation discipline becomes structural).

## Notes

Architectural anchor: [[adr-003-citation-mandate]] (the formal decision). This feature is the *operationalisation* — the rule has to live somewhere agents read; CLAUDE.md is that surface.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-003-citation-mandate]].
- Substrate evidence: `CLAUDE.md` § *Operating principles* + § *Skills convention* (citation paragraph).
