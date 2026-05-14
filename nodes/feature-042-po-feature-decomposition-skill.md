---
category: feature
id: feature-042-po-feature-decomposition-skill
parent: "[[cap-03-apply-po-discipline]]"
artifacts:
  - "[[.claude/skills/po-feature-decomposition/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 042 — Skill: `po-feature-decomposition`

> Authored via `po-feature-decomposition` itself. Wrapper around `.claude/skills/po-feature-decomposition/SKILL.md`. Delivers part of [[cap-03-apply-po-discipline]].

## What it delivers

Lets the PO decompose a capability into features + a feature into stories using INVEST (Independent / Negotiable / Valuable / Estimable / Small / Testable), Patton's User Story Mapping (Activity → Task → Sub-task), and the 5 Cs cycle (Card / Conversation / Confirmation / Construction / Consequences). The very skill currently being applied to author this layer of SEM-IA's graph.

## Stories (children)

- [[story-042-A-decompose-with-invest]] — As a PO under a capability, I want feature/story decomposition checked against INVEST letter-by-letter, so stories don't pretend to be features (or epics).
- [[story-042-B-story-map-narrative-flow]] — As a PO laying out a release, I want a story map with the user's narrative flow as backbone, so release slices are horizontal across activities.

## Spec sibling

- [[spec-042-po-feature-decomposition-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Self-application (Skill being used to author Skill's own wrapper) is the meta-recursive validation point.

## Source

- Anchoring authority: Cohn story format (GISF `gisf-delivery-backlog-management.pdf` slide 124); INVEST (slide 128, Wake 2003); 5 Cs (GISF `gisf-life-cycle.pdf` slide 56); Patton USM (`user-story-mapping.pdf` pp. 1–2; restated GISF slide 132).
- Substrate evidence: `.claude/skills/po-feature-decomposition/SKILL.md`.
