---
category: feature
id: feature-069-devops-post-release-change-skill
parent: "[[cap-07-apply-devops-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 069 — Skill: `devops-post-release-change`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/devops-post-release-change/SKILL.md`. Delivers part of [[cap-07-apply-devops-discipline]].

## What it delivers

Lets DevOps manage software change after release using Jones BP #47's 10-tool inventory for renovation: complexity analysis, static analysis, error-prone-module ID, dead-code ID, data mining, code conversion, FP enumeration, renovation workbenches, automated test generation, test coverage analysis. Same rigor as pre-release; "less rigorous post-release" is the observed default, not acceptable.

## Stories (children)

- [[story-069-A-post-release-same-rigor]] — As DevOps managing post-release change, I want the same rigor as pre-release (specs current, comments updated, complexity tracked), so the legacy doesn't drift into the failure mode Jones observes.

## Spec sibling

- [[spec-069-devops-post-release-change-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]].

## Source

- Anchoring authority: Capers Jones BP #47 (pp. 160–161); BP #48 cross-link; BP #28 practice 12.
- Substrate evidence: `.claude/skills/devops-post-release-change/SKILL.md`.
