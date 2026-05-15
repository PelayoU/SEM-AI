---
category: story
id: story-074-A-workflow-decision-verification
parent: "[[feature-074-agent-decision-verification]]"
artifacts:
  - "[[.claude/agents/product-owner.md]]"
  - "[[.claude/agents/architect.md]]"
  - "[[.claude/agents/qa.md]]"
  - "[[.claude/agents/developer.md]]"
  - "[[.claude/agents/devops.md]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Story 074-A — Workflow decision-verification step

## Cohn statement (GISF slide 124)

As **an agent in any role**,
I want **a Workflow step that verifies a human decision-prompt against jurisdiction + node-before-artifact before acting**,
so that **"do it" is not blindly executed — the originating failure becomes a checked path**.

## Conditions of Satisfaction (GISF slide 125)

- All 5 agent files contain the step in `## Workflow`, identical in substance.
- The step references CLAUDE.md § Role jurisdiction + the node-before-artifact hard rule.
- It states the bare-"do it" is verified, not executed.

## INVEST self-check (GISF slide 128)

- **I** ✅ · **N** ✅ · **V** ✅ · **E** ✅ · **S** ✅ (one inserted step ×5) · **T** ✅ (step present in each file).

## Source

- Skill: `po-feature-decomposition`. Cohn GISF slide 124; INVEST slide 128.
