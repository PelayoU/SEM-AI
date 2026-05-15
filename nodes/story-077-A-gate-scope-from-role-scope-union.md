---
category: story
id: story-077-A-gate-scope-from-role-scope-union
parent: "[[feature-077-portable-gate-scope]]"
artifacts:
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
status: draft
created: 2026-05-15
updated: 2026-05-15
---

# Story 077-A — Gate scope = role-scope.json glob union

## Cohn statement (GISF slide 124)

As **the SEM-IA framework dropped into any project**,
I want **the gate's "is this path governed?" answered by the union of all roles' globs in `.claude/role-scope.json`**,
so that **the gate is project-configurable by editing one file, with no code change (portability — `[[cap-13-portability]]`)**.

## Conditions of Satisfaction (GISF slide 125)

- The union is computed with `jq` excluding non-array keys (the `_comment` scalar must not crash iteration).
- A path matching ≥1 glob of ≥1 role → governed; matching none → ignored.
- Every real substrate path in SEM-AI today still classifies as governed (no observable regression).

## INVEST self-check (GISF slide 128)

- **I** ✅ · **N** ✅ · **V** ✅ (the core portability fix) · **E** ✅ · **S** ✅ (replace one function) · **T** ✅ (deterministic hook invocation).

## Source

- Skill: `po-feature-decomposition`. Cohn GISF slide 124; INVEST slide 128. Lineage `[[adr-013-gate-scope-is-project-configurable]]`.
