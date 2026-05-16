---
name: developer-static-analysis
description: "Run automated static analysis on the Developer's code as both a defect-removal activity (~87% DRE on coding defects) and a defect-prevention activity (programmers spontaneously avoid making the same mistakes after seeing them flagged). Use whenever new code in a supported language (Java, C, C++, C#, dialects — ~50 of the ~2,500 languages) is being written or reviewed, before a code inspection (static analysis catches the structural defects so inspection time focuses on deeper logic), when configuring or tuning a static-analysis tool for the project, or when a defect found in production traces to a class of issue the static analyser could have caught. Triggers include phrases like 'static analysis', 'lint', 'SonarQube', 'Coverity', 'Fortify', 'security scanner', 'configure linter', 'why does the linter complain', 'turn off this rule', 'is static analysis worth it', 'should we tune the rules'."
---

# developer-static-analysis

## Purpose

Automated static analysis tops ~87% defect removal efficiency on common coding defects — the highest single-activity DRE of any non-inspection method. Capers Jones reports the tool category has dual value: static analysis tools, run by programmers, also act as defect-prevention agents — programmers who carefully respond to the defects identified by static analysis spontaneously avoid making the same defects in the future. This skill lets the Developer treat static analysis as a programming discipline — configured per language, tuned to minimize false positives, integrated with code inspection rather than substituting for it.

## When this skill applies

- New code is being written or reviewed in a supported language (Java, C, C++, C#, dialects, others among the ~50 supported languages).
- A static-analysis tool is being selected, configured, or tuned for the project.
- A defect found in production traces to a class of issue static analysis could have detected.
- The team disputes whether to take static-analysis warnings seriously.
- Code inspection is scheduled and static analysis should run first to pre-filter.
- A language not currently supported is being adopted and the team must decide how to compensate.

## Formal criteria

A static-analysis pass is acceptable only if all of the following hold:

1. **Language support verified** — static analysis is best practice for languages where it is supported (Java, C, C++, C#, dialects, ~50 modern languages out of ~2,500). For unsupported languages (MUMPS, Coral, Chill, older / obscure), the program substitutes additional inspection rigor (cross-link `qa-inspections-program`).
2. **DRE level acknowledged** — automated static analysis ~87% DRE on common coding defects. Realistic working figure: 70–85% (the published figures are maxima). Used as the working projection for `qa-defect-removal-efficiency` stack calculations.
3. **Run before code inspection, not instead of** — code inspections after static analysis can find deeper problems such as embedded requirements defects, especially in key modules and algorithms. Static analysis pre-filters the structural defects so inspection time targets the deeper issues.
4. **False positives tuned, not ignored** — false positives are minimized by tuning the static analysis tools to match the specifics of the application. Suppressing entire rules to silence false positives is forbidden; tuning means narrowing the rule to the project's context.
5. **Defect prevention loop closed** — programmers respond to flagged defects, not auto-fix-and-move-on. The learning effect ("spontaneously avoid making the same defects in the future") only happens with deliberate engagement.
6. **Not a substitute for inspection or testing** — static analysis cannot find requirements defects (the Y2K problem is the classic illustration), cannot find embedded business-logic defects, and cannot find performance problems (use dynamic analysis for performance; cross-link `architect-performance-analysis`). It is one layer in the stack, not the stack.
7. **Empirical support beyond one source** — static-analysis tools are widely used by the open-source development community with good results; the practice has empirical support beyond Jones's own data.
8. **Integrated with CI** — modern practice runs static analysis on every commit or pull request. The integration is operationally part of `devops-` pipeline work; Developer is the consumer of the run results.

## How you proceed

1. **Confirm language support.** Java, C, C++, C# dialects → yes. Verify the specific dialect is covered by the chosen tool. Unsupported language → fall back to heavier inspection (cross-link `qa-inspections-program`) and document the gap.
2. **Choose the tool.** Selection criteria: language coverage, rule extensibility, CI integration, false-positive rate on the project's code. The ~87% figure is for the C/Java family; other languages may have different DRE. Selection is documented; tool brand is not authority.
3. **Configure the rule set.** Start from the tool's default rule set; tune additions and suppressions to the project. Document each tuning with a one-line reason.
4. **Run before code inspection.** Static analysis pre-filters structural defects so inspectors target deeper issues. The output is part of the inspection package (cross-link `qa-inspections-program`).
5. **Triage findings.** Each flag → fix / suppress-with-reason / open issue for later. Suppressions carry a comment that explains why; bare suppressions are forbidden.
6. **Close the learning loop.** Periodically review the recurring categories of findings. If the same defect class repeats, the issue is upstream (developer training, design pattern, or build config), not just downstream.
7. **Re-run after defect repairs and significant changes** (cross-link `developer-coding-practices` practice 11). Bad-fix injection rate averages ~5%; re-running static analysis after a fix catches the injection.
8. **Feed the DRE program.** Static analysis findings + post-release defect data feed `qa-defect-removal-efficiency` per-release DRE calculation. Measure the gap between projected and actual.

## Pitfalls to avoid

- **Treating static-analysis output as cosmetic.** The ~87% DRE figure refers to real defects (boundary conditions, calls, links, common code defects). Ignoring warnings drops the layer's DRE to zero.
- **Suppressing rules to silence noise.** Bare rule suppression hides genuine defects. Tune the rule's scope; do not disable it.
- **Static analysis instead of inspection.** Static analysis catches ~87% of structural defects; inspections catch the deeper requirements / design / business-logic defects (cross-link `qa-inspections-program`). Both are needed.
- **Static analysis instead of testing.** Static analysis cannot exercise the running system. Performance, integration, and dynamic-behaviour defects require testing (cross-link `developer-unit-testing` + `qa-testing-strategy`).
- **Auto-fix without engagement.** Some tools offer auto-fix for common findings. Taking the fix without understanding loses the defect-prevention learning effect.
- **Trusting the maximum DRE figure as the working projection.** The published figures are maxima; real-life DRE can be less than half. Use 70–85% as the working figure unless the project has measured otherwise.
- **Unsupported-language complacency.** "We can't use static analysis" is not an excuse to skip the layer; it is a trigger to compensate with heavier inspection.
- **Tool brand as authority.** A static-analysis tool's marketing is not authority; apply the discipline and treat specific tools as convention.
