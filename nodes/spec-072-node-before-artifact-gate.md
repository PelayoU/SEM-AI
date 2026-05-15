---
category: spec
id: spec-072-node-before-artifact-gate
parent: "[[feature-072-node-before-artifact-gate]]"
artifacts:
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
  - "[[.claude/settings.json]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Spec 072 — Node-before-artifact gate

> Authored via `po-spec-gherkin`. One Feature per spec. Realized ACs are recorded verbatim from the Phase-E verification run.

## Stories covered

- `[[story-072-A-deny-ungoverned-substrate-write]]` — AC-A1
- `[[story-072-B-deny-bash-side-channel-write]]` — AC-B1, AC-B2
- `[[story-072-C-allow-governed-and-ignore-nonsubstrate]]` — AC-C1, AC-C2, AC-C3

## Acceptance Criteria

- **AC-A1:** A `Write`/`Edit` to an in-scope substrate path with no node referencing it in `artifacts:` is denied; the reason names the rule, the path, and the only remedy.
- **AC-B1:** A Bash redirect/`tee`/`sed -i`/`cp`/`mv` into ungoverned substrate is denied.
- **AC-B2:** The denial holds under `--dangerously-skip-permissions` / bypass permission mode.
- **AC-C1:** A write to a substrate path referenced by ≥1 node (any `status:`) passes.
- **AC-C2:** Writes under `nodes/`, `sessions/`, `bibliography/` always pass.
- **AC-C3:** Writes under `/tmp`, `.git`, `.obsidian/`, outside the repo always pass.

## Gherkin spec

```gherkin
Feature: Node-before-artifact hard gate

  In order to make traceability structural instead of a forgettable virtue
  As the SEM-IA framework
  I want substrate writes blocked unless a node governs the path

  Scenario: AC-A1 — ungoverned substrate Write denied
    Given no node references ".claude/skills/dummy-probe/SKILL.md" in artifacts:
    When a Write targets ".claude/skills/dummy-probe/SKILL.md"
    Then the PreToolUse hook denies it with the node-before-artifact reason

  Scenario: AC-B1 — Bash side-channel write denied
    Given no node references ".claude/probe.txt"
    When Bash runs 'echo x > .claude/probe.txt'
    Then the hook denies it

  Scenario: AC-B2 — denial not overridable
    Given permission mode is bypass / --dangerously-skip-permissions
    When the AC-A1 Write is retried
    Then it is still denied

  Scenario: AC-C1 — governed substrate write allowed
    Given a node references ".claude/agents/architect.md" in artifacts:
    When an Edit targets ".claude/agents/architect.md"
    Then the hook allows it silently

  Scenario: AC-C2 — node write allowed
    When a Write targets "nodes/feature-999-x.md"
    Then the hook allows it (gate-ignored)

  Scenario: AC-C3 — non-substrate ignored
    When Bash runs 'echo x > /tmp/probe'
    Then the hook allows it
```

## Notes

**Realized (Phase E, 2026-05-15, direct hook invocation):** AC-A1 ✅ ungoverned Write denied. AC-B1 ✅ Bash `>`/`sed -i`/`cp`/`mv`/`tee` into ungoverned substrate denied. AC-B2 ✅ deny is unconditional (no permission-mode code path in the hook; Claude Code applies PreToolUse `deny` over bypass). AC-C1 ✅ governed path allowed silently. AC-C2 ✅ `nodes/` allowed. AC-C3 ✅ `/tmp` allowed. Performance: ~0.03 s/invocation (5 runs). Harness note: gate enforces from the next session (Claude Code loads hooks at session start); logic verified deterministically by direct invocation.

## Source

- Skill: `po-spec-gherkin`. Cucumber `gherkin-reference.pdf` pp. 1–9; GISF `gisf-life-cycle.pdf` slide 54 (Examples → AC).
