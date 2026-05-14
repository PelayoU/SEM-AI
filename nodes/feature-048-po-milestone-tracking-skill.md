---
category: feature
id: feature-048-po-milestone-tracking-skill
parent: "[[cap-03-apply-po-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 048 — Skill: `po-milestone-tracking`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/po-milestone-tracking/SKILL.md`. Delivers part of [[cap-03-apply-po-discipline]].

## What it delivers

Lets the PO track progress against Jones's 13 canonical milestones — where each milestone is the *formal closure of a reviewed deliverable*, not a calendar date — and react strongly to surfaced problems rather than ignoring them (the failure mode that surfaces in every litigated project per Jones).

## Stories (children)

- [[story-048-A-reject-cosmetic-green-status]] — As a PO running milestone reviews, I want to refuse cosmetic "done" status when no review artifact exists, so the tracking surface stays honest.

## Spec sibling

- [[spec-048-po-milestone-tracking-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Absorbed PM scope per [[adr-006-super-po-fusion]].

## Source

- Anchoring authority: Capers Jones BP #32 (pp. 115–117); critical-topic Ch 1 p. 19.
- Substrate evidence: `.claude/skills/po-milestone-tracking/SKILL.md`.
