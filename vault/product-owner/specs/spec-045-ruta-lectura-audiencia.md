---
type: spec
id: spec-045-ruta-lectura-audiencia
title: "Spec Gherkin para feature-045: Ruta de lectura por audiencia (progressive disclosure)"
parent: feature-045-ruta-lectura-audiencia
related-stories:
  - story-045-A
  - story-045-B
related-feature: feature-045-ruta-lectura-audiencia
related-capability: cap-10-articulacion-publica
also-relates-to: []
related-adrs: []
depends-on: []
dimensions-affected: [product, usability]
status: ready-for-implementation
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
ac-count: 6
---

```gherkin
Feature: feature-045-ruta-lectura-audiencia — Ruta de lectura por audiencia
  Como newcomer ante README de 65 KB
  Quiero sección "Cómo leer este repo" con ≥3 rutas + completitud mínima por ruta
  Para progressive disclosure efectivo según mi audiencia (técnica / académica / adoptante)

  Background:
    Given README.md existe

  # Scenarios de story-045-A: README incluye 3 rutas por audiencia
  Scenario: AC-A1 — Sección con encabezado visible
    Given newcomer abre README
    When busca guía de lectura
    Then encuentra sección "Cómo leer este repo" o equivalente
    And el encabezado es visible (h2 o h3)

  Scenario: AC-A2 — ≥3 rutas declaradas
    Given newcomer abre la sección
    When inspecciona rutas
    Then encuentra al menos 3:
      | ruta                  | audiencia primaria              |
      | Técnica               | contribuyente / arquitecto      |
      | Académica             | evaluador TFM / GISF            |
      | Adoptante             | ingeniero / equipo adoptando    |

  Scenario: AC-A3 — Cada ruta enumera archivos en orden
    Given newcomer elige ruta (ej. académica)
    When inspecciona el contenido
    Then ve enumeración ordenada:
      | orden | archivo/sección                                            |
      | 1     | README sección "Visión / Tesis"                           |
      | 2     | vault/product-owner/strategy/vision.md                     |
      | 3     | vault/product-owner/strategy/goal-*.md                     |
      | 4     | vault/architect/research/library/INDEX.md                  |
      | 5     | vault/shared/sessions/archive/* (WAs como evidencia)       |
    And el orden tiene sentido para la audiencia (no aleatorio)

  # Scenarios de story-045-B: Completitud mínima por ruta
  Scenario: AC-B1 — Cada ruta con 3 elementos mínimos
    Given newcomer inspecciona una ruta concreta
    When cuenta elementos
    Then incluye mínimo:
      | elemento                                          |
      | 1 path de arranque (sección README o archivo vault) |
      | ≥1 artefacto del vault                             |
      | ≥1 slash command relevante                          |

  Scenario: AC-B2 — Tras ruta: acción siguiente concreta
    Given newcomer terminó de leer una ruta (ej. adoptante)
    When considera "qué hago ahora"
    Then sabe la acción concreta siguiente:
      | ruta       | acción siguiente                       |
      | Adoptante  | Ejecutar `npm run sem`                  |
      | Académica  | Revisar WAs archivados como evidencia   |
      | Técnica    | Leer agent files + workflows.md         |

  Scenario: AC-B3 — Cobertura ~60-70% (no exhaustiva)
    Given el repo completo tiene N archivos
    When newcomer sigue una ruta
    Then la ruta cubre ~60-70% del valor para su audiencia
    And NO pretende cubrir 100% del repo (ahondar es opcional)
```

## Notas

- **Verificable vía**: cuando se materialice + grep sobre README + count de elementos por ruta.

## Historia del refactor

Consolida spec-045-A/B en Gherkin único. Refactor 2026-05-13.
