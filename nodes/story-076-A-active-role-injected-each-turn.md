---
category: story
id: story-076-A-active-role-injected-each-turn
parent: "[[feature-076-per-turn-role-reinforcement]]"
artifacts:
  - "[[.claude/hooks/role-reinforce.sh]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Story 076-A — Active role + checklist injected each turn

## Cohn statement (GISF slide 124)

As **any role-agent**,
I want **the active role, its jurisdiction, and the decision-verification checklist re-injected into context on every user prompt**,
so that **the discipline cannot be lost to context drift and is present exactly when a "do it" arrives**.

## Conditions of Satisfaction (GISF slide 125)

- On any prompt with `.active-role` set, injected context names the role + its allowed/forbidden paths + the checklist.
- Injection is terse (~4–6 lines) and never blocks the prompt.

## INVEST self-check (GISF slide 128)

- **I** ✅ · **N** ✅ (wording) · **V** ✅ (attacks the originating forgetting) · **E** ✅ · **S** ✅ · **T** ✅ (injected text observable).

## Source

- Skill: `po-feature-decomposition`. Cohn GISF slide 124; INVEST slide 128.
