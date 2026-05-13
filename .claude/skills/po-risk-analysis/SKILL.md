---
name: po-risk-analysis
description: "Identify, classify, and mitigate project risks using Capers Jones's 14-category risk inventory and the Cagan four-risks lens, with size-based escalation rules. Use whenever the human asks about risks, wants a risk register, sees warning signs (overruns, scope creep, key person dependencies, security concerns), is starting a project of any meaningful size, or wants to know whether the current risk posture is adequate. Triggers include phrases like 'what could go wrong?', 'risk register', 'project risks', 'we're worried about X', 'is this realistic?', 'risk mitigation', 'red flags', 'should we be concerned about this?'."
---

# po-risk-analysis

## Purpose

Most projects that end in court never performed formal risk analysis (Jones, p. 82). This skill lets the Product Owner make project risk explicit before bad outcomes harden into failure: identifying which of Jones's fourteen empirical risk categories apply, layering Cagan's four product-discovery risks, sizing the level of formality required by the project's function-point scale, and producing mitigations rather than warnings. Risk that is named loses half its power; risk that is mitigated loses the rest.

## When this skill applies

- A new project or release is starting and a risk baseline has not been set.
- Warning signs appear: cost or schedule slipping, requirements churn above 2% per month, a key engineer leaving, a stakeholder going silent.
- Application size crosses an escalation threshold (1,000 / 10,000 / 100,000 function points).
- A pre-mortem is requested before a major commitment.
- Security, legal, or financial review surfaces a category not yet in the register.
- An estimate looks suspiciously confident — confident estimates without risk lists are usually wrong.

## Formal criteria

A risk analysis passes review only if all of the following hold:

1. **Jones's fourteen categories swept** *(Capers Jones, BP #17, pp. 81–82)* — every analysis explicitly walks the canonical list below and either tags each as *applies* with a mitigation or marks it *not applicable* with a one-line reason. Silence on a category is the failure mode Jones observed in litigated projects.
2. **Cagan four risks layered** *(GISF `gisf-life-cycle.pdf` slide 64)* — value risk, usability risk, viability risk, and business viability risk are each addressed. Jones's list is project-execution-centric; Cagan's list catches product-discovery risk that Jones does not enumerate explicitly.
3. **Size escalation respected** *(Jones, p. 82)* —
   - **Below 1,000 FP**: risk management is *optional* but a minimal sweep is still good hygiene.
   - **Above 10,000 FP**: risk assessment is *mandatory*.
   - **Above 100,000 FP**: failure to perform careful risk assessment is *evidence of professional malpractice*.
   The skill must state which tier the project sits in and apply the corresponding formality.
4. **Mitigation per active risk** — every risk tagged *applies* carries a concrete mitigation, an owner (a role, not "the team"), and a re-evaluation trigger (date or event).
5. **Early-and-often, not one-shot** *(Jones, p. 82, "best practices for software risk management")* — the analysis is scheduled to refresh at minimum at every release boundary and on demand when warning signs appear. A one-time risk register is not a risk practice.
6. **Combinatorial budget** *(Jones, p. 83)* — Jones warns that automated models stumble past ten variables and the unaided mind past two. If the register grows past ~10 cross-cutting risks, group them rather than tracking them all flat; clustering preserves analytic usability.

## How you proceed

1. **Anchor the analysis with size and stage.** State function-point size (or best estimate) and project stage (discovery / delivery / release). Without this, the escalation tier and the relevant Cagan risks cannot be set.
2. **Sweep Jones's fourteen categories** *(BP #17, pp. 81–82)*. For each, tag *applies* or *not applicable*:
   1. Outright cancellation due to excessive cost and schedule overruns.
   2. Outright termination due to downsizing or bankruptcy.
   3. Cost overruns in excess of 50% versus initial estimates.
   4. Schedule overruns in excess of 12 months versus initial estimates.
   5. Quality control so inept that the software does not work effectively.
   6. Requirements changes in excess of 2% per calendar month.
   7. Executive or client interference that disrupts the project.
   8. Failure of clients to review requirements and plans effectively.
   9. Security flaws and vulnerabilities.
   10. Performance or speed too slow to be effective.
   11. Loss of key personnel from the project during development.
   12. Presence of error-prone modules in legacy applications.
   13. Patent violations or theft of intellectual property.
   14. External risks (fire, earthquake, hurricane, etc.) and sale/acquisition of similar business units.
3. **Layer Cagan four risks** *(slide 64)*: value (will customers use it?), usability (can they figure it out?), viability (can engineers build it with current technology and skills?), business viability (can sales/marketing/legal/finance cope?). Tag each as *low / medium / high* with a one-line reason.
4. **Apply Jones's seven 2009 best practices for risk management** *(BP #17, p. 82)* — translate each into an action item for this project:
   - Early risk assessment even before full requirements.
   - Early prediction of defect potentials and removal efficiency (consult QA role).
   - Comparison of project risk patterns to similar projects.
   - Acquisition of ISBSG benchmarks for similar applications.
   - Early review of contracts and inclusion of quality criteria.
   - Early analysis of change control methods (link to `po-change-control`).
   - Early analysis of value (link to `po-value-analysis`).
5. **Assign mitigation, owner, and re-evaluation trigger** per active risk. Mitigations name what changes; owners name a role (Architect for technical-feasibility risks, Security for vulnerability risks, PO for scope/value risks, DevOps for performance/deployment risks).
6. **Cluster if the register passes ten cross-cutting risks** *(Jones, p. 83)* — group by theme (e.g., *requirements stability*, *security*, *team capacity*) rather than presenting a flat list that overwhelms the human reader.
7. **Schedule the refresh.** Minimum cadence: release boundary + on-warning-sign. Record the next planned review in the register.

## Pitfalls to avoid

- **One-shot risk registers.** A register written at project start and never updated is the dominant failure mode Jones observed in litigation (p. 82). Schedule the refresh as part of writing the register.
- **Confident-estimate-without-risks.** Jones observed accurate estimates being rejected and replaced by impossible targets driven by business pressure (p. 82). When estimates jump in confidence after a meeting with executives, treat that as risk category #7 (executive interference).
- **Skipping security and external risks because they're rare.** Categories 9 (security) and 14 (external/M&A) are systematically under-weighted because they feel exotic. Tag them explicitly even if the answer is *not applicable, low likelihood* — make the call visible.
- **Owner = "the team".** Mitigations without a named role owner do not get done. Assign to a role, not a person, so the mitigation survives staff changes.
- **Treating Cagan risks as discovery-only.** Value risk and usability risk persist into delivery — a feature can be feasible to build and still not get used. Carry these into release reviews.
- **Importing risk frameworks not in audited bibliography.** PMI risk register conventions, FMEA, FAIR — none are in `bibliography/sources/`. Use Jones + Cagan as the authority surface; cite anything else explicitly as out-of-bibliography if the human requests it.

## Source

- **Best Practice #17 — *Software Project Risk Analysis* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 81–83).** Fourteen-category empirical risk inventory; seven 2009 best practices; size-based escalation rules (1k / 10k / 100k FP); malpractice clause above 100k FP.
- **Cagan four risks (value / usability / viability / business viability)** — Marty Cagan, *Inspired*. Captured in `gisf-life-cycle.pdf` slide 64.
- Full traceability: `bibliography/skill-references.md` § `po-risk-analysis`.
