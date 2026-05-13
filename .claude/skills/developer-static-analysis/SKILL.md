---
name: developer-static-analysis
description: "Run automated static analysis on the Developer's code as both a defect-removal activity (~87% DRE on coding defects per Capers Jones Table 9-22) and a defect-prevention activity (programmers spontaneously avoid making the same mistakes after seeing them flagged). Use whenever new code in a supported language (Java, C, C++, C#, dialects — ~50 of the ~2,500 languages) is being written or reviewed, before a code inspection (static analysis catches the structural defects so inspection time focuses on deeper logic), when configuring or tuning a static-analysis tool for the project, or when a defect found in production traces to a class of issue the static analyser could have caught. Triggers include phrases like 'static analysis', 'lint', 'SonarQube', 'Coverity', 'Fortify', 'security scanner', 'configure linter', 'why does the linter complain', 'turn off this rule', 'is static analysis worth it', 'should we tune the rules'."
---

# developer-static-analysis

## Purpose

Automated static analysis tops 87% defect removal efficiency on common coding defects (Jones Table 9-22 #1), the highest single-activity DRE of any non-inspection method. Jones (Ch 8 p. 523) reports the tool category has dual value: "static analysis tools are usually run by programmers, they have a double benefit of also acting as defect prevention agents. In other words, programmers who carefully respond to the defects identified by automated static analysis tools will spontaneously avoid making the same defects in the future." This skill lets the Developer treat static analysis as a programming discipline — configured per language, tuned to minimize false positives, integrated with code inspection rather than substituting for it.

## When this skill applies

- New code is being written or reviewed in a supported language (Java, C, C++, C#, dialects, others among the ~50 supported languages).
- A static-analysis tool is being selected, configured, or tuned for the project.
- A defect found in production traces to a class of issue static analysis could have detected.
- The team disputes whether to take static-analysis warnings seriously.
- Code inspection is scheduled and static analysis should run first to pre-filter.
- A language not currently supported is being adopted and the team must decide how to compensate.

## Formal criteria

A static-analysis pass is acceptable only if all of the following hold:

1. **Language support verified** *(Jones BP #36 p. 125 + Ch 8 p. 523)* — static analysis is best practice for languages where it is supported (Java, C, C++, C#, dialects, ~50 modern languages out of ~2,500). For unsupported languages (MUMPS, Coral, Chill, older / obscure), the program substitutes additional inspection rigor (cross-link `qa-inspections-program`).
2. **DRE level acknowledged** *(Jones Table 9-22 #1)* — automated static analysis ~87% DRE on common coding defects. Realistic working figure: 70–85% (Table 9-22 numbers are maxima per Jones Ch 9 p. 618). Used as the working projection for `qa-defect-removal-efficiency` stack calculations.
3. **Run before code inspection, not instead of** *(Jones BP #36 p. 125)* — Jones: "Code inspections after static analysis can find some deeper problems such as embedded requirements defects, especially in key modules and algorithms." Static analysis pre-filters the structural defects so inspection time targets the deeper issues.
4. **False positives tuned, not ignored** *(Jones BP #36 p. 125)* — false positives are "minimized by 'tuning' the static analysis tools to match the specifics of the applications." Suppressing entire rules to silence false positives is forbidden; tuning means narrowing the rule to the project's context.
5. **Defect prevention loop closed** *(Jones Ch 8 p. 523)* — programmers respond to flagged defects, not auto-fix-and-move-on. The learning effect ("spontaneously avoid making the same defects in the future") only happens with deliberate engagement.
6. **Not a substitute for inspection or testing** *(Jones BP #36 p. 125 + Ch 8 p. 523)* — static analysis cannot find requirements defects (the Y2K problem is the classic illustration), cannot find embedded business-logic defects, and cannot find performance problems (use dynamic analysis for performance; cross-link `architect-performance-analysis`). It is one layer in the stack, not the stack.
7. **Open-source community use as evidence** *(Jones Ch 8 p. 523)* — Jones notes static-analysis tools are "widely used by the open-source development community with good results" — the practice has empirical support beyond Jones's own data. Conventional citation point if challenged.
8. **Integrated with CI** — modern practice runs static analysis on every commit or pull request. The integration is operationally part of `devops-` pipeline work (M5); Developer is the consumer of the run results.

## How you proceed

1. **Confirm language support.** Java, C, C++, C# dialects → yes. Verify the specific dialect is covered by the chosen tool. Unsupported language → fall back to heavier inspection (cross-link `qa-inspections-program`) and document the gap.
2. **Choose the tool.** Jones references ~100 static-analysis tools in 2009. Selection criteria: language coverage, rule extensibility, CI integration, false-positive rate on the project's code. Open-source: e.g., FindBugs / SpotBugs / Checkstyle for Java; clang-tidy for C/C++; pylint for Python (with caveat — Jones's 87% figure is for the C/Java family; other languages may have different DRE). Commercial: Coverity, Fortify, SonarQube. Selection is documented; tool brand is not Jones-anchored authority.
3. **Configure the rule set.** Start from the tool's default rule set; tune additions and suppressions to the project. Document each tuning with a one-line reason.
4. **Run before code inspection.** Static analysis pre-filters structural defects so inspectors target deeper issues. The output is part of the inspection package (cross-link `qa-inspections-program`).
5. **Triage findings.** Each flag → fix / suppress-with-reason / open issue for later. Suppressions carry a comment that explains why; bare suppressions are forbidden.
6. **Close the learning loop.** Periodically review the recurring categories of findings. If the same defect class repeats, the issue is upstream (developer training, design pattern, or build config), not just downstream.
7. **Re-run after defect repairs and significant changes** (cross-link `developer-coding-practices` practice 11). Bad-fix injection rate averages ~5% (Table 9-22); re-running static analysis after a fix catches the injection.
8. **Feed the DRE program.** Static analysis findings + post-release defect data feed `qa-defect-removal-efficiency` per-release DRE calculation. Measure the gap between projected and actual.

## Pitfalls to avoid

- **Treating static-analysis output as cosmetic.** The 87% DRE figure refers to real defects (boundary conditions, calls, links, common code defects). Ignoring warnings drops the layer's DRE to zero.
- **Suppressing rules to silence noise.** Bare rule suppression hides genuine defects. Tune the rule's scope; do not disable it.
- **Static analysis instead of inspection.** Static analysis catches ~87% of structural defects; inspections catch the deeper requirements / design / business-logic defects (cross-link `qa-inspections-program`). Both are needed.
- **Static analysis instead of testing.** Static analysis cannot exercise the running system. Performance, integration, and dynamic-behaviour defects require testing (cross-link `developer-unit-testing` + `qa-testing-strategy`).
- **Auto-fix without engagement.** Some tools offer auto-fix for common findings. Taking the fix without understanding loses the defect-prevention learning effect (Jones Ch 8 p. 523).
- **Trusting the maximum DRE figure as the working projection.** Table 9-22 numbers are maxima (Jones Ch 9 p. 618: "real life ... can be less than half of the nominal maximum"). Use 70–85% as working figure unless the project has measured otherwise.
- **Unsupported-language complacency.** "We can't use static analysis" is not an excuse to skip the layer; it is a trigger to compensate with heavier inspection.
- **Tool brand as authority.** SonarQube / Coverity / Fortify marketing is not Jones-anchored authority. Cite Jones BP #36 + Ch 8 + Table 9-22; reference the tool as convention.

## Source

- **Best Practice #36 — *Inspections and Static Analysis* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 124–128).** Static-analysis best practice for supported languages; ~87% DRE on common coding defects; false-positive tuning rule; "code inspections after static analysis" sequence; ~50 supported languages.
- **Chapter 8 § *Automated static analysis as defect prevention* (Jones 2010, pp. 523–524).** Dual role (removal + prevention); programmer-learning effect; ~50 supported languages out of ~2,500; ~100 tools in 2009; open-source community adoption signal.
- **Chapter 9 Table 9-22 #1** — Automated static analysis: 0 test cases per FP, 87% DRE, 2% bad-fix injection rate.
- **Chapter 9 p. 618** — "Table 9-22 is sorted in descending order of defect removal efficiency. However, the results shown are maximum values. In real life, the range of measured defect removal efficiency can be less than half of the nominal maximum."
- **Cross-references**: `qa-inspections-program` (static analysis pre-filters for inspection), `qa-defect-removal-efficiency` (DRE stack composition), `developer-coding-practices` (practice 8 of 13), `architect-performance-analysis` (static analysis does NOT catch performance defects), `qa-testing-strategy` (static analysis does not exercise running system).
- Out-of-bibliography (convention pointers only): SonarQube, Coverity, Fortify, FindBugs / SpotBugs, Checkstyle, clang-tidy, pylint, ESLint, Semgrep, OWASP rule sets.
- Full traceability: `bibliography/skill-references.md` § `developer-static-analysis`.
