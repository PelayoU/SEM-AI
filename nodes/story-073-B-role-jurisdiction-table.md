---
category: story
id: story-073-B-role-jurisdiction-table
parent: "[[feature-073-claude-md-orientation-and-governance]]"
artifacts:
  - "[[CLAUDE.md]]"
status: draft
created: 2026-05-15
updated: 2026-05-15
---

# Story 073-B — Role-jurisdiction table

## Cohn statement (GISF slide 124)

As **any role**,
I want **a `## Role jurisdiction` table in CLAUDE.md (Role | Owns | Must NOT author | Escalation) for all 5 roles**,
so that **PO ≠ Architect is stated explicitly, not only discoverable at audit time — and the table mirrors the machine-authoritative `.claude/role-scope.json`**.

## Conditions of Satisfaction (GISF slide 125)

- Table present near § Roles, all 5 roles, 4 columns.
- Escalation column says: consultation = subagent (information only); cross-role work = `/role` switch (ADR-005).
- Table content agrees with `.claude/role-scope.json` (verified by [[spec-075-hard-role-jurisdiction]]).

## INVEST self-check (GISF slide 128)

- **I** ⚠️ couples to feature-075's role-scope.json (consistency requirement) — accepted, noted. **N** ✅ · **V** ✅ · **E** ✅ · **S** ✅ · **T** ✅.

## Source

- Skill: `po-feature-decomposition`. Cohn GISF slide 124; INVEST slide 128.
