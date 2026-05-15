---
category: story
id: story-072-A-deny-ungoverned-substrate-write
parent: "[[feature-072-node-before-artifact-gate]]"
artifacts:
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Story 072-A — Deny ungoverned substrate Write/Edit

> Acceptance criteria trace to the spec sibling as `AC-A1`, `AC-A2`, …

## Cohn statement (GISF `gisf-delivery-backlog-management.pdf` slide 124)

As **the framework**,
I want **any `Write`/`Edit` targeting an in-scope substrate path that no node references in `artifacts:` to be denied at the `PreToolUse` boundary**,
so that **node-before-artifact is a structural invariant, not a virtue the agent may forget on a bare "do it"**.

## Conditions of Satisfaction (back of card, GISF slide 125)

- A Write to a substrate path with zero governing nodes is denied with an instructive reason.
- The denial cannot be bypassed by permission mode or `--dangerously-skip-permissions`.
- A node referencing the path (any `status:`) makes the same Write pass.

## INVEST self-check (GISF slide 128)

- **I** ✅ independent of the role-scope and reinforcement stories.
- **N** ✅ message wording negotiable.
- **V** ✅ closes the exact failure observed in this conversation.
- **E** ✅ small hook branch.
- **S** ✅ one scenario family.
- **T** ✅ observable: the tool call is blocked.

## Source

- Skill: `po-feature-decomposition`. Cohn format GISF `gisf-delivery-backlog-management.pdf` slide 124; INVEST slide 128.
