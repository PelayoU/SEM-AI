---
name: qa-measurements
description: "Design the project's quality and productivity measurement program using Capers Jones's 9-measure inventory (effort, costs, milestone progress, dev productivity, maintenance productivity, requirements churn, defects by origin, defect removal efficiency, earned value), with explicit refusal of the two forbidden metrics (lines of code and cost-per-defect) that violate economic assumptions. Use whenever planning what to measure on a project, auditing a measurement program that 'measures nothing useful', deciding whether to track LOC or function points, computing defect removal efficiency, defending why a metric the org uses is wrong, or comparing the org's metrics against ISBSG benchmarks. Triggers include phrases like 'what should we measure', 'metrics', 'KPI', 'defect removal efficiency', 'DRE', 'are these the right metrics', 'lines of code', 'cost per defect', 'how do we measure productivity', 'function points', 'we don't measure anything', 'earned value'."
---

# qa-measurements

## Purpose

Capers Jones calls software measurement "embarrassingly bad" and "a professional embarrassment as of 2009". Most organizations measure little; among those that do, many use metrics that violate economic assumptions (lines of code, cost per defect) and produce inverted conclusions. This skill lets QA stand up a measurement program that captures the nine measure types Jones identifies as the state of the art, computes defect removal efficiency correctly, and refuses the two metrics Jones classifies as malpractice. Without valid measurement, the org cannot know its DRE, cannot benchmark, cannot improve, and cannot defend its work — Jones names this combination *"professional malpractice"*.

## When this skill applies

- Setting up the measurement program for a new project or organization.
- An audit reveals the org has no quality measurement at all (the majority case).
- An estimating, benchmarking, or process-improvement effort is blocked by absence of historical data.
- A stakeholder wants to compare productivity / quality against industry; the metric question opens.
- The team uses LOC or cost-per-defect and the question is whether to keep them.
- A regulatory or customer audit requires DRE evidence.

## Formal criteria

A measurement program is acceptable only if all of the following hold:

1. **All 9 state-of-the-art measure types covered** — for each, the program either captures the measure with a named owner and cadence, or marks it not applicable with a one-line reason:
   1. Accumulated effort.
   2. Accumulated costs.
   3. Accomplishing selected milestones.
   4. Development productivity.
   5. Maintenance and enhancement productivity.
   6. Volume of requirements changes.
   7. Defects by origin.
   8. Defect removal efficiency.
   9. Earned value (mandatory for defense projects; optional civilian).
2. **Function points are the size metric** — productivity expressed as function points per staff month and/or work hours per function point. Lines of code may appear as a secondary metric for code-density analysis only; LOC as a primary productivity or quality metric is forbidden.
3. **Forbidden metrics excluded**:
   - **Lines of code** as productivity or quality measure: it "penalizes high-level languages and makes assembly language look more productive than any other". Use FP.
   - **Cost per defect**: it "penalizes quality and makes buggy software look better than it is". Use defect removal cost per function point instead.
4. **Defect potentials measured by origin** — at minimum 5 categories: requirements defects, design defects, code defects, documentation defects, bad fixes (secondary bugs introduced while fixing other bugs). **For security-relevant projects, security defects are tracked as a 6th origin category (or sub-classified within requirements / design / code with a `@security` tag), with per-method DRE figures from `security-officer-testing-and-static-analysis`: requirements inspection 0% on security, design inspection 25%, code inspection 40%, SAST 25%, security testing 65%, ethical hacking 85% (Jones Table 5-6). Tracking by origin enables shift-left.**
5. **Severity levels recorded** — every defect carries a severity (1 = system fails completely, descending in seriousness). Number of plateaus varies 1–5.
6. **Defect Removal Efficiency computed correctly** — DRE = defects found during development / (defects found during development + defects found by clients within a fixed post-release window). Worked example: 900 dev-found + 100 client-found in the first 3 months ⇒ 90% DRE. Industry-leader band: >95% (Baldrige), 95–99%+ (top performers). U.S. average: ~85%. The post-release window must be fixed and documented; otherwise the metric is not comparable across projects.
7. **ISBSG submission planned** — for non-classified / non-proprietary applications, the ISBSG data collection tool is used from requirements through development; benchmark data is submitted at end. Cross-link to `product-manager-benchmarks-baselines`.
8. **Cost-of-quality components tracked** — 9 cost categories: (1) software assessments, (2) quality baseline studies, (3) reviews/inspections/testing, (4) warranty repairs + post-release maintenance, (5) quality tools, (6) quality education, (7) the SQA organization itself, (8) user satisfaction surveys, (9) quality litigation if any. Crosby's Cost of Quality principles apply with software-specific extensions.

