---
name: security-officer-testing-and-static-analysis
description: "Design the security-specific defect-removal portfolio for a project — security testing (~65% DRE on security defects), ethical hacking (~85% DRE), and static analysis for security (~25% DRE) — staffed at ~1 security tester per 50,000 FP. Coordinates with QA's overall testing strategy and DRE programme. Use when designing the test portfolio for a security-relevant application, planning ethical-hacker engagements, integrating static analysis for security into the development pipeline, computing the security contribution to cumulative DRE, or scoping the release security-gate test-pass criterion. Triggers include phrases like 'security testing', 'penetration testing', 'ethical hacker', 'SAST', 'security DRE', 'security test budget', 'static analysis for security'."
---

# security-officer-testing-and-static-analysis

## Purpose

Security defects have low DRE in generic methods (~25% via design / code inspection or generic static analysis) and high DRE in security-specific methods (~65% security testing, ~85% ethical hacking). A project that relies on the generic stack leaks security defects to production; a project that uses the security-specific methods plus the generic stack reaches the cumulative DRE that mission-critical applications need. This skill designs that portfolio, sizes its staffing, and feeds its DRE into the overall QA programme.

## When this skill applies

- A new project's test strategy is being designed and security testing is part of scope.
- An ethical-hacker engagement is being planned for a high-risk class (Internet-facing, financial, healthcare, military, privileged-data).
- Static analysis for security is being integrated into the deployment pipeline.
- The cumulative DRE projection needs the security contribution.
- An existing test programme is audited and the security forms are missing or under-staffed.
- The release security gate (cross-link `security-officer-security-program`) needs the test-pass criteria defined.

## Formal criteria

A security testing and static-analysis portfolio is acceptable only if all of the following hold:

1. **Security testing form scoped, with target DRE ~65% on security defects.** Test cases authored by security specialists, exercising known attack vectors against the application's threat surface (cross-link `security-officer-threats-and-defenses`).
2. **Ethical-hacking form scoped for high-risk classes, with target DRE ~85% on security defects.** External hacking consultants (or qualified internal red team) attempt penetration. Reserved for Internet-facing, financial, healthcare, military, privileged-data classes; rationale recorded if skipped.
3. **Static analysis for security integrated in the development pipeline.** ~25% DRE on security defects when used alone; substantially higher in combination. Coordinated with `developer-static-analysis` (the general SAST integration) and `security-officer-security-program` practice 7 (new code) / practice 8 (legacy code).
4. **Security tester staffed at ~1 per 50,000 FP.** Below the ratio, security testing collapses to a token activity. Ethical hackers are engaged per high-risk release, not per FP.
5. **Cumulative security DRE computed.** The combined leakage formula (leakage = product of (1 − DRE_i)) is computed for the security-specific stack plus the security contribution from inspections and design / code analysis. Mission-critical applications target cumulative security DRE ≥99%; standard business applications target ≥95%.
6. **Coordinated with the QA testing strategy.** Security forms are part of the 3–12 forms `qa-testing-strategy` selects. Effort budget for security testing fits within the 20–40% overall testing budget; over-allocation to security at the expense of other forms is flagged.
7. **Defect-data feedback loop.** Security defects found in test are recorded by origin (requirements / design / code / configuration / dependency) so the programme can shift left across releases — defects whose origin is requirements are addressed in SRD (`security-officer-requirements-and-inspection`), not by more testing.
8. **Pre-release security test pass declared.** The release security gate (cross-link `security-officer-security-program`) names the test-pass criterion: zero open Sev-1 security defects, zero open Sev-2 without compensating control, ethical-hacker engagement complete for in-scope classes, SAST clean on configured security rules.

## How you proceed

