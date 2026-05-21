---
name: qa-inspections-program
description: "Plan, schedule, and moderate formal inspections of software artifacts (architecture, requirements, design, database design, code, test plans, test cases, user documentation) using the Fagan-origin inspection method — average ~65% defect removal efficiency, peaks 85–88%, the highest single defect-removal method known. Use whenever planning the inspection cadence for a project, deciding what artifacts to inspect, choosing the inspection roles (moderator / recorder / author / reviewer), defending the time and cost of inspections against a 'just test it' push, or building a static-analysis program alongside inspections. Triggers include phrases like 'inspection', 'Fagan inspection', 'code review', 'design review', 'requirements inspection', 'static analysis', 'moderator', 'inspection program', 'why are we inspecting', 'inspection vs test', 'pre-test defect removal'."
---

# qa-inspections-program

## Purpose

Formal inspections originated more than 35 years ago at IBM (Michael Fagan, with Lew Priven, Ron Radice, and later Roger Stewart). Capers Jones reports they remain among the top-ranked methodologies for defect removal efficiency: ~65% average DRE across eight artifact types with peaks of 85–88% (Tom Gilb), versus testing's typical <35% per form. Yet most software organizations do not use inspections — the basic reason is that inspections are in the public domain, so no vendor sells them, while many vendors sell testing tools. This skill lets QA stand up the inspection program against the empirical pattern, run it correctly (the five preconditions), and combine it with static analysis (~87% DRE on structural code defects) — the combination that distinguishes 95%+ DRE organizations.

## When this skill applies

- The team is planning the quality program for a project and inspections are not yet scheduled.
- A defect escaped to production and root cause traces to a missing pre-test inspection.
- A code-review-only culture exists and the gap is the *formal* part (moderator, recorder, prep time, defect log).
- Requirements / architecture / design need inspection but the org has only code reviews.
- A budget conversation requires defending the time cost of inspections.
- Static analysis tools are being evaluated for the project.

## Formal criteria

An inspection program is acceptable only if all of the following hold:

1. **Five Fagan-style preconditions met per session**:
   1. There must be a **moderator** to keep the session moving.
   2. There must be a **recorder** to keep notes.
   3. There must be **adequate preparation time** before each session.
   4. **Records of defects discovered must be kept.**
   5. **Defect data must NOT be used for individual appraisals or punitive purposes** — using it that way destroys honest reporting and kills the program.
   Any inspection lacking any of these is "code review", not Fagan inspection.
