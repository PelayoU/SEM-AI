---
name: security-officer-requirements-and-inspection
description: "Run Security Requirements Deployment (SRD) — Capers Jones's QFD-analogue method for security requirements — and conduct formal security inspections of requirements and specifications. Engages a top-gun security expert with development team and user representatives; covers physical security plus advanced code-hardening methods (capability logic, permission restrictions, E language, Google Caja); produces a security plan, security test stages, and an ethical-hacker engagement plan. The security inspection role layers on the QA inspection programme. Use when running SRD for a new application or major release, when running a security inspection of requirements or specs, or when shifting security defect-removal left from testing to inspection. Triggers include phrases like 'SRD', 'security requirements deployment', 'security inspection of requirements', 'shift security left', 'QFD for security'."
---

# security-officer-requirements-and-inspection

## Purpose

Security defects whose origin is requirements cannot be removed by testing alone — requirements defects flow downstream into design, code, and production unchanged. Capers Jones prescribes Security Requirements Deployment (SRD) as the QFD-analogue method for security requirements, plus formal security inspections of requirements and specifications. Together these shift security defect-removal left, from the ~65% DRE of security testing to the higher cumulative DRE of inspection + SRD + testing.

## When this skill applies

- A new application or major release is in requirements-elicitation phase and SRD has not been run.
- A security inspection of requirements or specifications is needed (formal, with a security-focused checklist).
- The team is debugging "security defects we keep finding in test" — the defect-origin analysis points to requirements, not code.
- The 5 Fagan preconditions for a security inspection are being validated (cross-link `qa-inspections-program`).
- The release security gate (cross-link `security-officer-security-program`) requires an SRD pass and a security-requirements inspection pass.

## Formal criteria

An SRD pass and a security inspection are acceptable only if all of the following hold:

1. **SRD engages a top-gun security expert with development team and user representatives.** Without the expert, SRD collapses to a self-assessment that misses the requirements-stage defects Jones names.
2. **SRD covers physical security and advanced code-hardening.** Physical security of teams, devices, source repositories; advanced code hardening (capability logic, permission restrictions, E language, Google Caja). Skipping the code-hardening half collapses SRD to the perimeter-focused anti-pattern.
3. **SRD produces a security plan.** The plan names: trusted vs untrusted boundaries; authorization model; threat catalogue applied (cross-link `security-officer-threats-and-defenses`); security test stages with coverage targets; ethical-hacker engagement plan for in-scope classes; secure-coding standards for the implementation team.
4. **Security inspections of requirements scheduled before requirements are frozen.** Inspection participants include security expert + development reviewer + user representative; security-focused checklist applied alongside generic requirements-inspection checklist (cross-link `qa-inspections-program`).
5. **Five Fagan preconditions met per security inspection.** Moderator, recorder, adequate preparation, defect log, no-appraisal-use. The security inspection layers on the QA inspection programme; it does not replace it.
6. **Security-specific defect-origin tracked.** Defects found in inspection are tagged by origin (requirement / spec / threat-model gap / authorization-model gap / configuration / dependency). Feeds `qa-measurements` defects-by-origin tracking and `security-officer-testing-and-static-analysis` shift-left analysis.
7. **Ethical-hacker plan is part of SRD output.** For in-scope classes (Internet-facing, privileged-data, safety-critical), the engagement is named in SRD; engagement scheduled before release security gate.
8. **Coordinated with PM requirements discovery.** SRD is layered on `product-manager-requirements-discovery` — runs alongside JAD / QFD / prototypes / legacy mining as the security-specific elicitation track.
9. **Coordinated with QA inspection programme.** Security inspection participates in the QA inspection calendar (cross-link `qa-inspections-program`); it does not run as a parallel ungated track.

## How you proceed

