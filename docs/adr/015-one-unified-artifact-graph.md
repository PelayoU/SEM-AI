---
type: adr
parent: vision-001-sem-ai
status: proposed
created: 2026-05-15
updated: 2026-05-22
maintained_by_role: architect
supersedes:
  - ['adr-004-substrate-content-separation'
  - 'adr-007-obsidian-as-editor-surface'
  - 'adr-011-hard-enforcement-no-human-override'
  - 'adr-012-mandatory-active-role-hard-jurisdiction'
  - 'adr-013-gate-scope-is-project-configurable']
---

# ADR 015 - One unified artifact graph; the rule is an unenforced discipline

> One decision = one ADR. ADR format = Nygard convention, not in audited `bibliography/sources/`. (Rewritten clean: a prior automated edit mojibake-corrupted this file and it described an enforcement mechanism that was subsequently removed.)

## Status

proposed.

## Context

The graph reached 281 nodes + a 341-line CLAUDE.md: a framework self-build applied product-decomposition (feature/story/spec/Gherkin) to prose, and the doctrine tried to classify artifacts (substrate vs content vs management; a "3-layer model"; a "mirror invariant") when there is only one uniform thing. A hard PreToolUse gate + role-scope + per-turn reinforcement hooks were built (adr-011/012/013) to make the rule non-forgettable. The human then judged the mechanism's recursion/cost not worth it for this prose-heavy self-build and removed it.

## Decision

1. **One rooted artifact graph, one rule.** Root = `vision`. Every node carries `parent:` up to `vision`; non-node files (code, skills, config) are connected by a node's `artifacts:` reference. **The one rule: no file is created or changed unless a node in `graph/` names it.** No substrate/content/management categories, no 3-layer model, no mirror invariant - just the rule.
2. **The rule is an UNENFORCED discipline, stated plainly in CLAUDE.md.** All hooks were deleted, `settings.json` emptied, dead machinery removed (`role-scope.json`, `.active-role`, `/role`). Honest consequence: nothing prevents the rule being broken - it is the soft model whose failure originated this work, accepted knowingly by the human. The gate code survives in git history and can return when the framework is applied to a real product (`git show 51f3b80:.claude/hooks/...`). Per-role behaviour is in `.claude/agents/<role>.md`; methods are the skills.
3. **Identity is framework-first.** CLAUDE.md and agent files address the agent as *being* the framework, not a role that remembers rules. Generic, project-agnostic, no "SEM-IA" string, no editor/visual layer in the contract.
4. **The visual/navigation layer is the operator's free choice.** Obsidian is not the framework: `_obsidian/templates/` removed, `.obsidian/` is personal (`.gitignore`d). The `[[id]]` reference encoding stays - framework data, parseable by any tool.
5. **Minimal graph.** `feature` = one per skill (`artifacts:` = that `SKILL.md`). No `story`/`spec` wrappers in a framework self-build (the `SKILL.md` is the spec, ADR-009). `story`/`spec`/Gherkin remain available for real product projects.

## Consequences

**Positive:** scannable ~52-line contract; one rule replaces all classification doctrine; portability by construction; 281 -> ~64 nodes.

**Negative:** no enforcement - the rule depends on the agent holding it (the failure mode this project named). Mitigated only by reversibility: branch-only, `main` untouched, everything recoverable from git history.

**Neutral:** 37 skills, 5 agents, `sessions/` history untouched; `[[id]]` kept; superseded ADRs remain in history.

## Clarification (artifact/node ontology)

Everything created is an artifact. A *node* is the structured kind (has a template, lives in `graph/`, carries `parent:`/`artifacts:`); nodes govern the rest. A capability/goal/vision is a level of thinking; its written form is a node. The graph folder was renamed `nodes/` -> `graph/` (`git mv`, history preserved; pre-rename history at `git show 1b92365:nodes/...`).

## Source

- Skill: `architect-architecture-design`. Jones Ch 7 Software Architecture pp. 470-475. ADR format: Nygard (convention, not in audited bibliography). Absorbs the uncommitted `adr-014`. In force: `[[adr-001-sessions-as-git-branch]]`, `[[adr-002-backbone-hierarchy-parent-edges]]`, `[[adr-003-citation-mandate]]`, `[[adr-009-skill-as-canonical-method]]`, `[[adr-010-human-directed-ai-maintained]]`.
