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

### 2026-05-15 — architect (Phase C: substrate)

Refactored `.claude/hooks/enforce-node-before-artifact.sh`: replaced `is_substrate()` with `always_ignore()` (verbatim copy of the old ignore arms — load-bearing safety guard, runs first) + `is_governed()` (path matches any glob across all roles via `jq '[to_entries[]|select(.value|type=="array")|.value[]]|unique'` — `_comment` scalar tolerated); call-site became `always_ignore && continue` / `is_governed || continue`. Everything else (parsing, glob_match, node-before-artifact grep, per-role check, deny/allow/trap) byte-identical. Reframed `.claude/role-scope.json` `_comment` as the per-project gate config + added `.claude/role-scope.example.json` to the architect array; created `.claude/role-scope.example.json` (mobile-app worked example). CLAUDE.md: Orient block → 3-layer model, Terminology note, Graph-vs-/Node-before-artifact operating bullets reframed, § Role jurisdiction intro + Architect row + new `## Portability` section. A recurring stray-corruption (`. ` prepended to an Orient line) was reverted via `git checkout -- CLAUDE.md` after the clean Phase-C commit (committed version was correct; the working-tree stray was discarded — same class as the earlier `/` stray, unrelated to the work).

Skills applied: `architect-architecture-design`.
Artifacts: `.claude/hooks/enforce-node-before-artifact.sh`, `.claude/role-scope.json`, `.claude/role-scope.example.json`, `CLAUDE.md`.
Next: Phase D — verification.

### 2026-05-15 — qa + architect (Phase D: verification)

Direct hook invocation (gate enforces next session; logic verified deterministically — QA consulted on scenario design). **No observable regression** (self-hosting matrix == prior Phase E: governed+node ALLOW; ungoverned DENY; `cp`/`mv`/`>`/`>>`/`tee`/`dd` DENY; `/tmp`/`nodes/` ALLOW; no-role/wrong-role DENY). **Named intended delta** (ADR-013): old `.claude/skills/dummy-probe` probe now ignored (no role glob) — re-verified deny with `.claude/agents/probe.md`. **Consumer simulation** (`developer→src/**`): `src/app.ts` DENY, `.claude/agents/architect.md` ignored, `ios/Info.plist` DENY — the self-hosting→consumer inversion is fixed. **Careless config** (`nodes/**`,`.claude/.active-role` under a role): both ALLOW — always-ignore guard wins, no deadlock. `jq` tolerates `_comment`. role-scope.json ↔ CLAUDE.md table consistent incl. example file. **Honest residual** (pre-existing, documented adr-011, NOT a portability regression, deferred): `sed -i ""` BSD-form not caught by the heuristic Bash parser (the sed regex never matched it; Bash parsing untouched by this refactor). 6 nodes bumped → `implemented`; adr-013 stays `proposed` for human acceptance at close.

Skills applied: `qa-testing-strategy` (consulted), `architect-architecture-design`.
Artifacts: spec-077 realized notes; 6 node status bumps; this session doc.
Next: Phase E — `/session-close`.

## Artifacts touched

- Created `sessions/2026-05-15-gate-portability.md` — this session doc.
- Created 7 nodes — `adr-013`, `feature-077`, `story-077-{A,B,C,D}`, `spec-077` — governing graph for the portable gate scope.
- Edited substrate — `.claude/hooks/enforce-node-before-artifact.sh` (is_substrate→always_ignore+is_governed), `.claude/role-scope.json` (_comment reframe + example path), `CLAUDE.md` (3-layer reframe + §Portability); created `.claude/role-scope.example.json`.
- Edited nodes — 6 feature/story/spec-077 status `draft`→`implemented`; spec-077 realized-AC notes.

## Subagent consultations

> Consulting role retains scope authority; consulted role provides information only.

- `architect` → `qa` — Question: design the Phase-D verification matrix (no-regression vs prior Phase E + consumer simulation + careless-config + jq robustness). Response summary: re-run self-hosting matrix; consumer fixture (developer→src/**); careless fixture (nodes/** under a role); _comment-scalar jq check; table↔file consistency. Consultation only — Architect retained scope authority and authored the substrate.

## Closing summary

> Filled at `/session-close`.

**Outcome:** <pending>.

**Pending / next steps:** <pending>.

**Merge decision:** <pending>.
