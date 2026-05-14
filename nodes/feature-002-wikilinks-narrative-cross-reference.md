---
category: feature
id: feature-002-wikilinks-narrative-cross-reference
parent: "[[cap-01-vision-to-code-audit]]"
artifacts:
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 002 — Wikilinks `[[id]]` for narrative cross-reference

> Authored via `po-feature-decomposition`. Delivers part of [[cap-01-vision-to-code-audit]].

## What it delivers

Inside node bodies, narrative cross-references between artifacts use Obsidian-style `[[wikilinks]]`. Wikilinks are *narrative* references (a sentence mentioning a related node), distinct from the *formal* hierarchical edge in `parent:` frontmatter. Wikilinks activate Obsidian's backlinks pane and graph view.

## Story Map position

- **Activity (Epic):** Project graph maintenance.
- **Task:** This feature (wikilinks).
- **Release slice:** Walking skeleton — required for the graph's narrative richness.

## Stories (children)

- [[story-002-A-wikilinks-in-body]] — As a node author, I want to reference related artifacts via `[[id]]` in body prose, so backlinks and graph view light up automatically.

## Spec sibling

- [[spec-002-wikilinks-narrative-cross-reference]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (spec encodes "wikilink target must resolve to an existing node, or be flagged as deferred") → Construction (in force across all 33 nodes) → Consequences (backlinks pane populates without bookkeeping).

## Notes

Distinct from `parent:` (frontmatter, formal edge). Architectural anchor: [[adr-002-backbone-hierarchy-parent-edges]] explicitly separates the two. Empty frontmatter cross-link fields (`also-relates-to`, `depends-on`) were eliminated by design — narrative cross-references live in body via wikilinks only.

## Source

- Skill: `po-feature-decomposition`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54.
- ADRs: [[adr-002-backbone-hierarchy-parent-edges]].
- CLAUDE.md § *Wikilinks* describes the convention.
- Out-of-bibliography: Obsidian (vendor) implements wikilinks per common practice — convention pointer, not anchored authority.
