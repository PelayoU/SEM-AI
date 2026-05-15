---
category: story
id: story-073-C-decision-verification-principle
parent: "[[feature-073-claude-md-orientation-and-governance]]"
artifacts:
  - "[[CLAUDE.md]]"
status: draft
created: 2026-05-15
updated: 2026-05-15
---

# Story 073-C — Decision-verification operating principle

## Cohn statement (GISF slide 124)

As **any role**,
I want **a CLAUDE.md operating principle stating every human decision-prompt is verified (in-jurisdiction? governing node?) before execution, and a bare "do it" is not a bypass**,
so that **the originating failure — full context loaded, rule articulated, still obeyed "do it" — is named as forbidden, with the node-before-artifact half additionally hard-gated**.

## Conditions of Satisfaction (GISF slide 125)

- A new principle in `## Operating principles` stating the two-check verification.
- It explicitly says the node-before-artifact check is hard-enforced and non-overridable (names the hook).
- Relates to [[adr-010-human-directed-ai-maintained]] (human directs; AI maintains).

## INVEST self-check (GISF slide 128)

- **I** ✅ · **N** ✅ · **V** ✅ (names the exact failure mode) · **E** ✅ · **S** ✅ · **T** ✅ (principle present + content).

## Source

- Skill: `po-feature-decomposition`. Cohn GISF slide 124; INVEST slide 128.
