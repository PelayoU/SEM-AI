---
category: spec
id: spec-<NNN>-<slug>
parent: "[[feature-NNN-slug]]"
status: draft
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
also-relates-to: []
dimensions-affected: []
---

# Spec <NNN> — <Título de la feature>

> Convención canónica Adzic (literal): **1 archivo Gherkin por feature**, no por story. Los Scenarios dentro agrupan AC de todas las stories de la feature, con comentarios separadores `# Scenarios de story-NNN-X` para trazabilidad.

## Stories cubiertas

> Lista de wikilinks a las stories hijas + qué AC alimenta cada una. Cada story debe contribuir al menos un AC.

- `[[story-NNN-A-slug]]` — AC-A1, AC-A2, AC-A3
- `[[story-NNN-B-slug]]` — AC-B1, AC-B2
- `[[story-NNN-C-slug]]` — AC-C1

## Spec Gherkin

> Contrato formal. Cada Scenario es un AC numerado con prefijo de letra de su story origen + trazabilidad inline `(story-NNN-X)`. Los tests deben cubrir con `// @ac-coverage: AC-XN`.

~~~gherkin
Feature: feature-<NNN>-<slug> — <Título legible de la feature>

  As <role>
  I want <action>
  So that <benefit>

  Background:
    Given <contexto común a todos los Scenarios — opcional>
    And <más setup compartido>

  # Scenarios de story-<NNN>-A: <título corto de la story A>
  Scenario: AC-A1 — <título corto del AC> (story-<NNN>-A)
    Given <contexto>
    When <acción>
    Then <outcome esperado>
    And <más asserts si aplica>

  Scenario: AC-A2 — <título corto> (story-<NNN>-A)
    Given ...
    When ...
    Then ...

  # Scenarios de story-<NNN>-B: <título corto de la story B>
  Scenario: AC-B1 — <título corto> (story-<NNN>-B)
    Given ...
    When ...
    Then ...
~~~

## Notas

> Decisiones tomadas durante la escritura del spec, edge cases discutidos, AC descartados con justificación (Adzic: *"The biggest mistake is to specify too much upfront."*).
