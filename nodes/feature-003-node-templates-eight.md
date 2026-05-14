---
category: feature
id: feature-003-node-templates-eight
parent: "[[cap-01-vision-to-code-audit]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 003 — Eight node templates aligned to backbone categories

> Authored via `po-feature-decomposition`. Delivers part of [[cap-01-vision-to-code-audit]].

## What it delivers

Eight authoritative node templates under `_obsidian/templates/` — one per category in the backbone hierarchy plus session and adr. Each template encodes the canonical structure (required frontmatter, required body sections, citation discipline) of its category. New nodes are scaffolded by Templater (Obsidian community plugin) or by an agent reading the template and filling it.

Templates: `vision.md`, `goal.md`, `capability.md`, `feature.md`, `story.md`, `spec.md`, `adr.md`, `session.md`.

## Story Map position

- **Activity (Epic):** Project graph authoring.
- **Task:** This feature (templates).
- **Release slice:** Walking skeleton — without templates, the graph's structural conformance cannot be enforced.

## Stories (children)

- [[story-003-A-template-per-backbone-category]] — As a node author, I want a template per backbone category, so I scaffold a conformant node without copy-pasting from another.
- [[story-003-B-templater-integration]] — As a human using Obsidian, I want Templater to populate frontmatter at node-creation time, so date and id fields don't drift.

## Spec sibling

- [[spec-003-node-templates-eight]]

## 5 Cs cycle reminder

Card → Conversation (sessions of bootstrap iterations refined the templates) → Confirmation (spec lists required fields per category) → Construction (Templater + manual Read+Write) → Consequences (every node is structurally auditable).

## Notes

Architectural anchor: [[adr-008-markdown-frontmatter-data-format]]. Templater is convention-pointer (Obsidian community plugin) not Jones-anchored. Templates themselves are tier-1 SEM-IA assets — modifications go through CCB-equivalent review per [[cap-08-citation-discipline]].

## Source

- Skill: `po-feature-decomposition`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54.
- ADRs: [[adr-008-markdown-frontmatter-data-format]].
- Substrate evidence: 8 `.md` files under `_obsidian/templates/`.
