---
name: security-officer-threats-and-defenses
description: "Build the threat catalogue for an application — applying Capers Jones's enumeration of 17+ attack vectors (Section 42) with the corresponding architectural and operational defences, plus the seven Jones-named anti-patterns (global path names, no boundary checking, ACL-only authorization, untrusted executable attachments, unrestricted Java/JS/ActiveX, browser-stored passwords, silent privilege elevation). Use whenever cataloguing threats for a new application, refreshing the threat catalogue at a release boundary, mapping vectors to architectural defences (cross-link `security-officer-architecture`), or auditing an application against the named anti-patterns. Triggers include phrases like 'threat catalogue', 'attack vectors', 'what threats apply', 'is this configuration safe', 'defence against X', 'configuration anti-patterns'."
---

# security-officer-threats-and-defenses

## Purpose

Threats evolve; defences must enumerate and map to architecture and configuration. Jones catalogues 17+ named attack vectors and seven explicit anti-patterns; this skill builds the project's threat catalogue from that enumeration, cross-references each vector to the architectural and operational defence, and refreshes the catalogue at release boundaries. The catalogue is the input to `security-officer-architecture` (defences become section content of ADRs) and to `security-officer-testing-and-static-analysis` (vectors become security test cases).

## When this skill applies

- A new application starts and a threat catalogue is needed as input to `security-officer-architecture` and `security-officer-testing-and-static-analysis`.
- An existing threat catalogue is being refreshed at a release boundary (threats evolve; the catalogue stales).
- The architecture is being audited against the seven Jones-named anti-patterns.
- A specific configuration / dependency / runtime decision needs a threat-vector check.
- A new threat class emerges (industry-wide CVE class, novel attack technique) and needs to be folded into the catalogue.

## Formal criteria

A threat catalogue is acceptable only if all of the following hold:

1. **The 17+ Jones-named vectors are walked and tagged.** For each vector, the catalogue states *applies* (with named defence) or *not applicable* (with one-line reason):
   - Hackers (individual and organised)
   - Viruses (polymorphic)
   - Spyware / Adware
   - Denial of service (DoS) attacks
   - Worms
   - Trojan horses
   - Botnets / "zombie computers"
   - Browser hijackers
   - Back doors (error-handling routines, buffer overruns)
   - Phishing
   - Email-based attacks
   - Cookie poisoning
   - Cyberextortion
   - Cyberstalking
   - Smart card hijacking
   - Electromagnetic pulse (EMP)
   - Keystroke loggers
2. **The seven Jones-named anti-patterns are absent from the architecture and configuration, or each occurrence is explicitly justified:**
   1. **Global items / Global Name Space / Global path names** (e.g., `C:/directory/file`, URLs with fixed IP) — fragile to environment change; broad attack target.
   2. **Subroutines without boundary checking** on external input — buffer-overrun avenue (Section 42).
   3. **Static authorization (ACLs) without runtime identity verification** — virus inherits session-owner permissions.
   4. **Accepting untrusted executable attachments** without sandboxing.
   5. **Running Java / JavaScript / ActiveX without caution** — capability boundaries needed.
   6. **Saving passwords in browsers** without compensating control.
   7. **Allowing applications to request elevated privileges without query / consent.**
3. **Vector-to-defence mapping documented.** Each *applies* vector is paired with the architectural defence (cross-link `security-officer-architecture`: capability logic, Principle of Least Authority, whitelisting / blacklisting, boundary control), the operational defence (cross-link `devops-configuration-control`: signed artifacts, vulnerability scans), or the testing defence (cross-link `security-officer-testing-and-static-analysis`).
4. **Refresh cadence stated.** Minimum at every release boundary; out-of-cycle refresh when a novel industry-wide attack class emerges. Stale catalogues are diagnostic of post-deployment focus anti-pattern.
5. **Configuration controls named.** For each *applies* vector, the configuration controls that mitigate it are listed and cross-linked to `devops-configuration-control` for enforcement.
6. **Coordinated with the risk register.** Active vectors feed `product-manager-risk-analysis` category 9 (security flaws / vulnerabilities); category 14 (external risks including cyber-extortion); the catalogue and the risk register are mutually consistent.
7. **Coordinated with the ADR security-attributes section.** Vectors marked *applies* must appear in the ADR's 7th topic with the architectural defence (cross-link `security-officer-architecture`).

