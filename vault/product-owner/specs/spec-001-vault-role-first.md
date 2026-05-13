---
type: spec
id: spec-001-vault-role-first
title: "Spec Gherkin para feature-001: Vault role-first como organización física del grafo"
parent: feature-001-vault-role-first
related-stories:
  - story-001-A
  - story-001-B
  - story-001-C
related-feature: feature-001-vault-role-first
related-capability: cap-01-grafo-declarativo-persistente
also-relates-to:
  - feature-009-catalogo-roles
  - feature-024-contrato-filesystem-changes
related-adrs:
  - ADR-latente-002
depends-on:
  - feature-024-contrato-filesystem-changes
dimensions-affected: [product, technical]
status: ready-for-implementation  # transitado por /verify del WA-005 el 2026-05-13T08:30+02:00; conservado en refactor 2026-05-13 (1:1→agrupado)
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
ac-count: 9
---

```gherkin
Feature: feature-001-vault-role-first — Vault role-first como organización física del grafo
  Como operador (humano o agente)
  Quiero localizar y escribir artefactos del proyecto navegando por rol custodio (no por tipo técnico)
  Para encontrar cada artefacto en el directorio responsable, distinguir artefactos transversales de los custodiados, y evitar colisiones cross-rol en el filesystem

  Background:
    Given el repo SEM-IA está clonado en el filesystem del operador
    And `vault/shared/governance/role-catalog.md` declara los 8 roles custodios
    And `vault/shared/` existe como directorio para artefactos cross-rol

  # Scenarios de story-001-A: Navegación humana al directorio del rol
  Scenario: AC-A1 — Existencia de directorio por rol
    Given el operador conoce el id de un rol custodio (ej. "architect")
    When el operador ejecuta `ls vault/architect/`
    Then el directorio existe en el filesystem
    And el comando devuelve la lista de sub-directorios del rol (ej. "adrs research")

  Scenario: AC-A2 — Sub-directorios convencionales por rol
    Given el operador navega a `vault/architect/`
    When inspecciona los sub-directorios
    Then encuentra al menos `adrs/` y `research/`
    And cada sub-directorio refleja una sub-categoría del dominio del rol Architect

    Given el operador navega a `vault/product-owner/`
    When inspecciona los sub-directorios
    Then encuentra al menos `strategy/`, `specs/` y `discovery/`
    And cada sub-directorio refleja una sub-categoría del dominio del rol Product Owner

  Scenario: AC-A3 — Convención documentada en governance
    Given el operador necesita conocer la convención completa rol × sub-directorios
    When abre `vault/shared/governance/repo-structure.md`
    Then encuentra la tabla con las 8 filas (una por rol) y las columnas declarando sub-directorios convencionales
    And la tabla incluye al menos las sub-categorías que existen físicamente en el filesystem actual

  # Scenarios de story-001-B: Escritura agente en vault/<mi-rol>/
  Scenario: AC-B1 — Escritura en directorio propio del rol
    Given el rol activo es "architect"
    And el WA declara `scope-allowed` que incluye `vault/architect/adrs/*.md`
    When el agente produce un ADR
    Then el artefacto se escribe en `vault/architect/adrs/adr-NNN-slug.md`
    And NO se escribe en `vault/adrs/` ni en otros directorios cross-rol

  Scenario: AC-B2 — Escritura cross-rol requiere autorización explícita
    Given el rol activo es "product-owner"
    And el `scope-forbidden` del WA incluye `vault/architect/adrs/`
    When el PO intenta escribir un ADR en `vault/architect/adrs/`
    Then la escritura viola el scope-forbidden
    And el contrato `filesystem-changes` (Gap 9) detecta la violación al cierre del step
    And el orquestador del WA registra el flag

    Given el rol activo es "product-owner"
    And el `scope-allowed` del WA incluye explícitamente `vault/architect/adrs/adr-NNN.md` (autorización consciente)
    When el PO escribe en ese path
    Then la escritura es legítima
    And el contrato `filesystem-changes` registra el path como esperado

  Scenario: AC-B3 — Artefactos cross-rol en vault/shared/
    Given el artefacto es un Working Agreement (WA)
    And los WAs coordinan múltiples roles (cross-rol por naturaleza)
    When el orquestador (PO típicamente) drafta el WA
    Then el WA se escribe en `vault/shared/sessions/active/wa-YYYY-MM-DD-NNN.md`
    And NO se escribe en `vault/product-owner/sessions/` (sería role-first incorrecto)

  # Scenarios de story-001-C: Localización de artefactos cross-rol en vault/shared/
  Scenario: AC-C1 — WAs en vault/shared/sessions/
    Given el operador busca el WA activo del proyecto
    When ejecuta `ls vault/shared/sessions/active/`
    Then encuentra los WAs en curso con formato `wa-YYYY-MM-DD-NNN.md`
    And NO los encuentra en `vault/<algún-rol>/sessions/`

    Given el operador busca un WA archivado
    When ejecuta `ls vault/shared/sessions/archive/`
    Then encuentra los WAs cerrados

  Scenario: AC-C2 — Governance docs canónicos en vault/shared/governance/
    Given el operador busca el catálogo de roles
    When ejecuta `cat vault/shared/governance/role-catalog.md`
    Then encuentra el catálogo
    And el catálogo declara los 8 roles custodios

    Given el operador busca los workflow templates
    When ejecuta `cat vault/shared/governance/workflows.md`
    Then encuentra los 14 templates por fase SDLC

  Scenario: AC-C3 — Decisión de ownership por JTBD primario
    Given un artefacto candidato cuyo JTBD es de un único rol (ej. ADR técnico → Architect)
    When el rol drafta el artefacto
    Then el artefacto se escribe en `vault/<rol-único>/<sub>/`
    And NO se escribe en `vault/shared/` (sería over-share)

    Given un artefacto candidato cuyo JTBD requiere múltiples roles (ej. WA, governance doc)
    When el orquestador drafta el artefacto
    Then el artefacto se escribe en `vault/shared/<sub>/`
    And la decisión cross-rol queda implícita en el path (sin necesidad de declarar explícitamente)
```

## Notas de implementación / verificación

- **Verificable vía**: ejecución de comandos `ls` sobre el filesystem real + inspección de `repo-structure.md` + grep sobre paths escritos durante steps + comparación con `filesystem-changes` reportado por subagentes.
- **Trazabilidad a tests futuros**: cuando exista código en `src/` que dependa de la convención role-first (ej. `sem-ia check` validador de estructura), los tests anotarán `// @sem-ia: spec-001-vault-role-first` + `// @ac-coverage: AC-A1, AC-A2, AC-A3, AC-B1, AC-B2, AC-B3, AC-C1, AC-C2, AC-C3`.
- **Decisión arquitectónica subyacente**: ADR-latente-002 (a aflorar en Lote B WA `adr`) — alternatives consideradas: organización flat-by-type, organización mixed, organización feature-first. Decisión actual: role-first por modifiability (Bass QA).

## Historia del refactor

Esta spec consolida las 3 specs previas (spec-001-A, spec-001-B, spec-001-C) — una por story — en un único archivo Gherkin por feature, conforme a la convención canónica Adzic SbE (Feature: Gherkin = funcionalidad cohesiva entregable agrupando Scenarios de todas las stories). Refactor aplicado 2026-05-13 tras detección humana de alucinación bibliográfica previa (1:1 story:spec).
