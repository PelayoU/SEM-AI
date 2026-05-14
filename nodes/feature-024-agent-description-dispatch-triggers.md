---
category: feature
id: feature-024-agent-description-dispatch-triggers
parent: "[[cap-10-subagent-consultation]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 024 — Agent `description` field drives dispatch trigger matching

> Authored via `po-feature-decomposition`. Delivers part of [[cap-10-subagent-consultation]].

## What it delivers

Each `.claude/agents/<role>.md` carries a `description:` frontmatter field with concrete trigger phrases (*"drafting or auditing the architecture of a new application"*, *"deciding cyclomatic complexity thresholds"*, etc.). When a calling agent describes the work to dispatch via `Task`, the description field is the matching surface — clear descriptions route work to the correct role; vague descriptions trigger mis-dispatch.

## Story Map position

- **Activity (Epic):** Cross-role consultation substrate.
- **Task:** This feature (descriptions as dispatch surface).
- **Release slice:** Walking skeleton.

## Stories (children)

- [[story-024-A-precise-descriptions-route-correctly]] — As a calling agent describing work, I want descriptions to be precise trigger phrases rather than vague summaries, so dispatch routes to the right specialist on the first try.

## Spec sibling

- [[spec-024-agent-description-dispatch-triggers]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (5 agent files have concrete trigger descriptions) → Construction → Consequences (low mis-dispatch rate).

## Notes

Architectural anchor: [[adr-005-subagent-dispatch-not-authority-transfer]]. Companion to [[feature-023-task-tool-integration]]. The description field is the only dispatch trigger surface — keeping it precise is a maintenance responsibility per [[cap-02-role-scoped-agents]].

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-005-subagent-dispatch-not-authority-transfer]].
- Substrate evidence: each `.claude/agents/<role>.md` frontmatter `description:` field; meta-template enforces it.
