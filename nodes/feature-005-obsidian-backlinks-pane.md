---
category: feature
id: feature-005-obsidian-backlinks-pane
parent: "[[cap-01-vision-to-code-audit]]"
artifacts:
  - "[[.obsidian/core-plugins.json]]"
  - "[[.obsidian/workspace.json]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 005 — Obsidian backlinks pane

> Authored via `po-feature-decomposition`. Delivers part of [[cap-01-vision-to-code-audit]].

## What it delivers

Obsidian's backlinks pane (core plugin, enabled in `.obsidian/core-plugins.json` + workspace layout in `.obsidian/workspace.json`) shows, for any open node, every other node in the vault that references it via wikilink. Combined with [[feature-002-wikilinks-narrative-cross-reference]], backlinks turn the graph into a navigable web: from any node, walk to every artifact that mentions it.

## Story Map position

- **Activity (Epic):** Editor surface for the human director.
- **Task:** This feature (backlinks pane).
- **Release slice:** Walking skeleton.

## Stories (children)

- [[story-005-A-backlinks-surface-references]] — As a human reading a node, I want to see who references it without searching, so I can navigate the graph in both directions.

## Spec sibling

- [[spec-005-obsidian-backlinks-pane]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (visual test: open any node, see backlinks pane populate) → Construction (Obsidian core plugin) → Consequences (bidirectional navigation without bookkeeping).

## Notes

Companion to [[feature-002-wikilinks-narrative-cross-reference]] (wikilinks are the data; backlinks pane is the view). Architectural anchor: [[adr-007-obsidian-as-editor-surface]].

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-007-obsidian-as-editor-surface]].
- Substrate evidence: `.obsidian/core-plugins.json` enables backlinks; `.obsidian/workspace.json` includes the pane in layout.
- Out-of-bibliography: Obsidian (vendor).
