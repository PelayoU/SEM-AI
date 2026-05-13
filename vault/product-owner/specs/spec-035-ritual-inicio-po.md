---
type: spec
id: spec-035-ritual-inicio-po
title: "Spec Gherkin para feature-035: Ritual de inicio del PO (lectura + panorámica canónica)"
parent: feature-035-ritual-inicio-po
related-stories:
  - story-035-A
  - story-035-B
related-feature: feature-035-ritual-inicio-po
related-capability: cap-06-visibilidad-operativa
also-relates-to:
  - feature-001-vault-role-first
  - feature-032-slash-status
related-adrs: []
depends-on:
  - feature-001-vault-role-first
dimensions-affected: [product, usability]
status: ready-for-implementation
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
ac-count: 6
---

```gherkin
Feature: feature-035-ritual-inicio-po — Ritual de inicio del PO al arrancar sesión
  Como operador agente PO al arrancar sesión `npm run sem`
  Quiero leer 5 directorios canónicos y presentar panorámica con formato uniforme antes del primer prompt
  Para arrancar la conversación con contexto compartido y mapa mental del estado del proyecto

  Background:
    Given el operador humano ejecutó `npm run sem`
    And la sesión Claude Code arrancó con identidad PO cargada

  # Scenarios de story-035-A: PO lee 5 directorios al arrancar
  Scenario: AC-A1 — Lectura de strategy/
    Given el PO inicia el ritual
    When ejecuta lectura de `vault/product-owner/strategy/`
    Then detecta:
      | tipo de nodo  | dato                          |
      | vision.md     | status (active / draft / ausente) |
      | goal-N.md     | count + IDs                       |
      | cap-NN.md     | count active + count draft + IDs  |

  Scenario: AC-A2 — Lectura de sessions/active/
    Given el PO continúa el ritual
    When ejecuta lectura de `vault/shared/sessions/active/`
    Then detecta WAs activos
    And si hay WA con step `active-role: product-owner` pending/in-progress
    Then PO prioriza Modo 2 sobre Modo 1 (continúa step en lugar de pedir nuevo input al humano)

  Scenario: AC-A3 — Lectura de specs/ adrs/ governance/
    Given el PO continúa el ritual
    When ejecuta lecturas de los 3 directorios
    Then detecta:
      | directorio                          | dato                                   |
      | vault/product-owner/specs/          | count features por status              |
      | vault/architect/adrs/               | count ADRs por status                  |
      | vault/shared/governance/            | paths conocidos (sin re-leer contenido si ya cargado en sesiones previas) |

    And graciously continúa si algún directorio NO existe (vault incompleto/greenfield)

  # Scenarios de story-035-B: PO presenta panorámica al humano
  Scenario: AC-B1 — Formato canónico de 6 secciones
    Given el PO construye la panorámica
    When la presenta al humano
    Then el formato incluye las 6 secciones canónicas en orden:
      | sección       | dato                                      |
      | Estrategia    | visión + goals + capabilities             |
      | Producto      | features agrupadas por status             |
      | Arquitectura  | ADRs agrupados por status                 |
      | WAs activos   | count + IDs por track Dual                |
      | Backlog       | count + IDs nodos ready-for-implementation|
      | Audits        | counts por tipo (threat-model/usability/business/qa-report) |
    And el formato es **coherente con el output de `/status`** (feature-032)

  Scenario: AC-B2 — Termina con pregunta abierta
    Given panorámica presentada
    When el PO concluye el primer turn
    Then incluye al final "Qué quieres hacer?" (o equivalente)
    And espera respuesta del humano antes de proceder

  Scenario: AC-B3 — Greenfield: indica acciones de inception
    Given el vault está vacío (panorámica muestra 0s)
    When el PO presenta panorámica
    Then indica "Sin WAs activos · Sin Backlog · Visión: ausente"
    And sugiere acciones de inception ("¿quieres arrancar visión? cadena de WAs vision-creation → goal-definition → capability-creation → feature-design")
    And referencia feature-038 PO Modo 1 + feature-039 Cadena WAs greenfield
```

## Notas

- **Verificable vía**: arrancar `npm run sem` con vault en distintos estados (vacío vs maduro) + observación del PO leyendo 5 directorios + output canónico de 6 secciones.

## Historia del refactor

Consolida spec-035-A/B en Gherkin único. Refactor 2026-05-13.
