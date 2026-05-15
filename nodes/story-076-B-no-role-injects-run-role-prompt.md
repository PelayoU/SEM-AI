---
category: story
id: story-076-B-no-role-injects-run-role-prompt
parent: "[[feature-076-per-turn-role-reinforcement]]"
artifacts:
  - "[[.claude/hooks/role-reinforce.sh]]"
status: draft
created: 2026-05-15
updated: 2026-05-15
---

# Story 076-B — No role declared → inject the run-`/role` prompt

## Cohn statement (GISF slide 124)

As **a session with no declared role**,
I want **the per-turn injection to say "no active role — run `/role <name>`; substrate writes are hard-blocked until then"**,
so that **the missing-marker state is surfaced every turn, not discovered only at the first blocked write**.

## Conditions of Satisfaction (GISF slide 125)

- With `.claude/.active-role` absent/empty, the injection is the run-`/role` message.
- It never blocks the prompt (reinforcement, not a gate).

## INVEST self-check (GISF slide 128)

- **I** ✅ · **N** ✅ · **V** ✅ (closes the silent no-role gap proactively) · **E** ✅ · **S** ✅ · **T** ✅ observable injected text.

## Source

- Skill: `po-feature-decomposition`. Cohn GISF slide 124; INVEST slide 128.
