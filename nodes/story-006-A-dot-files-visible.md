---
category: story
id: story-006-A-dot-files-visible
parent: "[[feature-006-show-hidden-files-plugin]]"
artifacts:
  - "[[.obsidian/plugins/show-hidden-files/manifest.json]]"
  - "[[.obsidian/community-plugins.json]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 006-A — Dot-files visible in Obsidian file tree

> Parent: [[feature-006-show-hidden-files-plugin]].

## Cohn statement

As a **human navigating the vault in Obsidian**, I want **dot-prefixed files and directories (`.claude/`, etc.) visible in the file tree**, so that **I can open agent definitions, skill files, and slash commands without leaving the editor**.

## Conditions of Satisfaction

- `show-hidden-files` community plugin installed under `.obsidian/plugins/`.
- Plugin enabled in `.obsidian/community-plugins.json`.
- File tree shows `.claude/` after enable.

## INVEST self-check

✅ I · ✅ N · ✅ V (full substrate visible in editor) · ✅ E · ✅ S · ✅ T (look at the file tree).

## Source

- GISF `gisf-delivery-backlog-management.pdf` slides 124, 128, 125.
- Parent feature: [[feature-006-show-hidden-files-plugin]].
