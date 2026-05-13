---
type: spec
id: spec-044-glosario-publico
title: "Spec Gherkin para feature-044: Glosario público (cobertura + linkeo en README)"
parent: feature-044-glosario-publico
related-stories:
  - story-044-A
  - story-044-B
related-feature: feature-044-glosario-publico
related-capability: cap-10-articulacion-publica
also-relates-to:
  - feature-041-readme-onboarding
related-adrs: []
depends-on: []
dimensions-affected: [product, usability, business]
status: ready-for-implementation
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
ac-count: 6
---

```gherkin
Feature: feature-044-glosario-publico — Glosario público
  Como newcomer leyendo el repo SEM-IA
  Quiero glosario con cobertura mínima de jerga + linkeo en README primera aparición
  Para resolver términos sin leer todos los docs y mantener contexto al leer README

  Background:
    Given README.md existe
    And el glosario existe (paths a definir en WA feature-build posterior)

  # Scenarios de story-044-A: Glosario con ≥20 términos en ≥4 categorías
  Scenario: AC-A1 — Cobertura ≥20 términos
    Given newcomer cuenta entradas del glosario
    When inspecciona
    Then encuentra ≥20 términos canónicos del framework
    And cada uno con su propia entrada (no agregados)

  Scenario: AC-A2 — Agrupado en ≥4 categorías
    Given glosario completo
    When newcomer ve estructura
    Then encuentra al menos 4 categorías:
      | categoría                            |
      | Términos del frontmatter             |
      | Términos del WA lifecycle            |
      | Términos de roles + dimensiones      |
      | Términos de slash commands           |
    And cada categoría con sus términos agrupados

  Scenario: AC-A3 — Cada entrada con definición + ejemplo + cross-link
    Given newcomer abre una entrada (ej. "WA")
    When inspecciona el contenido
    Then incluye:
      | elemento                                                |
      | Definición concisa (1-3 frases)                          |
      | Ejemplo de uso (referencia a WA real archivado, ej. wa-2026-05-12-002.md) |
      | Cross-link al doc canónico (ej. CLAUDE.md raíz sección "Estructura de un WA") |

  # Scenarios de story-044-B: README enlaza glosario en primera aparición
  Scenario: AC-B1 — Primera aparición linkeada
    Given newcomer lee README
    When encuentra primera aparición de un término (ej. "WA")
    Then el término incluye link en formato markdown `[WA](path/to/glossary#wa)`
    And el link funciona (resuelve a la entrada correspondiente)

  Scenario: AC-B2 — Apariciones subsecuentes NO requieren link
    Given el término "WA" ya apareció con link en línea 50
    When aparece nuevamente en línea 200
    Then NO requiere link (evita ruido visual + repetición innecesaria)

  Scenario: AC-B3 — Sección "Términos" al final
    Given newcomer llega al final del README
    When busca acceso rápido al glosario
    Then encuentra sección "Términos" o equivalente con link al glosario completo
```

## Notas

- **Verificable vía**: cuando glosario se materialice (WA feature-build posterior), inspección del archivo + grep sobre README de patrones `[<término>](<glossary-path>)`.
- **No materializado en WA-005**: spec usable como blueprint cuando se construya.

## Historia del refactor

Consolida spec-044-A/B en Gherkin único. Refactor 2026-05-13.
