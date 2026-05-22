---
type: adr
parent: cap-13-portability
status: superseded
created: 2026-05-14
updated: 2026-05-22
maintained_by_role: architect
superseded-by:
  - adr-015-one-unified-artifact-graph
---

# ADR 004 — Substrate and content occupy disjoint directories; the substrate is the reusable framework, the content is the project

> Documents an architectural decision significant enough to be cross-cutting, reversible only with effort, and questioned by future readers. **One decision = one ADR**. Inmutable once accepted: if the decision changes, create a new ADR that `supersedes` the previous one.
>
> The ADR format (Context / Decision / Consequences) is widely-adopted industry convention (Michael Nygard) but is **not in audited `bibliography/sources/`** — it is cited here as practitioner convention. The Architect role's authoritative criteria live in `architect-architecture-design` (Jones BP #14 + Ch 7 § Software Architecture). When an architectural decision is recorded as an ADR, the seven fundamental topics (Jones Ch 7 p. 470: structure / data / interfaces / decomposition / linkage / performance / security) are the audit grid.

## Status

**accepted** — the separation is operating in the repo layout today. Substrate is `.claude/` + `_obsidian/` + `bibliography/` + `CLAUDE.md` + `LICENSE`; content is `nodes/` + `sessions/`. The CLAUDE.md § *Repo structure* table encodes the partition; the substrate directories carry no project-specific authoring; the content directories carry no framework-defining material.

## Context

The vision claims that *"anyone running a software engineering effort — from a solo builder to a large enterprise"* can operate under SEM-IA. The capability [[cap-13-portability]] declares the substrate must be liftable into a new project. Three forces are in tension:

1. **The substrate must be cleanly liftable.** A new project copying SEM-IA's framework should be able to take a known, bounded set of files and have a working framework — without inheriting SEM-IA's vision, goals, capabilities, or session history. If framework and content interleave at the directory level, the lifting operation becomes archaeological.
2. **The content must inherit substrate properties unchanged.** A node authored in any project must obey the same template, the same frontmatter schema, the same citation discipline. If the framework rules live inside the content directories (per-project copies), drift between projects is inevitable and the framework's claim of universality collapses.
3. **Substrate updates must propagate cleanly.** When the substrate evolves (a new skill, a corrected template, a tightened citation rule), downstream projects need a clear merge path that does not require manually patching content. Substrate-as-package or substrate-as-base requires the substrate to live in directories that don't carry project content.

A symmetric problem arises in reverse: content changes must not require substrate updates. Adding a new node should never touch a `.claude/` file or a `_obsidian/` template; if it does, the substrate has bled into content.

## Decision

We adopt **a hard partition** between two directory sets:

- **Substrate (reusable framework):**
  - `.claude/` — agents, skills, slash commands, meta-templates, settings, role catalog.
  - `_obsidian/` — node templates, base views (future).
  - `bibliography/` — audited primary sources, the navigable index, the per-skill traceability record.
  - `CLAUDE.md` — the universal contract; loaded by Claude Code into every conversation in this repo and into every subagent dispatch.
  - `LICENSE` — the legal substrate.

- **Content (project-specific):**
  - `nodes/` — the project's vision, goals, capabilities, features, stories, specs, ADRs.
  - `sessions/` — the project's session documents.

A file belongs to exactly one set. Substrate files never name a specific node ID, a specific goal, or a specific feature of the host project. Content files instantiate the substrate's schemas (frontmatter, sections, citation pattern) but never modify the schemas themselves.

A new project lifting the substrate copies the substrate set verbatim, starts a fresh `nodes/` and `sessions/`, and produces its own content under the inherited rules.

## Consequences

**Positive:**

- **Portability becomes a directory operation.** Lifting SEM-IA into a new project is `cp -r .claude _obsidian bibliography CLAUDE.md LICENSE <new-project>/`. The substrate is the unit of portability; the operation is mechanical.
- **Substrate updates can be cherry-picked.** A new skill in `.claude/skills/` can be pulled into a downstream project without touching content. A corrected template in `_obsidian/templates/` propagates without merge conflicts on `nodes/`.
- **Content drift between projects is structurally prevented.** Two projects running under the same substrate share template, schema, citation discipline by construction. The framework's universality claim is structurally — not socially — enforced.
- **Audit surface is bounded.** A reviewer auditing the framework reads `.claude/` + `_obsidian/` + `bibliography/` + `CLAUDE.md`; a reviewer auditing the project reads `nodes/` + `sessions/`. The two audits are orthogonal.
- **Subagent dispatch and `claude --agent <role>` inherit the contract cleanly.** Every Claude Code invocation in the repo loads `CLAUDE.md` automatically; the agent files in `.claude/agents/` are the role-specific layer; both live in substrate. The framework's operating mechanics are *built into the substrate, not into the content*.

**Negative:**

