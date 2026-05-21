---
name: security-officer-security-program
description: "Stand up or audit the software security programme for a project, applying Capers Jones's eight security best practices (Section 38) and the security-specialist role inventory (Table 9-23: rank #7 of 20 specialists, assignment scope 50,000 FP, 70% defect prevention impact, 20% defect removal impact, defect potential 7.0). Use whenever planning the security programme for a new application, deciding whether the team has a real security function or only perimeter tools, scoping the eight Jones practices (engineer training, formal security plan, security inspections of requirements/specs, physical security, home-office security, high-security languages, automated static analysis on new and legacy code), staffing the security specialist headcount (~1 per 1,000 FP, ~5 per 100,000 FP), defining the release security gate, or mapping the programme to ISO 17799 / ISO/IEC 10181. Triggers include phrases like 'set up security', 'is our security real', 'who has release veto on security', 'how many security specialists do we need', 'security programme', 'security gate', 'ISO 17799', 'eight security practices'."
---

# security-officer-security-program

## Purpose

Most "security" in industry is reactive perimeter defence — firewalls, antivirus, antispyware — without an underlying programme. Capers Jones documents this gap and prescribes eight specific practices for a software security programme that addresses security at architecture, requirements, design, and code stages, not only at deployment. This skill stands up or audits that programme against the empirically successful pattern, with the independence imperative made explicit because dependent Security cannot deliver objective risk reporting under schedule pressure.

## When this skill applies

- A new application above ~1,000 FP starts and no security programme exists, and the application will connect to the Internet or to other computers.
- The team has "security" but its activities suggest only perimeter / runtime tooling (AV / AS / WAF) and no architecture-stage or requirements-stage security work.
- A release is being decided and the question is who holds the authority to recommend against shipping on security grounds.
- An audit (regulatory, customer, certification) requires demonstrating that a software security programme exists.
- The security specialist headcount is being negotiated and the empirical staffing ratios are needed.
- The Internet-facing or privileged-data nature of the application makes the absence of a security programme a risk on its own.

## Formal criteria

A security programme is acceptable only if all of the following hold:

1. **Independence is structural** — Security personnel can recommend against release on security grounds and the recommendation is overturned only by a defined escalation path (e.g., division VP / corporate president / CISO equivalent). Security reporting into a development VP without escalation path is structurally compromised, analogous to dependent SQA.
2. **All eight Jones practices accounted for** — for each practice the programme states either *included* (with named owner) or *not applicable* (with one-line reason):
   1. **Improve the undergraduate and professional training of software engineers in security topics.** Generalist training is not deep in security; the programme either funds in-team security training or staffs the gap with specialists.
   2. **For every application that will connect to the Internet or to other computers, develop a formal security plan.** Internet/connectivity is the trigger; sizing is not the only trigger.
   3. **Perform security inspections of requirements and specifications.** Formal inspections analogous to QA inspections, with security-focused checklist. Cross-link `security-officer-requirements-and-inspection`.
   4. **Develop topnotch physical security for development teams.** Source-code repository, build artifacts, design documents protected against physical theft.
   5. **Develop topnotch security for home offices and portable equipment.** Laptops, mobile devices, and home networks of staff are part of the threat surface.
   6. **Utilize high-security programming languages such as E.** Capability-based languages (E, Google Caja) reduce structural attack surface. Cross-link `security-officer-architecture` (Principle of Least Authority, capability logic).
   7. **Utilize automated static analysis of code to find potential security vulnerabilities.** SAST for new code; integrated into the development pipeline. Cross-link `security-officer-testing-and-static-analysis`.
   8. **Utilize static analysis on legacy applications that are to be updated.** Legacy code carries undiscovered vulnerabilities; SAST is the practical removal lever before enhancement. Cross-link `devops-post-release-change`.
3. **Specialist headcount sized against Jones ratios** — ~1 security specialist per 1,000 FP for typical projects; ~5 per 100,000 FP at scale. Below the ratio is "token security" that cannot review deliverables.
4. **Defect-prevention impact stated** — Security specialists carry a 70% defect-prevention impact and 20% defect-removal impact (Table 9-23). The programme states which prevention activities the specialist owns (training, SRD, security inspections, secure-coding standards, threat catalogue) versus which removal activities are run by Testing / QA / static-analysis tools.
5. **Release security gate defined and documented before the first release decision is needed** — the gate criteria (SRD review pass, security test pass, ethical-hacker pass for high-risk classes, static-analysis clean on security rules, no open Sev-1 vulns) are written down. The escalation path for a gate failure is named.
6. **Standards baseline declared** — ISO 17799 and/or ISO/IEC 10181 named as the working standards for security framework alignment; conformance documented for regulated industries.
7. **Coordinated with related programmes** — security inspections coordinated with `qa-inspections-program`; security testing forms coordinated with `qa-testing-strategy`; release gate coordinated with `devops-releases` and `product-manager-project-planning`; ADR security-attributes coordinated with `architect-architecture-design`.