1. **Confirm trigger.** New application / major release with Internet-facing or privileged-data class → SRD mandatory. Below the trigger → SRD-lite (security-relevant requirements walked by Security Officer, no top-gun expert engagement).
2. **Engage the top-gun expert.** External expert preferred for independence. For internal teams that have the depth, the expert is the Security Officer themself; surface the choice and its independence implication.
3. **Hold the SRD sessions.** Joint sessions with development team + user representatives + expert; agenda covers: threat catalogue applied to this application; physical security; trust boundaries; authorization model; code-hardening choices (language, sandboxing, capability semantics); security test stages; ethical-hacker engagement.
4. **Produce the security plan.** A node-graph attached document (via `set_related` on the relevant `vision` or `capability` or `release` node), summarising the SRD outcomes. The plan is the input to architecture work (`security-officer-architecture`) and testing work (`security-officer-testing-and-static-analysis`).
5. **Schedule security inspections of requirements.** Before requirements are frozen; participants per Fagan preconditions; checklist combines generic requirements inspection (`qa-inspections-program`) with the security-specific list from SRD.
6. **Run the inspection.** Defects logged by origin; defect data not used for individual appraisals (cross-link `qa-inspections-program`); follow-up corrective actions tracked.
7. **Contribute security AC to specs (dispatch from PM).** When PM is authoring a spec for a feature with a security dimension, PM dispatches you to produce the `## Security AC` section content of the spec node. Derive AC-S1, AC-S2, … from the SRD output; each AC carries a Given/When/Then in the Gherkin block, tagged `@security`. Return the section to PM; PM integrates and signs.
8. **Schedule security inspections of specs.** Once specs include security-relevant Acceptance Criteria (`AC-S*`), inspect them with the security-focused checklist before the spec moves to `ready-for-implementation`.
9. **Coordinate with the release security gate.** SRD pass and security-requirements inspection pass are gate criteria (cross-link `security-officer-security-program`).
10. **Refresh at major release boundaries.** SRD is not one-shot — threats evolve, requirements evolve, the plan is refreshed. Mark stale plans as superseded.

## Pitfalls

- **SRD reduced to a self-assessment.** Without the top-gun expert, SRD becomes a tick-box exercise that misses the requirements-stage defects it exists to catch.
- **SRD covering only physical security.** The code-hardening half (capability logic, permission restrictions, language choice) is co-equal; perimeter-only SRD reproduces the post-deployment focus anti-pattern.
- **Security inspection of requirements skipped because "we'll catch it in test".** Requirements defects in security cost orders of magnitude more downstream; the only viable removal method for requirements defects is formal inspection (cross-link `qa-inspections-program`).
- **Security inspection running as parallel ungated track.** Not coordinated with the QA inspection calendar produces fragmentation. Layer on `qa-inspections-program`; do not run separately.
- **Defect-origin tracking absent.** Without origin tracking, the team cannot shift security defects left; the same class of defect resurfaces release after release.
- **Ethical-hacker engagement deferred to "if budget allows".** For in-scope classes, the engagement is a release security gate criterion, not an option.
- **Out-of-scope frameworks adopted as authority.** Microsoft SDL Security Requirements activity, NIST SP 800-30 (risk assessment), STRIDE / DREAD threat modeling, OWASP ASVS are widely used; they are practitioner convention, not anchored authority. Cite Jones (Section 38, Chapter 7 SRD discussion) as the audited anchor.
- **The human confirms.** Security Officer proposes; the human confirms before SRD output or inspection schedule changes.

## Source

★ **Security Requirements Deployment (SRD) method** — `se-best-practices.pdf` Chapter 7 ~lines 22012–22044.
★ **Engagement of top-gun security expert** — `se-best-practices.pdf` ~line 22016.
★ **Physical security + code-hardening dual coverage; capability logic, permission restrictions, E, Caja** — `se-best-practices.pdf` Chapter 7 ~lines 22017–22035.
★ **Formal security inspections of requirements and specifications** — `se-best-practices.pdf` Section 38 best-practice #3; defect-removal activity Section 38 ~line 6729.
★ **Ethical-hacker engagement** — `se-best-practices.pdf` ~line 22036; Table 5-3 entry #26.
★ **Requirements inspection as only viable removal method for requirements defects** — `se-best-practices.pdf` Table 5-6 (requirements inspection ~85% DRE on requirements defects vs ~0% via testing).

Complement (practitioner convention, not anchored authority): Microsoft SDL Security Requirements activity; NIST SP 800-30 risk assessment; STRIDE / DREAD threat modeling; OWASP ASVS.
