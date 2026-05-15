---
category: capability
id: cap-11-adr-capture
parent: "[[goal-01-self-bootstrap-validation]]"
status: draft
mvp: go
created: 2026-05-14
updated: 2026-05-14
---

# Capability 11 — Cross-cutting architectural-decision capture

> Authored via `po-capabilities`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54. MVP filter: slide 69. Cagan four risks: slide 64.

## Statement (slides 97–99 form)

In order to **capture significant architectural decisions as durable artifacts that cross-cut the linear backbone** (parent goal [[goal-01-self-bootstrap-validation]] — the M-criterion G1-A explicitly demands ≥ 1 ADR exists — also serves [[goal-03-portability-proof]]),
as **the Architect (and the wider team that reads architectural rationale)**,
I want **the ability to record each architectural decision as a standalone artifact with status (proposed / accepted / superseded / deprecated), context, the decision itself, consequences in three directions (positive / negative / neutral), and alternatives considered — so the rationale survives the moment of decision and the supersession chain remains navigable**.

## Implementation-agnostic test

- **Implementation A** (current): markdown nodes under `nodes/adr-NNN-slug.md` using the `_obsidian/templates/adr.md` template; supersession tracked via `supersedes:` / `superseded-by:` frontmatter; ADRs can hang off any node level via `parent:`.
- **Implementation B** (alternative): ADR database with structured fields and supersession-chain queries; one row per decision; status transitions modelled as events.

A third plausible: ADRs as long-form comments adjacent to code modules. The capability is *architectural-decision capture as cross-cutting durable artifacts*, not the storage medium.

## MVP Go / No-go

- **Value risk:** Without this capability, architectural rationale lives only in heads or commit messages — both lossy. Future re-evaluation requires reconstruction from artifacts that did not preserve the *why*.
- **Usability risk:** Moderate — requires discipline to recognise *"this is an architectural decision"* moments. The Architect role/skill provides the heuristic.
- **Viability risk:** Proven — ADR template exists; format follows Nygard convention (flagged in the template as out-of-bibliography convention, not Jones-anchored authority).
- **Business viability risk:** N/A.

**Decision: Go** — required for G1-A and for any project that outlives short-term memory.

## Non-overlap with sibling capabilities

- Sibling: [[cap-01-vision-to-code-audit]] — adjacent. The backbone is hierarchical (vision → spec); ADRs cross-cut and can hang from any node level. cap-01 is the *traversal capability*; this is the *artifact class*.
- Sibling: [[cap-04-apply-architect-discipline]] — adjacent. cap-04 is *the Architect's discipline being applicable*; this capability is *the artifact class that captures decisions taken under that discipline*. Distinct but tightly coupled.

## Non-coverage

- **Not about decision quality.** Whether an ADR captures a *good* decision is the Architect's judgement (cross-link to `architect-architecture-design` when authoring features under this capability).
- **Not about ADR format details.** Nygard format (Context / Decision / Consequences) is the current convention; other formats (Y-Statements, Markdown Any Decision Record, etc.) would satisfy the capability.
- **Not about ADR discoverability tooling.** Search, indexing, dashboards are implementation.

## Source

- Skill: `po-capabilities`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54, slide 69; `gisf-discovery.pdf` slides 97–99.
- Cagan four risks: `gisf-life-cycle.pdf` slide 64.
- Features delivering this capability: `_obsidian/templates/adr.md`; `architect-architecture-design` skill (covers ADR-class content); CLAUDE.md graph definition (*"adrs (architectural decisions can hang off anywhere)"*).
- ADR convention (Nygard) flagged as out-of-bibliography in the template's `## Source`.
