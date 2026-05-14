---
category: capability
id: cap-01-vision-to-code-audit
parent: "[[goal-01-self-bootstrap-validation]]"
status: draft
mvp: go
created: 2026-05-14
updated: 2026-05-14
---

# Capability 01 — Vision-to-code navigation and audit

> Authored via `po-capabilities`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54 (capability = ability to achieve a goal regardless of implementation; don't imply a particular implementation). MVP filter: slide 69. Cagan four risks: slide 64.

## Statement (slides 97–99 form)

In order to **verify that any project decision can be traced back to its strategic origin** (parent goal [[goal-01-self-bootstrap-validation]] — also serves [[goal-02-tfm-public-artifact]] and [[goal-03-portability-proof]]),
as **anyone running or auditing a software engineering effort under SEM-IA**,
I want **the ability to walk from any artifact in the project to its strategic origin (vision) along an unbroken parent chain, and back down to any code-affecting artifact, with the navigation surfaced through the human's editor**.

## Implementation-agnostic test

- **Implementation A** (current): markdown nodes with `parent:` frontmatter + `[[wikilinks]]` in body; Obsidian as the editor surface with graph view, backlinks pane, and the show-hidden-files plugin exposing `.claude/`; navigation by clicking through.
- **Implementation B** (alternative): knowledge graph database (Neo4j-class) with typed edges; navigation via Cypher queries or a custom UI.

A third plausible: traceability metadata in a separate manifest consumed by a generic doc viewer. The capability is *audit-by-navigation*; the editor surface is implementation.

## MVP Go / No-go

- **Value risk:** Without this capability, the vision's claim *"audit becomes inspection of the substrate"* is unfounded. Highest-value capability of the framework.
- **Usability risk:** Low for users who know Obsidian; backbone hierarchy is documented in CLAUDE.md.
- **Viability risk:** Proven — this very session demonstrates it.
- **Business viability risk:** N/A.

**Decision: Go** — structural foundation; without it no other capability adds value.

## Non-overlap with sibling capabilities

- Sibling: [[cap-02-role-scoped-agents]] — independent. Role scope is about *who authors*; this is about *how authored artifacts relate and are navigated*.
- Sibling: [[cap-11-adr-capture]] — adjacent. ADRs cross-cut the linear backbone; this capability includes the navigation surface that ADRs hang from.

## Non-coverage

- **Not about the storage substrate.** Markdown, graph DB, or other is implementation.
- **Not about audit method.** Sampling, exhaustive verification, etc. are QA-scope.
- **Not about content correctness.** Whether artifacts contain correct claims is [[cap-08-citation-discipline]]'s territory.
- **Not about filtered views.** Query-based filtered navigation is [[cap-14-filtered-graph-views]] (deferred / planned).

## Source

- Skill: `po-capabilities`.
- GISF UC3M `gisf-life-cycle.pdf` slides 53–54, 69; `gisf-discovery.pdf` slides 97–99.
- Cagan four risks: `gisf-life-cycle.pdf` slide 64.
- Cross-link to vision: [[vision-sem-ia]] Statement *"audit becomes inspection of the substrate; it is no longer reverse-engineering of the product"*.
- Features delivering this capability: 8 node templates, CLAUDE.md graph definition, `.obsidian/` config (graph.json, workspace.json, show-hidden-files plugin), 5 PO authoring skills (po-vision / po-goals / po-capabilities / po-feature-decomposition / po-spec-gherkin).
