---
category: adr
id: adr-015-one-unified-artifact-graph
parent: "[[vision-sem-ia]]"
artifacts:
  - "[[CLAUDE.md]]"
  - "[[.claude/agents/product-owner.md]]"
  - "[[.claude/agents/architect.md]]"
  - "[[.claude/agents/qa.md]]"
  - "[[.claude/agents/developer.md]]"
  - "[[.claude/agents/devops.md]]"
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
  - "[[.claude/role-scope.json]]"
status: proposed
created: 2026-05-15
updated: 2026-05-15
supersedes: "[[adr-004-substrate-content-separation]], [[adr-007-obsidian-as-editor-surface]], [[adr-012-mandatory-active-role-hard-jurisdiction]], [[adr-013-gate-scope-is-project-configurable]]"
superseded-by:
---

# ADR 015 — One unified artifact graph; doctrine in mechanism; generic editor-agnostic contract

> One decision = one ADR. ADR format = Nygard convention, not in audited `bibliography/sources/`.

## Status

proposed.

## Context

The graph reached 281 nodes (1 vision / 3 goals / 13 caps / 77 features / 96 stories / 77 specs / 14 ADRs) and CLAUDE.md 341 lines. Root cause: a framework self-build applied product-decomposition machinery (feature→story→spec→Gherkin) to *prose*, and the doctrine tried to *classify* artifacts (substrate vs content vs management; the "3-layer model"; the spec-075/adr-012 "mirror invariant") when there is only one uniform thing. Obsidian leaked in as if it were the framework. CLAUDE.md became a doctrine essay restating the same rule ~21× — soft context, the original null-enforcement failure this project exists to fix.

## Decision

1. **One rooted artifact graph.** Root = `vision`. Every node carries `parent:` up to `vision`; leaf artifacts (skills, code, config) are connected by a node's `artifacts:` reference. **One rule:** no artifact is created or modified unless a parent node already references it. This subsumes "node-before-artifact" and abolishes the substrate/content/management trichotomy, the 3-layer model, and the mirror invariant — there are no artifact categories, only the rule.
2. **Doctrine lives in mechanism, not CLAUDE.md prose.** The gate enforces the rule; `.claude/hooks/role-reinforce.sh` injects role + scope + checklist every turn; `.claude/agents/<role>.md` carries per-role behaviour; skills carry methods (including node structure — ADR-009). CLAUDE.md contains no enforceable-rule prose.
3. **The agent's identity is framework-first, role-second.** CLAUDE.md and agent files address the agent as *being* the framework, not as a role that must remember rules — discipline is identity, not memory (this is the strongest form of "doctrine in mechanism"). CLAUDE.md opens *"You are this framework — a discipline for software-engineering management with one inviolable rule…"*; each `agents/<role>.md` opens *"You are this framework, in the **<role>** role."* Generic, project-agnostic, no "SEM-IA" string, no editor/visual layer. The project's identity/vision/graph lives in `nodes/`.
4. **The visual/navigation layer is the operator's free choice.** Obsidian is not the framework — `_obsidian/templates/` is removed (node structure is carried by authoring skills), `.obsidian/` is personal tooling (`.gitignore`d). The `[[id]]` reference encoding in `parent:`/`artifacts:` STAYS — it is framework data, parseable by any tool, independent of Obsidian.
5. **Minimal graph.** `feature` = one per skill (`artifacts:` = that `SKILL.md`), parented to its role-discipline capability. No `story`/`spec` wrappers in a framework self-build (the `SKILL.md` *is* the spec/criteria, ADR-009). `story`/`spec`/Gherkin remain available vocabulary for real product projects (e.g. a dApp), not instantiated here.

## Consequences

**Positive:** the contract becomes scannable; portability is by construction (no special-casing); one rule replaces all the classification doctrine; rules cannot be forgotten because mechanism carries them; ~281 → ~60–70 nodes.

**Negative:** mass node deletion and a CLAUDE.md rewrite — mitigated: history-preserving (branch-only, `main` untouched, `git show <sha>:nodes/…` recovers anything; reversibility anchor `1b92365`). Supersedes 4 ADRs.

**Neutral:** 37 skills, 5 agents (bodies), 3 hooks, `role-scope.json`, `sessions/` history are untouched in substance; `[[id]]` encoding kept; superseded ADRs remain in history with `superseded-by:`.

## Alternatives considered

- **Rewrite the 3-layer/jurisdiction prose better** — rejected: better prose is still soft context; the model itself is redundant with the gate.
- **Keep story/spec wrappers, just thin them** — rejected: 3 nodes per skill of ceremony with no information beyond the `SKILL.md`.
- **Literal history burn** — rejected: irreversible, destroys the audit trail the thesis values.

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

- **1. Structure / 4. Decomposition:** one graph, one rule, doctrine relocated to its enforcing mechanisms.
- **2. Data:** `[[id]]` reference encoding is the canonical, editor-agnostic link format.
- **5. Linkage:** CLAUDE.md/agents → pointers to gate/hook/skills; no duplicated content.
- 3, 6, 7 not materially affected.

## Source

- Skill: `architect-architecture-design`. Jones Ch 7 §Software Architecture pp. 470–475. ADR format: Nygard (convention, not in audited bibliography). Absorbs the uncommitted `adr-014` (doctrine-in-mechanism). In force, unchanged: `[[adr-001-sessions-as-git-branch]]`, `[[adr-002-backbone-hierarchy-parent-edges]]`, `[[adr-003-citation-mandate]]`, `[[adr-009-skill-as-canonical-method]]`, `[[adr-010-human-directed-ai-maintained]]`, `[[adr-011-hard-enforcement-no-human-override]]`.
