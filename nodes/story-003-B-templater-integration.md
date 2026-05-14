---
category: story
id: story-003-B-templater-integration
parent: "[[feature-003-node-templates-eight]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 003-B — Templater populates frontmatter at creation time

> Parent: [[feature-003-node-templates-eight]].

## Cohn statement

As a **human using Obsidian**, I want **Templater (community plugin) to populate frontmatter (`created`, `updated`, `id`) at node-creation time**, so that **date and id fields don't drift from filename**.

## Conditions of Satisfaction

- Templater configured to use `_obsidian/templates/` as source.
- New-node creation populates dates without manual entry.

## INVEST self-check

✅ I · ✅ N · ✅ V (drift-resistance) · ✅ E · ✅ S · ✅ T (create a new node; observe frontmatter).

## Source

- GISF `gisf-delivery-backlog-management.pdf` slides 124, 128, 125.
- Parent feature: [[feature-003-node-templates-eight]].
- Out-of-bibliography: Templater (Obsidian community plugin).
