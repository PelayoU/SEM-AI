---
category: spec
id: spec-075-hard-role-jurisdiction
parent: "[[feature-075-hard-role-jurisdiction]]"
artifacts:
  - "[[.claude/commands/role.md]]"
  - "[[.claude/role-scope.json]]"
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Spec 075 — Hard role-jurisdiction

> Authored via `po-spec-gherkin`. One Feature per spec. Includes the role-scope.json ↔ CLAUDE.md table consistency check.

## Stories covered

- `[[story-075-A-declare-active-role]]` — AC-A1
- `[[story-075-B-deny-without-active-role]]` — AC-B1
- `[[story-075-C-deny-wrong-role-for-path]]` — AC-C1
- `[[story-075-D-allow-correct-role]]` — AC-D1, AC-D2

## Acceptance Criteria

- **AC-A1:** `/role architect` writes `.claude/.active-role`=`architect`; an invalid name is rejected listing the 5 valid roles.
- **AC-B1:** With the marker absent, any in-scope governed substrate write is denied with a "run `/role`" reason.
- **AC-C1:** With `.active-role`=developer, an Edit to a `CLAUDE.md`/ADR (architect) path is denied with a jurisdiction reason.
- **AC-D1:** With `.active-role`=architect, a governed write in architect scope passes silently.
- **AC-D2:** `.claude/role-scope.json` and the CLAUDE.md § Role jurisdiction table are content-consistent.

## Gherkin spec

```gherkin
Feature: Hard role-jurisdiction via mandatory active-role marker

  In order to make "each role does its own" structural, not audited
  As the SEM-IA framework
  I want substrate writes gated on a mandatory active-role marker and a role->path map

  Scenario: AC-A1 — declare role
    When the human runs "/role architect"
    Then .claude/.active-role contains "architect"

  Scenario: AC-B1 — no role, no write
    Given .claude/.active-role is absent
    When a governed substrate Edit is attempted
    Then the gate denies it asking to run /role

  Scenario: AC-C1 — wrong role for path
    Given .claude/.active-role is "developer"
    When an Edit targets CLAUDE.md (architect jurisdiction)
    Then the gate denies it naming the owning role

  Scenario: AC-D1 — correct role allowed
    Given .claude/.active-role is "architect"
    And a node governs ".claude/agents/architect.md"
    When an Edit targets ".claude/agents/architect.md"
    Then the gate allows it

  Scenario: AC-D2 — map/table consistency
    Given .claude/role-scope.json and CLAUDE.md Role-jurisdiction table
    Then every role's path set agrees between the two
```

## Notes

**Realized (Phase E, 2026-05-15):** AC-A1 ✅ `/role` ceremony writes the marker; invalid name rejected. AC-B1 ✅ no marker → all substrate writes denied. AC-C1 ✅ developer→CLAUDE.md denied (role-scope). AC-D1 ✅ architect→architect-scoped governed path allowed. AC-D2 ✅ role-scope.json keys ↔ CLAUDE.md jurisdiction table both cover all 5 roles, consistent.

## Source

- Skill: `po-spec-gherkin`. Cucumber `gherkin-reference.pdf` pp. 1–9; GISF `gisf-life-cycle.pdf` slide 54.
