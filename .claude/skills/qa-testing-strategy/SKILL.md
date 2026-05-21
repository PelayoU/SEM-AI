---
name: qa-testing-strategy
description: "Design the testing portfolio for a project from Capers Jones's 20+ test forms (organized as developer testing, specialist / SQA testing, customer testing), choosing the 3–12 forms typically applied per application — with explicit awareness that cumulative testing-alone DRE seldom tops 80% and the >95% safe minimum requires combining testing with inspections + static analysis. Use whenever planning the test strategy for a project, choosing which test forms to combine, evaluating whether the current testing portfolio is sufficient, defending why testing alone is not enough, deciding which tests are developer-owned vs QA-owned vs customer-owned, or designing the test library management approach. Triggers include phrases like 'test strategy', 'what tests do we need', 'test plan', 'testing portfolio', 'black box white box', 'unit test', 'system test', 'regression', 'acceptance test', 'how many test forms', 'cumulative defect removal'."
---

# qa-testing-strategy

## Purpose

Software testing has been the main form of defect removal since software began — and is systematically less effective than inspections per form (~35% DRE vs 65–85% for inspections). Cumulative testing-alone DRE seldom tops 80%, while 95% is the minimum safe level. This skill lets QA design the testing portfolio by choosing 3–12 forms from the 20+ Capers Jones inventories, place ownership correctly (developer / specialist / customer), and combine testing with inspections + static analysis to reach the >95% target. The strategy also addresses test-library hygiene — test cases themselves often contain more errors than the software being tested.

## When this skill applies

- Planning the test strategy for a new project.
- Auditing whether the current test portfolio is sufficient to reach the project's DRE target.
- A defect escaped to production and root cause traces to a missing test form.
- Test cases are accumulating without coverage analysis; redundancy and error density are unknown.
- Owners (developer vs QA vs customer) of testing activities are unclear.
- Stakeholders push for "testing only" as the quality strategy.

## Formal criteria

A test strategy is acceptable only if all of the following hold:

1. **Three to twelve test forms selected** — typically between 3 and 12 forms of testing are used on almost every software application. The exact selection is justified against the project's defect categories.
2. **Form ownership respected**:
   - **Developer-owned testing**: subroutine testing, module testing, unit testing.
   - **Specialist / SQA-owned testing**: new function testing, component testing, regression testing, performance testing, security testing, virus + spyware testing, usability testing, scalability testing, standards testing, nationalization testing, platform testing, independent testing (military), system testing.
   - **Customer / user-owned testing**: external beta testing (commercial), acceptance testing (IT, outsource), in-house customer testing (special hardware).
   Misassigned ownership is the most common test-strategy failure.
3. **Black box / white box / gray box mix declared** — black box (no knowledge of structure), white box (structure known), gray box (data structures known). Different defect categories need different visibility.
4. **Effort budget acknowledged** — testing in all forms typically consumes 20%–40% of total software development effort. A test strategy budgeted at 10% is unrealistic for any non-trivial application.
5. **Testing is layered with inspections + static analysis, not standalone** — the cumulative efficiency of all forms of testing seldom tops 80%, so inspections and static analysis are needed to raise DRE above 95%. A "testing only" strategy is malpractice for mission-critical applications.
6. **Defect prevention portfolio included** — testing is *defect removal*; the strategy also names the defect *prevention* steps that reduce the input population: JAD, QFD, formal design methods, structured coding, renovation of legacy code, complexity analysis, surgical removal of error-prone modules, formal defect + quality estimation, formal security plans, formal test plans, formal test case construction, formal change management, Six Sigma, CMM/CMMI, TSP/PSP, embedded users (Agile), test-first (XP), daily SCRUM.
7. **Test library hygiene** — test libraries are huge and require automation. Test cases themselves are subject to defects (some studies found more errors in test cases than in the software). Redundant test cases add cost without rigor. The strategy addresses test-case inspection (~83% DRE) and redundancy elimination.
8. **Test coverage measured** — coverage tools identify portions of the application where testing is sparse. Typically only ~75% or less of source code is executed during testing; the gap is intentional dead-code-or-rare-path or an unintentional miss.
9. **DRE per form recorded** — testing forms have known average DRE (subroutine ~50%, unit ~25%, new function ~35%, regression ~30%, system ~40%, performance ~80%, virus/spyware ~98%). Specialized testing tops 88%–98% on narrow targets.

