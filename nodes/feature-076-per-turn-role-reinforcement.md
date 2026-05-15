---
category: feature
id: feature-076-per-turn-role-reinforcement
parent: "[[cap-02-role-scoped-agents]]"
artifacts:
  - "[[.claude/hooks/role-reinforce.sh]]"
  - "[[.claude/settings.json]]"
status: draft
created: 2026-05-15
updated: 2026-05-15
---

# Feature 076 — Per-turn role reinforcement (`UserPromptSubmit`)

> Authored via `po-feature-decomposition`. Relates to [[feature-074-agent-decision-verification]] (it re-grounds the same discipline every turn) and [[feature-075-hard-role-jurisdiction]] (reads the same marker). The one proportionate hard lever for the soft behavioral layer: you cannot hook a model's reasoning, but you can make the guardrail non-forgettable.

## What it delivers

A `UserPromptSubmit` hook (`.claude/hooks/role-reinforce.sh`) that, every turn, injects (does not block): if `.claude/.active-role` absent → "no role declared, run `/role`"; else a terse block — active role + its jurisdiction one-liner (from `.claude/role-scope.json`) + the decision-verification checklist. Re-grounds the discipline at the instant a "do it" arrives; combats context-drift forgetting (the originating failure).

## Story Map position

- **Activity:** behavioral discipline made non-forgettable. **Task:** this feature. **Release slice:** thickening.

## Stories (children)

- `[[story-076-A-active-role-injected-each-turn]]`
- `[[story-076-B-no-role-injects-run-role-prompt]]`

## Spec sibling

- `[[spec-076-per-turn-role-reinforcement]]`

## Notes

Containment principle: all persistence is hard-gated, so this soft layer's drift cannot persist — it is the prefacio's "validation not discovery". Keep injection ~4–6 lines (per-turn context cost). `.claude/settings.json` had no governing node (pre-existing gap); feature-072 + this feature close it.

## Source

- Skill: `po-feature-decomposition`. GISF UC3M `gisf-life-cycle.pdf` slide 54 + slide 56. Light `## Source` per template.
