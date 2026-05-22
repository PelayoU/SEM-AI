---
title: Fagan formal inspections
anchor: |
  Michael Fagan — *Design and Code Inspections to Reduce Errors in Program
  Development* (IBM Systems Journal, 1976; revised in *IBM SJ* 1986);
  Capers Jones — *Software Engineering Best Practices* (2009), Section 5.
referenced_by:
  - .claude/agents/qa.md § Discipline / 3. Inspections programme
  - .claude/agents/qa.md § Discipline / 5. Defect-removal efficiency
  - .claude/agents/security-officer.md § Discipline / 2. Requirements & inspection
status: written
---

# Fagan formal inspections

## Method

A **formal inspection** is the highest-yield defect-removal activity in software engineering: per-pass DRE of **65–85 %** on the artifact under review, with peaks of **88 %** for well-trained teams on code, requirements, and design artifacts. The same five preconditions apply across all artifact types — *requirements · architecture · design · code · test plan · test cases · user documentation*.

**The five preconditions** (Fagan, 1976 — non-negotiable; missing any one drops the activity from "formal inspection" to "code walkthrough" with DRE around 35 %):

1. **A moderator** — owns the meeting, keeps it on the artifact, blocks personal critique.
2. **A recorder** — captures every defect with location, severity, originator-of-defect (NOT inspectee), and category.
3. **Preparation time** — inspectors read the artifact privately before the meeting; ratio guideline is ~125 lines of code per hour of prep, ~5 pages of design per hour, ~2 pages of requirements per hour.
4. **A defect log** — the recorder's output; lives in the QA program's repository (engine: `create_node type=inspection`), used for DRE projection and for `qa-measurements`.
5. **No appraisal use** — defect data **must not** flow into individual performance appraisals or punitive structures. Mixing them collapses honest reporting and kills the program within a quarter.

**Roles per session** — 3–6 participants (modal 4), distinct from the inspectee author:

- **Moderator** (1) — usually QA.
- **Author / inspectee** (1) — the artifact's owner; answers questions, does not defend.
- **Reader** (1) — paraphrases the artifact one logical chunk at a time.
- **Reviewers** (1–3) — domain experts; raise defects; the security-officer participates as a security reviewer in security inspections.

Sessions are **timeboxed**: 60–120 minutes; longer runs drop reviewer attention. If the artifact is too large for one session, break into chunks and inspect each in its own meeting.

**Output per session** — recorded as one `inspection` node via the engine MCP:

```python
mcp__sem_ai_engine__create_node(
  type="inspection",
  parent="<spec|story|adr|feature|release id>",
  slug="<artifact-slug>-fagan-N",
  acting_role="qa",
  body="""\
## Summary
One-line: what we inspected, when, who, headline DRE.

## Inspection-class
Fagan (requirements / architecture / design / code / test-plan / test-case / user-doc / security-review)

## Participants
4 participants: moderator (qa-X), reader (developer-Y), reviewer (architect-Z), reviewer (security-officer-W).

## DRE-percent-per-pass
~78%

## Defects-found-by-severity
- sev-1: 1
- sev-2: 3
- sev-3: 5
- sev-4: 2
- sev-5: 1

## Action-items
- defects converted to `defect` nodes via create_node type=defect parent=<spec> found_by=inspection
- rework + re-inspection scheduled (re-inspection DRE ~70%)
"""
)
```

Each defect found in the inspection becomes a `defect` node with `found_by: inspection` and `acting_role: qa` (QA owns inspection-found defects; Developer owns static-analysis / unit-test-found defects in the shared `defect` ledger — search first to avoid duplicates).

## Generic criteria recap (mirror of agent.md)

- The five Fagan preconditions enforced — moderator · recorder · prep time · defect log · no appraisal use.
- 3–6 participants per session (modal 4).
- All inspectable artifact types covered — requirements ≈ 85 % DRE · architecture/design 80–85 % · code ≈ 85 % · test plan 80–83 % · user docs ≈ 70 %.
- Static analysis layered on supported languages (complementary, not substitute).
- Defect-origin → optimal-method mapping respected.

## Inspectable artifact types and DRE figures

| Artifact | Typical DRE | Lower bound | Practice notes |
|---|---|---|---|
| Requirements | 85 % | 78 % | Highest-leverage point; requirements defects flow downstream into code. |
| Architecture | 85 % | 75 % | The 7 fundamental topics each checked; security topic dispatches to Security Officer. |
| Design | 80 % | 70 % | UML / Zachman / pattern-language; design notation primary + secondary. |
| Code | 85 % | 70 % | Pre-test code inspection; static analysis runs *before* (filters trivial defects). |
| Test plan | 83 % | 70 % | Test plan inspection prevents defects that "we'll catch in test" cannot reach. |
| Test cases | 80 % | 65 % | Test cases sometimes have higher error density than the code; canonical inspection. |
| User docs | 70 % | 60 % | Defects: out-of-date references, missing safety warnings, wrong examples. |
| Security inspection | 70 % | 60 % | Security-officer-led; subset of requirements / code / config inspections with a security checklist. |

