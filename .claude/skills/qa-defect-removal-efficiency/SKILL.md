---
name: qa-defect-removal-efficiency
description: "Compose the project's defect removal efficiency (DRE) program — selecting from Capers Jones's 80 defect-removal activities, sequencing inspections + static analysis + multi-form testing so the cumulative DRE projection meets the >95% safe minimum or the >99% industry-leader target, and combining defect prevention (JAD / QFD / TSP / structured coding / certified reuse) with defect removal. Use whenever the team has a DRE target and needs to design the activity stack to reach it, when current DRE is below safe, when projecting cumulative DRE for a release plan, or when explaining why no single activity reaches the target and combinations are mandatory. Triggers include phrases like 'defect removal efficiency', 'DRE', 'how do we get to 95 percent', 'defect prevention', 'cumulative DRE', 'quality stack', 'why combine inspections and testing', '99 percent defect removal'."
---

# qa-defect-removal-efficiency

## Purpose

No single defect removal activity reaches the >95% safe minimum on its own. Capers Jones is explicit: cumulative testing-alone DRE seldom tops 80%; inspections-alone average ~65%; static analysis tops ~87% but only on code-structural defects. Industry leaders that exceed 95% (Baldrige winners) — and the few that approach 99% — do so by *composing* the activity stack: defect prevention upstream, inspections + static analysis pre-test, multi-form testing post-build, and SQA oversight throughout. This skill lets QA design that stack against the 80-activity inventory, project the cumulative DRE before commitment, and operate the program so the target is actually reached.

## When this skill applies

- A new project sets a DRE target (95% / 97% / 99%) and the activity stack must be designed.
- An existing project's measured DRE is below target and the gap analysis is needed.
- A release plan projection requires a cumulative-DRE estimate to defend the schedule.
- Stakeholders push for cutting inspections to save time; the impact on cumulative DRE must be computed.
- A regulated industry (medical, defense, finance) requires evidence of the stack design.
- Process improvement is being initiated and the baseline DRE must be measured against the activity portfolio.

## Formal criteria

A DRE program is acceptable only if all of the following hold:

1. **DRE target stated explicitly** — three working targets: 95% minimum safe level (Baldrige threshold), 97% leader band, 99% industry leader. U.S. average ~85%. Below 95% is unsafe for mission-critical applications.
2. **Both prevention and removal are programmed** — *defect prevention* (reduces the input population): JAD for requirements, QFD for quality requirements, formal design methods, structured coding, renovation of legacy code, complexity analysis, error-prone-module surgery, formal defect + quality estimation, formal security plans, formal test plans + cases, formal change management, Six Sigma, CMM/CMMI, TSP/PSP, embedded users (Agile), test-first (XP), daily SCRUM, certified reuse. *Defect removal* (catches the defects that exist): requirements / design / document / security / code inspections, test plan + test case + defect-repair inspection, SQA reviews, automated static analysis, unit / component / new function / regression / performance / system / security / acceptance testing. The program names which prevention + removal activities apply.
3. **Cumulative DRE projection computed** — the chosen activities produce a projected cumulative DRE. Combination math: cumulative defect leakage = product of (1 − DRE_i) across activities. Example: inspections 65% + static analysis 87% + testing combination 80% → leakage = 0.35 × 0.13 × 0.20 = 0.0091 → cumulative DRE ≈ 99.1%. The projection is part of the deliverable.
4. **The Jones synergy stack is the baseline** — a combination of formal inspections of requirements and design, static analysis, formal testing by test specialists, and a formal (and active) SQA group are the methods most often associated with projects achieving cumulative DRE above 99%. Any program that omits a layer must explicitly justify the exclusion.
5. **The 80-activity inventory considered** — activities organized into six categories: static analysis (37 activities, avg ~67% DRE), general testing (8 activities, avg ~41%), automatic testing (5, avg ~45%), specialized testing (15, avg ~70%), user testing (7, avg ~42%), litigation analysis (8, avg ~77%). The program picks the relevant subset; covering all 80 is neither possible nor desirable.
6. **Defect potentials estimated, not just removal** — the program estimates how many defects the project will produce (defect potentials per FP by origin) and how many will leak through the stack. Jones typical: 4.0 defects/FP × 95% removal = 0.2 delivered/FP for successful 10,000-FP projects; 7.0 × 80% = 1.4 delivered/FP for failing projects.
7. **Severity distribution acknowledged** — not all delivered defects are equal. Typical distribution: ~10% serious, the rest minor or cosmetic. The program addresses serious-defect leakage specifically, not just overall counts.
8. **The forbidden metrics excluded** — cumulative DRE is the metric; lines of code per defect and cost per defect are not. Cross-link to `qa-measurements`.

