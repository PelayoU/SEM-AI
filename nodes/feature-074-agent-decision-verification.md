---
category: feature
id: feature-074-agent-decision-verification
parent: "[[cap-02-role-scoped-agents]]"
artifacts:
  - "[[.claude/agents/product-owner.md]]"
  - "[[.claude/agents/architect.md]]"
  - "[[.claude/agents/qa.md]]"
  - "[[.claude/agents/developer.md]]"
  - "[[.claude/agents/devops.md]]"
status: draft
created: 2026-05-15
updated: 2026-05-15
---

# Feature 074 — Per-agent decision-verification + scope-refusal step

> Authored via `po-feature-decomposition`. **Relates to, does not redefine:** [[feature-007-five-role-agent-identities]], [[feature-024-agent-description-dispatch-triggers]], [[adr-005-subagent-dispatch-not-authority-transfer]]. Delivers the `2026-05-14` session's deferred *consultation matrix* improvement candidate. The 5 agents are already governed by feature-007/024/adr-005; this adds a Workflow step, it does not touch identity.

## What it delivers

Each of the 5 `.claude/agents/*.md` gains a `## Workflow` step: on any human request to create/change something — (a) confirm within this role's jurisdiction; if not, distinguish *consultation* (subagent, information/feedback only — "a meeting") from *cross-role work* (human `/role` switch — the only thing that moves authorship), per ADR-005; (b) if it touches substrate, confirm a governing node + active role in scope, else author the node / `/role` first. A consulted subagent is non-authoring by construction (the active-role marker reflects the human's declared role). A bare "do it" is verified, not blindly executed.

## Story Map position

- **Activity:** behavioral role discipline at the agent boundary.
- **Task:** this feature. **Release slice:** thickening the hard-enforcement layer.

## Stories (children)

- `[[story-074-A-workflow-decision-verification]]`
- `[[story-074-B-workflow-scope-refusal]]`

## Spec sibling

- `[[spec-074-agent-decision-verification]]`

## Notes

This is the soft behavioral layer; its blast radius is contained because all *persistence* is hard-gated by [[feature-072-node-before-artifact-gate]] + [[feature-075-hard-role-jurisdiction]]. Reinforced every turn by [[feature-076-per-turn-role-reinforcement]].

## Source

- Skill: `po-feature-decomposition`. GISF UC3M `gisf-life-cycle.pdf` slide 54 + slide 56. Light `## Source` per template.
