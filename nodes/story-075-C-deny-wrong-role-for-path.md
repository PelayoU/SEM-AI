---
category: story
id: story-075-C-deny-wrong-role-for-path
parent: "[[feature-075-hard-role-jurisdiction]]"
artifacts:
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
  - "[[.claude/role-scope.json]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Story 075-C — Deny a write whose path is outside the active role

## Cohn statement (GISF slide 124)

As **the framework**,
I want **a substrate write denied when the target path is not in the active role's `.claude/role-scope.json` globs**,
so that **PO ≠ Architect is structurally enforced — a PO cannot author an ADR/CLAUDE.md change even with a governing node present**.

## Conditions of Satisfaction (GISF slide 125)

- With `.active-role`=developer, an Edit to `CLAUDE.md` (architect path) is denied; reason names the owning role + escalation.
- The deny fires after the node-before-artifact check (both must pass to allow).

## INVEST self-check (GISF slide 128)

- **I** ✅ · **N** ✅ (map negotiable) · **V** ✅ (the core "cada rol lo suyo") · **E** ✅ · **S** ✅ · **T** ✅ observable denial.

## Source

- Skill: `po-feature-decomposition`. Cohn GISF slide 124; INVEST slide 128. Lineage: Jones Ch 5 p.282 (role protected from coercion) via [[adr-012-mandatory-active-role-hard-jurisdiction]].
