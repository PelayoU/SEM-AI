---
category: story
id: story-075-D-allow-correct-role
parent: "[[feature-075-hard-role-jurisdiction]]"
artifacts:
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
  - "[[.claude/role-scope.json]]"
status: draft
created: 2026-05-15
updated: 2026-05-15
---

# Story 075-D — Allow a write by the correct role

## Cohn statement (GISF slide 124)

As **a role acting within its jurisdiction**,
I want **a governed substrate write whose path is in my role's globs to pass silently**,
so that **the gate enables correct work as frictionlessly as it blocks incorrect work (precision, not bluntness)**.

## Conditions of Satisfaction (GISF slide 125)

- `.active-role`=architect + governed path in architect globs → Edit passes (exit 0, silent).
- `/role` switch then a write in the new role's scope → passes.

## INVEST self-check (GISF slide 128)

- **I** ✅ · **N** ✅ · **V** ✅ (proves the gate is not a blanket block) · **E** ✅ · **S** ✅ · **T** ✅ observable pass.

## Source

- Skill: `po-feature-decomposition`. Cohn GISF slide 124; INVEST slide 128.
