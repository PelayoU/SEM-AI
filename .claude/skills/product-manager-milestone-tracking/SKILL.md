---
name: product-manager-milestone-tracking
description: "Track progress against the 13 canonical Capers Jones project milestones (requirements review, project plan review, cost/quality estimate review, external/database/internal design reviews, quality+test plan reviews, doc plan, deployment plan, training plan, code inspections, test stages, customer acceptance) — where a milestone is the formal closure of a reviewed deliverable, not a calendar date — and react strongly when problems are reported rather than ignoring them. Use whenever a project is in flight and progress reporting is needed, at scheduled milestone reviews, when a 'milestone' was reported complete but the deliverable was not actually reviewed, or when slippage signals require corrective action. Triggers include phrases like 'milestone', 'milestone review', 'are we on track', 'status report', 'completion', 'milestone slip', 'project tracking', 'how is the project going', 'corrective action'."
---

# product-manager-milestone-tracking

## Purpose

A milestone is not a calendar date but the *formal closure of a reviewed deliverable*. Failing projects reverse this — they treat dates as milestones, report activities finished while work continues, run skimpy reviews, and ignore slippage signals. Across litigated software projects, project tracking was inadequate in every one. This skill lets the Product Manager run milestone reviews against the canonical 13-milestone set, refuse to mark a milestone complete without an actual review of the deliverable, and ensure that surfaced problems trigger corrective action rather than being brushed aside.

## When this skill applies

- A scheduled milestone review is due.
- A status report is requested and the question is whether the team is actually on track.
- Someone reports a milestone "complete" but no review artifact exists.
- A trend (sprint after sprint of soft completion, growing test backlog, optimistic-only status) suggests project tracking is degrading.
- A stakeholder needs a status dashboard before a release boundary.

## Formal criteria

A milestone-tracking pass is acceptable only if all of the following hold:

1. **Milestone = formal review closure of a deliverable, not a calendar date** — a milestone is reached when a deliverable has been reviewed or inspected and accepted, not when a date arrives.
2. **Canonical milestone set covered** — for a nominal 10,000-FP project, the thirteen milestones below are scheduled and either completed or explicitly skipped with rationale:
   1. Requirements review.
   2. Project plan review.
   3. Cost and quality estimate review.
   4. External design reviews.
   5. Database design reviews.
   6. Internal design reviews.
   7. Quality plan and test plan reviews.
   8. Documentation plan review.
   9. Deployment plan review.
   10. Training plan review.
   11. Code inspections.
   12. Each development test stage.
   13. Customer acceptance test.
3. **No completion without review artifact** — reporting completion of any of the above without the review artifact (minutes, defect log, signoff) is a tracking defect and is forbidden.
4. **Strong, immediate reaction to reported problems** — industry leaders react to problem reports with planned corrective actions and task forces; laggards ignore. The tracking system must route surfaced problems to corrective action, not into silence.
5. **Truthful status** — the project office reports truthfully on whether milestones were completed or hit problems. Cosmetic green status on a problem milestone is the failure mode litigated projects share.
6. **Cost tracking parallel to milestone tracking** — actuals vs estimated cost are tracked alongside milestone status, because schedule and cost drift are correlated and reading either alone misses the joint trend.

## How you proceed

1. **Confirm the plan exists and names the milestones.** Without a plan (`product-manager-project-planning`) you cannot identify which of the 13 milestones are scheduled, when, or who owns the review.
2. **Walk the 13 canonical milestones.** For each, classify:
   - **In future**: scheduled, owner named, review artifact placeholder created.
   - **In progress**: review underway, defects being logged.
   - **Closed**: review artifact present (minutes, defect log, signoff). Mark closed only if the artifact exists.
   - **Not applicable**: explicitly skipped with one-line rationale.
3. **Run scheduled milestone reviews as formal events, not as status meetings.** A review identifies defects in the deliverable; a status meeting reports completion. They are different artifacts; do not substitute.
4. **Capture every milestone review's defect log.** Defect counts and types feed into `product-manager-benchmarks-baselines` (defect-potential and defect-removal topics) and into quality estimation for the next release.
5. **Refuse cosmetic closure.** If a milestone is reported done without its review artifact, mark it *open* and surface the gap. Cosmetic green status is the diagnostic sign of every litigated project.
6. **Route surfaced problems to corrective action.** Each surfaced problem gets an owner-role, a corrective plan, and a deadline. Ignored problems are escalated to `product-manager-risk-analysis` as active risks.
7. **Track cost actuals against the estimate per milestone.** Joint schedule + cost drift is the early-warning signal for the risk inventory (cost overruns > 50%, schedule overruns > 12 months).
8. **Report status at each milestone using the same template** so trend-reading across milestones is reliable. Cross-link to `product-manager-benchmarks-baselines` so milestone outputs feed organizational learning.

## Pitfalls to avoid

- **Date-as-milestone.** Calendar dates are not milestones. Without a reviewed deliverable, the date passing means nothing.
- **Cosmetic green status.** Reporting milestones done while review artifacts are missing is the dominant pattern in litigated projects. Refuse.
- **Skimpy reviews.** A 15-minute "review" of a 200-page requirements document is theatre. Inspections need preparation time and structured roles (handled under the QA inspections program when that role is built).
- **Problem reports without corrective action.** Surfaced problems that lead nowhere train the team to stop surfacing them. Always pair a problem with a named corrective action and owner.
- **Tracking schedule without cost (or vice versa).** They drift together. Tracking only one misses the joint trend.
- **Omitting non-coding milestones.** Documentation, deployment, and training plan reviews are often skipped. They are part of the canonical 13 for a reason — their omission emerges as release-time chaos.
