---
name: qa-sqa-program
description: "Design and audit the Software Quality Assurance organization for a project, applying Capers Jones's 13-activity SQA role inventory (mandatory above 2,500 FP) and the IBM-model independence imperative (~1–3% of staff, reporting to a senior VP of quality outside the development chain). Use whenever planning the quality program for a new project, deciding whether the team has 'real SQA' or one of the four observed failure patterns (50% test-only, 35% true SQA, 10% none, 5% figurehead), assigning the release-stop authority, or scoping the 10 traditional SQA activities (estimation, measurement, Six Sigma / QFD facilitation, inspection moderation, standards adherence, ISO 9000 / CMMI work, root-cause analysis, training, benchmark acquisition). Triggers include phrases like 'set up SQA', 'is our QA real', 'who has release authority', 'how much QA staffing do we need', 'we report to dev — is that OK', 'SQA vs test team', 'quality program', 'ISO 9000', 'CMMI level'."
---

# qa-sqa-program

## Purpose

Most "SQA" in industry is not SQA. Capers Jones observed that ~50% of companies use the SQA label for what is actually a testing organization, ~10% have no SQA at all, and ~5% have a figurehead SQA without staff. Only ~35% have the IBM-model SQA — an independent function, 1–3% of staff, reporting to its own senior VP of quality, with authority to recommend against release. This skill lets the QA agent stand up or audit that program against the empirically successful pattern, with the independence imperative made explicit because dependent SQA is structurally unable to deliver objective quality reporting.

## When this skill applies

- A new project above ~2,500 FP starts and no SQA program exists.
- The team has "QA" but its reporting line and activities suggest it is actually testing.
- A release is being decided and the question is who holds the authority to recommend against shipping.
- The org is undergoing reorganization and the SQA reporting line is up for negotiation.
- An audit (regulatory, customer, certification) requires demonstrating SQA presence.
- The SQA group is being asked to take on QA functions it is not staffed for.

## Formal criteria

A SQA program is acceptable only if all of the following hold:

1. **Independence is structural** — SQA reports to its own senior vice president of quality, separate from the development organization. SQA reporting to a CIO, VP of software engineering, or development manager fails this criterion regardless of how competent the SQA people are. The independence requirement exists because Jones observed that *"threats of poor appraisals or career damage"* compromise dependent SQA.
2. **Staff ratio in the 1%–5% band** — true SQA in the IBM model is 1%–3% of total software engineering staff, widening to ~5% for development-staff coverage. Below 1% is "token SQA" that cannot review deliverables.
3. **Mandatory above ~2,500 FP** — below this tier SQA may be optional and absorbed by Architect / QA-lite roles; above it, SQA is a named function with named staff.
4. **Release-stop authority exists and the appeal path is defined** — formal SQA approval is a prerequisite for delivery. If SQA recommends against release due to quality issues, the recommendation can be overturned only by the division VP or the corporate president. The appeal path is documented before the first release decision is needed.
5. **All 10 traditional SQA activities accounted for** — for each activity below, the program states either *included* (with named owner) or *not applicable* (with one-line reason):
   1. Collecting and measuring software quality during development and after release (including test results and test coverage; DRE calculation).
   2. Predicting software quality levels for major new applications (estimation tools).
   3. Performing statistical studies of quality / root-cause analysis.
   4. Examining and teaching quality methods such as QFD or Six Sigma for software.
   5. Participating in software inspections as moderators or recorders, and teaching inspections.
   6. Ensuring local, national, and international quality standards are followed (ISO 9000 etc.).
   7. Monitoring CMMI levels and process improvement.
   8. Performing specialized testing such as standards adherence.
   9. Teaching software quality topics to new employees.
   10. Acquiring quality benchmark data from external organizations (ISBSG).
6. **The 12-role SQA inventory covered** — SQA additionally exercises: estimating quality (defect potentials + DRE); measuring defect removal and assigning severity; applying Six Sigma; applying QFD; moderating and participating in inspections; teaching quality classes; monitoring standards adherence; reviewing deliverables; reviewing test plans and quality plans; measuring test results; root-cause analysis; reporting quality problems to higher management; approving release.
7. **The four failure patterns explicitly disqualified** — the program is none of:
   - **Test-only SQA** (~50% pattern): "SQA" name on a testing organization, reporting to development. Compromised authority.
   - **No SQA** (~10% pattern): testing organization, zero SQA staff.
   - **Figurehead SQA** (~5% pattern): VP-SQA-and-two-assistants, no working staff.
   - **Embedded SQA without independence**: SQA staff inside development reporting chains.

## How you proceed

1. **Confirm size tier.** Below ~2,500 FP, SQA is optional; recommend a lite version absorbed by the QA agent. Above, set up formally.
2. **Diagnose the current state against the four organizational patterns.** Which of the four matches what exists today? The ~35% IBM-model is the target; the other three are failure modes.
3. **Establish or relocate the reporting line.** SQA must report to a senior VP of quality outside the development chain. If no such VP exists at the org, the SQA program is structurally compromised and the gap is flagged to executive leadership; the QA agent does not proceed as if the gap were resolved.
4. **Size the SQA staff at 1%–3% of total software engineering staff.** If TSP teams are used, they have internal SQA equivalents and do not need embedded corporate SQA; they still report data to the corporate SQA function.
5. **Walk the activity inventory.** Mark each *included with owner*, *not applicable with reason*, or *outsourced to <named function>*. Silence on an activity is a defect.
6. **Define the release authority and the appeal path.** Formal SQA approval as prerequisite for delivery; appeal path through division VP / corporate president. Document and brief executive leadership before the first release decision.
7. **Coordinate with Testing if it is a separate function.** ~50% of organizations confuse SQA and Testing; in the IBM model they are separate but coordinated — Jones reports that organizations with both a formal SQA organization and a formal testing organization tend to exceed 95% cumulative defect removal efficiency.
8. **Schedule the recurring obligations**: customer satisfaction surveys (annual/semiannual), CMMI assessments, ISO 9000 audits, benchmark data submissions (ISBSG).

## Pitfalls to avoid

- **SQA reporting to dev / CIO.** A dependent SQA cannot do its job — threats of poor appraisals or career damage compromise the function.
- **"Token SQA" understaffing.** Below 1% of staff SQA cannot review deliverables. The label is then a fiction.
- **SQA-as-testing.** The ~50% failure pattern. If the "SQA" group spends >80% of its time running regression / system tests, it is a testing organization. Inspections, estimation, standards, root-cause, benchmark work, and release-authority are the activities that distinguish SQA.
- **Figurehead SQA.** The ~5% pattern. A VP-SQA plus one or two assistants and no working staff exists only "to be played when customers visit". Customers see through it; auditors see through it.
- **Missing release authority.** If SQA cannot recommend against release, the rest of the activities are reduced to advisory work.
- **Quality data used for individual appraisals.** Defect data must NOT feed appraisal or punitive processes — doing so destroys honest reporting and pollutes the SQA data pool.
- **Treating Six Sigma / CMMI / ISO 9000 as SQA's identity.** These are tools SQA uses, not the function itself. Skipping the rest of the activity inventory because "we have CMMI" misses the point.
