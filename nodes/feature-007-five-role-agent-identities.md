---
category: feature
id: feature-007-five-role-agent-identities
parent: "[[cap-02-role-scoped-agents]]"
artifacts:
  - "[[.claude/agents/product-owner.md]]"
  - "[[.claude/agents/architect.md]]"
  - "[[.claude/agents/qa.md]]"
  - "[[.claude/agents/developer.md]]"
  - "[[.claude/agents/devops.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 007 — Five implemented role-agent identities (PO, Architect, QA, Developer, DevOps)

> Authored via `po-feature-decomposition`. Delivers part of [[cap-02-role-scoped-agents]].

## What it delivers

Five `.claude/agents/<role>.md` identity files — `product-owner.md`, `architect.md`, `qa.md`, `developer.md`, `devops.md` — each defining the role's scope, skill catalog, workflow, cross-role interaction table, and gotchas. Loaded by the harness via `--agent <role>` flag or `Task` subagent dispatch. Tier-3 roles (Security, Designer) are documented in `sem-role-catalog.md` but not yet implemented.

## Story Map position

- **Activity (Epic):** Role substrate.
- **Task:** This feature (5 implemented agents).
- **Release slice:** Walking skeleton — the 5-role coverage is the visible AI-as-infrastructure paradigm.

## Stories (children)

- [[story-007-A-invoke-role-agent]] — As a human, I want to invoke any of the 5 role-agents with `--agent <role>`, so I engage role-scoped expertise.
- [[story-007-B-subagent-dispatch-by-description]] — As a calling agent, I want to dispatch a sibling agent via `Task` and have its description trigger the correct match, so cross-role consultation routes automatically.

## Spec sibling

- [[spec-007-five-role-agent-identities]]

## 5 Cs cycle reminder

Card → Conversation (role-by-role custody articulated across multiple sessions) → Confirmation (spec encodes "each agent loads CLAUDE.md + its own identity file") → Construction (5 agent files exist) → Consequences (role-scoped reasoning operational).

## Notes

Architectural anchors: [[adr-006-super-po-fusion]] (PO is super-PO at Tier-1); [[adr-005-subagent-dispatch-not-authority-transfer]] (Task dispatch preserves scope authority). Security + Designer agents planned per [[cap-02-role-scoped-agents]] and `sem-role-catalog.md`; out of current MVP.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-006-super-po-fusion]], [[adr-005-subagent-dispatch-not-authority-transfer]].
- Substrate evidence: 5 files under `.claude/agents/`.
- Bibliography anchors via individual agent definitions: Cagan, Capers Jones BPs, GISF UC3M.
