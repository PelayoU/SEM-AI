---
name: developer-unit-testing
description: "Write and run the developer-owned testing layer — subroutine testing (~50% DRE), module testing, unit testing (~25% plain, ~52% under PSP/TSP discipline) — with explicit awareness that this layer is a complement to inspection + static analysis, not a substitute, and that test cases themselves require inspection because their error density can exceed the code's. Use whenever a Developer is about to write unit / module / subroutine tests for new code, deciding test-first vs test-after, sizing the test coverage target, or evaluating whether unit-test coverage is sufficient given the rest of the DRE stack. Triggers include phrases like 'unit test', 'subroutine test', 'module test', 'how much coverage', 'TDD', 'test-first', 'developer testing', 'should I write a test for this', 'PSP unit test', 'test case inspection', 'coverage target'."
---

# developer-unit-testing

## Purpose

Developer-owned testing is the most-cited and least-effective single layer of quality work: plain unit testing reaches ~25% DRE, with PSP/TSP-disciplined unit testing reaching ~52% — still well below inspections (65–85%) and static analysis (~87%). Yet without it, the upstream stack has no run-time validation of the modules. This skill lets the Developer write the layer correctly: as defect *complement*, not defect *guarantee*; with test cases themselves inspected; with TDD or test-concurrent design when supported; with coverage measured and the gap explicit.

## When this skill applies

- New code is being written and the developer-test layer must be scoped.
- A test-first vs test-after decision is open.
- Coverage measurement shows gaps in the developer-test layer.
- Defects escape unit testing and the analysis points at missing test cases.
- The team disputes whether unit-test work is worth the effort given inspection + static analysis already in the stack.
- Test cases are accumulating and their own quality is uncertain.

## Formal criteria

A developer-test pass is acceptable only if all of the following hold:

1. **The three developer-owned forms are scoped**:
   - **Subroutine testing** — ~0.25 test cases per FP; ~50% DRE; ~2% bad-fix injection.
   - **Module testing** — between subroutine and unit; integrates subroutines within a module.
   - **Unit testing** — ~3.0 test cases per FP at ~25% DRE plain, or ~3.5 test cases per FP at ~52% DRE under PSP/TSP discipline.
   Each form scoped or marked not applicable with a reason.
2. **DRE expectation calibrated** — plain unit testing finds about one bug in three. The team budgets accordingly: more layers needed downstream, or upgrade to PSP/TSP unit-testing discipline (~52% DRE).
3. **Test-first or concurrent test design** — create test cases before or concurrently with the code. Test-after as the default is suboptimal because design pressure on testability is lost.
4. **Test cases inspected** — test cases sometimes contain more errors than the software being tested. Test-case inspection ~83% DRE. Cross-link `qa-inspections-program`.
5. **Coverage measured** — coverage tools identify untested branches; typical applications execute only ~75% of source under test. The coverage gap — intentional (dead code, rare paths) or accidental (missed segments) — is named.
6. **Black-box / white-box / gray-box mix declared** — unit testing typically white-box (structure known to the developer who wrote it); module testing mixed; subroutine testing white-box.
7. **Not a substitute for inspection or static analysis** — unit testing alone is the lowest-DRE layer of the stack. Cumulative DRE >95% requires inspection + static analysis + multi-form testing combined. Cross-link `qa-defect-removal-efficiency`.
8. **Test-library hygiene** — automation for execution and storage; redundancy elimination; defect-density tracking on tests themselves.

## How you proceed

1. **Confirm the parent spec exists.** Gherkin AC from `product-manager-spec-gherkin` are the acceptance contract; developer-tests are the white-box layer below them.
2. **Decide test-first or concurrent test design.** TDD when methodology supports it (XP and similar); concurrent test design otherwise. Test-after is a fallback, not a default.
3. **Pick the form mix.** Subroutine + module + unit for most code. Subroutine testing alone is rarely sufficient; module testing alone misses small-grained defects; unit testing alone misses integration. The combination is the working baseline.
4. **Pick the discipline.** Plain unit testing ~25% DRE. PSP/TSP unit testing ~52% DRE — requires the PSP/TSP measurement discipline (`architect-methodology-selection`). If the project uses TSP, leverage the higher-DRE form; if not, plan more layers downstream.
5. **Design the test cases.** White-box for unit and subroutine (structure known); design for boundary conditions, error paths, edge cases. Cover at minimum the AC paths; extend to the structural paths.
6. **Inspect the test cases before execution** (cross-link `qa-inspections-program`). Test-case inspection ~83% DRE on test defects.
7. **Automate execution and storage.** Test runner, fixtures, isolation, repeatable runs. Treat tests as code: subject to the same coding-practice criteria (cross-link `developer-coding-practices`).
8. **Measure coverage.** Tool of choice for the language. Target: ~85–95% executed for mission-critical code; ~75% for non-critical. Explicit list of intentional gaps (dead code, defensive paths).
9. **Re-run after defect repair.** When a fix changes a module, re-run the developer tests + any module / system tests that touch the module (cross-link `qa-testing-strategy`).
10. **Report DRE per release.** Track developer-test defects-found alongside the stack's other layers; feed `qa-defect-removal-efficiency` projection vs actual.

## Pitfalls to avoid

- **Unit testing as the entire quality strategy.** ~25% DRE plain, ~52% under TSP. Far below the >95% target. Inspection + static analysis + multi-form testing required.
- **Test-after as default.** Loses the design-for-testability pressure that test-first or concurrent design provides.
- **Test cases not inspected.** Higher error density than code in some samples. The ~83%-DRE test-case inspection layer is part of the stack.
- **Coverage not measured.** Without coverage, the ~25% missing source is unknown — dead code, rare paths, or actual miss.
- **High-coverage but low-DRE.** Coverage measures *what was executed*, not *what was effectively tested*. A test that exercises a branch without meaningful assertions raises coverage without raising DRE.
- **Tests not treated as code.** Tests carry their own defects, complexity, comments, structure. Apply `developer-coding-practices` to them too.
- **Skipping subroutine and module testing because "we have unit tests".** Different granularity; different defect categories. Unit alone misses subroutine-level boundary defects.
- **Layer substitution.** Unit tests cannot find requirements defects, design defects, or many of the structural defects static analysis catches. "The unit tests pass" does not clear the upstream defect classes.