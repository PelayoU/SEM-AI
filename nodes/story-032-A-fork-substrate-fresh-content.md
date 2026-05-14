---
category: story
id: story-032-A-fork-substrate-fresh-content
parent: "[[feature-032-substrate-content-directory-separation]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 032-A — Fork substrate, start fresh content

> Parent: [[feature-032-substrate-content-directory-separation]].

## Cohn statement

As a **new-project author lifting SEM-IA**, I want **to copy the substrate paths (`.claude/`, `_obsidian/`, `bibliography/`, `CLAUDE.md`, `LICENSE`) and start with empty `nodes/` + `sessions/`**, so that **my new project inherits the framework without dragging SEM-IA's own graph along**.

## Conditions of Satisfaction

- Directory layout cleanly partitioned (substrate vs content).
- Copy-paste-instantiate workflow yields a working SEM-IA-derived project.

## INVEST self-check

✅ I · ✅ N · ✅ V (portability operational) · ✅ E · ✅ S · ✅ T (G3 will exercise this on a secondary project).

## Source

- GISF slides 124, 128, 125.
- Parent feature: [[feature-032-substrate-content-directory-separation]].
- [[adr-004-substrate-content-separation]].
