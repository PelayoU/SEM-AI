---
category: feature
id: feature-027-architect-skill-adr-coverage
parent: "[[cap-11-adr-capture]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 027 — `architect-architecture-design` skill covers ADR content

> Authored via `po-feature-decomposition`. Delivers part of [[cap-11-adr-capture]].

## What it delivers

The `architect-architecture-design` skill carries the formal criteria for ADR content: the seven fundamental topics (Jones Ch 7 p. 470), the size-tier importance (Table 7-7), the architectural-style catalog (monolithic / SOA / event-driven / 3-tier / cloud / etc.), and the design-notation alternatives. Architect agents authoring an ADR apply this skill to ensure the decision is anchored, the alternatives are documented, and the seven-topics audit grid is filled. Demonstrated in Phase 1's 10 ADRs.

## Story Map position

- **Activity (Epic):** Architectural-decision substrate.
- **Task:** This feature (skill provides ADR content criteria).
- **Release slice:** Walking skeleton.

## Stories (children)

- [[story-027-A-architect-skill-as-adr-criteria]] — As an Architect authoring an ADR, I want my own skill to provide the formal criteria (7 topics, alternatives, size-tier), so the ADR is content-defensible.

## Spec sibling

- [[spec-027-architect-skill-adr-coverage]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (10 ADRs in Phase 1 each carry the Seven fundamental topics section per the skill) → Construction → Consequences (ADR content rigour anchored in Jones Ch 7).

## Notes

Companion to [[feature-026-adr-template-nygard-format]] (template is structure; this is content criteria). Architect-skill is loaded by the Architect agent; ADR template is loaded as scaffolding by both PO (for skeletons) and Architect (for content authoring).

## Source

- Skill: `po-feature-decomposition`.
- Anchoring authority: Capers Jones (2010) Ch 7 § *Software Architecture* pp. 470–475; BP #14 pp. 75–77; Ch 9 Table 9-23.
- Substrate evidence: `.claude/skills/architect-architecture-design/SKILL.md`.
