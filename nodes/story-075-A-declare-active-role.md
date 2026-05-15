---
category: story
id: story-075-A-declare-active-role
parent: "[[feature-075-hard-role-jurisdiction]]"
artifacts:
  - "[[.claude/commands/role.md]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Story 075-A — Declare the active role

## Cohn statement (GISF slide 124)

As **the human operating a role**,
I want **`/role <name>` to validate the name and write `.claude/.active-role`**,
so that **the active role is an explicit, machine-readable fact the gate can enforce against**.

## Conditions of Satisfaction (GISF slide 125)

- `/role architect` writes `.claude/.active-role` containing `architect`; invalid name is rejected with the 5 valid names.
- The marker write always succeeds even with the gate live (gate-ignored path).

## INVEST self-check (GISF slide 128)

- **I** ✅ · **N** ✅ · **V** ✅ (precondition for all hard role-scope) · **E** ✅ · **S** ✅ · **T** ✅ (marker content observable).

## Source

- Skill: `po-feature-decomposition`. Cohn GISF slide 124; INVEST slide 128.