## How you proceed

1. **Identify the project's defect categories.** Cross-link to `qa-measurements` for defect-by-origin classification. The test strategy targets the categories the project is likely to produce.
2. **Pick the developer-owned test set** (subroutine + module + unit at minimum). Specify whether automated, manual, or both. PSP/TSP unit testing reaches ~52% DRE; plain unit testing ~25% — choose accordingly.
3. **Pick the specialist / SQA-owned test set.** Start with new function + regression + system testing as the baseline. Add performance testing for systems with performance criteria; **for Internet-facing / privileged-data / financial / medical / military / classified applications, dispatch `security-officer-testing-and-static-analysis` for the security portfolio: security testing (~65% DRE on security defects, Jones Table 5-6) and ethical hacking (~85% DRE, the highest single-method DRE on security defects) are co-equal forms within the 3–12 portfolio, owned operationally by Security Officer**; usability testing for user-facing systems; scalability + platform testing for distributed systems; nationalization testing for international releases; standards testing for regulated industries.
4. **Pick the customer / user-owned test set.** Acceptance testing always; external beta for commercial software; in-house customer testing for embedded / special-hardware systems.
5. **Declare the visibility mix.** State which tests are black-box, white-box, gray-box. White-box tests find structural defects; black-box tests find user-visible defects; both are needed.
6. **Budget effort** in the 20%–40% band, weighted toward applications with high reliability requirements.
7. **Schedule test inspection.** Test plan inspection (~80% DRE), test case inspection (~83%), test script inspection (~78%) — apply before test execution to remove test defects.
8. **Set up coverage measurement.** Specify the coverage tool, the target percentage (75%–95% depending on criticality), and how the gaps will be reviewed.
9. **Integrate with inspections + static analysis** (cross-link `qa-inspections-program`) so the cumulative DRE projection reaches >95%. Compute the expected cumulative DRE using the per-form figures as working estimates.
10. **Manage the test library** — automation for execution, archival, and search; redundancy elimination; defect-density tracking on test cases themselves.

## Pitfalls to avoid

- **"Testing only" quality strategy.** Cumulative testing alone < 80% DRE. The 95% safe minimum requires inspections + static analysis layered. A test-only plan fails for any non-trivial application.
- **Misassigned ownership.** Unit testing run by SQA, system testing run by developers, acceptance testing run by an internal QA group rather than customers — each misalignment dilutes the test's strength.
- **No coverage measurement.** Without coverage tools, the team does not know which portions were tested. Typically ~25% is left untested by default.
- **Test cases without inspection.** Test cases have higher error density than the code in some samples. Test-case inspection (~83% DRE) is part of the strategy.
- **Redundant test cases inflate cost.** Multiple developers running parallel testing easily create duplicates. The strategy includes redundancy review.
- **Effort budget at 10% or less.** Testing typically consumes 20–40% of effort; under-budgeting guarantees rushed execution and missed forms.
- **All-automated or all-manual.** Both have roles. Test plans, cases, and scripts still need human design; automation is for execution, regression, and library management.
- **Skipping security / virus / spyware testing on internet-facing applications.** These forms have 90–98% DRE on their target defects; skipping them is a security gap, not a test gap.
- **Security testing absent or treated as a checkbox.** Jones names security testing (~65% DRE on security defects) and ethical hacking (~85% DRE) as distinct forms in the 20+ test list. For Internet-facing / privileged-data / financial / medical / military / classified applications, both are required, not optional. Dispatch `security-officer-testing-and-static-analysis` for portfolio scope, DRE figures, and ethical-hacker engagement plan; do not author the security test scope in isolation.
