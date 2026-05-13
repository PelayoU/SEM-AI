---
name: architect-reuse-certification
description: "Establish the certification gate that decides whether a candidate reusable artifact is safe to admit into the project's reuse library, using Capers Jones's certification preconditions (zero-defect target, formal taxonomy, standard interfaces, test cases + scripts, defect repository, source identification, change records, distribution records, warranties). Use whenever someone proposes adopting a reusable component (internal or external, library or framework or SOA service or ERP module), or wants to audit the current reuse library for unsafe artifacts. Triggers include phrases like 'is this component safe to reuse', 'can we adopt this library', 'reuse certification', 'how do we vet reusable code', 'open-source reuse risk', 'is our reuse library hygiene OK', 'should we trust this dependency'."
---

# architect-reuse-certification

## Purpose

Without certification, reuse propagates defects, security holes, and license risk across every application that consumes the reused artifact. Jones (BP #27, p. 101) frames it bluntly: "reuse of code, specifications, and other material is a two-edged sword". The favourable edge (best ROI of any known technology) only materializes when the reused material approaches zero defects; the unfavourable edge (worst negative ROI in the industry) materializes whenever buggy or compromised material is admitted. This skill operationalizes the gate: what a candidate must satisfy before entering the reuse library and how the library guards against drift after entry.

## When this skill applies

- A new reusable artifact is proposed for the library (internal contribution, third-party library, OSS dependency, SOA service, ERP module).
- An existing reuse library is being audited for hygiene.
- A defect found in production is traced to a reused artifact and the question is whether the certification gate was correctly applied.
- A regulatory or security requirement forces reuse-library review (medical devices, defense, finance).
- A reuse vehicle vendor (SOA provider, library publisher) claims certification and the claim must be evaluated.

## Formal criteria

A reusable artifact is admissible only if all of the following hold:

1. **Substantially bug-free, demonstrably** *(Jones BP #27, p. 101)* — the artifact has empirical evidence of approaching zero defects: inspection results, static-analysis clean reports, test execution history with defect counts, third-party certification certificates where available. Trust-by-reputation is insufficient.
2. **Free of viruses, spyware, keystroke loggers, back doors** *(Jones BP #27, p. 102)* — security validation is a separate precondition from functional defect-freeness. Jones is explicit that "reusable material, or at least source code, may have security flaws or even deliberate 'back doors' inserted by hackers, who then offer the materials as a temptation to the unwary".
3. **Eleven supporting practices present** *(Jones BP #27, pp. 102–103)* — admission also requires:
   1. Formal taxonomy of reusable objects and their purposes.
   2. Standard interface definitions for linking reusable objects.
   3. User information / HELP text for all reusable objects.
   4. Test cases and test scripts associated with all reusable objects.
   5. Repository of all bug reports against reusable objects.
   6. Identification of the sources of reusable objects.
   7. Records of all changes made to reusable objects.
   8. Records of all variations of reusable objects.
   9. Records of all distributions of reusable objects (for recall capability).
   10. Charging method for non-free reusable material.
   11. Warranties for reusable material against copyright and patent violations.
4. **Central certification authority exists** *(Jones BP #27, p. 102)* — admission is governed by an authority, not the consuming team's individual judgement. Jones proposes a model: industry-funded nonprofit, analogous to Underwriters Laboratories or Consumer Reports. Within an organization, this maps to an internal certification function (often the Architect role with QA support).
5. **Post-admission monitoring** — admission is not a one-shot. The reuse library tracks every distribution so a defect or vulnerability discovered post-admission triggers recall to every consuming application. Without recall capability the gate is illusory.
6. **Industry-funded model awareness** — for third-party reuse, prefer vehicles with auditable certification trails (cryptographic signatures, published defect history, security advisories) over vehicles with marketing-only claims.

## How you proceed

1. **Receive the admission request.** Capture: source, version, license, claimed functionality, claimed certification status. No artifact enters the library by silent inclusion.
2. **Run the defect-freeness check** *(BP #27, p. 101)*. Inspection log present? Static analysis clean? Test results with defect counts visible? If any is missing, the artifact is *not* admissible regardless of how attractive its functionality is.
3. **Run the security check** *(BP #27, p. 102)*. Provenance verifiable? Cryptographic signature valid? Known-vulnerability database (CVE-equivalent) checked? "Back door" risk evaluated for low-reputation sources?
4. **Walk the eleven supporting practices** *(BP #27, pp. 102–103)*. Each must be present or explicitly waived with a reason that survives audit. The most commonly missing in practice are: change records, distribution records, and warranties — and missing any of these creates an irreversible problem at first defect discovery.
5. **Record the certification decision in the library catalog.** Admission status, version pinned, dependencies tracked, consuming applications listed. Cross-link to `architect-reusability-strategy` for the library's tracking schema.
6. **Establish the recall mechanism.** Define the trigger (defect discovery, vulnerability disclosure, license change) and the notification path (which consuming applications to alert). Without recall, admission is permanent commitment.
7. **Re-audit on schedule.** Versions update, vulnerabilities are disclosed, licenses change. Schedule annual (or release-boundary) recertification.

## Pitfalls to avoid

- **Trust by reputation.** "It's a popular library / it's used everywhere / it's from a big vendor" is not certification. Jones (p. 101) is explicit: certification must be demonstrable, not assumed.
- **Skipping the security check on third-party code.** Back doors and spyware in reusable code are real (Jones p. 102) and increasing. Provenance + signature + CVE check are not optional.
- **No recall mechanism.** A library without a recall pipeline cannot remediate a defect found post-admission. The first severe defect then has to be patched in every consuming application individually.
- **No change / distribution / warranty records.** These are the practices most commonly skipped and they are the ones that matter when a problem arises. Their absence converts a contained problem into an organization-wide incident.
- **Permanent admission.** Versions drift, vulnerabilities surface, licenses change. Single-admission-forever is the recipe for waking up to a license violation or known CVE in production.
- **"Internal therefore safe."** Internally-built artifacts need the same certification gate as third-party. Internal contributors are not exempt from inspection, static analysis, and test-history requirements.
- **Adopting industry "certification" claims without evidence.** Vendor-claimed certification ranges from rigorous (e.g., DO-178 in avionics) to marketing. Evaluate the underlying evidence.

## Source

- **Best Practice #27 — *Certification of Reusable Materials* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 101–103).** Two-edged-sword framing, central certification authority model (Underwriters-Laboratories-like), 11 supporting-practice inventory, security caveats including deliberate back doors, Table 2-4 economic value of certified reuse on a 10,000-FP application.
- **Cross-reference: ±300% ROI swing and 15 reusable artifact types** — Jones BP #26 (depth in `architect-reusability-strategy`).
- Full traceability: `bibliography/skill-references.md` § `architect-reuse-certification`.
