---
name: devops-legacy-retirement
description: "Plan and execute retirement or replacement of a legacy software application using Capers Jones's 8 retirement best practices (mine business rules + algorithms, survey users, search for similar applications, stabilize legacy during transition, evaluate SOA fit, look for certified reusable material, consider automated language conversion, apply static analysis), with explicit recognition that large systems may have 20–30+ year lifespans (the U.S. air-traffic-control example) and dead-language compiler / scarce-programmer problems. Use whenever a legacy application is being retired or replaced, when a new replacement is being scoped, when migration / SOA fit is being evaluated, when business-rule extraction from legacy code is needed, or when planning the stabilization period of the legacy during replacement. Triggers include phrases like 'retire this application', 'replace the legacy', 'sunset', 'migrate off mainframe', 'rewrite from scratch', 'SOA migration', 'extract business rules', 'dead language', 'COBOL replacement', 'should we retire or rewrite'."
---

# devops-legacy-retirement

## Purpose

Large software applications have surprisingly long life expectancies — 30+ years for U.S. air traffic control, 20+ years for many corporate IT systems. Vendors retire commercial applications more aggressively but often badly (retiring still-popular versions with file-format breakage). Retirement of a custom or large system is not "turn it off" — it requires business-rule mining, user surveys, search for alternatives, often a full replacement application development, and handling of dead-language / scarce-programmer problems. This skill lets DevOps + Architect co-plan retirement / replacement against the 8-practice baseline.

## When this skill applies

- A legacy application is being formally retired.
- Replacement of a legacy by a new custom-built or commercial application is being scoped.
- Migration of a legacy from one platform to another is being planned.
- The legacy's programming language has lost compiler / programmer support (the "dead language" problem).
- SOA fit for the replacement architecture is being evaluated.
- Stabilization of the legacy during a multi-year replacement period is being planned.

## Formal criteria

A retirement / replacement plan is acceptable only if all of the following hold:

1. **Long-lifespan reality acknowledged** — large legacy applications run 20–30+ years; replacement is a multi-year project, not an event. Plans that assume "we replace next quarter" for 10,000+ FP systems are systematically optimistic.
2. **The 8 retirement best practices walked**:
   1. **Mine the application** to extract business rules and algorithms needed for a new version (cross-link `devops-post-release-change` — data mining).
   2. **Survey all users** to determine the importance of the application to business operations.
   3. **Do extensive searches** for similar applications via the web or with consultants (a custom legacy may be replaceable with commercial / OSS).
   4. **Attempt to stabilize the legacy application** so it stays useful while the new one is being built.
   5. **Consider whether SOA may be suitable** for the replacement architecture.
   6. **Look for certified sources of reusable material** (cross-link `architect-reuse-certification`).
   7. **Consider automated language conversion** when the legacy uses dead languages (cross-link `devops-post-release-change` — code conversion).
   8. **Utilize static analysis tools** if the legacy languages are suitable (cross-link `developer-static-analysis`).
3. **Dead-language problem assessed** — older legacy systems often use languages whose compilers / interpreters no longer have working support, with very few programmers available. The plan names this risk explicitly when applicable.
4. **Custom-vs-commercial-replacement decision documented** — when a commercial replacement exists (the typical case for IT systems), evaluate it. When custom features are unique, a new application with all original features + new ones is required.
5. **Trouble expected** — unless an application has zero users, replacement and withdrawal are likely to cause trouble. Plan for it: communication, training, side-by-side run, support during transition.
6. **Architecture choice for replacement** — cross-link `architect-architecture-design` for the seven-fundamental-topics evaluation of the replacement architecture; SOA evaluation is one option among the catalog.
7. **Coordination with Product Manager + Architect** — retirement / replacement is a major project, not just a DevOps operation. Product Manager drives the vision / goals for the replacement; Architect designs it; DevOps runs the retirement + deployment + customer-facing aspects.

## How you proceed

1. **Confirm the project class.** Pure retirement (turn off, no replacement)? Replacement by commercial / OSS? Replacement by custom-built? Migration to a new platform? Each has different scope.
2. **Survey users.** Importance of the application; features they actually use; features they don't. The survey informs the replacement's scope.
3. **Search for similar applications.** For IT systems a commercial replacement often exists (ERP packages, SaaS). For specialized systems often not — custom build required.
4. **Mine the legacy for business rules and algorithms** (cross-link `devops-post-release-change`). The mined rules feed the replacement's requirements (`product-manager-requirements-discovery`).
5. **Apply static analysis if the language is supported.** Find error-prone modules + dead code in the legacy as part of stabilization (cross-link `developer-static-analysis`).
6. **Stabilize the legacy.** It runs for the multi-year replacement period; stabilization keeps it useful, not pristine. Minimal patching, maximal defensive operations.
7. **Evaluate SOA fit for replacement** and other modern architectures (cross-link `architect-architecture-design`).
8. **Search for certified reusable material** for the replacement (cross-link `architect-reuse-certification`).
9. **Plan automated language conversion** if applicable. For dead-language legacy, automated conversion to modern languages is often more economical than rewrite.
10. **Plan the customer / user transition.** Side-by-side run period, communication, training, support escalation during transition (cross-link `devops-customer-support`).

## Pitfalls to avoid

- **"Just turn it off."** For any non-trivial application, replacement and withdrawal will cause trouble. Plan the trouble.
- **Vendor-style sunset.** Commercial vendors sunset old versions with file-format breakage; their pattern is what *not* to do for internal legacy retirement.
- **Underestimating replacement effort.** A 10,000-FP legacy replacement is a 10,000-FP project (plus possibly more for new features). Size and estimate it (cross-link `product-manager-early-sizing` + `product-manager-cost-estimating`).
- **Skipping business-rule mining.** A replacement built from interviews alone misses rules that exist only in legacy code. Data mining is the safety net.
- **Treating SOA as the universal answer.** SOA is one architectural option to evaluate, not a foregone conclusion. Cross-link `architect-architecture-design` for the trade-off analysis.
- **Dead-language replacement without language-conversion tools.** Hand-rewrite from COBOL / MUMPS / PL/I to a modern language is expensive and error-prone. Automated conversion is often the better path.
- **No legacy stabilization plan.** During the 2–5 year replacement period the legacy still runs; defensive operations are part of the retirement plan, not separate from it.