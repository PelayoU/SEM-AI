---
category: feature
id: feature-037-po-capabilities-skill
parent: "[[cap-03-apply-po-discipline]]"
artifacts:
  - "[[.claude/skills/po-capabilities/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 037 — Skill: `po-capabilities`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/po-capabilities/SKILL.md`. Delivers part of [[cap-03-apply-po-discipline]].

## What it delivers

Lets the PO derive / refine / audit capabilities under a goal, keeping them implementation-agnostic (two-implementations test), MVP-filterable via Cagan four risks, non-overlapping with siblings, decomposable into features. The very skill exercised to author SEM-IA's own 13 capabilities.

## Stories (children)

- [[story-037-A-derive-implementation-agnostic-capabilities]] — As a PO under a goal, I want capabilities stated as user-abilities-regardless-of-implementation, so design space is not locked prematurely.

## Spec sibling

- [[spec-037-po-capabilities-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]].

## Source

- Anchoring authority: GISF `gisf-life-cycle.pdf` slide 54 (canonical definition); slide 69 (MVP filter); `gisf-discovery.pdf` slides 97–99 (capability listing form); slide 64 (Cagan four risks).
- Substrate evidence: `.claude/skills/po-capabilities/SKILL.md`.
