---
category: feature
id: feature-071-devops-legacy-retirement-skill
parent: "[[cap-07-apply-devops-discipline]]"
artifacts:
  - "[[.claude/skills/devops-legacy-retirement/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 071 — Skill: `devops-legacy-retirement`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/devops-legacy-retirement/SKILL.md`. Delivers part of [[cap-07-apply-devops-discipline]].

## What it delivers

Lets DevOps plan / execute retirement or replacement of legacy applications per Jones BP #50's 8 best practices: mine business rules + algorithms, survey users, search alternatives, stabilize legacy during transition, evaluate SOA fit, look for certified reuse, consider automated language conversion, apply static analysis. Long-lifespan empirics (20–30+ years) acknowledged; "just turn it off" anti-pattern refused.

## Stories (children)

- [[story-071-A-mine-rules-before-replacement]] — As DevOps planning legacy retirement, I want business-rule mining from the legacy code as a precondition for the replacement, so tribal-knowledge rules don't get lost in transition.

## Spec sibling

- [[spec-071-devops-legacy-retirement-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]].

## Source

- Anchoring authority: Capers Jones BP #50 (pp. 166–167); BP #47 cross-link (10-tool inventory).
- Substrate evidence: `.claude/skills/devops-legacy-retirement/SKILL.md`.
