---
name: devops-releases
description: "Plan and execute software releases (bug-fix releases, feature releases, new versions) avoiding Capers Jones BP #49's 16 named anti-patterns (long wait times, no e-mail support, fee for bug reports, forced upgrades, arbitrary file format changes, dropped features, etc.) and applying the 11 theoretical-but-correct best practices (e-mail bug reporting with 48h SLA, ≤5 min phone wait, self-installing bug repairs, no forced re-installs, free format conversion, etc.). Use whenever planning a release, designing release cadence, deciding what to do with old versions when shipping new, handling fee-vs-free for support, configuring file-format migration, or auditing release practice against industry empirics. Triggers include phrases like 'release plan', 'how often should we release', 'support old versions', 'force upgrade', 'file format migration', 'release cadence', 'why are users angry', 'sunset old version', 'release notes', 'fee for support'."
---

# devops-releases

## Purpose

Jones (BP #49 p. 164) observes that once software is installed, three forces meet: bugs appear, business / law requires new features, and vendors want to monetize new versions. Most release practice in the industry has accumulated *anti*-patterns: long wait times, no e-mail support, forced upgrades, arbitrary file-format changes. Jones names 16 explicitly. The 11 theoretical best practices are "more theoretical than real as of 2009" — yet they are the auditable spec for what a good release program should do. This skill lets DevOps plan releases that avoid the named anti-patterns and approach the empirically-correct practice baseline.

## When this skill applies

- A bug-fix or feature release is being planned.
- A new major version is shipping and the team must decide how to handle old versions.
- Customers report friction (long waits, surprise upgrades, file incompatibility) and the cause is release-practice anti-pattern.
- Fee-vs-free decisions for support are open.
- File format changes are being considered between versions.
- A release cadence is being defined for the project.

## Formal criteria

A release plan is acceptable only if all of the following hold:

1. **None of the 16 anti-patterns present** *(Jones BP #49 pp. 164–165)*. Audit the plan against each:
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
2. **11 theoretical-but-correct practices applied** *(Jones BP #49 p. 165)*:
   1. Known bugs and problems displayed on a vendor web site.
   2. Bug reports / assistance requests handled by e-mail with ≤48h response.
   3. Phone support reachable in ≤5 minutes.
   4. ≥60% of problems resolved by first tier of phone support.
   5. Hearing-impaired access provided.
   6. Fee-based support excludes vendor-caused bug reports.
   7. Bug repairs are self-installing.
   8. New versions install without manual uninstalls of prior versions.
   9. File-format changes include free conversion to / from older formats.
   10. Support of applications with thousands of users not arbitrarily withdrawn.
   11. No forced annual upgrade unless customer wants new features.
3. **Release cadence chosen explicitly** *(GISF `gisf-pipeline-devops.pdf` slide 34)* — Roadmap-Based / Timeboxed / Regular / Continuous Deployment / Feature Management-Based. Cadence + the deployment strategy (cross-link `devops-deployment`) compose the release model.
4. **Old-version support policy stated** *(BP #49 anti-pattern 9 + practice 10)* — applications with thousands of users do not get support arbitrarily withdrawn; support timeline is announced in advance.
5. **File-format migration plan when applicable** *(BP #49 anti-pattern 11 + practice 9)* — format changes carry free conversion in both directions; old format remains readable.
6. **Coordinated with customer support staffing** *(BP #49 + BP #45)* — release volume drives support volume; the release plan checks the customer-support staffing model (cross-link `devops-customer-support`) is still valid.
7. **Coordinated with configuration control + post-release change** — each release is a new baseline; CRs against the release flow through `product-manager-change-control` + `devops-post-release-change`.

## How you proceed

1. **Walk the 16 anti-patterns** against the proposed release plan. Any present is flagged and rewritten.
2. **Walk the 11 theoretical practices.** For each, either *included* (with concrete owner + SLA) or *deferred* (with reason).
3. **Pick the release cadence and deployment strategy** (cross-link `devops-deployment`).
4. **Set the old-version support policy.** Announce the support window in advance; do not surprise customers with sunset.
5. **Plan file-format migration** if applicable. Bidirectional, free, in-place upgrade.
6. **Update customer-support model** (cross-link `devops-customer-support`) to account for the new release's expected ticket volume.
7. **Publish release notes** including known bugs (per practice 1).
8. **Measure post-release.** Support volume by category, defect-discovery rate, MTTF; feed back to Product Manager / QA / next release planning.

## Pitfalls to avoid

- **Mainframe-vs-PC dichotomy** *(BP #49 p. 165)* — Jones observes mainframe vendors of expensive packages (>$100k) do better customer support than low-end PC / Mac vendors. Knowing where the project sits in this spectrum sets the support expectation; aspiring to mainframe-style support on a consumer-priced product is unrealistic.
- **Sunset by silence.** Withdrawing support without announcement = anti-pattern 9. Always announce in advance.
- **File-format change as marketing.** Format changes for arbitrary reasons (BP #49 anti-pattern 11) anger customers and trigger support volume; only change format when functionally required, and with free bidirectional conversion.
- **Forced upgrade as revenue.** Anti-pattern 10. Customer outrage compounds; over time it drives churn faster than the upgrade revenue compensates.
- **Anti-pattern presence treated as "industry standard."** Many anti-patterns are common (Jones p. 165) but their commonness does not make them right.
- **No release notes with known bugs.** Practice 1 is to publish known bugs proactively. Customers find them anyway; publishing first turns a surprise into a known limitation.
- **Phone-only support model.** Anti-patterns 2 + 3. E-mail with 48h SLA + accessible-channel option for hearing-impaired are practice 2 + practice 5.

## Source

- **Best Practice #49 — *Updates and Releases of Software Applications* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 164–165).** Three release-driving forces (bugs / business + law / vendor monetization); 16 named anti-patterns; 11 theoretical-but-correct best practices; mainframe-vs-PC support dichotomy.
- **Best Practice #45 — *Customer Support* (Jones 2010, pp. 157–158)** — release volume drives support volume; staffing baseline 1/10kFP or 1/150 customers; cross-link `devops-customer-support`.
- **GISF UC3M `gisf-pipeline-devops.pdf`** — Release strategies (slide 34): Roadmap-Based / Timeboxed / Regular / Continuous Deployment / Feature Management-Based.
- **Cross-references**: `devops-deployment` (deployment strategy pairs with release strategy); `devops-customer-support` (support model checked at each release); `product-manager-change-control` (CRs per release); `devops-post-release-change` (post-release renovation).
- Out-of-bibliography (convention pointers only): semantic versioning (semver), release notes conventions, EULA standards.
- Full traceability: `bibliography/skill-references.md` § `devops-releases`.
