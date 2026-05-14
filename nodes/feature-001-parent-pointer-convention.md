---
category: feature
id: feature-001-parent-pointer-convention
parent: "[[cap-01-vision-to-code-audit]]"
artifacts:
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 001 — Parent-pointer convention in node frontmatter

> Authored via `po-feature-decomposition`. Delivers part of [[cap-01-vision-to-code-audit]].

## What it delivers

Every node (except `vision-sem-ia`) carries a `parent:` field in YAML frontmatter pointing to its parent via `[[wikilink]]`. The field forms the formal backbone tree and makes any audit walk vision↔code navigable without external metadata. Implementation already in force across all 33 existing nodes.

## Story Map position (Patton via slide 132)

- **Activity (Epic):** Project graph maintenance.
- **Task:** This feature (parent-pointer convention).
- **Release slice:** Walking skeleton — backbone cannot exist without this feature.

## Stories (children)

- [[story-001-A-parent-pointer-authoring]] — As a node author, I want every non-root node to declare its parent in frontmatter, so the audit chain is automatically navigable.

## Spec sibling

- [[spec-001-parent-pointer-convention]]

## 5 Cs cycle reminder (GISF slide 56 + agile-story-essentials.pdf)

Card → Conversation → Confirmation (the spec encodes *"parent: must resolve to an existing file under `nodes/`"*) → Construction (substrate-wide, already in force) → Consequences (audit-by-navigation works on every artifact).

## Notes

Architectural anchors: [[adr-002-backbone-hierarchy-parent-edges]] (the decision); [[adr-008-markdown-frontmatter-data-format]] (the format). Cross-cap usage: serves [[goal-01-self-bootstrap-validation]] M-criterion "end-to-end navigation succeeds with no broken parent edges".

## Source

- Skill: `po-feature-decomposition`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54 (feature definition); slide 56 (5 Cs).
- ADRs: [[adr-002-backbone-hierarchy-parent-edges]], [[adr-008-markdown-frontmatter-data-format]].
- Substrate evidence: every file under `nodes/` carries the `parent:` field (verifiable via `grep '^parent:' nodes/*.md`).
