---
category: adr
id: adr-012-mandatory-active-role-hard-jurisdiction
parent: "[[cap-02-role-scoped-agents]]"
artifacts:
  - "[[CLAUDE.md]]"
  - "[[.claude/role-scope.json]]"
  - "[[.claude/agents/product-owner.md]]"
  - "[[.claude/agents/architect.md]]"
  - "[[.claude/agents/qa.md]]"
  - "[[.claude/agents/developer.md]]"
  - "[[.claude/agents/devops.md]]"
status: accepted
created: 2026-05-15
updated: 2026-05-15
supersedes:
superseded-by:
---

# ADR 012 — Active-role marker is mandatory; per-role path-scope is hard-enforced

> One decision = one ADR. ADR format = Nygard convention, not in audited `bibliography/sources/`. Architect audit grid: Jones Ch 7 seven fundamental topics.

## Status

accepted (human-confirmed at session close 2026-05-15).

## Context

The Claude Code harness exposes **no signal** to a hook indicating which `claude --agent <role>` (or Task `subagent_type`) is active: no documented environment variable; the git branch encodes the session, not the role; the session-doc Log lags (manual `/session-log`). Node-before-artifact ([[adr-011-hard-enforcement-no-human-override]]) is path-based and hard-enforceable without a role signal. Per-role *path* scope ("PO ≠ Architect") cannot be hard-enforced unless the active role is made explicit. Relates to [[adr-005-subagent-dispatch-not-authority-transfer]] and [[adr-010-human-directed-ai-maintained]]; lineage: SQA role independence — a role must be able to refuse out-of-jurisdiction direction (Jones Ch 5 p. 282), named once here.

## Decision

An explicit marker `.claude/.active-role` (one role name) is **mandatory**. The gate denies *all* in-scope substrate writes when the marker is absent/empty, and denies any write whose path is outside the active role's entry in `.claude/role-scope.json` (the authoritative map; the CLAUDE.md § Role jurisdiction table mirrors it). `.claude/.active-role` is runtime state — **gate-ignored**, like `.obsidian/` UI state — and is set by the `/role <name>` ceremony. Soft jurisdiction (CLAUDE.md text + agent Workflow) is retained as documentation and behaviour, but is no longer the *only* layer.

## Consequences

**Positive:** "each role does its own" becomes structural; no-role-declared is a hard stop, not a silent path; composes with subagent=consultation (a consulted role cannot author out-of-role because the marker reflects the human's declared role).

**Negative:** a `/role` ceremony is required; `.claude/role-scope.json` is new state that must stay consistent with the CLAUDE.md table (asserted by [[spec-075-hard-role-jurisdiction]]); **residual risk: marker/reality desync** if the human changes hat without `/role` — this is a *correctness* risk, not an enforcement-bypass risk, and is acceptable because role switching in SEM-IA is already an explicit ceremony.

**Neutral:** `bibliography/**` is gate-ignored so it carries no role-scope entry.

## Alternatives considered

- **Soft jurisdiction only** — rejected: the status quo the user explicitly rejected; same softness that failed.
- **Per-agent `tools:` allowlist** — rejected as the primary mechanism: tool-level, not path-level; cannot express "PO may touch specs but not ADRs". May still be added later as a complementary coarse layer.
- **Parsing the transcript for the last subagent** — rejected: fragile, undocumented.

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

- **4. Decomposition into functional components:** roles ↔ substrate path partitions.
- **5. Linkage:** `.claude/.active-role` + `role-scope.json` ↔ the gate.
- **7. Security:** mandatory-marker fail-closed (no marker → no write).
- Others: not materially affected.

## Source

- Skill: `architect-architecture-design`.
- Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), Ch 7 § Software Architecture (pp. 470–475).
- ADR format: Michael Nygard — convention, not in audited `bibliography/sources/`.
