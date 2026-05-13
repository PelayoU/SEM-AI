---
type: spec
id: spec-039-cadena-was-greenfield
title: "Spec Gherkin para feature-039: Cadena WAs greenfield (gaps upstream → propuesta cadena → iteración)"
parent: feature-039-cadena-was-greenfield
related-stories:
  - story-039-A
  - story-039-B
  - story-039-C
related-feature: feature-039-cadena-was-greenfield
related-capability: cap-07-inception-greenfield
also-relates-to: []
related-adrs: []
depends-on: []
dimensions-affected: [product, technical]
status: ready-for-implementation
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
ac-count: 9
---

```gherkin
Feature: feature-039-cadena-was-greenfield — Cadena WAs greenfield
  Como PO en Modo 1 ante propuesta que requiere padres upstream ausentes
  Quiero detectar gaps, proponer cadena ordenada en 3 formas canónicas, y draftear iterativamente (uno por uno tras /verify)
  Para construir grafo orgánico desde vault vacío sin commit prematuro de WAs futuros

  Background:
    Given PO en Modo 1 paso 5 convocando scope-scan
    And propuesta del humano requiere padre upstream según outcome-type

  # Scenarios de story-039-A: Gaps upstream detectados
  Scenario: AC-A1 — Advisors inspeccionan upstream
    Given propuesta de feature concreta
    When cada advisor procesa scope-scan
    Then cada uno inspecciona si la feature tiene capability padre
    And si NO existe, advisor flagea "gap: capability padre"

    Given propuesta de capability
    When advisor procesa
    Then inspecciona si hay goal padre
    And si NO existe, flagea "gap: goal padre"

  Scenario: AC-A2 — PO consolida gaps con Filtro PO
    Given los advisors devolvieron flags upstream
    When PO consolida
    Then aplica Filtro PO regla 12
    And clasifica los gaps como cat-1 (aplica yo proponiendo cadena) si son legítimos
    And documenta en artefacto declarativo filtro-po-*.md

  Scenario: AC-A3 — Presenta resumen al humano
    Given gaps consolidados
    When PO presenta al humano
    Then incluye:
      | dato                                              |
      | Lista de gaps upstream detectados (visión/goals/capability) |
      | Implicación: cadena de WAs propuesta              |
      | Pregunta: "¿Confirmas arranque de cadena?"        |

  # Scenarios de story-039-B: PO propone cadena en 3 formas
  Scenario: AC-B1 — Cadena directa greenfield (4 WAs)
    Given vault completamente vacío + propuesta de feature
    When PO determina cadena
    Then propone 4 WAs en orden:
      | WA           | outcome-type         |
      | WA-1         | vision-creation       |
      | WA-2..N+1    | goal-definition × N   |
      | WA-N+2..M+1  | capability-creation × M |
      | WA-final     | feature-design × K    |

    Given vault con visión + goals pero sin capability
    When PO determina cadena
    Then propone cadena corta de 2 WAs: `capability-creation` → `feature-design`

  Scenario: AC-B2 — Modo arbitraje: 3 opciones al humano
    Given propuesta contradice visión vigente o es cross-cutting
    When PO presenta al humano
    Then NO propone cadena automática
    And presenta 3 opciones explícitamente:
      | opción                            | descripción                                  |
      | Descartar el cambio               | Visión/grafo prevalece                      |
      | Modificar nivel superior + propagar | WA vision-realignment + re-design capabilities |
      | Documentar excepción consciente   | Cross-cutting feature con coherence-exception + ADR |

  Scenario: AC-B3 — Drafta solo primer WA, no toda la cadena
    Given humano confirma cadena
    When PO procede
    Then drafta SOLO el primer WA (ej. vision-creation)
    And NO drafttea WA-2, WA-3, etc. por adelantado
    And tras /verify del WA-N, drafta WA-N+1 (story-039-C cubre la iteración)

  # Scenarios de story-039-C: Iteración cadena WAs
  Scenario: AC-C1 — Drafta solo primer WA
    Given cadena de 4 WAs propuesta
    When PO procede tras confirmación
    Then drafta SOLO WA-1 (vision-creation)
    And `vault/shared/sessions/active/` contiene 1 WA (no 4)
    And el WA-1 declara `objective`, `steps[]`, `closure-criteria`, `on-close` propios

  Scenario: AC-C2 — Drafta siguiente tras /verify del previo
    Given WA-1 completado con /verify aprobado
    And vision.md transitó a `status: active`
    When PO procede al siguiente eslabón
    Then drafta WA-2 (goal-definition) con:
      | campo del WA-2     | valor                                |
      | consumes.node-id   | vision (el nodo producido por WA-1)  |
      | consumes.status    | active                                |
      | parent-WA-cadena   | wa-N-1 (referencia para audit trail) |
    And NO se drafta WA-3, WA-4 antes de cerrar WA-2

  Scenario: AC-C3 — Independencia + pivots aplican Gap 4
    Given cada WA de la cadena
    When PO los procesa
    Then cada uno es independiente (closure-criteria + on-close propios)
    And si emerge pivot mid-WA (4 señales Gap 4)
    Then PO aplica Protocolo Gap 4 sobre el WA actual (sin afectar a WAs ya cerrados de la cadena ni a planeados)
```

## Notas

- **Verificable vía**: observación del comportamiento del PO + inspección de `active/` y `archive/` durante el lifecycle de la cadena (1 WA cada vez).

## Historia del refactor

Consolida spec-039-A/B/C en Gherkin único. Refactor 2026-05-13.