- **The hard partition occasionally pushes against natural placement.** A project-specific deviation from the substrate (e.g., a non-standard template variant for a particular project type) has nowhere clean to live. It must either go into the substrate (polluting universality) or into the project content (breaking the framework's template contract). The framework currently resolves this by forbidding such deviations; future projects may push for a third tier (project-local overrides).
- **Templates are read-only from content's perspective.** A node author who wants to alter a template for their specific use case must change the substrate, not the node. This is the right default (universality), but it raises the cost of legitimate template evolution.
- **The substrate is not yet packaged.** Lifting is currently fork-and-adapt (per [[cap-13-portability]] Implementation A); there is no `sem-ia init` command, no installable package. The partition is necessary but not sufficient for frictionless portability.
- **`CLAUDE.local.md` is a deliberate exception.** Local preferences live at the repo root in a gitignored `CLAUDE.local.md` (CLAUDE.md § *Local preferences*). It is substrate-tier in location (alongside CLAUDE.md) but content-tier in nature (project-specific). The exception is explicit and small, but it is an exception to the otherwise clean partition.

**Neutral:**

- **The partition does not specify a delivery format.** Whether the substrate is delivered as a directory copy, a git submodule, a package, or a cookiecutter template is downstream of the partition. [[cap-13-portability]] Implementation A names the directory-copy approach; Implementation B names packaging; both honour this ADR.
- **The substrate / content distinction is not Jones-anchored.** Jones speaks of reusable artifacts (BP #26, 15 reusable artifact types) but does not prescribe a directory-level separation for methodology frameworks. The decision derives from the portability claim of the vision, not from Jones directly. The Architect skill on reusability strategy applies in spirit.
- **Sessions live in content even though they are operational scaffolding.** A session is project-specific by definition (it records what happened on *this* project), so `sessions/` belongs to content. The slash commands that operate sessions live in substrate; the artifacts the commands produce live in content. This split is correct and intentional.

## Alternatives considered

- **All files in one flat `sem-ia/` directory.** Rejected. Mixing substrate and content destroys portability; every fork operation becomes manual archaeology, and substrate updates require per-project patching.
- **Substrate as a separate repository, content as another repository, linked by submodule.** Considered seriously. Real benefit: substrate is independently versioned and consumable as a dependency. Real cost: doubles the repository count for every project; complicates the universal-`CLAUDE.md`-loading mechanism (CLAUDE.md must live at the project root for Claude Code to pick it up, not in the submodule); submodule semantics are friction-laden for non-git-expert contributors. **Deferred, not rejected** — this may become Implementation B of [[cap-13-portability]] when external-author portability is exercised. For now the single-repo partition is the lower-friction default.
- **Substrate as an installable package (`pip install sem-ia` or `npm i sem-ia`).** Deferred. Would be Implementation C of [[cap-13-portability]]; not currently implemented; depends on a stable substrate API surface which the framework does not yet guarantee.
- **`.sem-ia/` hidden directory holding all substrate.** Rejected. Mixing `.claude/` (already required at the top level for Claude Code) with other substrate directories under a single hidden parent breaks Claude Code's discovery conventions; would require fighting the harness rather than leveraging it.
- **No partition; rely on naming conventions only.** Rejected. Naming conventions degrade under time pressure; structural partition does not.

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

- **1. Overall structure:** Materially affected. The top-level directory layout of every SEM-IA project *is* this partition. It is the most visible structural property of the framework.
- **2. Data structure:** Materially affected. Schemas (templates, frontmatter contract, citation patterns) live in substrate; instances live in content. The data architecture of the framework is the substrate; the data architecture of any project under it is the content.
- **3. Interfaces to outside world:** Materially affected. The contributor encounters substrate via `CLAUDE.md` (universal contract) and via the editor's view of `.claude/` and `_obsidian/`; encounters content via `nodes/` and `sessions/`. The partition is the contributor's mental model of "what is the framework vs what is my project".
- **4. Decomposition into functional components:** Materially affected. The framework decomposes into: agents (substrate), skills (substrate), templates (substrate), bibliography (substrate), session ceremony (substrate-defined / content-instantiated), nodes (content). Each component is independently replaceable; the partition defines the replacement boundaries.
- **5. Linkage / information transmission among components:** Affected. Content nodes link to substrate via wikilinks to skill files when explaining their authoring lineage (e.g., a node's *"Authored via `po-vision`"* line). The linkage is one-way: content → substrate. Substrate never links to content. This asymmetry is part of the portability property.
- **6. Performance attributes:** Not materially affected. Directory operations are cheap; the partition affects no runtime path. Not applicable.
- **7. Security attributes:** Indirectly affected. A downstream project that pulls in the substrate inherits the substrate's audit posture (bibliography, citation discipline). Substrate is the trusted base; content is the variable. Compromise of substrate would affect every project under it — analogous to a compromised base image. The partition makes this trust boundary visible.

## Source

- Skill: `architect-architecture-design`.
- Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), Ch 7 § Software Architecture (pp. 470–475) — seven fundamental topics; BP #26 *Reusability* (pp. 99–101) as the conceptual neighbour (the substrate is the framework's reusable layer).
- CLAUDE.md § *Repo structure* — the substrate-vs-content table; CLAUDE.md § *Local preferences* — the explicit `CLAUDE.local.md` exception.
- ADR format: Michael Nygard, *Documenting Architecture Decisions* (industry convention) — **not in audited `bibliography/sources/`**.
- Capability anchor: [[cap-13-portability]] (the property this decision materialises).
