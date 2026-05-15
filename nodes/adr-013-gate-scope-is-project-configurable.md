---
category: adr
id: adr-013-gate-scope-is-project-configurable
parent: "[[cap-13-portability]]"
artifacts:
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
  - "[[.claude/role-scope.json]]"
  - "[[.claude/role-scope.example.json]]"
  - "[[CLAUDE.md]]"
status: superseded
created: 2026-05-15
updated: 2026-05-15
supersedes:
superseded-by: "[[adr-015-one-unified-artifact-graph]]"
---

# ADR 013 — The gate's governed scope is the project's role-scope.json glob union, not a hardcoded layout

> One decision = one ADR. ADR format = Nygard convention, not in audited `bibliography/sources/`. Architect audit grid: Jones Ch 7 seven fundamental topics.

## Status

proposed.

## Context

[[adr-004-substrate-content-separation]] fixes substrate (reusable framework) vs content (`nodes/`+`sessions/`) **structurally**, but only for self-hosting; its Consequences explicitly defer `sem-ia init` (fork-and-adapt) and note downstream portability is untested (`[[cap-13-portability]]` viability risk = highest). The merged gate ([[feature-072-node-before-artifact-gate]], [[adr-011-hard-enforcement-no-human-override]], [[adr-012-mandatory-active-role-hard-jurisdiction]]) hardcodes `is_substrate()` to SEM-AI's self-hosting layout (`.claude/**`,`_obsidian/**`,`CLAUDE.md`,`LICENSE`). Dropped into a consumer project (mobile app) it gates the *imported, never-edited framework* and leaves the consumer's product code (`src/**`,`ios/**`) **ungated** — the inverse of intent — and the CLAUDE.md Orient block ("SEM-IA *is* the substrate") misdirects the consumer's agent. Forces: (1) gate must be project-portable (`[[cap-13-portability]]`/`[[goal-03-portability-proof]]`); (2) SEM-AI self-hosting behaviour must not regress; (3) no new mechanism/config surface (ADR-004 deferred packaging; a second config file duplicates `role-scope.json` and risks the drift adr-012/spec-075 guard against); (4) universal SEM-IA invariants (`nodes/`/`sessions/` per ADR-004, the `/role` escape valve `.claude/.active-role`, the bootstrap marker) must never become gated by a careless project config.

## Decision

We adopt the project's `.claude/role-scope.json` as the single source of the gate's governed scope. "Is this path governed?" = **the union of every glob across every role in `role-scope.json` is the project's governed artifact space; per-role membership is jurisdiction (ADR-012)**. The hardcoded self-hosting in-scope set in `is_substrate()` is removed. A small **hardcoded always-ignore safety guard** runs *first* and *wins* over the union: `nodes/**`, `sessions/**`, `bibliography/**`, `.git/**`, `.obsidian/**`, `.claude/.active-role`, `CLAUDE.local.md`, `/tmp/**`, `/var/folders/**`, any absolute path outside the repo. No new config file: `role-scope.json` is reframed in doctrine as the per-project gate configuration. A consumer project rewrites the role arrays to its product roots; the imported `.claude/**` is simply absent from the union → ungated (opt-in to protect via a maintainer-role glob). `.claude/role-scope.example.json` ships as a documented consumer pattern.

## Consequences

**Positive:** gate becomes project-portable with **zero new mechanism**; one file (`role-scope.json`) is the per-project gate config; `role-reinforce.sh` already reads it so reinforcement stays consistent; consumer projects gate their own code; the always-ignore guard makes the escape valve + management layer structurally unbreakable.

**Negative:** `role-scope.json` becomes load-bearing for *scope*, not only jurisdiction — a malformed/empty file means nothing is gated (fail-open on scope), mitigated by the always-ignore guard being independent of it and the existing fail-closed jq-missing/unparseable behaviour preserved. **Not byte-identical to the old gate:** hypothetical *unowned* `.claude/` paths (matched by old `.claude/*` but no role glob) become ungated. Acceptable: no such path exists in the repo, and an unowned path is unauthorable under any role anyway (ADR-012). Claim is "no regression on observable SEM-AI behaviour" (full 13-scenario matrix re-run), **not** universal byte-identity.

**Neutral:** `.claude/role-scope.example.json` is itself `.claude/` substrate → a governed path: governed by this ADR + `[[feature-077-portable-gate-scope]]` + `[[story-077-D-consumer-project-example]]`, architect-owned (added to the architect entry of `role-scope.json`). ADR-004's directory partition is unchanged (this is about *gate scope*, not layout). `sem-ia init` remains a deferred `[[cap-13-portability]]` Implementation-B follow-up, explicitly not built here.

## Alternatives considered

- **Keep hardcoded `is_substrate()` + a `--project-globs` env var** — rejected: adds mechanism, duplicates role-scope.json.
- **New `.claude/gate-scope.json`** — rejected: second source of truth, drift risk vs role-scope.json (the exact failure adr-012/spec-075 guard for the CLAUDE.md table).
- **Detect project type and switch layouts** — rejected: fragile, undocumented harness assumptions.
- **`sem-ia init` scaffolder that writes role-scope.json** — deferred (`[[cap-13-portability]]` Implementation-B), not built now.

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

- **1. Overall structure:** gate scope source moves from code to config.
- **2. Data structure:** `role-scope.json` gains a second semantic (scope union, not only jurisdiction).
- **4. Decomposition:** gate ↔ role-scope.json coupling replaces gate ↔ hardcoded set.
- **5. Linkage:** always-ignore guard → union → per-role checks ordering is now the load-bearing contract.
- **7. Security:** the always-ignore guard is the fail-safe trust boundary; empty-role-scope = fail-open-on-scope risk analysed.
- 3, 6 not materially affected.

## Source

- Skill: `architect-architecture-design`.
- Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), Ch 7 § Software Architecture (pp. 470–475).
- ADR format: Michael Nygard — convention, not in audited `bibliography/sources/`. Relates-to/refines `[[adr-004-substrate-content-separation]]` + `[[adr-012-mandatory-active-role-hard-jurisdiction]]`; capability anchor `[[cap-13-portability]]`.
