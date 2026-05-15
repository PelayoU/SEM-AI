---
category: spec
id: spec-077-portable-gate-scope
parent: "[[feature-077-portable-gate-scope]]"
artifacts:
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
  - "[[.claude/role-scope.json]]"
  - "[[.claude/role-scope.example.json]]"
  - "[[CLAUDE.md]]"
status: draft
created: 2026-05-15
updated: 2026-05-15
---

# Spec 077 — Portable gate scope

> Authored via `po-spec-gherkin`. One Feature per spec. Realized notes appended verbatim from the Phase-D verification run (mirroring spec-072/075).

## Stories covered

- `[[story-077-A-gate-scope-from-role-scope-union]]` — AC-A1, AC-A2
- `[[story-077-B-always-ignore-safety-guard]]` — AC-B1, AC-B2
- `[[story-077-C-claude-md-three-layer-reframe]]` — AC-C2 (consistency)
- `[[story-077-D-consumer-project-example]]` — AC-C1, AC-C2

## Acceptance Criteria

- **AC-A1:** every real substrate path in SEM-AI today that the old gate gated is still gated under the union (13-scenario matrix outcomes unchanged, with the documented probe-path substitution).
- **AC-A2:** the union jq filter excludes the `_comment` scalar (no `Cannot iterate over string` crash).
- **AC-B1:** with `role-scope.json` accidentally listing `nodes/**` under a role, a write to `nodes/x.md` is still allowed (always-ignore guard wins, runs first).
- **AC-B2:** the `/role` ceremony writing `.claude/.active-role` is allowed even though architect's role-scope entry lists it (guard wins → no deadlock).
- **AC-C1:** with a simulated consumer `role-scope.json` (`developer→["src/**"]`): `src/app.ts` + developer + no node → node-before-artifact **deny**; `.claude/agents/architect.md` → **ignored** (not in the consumer union — the imported framework is ungated in a consumer project).
- **AC-C2:** `.claude/role-scope.json` keys ↔ CLAUDE.md § Role jurisdiction table remain consistent, including the newly added `.claude/role-scope.example.json` in the Architect row of both (spec-075 AC-D2 invariant preserved).
- **AC-D1:** the 13-scenario hard-enforcement matrix (spec-072 + spec-075 ACs) yields the same outcomes post-refactor (no observable regression).

## Gherkin spec

```gherkin
Feature: Portable gate scope (role-scope.json union, not hardcoded layout)

  In order to make the gate work on projects other than SEM-IA itself
  As the SEM-IA framework
  I want the gate's scope derived from the project's role-scope.json

  Scenario: AC-A1 — real substrate still gated
    Given SEM-AI's own role-scope.json
    When the 13-scenario matrix is re-run by direct hook invocation
    Then every outcome equals the prior Phase-E result (probe-path substitution noted)

  Scenario: AC-A2 — jq tolerates the _comment scalar
    When is_governed computes the glob union
    Then jq selects only array-valued entries and does not crash

  Scenario: AC-B1 — always-ignore guard wins over a careless config
    Given role-scope.json lists "nodes/**" under developer
    When a Write targets "nodes/x.md"
    Then the gate allows it (always-ignore runs first)

  Scenario: AC-B2 — no /role deadlock
    Given architect's role-scope entry lists ".claude/.active-role"
    When the /role ceremony writes ".claude/.active-role"
    Then the gate allows it

  Scenario: AC-C1 — consumer project: product gated, framework ignored
    Given a consumer role-scope.json with developer -> ["src/**"]
    When developer writes "src/app.ts" with no governing node
    Then the gate denies it (node-before-artifact)
    And a write to ".claude/agents/architect.md" is ignored (not in the consumer union)

  Scenario: AC-C2 — map/table consistency preserved
    Given .claude/role-scope.json and CLAUDE.md Role-jurisdiction table
    Then all 5 roles agree, including .claude/role-scope.example.json in the Architect row

  Scenario: AC-D1 — no observable regression
    Then the spec-072 + spec-075 matrix outcomes are unchanged post-refactor
```

## Notes

Realized verbatim results appended during Phase D. The old `.claude/skills/dummy-probe/SKILL.md` probe (spec-072 AC-A1) no longer matches any role glob → now *ignored*, not *denied*: this is the **named, intended** coverage delta of ADR-013 (not a regression); the node-before-artifact deny is re-verified with `.claude/agents/probe.md` (matches `.claude/agents/**`, ungoverned-by-node).

## Source

- Skill: `po-spec-gherkin`. Cucumber `gherkin-reference.pdf` pp. 1–9; GISF `gisf-life-cycle.pdf` slide 54. Lineage `[[adr-013-gate-scope-is-project-configurable]]`.
