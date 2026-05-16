---
name: product-manager-project-planning
description: "Build and maintain the project plan — Work Breakdown Structure, activity network, critical path, historical-benchmark calibration, multi-release segmentation, time allotted for requirements, change handling, inspections, testing, and risk reaction — using Capers Jones's eleven planning-best-practice elements and the GISF multilevel hierarchical planning horizons (Roadmap 1–2 years, Release 2–9 months, Iteration 1–4 weeks). Use whenever a project or release is being planned, when a replan is triggered by significant change, when the schedule looks too aggressive, or when the team is unclear on the WBS. Triggers include phrases like 'project plan', 'WBS', 'work breakdown', 'release plan', 'roadmap', 'critical path', 'when does this finish', 'replan', 'plan vs estimate', 'are we on track'."
---

# product-manager-project-planning

## Purpose

Planning and estimating are related but distinct: planning concerns the network of activities and the critical path; estimating concerns cost, resource, and quality predictions. Failed and delayed projects almost always have planning failures — the five most common being inadequate handling of changing requirements, ignoring staff turnover, allotting too little time for requirements analysis, allotting too little time for inspections and testing, and essentially ignoring risks until they materialize. This skill lets the Product Manager produce and maintain a plan that survives these failure modes by anchoring it in eleven empirical practices and the three GISF planning horizons (Roadmap, Release, Iteration).

## When this skill applies

- A project, release, or major iteration needs an initial plan.
- A significant change has rendered the existing plan stale (CR over 10 FP, staff change, vision/goal shift).
- A milestone slipped and the question is whether the plan can recover or must be redrawn.
- A roadmap horizon needs new releases mapped against the vision.
- A stakeholder asks "when will we finish?" and there is no plan with critical path to answer from.

## Formal criteria

A plan passes review only if all of the following hold:

1. **Work Breakdown Structure exists** — a complete WBS decomposes the work to a level where leaf activities can be estimated and tracked. WBS-less plans cannot expose hidden gaps.
2. **Historical benchmark calibration** — the plan compares to historical benchmarks from similar projects (ISBSG or in-house). A plan whose dates have no historical basis is fiction. Depth in `product-manager-benchmarks-baselines`.
3. **Multi-horizon structure** — three GISF planning horizons coexist:
   - **Roadmap** — 1–2 years, focus on vision and product evolution.
   - **Release** — 2–9 months, focus on the best value within constraints.
   - **Iteration** — 1–4 weeks, focus on the features deliverable now.
   Skipping a horizon (e.g., roadmap-less Agile, or release-less waterfall) is the dominant cause of cross-horizon incoherence.
4. **Critical path identified** — the activity network names the critical path and the slack on non-critical chains. Without the critical path, milestone slips cannot be triaged.
5. **Time allotted for the five most-skipped categories**:
   - Detailed requirements analysis time.
   - Time to handle changing requirements (1%–3%/month).
   - Time for formal inspections.
   - Time for testing and defect repairs.
   - Risk handling time and reserve.
   Plans that under-allocate any of these are diagnostic of failing-project patterns.
6. **Staff hiring and turnover modelled** — explicit accounting for expected joiners and leavers across the schedule horizon. Multi-quarter projects without turnover modelling silently absorb the loss until release.
7. **Multirelease consideration when creep is extreme** — when requirements creep is expected to be high, the plan structures multiple releases at 12–18 month intervals rather than absorbing all churn into one release.
8. **Supply chain and outsourcing accounted for** — multi-company projects model the transfer/coordination time. Implicit assumptions of "one team" are a failure mode when the team is in fact several.
9. **Quality activities allotted** — the full suite of quality control (inspections, static analysis, multiple test stages) has time in the plan. This is the single most under-allotted category in failing projects.

## How you proceed

1. **Confirm sizing and estimate exist.** Planning without size (`product-manager-early-sizing`) and estimate (`product-manager-cost-estimating`) is unanchored. Pull them first.
2. **Place the work on the three horizons.** Roadmap (1–2 y, where the releases live), Release (2–9 mo, what is in this release), Iteration (1–4 w, what is in this iteration). The same scope shows up at three resolutions.
3. **Build the WBS.** Decompose to leaf activities estimable in the underlying estimating tool. Use the team's chart of accounts (`product-manager-benchmarks-baselines` includes the canonical 25-topic list).
4. **Lay out the activity network and identify the critical path.** Tools: Microsoft Project, Artemis Views, equivalents. The output is the schedule plus the activities whose slip moves the release.
5. **Insert the five often-skipped allotments explicitly.** Requirements analysis time, change-handling time, inspection time, test and defect-repair time, risk reserve. Each appears as a labelled WBS line, not as a hidden 10% buffer.
6. **Model staff hiring and turnover.** Project managers typically under-account for the productive ramp-down of leavers and ramp-up of joiners; model both.
7. **Decide single-release or multirelease.** If creep is expected high and the horizon is long, split into releases 12–18 months apart.
8. **Cross-check against historical benchmarks** (`product-manager-benchmarks-baselines`). If the plan finishes 30% sooner than comparable historical projects, treat that as a planning-fiction risk (`product-manager-risk-analysis` — executive interference, or cost-overrun risk).
9. **Stamp the plan with assumptions and re-plan triggers.** Significant change events (>10 FP CR, key staff change, vision/goal shift, milestone slip beyond X%) trigger replan, not buffer absorption.

## Pitfalls to avoid

- **Roadmap-less Agile.** Iteration plans without a release horizon and a roadmap silently lose direction; the iterations may finish but the releases do not converge on the vision.
- **Release-less waterfall.** A single release plan over 18+ months without intermediate releases makes change-absorption catastrophic — every CR competes for the same single delivery slot.
- **No critical path.** Without the critical path the team cannot tell which slip matters. Every activity feels equally urgent.
- **Implicit buffer absorbing skipped categories.** A 10% schedule buffer that has to absorb requirements churn + inspection + test + defect repair + risk has no chance. Allot each explicitly.
- **No staff turnover model.** Multi-quarter plans without turnover modelling consistently overrun.
- **Estimate-as-plan.** Planning and estimating are not the same. A plan needs the activity network and critical path; an estimate provides cost/resource. Conflating them loses the activity structure.
