---
category: session
id: 2026-05-15-gate-portability
date: 2026-05-15
participants: [architect]
related-nodes:
  - "[[adr-013-gate-scope-is-project-configurable]]"
  - "[[feature-077-portable-gate-scope]]"
  - "[[cap-13-portability]]"
artifacts: []
---

# Make the hard-enforcement gate portable

> Session = git branch. State is branch state.

## Context

The merged hard-enforcement gate (session `2026-05-15-hard-enforcement-layer`) hardcodes SEM-AI's self-hosting layout: `is_substrate()` fixes in-scope = `.claude/**`/`_obsidian/**`/`CLAUDE.md`/`LICENSE`, and CLAUDE.md says "SEM-IA *is* the substrate". Dropped into a consumer project (mobile app) this gates the imported framework nobody edits and leaves the product code ungated — the inverse of intent — and the Orient block misdirects the agent. This session makes the gate **project-portable**: it derives its governed scope from `.claude/role-scope.json` itself (union of all roles' globs = the project's gated artifact space; per-role = jurisdiction), keeps a hardcoded always-ignore safety guard, reframes CLAUDE.md to a 3-layer model, and ships a consumer example. It is the gate-scope corollary of ADR-004 / cap-13. **The merged layer is extended, never reverted.** Scope: gate portability only — `sem-ia init` stays a deferred cap-13 Implementation-B node. Pre-session hygiene reverted a stray 1-char `CLAUDE.md` corruption and an empty `nodes/Untitled.md` (unrelated strays). Pre-existing untracked `.claude/commands/session-log.md` (governed by feature-017, uncommitted from a prior session) is **flagged as a separate concern, not adopted here**.

## Log

### 2026-05-15 — architect

Opened session `2026-05-15-gate-portability` off clean `main`. Plan approved (gate scope from role-scope.json union + always-ignore guard + 3-layer CLAUDE.md reframe + consumer example; honest non-byte-identical regression framing; sem-ia init deferred). Next: declare `/role architect`, then author governing nodes (adr-013 + feature-077 + stories + spec-077) before any substrate edit.

Skills applied: `architect-architecture-design`.
Artifacts: this session doc.
Next: Phase B — nodes first.

### 2026-05-15 — product-owner + architect (Phase B: nodes first)

Set `/role architect` (gate-ignored marker). Authored **7 governing nodes** before any substrate edit, parents before children, light `## Source`: `adr-013-gate-scope-is-project-configurable` (Architect; relates-to/refines adr-004 + adr-012, names the non-byte-identical coverage delta honestly, defers `sem-ia init`), `feature-077-portable-gate-scope` + `story-077-A..D` + `spec-077-portable-gate-scope` (PO). All `artifacts:` pre-list the substrate paths Phase C will touch (hook, role-scope.json, role-scope.example.json, CLAUDE.md) → node-before-artifact satisfied in advance. Parent-chain sanity: 7/7 present, parents resolve. **No substrate touched yet.**

Skills applied: `po-feature-decomposition`, `po-spec-gherkin`, `architect-architecture-design`.
Artifacts: 7 nodes (adr-013, feature-077, story-077-A..D, spec-077); this session doc.
Next: Phase C — gate refactor + doctrine reframe + consumer example.

## Artifacts touched

- Created `sessions/2026-05-15-gate-portability.md` — this session doc.
- Created 7 nodes — `adr-013`, `feature-077`, `story-077-{A,B,C,D}`, `spec-077` — governing graph for the portable gate scope.

## Subagent consultations

> Consulting role retains scope authority; consulted role provides information only.

- (none yet)

## Closing summary

> Filled at `/session-close`.

**Outcome:** <pending>.

**Pending / next steps:** <pending>.

**Merge decision:** <pending>.
