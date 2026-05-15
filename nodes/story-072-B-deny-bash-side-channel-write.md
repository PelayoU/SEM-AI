---
category: story
id: story-072-B-deny-bash-side-channel-write
parent: "[[feature-072-node-before-artifact-gate]]"
artifacts:
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
status: draft
created: 2026-05-15
updated: 2026-05-15
---

# Story 072-B — Deny Bash side-channel writes into substrate

> Acceptance criteria trace to the spec sibling as `AC-B1`, `AC-B2`, …

## Cohn statement (GISF slide 124)

As **the framework**,
I want **Bash write verbs into substrate (`>`, `>>`, `tee`, `sed -i`, `cp`, `mv`, `dd of=`, heredoc, …) subject to the same node-before-artifact check as `Write`/`Edit`**,
so that **the gate is not trivially bypassed by shelling out (Jones BP #33 practice 2: side-channel edits are forbidden)**.

## Conditions of Satisfaction (GISF slide 125)

- `bash -c 'echo x > .claude/probe.txt'` with no governing node is denied.
- `sed -i` / `cp` / `mv` / `tee` into ungoverned substrate are denied.
- Writes outside substrate (e.g. `/tmp`) are not affected.

## INVEST self-check (GISF slide 128)

- **I** ✅ · **N** ✅ (verb list negotiable) · **V** ✅ (closes the obvious bypass) · **E** ✅ · **S** ✅ · **T** ✅ observable denial.

## Source

- Skill: `po-feature-decomposition`. Cohn format GISF slide 124; INVEST slide 128.
