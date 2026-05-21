---
name: product-manager-cost-estimating
description: "Estimate effort, cost, schedule, and quality for a software project using function-point-driven automated estimating tools (COCOMO II, KnowledgePlan, SEER, SLIM, Price-S, SoftCost, CHECKPOINT), with historical benchmarks as defense against unrealistic top-down demands. Use whenever a project size has been established and stakeholders need a cost or schedule projection, when a release boundary requires re-estimation, when a change request crosses the 10-FP threshold, or when an existing estimate looks suspiciously optimistic. Triggers include phrases like 'how much will this cost', 'how long will it take', 'estimate', 'cost estimate', 'effort estimate', 'COCOMO', 'productivity rate', 'budget for this', 'is this estimate realistic', 'why is QA reducing this number'."
---

# product-manager-cost-estimating

## Purpose

Cost estimating fails in two ways: by being manual on projects too large for human heuristics (above 1,000 FP, manual estimates are systematically optimistic; above 10,000 FP, manual estimating is close to professional malpractice), and by being technically correct but politically rejected — accurate estimates are sometimes overruled precisely because they show longer schedules than stakeholders wanted, after which the project has an ~80% chance of outright failure and a ~99% chance of severe overrun. This skill lets the Product Manager produce defensible estimates that survive both technical scrutiny and political pressure: automated tooling above 1,000 FP, historical benchmarks for defense, explicit quality and risk components.

## When this skill applies

- A sizing (`product-manager-early-sizing`) has produced an FP figure and a cost/schedule estimate is needed.
- A release is about to be planned and prior estimates must be refreshed.
- A change request greater than 10 FP arrived (`product-manager-change-control` mandates re-estimation).
- A stakeholder pushes back on an estimate as "too long" or "too expensive" — the question is whether the estimate is wrong or the demand is unrealistic.
- A new project category is being entered where the team's manual estimating intuition has no historical basis.

## Formal criteria

A cost estimate is acceptable only if all of the following hold:

1. **Automated tooling above 1,000 FP** — at 1,000 FP and below, manual and automated estimates are similar in accuracy. Above 10,000 FP, manual is close to malpractice. Established automated tools: CHECKPOINT, COCOMO, KnowledgePlan, Price-S, SEER, SLIM, SoftCost. Use at least one; mature project offices use several and look for convergence.
2. **Primary input is function points** — sizing in FP is the primary input. LOC and screens/reports counts are secondary and tertiary, not substitutes.
3. **Quality estimation included, not only cost and schedule** — quality predictions are part of the estimate. Failing projects systematically omit quality estimation; its absence is a diagnostic sign.
4. **Changing requirements included** — the estimate factors in the 1%–3%/month requirements-creep band. Updating the estimate every few weeks to absorb changes is mandatory when using manual estimates; with automated tools the update is cheap.
5. **Historical benchmarks supplied as defense** — every major-project estimate is supported by ISBSG or in-house historical benchmarks. Even accurate estimates are rejected unless backed by historical data; benchmarks are perceived as being more real than estimates.
6. **All overhead components included** — project management tasks, plans, specifications, and tracking costs. Omitting these is the second most common manual-estimating defect after under-estimating testing.
7. **Risk prediction attached** — a risk-adjusted estimate cross-references `product-manager-risk-analysis`.
8. **Re-estimation cadence stated** — when the estimate will be refreshed (release boundary, +10 FP CR via `product-manager-change-control`, end of each iteration's reality vs. plan delta).

## How you proceed

1. **Confirm sizing exists.** No FP, no estimate. If absent, run `product-manager-early-sizing` first.
2. **Pick the tier.**
   - **Below 1,000 FP**: manual estimate with templates is acceptable; supplement with one automated tool for cross-check.
   - **1,000 – 10,000 FP**: automated tool is the primary, manual estimate is the secondary cross-check.
   - **Above 10,000 FP**: at least two automated tools, look for convergence; trained estimating specialist preferred. Manual estimation alone is malpractice.
3. **Feed the tool the FP figure with growth band.** Estimate three scenarios: low-growth, central, high-growth. The spread is the honest range; the central number is the working figure.
4. **Include all components**: code, paperwork (requirements, design, plans, manuals), testing (the most under-estimated by manual methods), inspections, project management, tracking, defect repair, supply chain, travel, reusable materials credit.
5. **Estimate quality.** Defect potentials by origin (requirements, design, code, documents, bad fixes) and projected defect-removal efficiency. Cross-references QA when that role exists.
6. **Compare to ISBSG / internal benchmarks.** Surface adjacencies: applications of similar class, size, and methodology. The comparison is part of the deliverable — without it, the estimate is undefended. Depth in `product-manager-benchmarks-baselines`.
7. **Stamp the estimate with risk band and assumptions.** Tag which `product-manager-risk-analysis` items materially shift the estimate (e.g., requirements-churn high band, key-personnel risk active).
8. **Hand off and watch for political rejection.** If the estimate is rejected with no technical counter-argument, the rejection itself is a project risk (executive interference; accurate estimates rejected ⇒ ~80% failure / ~99% overrun).

## Pitfalls to avoid

- **Manual estimating on >10,000 FP work.** Close to professional malpractice. If only manual is possible, present it as a band ±50% and surface that automated tooling is the empirical best practice.
- **Estimating only code.** Coding is roughly fairly estimated even by manual methods; testing, paperwork, defect repair, and changing-requirements absorption are where manual estimates collapse. The most under-estimated single category is testing.
- **No historical benchmark.** Estimates without ISBSG or in-house benchmark backing are systematically over-ruled. The benchmark is the political defense.
- **Accepting a top-down "make it half" cut without re-running the tool.** Halving an estimate without changing the inputs that produced it is fiction. Either change the scope (then re-estimate) or refuse the cut with the historical data as defense.
- **Skipping quality estimation.** Projects that omit defect potentials and removal efficiency are systematically among the failing-project set.
- **Estimate-once-forget.** Manual estimates that are not updated when requirements change drift out of touch within weeks. Automated tools enable cheap re-runs — use them.
- **Security testing + Security specialist budget absent.** For Internet-facing / privileged-data applications, the estimate must include security testing staff (~1 per 50,000 FP per Jones Table 5-4), security specialist staff (~1 per 1,000 FP per Jones Table 2-3), and per-release ethical-hacker engagement budget. Dispatch `security-officer-security-program` and `security-officer-testing-and-static-analysis` for the figures. Absent these, the security work appears as "unbudgeted overrun" at release.