1. **Confirm class of application.** Internet-facing, financial, healthcare, military, privileged-data → ethical-hacking form mandatory. Internal / commodity → ethical-hacking can be deferred or scoped narrower.
2. **Size the security testing budget.** ~1 security tester per 50,000 FP; staffing required for the test-cases-per-FP rate to match the threat surface complexity. Surface to `product-manager-cost-estimating` so cost is in the estimate.
3. **Pick test forms.** Security testing (always); ethical hacking (for in-scope classes); static analysis for security (always — but practically integrated via the pipeline, not run by the security tester).
4. **Coordinate with QA.** Submit the security forms to `qa-testing-strategy` as part of the 3–12 forms; ensure the effort budget aggregates within 20–40% overall testing; participate in test-case inspection (~83% DRE) per `qa-inspections-program`.
5. **Integrate SAST in the pipeline.** Coordinate with `developer-static-analysis` (general SAST) and `devops-deployment` (pipeline integration); tune the security rule set; suppressions require recorded reasoning (no bare suppressions).
6. **Engage ethical hackers per release for in-scope classes.** External consultants preferred for independence; engagement scope documented; findings triaged by severity; remediation tracked.
7. **Compute the cumulative security DRE.** Per-form DRE × per-stage haircut for overlap; project conservatively (70–85% of published DRE figures); validate against target.
8. **Record the security release gate criteria.** Pre-release pass: SAST clean, security test pass, ethical-hacker pass for in-scope, no open Sev-1, no open Sev-2 without compensating control.
9. **Run defect-origin analysis after each release.** Security defects from requirements / design feed `security-officer-requirements-and-inspection` (shift-left); from code feed `developer-coding-practices`; from configuration feed `devops-configuration-control`; from dependencies feed `architect-reuse-certification`.

## Pitfalls

- **Security testing replaced by static analysis.** SAST alone is ~25% DRE on security defects. Security testing is ~65%. Ethical hacking is ~85%. The combination matters; substitution misses the target.
- **Ethical hacking treated as optional for Internet-facing applications.** The 85% DRE figure is the highest of any removal method for security defects; skipping it for high-risk classes is malpractice.
- **Internal red-team only.** External engagement is preferred for independence; internal red-team is acceptable if independence from development is structural (cross-link `security-officer-security-program` independence criterion).
- **SAST suppressions used to silence noise.** Bare suppression hides genuine defects; tuning rule scope is the response, not blanket suppression.
- **Cumulative DRE computed without overlap haircut.** Per-form DRE figures assume independent defect populations; in practice overlaps exist. Haircut the projection by 10–20% for overlap.
- **Defect origin not tracked.** Without origin tracking, the programme cannot shift defect removal left to where the defect originated.
- **Security forms over-allocated within the testing budget.** Security is 20–40% of total testing in high-risk classes; eating the entire budget starves other necessary forms (performance, usability, regression). Coordinate with `qa-testing-strategy`.
- **Out-of-scope frameworks adopted as authority.** OWASP ZAP / Burp Suite / Snyk / npm audit / Aikido / 42Crunch are widely used tools; NIST SP 800-115 is a widely cited penetration testing framework; Microsoft SDL provides a security testing track. These are practitioner convention, not anchored authority. The Anthropic `security-guidance` plugin is a usable hook for in-IDE secure-coding reminders (cross-link in pipeline integration) but is not a substitute for a programmed security test portfolio.
- **The human confirms.** Security Officer proposes; the human confirms before any node or release gate is changed.

## Source

★ **Security testing 65% DRE on security defects** — `se-best-practices.pdf` Table 5-6.
★ **Ethical hacking 85% DRE on security defects** — `se-best-practices.pdf` Table 5-6, Table 5-3 entry #26 ("Ethical hacking").
★ **Static analysis for security 25% DRE on security defects** — `se-best-practices.pdf` Table 5-6.
★ **Security tester staffing 1 per 50,000 FP** — `se-best-practices.pdf` Table 5-4.
★ **Cumulative DRE formula and Jones synergy stack** — `se-best-practices.pdf` Tables 5-3, 5-6; defect-removal-efficiency chapter.
★ **Hard-to-remove defect classes (security defects)** — `se-best-practices.pdf` Table 5-6 commentary ("requirements defects, security defects, and defects in test materials are the most difficult to eliminate").

Complement (practitioner convention, not anchored authority): NIST SP 800-115 (penetration testing); OWASP ZAP; Burp Suite; Snyk; npm audit; Microsoft SDL security testing; Anthropic `security-guidance` plugin (PreToolUse(Edit|Write|MultiEdit) regex hook for 9 unsafe-code patterns).
