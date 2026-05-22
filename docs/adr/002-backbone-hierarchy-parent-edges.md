---
type: adr
parent: vision-001-sem-ai
status: accepted
created: 2026-05-14
updated: 2026-05-22
maintained_by_role: architect
---

# ADR 002 — Backbone hierarchy with `parent:` as the formal edge; wikilinks for narrative; ADRs cross-cut

> Documents an architectural decision significant enough to be cross-cutting, reversible only with effort, and questioned by future readers. **One decision = one ADR**. Inmutable once accepted: if the decision changes, create a new ADR that `supersedes` the previous one.
>
> The ADR format (Context / Decision / Consequences) is widely-adopted industry convention (Michael Nygard) but is **not in audited `bibliography/sources/`** — it is cited here as practitioner convention. The Architect role's authoritative criteria live in `architect-architecture-design` (Jones BP #14 + Ch 7 § Software Architecture). When an architectural decision is recorded as an ADR, the seven fundamental topics (Jones Ch 7 p. 470: structure / data / interfaces / decomposition / linkage / performance / security) are the audit grid.

## Status

**accepted** — the decision is operating across every node in `nodes/`. CLAUDE.md § *The graph* declares the backbone *vision → goals → capabilities → features → stories → specs* with ADRs cross-cutting from any level; `_obsidian/templates/*.md` enforce `parent:` in frontmatter for every non-vision node; the eight existing capability and goal nodes in the bootstrap demonstrate the property in force.

## Context

A traceability claim is structurally meaningful only if the graph that carries it is **acyclic, single-parent, and walkable in both directions**. Two forces are in tension:

1. **Audit demands a uniquely determined parent chain.** The vision's claim *"audit becomes inspection of the substrate; it is no longer reverse-engineering of the product"* (vision-sem-ia Statement) holds only if walking from any artifact to the vision is deterministic. Multi-parent graphs branch at audit time; the auditor has to choose which parent edge to follow, and the audit becomes a search rather than a walk. Goal G1's M-criterion *"end-to-end navigation from `vision-sem-ia` to a spec-affecting code node succeeds with no broken `parent:` edges"* requires this property.
2. **Real-world artifacts have horizontal relationships.** A feature does cross-reference another feature. A spec does depend on an ADR. A goal does relate to another goal. Forcing all such relationships through the formal edge would either pollute the parent chain (tree becomes DAG, audit becomes search) or hide the relationships (lose discoverability).

A third tension: **some decisions cut across the entire hierarchy and have no single natural parent**. An architectural decision about session model affects every category of node; an architectural decision about citation discipline affects every goal. Pinning such decisions under one arbitrary parent loses the cross-cutting nature; leaving them parentless breaks the universal navigation property.

## Decision

We adopt a **strict tree on `parent:`** with the following rules:

1. **The backbone hierarchy is `vision → goal → capability → feature → story → spec`.** Every non-vision node has exactly one `parent:` field naming its immediate hierarchical parent. The chain is acyclic and single-parent by construction.
2. **`[[wikilinks]]` in node bodies carry horizontal references** — narrative cross-references between siblings, cousins, related goals, related capabilities, prior ADRs. Wikilinks activate Obsidian's backlinks pane and the graph view. They are not formal edges; the `parent:` field is.
3. **ADRs are the cross-cutting node class.** An ADR's `parent:` is the *highest applicable backbone node* — typically the vision itself for paradigm-level decisions, the affected goal for goal-scoped decisions, the affected capability for capability-scoped decisions. ADRs are read as cross-cutting because their effects apply across all descendants of their parent; the formal edge places them at the level of greatest applicability.
4. **No `also-relates-to:`, `depends-on:`, or `dimensions-affected:` frontmatter fields.** The framework deliberately *forbids* these. Horizontal relationships live in node bodies as wikilinks, never as frontmatter edges. This is an active design constraint, not a default.

## Consequences

**Positive:**

- **Deterministic audit walk.** From any node, the parent chain to the vision is unique and computable by simple traversal. The M-criterion of [[goal-01-self-bootstrap-validation]] is structurally satisfiable.
- **Backlinks remain rich.** Obsidian's backlinks pane shows every wikilink reference, so the loss of horizontal frontmatter edges does not lose horizontal navigation — it just moves it from machine-structured to body-structured form.
- **Two-tier semantics.** Formal traceability (frontmatter) and narrative reference (body wikilinks) are explicitly distinguished. Auditors know which edges to walk; readers know which references to follow narratively.
- **ADRs find their natural home.** A cross-cutting decision parent-linked to its highest-applicable backbone node makes the scope of the decision visible in the graph itself — an ADR under `vision-sem-ia` *is* a paradigm decision; an ADR under a specific capability *is* a capability-scoped decision.
- **Substrate portability.** A new project inheriting the substrate inherits the parent-tree property unchanged; the rule is graph-theoretic, not domain-specific.

**Negative:**

- **Some real-world relationships are awkward to express.** A feature that genuinely supports two goals equally (cross-goal feature) has to pick one parent and put the other as a body wikilink — a slight semantic loss. The cap-08 / cap-09 / cap-10 capabilities show this pattern: their bodies say *"also serves [[goal-X]]"* in the statement, but the `parent:` points to one goal only.
- **Frontmatter cannot answer "what depends on this?".** Without a `depends-on:` field, dependency analysis is a wikilink-mining exercise rather than a frontmatter scan. Tooling that wants to compute a dependency graph must parse node bodies.
- **ADR parent choice is judgmental.** An ADR that touches two goals or two capabilities equally requires a parent-selection judgement. We resolve it conventionally (pick the higher one in the backbone, or the most-affected one) but the rule does not eliminate the judgement.
- **Single-parent is a constraint readers must learn.** New contributors familiar with multi-parent ontologies (Topic Maps, RDF, etc.) will instinctively reach for `also-relates-to:` and find it forbidden. The discipline pays off, but the learning curve is real.