## How you proceed

1. **Confirm the current state.** Inventory which of the 9 measures are captured today, by whom, at what cadence. The most common answer is "few or none".
2. **Pick the size metric.** Function points (IFPUG or COSMIC). If the org uses LOC today, plan migration to FP for primary metrics; LOC stays as secondary.
3. **Set up effort + cost capture** (measures 1–2). Granular enough to support the WBS (cross-link to `product-manager-project-planning`). Document the burden-rate assumption explicitly — burden rates distort cross-company comparison.
4. **Set up milestone progress capture** (measure 3). Cross-link to `product-manager-milestone-tracking`. Milestones are formal review closures, not calendar dates.
5. **Set up productivity capture** (measures 4–5). Development productivity in FP per staff month or work hours per FP; maintenance productivity separately because the work is different.
6. **Set up requirements churn capture** (measure 6). Monthly rate. Jones reports the band 0.5%–3% with average 1%–3% and cumulative up to 50%+ by deployment. Cross-link to `product-manager-change-control`.
7. **Set up defect tracking** (measures 7–8). By origin (5 categories minimum); by severity (1–5 scale); count both dev-found and client-found in a fixed post-release window. Compute DRE per project at release.
8. **For defense projects, add earned value** (measure 9). Less common in civilian work, but accepted.
9. **Plan benchmark submission** to ISBSG when non-classified/non-proprietary. Submit at release; pull comparables from ISBSG for the next project.
10. **Track cost-of-quality components** in parallel — feeds the economic-value-of-quality argument: every reduction of ~120 delivered defects ≈ one less maintenance staff person; every ~240 ≈ one less customer-support staff person.

## Pitfalls to avoid

- **Lines of code as productivity / quality metric.** Malpractice: it penalizes high-level languages and is uneconomic.
- **Cost per defect as quality metric.** Penalizes quality, makes buggy software look better. Use defect-removal-cost-per-function-point instead.
- **Not measuring DRE.** "Laggards almost never measure quality, while top software companies always do." Without DRE the team is blind to its own quality position.
- **DRE without a fixed post-release window.** A 90-day window and a 365-day window give different DRE values for the same project; comparing across projects requires the window be fixed and documented.
- **Mixing burden rates without disclosure.** Cross-company cost comparisons distort silently when burden rates vary. Disclose the burden assumption with every cost figure.
- **Measurement-as-appraisal.** Using defect data for individual appraisals kills honest reporting.
- **No historical baseline.** Without a baseline, process improvement cannot show progress. Cross-link to `product-manager-benchmarks-baselines`.
- **Security defects rolled into "code defects".** Jones names security defects as a distinct category with very different DRE profiles per removal method (Table 5-6: requirements inspection 0% on security, code inspection 40%, SAST 25%, security testing 65%, ethical hacking 85%). Tracking them under "code defects" hides the leakage pattern and prevents shift-left. For security-relevant projects, dispatch `security-officer-testing-and-static-analysis` for the figures and track security as a separate origin category.
- **Importing metric frameworks the project has not audited.** PMI / IEEE / ISO have many metric definitions; the Jones nine-measure set is this skill's canonical set. Do not apply the others as authority here.
