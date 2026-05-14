---
category: feature
id: feature-040-po-requirements-discovery-skill
parent: "[[cap-03-apply-po-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 040 — Skill: `po-requirements-discovery`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/po-requirements-discovery/SKILL.md`. Delivers part of [[cap-03-apply-po-discipline]].

## What it delivers

Lets the PO elicit / analyse / validate requirements using Jones BP #11's 14-practice inventory (JAD, QFD, prototypes, legacy mining, requirements inspections, traceability, etc.) with explicit handling of the empirical 1–3 %/month churn rate and the 80 % legacy-replacement case. Absorbs BA function per super-PO fusion.

## Stories (children)

- [[story-040-A-baseline-JAD-not-interviews]] — As a PO above 1k FP, I want JAD as the baseline elicitation, so requirements aren't dependent on the loudest stakeholder.

## Spec sibling

- [[spec-040-po-requirements-discovery-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Absorbed BA scope per [[adr-006-super-po-fusion]].

## Source

- Anchoring authority: Capers Jones BP #11 (pp. 70–72); requirements as success/failure determinant (p. 73).
- Substrate evidence: `.claude/skills/po-requirements-discovery/SKILL.md`.
