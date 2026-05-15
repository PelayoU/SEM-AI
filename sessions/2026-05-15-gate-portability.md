---
category: session
id: 2026-05-15-gate-portability
date: 2026-05-15
participants: [architect]
related-nodes: []
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

## Artifacts touched

- Created `sessions/2026-05-15-gate-portability.md` — this session doc.

## Subagent consultations

> Consulting role retains scope authority; consulted role provides information only.

- (none yet)

## Closing summary

> Filled at `/session-close`.

**Outcome:** <pending>.

**Pending / next steps:** <pending>.

**Merge decision:** <pending>.
