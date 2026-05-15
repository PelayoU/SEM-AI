---
category: story
id: story-072-C-allow-governed-and-ignore-nonsubstrate
parent: "[[feature-072-node-before-artifact-gate]]"
artifacts:
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Story 072-C — Allow governed substrate; ignore non-substrate

> Acceptance criteria trace to the spec sibling as `AC-C1`, `AC-C2`, …

## Cohn statement (GISF slide 124)

As **a contributor**,
I want **a write to a substrate path that IS referenced by some node's `artifacts:`, and every write to `nodes/`, `sessions/`, `bibliography/`, `/tmp`, `.git`, `.obsidian/`, to pass without friction**,
so that **the gate is precise (closes the hole, not the work) — the prefacio's "no friction added" property holds**.

## Conditions of Satisfaction (GISF slide 125)

- Governed substrate Edit passes silently (exit 0, no output).
- Node/session writes always pass (the governance escape valve).
- Non-repo / temp / git-internal writes always pass.

## INVEST self-check (GISF slide 128)

- **I** ✅ · **N** ✅ · **V** ✅ (prevents the gate becoming a blunt instrument) · **E** ✅ · **S** ✅ · **T** ✅ observable pass.

## Source

- Skill: `po-feature-decomposition`. Cohn format GISF slide 124; INVEST slide 128.
