---
category: story
id: story-003-A-template-per-backbone-category
parent: "[[feature-003-node-templates-eight]]"
artifacts:
  - "[[_obsidian/templates/vision.md]]"
  - "[[_obsidian/templates/goal.md]]"
  - "[[_obsidian/templates/capability.md]]"
  - "[[_obsidian/templates/feature.md]]"
  - "[[_obsidian/templates/story.md]]"
  - "[[_obsidian/templates/spec.md]]"
  - "[[_obsidian/templates/adr.md]]"
  - "[[_obsidian/templates/session.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 003-A — One template per backbone category

> Parent: [[feature-003-node-templates-eight]].

## Cohn statement

As a **node author**, I want **a template per backbone category (vision, goal, capability, feature, story, spec, adr, session)**, so that **I scaffold a conformant node without copy-pasting from another**.

## Conditions of Satisfaction

- 8 templates exist under `_obsidian/templates/`.
- Each carries category-specific frontmatter + required body sections.

## INVEST self-check

✅ I · ✅ N · ✅ V (consistent structure across the graph) · ✅ E · ✅ S · ✅ T (`ls _obsidian/templates/` shows the 8 files).

## Source

- GISF `gisf-delivery-backlog-management.pdf` slides 124, 128, 125.
- Parent feature: [[feature-003-node-templates-eight]].
