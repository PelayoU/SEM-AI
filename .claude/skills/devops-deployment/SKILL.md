---
name: devops-deployment
description: "Design the deployment pipeline and execute installation of a software application — combining Capers Jones BP #43 (10 deployment best practices, ERP-class effort sizing $1M+ / 12 months / 25 consultants + 30 in-house) with Humble & Farley's Deployment Pipeline model (7 generic stages: Develop → Confirm → Build → Test → Provide → Deploy → Release) captured in GISF `gisf-pipeline-devops.pdf`, branching strategies (Trunk-Based / Feature Branch / Gitflow), and production deployment strategies (Re-create / Blue/Green / Rolling / Canary / A/B / Continuous Deployment / Feature Management). Use whenever designing or auditing a CI/CD pipeline, picking a deployment strategy for a new application, sizing the deployment effort for ERP-class work, planning installation of a major system, or evaluating an existing pipeline against the empirical model. Triggers include phrases like 'deployment pipeline', 'CI/CD', 'continuous delivery', 'continuous integration', 'Blue/Green', 'Canary', 'Rolling deployment', 'A/B test', 'feature flag', 'release strategy', 'install plan', 'ERP deployment', 'pipeline stages'."
---

# devops-deployment

## Purpose

Jones (BP #43 p. 154) flags deployment as "a gray area that is seldom covered by the software literature" yet observes that ERP-class deployment "can take more than 12 calendar months, cost more than $1 million, and involve more than 25 consultants and 30 in-house personnel." Humble & Farley's *Continuous Delivery* (captured in GISF `gisf-pipeline-devops.pdf`) provides the modern model: a 7-stage Deployment Pipeline that gates every change from develop to customer with explicit branching, build, test, release, and production-deployment strategies. This skill lets DevOps combine Jones's empirical deployment effort baseline with Humble & Farley's pipeline model to design or audit the project's pipeline against current best practice.

## When this skill applies

- A new project needs a CI/CD pipeline designed from scratch.
- An existing pipeline is being audited against the 7-stage model.
- A deployment strategy decision is open (Blue/Green vs Rolling vs Canary vs Re-create).
- A branching strategy decision is open (Trunk-Based vs Feature Branch vs Gitflow).
- An ERP-class or large mainframe deployment is being scoped (effort, cost, schedule).
- Continuous Deployment adoption is being evaluated.

## Formal criteria

A deployment pipeline pass is acceptable only if all of the following hold:

1. **7-stage Deployment Pipeline model present** *(GISF `gisf-pipeline-devops.pdf` slide 30, citing Humble & Farley)* — every change traverses: **Develop → Confirm → Build → Test → Provide → Deploy → Release / Deliver to Customer**. A pipeline missing a stage either skips a gate or merges stages without acknowledging the loss.
2. **Generic-process stages instrumented** *(GISF slide 32)* — the detailed process: Validate start criteria → Build → Unit tests → Code analysis → Package artifact → Publish artifact → Provide test environment → Deploy artifact to tests → Run tests → Validate compliance → Validate completion criteria → Dual Control → Provide production environment → Deploy artifact to production → Notify actors. Each stage either runs or is explicitly skipped with rationale.
3. **Branching strategy declared** *(GISF slide 34)* — Trunk-Based / Feature Branch / Gitflow. Gitflow (GISF slides 35–38) is illustrated as the worked example. Trunk-Based is preferred for high-frequency deployment; Gitflow for release-train cadence.
4. **Build strategy declared** *(GISF slide 34)* — Vertical Scaling / Full vs Incremental / Parallel / Pipeline Caching / Build Targets / Cross-Platform / Multiteam. Choice depends on project size and team count.
5. **Test strategy declared** *(GISF slide 34)* — Automated vs Manual / Functional vs Nonfunctional / Parallel vs Sequential / Long Execution vs Short Execution. The choice is constrained by the test portfolio (cross-link `qa-testing-strategy`).
6. **Release strategy declared** *(GISF slide 34)* — Roadmap-Based / Timeboxed / Regular / Continuous Deployment / Feature Management-Based. The choice constrains release cadence and feature-flag use.
7. **Production deployment strategy declared** *(GISF slide 34)* — Re-create / Blue/Green / Rolling Update / Canary / A/B Test. Each has distinct rollback and risk profile.
8. **Jones BP #43 10 practices walked** *(Jones BP #43 pp. 154–155)*: join user associations; interview existing customers; find experienced consultants; acquire course-creation software; acquire training courses; customize for local needs; develop legacy interfaces; record + report deployment defects; install vendor patches; evaluate success. Each practice either scheduled or marked not applicable.
9. **ERP-class effort recognized** *(Jones BP #43 p. 154)* — for ERP-class or large mainframe deployments, the cost / schedule / staffing baseline is $1M+ / 12 months / 25 consultants + 30 in-house. Plans below this baseline for ERP-class work are under-budgeted.
10. **Customization expected, not exception** *(Jones BP #43 p. 155)* — large applications require extensive customization for local conditions; side-by-side runs with legacy for several months typical.

## How you proceed

1. **Classify the application size and class.** PC / Mac / mobile: lightweight pipeline, customer-self-install. Mid-size IT: full CI/CD pipeline. ERP / mainframe: full 7-stage + customization + side-by-side runs + ~12-month rollout. Cross-link `po-early-sizing`.
2. **Pick the 7-stage instrumentation.** For each generic-process stage (GISF slide 32), name the tool / activity / gate.
3. **Pick the strategies** (5 axes: branching / build / test / release / production deployment). Document trade-offs for each.
4. **Walk Jones BP #43 10 practices.** Identify which apply, schedule them, name owners.
5. **For ERP-class work, build the deployment plan** with 12-month scaffold, consultant + in-house staffing, side-by-side run, customization budget. Surface to PO (`po-project-planning`, `po-cost-estimating`) for inclusion in the overall release plan.
6. **Integrate with QA gates.** Test environments provisioned per pipeline stage; static analysis (cross-link `developer-static-analysis`) integrated; inspection results (cross-link `qa-inspections-program`) feed pipeline progression decisions.
7. **Integrate with configuration control** (cross-link `devops-configuration-control`). Artifacts in pipeline are versioned and master-locked.
8. **Monitor and evolve** — pipeline metrics fed back to PO for next-release planning (cross-link `po-benchmarks-baselines`).

## Pitfalls to avoid

- **Skipping pipeline stages.** Missing "Validate completion criteria" or "Dual Control" lets unreviewed artifacts through; missing "Provide production environment" means environment drift.
- **One strategy fits all.** Branching / build / test / release / deployment are 5 independent axes — each picked separately based on project parameters.
- **Continuous Deployment without test stack.** CD requires ~99% DRE upstream (cross-link `qa-defect-removal-efficiency`); without it, CD pushes defects to customers.
- **Blue/Green without rollback discipline.** The strategy requires both environments live and ready; Blue/Green with no rollback plan is just two environments.
- **Canary without metrics gates.** Canary deployment to a slice of traffic without automated quality gates becomes "ship to some users and hope."
- **Under-budgeting ERP deployment.** Jones BP #43 baseline is $1M+ / 12 months / 25 consultants + 30 in-house. Plans below this for ERP-class work are systematically optimistic.
- **Treating customization as exception.** For large applications, customization for local conditions is the norm (BP #43 p. 155).
- **Three Ways / DORA metrics adopted as authority.** GISF cites Humble & Farley *Continuous Delivery*; DORA *State of DevOps Report* and Kim et al *Three Ways* (Flow / Feedback / Continual Learning) are widely-cited but not in audited bibliography. Adopt as practitioner convention.

## Source

- **Best Practice #43 — *Software Deployment and Customization* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 154–155).** Deployment-is-poorly-covered observation; ERP-class baseline ($1M+ / 12 months / 25 consultants + 30 in-house); 10 deployment best practices; side-by-side run pattern; customization as norm for large applications.
- **GISF UC3M `gisf-pipeline-devops.pdf` — Deployment Pipeline model** (slide 30, citing Humble & Farley *Continuous Delivery*). 7-stage model (Develop → Confirm → Build → Test → Provide → Deploy → Release); generic-process detailed instrumentation (slide 32); 5-axis strategy framework (slide 34: branching / build / test / release / deployment); Gitflow worked example (slides 35–38).
- **Cross-references**: `qa-testing-strategy` (test portfolio constrains pipeline test stage), `qa-defect-removal-efficiency` (CD precondition >99% DRE), `developer-static-analysis` (pipeline integration), `qa-inspections-program` (gating), `devops-configuration-control` (artifact versioning), `po-early-sizing` (ERP-class detection), `po-project-planning` + `po-cost-estimating` (deployment plan integration).
- Out-of-bibliography (convention pointers only): Humble & Farley *Continuous Delivery* (book itself not in `sources/`, captured via GISF); Kim et al *The Phoenix Project* / Three Ways; DORA *State of DevOps Report* metrics; specific tooling (Jenkins, GitLab CI, GitHub Actions, ArgoCD, Spinnaker, Tekton).
- Full traceability: `bibliography/skill-references.md` § `devops-deployment`.
