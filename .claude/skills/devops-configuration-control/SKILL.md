---
name: devops-configuration-control
description: "Set up and run software configuration control for the project — keeping track of every change to requirements, specifications, source code, test cases, user documents — using Capers Jones's configuration-control discipline with ISO 10007 and IEEE 828 as the standards baseline and the CMMI key-practice-area framing. Use whenever standing up configuration management on a new project, deciding the tooling, auditing whether the team has 'real' configuration control or informal change tracking, locking master copies, or mapping change traceability across deliverables. Triggers include phrases like 'configuration control', 'configuration management', 'CM', 'master copy', 'lock the baseline', 'ISO 10007', 'IEEE 828', 'CMMI configuration', 'version control vs configuration management', 'how do we track changes'."
---

# devops-configuration-control

## Purpose

Configuration control originated in 1950s U.S. Department of Defense weapons systems and is older than software configuration control. It is a *mechanical* activity — it tracks changes, it does not judge them — supported by automation but requiring human-set rules. Without it, change control (`product-manager-change-control`) has nothing to operate on: there is no baseline to gate against. This skill lets DevOps stand up configuration control to the ISO 10007 / IEEE 828 / CMMI baseline so every change to every deliverable is uniquely identified, cross-mapped, and locked behind formal update procedures.

## When this skill applies

- A new project is starting and configuration control is unset.
- An audit (regulatory, customer, CMMI assessment) requires demonstrating configuration control practice.
- The team has version control on code but no configuration management on requirements, specs, tests, manuals.
- Master copies are being accidentally edited outside the formal change pipeline.
- Cross-deliverable traceability (one change affecting multiple artifacts) is broken.

## Formal criteria

A configuration control program is acceptable only if all of the following hold:

1. **Scope covers all deliverables, not only code** — requirements, specifications, source code, test cases, user documents are all under configuration control. Code-only configuration management is the typical industry shortfall.
2. **Unique identification for every feature/artifact** — every controlled item carries a stable identifier so traceability across deliverables can be established.
3. **Cross-deliverable mapping maintained** — every change affecting more than one deliverable is linked to all related deliverables. Without this mapping, a single change goes into code but not the spec / test / manual; the system drifts out of consistency.
4. **Master copies locked** — the master copy of each deliverable changes only via formal methods with formal validation. Direct side-channel edits are forbidden.
5. **Standards baseline declared** — ISO 10007 and/or IEEE 828 named as the working standards; configuration management as a CMMI key practice area.
6. **Automation present but supervised** — configuration control is largely automated but still requires human intervention to be done well. Tool selection is part of the program; tool-only "automated CM" without human oversight misses cross-deliverable mappings.
7. **Coordinated with change control** — configuration control tracks the changes; change control (`product-manager-change-control`) decides whether each change is valuable. Both functions present; neither substitutes for the other.

## How you proceed

1. **Inventory deliverables under control.** Requirements, specs, source code, test cases, test scripts, user docs, design documents, build scripts, infrastructure-as-code, configuration files. List explicitly.
2. **Assign unique identifiers** to each controlled item. Stable IDs propagate across deliverables.
3. **Choose the tooling.** Version control (git, mercurial, etc.) is necessary but not sufficient — configuration management adds the cross-deliverable mapping and master-copy locking on top. Tool brand is convention, not authority.
4. **Establish the change pipeline.** Master copies live in the locked repositories; changes flow through formal pull-requests / change-requests, get reviewed, get linked to the originating CR (cross-link `product-manager-change-control`), get merged with full traceability.
5. **Maintain cross-deliverable mapping.** Every CR records which deliverables it touches. Tooling that does this automatically is preferred; manual mapping is brittle but acceptable below ~1,000 FP.
6. **Audit periodically.** Sample CRs and confirm cross-deliverable updates happened. Drift surfaces when the audit finds code changes without spec updates (or vice versa).
7. **Map to standards** for regulated industries. ISO 10007 / IEEE 828 / CMMI conformance documented.

## Pitfalls to avoid

- **Version control mistaken for configuration management.** Git tracks code changes; configuration management additionally tracks every deliverable cross-referenced. The two are not the same.
- **Code-only CM.** Specs / tests / manuals not under formal CM drift out of consistency with code over time.
- **Manual cross-deliverable mapping above ~1,000 FP.** Volume defeats it. Tooling required at scale.
- **Side-channel edits to master copies.** Defeats the entire lock. Enforce technically (repository permissions), not just by policy.
- **Configuration control judging change value.** Out of scope — that is `product-manager-change-control`'s job. Conflating the two collapses both.
- **No coordination with change control.** Configuration tracks; change control decides. Each presupposes the other.
- **Signed-artifact policy absent.** For Internet-facing / privileged-data deployments, the configuration-control program includes artifact signing at build, verification at deployment, and a recall mechanism if a vulnerability is disclosed post-admission. Dispatch `security-officer-testing-and-static-analysis` for the policy; cross-link `devops-deployment` for pipeline integration. Unsigned artifacts flowing through the pipeline are one of the named supply-chain attack vectors.
- **Tool brand as authority.** Specific CM tools are convention; the configuration-control discipline plus ISO 10007 / IEEE 828 are the anchored authority.
