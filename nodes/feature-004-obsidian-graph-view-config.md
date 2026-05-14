---
category: feature
id: feature-004-obsidian-graph-view-config
parent: "[[cap-01-vision-to-code-audit]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 004 — Obsidian graph-view configuration for SEM-IA backbone

> Authored via `po-feature-decomposition`. Delivers part of [[cap-01-vision-to-code-audit]].

## What it delivers

`.obsidian/graph.json` carries the SEM-IA-tuned graph-view configuration: filters, colour groups, force-layout parameters that surface the vision↔goals↔caps↔features↔stories↔specs backbone visually. Opening the vault in Obsidian and toggling graph view shows the backbone as a navigable map without manual configuration.

## Story Map position

- **Activity (Epic):** Editor surface for the human director.
- **Task:** This feature (graph-view config).
- **Release slice:** Walking skeleton — first concrete visual surface for the human to "see" the project.

## Stories (children)

- [[story-004-A-graph-view-renders-backbone]] — As a human navigating the graph, I want graph view to render the backbone hierarchy legibly, so the project's shape is visible without reading files.

## Spec sibling

- [[spec-004-obsidian-graph-view-config]]

## 5 Cs cycle reminder

Card → Conversation (which filters and colour groups are useful for SEM-IA) → Confirmation (visual sanity test) → Construction (config in `.obsidian/graph.json`) → Consequences (backbone navigable visually).

## Notes

Architectural anchor: [[adr-007-obsidian-as-editor-surface]] (Obsidian recommended, not mandated; data layer remains editor-agnostic). Config is project-level (committed); user-local overlays via Obsidian's profile settings.

## Source

- Skill: `po-feature-decomposition`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54.
- ADRs: [[adr-007-obsidian-as-editor-surface]].
- Substrate evidence: `.obsidian/graph.json` in repo.
- Out-of-bibliography: Obsidian (vendor) — convention pointer, not authority.
