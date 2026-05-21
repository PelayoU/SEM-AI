---
name: developer-reuse-application
description: "Apply already-certified reusable code, designs, or other artifacts when implementing a feature — pulling from the project's certified reuse library (curated by Architect) and respecting the strict hazard rule that uncertified reuse can produce the worst negative ROI in the industry. Use whenever the Developer is about to implement functionality that may already exist as a reusable artifact, evaluating whether a candidate library / class / pattern from the reuse catalog fits the current need, or pushing back on a request to use an uncertified reusable source. Triggers include phrases like 'can we reuse this', 'is there a library for', 'should we adopt this component', 'use the reuse library', 'plug in a reusable module', 'why can't we just use X', 'reusable design', 'reuse this pattern'."
---

# developer-reuse-application

## Purpose

Reuse is the highest-ROI lever in software (about +300% ROI for certified reuse) and the most negative when applied wrong (about −300% for uncertified buggy reuse). Architect designs the reusability strategy (`architect-reusability-strategy`) and runs the certification gate (`architect-reuse-certification`); Developer is the *consumer* of the resulting reuse library. This skill operationalizes the consumer side: how to find the right reusable artifact for the work at hand, plug it in correctly, and refuse uncertified candidates that look attractive but are hazardous.

## When this skill applies

- Implementing a feature that overlaps with functionality already in the reuse library.
- A teammate or stakeholder proposes pulling a library / framework / class / module that is not in the certified library.
- A pattern or design is being applied and the question is whether the project has it already standardized.
- The reuse library lists a candidate whose fit for this case must be evaluated.
- An open-source / commercial dependency is being considered.

## Formal criteria

A reuse application pass is acceptable only if all of the following hold:

1. **Reuse before custom-code** — the work checks the certified reuse library first; custom coding is the fallback, not the default. Jones: "the software industry will continue with high costs and high error rates so long as software applications are custom-coded."
2. **Certified status verified** — the candidate artifact carries the certification certificate from `architect-reuse-certification`. Uncertified reuse is hazardous; Jones: "uncertified reuse is hazardous and can be more expensive than custom development of the same module — hence, the reason the uncertified reuse can have a significant negative return on investment."
3. **Fit evaluated against the present need** — certification verifies the artifact is bug-free + secure; fit verifies it does what the current feature needs. The two are independent. A well-certified artifact applied to the wrong problem produces defects of misuse.
4. **License + provenance checked** — copyright, patent, and license constraints (especially for open-source) must be compatible with the project's distribution model. Cross-link to `architect-reuse-certification` for the warranty record.
5. **Defect-density expectation calibrated** — certified zero-defect-targeted code carries defect potentials around 1/100th of custom code (typical custom: ~15 defects per KLOC; certified reuse can be ~0.15/KLOC). Uncertified code at >1 defect/KLOC plugged into >10 applications has negative combined-debugging ROI.
6. **Code reuse extends beyond source code** — when applying reuse, consider also reusable designs, test cases, HELP text, and work-breakdown structures associated with the code module. The package travels together.
7. **Modification minimized** — modifying certified reusable code voids its certification. Either the modification goes through re-certification (cross-link `architect-reuse-certification`) or the artifact is forked from the library and re-baselined as a project-local artifact. Silent modification of library artifacts is forbidden.
8. **Familiarity gap acknowledged** — it is much harder to debug someone else's unfamiliar code than your own. Reuse imports debugging burden if defects appear; the gain (defect prevention via lower defect potential) only outweighs the burden when certification is genuine.

## How you proceed

1. **Identify the need.** What functional contract must the new code satisfy? Functional signature, performance budget, security constraints. Pull from the parent Gherkin spec (`product-manager-spec-gherkin`).
2. **Search the certified reuse library.** Architect curates it (cross-link `architect-reusability-strategy`). Match against name, taxonomy, contract.
3. **Verify certification status.** Certificate present, version pinned, dependencies tracked, known-defect log accessible. If any is missing, the candidate is *not yet admissible*; refer back to `architect-reuse-certification`.
4. **Evaluate fit.** Does the artifact's contract match the feature's contract? Examine inputs, outputs, side effects, threading model, error semantics. Mismatches large enough to require modification mean either re-certification or reject + custom code.
5. **Check license + provenance** for third-party artifacts. The Architect's certification record carries the warranties.
6. **Plug it in without modification** when fit is good. Document the version and the certification reference in the consuming module so post-release recall can reach this site.
7. **If modification is unavoidable**, either:
   - Submit the modification request to Architect for re-certification of the modified artifact, or
   - Fork the artifact into the project's local code with an explicit "no longer claimed as certified library artifact" marker.
8. **Record the reuse instance.** Every reuse distribution is recorded so a defect / vulnerability post-admission triggers recall to this site.
9. **Reject uncertified candidates with a written reason.** Track refusals — the gap may motivate a future certification effort if the candidate is high-value.

## Pitfalls to avoid

- **Pulling from popular OSS without certification.** Popularity is not certification. A package with 10 million downloads can still have undisclosed defects or back doors.
- **Modifying library artifacts silently.** Voids certification and breaks the recall pipeline. Either re-certify or fork explicitly.
- **Reusing only source code.** The 14 other reusable artifact types (designs, tests, HELP text, etc.) often compound the gain.
- **Plugging a certified artifact into the wrong problem.** Certification verifies the artifact is bug-free; fit is a separate check.
- **Ignoring the familiarity-gap debugging cost.** When defects do appear in reused code, debugging is more expensive than for own code. The certification-derived prevention must be high enough to offset this.
- **Combining many uncertified reusable modules.** Each adds independent defect probability; aggregate quality drops fast. >1 defect/KLOC × >10 applications → negative ROI.
- **Adopting a dependency by brand rather than by the gate.** "Just use Spring" / "use this React library" — the decision needs the certification gate, not the brand.
- **Security-touching dependency adopted on generic certification alone.** For reusable artifacts touching auth, crypto, network, deserialization, or privileged-data handling, the generic certification (`architect-reuse-certification`) is necessary but not sufficient — also dispatch `security-officer-threats-and-defenses` for the security review of the specific dependency. CVE history, known back doors, signing chain, and security-issue cadence are security-specialist judgments, not generalist ones.
