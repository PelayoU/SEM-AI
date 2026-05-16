---
name: devops-deployment
description: "Design the deployment pipeline and execute installation of a software application — combining Capers Jones's deployment best practices (ERP-class effort sizing $1M+ / 12 months / 25 consultants + 30 in-house) with Humble & Farley's Deployment Pipeline model (7 generic stages: Develop → Confirm → Build → Test → Provide → Deploy → Release), branching strategies (Trunk-Based / Feature Branch / Gitflow), and production deployment strategies (Re-create / Blue/Green / Rolling / Canary / A/B / Continuous Deployment / Feature Management). Use whenever designing or auditing a CI/CD pipeline, picking a deployment strategy for a new application, sizing the deployment effort for ERP-class work, planning installation of a major system, or evaluating an existing pipeline against the empirical model. Triggers include phrases like 'deployment pipeline', 'CI/CD', 'continuous delivery', 'continuous integration', 'Blue/Green', 'Canary', 'Rolling deployment', 'A/B test', 'feature flag', 'release strategy', 'install plan', 'ERP deployment', 'pipeline stages'."
---

# devops-deployment

## Purpose

Capers Jones flags deployment as a gray area seldom covered by the software literature, yet observes that ERP-class deployment can take more than 12 calendar months, cost more than $1 million, and involve more than 25 consultants and 30 in-house personnel. Humble & Farley's *Continuous Delivery* provides the modern model: a 7-stage Deployment Pipeline that gates every change from develop to customer with explicit branching, build, test, release, and production-deployment strategies. This skill lets DevOps combine Jones's empirical deployment-effort baseline with Humble & Farley's pipeline model to design or audit the project's pipeline against current best practice.

## When this skill applies

- A new project needs a CI/CD pipeline designed from scratch.
- An existing pipeline is being audited against the 7-stage model.
- A deployment strategy decision is open (Blue/Green vs Rolling vs Canary vs Re-create).
- A branching strategy decision is open (Trunk-Based vs Feature Branch vs Gitflow).
- An ERP-class or large mainframe deployment is being scoped (effort, cost, schedule).
- Continuous Deployment adoption is being evaluated.

## Formal criteria

A deployment pipeline pass is acceptable only if all of the following hold:

1. **7-stage Deployment Pipeline model present** (Humble & Farley) — every change traverses: **Develop → Confirm → Build → Test → Provide → Deploy → Release / Deliver to Customer**. A pipeline missing a stage either skips a gate or merges stages without acknowledging the loss.
2. **Generic-process stages instrumented** — the detailed process: validate start criteria → build → unit tests → code analysis → package artifact → publish artifact → provide test environment → deploy artifact to tests → run tests → validate compliance → validate completion criteria → dual control → provide production environment → deploy artifact to production → notify actors. Each stage either runs or is explicitly skipped with rationale.
3. **Branching strategy declared** — Trunk-Based / Feature Branch / Gitflow. Trunk-Based is preferred for high-frequency deployment; Gitflow for release-train cadence.
4. **Build strategy declared** — Vertical Scaling / Full vs Incremental / Parallel / Pipeline Caching / Build Targets / Cross-Platform / Multiteam. The choice depends on project size and team count.
5. **Test strategy declared** — Automated vs Manual / Functional vs Nonfunctional / Parallel vs Sequential / Long vs Short execution. The choice is constrained by the test portfolio (cross-link `qa-testing-strategy`).
6. **Release strategy declared** — Roadmap-Based / Timeboxed / Regular / Continuous Deployment / Feature Management-Based. The choice constrains release cadence and feature-flag use.
7. **Production deployment strategy declared** — Re-create / Blue/Green / Rolling Update / Canary / A/B Test. Each has a distinct rollback and risk profile.
8. **The 10 deployment best practices walked**: join user associations; interview existing customers; find experienced consultants; acquire course-creation software; acquire training courses; customize for local needs; develop legacy interfaces; record + report deployment defects; install vendor patches; evaluate success. Each practice either scheduled or marked not applicable.
9. **ERP-class effort recognized** — for ERP-class or large mainframe deployments, the cost / schedule / staffing baseline is $1M+ / 12 months / 25 consultants + 30 in-house. Plans below this baseline for ERP-class work are under-budgeted.
10. **Customization expected, not exception** — large applications require extensive customization for local conditions; side-by-side runs with legacy for several months are typical.

## How you proceed

1. **Classify the application size and class.** PC / Mac / mobile: lightweight pipeline, customer self-install. Mid-size IT: full CI/CD pipeline. ERP / mainframe: full 7-stage + customization + side-by-side runs + ~12-month rollout. Cross-link `product-manager-early-sizing`.
2. **Pick the 7-stage instrumentation.** For each generic-process stage, name the tool / activity / gate.
3. **Pick the strategies** (five axes: branching / build / test / release / production deployment). Document trade-offs for each.
4. **Walk the 10 deployment best practices.** Identify which apply, schedule them, name owners.
5. **For ERP-class work, build the deployment plan** with a 12-month scaffold, consultant + in-house staffing, side-by-side run, customization budget. Surface to Product Manager (`product-manager-project-planning`, `product-manager-cost-estimating`) for inclusion in the overall release plan.
6. **Integrate with QA gates.** Test environments provisioned per pipeline stage; static analysis (cross-link `developer-static-analysis`) integrated; inspection results (cross-link `qa-inspections-program`) feed pipeline progression decisions.
7. **Integrate with configuration control** (cross-link `devops-configuration-control`). Artifacts in the pipeline are versioned and master-locked.
8. **Monitor and evolve** — pipeline metrics fed back to Product Manager for next-release planning (cross-link `product-manager-benchmarks-baselines`).

## Pitfalls to avoid

- **Skipping pipeline stages.** Missing "validate completion criteria" or "dual control" lets unreviewed artifacts through; missing "provide production environment" means environment drift.
- **One strategy fits all.** Branching / build / test / release / deployment are five independent axes — each picked separately based on project parameters.
- **Continuous Deployment without the test stack.** CD requires ~99% DRE upstream (cross-link `qa-defect-removal-efficiency`); without it, CD pushes defects to customers.
- **Blue/Green without rollback discipline.** The strategy requires both environments live and ready; Blue/Green with no rollback plan is just two environments.
- **Canary without metrics gates.** Canary deployment to a slice of traffic without automated quality gates becomes "ship to some users and hope."
- **Under-budgeting ERP deployment.** The empirical baseline is $1M+ / 12 months / 25 consultants + 30 in-house. Plans below this for ERP-class work are systematically optimistic.
- **Treating customization as exception.** For large applications, customization for local conditions is the norm.
- **Adopting a metrics framework as authority.** Humble & Farley's *Continuous Delivery* is the named model here; DORA's *State of DevOps Report* and Kim et al's *Three Ways* are widely-cited practitioner conventions, not this skill's governing body of knowledge.
