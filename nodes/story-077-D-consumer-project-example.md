---
category: story
id: story-077-D-consumer-project-example
parent: "[[feature-077-portable-gate-scope]]"
artifacts:
  - "[[.claude/role-scope.json]]"
  - "[[.claude/role-scope.example.json]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Story 077-D — Documented consumer-project example

## Cohn statement (GISF slide 124)

As **a consumer-project author (e.g. a mobile app team)**,
I want **a documented example `role-scope.json` for a non-SEM-IA project**,
so that **adoption is copy → edit → rename, not archaeology — and it is explicit that the imported `.claude/**` is intentionally ungated (the tool, not the product)**.

## Conditions of Satisfaction (GISF slide 125)

- `.claude/role-scope.json` `_comment` reframed as the per-project gate config (union=scope, per-role=jurisdiction, always-ignore guard independent, consumer rewrites arrays).
- `.claude/role-scope.example.json` shipped (mobile-app roles → `src/**`, `ios/**`, `android/**`, …); `_comment` explains copy-to-`role-scope.json` and that `.claude/**` is intentionally absent.
- `.claude/role-scope.example.json` added to the architect entry of `role-scope.json` (so creating it passes role-scope) and to the CLAUDE.md § Role jurisdiction Architect row (mirror invariant).

## INVEST self-check (GISF slide 128)

- **I** ⚠️ shares the mirror-consistency requirement with story-077-C (accepted) · **N** ✅ · **V** ✅ (makes portability adoptable) · **E** ✅ · **S** ✅ · **T** ✅.

## Source

- Skill: `po-feature-decomposition`. Cohn GISF slide 124; INVEST slide 128. Lineage `[[adr-013-gate-scope-is-project-configurable]]`, `[[adr-004-substrate-content-separation]]`.
