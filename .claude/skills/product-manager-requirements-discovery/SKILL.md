---
name: product-manager-requirements-discovery
description: "Elicit, analyze, and validate software requirements using Capers Jones's 14-practice requirements method (JAD, QFD, prototypes, legacy mining, requirements inspections, traceability) with explicit handling of the empirical 2%/month requirements-churn rate. Use whenever the human starts a new feature area, finds requirements unclear or contradictory, asks how to gather requirements for a legacy replacement, wants to validate that requirements are complete, or is bracing for stakeholder conflict on scope. Triggers include phrases like 'requirements', 'what does the user actually need', 'legacy replacement', 'JAD', 'requirements workshop', 'are these requirements complete?', 'business rules', 'scope discovery', 'requirements traceability'."
---

# product-manager-requirements-discovery

## Purpose

The requirements phase is where large software projects succeed or fail — Capers Jones is explicit that the success or failure of a large software project is determined during the requirements phase. Yet most projects skip the empirical practices that distinguish successful requirements work from documentary theatre. This skill lets the Product Manager run requirements elicitation against the practices Jones validated across thousands of projects, with the understanding that requirements churn is normal (~2%/month average), legacy mining is mandatory (~80% of new applications are replacements), and inspections — not interviews — are the highest-yield activity.

## When this skill applies

- A new feature area is opening and the team needs to gather requirements.
- An existing application is being replaced and the legacy code is the only living spec.
- Stakeholders disagree about what the system should do.
- A spec or backlog item reads vaguely and the upstream requirements appear thin.
- Requirements churn feels high and the human wants to know what is normal.
- A compliance, security, or quality requirement was overlooked and the question is how to systematically prevent recurrence.

## Formal criteria

A requirements pass is acceptable only if the following hold:

1. **Initial elicitation uses at least JAD** — Joint Application Design is the baseline elicitation technique for sizes above ~1,000 FP. Substituting unstructured interviews for JAD is the most common failure mode.
2. **Quality requirements use QFD** — Quality Function Deployment is applied for non-functional requirements (reliability, performance, security, maintainability). Quality requirements not made explicit via QFD silently default to "best effort" and are blamed at release.
3. **Prototypes for key features** — high-risk or novel features are prototyped before written specification. Spec-without-prototype on novel features is high-risk.
4. **Legacy mining when replacing** — for the ~80% of cases where the application replaces existing software, requirements work must include extraction of business rules and algorithms from legacy code, not just stakeholder interviews. Many critical rules live only in legacy code.
5. **Requirements inspections are scheduled** — formal inspections of the requirements document with both users and engineering. Inspections detect defects an interview cycle cannot. This is the highest-yield single practice for requirements quality.
6. **Traceability is enforced** — every requirement has a stable identifier carried into design, code, and test. Without traceability, change impact cannot be assessed and the change control board (`product-manager-change-control`) cannot operate.
7. **Churn is expected and budgeted** — the team plans for 0.5%–3% requirements change per calendar month, with a cumulative range typically 10% to 200% by release time. A plan that assumes zero churn is unrealistic above 500 FP.
8. **Multirelease segmentation** — requirements arriving after roughly 9–12 months are deferred to follow-on releases rather than absorbed into the current one. A single-release sink eventually drowns.

## How you proceed

1. **Classify the situation: new build or legacy replacement.** If replacement (the common case at ~80%), the legacy code is part of the requirements inventory. Plan time to mine it.
2. **Pick the size tier.** Under ~500 FP, lightweight elicitation may suffice. Above 1,000 FP, JAD is the baseline. Above 10,000 FP, the full inventory is needed.
3. **Run JAD for initial elicitation.** A structured group session with users, engineering, and a facilitator (the Product Manager acts as facilitator). The output is a draft requirements list — not a final spec.
4. **Layer QFD for quality requirements.** Walk reliability, performance, security, maintainability, usability one-by-one with the stakeholder who feels the consequence of each. Quality requirements that have no consequence-holder rarely get respected.
5. **Prototype the novel features.** For each high-risk or first-of-its-kind feature, build a thin prototype (often paper or click-through) before the spec is written. Spec-first on novel features ossifies wrong assumptions.
6. **Mine the legacy code.** For replacements, walk the legacy modules with a domain expert and a maintenance workbench. Tag each rule found with its origin and confidence. Many rules are tribal knowledge that will otherwise be lost.
7. **Run a formal requirements inspection.** Roles: moderator, author (the Product Manager), users, engineering reviewer. Inspections detect substantially more defects than interviews per hour invested.
8. **Stand up a joint change control board.** Even at the requirements stage, requirements changes appear. Tag and route them via `product-manager-change-control`. Do not let the requirements document itself silently mutate.
9. **Set traceability from day one.** Assign each requirement a stable identifier and carry it through capability, feature, spec, and test artifacts. Parent / child references between artifacts make the chain navigable end to end.
10. **Plan churn explicitly.** Build the schedule against ~2%/month average churn rather than 0%. Surface this to stakeholders so they understand requirements completion is asymptotic, not binary.

## Pitfalls to avoid

- **Treating interviews as elicitation.** Unstructured interviews are useful complements but cannot substitute for JAD on projects above 1,000 FP.
- **Skipping legacy mining on replacements.** Stakeholders rarely remember every business rule the legacy system encodes. The legacy code is the most reliable source — mine it.
- **Spec without inspection.** Writing the spec and circulating it for "comments" misses the defects a formal inspection would catch. Schedule the inspection as part of writing the spec.
- **Pretending requirements freeze is achievable.** It is not, above 500 FP. Refusing to plan for churn just relocates the problem to release time.
- **No traceability.** A requirement without a stable ID cannot be traced through to test. When change comes, impact analysis collapses.
- **Importing a discovery framework the project has not audited.** Continuous Discovery Habits (opportunity solution trees, weekly continuous interviews) is a strong complement but is not this skill's governing body of knowledge. Use it as practitioner technique; do not apply it as authority here.