2. **Three to six participants per session** — normal complement is four: moderator, recorder, person whose work is being inspected, and at least one other. New hires or specialists (testers) may join occasionally.
3. **All inspectable artifacts considered** — for each, the program either schedules inspection (with cadence) or marks it not applicable (with reason). Typical empirical DRE per artifact:
   - **Requirements inspections** — ~85% DRE. The only known method that removes requirements defects; testing cannot find them.
   - **Architecture inspections** — ~80% DRE.
   - **Design inspections** (external and internal) — ~85% DRE.
   - **Database design inspections.**
   - **Code inspections** — ~85% DRE (legacy code ~83%).
   - **Test plan inspections** — ~80% DRE.
   - **Test case inspections** — ~83% DRE (test scripts ~78%).
   - **User documentation inspections.**
   - **Security inspections of requirements and specifications** (Jones BP #38 practice 3) — a distinct inspection form for Internet-facing / privileged-data / safety-critical applications. Checklist and security reviewer supplied by `security-officer-requirements-and-inspection`; the five Fagan preconditions still apply. This is the only viable removal method for requirements-stage security defects (which testing cannot catch).
4. **Static analysis layered for supported languages** — for Java, C, C++ and other C dialects, automated static analysis is best practice and tops ~87% DRE on common coding defects. For security-specific structural defects, configure security rules in coordination with `security-officer-testing-and-static-analysis` (~25% DRE on security defects when used alone; substantially higher in the combined stack). False positives are minimized by tuning to the application's specifics.
5. **Defect-origin → optimal-removal mapping respected**:
   | Defect origin | Optimal discovery method |
   |---|---|
   | Requirements defects | Formal requirements inspections |
   | Design defects | Formal design inspections |
   | Coding defects | Static analysis + formal code inspections + testing |
   | Document defects | Editing + formal document inspections |
   | Bad fixes | Re-inspection after defect repairs + re-run static analysis + regression testing |
   | Test case defects | Inspection of test cases |
6. **Remote inspections allowed when teams are geographically dispersed** — the original Fagan model used live meetings; effective online tools support remote inspections that save travel cost. The five preconditions still apply.
7. **Defects found within hours / days of origin** — the central rule: defects that originate in a phase should not be allowed downstream. Requirements defects must not reach design; design defects must not reach code.

## How you proceed

1. **Confirm project size tier and risk class.** Inspections are best practice for all mission-critical software. Below ~1,000 FP, inspection cadence can be lighter; above 10,000 FP and for safety-critical or financial systems, full eight-artifact coverage.
2. **Build the inspection schedule** keyed to project milestones (cross-link `product-manager-milestone-tracking`): requirements review → requirements inspection; design milestones → architecture / external / internal design / DB design inspections; code milestone → code inspections; test plan / test case milestones → test plan and test case inspections; documentation milestone → user-doc inspection.
3. **Assign roles per session.** Moderator (often QA / SQA, or an inspection-moderator specialist). Recorder. Author. Reviewer(s). Coordinate participation with Architect, Developer, Designer, Product Manager as appropriate.
4. **Set the preparation requirement.** Each reviewer reads the artifact before the session and prepares notes. Sessions without prep are theatre.
5. **Run the session.** Page-by-page for design / docs; line-by-line for code. Moderator keeps pace; recorder logs defects. Time-box the session; long sessions reduce defect-detection rate.
6. **Record defects** by origin and severity (cross-link `qa-measurements`). The record is for program improvement, not for individual appraisals (precondition 5).
7. **Schedule static analysis** for code in supported languages. Run it before code inspection; the inspection then targets defects static analysis cannot find (embedded requirements defects, deeper logic issues).
8. **Schedule security inspections for security-relevant artifacts.** Jones BP #38 practice 3: for Internet-facing / privileged-data / safety-critical applications, requirements and specs receive a formal security inspection in addition to the generic requirements / spec inspection. Dispatch `security-officer-requirements-and-inspection` for the security-focused checklist and the security expert as additional reviewer. The five Fagan preconditions still apply; record security defects with origin (requirement / spec / threat-model gap / authorization-model gap / configuration / dependency).
9. **Use dynamic analysis for performance / timing defects** — neither inspections nor static analysis catch these well. Cross-link `architect-performance-analysis`.
10. **Re-inspect after defect repairs and after major changes.** Re-inspection prevents the bad-fix injection problem (bug-repair inspection ~70% DRE).
11. **Report DRE per inspection class to the SQA program** (cross-link `qa-sqa-program`). The measurement feeds organizational learning and benchmark submission. Security-specific DRE figures (inspection of requirements / specs for security defects) feed `security-officer-testing-and-static-analysis` for the cumulative security DRE projection.

## Pitfalls to avoid

- **Code-review instead of formal inspection.** No moderator, no recorder, no prep time, no defect log → not Fagan inspection. The ~65% DRE figure does not apply.
- **Using defect data for appraisals.** Destroys honest reporting and pollutes the data pool. The data is for program improvement only.
- **Skipping requirements / architecture / design inspections.** The Y2K problem is the classic illustration: it was a requirements defect; static analysis and testing both miss it. Only requirements inspections find requirements defects.
- **Relying on inspections alone for code defects.** Static analysis at ~87% DRE catches what inspections may miss in supported languages; the combination is the best practice.
- **Skipping inspections because "we test thoroughly".** Testing alone seldom tops 35% per form; cumulative testing seldom tops 80%. Reaching 95%+ DRE requires inspections in the stack.
- **Single inspection role pair.** New-code inspection is necessary but not sufficient. Test plan, test case, and user-doc inspections are systematically skipped and produce escape categories.
- **Long, overstaffed sessions.** Beyond six participants per session the discussion overheads exceed the marginal defect-detection. Four is the modal best practice.
- **No re-inspection after repairs.** Bad-fix injection rate runs ~2–10%. Without re-inspection these become the next release's defects.
- **Security inspections skipped for Internet-facing / privileged-data applications.** Jones lists "Perform security inspections of requirements and specifications" as BP #38 practice 3 — a forcing function. A generic requirements/spec inspection by moderator + recorder + author + reviewer cannot substitute for a security expert participating with a security-focused checklist (`security-officer-requirements-and-inspection`). Requirements-stage security defects cannot be removed by testing alone.
