---
category: feature
id: feature-032-substrate-content-directory-separation
parent: "[[cap-13-portability]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 032 — Substrate / content directory separation

> Authored via `po-feature-decomposition`. Delivers part of [[cap-13-portability]].

## What it delivers

The repo enforces a hard partition: **substrate** lives in `.claude/` + `_obsidian/` + `bibliography/` + `CLAUDE.md` + `LICENSE` (reusable across projects); **content** lives in `nodes/` + `sessions/` (project-specific). A fork of SEM-IA for a new project copies the substrate paths verbatim and starts a fresh `nodes/` + `sessions/`. The separation is the load-bearing property of [[cap-13-portability]].

## Story Map position

- **Activity (Epic):** Portability substrate.
- **Task:** This feature (directory partition).
- **Release slice:** Walking skeleton — without this separation, portability is structurally impossible.

## Stories (children)

- [[story-032-A-fork-substrate-fresh-content]] — As a new-project author lifting SEM-IA, I want to copy the substrate paths and start with empty content, so my new project inherits the framework without dragging SEM-IA's own graph along.

## Spec sibling

- [[spec-032-substrate-content-directory-separation]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (cleanly testable: `ls` distinguishes substrate vs content directories) → Construction (in force) → Consequences (portability operational).

## Notes

Architectural anchor: [[adr-004-substrate-content-separation]] (the decision). The separation is the *unit of portability* claim per ADR 004. Goal-03 (portability proof) directly tests this feature.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-004-substrate-content-separation]].
- Substrate evidence: directory layout per CLAUDE.md § *Repo structure*.