## How you proceed

1. **Set the DRE target** based on application criticality. Mission-critical / regulated → 99%. Standard business application → 95–97%. Internal-only experiment → 90% with explicit acceptance.
2. **Estimate defect potentials** by origin (requirements, design, code, documents, bad fixes). Typical 10,000-FP application: ~4.0 defects/FP successful, ~7.0 failing. Use the project's prior baseline (cross-link `product-manager-benchmarks-baselines`) or industry typical.
3. **Pick the defect prevention activities.** JAD + QFD upstream + structured coding + complexity analysis are the high-impact starter set. Add TSP/PSP for new development at scale; add certified reuse (cross-link `architect-reuse-certification`) when reuse strategy is in place; add embedded users / test-first when methodology supports them.
4. **Pick the inspection set** (cross-link `qa-inspections-program`). Requirements, design, code at minimum; architecture, DB design, test plan, test case for >95% targets; user-doc for safety-critical or customer-impact-sensitive applications.
5. **Pick the static analysis tools** for code in supported languages (Java, C, C++, dialects). ~87% DRE on coding defects. Tune to minimize false positives.
6. **Pick the testing set** (cross-link `qa-testing-strategy`). 3–12 forms typical, spread across developer / specialist / customer ownership.
7. **Schedule SQA oversight** through the stack (cross-link `qa-sqa-program`). SQA reviews are themselves a removal activity (~45% DRE — modest, but adds to the cumulative).
8. **Compute the projected cumulative DRE** using the formula. Validate that the projection meets the target. If not, add layers or upgrade activities (e.g., replace plain unit testing ~25% DRE with TSP/PSP unit testing ~52% DRE).
9. **Operate, measure, and report.** Capture defects found at each stage; compute per-stage and cumulative DRE at release. Submit to the SQA program for organizational learning and benchmark submission.
10. **Re-project when the activity stack changes.** Cutting an inspection layer or downgrading a test form drops cumulative DRE — surface the new projection before the change is committed.

## Pitfalls to avoid

- **Single-layer strategy.** No single activity reaches 95%. Inspections 65% + static analysis 87% + testing 80% only reach 99% *combined*. Single-layer plans miss the target by design.
- **Skipping defect prevention.** Reducing the input population is cheaper than removing defects. A program that focuses only on detection works harder than necessary.
- **Optimistic per-activity DRE.** The published figures are maxima; real-life values are often lower. Project conservatively (use 70–85% of the figures as the working estimate) and confirm by measurement.
- **Activity overlap that double-counts.** Combination math assumes activities catch *independent* defect populations. In practice they overlap; the cumulative projection should haircut for overlap.
- **No defect-potential estimate.** Reporting DRE without defect potential is half the story — 99% DRE on 10 defects/FP is worse than 95% on 3 defects/FP.
- **Stack cut for schedule pressure.** Pulling inspections to "save time" drops cumulative DRE non-linearly. Compute the new projection before agreeing.
- **Ignoring serious-defect leakage.** Aggregate DRE numbers can hide serious-defect escapes. Report serious-defect DRE separately.
- **Importing quality frameworks the project has not audited.** Six Sigma DMAIC, CMMI specific-practice mapping, ISO 9000's principles are useful tools but are not this skill's governing body of knowledge; do not apply them as authority here.
