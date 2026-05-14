---
category: feature
id: feature-068-devops-customer-support-skill
parent: "[[cap-07-apply-devops-discipline]]"
artifacts:
  - "[[.claude/skills/devops-customer-support/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 068 — Skill: `devops-customer-support`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/devops-customer-support/SKILL.md`. Delivers part of [[cap-07-apply-devops-discipline]].

## What it delivers

Lets DevOps size and run the customer-support function per Jones BP #45's empirics: 1 support per 10 k FP or 1 per 150 customers (drifting to 1 per 1,000 at scale); 220-defect-reduction ≈ 1 fewer support FTE per year. Quality investment upstream is the only sustainable scale lever.

## Stories (children)

- [[story-068-A-quality-as-support-lever]] — As DevOps sizing support, I want the 220-defect multiplier explicit when negotiating with PO/QA, so the trade-off between upstream quality investment and downstream support cost is visible.

## Spec sibling

- [[spec-068-devops-customer-support-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. L0/L1/L2/L3 tiering: L1 ≥60 % first-call resolution per BP #49 practice 4.

## Source

- Anchoring authority: Capers Jones BP #45 (pp. 157–158); BP #49 cross-link.
- Substrate evidence: `.claude/skills/devops-customer-support/SKILL.md`.
