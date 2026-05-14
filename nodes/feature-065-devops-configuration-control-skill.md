---
category: feature
id: feature-065-devops-configuration-control-skill
parent: "[[cap-07-apply-devops-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 065 — Skill: `devops-configuration-control`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/devops-configuration-control/SKILL.md`. Delivers part of [[cap-07-apply-devops-discipline]].

## What it delivers

Lets DevOps stand up software configuration control per Jones BP #34 + ISO 10007-2003 + IEEE 828-1998 + CMMI key-practice-area: every deliverable under control (requirements / specs / code / tests / user docs), unique IDs, cross-deliverable mapping, master-copy locking, formal change pipeline. Mechanical activity supported by automation; coordinates with `po-change-control` (BP #33).

## Stories (children)

- [[story-065-A-all-deliverables-under-cm]] — As DevOps setting up CM, I want every deliverable class under control (not just code), so cross-deliverable consistency survives changes.

## Spec sibling

- [[spec-065-devops-configuration-control-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. CM tracks; CCB (BP #33 via `po-change-control`) judges.

## Source

- Anchoring authority: Capers Jones BP #34 (p. 119); ISO 10007-2003 + IEEE 828-1998 (cited via Jones, full standards out-of-bibliography).
- Substrate evidence: `.claude/skills/devops-configuration-control/SKILL.md`.
