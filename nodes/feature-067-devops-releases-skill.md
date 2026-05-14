---
category: feature
id: feature-067-devops-releases-skill
parent: "[[cap-07-apply-devops-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 067 — Skill: `devops-releases`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/devops-releases/SKILL.md`. Delivers part of [[cap-07-apply-devops-discipline]].

## What it delivers

Lets DevOps plan / execute releases (bug-fix / feature / new version) avoiding Jones BP #49's 16 named anti-patterns (long phone wait, no e-mail support, fee for bug reports, forced upgrades, arbitrary file format changes, dropped features, etc.) and applying the 11 theoretical-but-correct practices (e-mail bug reporting ≤48 h SLA, phone ≤5 min, self-installing repairs, free format conversion, etc.).

## Stories (children)

- [[story-067-A-no-named-anti-patterns]] — As DevOps planning a release, I want every release-plan candidate audited against the 16 anti-patterns, so common dissatisfaction sources are excluded by construction.

## Spec sibling

- [[spec-067-devops-releases-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Pairs with [[feature-068-devops-customer-support-skill]] (release volume drives support volume).

## Source

- Anchoring authority: Capers Jones BP #49 (pp. 164–165); BP #45 (cross-link); GISF release strategies slide 34.
- Substrate evidence: `.claude/skills/devops-releases/SKILL.md`.