## How you proceed

1. **Walk the 17-vector Jones enumeration.** For each, tag *applies* (with one-line rationale) or *not applicable* (with one-line rationale). Vectors that apply to the application class are determined by: Internet-facing? privileged-data? user-uploaded content? browser-rendered output? cryptographic operations? email channel? mobile device? Each yes pulls in specific vectors.
2. **Walk the seven Jones-named anti-patterns.** For each, audit the architecture and configuration; record absence (with one-line evidence) or presence with justification. Presence without justification is a defect.
3. **Map each *applies* vector to defence.** Architectural defence (cross-link `security-officer-architecture`); operational defence (cross-link `devops-configuration-control`); testing defence (cross-link `security-officer-testing-and-static-analysis`). Vectors without a defence are open risk and feed `product-manager-risk-analysis`.
4. **Name configuration controls.** For example: vulnerability scanning per release; signed artifacts in the pipeline; secrets management; logging and intrusion detection; firewall rules; antivirus / antispyware at endpoint; backup integrity verification.
5. **Set refresh cadence.** Every release boundary; out-of-cycle when a novel attack class emerges; surfaces in `product-manager-milestone-tracking` as a recurring milestone.
6. **Coordinate with risk register.** Active vectors → category 9 (security flaws / vulnerabilities), category 14 (external including cyber-extortion) in `product-manager-risk-analysis`.
7. **Coordinate with the ADR.** Each *applies* vector appears in the 7th topic of the relevant ADR with the architectural defence; cross-link `security-officer-architecture`.
8. **Coordinate with operations.** Configuration controls integrate with `devops-configuration-control`; vulnerability scanning integrates with `devops-deployment` pipeline.

## Pitfalls

- **Catalogue treated as one-shot inventory.** Threats evolve; catalogues stale fast. Refresh at every release boundary minimum.
- **Anti-pattern audit deferred until a defect surfaces.** The seven anti-patterns are named precisely so they can be caught at architecture / configuration stage, not at production-incident stage.
- **Vector mapped to "we'll handle it in testing".** Testing is one defence layer; relying on testing alone produces post-deployment focus. Architecture and configuration defences shift left.
- **Stale enumeration omitting modern vectors.** Jones's 2009 catalogue covers ~17 vectors; modern catalogues (OWASP Top 10, MITRE ATT&CK, CVE / CWE) extend this. Use the Jones list as the audited baseline and add convention-cited modern vectors with explicit caveat. Do not adopt OWASP / MITRE / CVE as anchored authority.
- **Anti-pattern justification accepted without scrutiny.** "We need globals because legacy code does X" is not a justification; it is a debt note. Either accept the debt explicitly (and surface to risk register) or refactor.
- **Out-of-scope frameworks adopted as authority.** OWASP Top 10, MITRE ATT&CK, CVE / CWE, CIS Controls are widely used in industry and excellent practitioner conventions; they are not part of this framework's audited sources. Cite Jones (Section 42) as anchored authority; cite OWASP / MITRE / CVE / CIS as practitioner convention with caveat.
- **The human confirms.** Security Officer proposes; the human confirms before the catalogue is created or refreshed.

## Source

★ **17+ named attack vectors** — `se-best-practices.pdf` Section 42 "Protection against viruses, spyware, hacking" — full chapter covers hackers, viruses, spyware, DoS, worms, trojans, botnets, browser hijackers, back doors, phishing, email-based, cookie poisoning, cyberextortion, cyberstalking, smart card hijacking, EMP, keystroke loggers.
★ **Seven anti-patterns enumeration** — `se-best-practices.pdf` Section 42 ~lines 7167–7208 (globals; subroutines without boundary checking; ACL-only authorization; untrusted executable attachments; Java/JS/ActiveX without caution; browser-stored passwords; silent privilege elevation).
★ **Configuration controls / defence enumeration** — `se-best-practices.pdf` Section 42 + Section 38 cross-references.
★ **DHS Software Assurance, FBI InfraGuard, Center for Internet Security** — `se-best-practices.pdf` Section 38 ~lines 6819–6820, 7111–7125 as named partners for threat intelligence.

Complement (practitioner convention, not anchored authority): OWASP Top 10; MITRE ATT&CK; CVE / CWE; CIS Controls.
