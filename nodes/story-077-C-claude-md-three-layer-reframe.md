---
category: story
id: story-077-C-claude-md-three-layer-reframe
parent: "[[feature-077-portable-gate-scope]]"
artifacts:
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Story 077-C — CLAUDE.md 3-layer reframe

## Cohn statement (GISF slide 124)

As **a fresh session in a consumer project (not SEM-IA itself)**,
I want **CLAUDE.md to distinguish (1) the imported SEM-IA framework, (2) the project's declared artifacts (`role-scope.json` union), (3) the management graph (`nodes/`+`sessions/`)**,
so that **I protect/trace the project's product code, not the imported tool — the Orient block no longer says "SEM-IA *is* the substrate" unconditionally**.

## Conditions of Satisfaction (GISF slide 125)

- Orient block reframed to the 3 layers; self-hosting still reads correctly (SEM-AI = "declared artifacts are the framework itself").
- Terminology Substrate note + Graph-vs-substrate + Node-before-artifact operating bullets reframed (+`[[adr-013-gate-scope-is-project-configurable]]` backlinks).
- A short `## Portability` subsection added (fork-and-adapt; rewrite role-scope.json; `sem-ia init` deferred).
- § Role jurisdiction notes role-scope.json = per-project gate config; Architect row + role-scope.json both gain `.claude/role-scope.example.json` (mirror invariant, spec-075/spec-077).

## INVEST self-check (GISF slide 128)

- **I** ⚠️ couples to story-077-D (the example path appears in both CLAUDE.md table and role-scope.json — consistency requirement; accepted, noted) · **N** ✅ · **V** ✅ · **E** ✅ · **S** ✅ · **T** ✅.

## Source

- Skill: `po-feature-decomposition`. Cohn GISF slide 124; INVEST slide 128. Lineage `[[adr-013-gate-scope-is-project-configurable]]`, `[[adr-004-substrate-content-separation]]`.
