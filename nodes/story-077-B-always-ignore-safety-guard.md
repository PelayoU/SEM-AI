---
category: story
id: story-077-B-always-ignore-safety-guard
parent: "[[feature-077-portable-gate-scope]]"
artifacts:
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Story 077-B — Hardcoded always-ignore safety guard

## Cohn statement (GISF slide 124)

As **the SEM-IA framework**,
I want **a hardcoded always-ignore guard that runs before and overrides the role-scope union**,
so that **the `/role` escape valve (`.claude/.active-role`), the management layer (`nodes/`/`sessions/`), and OS/temp paths can never be gated by a careless project `role-scope.json` (which would deadlock the framework or lock out the graph)**.

## Conditions of Satisfaction (GISF slide 125)

- Guard arms are a verbatim copy of the old `is_substrate()` ignore set: `nodes/* sessions/* bibliography/* .git/* .obsidian/* .claude/.active-role CLAUDE.local.md /tmp/* /var/folders/* /*`.
- Even if `role-scope.json` lists `nodes/**` (or `.claude/.active-role`) under some role, those paths are still allowed (guard wins, runs first).
- The `/role` ceremony (writing `.claude/.active-role`) is never blocked → no bootstrap deadlock.

## INVEST self-check (GISF slide 128)

- **I** ✅ · **N** ✅ · **V** ✅ (load-bearing safety invariant) · **E** ✅ · **S** ✅ · **T** ✅ (careless-config probe).

## Source

- Skill: `po-feature-decomposition`. Cohn GISF slide 124; INVEST slide 128. Lineage `[[adr-013-gate-scope-is-project-configurable]]`.
