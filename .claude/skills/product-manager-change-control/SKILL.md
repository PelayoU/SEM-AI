---
name: product-manager-change-control
description: "Manage scope changes before release using Capers Jones's 16-practice change-control inventory, with a joint client/development Change Control Board, function-point-quantified change requests, and explicit re-estimation triggers for changes greater than 10 function points. Use whenever a change request arrives, when scope creep is suspected, when a release is at risk because of accepted late changes, when stakeholders argue 'small tweak' on something that ripples across artifacts, or at scheduled CCB reviews. Triggers include phrases like 'scope change', 'change request', 'CR', 'scope creep', 'can we just add', 'late change', 'change control board', 'CCB', 'is this in scope?', 'do we have to re-estimate?'."
---

# product-manager-change-control

## Purpose

Jones is explicit (p. 117): requirements grow 1%–3% per month and accumulate up to 50% of the initial requirement volume by deployment. Change is normal — uncontrolled change kills releases. This skill lets the Product Manager intercept change requests through a formal Change Control Board, quantify each change in function points so cost and schedule re-estimation can fire automatically above the 10-FP threshold, and route changes either into the current release (rare) or into multi-release planning (the default). Without this discipline, late changes silently consume slack and surface at release as missed dates.

## When this skill applies

- A stakeholder asks for "a small addition" mid-release.
- A capability or feature scope appears to be drifting between sprints.
- A new external trigger arrives (regulation, competitor move, business reorg) that may force re-scoping.
- A defect investigation reveals the spec is wrong, not the code — that is a change request.
- A government / regulated context requires traceability of every change to an approved requirement.
- A scheduled CCB review is due.

## Formal criteria

A change-control practice passes review only if all of the following hold:

1. **Joint Client/Development Change Control Board exists** *(Jones BP #33, p. 117, practice 6)* — a single body with both sides represented evaluates each change. Single-sided "I approved it" decisions are the dominant failure mode Jones reports in litigation.
2. **Owners assigned per deliverable** *(Jones BP #33, p. 117, practice 1)* — every key deliverable (requirements, design, code, manuals, tests) has a named owner-role responsible for approving changes that touch it. Ownerless deliverables accept every change.
3. **Locked master copies** *(Jones BP #33, p. 117, practice 2)* — deliverables change only via the formal CR pipeline. Side-channel edits are forbidden.
4. **Function-point quantification per CR** *(Jones BP #33, p. 117, practice 5)* — every change carries a function-point delta. This makes the "is this small?" debate quantitative and is the trigger for re-estimation.
5. **Re-estimation mandatory above 10 FP** *(Jones BP #33, p. 118, practice 13)* — any change greater than 10 function points triggers revised cost and schedule estimates. Below 10 FP can absorb into slack, but the FP count must still be recorded.
6. **Multirelease assignment, not single-release sink** *(Jones BP #33, p. 117, practice 3 + p. 118, practice 15)* — every CR is explicitly routed to a release. The default route for late-arriving CRs is the next release, not the current one.
7. **Business-impact prioritization** *(Jones BP #33, p. 118, practice 14)* — CRs are prioritized by business impact, not by political volume. Tie this to `product-manager-value-analysis` for the impact estimate.
8. **Traceability preserved** *(Jones BP #33, p. 119)* — every CR is traced from origin through the affected artifacts (requirement → spec → code → manual → test). For government / regulated work this is mandatory; for everyone else it is the safety net when audit, defect, or regression questions arrive.
9. **JAD + prototypes used upstream to reduce CR volume** *(Jones BP #33, p. 119)* — Jones observes JAD drops unplanned changes below 1%/month vs the 1%–3% baseline. Investment upstream is cheaper than CCB throughput downstream. Cross-link to `product-manager-requirements-discovery`.
10. **Cross-artifact ripple respected** *(Jones BP #33, p. 119)* — one CR commonly touches requirements, specs, code, manuals, tests, plans, and estimates. The CR record names every artifact it ripples through; partial updates leave inconsistent state.

## How you proceed

1. **Receive the change request.** Treat any "small tweak", "quick add", or defect-that-is-actually-a-spec-change as a CR. A request that bypasses the CR pipeline is the bug.
2. **Open a CR node** in the project graph (a short markdown stub under the affected feature or capability node), capturing: origin, requested change, requesting party, date, and the artifacts it claims to affect.
3. **Size the CR in function points** *(BP #33 practice 5)*. Use FP because it is comparable across teams and historical data. If the team cannot estimate FP, surface that as a precondition gap and pull in `product-manager-early-sizing`.
4. **Decide single-release or multi-release** *(practice 15)*. The default for CRs arriving after roughly 9 months into a release is the next release (Jones BP #11, p. 71). Single-release inclusion is the exception, justified by business impact.
5. **Route to the CCB** *(practice 6 + 12)*. The CCB reviews each CR with the joint client/dev composition. Decisions: accept-current-release / accept-next-release / reject / send-back-for-detail.
6. **Trigger re-estimation if FP > 10** *(practice 13)*. Cost, schedule, and impact estimates are revised. Cross-link to `product-manager-cost-estimating` and `product-manager-milestone-tracking` to update plans.
7. **Update all affected artifacts in the same change-set.** Requirements, spec (`product-manager-spec-gherkin`), affected nodes (capability, feature, story), and the change log under the relevant release node. Partial updates leave the audit trail broken.
8. **Record the decision and rationale** in the CR node. Even rejected CRs are valuable history — they prevent re-litigation.
9. **Review CR throughput periodically.** If CR rate exceeds 3%/month, surface it as a risk under `product-manager-risk-analysis` category 6 (requirements churn). Sustained high rate signals upstream defects in elicitation or in vision/goal stability.

## Pitfalls to avoid

- **"Small change" without FP quantification.** "Small" is a feeling, not a measurement. Without an FP delta there is no objective basis for the 10-FP re-estimation trigger.
- **CCB of one.** Jones is explicit (practice 6): the CCB is joint. Single-sided approval is the fingerprint of litigated projects.
- **Side-channel edits.** Direct edits to "locked master copies" outside the CR pipeline are the failure mode practice 2 exists to prevent.
- **Single-release sink.** Defaulting every late CR into the current release silently consumes slack. Multirelease assignment is the rule, not the exception.
- **Ignoring cross-artifact ripple.** Updating only the requirement and not the spec / tests / manuals leaves the system in inconsistent state. The CR is not done until every named artifact is updated.
- **Treating spec-bugs as code-bugs.** Bug reports that turn out to mean "the spec was wrong" are CRs. Route them through the CCB rather than fixing in code and pretending the spec was always right.
- **No CR rate monitoring.** A team with no view of CR throughput cannot detect creeping requirements (Jones BP #11) until release. Read CR rate weekly.

## Source

- **Best Practice #33 — *Software Change Control Before Release* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 117–119).** Sixteen state-of-the-art change-control practices; 1%–3%/month change rate empirics with 50% cumulative growth; 10-FP re-estimation threshold; JAD's effect on downstream change rate (below 1%/month); cross-artifact ripple inventory.
- **Critical-topic status of change control** — Capers Jones, *Software Engineering Best Practices*, Ch. 1, p. 19 ("three critical topics": quality control, change control, project management). Change control is one of the three; absence is a known cause of project failure.
- **Joint Application Design (JAD) cross-reference for upstream change-rate reduction** — `gisf-delivery-backlog-management.pdf` slides 124–126 (story/spec format) and `product-manager-requirements-discovery` (BP #11).
- Full traceability: `bibliography/skill-references.md` § `product-manager-change-control`.
