---
name: qa-testing-strategy
description: "Design the testing portfolio for a project from Capers Jones BP #37 (20+ test forms organized as developer testing, specialist / SQA testing, customer testing), choosing the 3–12 forms typically applied per application — with explicit awareness that cumulative testing-alone DRE seldom tops 80% and the >95% safe minimum requires combining testing with inspections + static analysis. Use whenever planning the test strategy for a project, choosing which test forms to combine, evaluating whether the current testing portfolio is sufficient, defending why testing alone is not enough, deciding which tests are developer-owned vs QA-owned vs customer-owned, or designing the test library management approach. Triggers include phrases like 'test strategy', 'what tests do we need', 'test plan', 'testing portfolio', 'black box white box', 'unit test', 'system test', 'regression', 'acceptance test', 'how many test forms', 'cumulative defect removal'."
---

# qa-testing-strategy

## Purpose

Software testing has been the main form of defect removal since software began (Jones BP #37, p. 128) — and is systematically less effective than inspections per form (~35% DRE vs 65–85% for inspections). Cumulative testing-alone DRE seldom tops 80%, while 95% is the minimum safe level. This skill lets QA design the testing portfolio by choosing 3–12 forms from the 20+ Jones inventories, place ownership correctly (developer / specialist / customer), and combine testing with inspections + static analysis to reach the >95% target. The strategy also addresses test-library hygiene — Jones reports test cases themselves often contain more errors than the software being tested.

## When this skill applies

- Planning the test strategy for a new project.
- Auditing whether the current test portfolio is sufficient to reach the project's DRE target.
- A defect escaped to production and root cause traces to missing test form.
- Test cases are accumulating without coverage analysis; redundancy and error density are unknown.
- Owners (developer vs QA vs customer) of testing activities are unclear.
- Stakeholders push for "testing only" as the quality strategy.

## Formal criteria

A test strategy is acceptable only if all of the following hold:

1. **Three to twelve test forms selected** *(Jones BP #37, p. 128)* — "typically between 3 and 12 forms of testing will be used on almost every software application." The exact selection is justified against the project's defect categories.
2. **Form ownership respected** *(Jones BP #37, pp. 129–130)*:
   - **Developer-owned testing**: subroutine testing, module testing, unit testing.
   - **Specialist / SQA-owned testing**: new function testing, component testing, regression testing, performance testing, security testing, virus + spyware testing, usability testing, scalability testing, standards testing (ISO etc.), nationalization testing, platform testing, independent testing (military), system testing.
   - **Customer / user-owned testing**: external beta testing (commercial), acceptance testing (IT, outsource), in-house customer testing (special hardware).
   Misassigned ownership is the most common test-strategy failure.
3. **Black box / white box / gray box mix declared** *(Jones BP #37, p. 129)* — black box (no knowledge of structure), white box (structure known), gray box (data structures known). Different defect categories need different visibility.
4. **Effort budget acknowledged** *(Jones BP #37, p. 129)* — testing in all forms typically consumes 20%–40% of total software development effort. A test strategy budgeted at 10% is unrealistic for any non-trivial application.
5. **Testing is layered with inspections + static analysis, not standalone** *(Jones BP #37, p. 130)* — "the cumulative efficiency of all forms of testing seldom tops 80 percent, so additional steps such as inspections and static analysis are needed to raise defect removal efficiency levels above 95 percent." A "testing only" strategy is malpractice for mission-critical applications.
6. **Defect prevention portfolio included** *(Jones BP #37, p. 130)* — testing is *defect removal*; the strategy also names the defect *prevention* steps that reduce the input population: JAD, QFD, formal design methods, structured coding, renovation of legacy code, complexity analysis, surgical removal of error-prone modules, formal defect and quality estimation, formal security plans, formal test plans, formal test case construction, formal change management, Six Sigma, CMM/CMMI, TSP/PSP, embedded users (Agile), test-first (XP), daily SCRUM.
7. **Test library hygiene** *(Jones BP #37, p. 129)* — test libraries are huge and require automation. Test cases themselves are subject to defects (some IBM studies found more errors in test cases than in the software). Redundant test cases add cost without rigor. The strategy addresses test-case inspection (Table 9-22 #8: 83% DRE) and redundancy elimination.
8. **Test coverage measured** *(Jones BP #37, p. 130)* — coverage tools used to identify portions of the application where testing is sparse. Typically only ~75% or less of source code is executed during testing; the gap is intentional dead-code-or-rare-path or unintentional miss.
9. **DRE per form recorded** *(Jones BP #37, p. 130 + Table 9-22)* — testing forms have known average DRE (subroutine ~50%, unit ~25%, new function ~35%, regression ~30%, system ~40%, performance ~80%, virus/spyware ~80%). Specialized testing tops 88%–98% on narrow targets.

## How you proceed

1. **Identify the project's defect categories.** Cross-link to `qa-measurements` for defect-by-origin classification. The test strategy targets the categories the project is likely to produce.
2. **Pick the developer-owned test set** (subroutine + module + unit at minimum). Specify whether automated, manual, or both. PSP/TSP unit testing reaches 52% DRE (Table 9-22 #38); plain unit testing 25% (#45) — choose accordingly.
3. **Pick the specialist / SQA-owned test set.** Start with new function + regression + system testing as the baseline (Table 9-22 entries #43, #44, #42). Add performance testing for systems with performance criteria; security + virus + spyware testing for internet-connected applications (Jones BP #37 p. 129 + BP #38); usability testing for user-facing systems; scalability + platform testing for distributed systems; nationalization testing for international releases; standards testing for regulated industries.
4. **Pick the customer / user-owned test set.** Acceptance testing always; external beta for commercial software; in-house customer testing for embedded / special-hardware systems.
5. **Declare visibility mix.** State which tests are black-box, white-box, gray-box. White-box tests can find structural defects; black-box tests find user-visible defects; both are needed.
6. **Budget effort** in the 20%–40% band, weighted toward applications with high reliability requirements.
7. **Schedule test inspection.** Test plan inspection (Table 9-22 #15: 80% DRE), test case inspection (#8: 83%), test script inspection (#16: 78%) — apply before test execution to remove test defects.
8. **Set up coverage measurement.** Specify the coverage tool, the target percentage (75%–95% depending on criticality), and how the gaps will be reviewed.
9. **Integrate with inspections + static analysis** (cross-link `qa-inspections-program`) so cumulative DRE projection reaches >95%. Compute the expected cumulative DRE using Table 9-22 numbers as the working estimates.
10. **Manage the test library** — automation for execution, archival, and search; redundancy elimination; defect-density tracking on test cases themselves.

## Pitfalls to avoid

- **"Testing only" quality strategy.** Cumulative testing alone < 80% DRE. 95% safe minimum requires inspections + static analysis layered (Jones BP #37 p. 130). A test-only plan fails for any non-trivial application.
- **Misassigned ownership.** Unit testing run by SQA, system testing run by developers, acceptance testing run by an internal QA group rather than customers — each misalignment dilutes the test's strength.
- **No coverage measurement.** Without coverage tools, the team does not know which portions were tested. Typically ~25% is left untested by default (BP #37 p. 130).
- **Test cases without inspection.** Test cases have higher error density than the code in some IBM samples (BP #37 p. 129). Test-case inspection (83% DRE) is part of the strategy.
- **Redundant test cases inflate cost.** Multiple developers running parallel testing easily create duplicates. The strategy includes redundancy review.
- **Effort budget at 10% or less.** Testing typically consumes 20–40% of effort; under-budgeting guarantees rushed test execution and missed forms.
- **All-automated or all-manual.** Both have roles. Test plans, test cases, and test scripts still need human design (BP #37 p. 130); automation is for execution, regression, and library management.
- **Skipping security / virus / spyware testing on internet-facing applications.** These forms have 90–98% DRE on their target defects (Table 9-22 #51, #52, #53); skipping them is a security gap, not a test gap.

## Source

- **Best Practice #37 — *Testing and Test Library Control*** (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 128–132). 20+ test forms inventory grouped as developer / specialist / customer; 3–12 forms typically applied per application; testing alone < 80% cumulative DRE; 20–40% of effort consumed by testing; black/white/gray box framing; defect-prevention portfolio list (JAD, QFD, formal design, structured coding, TSP/PSP, embedded users, test-first, Six Sigma, CMM/CMMI); test-library size + automation need; test-case error-density problem.
- **Chapter 9 Table 9-22** (Jones 2010, pp. 615–617) — DRE for testing forms: PSP/TSP unit testing 52% (#38), subroutine testing 50% (#39), XP testing 40% (#40), component testing 40% (#41), system testing 40% (#42), new function testing 35% (#43), regression testing 30% (#44), unit testing 25% (#45); automatic testing average 45%; specialized testing: virus 98% (#51), spyware 98% (#52), security 90% (#53), limits/capacity 90% (#54), penetration 90% (#55), reusability 88% (#56), firewall 87% (#57), performance 80% (#58), nationalization 75% (#59), scalability 65% (#60); user testing: usability 65% (#66), beta 40% (#69), acceptance 25–30% (#70–72).
- **Chapter 9 Table 9-23** — Testers: 10,000 FP assignment scope, defect prevention 15%, defect removal 50% (highest of any role).
- **Cross-reference: inspections needed to reach >95%** — Jones BP #36 (depth in `qa-inspections-program`).
- **Cross-reference: Gherkin acceptance contract for acceptance testing** — Cucumber `gherkin-reference.pdf` (depth in `po-spec-gherkin`).
- Out-of-bibliography (convention pointers only): IEEE 829 test documentation standard, ISTQB testing body of knowledge, agile testing quadrants (Crispin / Gregory).
- Full traceability: `bibliography/skill-references.md` § `qa-testing-strategy`.
