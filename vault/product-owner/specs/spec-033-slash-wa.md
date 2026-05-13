---
type: spec
id: spec-033-slash-wa
title: "Spec Gherkin para feature-033: Slash /wa (detalle del WA + reorientación agente)"
parent: feature-033-slash-wa
related-stories:
  - story-033-A
  - story-033-B
related-feature: feature-033-slash-wa
related-capability: cap-06-visibilidad-operativa
also-relates-to:
  - feature-024-contrato-filesystem-changes
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
Feature: feature-033-slash-wa — Slash /wa (detalle WA activo + reorientación agente)
  Como operador humano o agente en sesión durante un WA activo
  Quiero ejecutar /wa y ver detalle estructurado para ubicarme sin abrir el archivo manualmente
  Para humanos: ubicación rápida; para agentes: arrancar step con contexto curado (Briefing Gap 10)

  Background:
    Given el operador está en una sesión Claude Code
    And existe al menos un WA en `vault/shared/sessions/active/`

  # Scenarios de story-033-A: Humano ve detalle del WA activo
  Scenario: AC-A1 — Identificación automática si un solo WA
    Given hay un único WA activo `wa-2026-05-13-005.md`
    When el operador ejecuta `/wa`
    Then el slash identifica el WA automáticamente
    And presenta detalle sin preguntar

    Given hay 2 WAs activos
    When el operador ejecuta `/wa`
    Then el slash pregunta cuál de los IDs detectados
    And tras elección, presenta detalle

  Scenario: AC-A2 — Output con detalle estructurado
    Given el WA detectado tiene 14 steps (mezcla pending/done/in-progress)
    When `/wa` produce output
    Then incluye:
      | sección                              | contenido                       |
      | Encabezado                           | ID + outcome-type + status      |
      | Steps[]                              | lista con status visual         |
      | active-role por step                 | rol declarado                   |
      | Progreso entries done                | resumen 1-3 líneas por entrada  |
      | Próximo step pending                 | destacado con acción sugerida   |
      | Scope (compacto)                     | scope-allowed + scope-forbidden |

  Scenario: AC-A3 — Sin WA activo
    Given `vault/shared/sessions/active/` está vacío (solo .gitkeep)
    When el operador ejecuta `/wa`
    Then reporta "Sin WAs activos."
    And sugiere "Para arrancar trabajo, ejecuta `npm run sem`."

  # Scenarios de story-033-B: Agente reorientación al continuar step
  Scenario: AC-B1 — Agente lee WA + Progreso entries previas
    Given el agente identifica su step
    When inspecciona el WA
    Then lee la sección Progreso del step anterior
    And extrae inputs concretos para su step (declarados en sección "Para el siguiente step" del Progreso)

  Scenario: AC-B2 — Agente lee Briefing por step (Gap 10)
    Given el WA contiene sección "Briefing por step" con bloques canónicos
    When el agente busca su briefing específico
    Then encuentra 4 bloques:
      | bloque                                    |
      | Mapa del grafo relevante (curado por PO)  |
      | Contexto conversacional del humano        |
      | Razonamiento del orquestador (PO)         |
      | Output esperado complementario            |
    And aplica el contexto curado al conducir su step

  Scenario: AC-B3 — Subagente con autoridad de edición registra filesystem-changes
    Given el step declara `modality: subagente`
    And el agente edita archivos en su carpeta
    When cierra el step
    Then incluye bloque `filesystem-changes` literal en su output
    And el orquestador lo registra en Progreso del WA (Gap 9 protocolo)
```

## Notas

- **Verificable vía**: ejecución `/wa` real + comportamiento del agente al arrancar (cita el WA + aplica briefing) + presencia de `filesystem-changes` en Progreso si modality es subagente.

## Historia del refactor

Consolida spec-033-A/B en Gherkin único. Refactor 2026-05-13.
