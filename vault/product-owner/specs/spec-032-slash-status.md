---
type: spec
id: spec-032-slash-status
title: "Spec Gherkin para feature-032: Slash /status (panorámica + Dual Track + backlog query)"
parent: feature-032-slash-status
related-stories:
  - story-032-A
  - story-032-B
related-feature: feature-032-slash-status
related-capability: cap-06-visibilidad-operativa
also-relates-to:
  - feature-035-ritual-inicio-po
related-adrs:
  - ADR-latente-008
depends-on: []
dimensions-affected: [product, usability]
status: ready-for-implementation
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
ac-count: 7
---

```gherkin
Feature: feature-032-slash-status — Slash /status (panorámica completa + Dual Track)
  Como operador humano (o agente al arrancar sesión)
  Quiero ejecutar /status desde cualquier sesión y recibir snapshot agregado del proyecto
  Para validar estado conocido sin re-explorar el vault y visualizar el Dual Track materializado

  Background:
    Given un proyecto SEM-IA con vault accesible
    And `vault/shared/governance/workflows.md` declara templates con su fase SDLC

  # Scenarios de story-032-A: Operador ve panorámica completa con /status
  Scenario: AC-A1 — Output con 6 secciones canónicas siempre presentes
    Given el operador ejecuta `/status`
    When el comando produce output
    Then el output incluye 6 secciones en este orden:
      | sección       | contenido                                          |
      | Estrategia    | visión + goals + capabilities                      |
      | Producto      | features agrupadas por status                      |
      | Arquitectura  | ADRs agrupados por status                          |
      | WAs activos   | lista compacta por track Dual                      |
      | Backlog       | query emergente sobre ready-for-implementation     |
      | Audits        | counts de audits/reports por tipo                  |
    And cada sección incluso vacía aparece con encabezado (no se omite)

  Scenario: AC-A2 — Sección Estrategia poblada
    Given el vault tiene visión + N goals + M capabilities
    When `/status` procesa la sección Estrategia
    Then muestra:
      | dato                | formato                                  |
      | Visión              | active / draft / ausente                 |
      | Goals               | count + IDs ("goal-1, goal-2, ...")      |
      | Capabilities        | count active + count draft + IDs cortos  |

  Scenario: AC-A3 — Sección Producto agrupada por status
    Given el vault tiene N features en distintos estados
    When `/status` procesa la sección Producto
    Then agrupa por status: draft / active / ready-for-implementation / in-implementation / implemented / deprecated
    And cada grupo muestra count + IDs si count > 0

  Scenario: AC-A4 — Sección Backlog query emergente
    Given el vault tiene N specs con `status: ready-for-implementation`
    When `/status` procesa la sección Backlog
    Then ejecuta query: `find vault/ -name "*.md" + filtrar por status: ready-for-implementation`
    And reporta: count + IDs de los nodos en backlog
    And la query es computada en tiempo real (no estructura persistente paralela)
    And referencia ADR-latente-008 (Backlog query emergente) como decisión arquitectónica subyacente

  # Scenarios de story-032-B: /status agrupa WAs por track Dual
  Scenario: AC-B1 — 4 tracks agrupados según fase SDLC
    Given hay WAs activos
    When `/status` procesa la sección WAs
    Then agrupa en 4 tracks según fase del template del WA:
      | fase             | track       |
      | discovery        | Discovery   |
      | design           | Discovery   |
      | implementation   | Delivery    |
      | operations       | Operations  |
      | meta             | Meta        |
    And el mapping se lee de `vault/shared/governance/workflows.md` (template del outcome-type del WA)

  Scenario: AC-B2 — Formato compacto por WA + Dual Track visible
    Given un WA activo wa-2026-05-13-005 (outcome-type: feature-design, step actual: 2f, active-role: product-owner)
    When `/status` lo lista en track Discovery
    Then muestra una línea compacta:
      | formato                                                       |
      | "wa-2026-05-13-005 · feature-design · product-owner · 5/14"   |
    And cada WA ocupa una línea similar

    Given proyecto maduro con WA Discovery (feature-design) + WA Delivery (feature-build) simultáneos
    When `/status` procesa
    Then ambos aparecen en sus tracks respectivos
    And el operador visualiza Dual Track materializado

  Scenario: AC-B3 — Sin WAs activos: mensaje consistente
    Given no hay archivos en `vault/shared/sessions/active/` (excepto .gitkeep)
    When `/status` procesa la sección WAs
    Then reporta "Sin WAs activos"
    And el formato es consistente entre proyectos vacíos y maduros (la sección siempre aparece)
```

## Notas

- **Verificable vía**: ejecución `/status` real + inspección del output + comparación con WAs físicos en `vault/shared/sessions/active/`.
- **Performance**: query O(N) sobre filesystem. Para vault grande considerar caching (potencial ADR latente futuro).

## Historia del refactor

Consolida spec-032-A/B en Gherkin único por feature. Refactor 2026-05-13.
