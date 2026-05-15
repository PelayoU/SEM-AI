---
category: story
id: story-075-B-deny-without-active-role
parent: "[[feature-075-hard-role-jurisdiction]]"
artifacts:
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
status: draft
created: 2026-05-15
updated: 2026-05-15
---

# Story 075-B — Deny substrate writes when no active role

## Cohn statement (GISF slide 124)

As **the framework**,
I want **every in-scope substrate write denied when `.claude/.active-role` is absent or empty**,
so that **"no role declared" cannot be a silent path to writing the framework — the marker is mandatory, not advisory**.

## Conditions of Satisfaction (GISF slide 125)

- With no marker, a governed substrate Edit is still denied; reason says run `/role <name>`.
- Removing the marker mid-session re-enables the denial immediately.

## INVEST self-check (GISF slide 128)

- **I** ✅ · **N** ✅ · **V** ✅ (turns soft jurisdiction hard) · **E** ✅ · **S** ✅ · **T** ✅ observable denial.

## Source

- Skill: `po-feature-decomposition`. Cohn GISF slide 124; INVEST slide 128.
