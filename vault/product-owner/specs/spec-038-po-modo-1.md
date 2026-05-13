---
type: spec
id: spec-038-po-modo-1
title: "Spec Gherkin para feature-038: PO Modo 1 — Entrada al sistema (clasifica + decide + drafta + handoff)"
parent: feature-038-po-modo-1
related-stories:
  - story-038-A
  - story-038-B
  - story-038-C
  - story-038-D
related-feature: feature-038-po-modo-1
related-capability: cap-07-inception-greenfield
also-relates-to:
  - feature-036-orientacion-rol
  - feature-014-estructura-wa
  - feature-024-contrato-filesystem-changes
related-adrs:
  - ADR-latente-007
depends-on: []
dimensions-affected: [product, technical, usability, quality]
status: ready-for-implementation
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
ac-count: 12
---

```gherkin
Feature: feature-038-po-modo-1 — PO Modo 1 (entrada al sistema con propuesta humano)
  Como Product Owner extendido tras ritual de inicio
  Quiero escuchar propuesta, clarificar/clasificar outcome-type, decidir conduzco/delego, draftar WA autocontenido con briefings, presentar + confirmar + handoff
  Para que toda propuesta humano entre al sistema con WA legible standalone y rol orquestador correcto activado

  Background:
    Given el PO presentó panorámica al humano (feature-035 aplicada)
    And el humano respondió con propuesta
    And `vault/shared/governance/workflows.md` declara templates + heurística clasificación

  # Scenarios de story-038-A: PO escucha + clarifica + clasifica
  Scenario: AC-A1 — Clarifica ambigüedades
    Given humano propone "mejorar arquitectura" (ambiguo)
    When PO procesa la propuesta
    Then formula pregunta concreta:
      | tipo de clarificación                                  |
      | "¿Es ADR específico, refactor focal, o reorganización?" |
    And NO procede a clasificar sobre la ambigüedad

  Scenario: AC-A2 — Clasifica vía workflows.md heurística
    Given humano propone "definir visión"
    When PO consulta `vault/shared/governance/workflows.md` sección "Heurística de clasificación"
    Then matchea keywords "definir visión" → `outcome-type: vision-creation`
    And confirma con humano: "Clasifico como vision-creation. ¿De acuerdo?"

  Scenario: AC-A3 — Cross-cutting requiere declaración explícita
    Given humano propone "implementar login Google end-to-end"
    When PO procesa
    Then detecta que es cross-cutting (sin spec previa)
    And propone partición: "feature-design ahora + feature-build después (cadena de 2 WAs)"
    And confirma con humano antes de proceder

  # Scenarios de story-038-B: PO decide conduzco/delego
  Scenario: AC-B1 — Consulta tabla decisión
    Given outcome-type clasificado
    When PO procesa Modo 1 paso 4
    Then consulta tabla en agent file:
      | outcome-type                          | acción PO          |
      | vision-creation, goal-definition       | conduce             |
      | capability-creation, feature-design    | conduce             |
      | feature-build                          | conduce             |
      | adr (sin contexto product)             | delega Architect    |
      | refactor (sin spec previa)             | delega Architect    |
      | threat-model (standalone)              | delega Security     |
      | pipeline-change, infra-decision        | delega DevOps       |
      | observability-instrument               | delega DevOps       |
      | doc-edit no-estratégico                | infiere rol por path |
      | trivial                                | ejecuta sin WA      |

  Scenario: AC-B2 — Delegación con comunicación clara al humano
    Given PO decide delegar (ej. outcome-type = adr puro)
    When responde al humano
    Then incluye:
      | componente                                                |
      | "Esta es decisión arquitectónica pura"                    |
      | "Sal de mi sesión y abre `npm run arch`"                  |
      | "El Architect conduce ADRs aplicando adr-writing (Nygard)" |
      | "Si emerge implicación de producto, el Architect me invocará como subagente" |

  Scenario: AC-B3 — Si conduce, procede a paso 5
    Given PO decide conducir
    When procesa paso 5
    Then convoca scope-scan multi-rol via feature-018 `/scope-scan`
    And procede al resto del Modo 1

  # Scenarios de story-038-C: PO drafta WA autocontenido con briefings
  Scenario: AC-C1 — Carga + adaptación de template
    Given template `feature-design` cargado desde workflows.md
    When PO adapta steps
    Then mantiene steps "siempre"
    And mantiene steps `optional` cuya `condition` matchea dimensions-affected del scope-scan
    And omite steps `optional` cuya condition NO aplica
    And copia `on-close` del template al frontmatter del WA

  Scenario: AC-C2 — WA autocontenido (Gap 7)
    Given el WA consume contenido de archivos previos (aborted-references, discovery docs)
    When PO drafta el cuerpo
    Then reproduce el contenido relevante in extenso
    And NO solo referencia paths
    And un lector standalone entiende el WA sin abrir otros archivos
    And aplica el criterio Cohn INVEST `I = Independent`

  Scenario: AC-C3 — Briefing por step para steps no-PO (Gap 10)
    Given el WA tiene steps con `active-role` distinto del PO
    When PO drafta los briefings
    Then por cada step no-PO escribe sección "Briefing del step-N" con 4 bloques:
      | bloque                                       |
      | Mapa del grafo relevante (curado)            |
      | Contexto conversacional del humano           |
      | Razonamiento del orquestador al draftar      |
      | Output esperado complementario               |

    Given step con `modality: subagente` y autoridad de edición
    When PO drafta su purpose
    Then incluye requisito explícito: "el subagente DEBE declarar bloque `filesystem-changes` al cerrar (Gap 9)"

  # Scenarios de story-038-D: PO presenta WA + confirma + handoff
  Scenario: AC-D1 — Presentación legible
    Given WA en draft
    When PO presenta al humano
    Then formato incluye:
      | sección                                     |
      | outcome-type + fase                          |
      | dimensions detectadas                        |
      | flags relevantes del scope-scan (cat-4 categoría humano) |
      | lista compacta de steps con active-role     |
    And el formato es escaneable rápido

  Scenario: AC-D2 — Confirma antes de marcar active
    Given PO presentó WA
    When espera respuesta del humano
    Then NO marca `status: active` hasta confirmación
    And si humano pide ajustes (ej. "añade step Security"), PO edita el WA + re-presenta

  Scenario: AC-D3 — Handoff según active-role del step-1
    Given humano confirma WA
    When PO determina próximo paso
    Then aplica:
      | active-role del step-1 | acción PO                                  |
      | product-owner          | arranca Modo 2 sin cambio de sesión        |
      | architect              | handoff: "Sal y abre `npm run arch`"       |
      | designer               | handoff: "Sal y abre `npm run des`"        |
      | ... otros roles        | handoff con atajo correspondiente          |
    And marca WA `status: active` + crea archivo en `vault/shared/sessions/active/`
```

## Notas

- **Verificable vía**: observación del comportamiento del PO durante Modo 1 en sesiones reales + inspección del WA producido (cuerpo autocontenido + briefings + filesystem-changes requisito) + presencia en `active/` con status correcto.

## Historia del refactor

Consolida spec-038-A/B/C/D (4 specs) en Gherkin único. Refactor 2026-05-13.
