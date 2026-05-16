---
name: qa-inspections-program
description: "Plan, schedule, and moderate formal inspections of software artifacts (architecture, requirements, design, database design, code, test plans, test cases, user documentation) using the Fagan-origin inspection method (IBM, 35+ years history) — average 65% defect removal efficiency, peaks 85–88% per Tom Gilb, the highest single defect-removal method known. Use whenever planning the inspection cadence for a project, deciding what artifacts to inspect, choosing the inspection roles (moderator / recorder / author / reviewer), defending the time and cost of inspections against a 'just test it' push, or building a static-analysis program alongside inspections. Triggers include phrases like 'inspection', 'Fagan inspection', 'code review', 'design review', 'requirements inspection', 'static analysis', 'moderator', 'inspection program', 'why are we inspecting', 'inspection vs test', 'pre-test defect removal'."
---

# qa-inspections-program

## Purpose

Formal inspections originated more than 35 years ago at IBM (Michael Fagan with Lew Priven, Ron Radice, and later Roger Stewart). Jones (BP #36, p. 124) reports they remain "among the top-ranked methodologies in terms of defect removal efficiency": 65% average DRE across 8 artifact types with peaks of 85–88% (Tom Gilb), versus testing's typical <35% per form. Yet most software organizations do not use inspections — Jones notes (p. 127) the basic reason is that "inspections are in the public domain... no company except a few training companies tries to 'sell' inspections, while there are many vendors selling testing tools." This skill lets QA stand up the inspection program against the empirical pattern, run it correctly (5 preconditions), and combine it with static analysis (87% DRE on structural code defects) — the combination that distinguishes 95%+ DRE organizations.

## When this skill applies

- The team is planning the quality program for a project and inspections are not yet scheduled.
- A defect escaped to production and root cause traces to a missing pre-test inspection.
- A code-review-only culture exists and the gap is the *formal* part (moderator, recorder, prep time, defect log).
- Requirements / architecture / design need inspection but the org has only code reviews.
- A budget conversation requires defending the time cost of inspections.
- Static analysis tools are being evaluated for the project.

## Formal criteria

An inspection program is acceptable only if all of the following hold:

1. **Five Fagan-style preconditions met per session** *(Jones BP #36, p. 125)*:
   1. There must be a **moderator** to keep the session moving.
   2. There must be a **recorder** to keep notes.
   3. There must be **adequate preparation time** before each session.
   4. **Records of defects discovered must be kept.**
   5. **Defect data must NOT be used for individual appraisals or punitive purposes** — using it that way destroys honest reporting and kills the program.
   Any inspection lacking any of these is "code review", not Fagan inspection.
2. **Three to six participants per session** *(Jones BP #36, p. 125)* — normal complement is four: moderator, recorder, person whose work is being inspected, and at least one other. New hires or specialists (testers) may join occasionally.
3. **All inspectable artifacts considered** *(Jones BP #36, p. 126)* — for each, the program either schedules inspection (with cadence) or marks it not applicable (with reason):
   1. **Architecture inspections** — 80% DRE (Table 9-22 #14).
   2. **Requirements inspections** — 85% DRE (Table 9-22 #2). The only known method that removes requirements defects; testing cannot find them.
   3. **Design inspections** (external) — 85% DRE (Table 9-22 #3). Internal design 85% (#5).
   4. **Database design inspections**.
   5. **Code inspections** — 85% DRE (Table 9-22 #6); legacy code inspections 83% (#10).
   6. **Test plan inspections** — 80% DRE (Table 9-22 #15).
   7. **Test case inspections** — 83% DRE (Table 9-22 #8); test script inspections 78% (#16).
   8. **User documentation inspections**.
4. **Static analysis layered for supported languages** *(Jones BP #36, p. 125)* — for Java, C, C++ and other C dialects, automated static analysis is best practice; tops 87% DRE on common coding defects (Table 9-22 #1). False positives minimized by tuning to the application's specifics.
5. **Defect-origin → optimal-removal mapping respected** *(Jones BP #36, p. 127)*:
   | Defect origin | Optimal discovery method |
   |---|---|
   | Requirements defects | Formal requirements inspections |
   | Design defects | Formal design inspections |
   | Coding defects | Static analysis + formal code inspections + testing |
   | Document defects | Editing + formal document inspections |
   | Bad fixes | Re-inspection after defect repairs + re-run static analysis + regression testing |
   | Test case defects | Inspection of test cases |
6. **Remote inspections allowed when teams are geographically dispersed** *(Jones BP #36, p. 125)* — original Fagan model used live meetings; effective online tools support remote inspections that save travel cost. The 5 preconditions still apply.
7. **Defects found within a few hours / days of origin** *(Jones BP #36, p. 127)* — the central rule: defects that originate in a specific phase should not be allowed downstream. Requirements defects must not reach design; design defects must not reach code.

## How you proceed

1. **Confirm project size tier and risk class.** Inspections are best practice for all mission-critical software (BP #36 p. 127–128). Below ~1,000 FP, inspection cadence can be lighter; above 10,000 FP and for safety-critical or financial systems, full 8-artifact coverage.
2. **Build the inspection schedule** keyed to project milestones (cross-link `product-manager-milestone-tracking`): requirements review milestone → requirements inspection; design milestones → architecture / external / internal design / DB design inspections; code milestone → code inspections; test plan / test case milestones → test plan and test case inspections; documentation milestone → user-doc inspection.
3. **Assign roles per session.** Moderator (often QA / SQA, or inspection moderator specialist per Table 9-23 #20: 1,000 FP scope, 35% defect removal impact). Recorder. Author. Reviewer(s). Coordinate participation with Architect, Developer, Designer, Product Manager as appropriate.
4. **Set preparation requirement.** Adequate prep time (BP #36 p. 125): each reviewer reads the artifact before the session and prepares notes. Sessions without prep are theatre.
5. **Run the session.** Page-by-page for design / docs; line-by-line for code. Moderator keeps pace; recorder logs defects. Time-box the session; long sessions reduce defect-detection rate.
6. **Record defects** by origin and severity (cross-link `qa-measurements`). The record is for program improvement, not for individual appraisals (precondition 5).
7. **Schedule static analysis** for code in supported languages. Run before code inspection; the inspection then targets defects static analysis cannot find (embedded requirements defects, deeper logic issues).
8. **Use dynamic analysis for performance / timing defects** *(BP #36 p. 125)* — neither inspections nor static analysis catch these well. Cross-link `architect-performance-analysis`.
9. **Re-inspect after defect repairs and after major changes.** Re-inspection prevents the bad-fix injection problem (Table 9-22 #21 bug repair inspection: 70% DRE).
10. **Report DRE per inspection class to the SQA program** (cross-link `qa-sqa-program`). The measurement feeds organizational learning and benchmark submission.

## Pitfalls to avoid

- **Code-review instead of formal inspection.** No moderator, no recorder, no prep time, no defect log → not Fagan inspection. The 65% DRE figure does not apply. (BP #36 p. 125.)
- **Using defect data for appraisals.** Jones is explicit (p. 125): destroys honest reporting and pollutes the data pool. The data is for program improvement only.
- **Skipping requirements / architecture / design inspections.** The Y2K problem (Jones p. 124–125) is the classic illustration: it was a requirements defect; static analysis and testing both miss it. Only requirements inspections find requirements defects.
- **Relying on inspections alone for code defects.** Static analysis at 87% DRE catches what inspections may miss in supported languages; the combination is the best practice.
- **Skipping inspections because "we test thoroughly".** Testing alone seldom tops 35% per form; cumulative testing seldom tops 80%. Reaching 95%+ DRE requires inspections in the stack (BP #37 p. 130).
- **Single inspection role pair.** New code inspection is necessary but not sufficient. Test plan, test case, user-doc inspections are systematically skipped and produce escape categories.
- **Long, overstaffed sessions.** Beyond 6 participants per session the discussion overheads exceed the marginal defect-detection. 4 is the modal best practice.
- **No re-inspection after repairs.** Bad-fix injection rate runs 2–10% (Table 9-22). Without re-inspection these become the next release's defects.

## Source

- **Best Practice #36 — *Inspections and Static Analysis*** (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 124–128). Fagan inspection origin (IBM, 35+ years), 5 preconditions for inspection, 3–6 participants per session, 8 inspectable artifacts, 65–85% DRE per artifact, static analysis ~87% DRE on coding defects in C/Java family, defect-origin → optimal-removal table, "inspections are not glamorous" market analysis, Gilb / Priven / Radice / Stewart attribution.
- **Chapter 9 Table 9-22** (Jones 2010, pp. 615–617) — DRE by activity: automated static analysis 87% (#1), requirements inspections 85% (#2), external design inspection 85% (#3), use-case inspection 85% (#4), internal design inspection 85% (#5), new code inspections 85% (#6), reuse certification inspection 84% (#7), test case inspection 83% (#8), legacy code inspections 83% (#10), architecture inspections 80% (#14), test plan inspection 80% (#15), test script inspection 78% (#16), test coverage analysis 77% (#17), pair programming review 75% (#19), bug repair inspection 70% (#21).
- **Chapter 9 Table 9-23** (Jones 2010, p. 621) — Inspection Moderator: 1,000 FP assignment scope, defect prevention impact 27%, defect removal impact 35%.
- **Cross-reference: requirements defects need requirements inspections** — Jones BP #11 (depth in `product-manager-requirements-discovery`).
- Out-of-bibliography (convention pointers only): Tom Gilb books on inspections, IEEE 1028 (Software Reviews and Audits).
- Full traceability: `bibliography/skill-references.md` § `qa-inspections-program`.
