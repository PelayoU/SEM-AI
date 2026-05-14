---
category: feature
id: feature-070-devops-maintenance-operations-skill
parent: "[[cap-07-apply-devops-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 070 — Skill: `devops-maintenance-operations`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/devops-maintenance-operations/SKILL.md`. Delivers part of [[cap-07-apply-devops-discipline]].

## What it delivers

Lets DevOps run the operational side of maintenance — ITIL-aligned change response, Release Kanban (PBIs To Do / In Progress / Delivered), Daily stand-up, Release Burn-Up Charts, response-time SLAs (defect-repair AND change-request-completion), maintenance-staff sizing. Coordinates with Developer's code-side maintenance per Jones Table 5-1 specialty aggregation.

## Stories (children)

- [[story-070-A-flow-visualised-not-tribal]] — As DevOps running maintenance ops, I want Release Kanban + Burn-Up Chart maintained, so progress is visible rather than tribal knowledge.

## Spec sibling

- [[spec-070-devops-maintenance-operations-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. ITIL is convention pointer; full standard out-of-bibliography.

## Source

- Anchoring authority: Capers Jones BP #48 (pp. 161–164); Ch 5 Table 5-1; GISF UC3M `gisf-delivery-control-and-monitoring.pdf` (Release Kanban + Burn-Up + Daily stand-up).
- Substrate evidence: `.claude/skills/devops-maintenance-operations/SKILL.md`.