**Neutral:**

- **The choice is graph-theoretic, not Jones-anchored.** Jones speaks of architectural decomposition (Ch 7 topic 4) and linkage (topic 5) but does not prescribe a tree-vs-DAG choice for the substrate of a methodology. The decision is grounded in audit-walk determinism, which is a consequence of the vision's claim, not a Jones requirement.
- **The wikilink convention is Obsidian-native** *(Obsidian.md community convention)*. It works on any markdown viewer that resolves `[[id]]`; it degrades gracefully (to literal text) on viewers that don't. Not in audited `bibliography/sources/`; cited as community convention.
- **Status is independent of parent topology.** A node's status (`draft`, `active`, `superseded`, etc.) is a property of the node, not of its position in the tree. The tree is a *structural* edge; status is a *lifecycle* attribute.

## Alternatives considered

- **DAG (multi-parent) graph with `parents:` as an array.** Rejected. Makes the audit walk non-deterministic (auditor must pick which parent to follow at each branching node), inflates the formal edge set, and removes the cleanest answer to *"what's the strategic origin of this artifact?"*. The audit value of the vision-to-code claim collapses.
- **Flat graph with all relationships as typed edges in a separate manifest.** Rejected. Adds a second source of truth alongside frontmatter; requires tooling to render; breaks the "every node is human-readable on its own" property; defeats Obsidian-native browsing.
- **`parent:` plus `also-relates-to:` array in frontmatter.** Rejected as historical alternative — the framework actively *eliminated* this in an earlier iteration (CLAUDE.md § *Frontmatter* lists `also-relates-to`, `depends-on`, `dimensions-affected` as "not used in this project — eliminated by design"). The rationale: ambient horizontal frontmatter encourages over-decoration and turns frontmatter into a knowledge graph that competes with the body.
- **ADRs in a separate directory tree with their own hierarchy.** Rejected. Breaks the property that *all artifacts of the project live in `nodes/`*. Separating ADRs into a parallel hierarchy duplicates the navigation surface and complicates substrate portability.
- **No formal edges at all; everything via wikilinks.** Rejected. Audit cannot deterministically walk a graph that has no canonical edge class. The vision's audit claim is structurally unfounded.

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

- **1. Overall structure:** Materially affected. The strict tree on `parent:` *is* the principal structural property of the SEM-IA graph. Every other structural concern (substrate vs content, ADR placement, session model) builds on top of this rule.
- **2. Data structure:** Materially affected. Frontmatter schema is constrained: every non-vision node has exactly one `parent:` field; no `also-relates-to`, `depends-on`, `dimensions-affected`. The constraint is encoded in `_obsidian/templates/*.md` and in CLAUDE.md § *Frontmatter*.
- **3. Interfaces to outside world:** Affected. The contributor sees the graph through Obsidian (graph view, backlinks pane) and through plain markdown readers. The wikilink syntax is the contributor's primary horizontal-navigation interface; the parent-frontmatter edge drives the formal traversal.
- **4. Decomposition into functional components:** Materially affected. The seven backbone categories (vision, goal, capability, feature, story, spec) + ADRs as cross-cutting class are *the* decomposition of the framework's artifact space. The category labels are not free — each maps to a template with required sections and to one or more authoring skills.
- **5. Linkage / information transmission among components:** Materially affected. Linkage between nodes happens through two channels: formal (`parent:` for hierarchical traceability) and narrative (`[[wikilink]]` for cross-reference). The two-tier separation is a load-bearing decision: it keeps audit walks deterministic while allowing narrative richness.
- **6. Performance attributes:** Not materially affected. Tree traversal is O(depth); the SEM-IA backbone is six levels deep; performance is uninteresting at this scale. If a project ever grew to a graph of 10,000+ nodes, this might require attention; not applicable today.
- **7. Security attributes:** Not materially affected. The graph property is structural, not authentication-related. Access control on nodes is repository-level (git permissions), not node-level. No new security surface introduced.

## Source

- Skill: `architect-architecture-design`.
- Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), Ch 7 § Software Architecture (pp. 470–475) — seven fundamental topics; topic 5 (linkage) anchors the two-tier formal/narrative distinction.
- CLAUDE.md § *The graph*, § *Wikilinks*, § *Frontmatter* — the substrate that operationalises this decision; the explicit "Not used in this project" clause documents the negative choice.
- GISF UC3M `gisf-life-cycle.pdf` slide 53 — the source of the backbone hierarchy *vision → goals → capabilities → features → stories → specs*.
- `_obsidian/templates/*.md` — template-level enforcement.
- ADR format: Michael Nygard, *Documenting Architecture Decisions* (industry convention) — **not in audited `bibliography/sources/`**.
- Obsidian wikilink convention: Obsidian.md (community convention) — **not in audited `bibliography/sources/`**.
- Capability anchors: [[cap-01-vision-to-code-audit]] (traversal property), [[cap-11-adr-capture]] (cross-cutting ADR class).
