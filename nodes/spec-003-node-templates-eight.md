---
category: spec
id: spec-003-node-templates-eight
parent: "[[feature-003-node-templates-eight]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 003 — Eight node templates aligned to backbone

> Parent: [[feature-003-node-templates-eight]].

## Stories covered

- [[story-003-A-template-per-backbone-category]] — AC-A1, AC-A2
- [[story-003-B-templater-integration]] — AC-B1

## Acceptance Criteria

- **AC-A1:** Exactly 8 templates exist under `_obsidian/templates/` (vision, goal, capability, feature, story, spec, adr, session).
- **AC-A2:** Each template carries category-specific required frontmatter + body sections.
- **AC-B1:** Templater is enabled and populates `created:`, `updated:`, `id:` at node-creation time.

## Gherkin spec

```gherkin
Feature: Node templates aligned to backbone categories

  Scenario: AC-A1 — Eight templates present
    Given the directory "_obsidian/templates/"
    When I list its files
    Then I see exactly 8 markdown files corresponding to backbone categories

  Scenario: AC-A2 — Template carries required sections
    Given a template "_obsidian/templates/<category>.md"
    When I open it
    Then required frontmatter fields and body sections for that category are present

  Scenario: AC-B1 — Templater populates frontmatter on creation
    Given Templater is enabled in ".obsidian/community-plugins.json"
    When I create a new node from a template
    Then "created:", "updated:", and "id:" are populated automatically
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-003-node-templates-eight]].
