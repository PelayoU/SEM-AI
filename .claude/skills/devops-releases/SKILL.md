---
name: devops-releases
description: "Plan and execute software releases (bug-fix releases, feature releases, new versions) avoiding Capers Jones's 16 named release anti-patterns (long wait times, no e-mail support, fee for bug reports, forced upgrades, arbitrary file format changes, dropped features, etc.) and applying the 11 theoretical-but-correct best practices (e-mail bug reporting with 48h SLA, ≤5 min phone wait, self-installing bug repairs, no forced re-installs, free format conversion, etc.). Use whenever planning a release, designing release cadence, deciding what to do with old versions when shipping new, handling fee-vs-free for support, configuring file-format migration, or auditing release practice against industry empirics. Triggers include phrases like 'release plan', 'how often should we release', 'support old versions', 'force upgrade', 'file format migration', 'release cadence', 'why are users angry', 'sunset old version', 'release notes', 'fee for support'."
---

# devops-releases

## Purpose

Once software is installed, three forces meet: bugs appear, business / law requires new features, and vendors want to monetize new versions. Most release practice in the industry has accumulated *anti*-patterns: long wait times, no e-mail support, forced upgrades, arbitrary file-format changes. Capers Jones names 16 explicitly. The 11 theoretical best practices are "more theoretical than real as of 2009" — yet they are the auditable spec for what a good release program should do. This skill lets DevOps plan releases that avoid the named anti-patterns and approach the empirically-correct practice baseline.

## When this skill applies

- A bug-fix or feature release is being planned.
- A new major version is shipping and the team must decide how to handle old versions.
- Customers report friction (long waits, surprise upgrades, file incompatibility) and the cause is a release-practice anti-pattern.
- Fee-vs-free decisions for support are open.
- File-format changes are being considered between versions.
- A release cadence is being defined for the project.

## Formal criteria

A release plan is acceptable only if all of the following hold:

1. **None of the 16 anti-patterns present.** Audit the plan against each:
   1. Long wait times for telephone support.
   2. Telephone support inaccessible to users with hearing problems.
   3. No e-mail support or very limited support.
   4. Incompetent first-tier support.
   5. Charging fees for support (especially for reporting bugs).
   6. Inadequate methods of reporting bugs to vendors.
   7. Poor response times to reported bugs.
   8. Inadequate repairs of reported bugs.
   9. Stopping support of older versions prematurely.
   10. Forcing customers to buy new versions.
   11. Changing file formats arbitrarily.
   12. Refusing to allow customers to continue using old versions.
   13. Warranties covering only media replacement.
   14. One-sided agreements favouring only the vendor.
   15. Quirky new releases that cannot install over old releases.
   16. Quirky new releases dropping useful features OR breaking competitive software.
2. **The 11 theoretical-but-correct practices applied**:
   1. Known bugs and problems displayed on a vendor web site.
   2. Bug reports / assistance requests handled by e-mail with ≤48h response.
   3. Phone support reachable in ≤5 minutes.
   4. ≥60% of problems resolved by the first tier of phone support.
   5. Hearing-impaired access provided.
   6. Fee-based support excludes vendor-caused bug reports.
   7. Bug repairs are self-installing.
   8. New versions install without manual uninstalls of prior versions.
   9. File-format changes include free conversion to / from older formats.
   10. Support of applications with thousands of users not arbitrarily withdrawn.
   11. No forced annual upgrade unless the customer wants new features.
3. **Release cadence chosen explicitly** — Roadmap-Based / Timeboxed / Regular / Continuous Deployment / Feature Management-Based. Cadence + the deployment strategy (cross-link `devops-deployment`) compose the release model.
4. **Old-version support policy stated** — applications with thousands of users do not get support arbitrarily withdrawn; the support timeline is announced in advance.
5. **File-format migration plan when applicable** — format changes carry free conversion in both directions; the old format remains readable.
6. **Coordinated with customer-support staffing** — release volume drives support volume; the release plan checks that the customer-support staffing model (cross-link `devops-customer-support`) is still valid.
7. **Coordinated with configuration control + post-release change** — each release is a new baseline; CRs against the release flow through `product-manager-change-control` + `devops-post-release-change`.
8. **Release security gate present for in-scope classes** — for Internet-facing / privileged-data / financial / medical / military / classified applications, the release node's `## Security gate` section is filled by `security-officer-security-program` (SRD pass, security test pass, ethical-hacker pass for in-scope, SAST clean, no open Sev-1). Security Officer holds independent release-stop authority on security grounds parallel to QA's quality-grounds veto (modern hybrid model). Sub-1k-FP non-Internet-facing applications may mark the section `N/A — reason`.

## How you proceed

1. **Walk the 16 anti-patterns** against the proposed release plan. Any present is flagged and rewritten.
2. **Walk the 11 theoretical practices.** For each, either *included* (with concrete owner + SLA) or *deferred* (with reason).
3. **Pick the release cadence and deployment strategy** (cross-link `devops-deployment`).
4. **Set the old-version support policy.** Announce the support window in advance; do not surprise customers with sunset.
5. **Plan file-format migration** if applicable. Bidirectional, free, in-place upgrade.
6. **Update the customer-support model** (cross-link `devops-customer-support`) to account for the new release's expected ticket volume.
7. **Define the release security gate.** For Internet-facing / privileged-data / financial / medical / military / classified applications, dispatch `security-officer-security-program` to author the gate criteria for the release node's `## Security gate` section (per `node-templates`): SRD pass, security test pass (~65% DRE), ethical-hacker pass for in-scope (~85% DRE), SAST clean on security rules, no open Sev-1 vulns. **The gate carries Security Officer's independent release-stop authority, operating in parallel with SQA's quality-grounds veto under this framework's modern hybrid model** (cross-link `qa-sqa-program`).
8. **Publish release notes** including known bugs (per practice 1).
9. **Measure post-release.** Support volume by category, defect-discovery rate, MTTF; feed back to Product Manager / QA / next-release planning.

## Pitfalls to avoid

- **Mainframe-vs-PC dichotomy.** Mainframe vendors of expensive packages (>$100k) do better customer support than low-end PC / Mac vendors. Knowing where the project sits in this spectrum sets the support expectation; aspiring to mainframe-style support on a consumer-priced product is unrealistic.
- **Sunset by silence.** Withdrawing support without announcement = anti-pattern 9. Always announce in advance.
- **File-format change as marketing.** Format changes for arbitrary reasons anger customers and trigger support volume; only change format when functionally required, and with free bidirectional conversion.
- **Forced upgrade as revenue.** Anti-pattern 10. Customer outrage compounds; over time it drives churn faster than the upgrade revenue compensates.
- **Anti-pattern presence treated as "industry standard."** Many anti-patterns are common, but their commonness does not make them right.
- **No release notes with known bugs.** Practice 1 is to publish known bugs proactively. Customers find them anyway; publishing first turns a surprise into a known limitation.
- **Phone-only support model.** Anti-patterns 2 + 3. E-mail with a 48h SLA + an accessible channel for the hearing-impaired are practice 2 + practice 5.
- **Release ships without security gate evaluation.** For in-scope classes (Internet-facing / privileged-data / financial / medical / military / classified), the release node's `## Security gate` section is mandatory. A release without security gate criteria (or with `N/A` not justified) ships blind to security defects. Security Officer's independent release-stop authority operates in parallel to QA's quality-grounds veto; the gate makes that authority operational, not advisory.
