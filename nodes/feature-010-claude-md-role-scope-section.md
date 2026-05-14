---
category: feature
id: feature-010-claude-md-role-scope-section
parent: "[[cap-02-role-scoped-agents]]"
artifacts:
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 010 — CLAUDE.md `## Roles` section + invocation modes

> Authored via `po-feature-decomposition`. Delivers part of [[cap-02-role-scoped-agents]].

## What it delivers

`CLAUDE.md` (universal contract, loaded into every session) carries a `## Roles` table listing the 5 implemented + 2 planned roles, their custody scope, skill counts, agent file paths, and tier; plus the *Invocation modes* subsection distinguishing Role-as-agent (`claude --agent <role>`) from Subagent dispatch (`Task` tool with `subagent_type`). Every agent and every conversation start inherits this canonical framing.

## Story Map position

- **Activity (Epic):** Role substrate framing.
- **Task:** This feature (CLAUDE.md role section).
- **Release slice:** Walking skeleton — without this, role boundaries are tribal knowledge rather than contractual.

## Stories (children)

- [[story-010-A-roles-table-loaded]] — As any agent or human in a session, I want the roles table loaded at session start, so role boundaries are common knowledge from turn zero.
- [[story-010-B-invocation-mode-clarity]] — As a human deciding how to engage SEM-IA, I want the two invocation modes (full role vs subagent consultation) explicitly documented, so I don't conflate them.

## Spec sibling

- [[spec-010-claude-md-role-scope-section]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (the section is loaded automatically; verifiable in any session start) → Construction (lives in `CLAUDE.md`) → Consequences (role-scope contamination is structurally prevented).

## Notes

Architectural anchors: [[adr-005-subagent-dispatch-not-authority-transfer]], [[adr-006-super-po-fusion]]. Companion to [[feature-009-role-catalog-design-doc]] (catalog is the design; this is the contract surface visible to every session).

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-005-subagent-dispatch-not-authority-transfer]], [[adr-006-super-po-fusion]].
- Substrate evidence: `CLAUDE.md` § *Roles*.
