---
category: feature
id: feature-028-claude-md-adr-cross-cut-rule
parent: "[[cap-11-adr-capture]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 028 — CLAUDE.md rule: ADRs cross-cut the backbone

> Authored via `po-feature-decomposition`. Delivers part of [[cap-11-adr-capture]].

## What it delivers

`CLAUDE.md` graph-definition section explicitly states *"adrs (architectural decisions can hang off anywhere)"*. ADRs are not on the linear vision→spec backbone; they cross-cut and can attach to any backbone node via `parent:`. The rule loads at every session start, making the cross-cutting nature common knowledge — preventing the failure mode where ADRs get force-fitted under a specific capability when their scope spans multiple.

## Story Map position

- **Activity (Epic):** Architectural-decision substrate.
- **Task:** This feature (cross-cut rule in CLAUDE.md).
- **Release slice:** Walking skeleton.

## Stories (children)

- [[story-028-A-adr-cross-cut-rule-loaded]] — As an Architect choosing where to parent an ADR, I want the cross-cut rule loaded, so I attach to the highest applicable backbone node rather than forcing a hierarchical fit.

## Spec sibling

- [[spec-028-claude-md-adr-cross-cut-rule]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (10 ADRs in Phase 1 are parented to a mix of vision, goal, and capability nodes — none forced under a feature) → Construction (text in CLAUDE.md) → Consequences (ADRs hang at the right altitude).

## Notes

Architectural anchor: [[adr-002-backbone-hierarchy-parent-edges]] explicitly treats ADRs as a side-branch of the backbone, distinct from the linear chain.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-002-backbone-hierarchy-parent-edges]].
- Substrate evidence: `CLAUDE.md` § *The graph* — *"adrs (architectural decisions can hang off anywhere)"*.
