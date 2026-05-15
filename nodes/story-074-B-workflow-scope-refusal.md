---
category: story
id: story-074-B-workflow-scope-refusal
parent: "[[feature-074-agent-decision-verification]]"
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

# Story 074-B — Workflow scope-refusal + consultation/work split

## Cohn statement (GISF slide 124)

As **an agent asked to act outside its jurisdiction**,
I want **an explicit refusal that distinguishes subagent *consultation* (feedback only, never authoring) from *cross-role work* (human `/role` switch)**,
so that **role-bleed is behaviourally refused and ADR-005 (dispatch ≠ authority transfer) is operationalised in the Workflow**.

## Conditions of Satisfaction (GISF slide 125)

- The step refuses out-of-jurisdiction action even on an explicit "do it" (cite Jones Ch 5 p.282 — protected from coercion).
- It routes: feedback → subagent consultation; work → `/role` / conversation handoff.
- It states a consulted subagent cannot author out-of-role substrate (gate blocks; marker = human's role).

## INVEST self-check (GISF slide 128)

- **I** ✅ · **N** ✅ · **V** ✅ (delivers the consultation-matrix candidate) · **E** ✅ · **S** ✅ · **T** ✅.

## Source

- Skill: `po-feature-decomposition`. Cohn GISF slide 124; INVEST slide 128. Lineage: [[adr-005-subagent-dispatch-not-authority-transfer]].
