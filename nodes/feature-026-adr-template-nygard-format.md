---
category: feature
id: feature-026-adr-template-nygard-format
parent: "[[cap-11-adr-capture]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 026 — ADR template (Nygard format)

> Authored via `po-feature-decomposition`. Delivers part of [[cap-11-adr-capture]].

## What it delivers

`_obsidian/templates/adr.md` encodes the Nygard-format ADR structure: frontmatter (id, parent, status, supersedes/superseded-by), body sections (Status, Context, Decision, Consequences positive/negative/neutral, Alternatives considered, Seven fundamental topics touchpoints per Jones Ch 7, Source). Used by Architect to author each cross-cutting architectural decision. Status transitions: proposed → accepted; superseded chain tracked via frontmatter.

## Story Map position

- **Activity (Epic):** Architectural-decision substrate.
- **Task:** This feature (ADR template).
- **Release slice:** Walking skeleton — Phase 1 of this session depended on it.

## Stories (children)

- [[story-026-A-adr-template-enforces-structure]] — As an Architect authoring a decision, I want the template to enforce Context / Decision / Consequences / Alternatives / Seven-topics-touchpoints, so the audit grid is structural.

## Spec sibling

- [[spec-026-adr-template-nygard-format]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (10 ADRs authored in Phase 1 demonstrate the template works) → Construction → Consequences (architectural rationale survives the moment of decision).

## Notes

Architectural anchors: [[adr-011-architect-as-adr-author]] (if added in future; currently implicit) and the seven fundamental topics audit grid from Jones Ch 7 p. 470. Nygard's *Documenting Architecture Decisions* is **out-of-bibliography** (not in `bibliography/sources/`); flagged in the template's own `## Source` per [[adr-003-citation-mandate]].

## Source

- Skill: `po-feature-decomposition`.
- Jones Ch 7 § *Software Architecture* (seven fundamental topics) — anchored authority.
- Nygard, *Documenting Architecture Decisions* — out-of-bibliography convention, flagged.
- Substrate evidence: `_obsidian/templates/adr.md`.
