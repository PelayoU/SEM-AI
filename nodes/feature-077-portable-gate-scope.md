---
category: feature
id: feature-077-portable-gate-scope
parent: "[[cap-13-portability]]"
artifacts:
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
  - "[[.claude/role-scope.json]]"
  - "[[.claude/role-scope.example.json]]"
  - "[[CLAUDE.md]]"
status: draft
created: 2026-05-15
updated: 2026-05-15
---

# Feature 077 — Portable gate scope (role-scope.json union, not hardcoded layout)

> Authored via `po-feature-decomposition`. **Relates to, does not duplicate:** [[adr-013-gate-scope-is-project-configurable]], [[adr-004-substrate-content-separation]], [[adr-012-mandatory-active-role-hard-jurisdiction]], [[feature-072-node-before-artifact-gate]], [[feature-073-claude-md-orientation-and-governance]], [[feature-075-hard-role-jurisdiction]], [[feature-034-substrate-as-portable-unit]]. Home for the **portability reframe of CLAUDE.md only** (CLAUDE.md is multi-governed; mirror feature-073's "this change only" discipline).

## What it delivers

The gate derives its governed scope from `.claude/role-scope.json`'s glob union (a consumer project gates its own product code by rewriting that one file) instead of a hardcoded self-hosting layout; a hardcoded always-ignore guard protects universal invariants + the `/role` escape valve; a documented `.claude/role-scope.example.json` (mobile-app); CLAUDE.md reframed to a 3-layer model (imported framework / project's declared artifacts / management graph). SEM-AI self-hosting behaviour is preserved on every observable path (full matrix re-run).

## Story Map position (Patton via slide 132)

- **Activity (Epic):** Portability substrate (same epic as [[feature-034-substrate-as-portable-unit]]).
- **Task:** this feature. **Release slice:** `[[goal-03-portability-proof]]` — the gate stops being a self-hosting-only artifact.

## Stories (children)

- `[[story-077-A-gate-scope-from-role-scope-union]]`
- `[[story-077-B-always-ignore-safety-guard]]`
- `[[story-077-C-claude-md-three-layer-reframe]]`
- `[[story-077-D-consumer-project-example]]`

## Spec sibling

- `[[spec-077-portable-gate-scope]]`

## Notes

Scope guards: do NOT build `sem-ia init` (deferred `[[cap-13-portability]]` Implementation-B); do NOT parameterize session-branch/wikilink/`artifacts:` conventions (ADR-004 fixes them universal); do NOT fix the pre-existing bootstrap-drift line (flag only); do NOT adopt the untracked `.claude/commands/session-log.md` (separate concern). `.claude/role-scope.example.json` is governed substrate (this feature + adr-013 + story-077-D `artifacts:`; architect-owned).

## Source

- Skill: `po-feature-decomposition`. GISF UC3M `gisf-life-cycle.pdf` slide 54 + slide 56. Light per template; lineage `[[adr-013-gate-scope-is-project-configurable]]`, `[[cap-13-portability]]`.
