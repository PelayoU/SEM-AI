---
name: security-officer-architecture
description: "Analyse and contribute the security-attributes section of an ADR — the 7th fundamental architecture topic. The Architect authors the ADR; the Security Officer supplies the security-attributes analysis through dispatch. Applies Capers Jones's framing of security as one of seven fundamental architecture topics (silence on it is the #1 architectural defect), plus Principle of Least Authority, capability logic, language-level hardening (E, Google Caja), whitelisting / blacklisting of interfacing applications, and boundary control. Use whenever an ADR's security attributes need analysis, an architecture choice has security implications, an authorization model is being chosen (ACL / RBAC / ABAC / capability-based), a reusable component's security posture must be analysed, or an existing architecture is being audited for security coverage. Triggers include phrases like '7th topic', 'security attributes of an ADR', 'capability logic', 'Principle of Least Authority', 'is this architecture safe', 'authorization model'."
---

# security-officer-architecture

## Purpose

Capers Jones names security as one of seven fundamental topics of software architecture, alongside structure, data, interfaces, decomposition, linkage, and performance. Silence on any of the seven is the dominant architectural defect; silence on security specifically is increasingly costly as adversaries become more sophisticated. The Security Officer does not author ADRs (the Architect does), but contributes the security-attributes section under author-dispatch so that the ADR's 7th topic is analysed by the role with the required depth.

## When this skill applies

- An Architect is drafting or auditing an ADR and the 7th fundamental topic (security attributes) needs analysis.
- An architecture choice (style, decomposition, interface model, deployment topology) has security implications the Architect cannot fully derive.
- An authorization model (ACL vs capability vs RBAC vs ABAC) is being chosen and security needs to validate.
- A reusable component or third-party dependency is being considered and its security posture must be analysed.
- An existing architecture is being audited and the security-attributes section is missing or thin.

## Formal criteria

A security-attributes contribution to an ADR is acceptable only if all of the following hold:

1. **The 7th topic is addressed, not skipped or marked TBD without follow-on.** Jones is explicit: silence on a fundamental topic is the #1 architectural defect. *N/A — reason* is acceptable only with the reason; bare TBD is not.
2. **Threat surface stated.** The contribution names what the architecture exposes (Internet endpoints, intra-application interfaces, data at rest, data in motion, build pipeline, deployment surface, supply chain dependencies).
3. **Principle of Least Authority applied.** Each component is described in terms of the least permission set it needs; broad permission grants (root / administrator / "all of session owner's permissions") are flagged as risk.
4. **Authorization model named.** ACL / RBAC / ABAC / capability-based / hybrid — with rationale. ACL-only authorization is flagged as anti-pattern for applications where untrusted code can run in the session context (because a virus inherits session-owner permissions and can damage anything the user could).
5. **Language and platform hardening considered.** Where the architecture allows, high-security languages (E, Google Caja) or sandboxing platforms are considered; if rejected, the rationale is recorded.
6. **Whitelisting / blacklisting of interfacing applications declared.** For each external interface, the model is whitelist (default-deny) or blacklist (default-allow); default-allow is flagged as risk and requires justification.
7. **Boundary control specified.** Subroutines / functions / API endpoints that receive external input have boundary-check requirements stated; the absence of boundary checking on a known-external interface is an anti-pattern (Jones Section 42).
8. **Performance and quality overlap acknowledged.** The contribution names where security overlaps performance (DoS surface) and quality (error-handling routines as attack vectors), and coordinates with `architect-performance-analysis` and `qa-defect-removal-efficiency`.
9. **Coordinated with the threat catalogue.** The 17+ named vectors from `security-officer-threats-and-defenses` are checked against the architecture; vectors that apply are listed with the architectural defence.
10. **The Architect remains the author of the ADR.** The Security Officer's contribution is dispatched back as content for the 7th topic section; the Architect integrates and signs. Authority remains with the Architect.

## How you proceed

