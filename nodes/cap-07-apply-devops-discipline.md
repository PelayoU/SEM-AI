---
category: capability
id: cap-07-apply-devops-discipline
parent: "[[goal-02-tfm-public-artifact]]"
status: draft
mvp: go
created: 2026-05-14
updated: 2026-05-14
---

# Capability 07 — Apply audited DevOps discipline (configuration control, deployment, releases, support, maintenance ops, legacy retirement)

> Authored via `po-capabilities`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54. MVP filter: slide 69. Cagan four risks: slide 64.

## Statement (slides 97–99 form)

In order to **run the operations dimension from "code merged" through "running in production" through "end of life" under rigorous, citable practice** (parent goal [[goal-02-tfm-public-artifact]] — public publication is a release-class event that exercises DevOps discipline — also serves [[goal-01-self-bootstrap-validation]] (5-role coverage) and [[goal-03-portability-proof]]),
as **anyone running a software engineering effort under SEM-IA in a DevOps capacity**,
I want **the ability to stand up configuration control (ISO 10007 / IEEE 828); design the deployment pipeline (Humble & Farley's 7-stage model + 5-axis strategy framework); plan releases avoiding the 16 named anti-patterns; staff and run customer support against the 1-per-10kFP / 1-per-150-customers ratios; manage post-release change with the 10-tool renovation inventory; run maintenance operations across the 23 work-type taxonomy with ITIL alignment; and plan legacy retirement against the 8-practice baseline**.

## Implementation-agnostic test

- **Implementation A** (current): 7 DevOps skills under `.claude/skills/devops-*/SKILL.md` applied via the DevOps agent.
- **Implementation B** (alternative): same discipline encoded as a runbook + ITIL service-management playbook + CI/CD platform configuration; applied by a human DevOps team without an AI agent.

A third plausible: discipline distributed across separate Configuration Manager + Release Manager + Support Manager + Maintenance Specialist roles per Jones Table 5-1 (which DevOps aggregates). The capability is *audited operations discipline being available*, not the role-aggregation choice.

## MVP Go / No-go

- **Value risk:** Without this capability, public publication (G2) lacks process; deployment, customer support, and post-release change run on improvisation. Maintenance is the dominant expense of the software industry (Jones BP #48 p. 163); operating it without discipline is malpractice at any non-trivial scale.
- **Usability risk:** Moderate-high — 7 skills cover a wide operational surface; for SEM-IA-modelling-itself the operational surface is small (one repo, no customers yet), so most of the discipline is latent.
- **Viability risk:** Proven — all 7 DevOps skills implemented; bibliography anchored on Jones BPs #34 / #43 / #45 / #47 / #48 / #49 / #50 + Ch 5 Table 5-1 + GISF `gisf-pipeline-devops.pdf` (Humble & Farley) + `gisf-delivery-control-and-monitoring.pdf` (Release Kanban + daily stand-up).
- **Business viability risk:** N/A.

**Decision: Go** — required for G2 (publication as a release event) and reinforces G1 (5-role coverage).

## Non-overlap with sibling capabilities

- Sibling (same parent): [[cap-08-citation-discipline]] — independent. Citation is *content rigor*; DevOps discipline is *operational rigor*.
- Sibling (same parent): [[cap-12-public-publication]] — adjacent. Public publication is the *outcome*; DevOps discipline is *the discipline applied to achieve it*.
- Siblings (different parents): [[cap-03-apply-po-discipline]], [[cap-04-apply-architect-discipline]], [[cap-05-apply-qa-discipline]], [[cap-06-apply-developer-discipline]] — same shape, different role.

## Non-coverage

- **Not about specific operational decisions.** The capability is *the discipline being applicable*; specific pipeline configs / release plans / support staffing for SEM-IA's own release are content authored by DevOps at feature time.
- **Not about ITIL as anchored authority.** Per Jones BP #48 p. 162 ITIL is referenced as relevant framework but the standard itself is not in audited `bibliography/sources/`; the capability respects this flagging.
- **Not about Three Ways / DORA metrics as authority.** Convention pointers only.

## Source

- Skill: `po-capabilities`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54, slide 69; `gisf-discovery.pdf` slides 97–99.
- Cagan four risks: `gisf-life-cycle.pdf` slide 64.
- DevOps agent definition: `.claude/agents/devops.md`.
- 7 DevOps skills under `.claude/skills/devops-*/SKILL.md` are the features delivering this capability.
- Anchoring sources via skills: Capers Jones BPs #34 / #43 / #45 / #47 / #48 / #49 / #50; Jones Ch 5 Table 5-1 (specialist split — DevOps aggregates Config Control + Maintenance ops portion + Customer Support); GISF UC3M `gisf-pipeline-devops.pdf` (Humble & Farley); `gisf-delivery-control-and-monitoring.pdf` (Release Kanban + daily stand-up).
