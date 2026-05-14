---
category: feature
id: feature-025-claude-md-subagent-rule
parent: "[[cap-10-subagent-consultation]]"
artifacts:
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 025 — CLAUDE.md subagent-dispatch rule

> Authored via `po-feature-decomposition`. Delivers part of [[cap-10-subagent-consultation]].

## What it delivers

`CLAUDE.md` Layer B carries the operating rule *"Subagent dispatch ≠ authority transfer"* — explicit framing that consulting another role is information transfer; the calling role retains scope authority. Full ownership transfer requires closing the conversation and opening a new one with a different agent on the same branch. The rule loads at every session start so the boundary is common knowledge.

## Story Map position

- **Activity (Epic):** Cross-role consultation substrate.
- **Task:** This feature (CLAUDE.md rule surface).
- **Release slice:** Walking skeleton.

## Stories (children)

- [[story-025-A-rule-loaded-at-session-start]] — As any agent considering dispatch, I want the consultation-vs-handoff rule loaded, so I don't accidentally cede scope when I meant to consult.

## Spec sibling

- [[spec-025-claude-md-subagent-rule]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (rule present in CLAUDE.md; observed in Phase 1 where PO retained authority despite Architect's authoring) → Construction (text in CLAUDE.md) → Consequences (scope contamination structurally prevented).

## Notes

Architectural anchor: [[adr-005-subagent-dispatch-not-authority-transfer]] (the decision). This feature is the *operationalisation* — the rule has to live where every agent reads. CLAUDE.md is that surface.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-005-subagent-dispatch-not-authority-transfer]].
- Substrate evidence: `CLAUDE.md` Layer B § *Subagent dispatch ≠ authority transfer*.
