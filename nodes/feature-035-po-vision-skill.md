---
category: feature
id: feature-035-po-vision-skill
parent: "[[cap-03-apply-po-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 035 — Skill: `po-vision`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/po-vision/SKILL.md`. Delivers part of [[cap-03-apply-po-discipline]].

## What it delivers

Lets the PO draft / refine / audit a product vision against Cagan's Ten Principles of Product Vision (verbatim per slide 89) + GISF five-step construction method + 2-to-10-year horizon + positioning-statement template.

## Stories (children)

- [[story-035-A-author-vision-against-cagan-ten]] — As a PO, I want the vision skill to walk me through Cagan's 10 principles + the 5-step method, so my vision is defensible against external audit.

## Spec sibling

- [[spec-035-po-vision-skill]]

## Notes

Full formal criteria, workflow, and pitfalls live in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. This wrapper is the backbone-graph node, not the criteria source.

## Source

- Anchoring authority: Cagan *Inspired* (Ten Principles) via GISF `gisf-discovery.pdf` slide 89; horizon + 5-step method on slides 82, 86, 84.
- Substrate evidence: `.claude/skills/po-vision/SKILL.md`.
