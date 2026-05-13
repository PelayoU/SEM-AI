---
name: devops-configuration-control
description: "Set up and run software configuration control for the project — keeping track of every change to requirements, specifications, source code, test cases, user documents — using Capers Jones BP #34 with ISO 10007-2003 and IEEE 828-1998 as the standards baseline and the CMM/CMMI key-practice-area framing. Use whenever standing up configuration management on a new project, deciding the tooling, auditing whether the team has 'real' configuration control or informal change tracking, locking master copies, or mapping change traceability across deliverables. Triggers include phrases like 'configuration control', 'configuration management', 'CM', 'master copy', 'lock the baseline', 'ISO 10007', 'IEEE 828', 'CMMI configuration', 'version control vs configuration management', 'how do we track changes'."
---

# devops-configuration-control

## Purpose

Configuration control originated in 1950s U.S. Department of Defense weapons systems and is older than software configuration control (Jones BP #34 p. 119). It is a *mechanical* activity — tracks changes, does not judge them — supported by automation but requiring human-set rules. Without it, change-control (`po-change-control`) has nothing to operate on: there is no baseline to gate against. This skill lets DevOps stand up configuration control to ISO 10007-2003 / IEEE 828-1998 / CMMI standards so every change to every deliverable is uniquely identified, cross-mapped, and locked behind formal update procedures.

## When this skill applies

- A new project is starting and configuration control is unset.
- An audit (regulatory, customer, CMMI assessment) requires demonstrating configuration control practice.
- The team has version control on code but no configuration management on requirements, specs, tests, manuals.
- Master copies are being accidentally edited outside formal change pipeline.
- Cross-deliverable traceability (one change affecting multiple artifacts) is broken.

## Formal criteria

A configuration control program is acceptable only if all of the following hold:

1. **Scope covers all deliverables, not only code** *(Jones BP #34 p. 119)* — requirements, specifications, source code, test cases, user documents are all under configuration control. Code-only configuration management is the typical industry shortfall.
2. **Unique identification for every feature/artifact** *(Jones BP #34 p. 119)* — every controlled item carries a stable identifier so traceability across deliverables can be established.
3. **Cross-deliverable mapping maintained** *(Jones BP #34 p. 119)* — every specific change affecting more than one deliverable is linked to all related deliverables. Without this mapping, a single change goes into code but not the spec / test / manual; the system drifts out of consistency.
4. **Master copies locked** *(Jones BP #34 p. 119)* — the master copy of each deliverable changes only via formal methods with formal validation. Direct side-channel edits are forbidden.
5. **Standards baseline declared** *(Jones BP #34 p. 119)* — ISO 10007-2003 and/or IEEE 828-1998 named as the working standards. CMMI configuration management as one of the key practice areas (CMM Level 2).
6. **Automation present but supervised** *(Jones BP #34 p. 119)* — Jones is explicit: "largely automated, [but] still requires human intervention to be done well." Tool selection is part of the program; tool-only "automated CM" without human oversight misses cross-deliverable mappings.
7. **Coordinated with change control** *(Jones BP #33 + BP #34)* — configuration control tracks the changes; change control (`po-change-control`) decides whether each change is valuable. Both functions present; neither substitutes for the other.

## How you proceed

1. **Inventory deliverables under control.** Requirements, specs, source code, test cases, test scripts, user docs, design documents, build scripts, infrastructure-as-code, configuration files. List explicitly.
2. **Assign unique identifiers** to each controlled item. Stable IDs propagate across deliverables.
3. **Choose the tooling.** Version control (git, mercurial, etc.) is necessary but not sufficient — configuration management adds the cross-deliverable mapping and master-copy locking on top. Common combinations: git for code + Jira/Confluence for requirements + dedicated test management for test cases; or unified ALM platform (Polarion, Jama Connect, etc.). Tool brand is not Jones-anchored authority.
4. **Establish the change pipeline.** Master copies live in the locked repositories; changes flow through formal pull-requests / change-requests, get reviewed, get linked to the originating CR (cross-link `po-change-control`), get merged with full traceability.
5. **Maintain cross-deliverable mapping.** Every CR records which deliverables it touches. Tooling that does this automatically is preferred; manual mapping is brittle but acceptable below ~1,000 FP.
6. **Audit periodically.** Sample CRs and confirm cross-deliverable updates happened. Drift surfaces when the audit finds code changes without spec updates (or vice versa).
7. **Map to standards** for regulated industries. ISO 10007 / IEEE 828 / CMMI key practice area conformance documented.

## Pitfalls to avoid

- **Version control mistaken for configuration management.** Git tracks code changes; configuration management additionally tracks every deliverable cross-referenced. The two are not the same.
- **Code-only CM.** Specs / tests / manuals not under formal CM drift out of consistency with code over time.
- **Manual cross-deliverable mapping above ~1,000 FP.** Volume defeats it. Tooling required at scale.
- **Side-channel edits to master copies.** Defeats the entire lock. Enforce technically (repository permissions) not just by policy.
- **Configuration control judging change value.** Jones (p. 119): out of scope. That is `po-change-control`'s job. Conflating the two collapses both.
- **No coordination with change control.** Configuration tracks; change control decides. Each presupposes the other.
- **Tool brand as authority.** Polarion / Jama / git / SVN are convention; Jones BP #34 + ISO 10007 + IEEE 828 are the anchored authority.

## Source

- **Best Practice #34 — *Configuration Control* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, p. 119).** 1950s DoD weapons-systems origin; mechanical activity supported by automation; scope covers all deliverables (requirements / specs / code / test cases / user docs); unique identification + cross-deliverable mapping + master-copy locking + formal-method updates; ISO 10007-2003 + IEEE 828-1998 standards; CMM/CMMI key practice area; out-of-scope: judging change value (that is change-control, BP #33).
- **Cross-references**: `po-change-control` (BP #33 change-control judges; CM tracks); cross-deliverable update rule for accepted CRs.
- Out-of-bibliography (convention pointers only): ISO 10007-2003 full standard, IEEE 828-1998 full standard, CMMI Configuration Management process area, git / SVN / Polarion / Jama Connect tooling.
- Full traceability: `bibliography/skill-references.md` § `devops-configuration-control`.
