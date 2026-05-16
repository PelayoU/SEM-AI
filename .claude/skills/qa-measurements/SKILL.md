---
name: qa-measurements
description: "Design the project's quality and productivity measurement program using Capers Jones BP #30 (9-measure inventory: effort, costs, milestone progress, dev productivity, maintenance productivity, requirements churn, defects by origin, defect removal efficiency, earned value), with explicit refusal of the two forbidden metrics (lines of code and cost-per-defect) that violate economic assumptions. Use whenever planning what to measure on a project, auditing a measurement program that 'measures nothing useful', deciding whether to track LOC or function points, computing defect removal efficiency, defending why a metric the org uses is wrong, or comparing the org's metrics against ISBSG benchmarks. Triggers include phrases like 'what should we measure', 'metrics', 'KPI', 'defect removal efficiency', 'DRE', 'are these the right metrics', 'lines of code', 'cost per defect', 'how do we measure productivity', 'function points', 'we don't measure anything', 'earned value'."
---

# qa-measurements

## Purpose

Jones (BP #30, p. 112) calls software measurement "embarrassingly bad" and "a professional embarrassment as of 2009". Most organizations measure little; among those that do, many use metrics that violate economic assumptions (lines of code, cost per defect) and produce inverted conclusions. This skill lets QA stand up a measurement program that captures the nine measure types Jones identifies as the state of the art, computes defect removal efficiency correctly, and refuses the two metrics that Jones classifies as malpractice. Without valid measurement, the org cannot know its DRE, cannot benchmark, cannot improve, and cannot defend its work — Jones names this combination as *"professional malpractice"* (BP #30 p. 112).

## When this skill applies

- Setting up the measurement program for a new project or organization.
- An audit reveals the org has no quality measurement at all (Jones: the majority case).
- An estimating, benchmarking, or process-improvement effort is blocked by absence of historical data.
- A stakeholder wants to compare productivity / quality against industry; the metric question opens.
- The team uses LOC or cost-per-defect and the question is whether to keep them.
- A regulatory or customer audit requires DRE evidence.

## Formal criteria

A measurement program is acceptable only if all of the following hold:

1. **All 9 state-of-the-art measure types covered** *(Jones BP #30, p. 110)* — for each, the program either captures the measure with a named owner and cadence, or marks it not applicable with one-line reason:
   1. Accumulated effort.
   2. Accumulated costs.
   3. Accomplishing selected milestones.
   4. Development productivity.
   5. Maintenance and enhancement productivity.
   6. Volume of requirements changes.
   7. Defects by origin.
   8. Defect removal efficiency.
   9. Earned value (mandatory for defense projects; optional civilian).
2. **Function points are the size metric** *(Jones BP #30, p. 111)* — productivity expressed as function points per staff month and/or work hours per function point. Lines of code may appear as a secondary metric for code-density analysis only; LOC as a primary productivity or quality metric is forbidden.
3. **Forbidden metrics excluded** *(Jones BP #30, p. 111)*:
   - **Lines of code** as productivity or quality measure: "penalizes high-level languages and makes assembly language look more productive than any other". Use FP.
   - **Cost per defect**: "penalizes quality and makes buggy software look better than it is". Use defect removal cost per function point instead.
4. **Defect potentials measured by origin** *(Jones BP #30, p. 111)* — at minimum 5 categories: requirements defects, design defects, code defects, documentation defects, bad fixes (secondary bugs introduced while fixing other bugs).
5. **Severity levels recorded** *(Jones BP #35, p. 122)* — every defect carries a severity (1 = system fails completely, descending in seriousness). Number of plateaus varies 1–5.
6. **Defect Removal Efficiency computed correctly** *(Jones BP #30, pp. 111–112)* — DRE = defects found during development / (defects found during development + defects found by clients within a fixed post-release window). Example from Jones: 900 dev-found + 100 client-found in first 3 months ⇒ 90% DRE. Industry-leader band: >95% (Baldrige), 95–99%+ (top performers). U.S. average: ~85%. The post-release window must be fixed and documented; otherwise the metric is not comparable across projects.
7. **ISBSG submission planned** *(Jones BP #30, p. 111)* — for non-classified / non-proprietary applications, the ISBSG data collection tool is used from requirements through development; benchmark data is submitted at end. Cross-link to `product-manager-benchmarks-baselines`.
8. **Cost-of-quality components tracked** *(Jones BP #35, p. 122)* — 9 cost categories: (1) software assessments, (2) quality baseline studies, (3) reviews/inspections/testing, (4) warranty repairs + postrelease maintenance, (5) quality tools, (6) quality education, (7) SQA organization itself, (8) user satisfaction surveys, (9) quality litigation if any. Crosby Cost of Quality principles apply with software-specific extensions.

## How you proceed

1. **Confirm the current state.** Inventory which of the 9 measures are captured today, by whom, at what cadence. The most common answer is "few or none" — Jones BP #30 p. 112.
2. **Pick the size metric.** Function points (IFPUG or COSMIC). If the org uses LOC today, plan migration to FP for primary metrics; LOC stays as secondary.
3. **Set up effort + cost capture** *(measures 1–2)*. Granular enough to support WBS (cross-link to `product-manager-project-planning`). Document the burden-rate assumption explicitly — Jones BP #30 p. 110 warns burden rates distort cross-company comparison.
4. **Set up milestone progress capture** *(measure 3)*. Cross-link to `product-manager-milestone-tracking`. Milestones are formal review closures, not calendar dates.
5. **Set up productivity capture** *(measures 4–5)*. Development productivity in FP per staff month or work hours per FP; maintenance productivity separately because the work is different.
6. **Set up requirements churn capture** *(measure 6)*. Monthly rate. Jones reports the band 0.5%–3% with average 1%–3% and cumulative up to 50%+ by deployment (BP #11). Cross-link to `product-manager-change-control`.
7. **Set up defect tracking** *(measures 7–8)*. By origin (5 categories minimum); by severity (1–5 scale); count both dev-found and client-found in a fixed post-release window. Compute DRE per project at release.
8. **For defense projects, add earned value** *(measure 9)*. Less common in civilian work, but accepted.
9. **Plan benchmark submission** to ISBSG when non-classified/non-proprietary. Submit at release; pull comparables from ISBSG for the next project.
10. **Track cost-of-quality components** in parallel — feeds the economic-value-of-quality argument (BP #35 p. 123: every reduction of 120 delivered defects ≈ one less maintenance staff person; every 240 ≈ one less customer support staff person).

## Pitfalls to avoid

- **Lines of code as productivity / quality metric.** Jones is explicit (BP #30 p. 111): malpractice. It penalizes high-level languages and is uneconomic.
- **Cost per defect as quality metric.** Same source: penalizes quality, makes buggy software look better. Use defect-removal-cost-per-function-point instead.
- **Not measuring DRE.** "Laggards almost never measure quality, while top software companies always do" (BP #30 p. 111). Without DRE the team is blind to its own quality position.
- **DRE without fixed post-release window.** A 90-day window and a 365-day window give different DRE values for the same project; comparing across projects requires the window be fixed and documented.
- **Mixing burden rates without disclosure.** Cross-company cost comparisons distort silently when burden rates vary. Disclose burden assumption with every cost figure.
- **Measurement-as-appraisal.** Jones BP #36 (p. 125) explicitly forbids using defect data for individual appraisals. Doing so kills honest reporting.
- **No historical baseline.** Without baseline, process improvement cannot show progress. Cross-link to `product-manager-benchmarks-baselines`.
- **Adopting metrics from out-of-bibliography frameworks as authority.** PMI / IEEE / ISO have many metric definitions; cite them as convention, not as Jones-anchored authority. The Jones nine-measure set is the audited canonical set.

## Source

- **Best Practice #30 — *Software Project Measurements and Metrics*** (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 110–112). Nine state-of-the-art measure types; FP-as-primary size metric; LOC and cost-per-defect as forbidden metrics; DRE definition with worked example; U.S. average ~85% / leaders >95%; ISBSG ~4,000 projects as of 2008; "measurement is professional malpractice" framing (p. 112).
- **Best Practice #35 — *SQA*** (Jones 2010, pp. 120–124) — severity levels, 9 cost-of-quality components, economic-value-of-quality empirics (120 delivered defects ≈ 1 maintenance staff person; 240 ≈ 1 customer support staff person).
- **Best Practice #11 — *Requirements*** (Jones 2010, pp. 70–72) — requirements-churn empirics for measure 6.
- **ISBSG as benchmark source** — Jones BP #31 (depth in `product-manager-benchmarks-baselines`).
- Out-of-bibliography (convention pointers only): Crosby Cost of Quality (cited via Jones BP #35), PMI/IEEE/ISO metric standards.
- Full traceability: `bibliography/skill-references.md` § `qa-measurements`.
