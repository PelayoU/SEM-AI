---
category: feature
id: feature-066-devops-deployment-skill
parent: "[[cap-07-apply-devops-discipline]]"
artifacts:
  - "[[.claude/skills/devops-deployment/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 066 — Skill: `devops-deployment`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/devops-deployment/SKILL.md`. Delivers part of [[cap-07-apply-devops-discipline]].

## What it delivers

Lets DevOps design / execute the deployment pipeline combining Jones BP #43 (10 practices, ERP-class baseline $1M+ / 12 months / 25 consultants + 30 in-house) with Humble & Farley's Deployment Pipeline (7 generic stages: Develop → Confirm → Build → Test → Provide → Deploy → Release) per GISF `gisf-pipeline-devops.pdf`. Branching / build / test / release / deployment strategies decided explicitly.

## Stories (children)

- [[story-066-A-seven-stage-pipeline]] — As DevOps designing CI/CD, I want every change to traverse the 7 stages explicitly (no skipped gates), so deployment defects are caught at the right phase.

## Spec sibling

- [[spec-066-devops-deployment-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Humble & Farley book is out-of-bibliography (captured via GISF slides).

## Source

- Anchoring authority: Capers Jones BP #43 (pp. 154–155); GISF UC3M `gisf-pipeline-devops.pdf` slides 30 (Humble & Farley model), 32, 34, 35–38.
- Substrate evidence: `.claude/skills/devops-deployment/SKILL.md`.