1. **Receive dispatch from the Architect.** The Architect is authoring or auditing an ADR; you are dispatched to produce the security-attributes section. Read the ADR draft, the parent capability or goal, and any related architecture decisions via `get_node` / `ancestors_of`.
2. **Name the threat surface.** Walk the architecture and list every surface where untrusted input or code can enter: Internet endpoints, intra-application interfaces, file uploads, message queues, deserialization points, dependency surface, build pipeline, deployment surface.
3. **Apply Principle of Least Authority to each component.** What is the minimum permission each component needs? Where does the architecture over-grant?
4. **Choose / validate the authorization model.** ACL is sufficient only when no untrusted code runs in the session context; capability-based is the default for high-risk classes. RBAC / ABAC fit intermediate cases.
5. **Consider language / platform hardening.** Is the implementation language amenable to memory-safety, capability semantics, sandboxing? Are dependencies vetted? Cross-link `architect-reuse-certification`.
6. **Declare whitelist / blacklist per interface.** Default-deny for external; default-allow only with explicit justification.
7. **Specify boundary-control requirements.** Every external-input subroutine carries a stated boundary-check obligation; absence is documented as a known gap (and feeds risk register `product-manager-risk-analysis` category 9 security flaws).
8. **Cross-check the threat catalogue.** For each vector in `security-officer-threats-and-defenses` that applies to this architecture, name the defence in the ADR's security-attributes section.
9. **Acknowledge overlap with performance and quality.** Coordinate with `architect-performance-analysis` (DoS surface, error-handling) and `qa-defect-removal-efficiency` (error-handling defects as attack vectors).
10. **Return the section to the Architect.** Dispatched-back content; the Architect integrates into the ADR and signs. You do not author the ADR yourself.

## Pitfalls

- **Treating security attributes as a paragraph at the end.** The 7th topic deserves the same depth as the other six; a single sentence is not analysis.
- **ACL as default authorization model.** ACLs cannot distinguish identities of processes running in the user's session; a virus inherits session-owner permissions. Use capability-based for high-risk classes.
- **Default-allow on external interfaces.** Whitelisting is the security-conscious default; default-allow is the anti-pattern.
- **No boundary checking on external-input subroutines.** Listed by Jones as one of the canonical anti-patterns. Boundary checks belong in the architecture-level contract, not deferred to implementation.
- **Hardening rejected by reflex without analysis.** "We can't use E / Caja / sandboxing" without a recorded rationale is incomplete; rejection is a legitimate outcome only with reasoning.
- **Performance / quality / security treated as disjoint.** A DoS attack is a performance issue. A high-severity bug drops performance to zero. Error-handling routines are major attack vectors. Coordinate, don't silo.
- **Security Officer authors the ADR.** That is the Architect's authorship. Security contributes the section; the Architect integrates and signs.
- **Out-of-scope frameworks adopted as authority.** STRIDE / DREAD threat modeling, NIST SP 800-30 risk assessment, Microsoft SDL secure-design principles, OWASP ASVS are widely cited but are not part of this framework's audited sources. Cite Jones's 7-topic framing; reference STRIDE / NIST / MS SDL / OWASP as practitioner convention.
- **The human confirms.** Security Officer proposes; the Architect signs the ADR; the human confirms before the node changes.

## Source

★ **Seven fundamental architecture topics including security** — `se-best-practices.pdf` architecture chapter, around lines 22289–22301.
★ **Security as architectural concern, post-deployment focus anti-pattern** — `se-best-practices.pdf` Section 38 + Section 42 lines ~7137–7152.
★ **Principle of Least Authority, capability logic, protected classes of objects** — `se-best-practices.pdf` Section 42 lines ~7169–7170, 7289–7295; Section 38 SRD discussion ~line 22027.
★ **High-security languages: E, Google Caja** — `se-best-practices.pdf` Section 38 ~line 22027.
★ **Whitelisting / blacklisting interfacing applications** — `se-best-practices.pdf` Section 38 ~line 6807.
★ **Boundary control / boundary management** — `se-best-practices.pdf` Section 42 ~lines 7144, 7167–7177.
★ **ACL anti-pattern** — `se-best-practices.pdf` Section 42 ~lines 7282–7288.

Complement (practitioner convention, not anchored authority): STRIDE / DREAD threat modeling; NIST SP 800-30 risk assessment; Microsoft SDL secure-design principles; OWASP ASVS.
