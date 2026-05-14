---
category: story
id: story-005-A-backlinks-surface-references
parent: "[[feature-005-obsidian-backlinks-pane]]"
artifacts:
  - "[[.obsidian/core-plugins.json]]"
  - "[[.obsidian/workspace.json]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 005-A — Backlinks pane surfaces references bidirectionally

> Parent: [[feature-005-obsidian-backlinks-pane]].

## Cohn statement

As a **human reading a node**, I want **to see who references this node without searching**, so that **I can navigate the graph in both directions (parent and children, but also lateral references)**.

## Conditions of Satisfaction

- Backlinks pane core-plugin enabled.
- Workspace layout includes the pane.
- Opening any referenced node populates the pane within one frame.

## INVEST self-check

✅ I · ✅ N · ✅ V (bidirectional navigation) · ✅ E · ✅ S · ✅ T (observational).

## Source

- GISF `gisf-delivery-backlog-management.pdf` slides 124, 128, 125.
- Parent feature: [[feature-005-obsidian-backlinks-pane]].