(Numerical thresholds in this instance: `instance/thresholds.yaml::fagan` for participant range; per-artifact DRE values are calibration data, not enforcement.)

## Bibliographic anchors

- **Fagan original** — M. E. Fagan, *Design and Code Inspections to Reduce Errors in Program Development*, IBM Systems Journal 15(3), 1976, pp. 182–211 (the five preconditions, the 3–6 participant range, the appraisal-data prohibition).
- **Fagan extended** — M. E. Fagan, *Advances in Software Inspections*, IBM Systems Journal 25(3-4), 1986 (re-inspection DRE, defect-density correlation with project schedule).
- **DRE per artifact type** — Jones, *Software Engineering Best Practices* (2009), Section 5, Tables 5-3 / 5-6 (DRE values per artifact and per removal method).
- **Static analysis layered** — Jones, ibid., Section 5, pp. 130–135 (static analysis as pre-inspection filter).
- **Security inspection** — Jones, ibid., Section 38, *Best practices for software security analysis*, practice 3 (formal security inspections of requirements and specs).
- **Appraisal-data prohibition** — Jones, ibid., Section 5, p. 137 (defect data ≠ appraisal data — categorical).

## Worked example

> *"The PM and Architect drafted spec-042 for the payment-flow feature. Run a Fagan inspection."*

**Pre-inspection (≈ 1 day):**

- Moderator (QA) circulates the spec + the role-specific checklist to 3 reviewers (Architect, Developer, Security Officer) 3 days before the meeting.
- Each reviewer privately reads + annotates the spec — ~45 minutes for a 5-page spec, per the Fagan ratio.
- Reviewers email annotations to the moderator the morning of the meeting.

**Inspection (90 min):**

- Reader (Developer) paraphrases the spec scenario by scenario.
- Reviewers raise defects: scenario 3 missing `When` for the rate-limited path → defect sev-3, origin requirements. Scenario 5 silently drops failed-3DS path → defect sev-2 origin requirements. Security AC missing — Security Officer flags as sev-2 (security-content present in body, security section empty). 3 minor wording defects sev-4.
- Recorder logs each: defect-id, location (scenario number, line), severity, origin.
- Moderator timeboxes any debate; resolutions are *"author rewrites or surfaces a question; we do not re-author in the meeting"*.

**Post-inspection (~30 min):**

- Moderator publishes the `inspection` node with summary + per-severity defect counts + per-pass DRE estimate.
- Each defect becomes a `defect` node parented to spec-042 via `create_node type=defect found_by=inspection acting_role=qa`.
- Re-inspection scheduled after author rework (~70 % DRE on the rework, per Jones BP #5).
- The DRE figure feeds `qa-defect-removal-efficiency` projection on the parent release.

**Outcome:** 8 defects removed at the requirements layer at a cost of ~6 person-hours total inspection effort. The same 8 defects in production would have averaged 100–1 000× higher repair cost.

## Common pitfalls (extends agent.md)

- **"Code review" called "Fagan inspection".** Without the 5 preconditions, the 65–85 % DRE figure does **not** apply; the activity averages ~35 % and consumes the same engineer-hours. Audit by name: moderator named? recorder named? prep time logged? defect log persistent? appraisal-prohibition documented? — five yeses or it is not a Fagan inspection.
- **Defect data used for appraisals.** Within a quarter, defect reporting collapses to cosmetic; the program is dead with no public death certificate. Categorical: never.
- **Skipping requirements / architecture / design inspections.** Testing does not reach requirements defects. The optimal removal method for requirements defects is a *formal requirements inspection* (Jones Table 5-6, ~85 % DRE).
- **Inspecting only code.** Test plan inspection (~83 % DRE) and test-case inspection (~80 % DRE) are systematically skipped despite their leverage; test cases sometimes have higher error density than the code.
- **Static analysis as substitute.** SAST is complementary to inspection (~87 % DRE on coding defects, mostly disjoint from inspection's set); running both raises cumulative DRE significantly. Running only SAST caps cumulative DRE at the SAST band.
- **Participant count outside the 3–6 range.** Two participants → not enough perspective. Seven+ → attention drops and the moderator cannot keep the meeting on the artifact. Modal 4 is the empirical sweet spot.
- **Skipping re-inspection.** After defects are repaired, ~7 % of repairs are bad fixes that introduce new defects (Jones BP #5). Re-inspection catches them with ~70 % DRE; skipping it lets bad fixes ship.
- **Inspecting security separately from the artifact inspection.** A security-officer-led security inspection works **inside** the artifact's Fagan inspection as a reviewer with a security checklist — not as a separate session that duplicates the prep time. The DRE figures compose; the duplicated effort does not.