## How you proceed

1. **Confirm trigger.** Internet/connectivity-facing application of any size, or application above ~1,000 FP, or privileged-data / safety-critical class → security programme required. Below the trigger → recommend a lite version with named owner (often the Architect) and an explicit deferral; do not staff a full programme.
2. **Diagnose the current state.** Of the eight Jones practices, which are present? Which are absent? Which are mis-staffed (training as a tick-box, SRD missing, static analysis on new code but not legacy, etc.)? The dominant failure mode is post-deployment focus only (firewall / antivirus / antispyware) with no architecture-stage or requirements-stage security work.
3. **Decide independence and reporting line.** If a CISO / VP Security exists, security reports there; otherwise to an executive above the development organization, with named escalation for release recommendations against shipping. Document the line before staffing.
4. **Size specialist headcount.** Apply ~1 per 1,000 FP for typical projects, ~5 per 100,000 FP at scale. For Internet-facing or privileged-data applications, do not go below 1 specialist regardless of size.
5. **Walk the eight Jones practices.** For each, set *included* with named owner and cadence, or *not applicable* with one-line reason. Sub-1k-FP non-Internet-facing applications can mark practice 2 (formal security plan) *not applicable* with reason; Internet-facing of any size cannot.
6. **Define the release security gate.** Criteria (SRD pass, security test pass, ethical-hacker pass for high-risk, static-analysis clean, no Sev-1 open vulns) + escalation for failure. Coordinate with `devops-releases` so the gate is enforced as part of the release flow.
7. **Map to standards.** ISO 17799 and ISO/IEC 10181 alignment for regulated industries; document conformance.
8. **Stand up the recurring obligations.** SRD for each new application or major release (cross-link `security-officer-requirements-and-inspection`); threat-catalogue refresh per release boundary (cross-link `security-officer-threats-and-defenses`); security inspections scheduled in the QA inspection calendar; static analysis integrated in the deployment pipeline (cross-link `devops-deployment`).
9. **Report defect-removal participation.** Security-specific DRE figures (security testing 65%, ethical hacking 85%, static analysis ~25% on security defects) feed `qa-defect-removal-efficiency` projection; surface to QA at release boundaries.

## Pitfalls

- **Security as a perimeter problem only.** Firewalls + antivirus + antispyware are necessary but never sufficient. A programme without architecture-stage and requirements-stage security work is incomplete by Jones's eight practices.
- **Practice 2 (formal security plan) treated as paperwork.** The plan is the input to SRD; without it, the SRD has nothing to deploy against. Practice 2 is the foundation of practices 3, 6, 7.
- **Practice 8 (static analysis on legacy) skipped because "legacy is being replaced soon".** Replacement is multi-year; legacy carries undiscovered vulnerabilities during the entire window. SAST on legacy is part of `devops-post-release-change` and `devops-legacy-retirement` work, not deferred to retirement.
- **Independent reporting line absent.** Security under development VP with no escalation path collapses under release pressure. Independence is a structural property, not a stylistic preference.
- **Specialist headcount below 1 per 1,000 FP for Internet-facing applications.** Token staffing produces token coverage. The 70% defect-prevention impact requires the specialist to actually do prevention work (training, SRD, inspections, secure-coding standards), which requires time.
- **Release gate defined after the first release crisis.** By then the appeal path is negotiated under pressure and the gate is undermined. Define before the first release decision is needed.
- **Out-of-scope frameworks adopted as authority.** OWASP (Top 10 / ASVS / SAMM), NIST SP 800-53, Microsoft SDL, BSIMM are widely used in industry but are not part of this framework's audited sources. Cite Jones + ISO 17799 / ISO/IEC 10181 as anchored authority; reference OWASP / NIST / Microsoft SDL / BSIMM as practitioner convention with explicit caveat.
- **The human confirms.** Security Officer proposes; the formal release-stop authority on security grounds is a human decision.

## Source

★ **Eight security best practices** — `se-best-practices.pdf` Section 38 "Best Practices for Software Security Analysis and Control".
★ **Security specialist role definition** — `se-best-practices.pdf` Table 9-23 (rank #7/20, assignment scope 50,000 FP, 70% defect prevention impact, 20% defect removal impact, defect potential 7.0); Table 2-3 staffing ratios (~1 per 1,000 FP, ~5 per 100,000 FP).
★ **Independence implication and training gap** — `se-best-practices.pdf` Section 38; specialist role text on training currency.
★ **Standards baseline** — `se-best-practices.pdf` Section 38: ISO 17799, ISO/IEC 10181 Security Frameworks; also DHS Software Assurance, FBI InfraGuard, Center for Internet Security as named partners.

Complement (practitioner convention, not anchored authority): OWASP ASVS / SAMM; NIST SP 800-53; Microsoft SDL; BSIMM. Cited in `## Pitfalls` as "do not adopt as authority".
