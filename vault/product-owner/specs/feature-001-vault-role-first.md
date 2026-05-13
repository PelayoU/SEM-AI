---
type: feature
id: feature-001-vault-role-first
title: "Vault role-first como organización física del grafo"

# JTBD outcome (Cagan principio 1 — solve problems not features)
jtbd-outcome: "Cuando el operador (humano o agente) necesita localizar artefactos del proyecto, quiere navegar por rol custodio (no por tipo técnico), so I can encontrar el artefacto en el directorio responsable y evitar colisiones cross-rol en el sistema de archivos."

# Espina dorsal jerárquica
parent: cap-01-grafo-declarativo-persistente

# Dimensiones holísticas que toca
dimensions-affected: [product, technical]

# Aristas cross-link
depends-on: []
also-relates-to:
  - cap-02-multirol-agentes-homologos  # los roles que custodian existen por CAP-B
depends-on-harness:
  - filesystem-versionado-por-git  # estructura física del repo

# ADRs latentes apuntados (a aflorar en Lote B WAs `adr` posteriores)
related-adrs:
  - ADR-latente-002  # Vault role-first como organización física del grafo

# Estado
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005

# Fundamento bibliográfico
fundamento-bibliografico:
  - Ousterhout — A Philosophy of Software Design (deep modules: vault role-first como módulo profundo con interfaz simple)
  - Cohn — User Stories Applied (INVEST: organización que evita coupling implícito cross-rol)
  - Bass — Software Architecture in Practice (modifiability via separation of concerns)
---

# feature-001 · Vault role-first como organización física del grafo

## Problem

El proyecto SEM-IA tiene 8 roles custodios (PO, Architect, Designer, Business-analyst, Security-officer, QA, Developer, DevOps) que producen artefactos heterogéneos: strategy docs, specs, ADRs, audits, learnings, threat-models, reports, etc.

Sin una convención clara de organización física, surgen tres problemas:

1. **Colisión cross-rol**: dos roles que producen artefactos del mismo tipo técnico (ej. `.md` con frontmatter) pueden escribir sobre el mismo path por accidente.
2. **Navegación opaca**: el operador no sabe dónde buscar artefactos del rol X — debe inspeccionar todos los directorios.
3. **Acoplamiento implícito**: si la organización se hace por tipo (ej. `vault/specs/`, `vault/adrs/`, `vault/audits/`), un cambio en cualquier tipo afecta a múltiples roles simultáneamente.

## Hypothesis

Si organizamos el vault **por rol custodio** (`vault/<rol>/` para los 8 roles + `vault/shared/` para cross-rol), entonces:

1. La navegación es predecible — el operador sabe que los artefactos del rol X viven en `vault/<rol>/`.
2. La modificabilidad mejora (Bass QA) — cambios en convenciones de un rol no afectan a otros.
3. El acoplamiento queda explícito — para que dos roles compartan artefactos, deben usar `vault/shared/` deliberadamente.

## Expected outcome (JTBD)

*Cuando el operador (humano o agente) necesita localizar artefactos del proyecto, navega por rol custodio (no por tipo técnico), de modo que encuentra el artefacto en el directorio responsable y evita colisiones cross-rol.*

## Stories

Esta feature se descompone en 3 stories candidatas (a formalizar vía `spec-writing` skill con specs Gherkin formales):

- **story-001-A**: Como operador humano, navego al directorio del rol que necesito vía `vault/<rol>/`
- **story-001-B**: Como operador agente, escribo artefactos en `vault/<mi-rol>/<subcategoría>/` siguiendo convención role-first
- **story-001-C**: Como operador, encuentro artefactos cross-rol en `vault/shared/`

## Piezas del bootstrap que materializan esta feature

- Estructura física `vault/<rol>/` para los 8 roles (8 directorios)
- Estructura `vault/shared/` con sub-directorios: `sessions/`, `governance/`, `plans/`, `retros/`, `reviews/`
- `vault/shared/governance/repo-structure.md` que documenta el modelo

## Notas

- **Decisión arquitectónica subyacente**: ADR-latente-002 (Vault role-first como organización física del grafo) a aflorar en WA `adr` posterior con alternatives consideradas (organizar por tipo, organizar flat, etc.).
- **Coupling apropiado declarado**: feature `also-relates-to` cap-02 porque los roles que custodian existen por CAP-B. Sin CAP-B no hay roles custodios.
- **Dependencia del harness**: filesystem-versionado-por-git como sustrato — SEM-IA no provee filesystem, lo usa.
