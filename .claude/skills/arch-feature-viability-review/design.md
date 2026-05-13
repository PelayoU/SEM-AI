---
type: research
id: borrador-skill-architect-feature-viability-review
title: "Borrador de skill: architect.feature-viability-review"
status: draft
created: 2026-04-30
author: pelayo
tags: [skill-borrador, architect, feature, viability, happy-path]
---

# Borrador de skill: architect.feature-viability-review

> **Estado: borrador.** Materialización en `.claude/skills/architect/feature-viability-review/SKILL.md`.

## Propósito

Evaluar la **viabilidad técnica de una feature** candidata: qué archivos de código requiere crear/modificar, qué ADRs aplican, si introduce nuevos ADRs, qué tactics arquitectónicas usa, si encaja en los boundaries definidos. Producir review formal en `vault/architect/research/feature-N-architect-review.md`.

Esta skill se invoca **durante el flujo del PO** para una feature, después de `feature-decomposition` y antes de `feature-quality-check`. Es input crítico para cerrar la feature.

## Cuándo se invoca

- **Trigger principal:** PO ha descompuesto una capability en features y necesita validación técnica para cada feature antes de implementación.
- **Trigger secundario:** revisión de feature existente cuyo alcance ha cambiado.
- **Trigger asistencial:** humano pide "revisión técnica de esta feature".

## Inputs

- Feature candidata (frontmatter + descripción + stories embebidas + AC propuestos).
- Capability padre (para alineación top-down).
- ADRs existentes en `vault/architect/adrs/`.
- Features hermanas y existentes (para detección de coupling vía `coupling-detection`).
- Estructura de código actual (lectura focalizada en directorios relevantes).
- Library: [[library-bass-software-architecture]], [[library-ousterhout-philosophy-software-design]], [[library-martin-clean-architecture]].

## Proceso — 6 pasos

### Paso 1 — Identificar archivos de código a tocar
Por la spec en Gherkin + AC:
- ¿Qué archivos nuevos hay que crear?
- ¿Qué archivos existentes hay que modificar?
- ¿Qué tests nuevos hay que añadir?
- ¿Hay migrations / cambios de datos?

### Paso 2 — Identificar ADRs aplicables
- ADRs ya aceptados que **constriñen** la implementación. La feature debe respetarlos.
- ¿Requiere ADR nuevo? Identificar si la feature toma una decisión arquitectónica significativa (cross-cutting, alternativas razonables, alguien futuro lo va a cuestionar). Si sí, escalar a `adr-writing`.

### Paso 3 — Evaluar respecto a Clean Architecture (Martin)
- ¿Las dependencias introducidas apuntan hacia adentro (capas internas)?
- ¿La feature respeta los boundaries existentes?
- ¿Introduce violación de SOLID? (especialmente SRP y DIP)

Si rompe Dependency Rule → rojo. Si rompe SOLID → amarillo, marcar.

### Paso 4 — Evaluar modularidad (Ousterhout)
- ¿La feature introduce módulos nuevos? Si sí, ¿son **deep modules** (interfaz pequeña, implementación grande)?
- ¿Hay riesgo de **information leakage** (mismo conocimiento usado en múltiples lugares)?
- ¿La feature aumenta cognitive load del sistema?

### Paso 5 — Detectar coupling problemático
Invocar `coupling-detection` (skill separada) sobre las features hermanas y existentes. La feature no debe introducir acoplamiento no deseado.

### Paso 6 — Producir review estructurada
Output como archivo en `vault/architect/research/feature-N-architect-review.md` con:
- Viabilidad: aprobada / aprobada con condiciones / rechazada.
- Archivos a crear (lista).
- Archivos a modificar (lista).
- ADRs aplicables (referencias).
- ADRs nuevos requeridos (lista para `adr-writing`).
- Tactics arquitectónicas usadas.
- Acoplamientos identificados (con `coupling-detection`).
- Riesgos arquitectónicos detectados.
- Recomendaciones de implementación.

## Output format

Archivo `vault/architect/research/feature-N-architect-review.md` con estructura completa anterior. Frontmatter:

```yaml
---
type: research
id: research-feature-N-architect-review
title: "Architect review — feature-N"
related-feature: feature-N
status: draft
created: YYYY-MM-DD
author: architect
---
```

**Recomendación final** explícita en el cuerpo:
1. Aprobar.
2. Aprobar con condiciones (lista de qué resolver antes de implementar).
3. Reformular feature (volver al PO).
4. Bloquear (la feature no es técnicamente viable como está; requiere revisión de capability).

## Fundamento bibliográfico

- [[library-bass-software-architecture]] — análisis arquitectónico de features.
- [[library-ousterhout-philosophy-software-design]] — modularidad, information hiding.
- [[library-martin-clean-architecture]] — Dependency Rule, SOLID.
- [[library-ford-evolutionary-architecture]] — appropriate coupling, fitness functions aplicables.

## Ejemplo aplicado

**Feature:** `feature-009` (favoritos) — del ejemplo boceto inicial sec. 19.

Output del Architect (extracto):

> *Viabilidad: aprobada.*
> *Acuerdo con Opción A propuesta por DBA. Actualización de adr-001 es lo correcto.*
> *Persistencia del filtro: estado en memoria del componente, no localStorage ni DB.*
> *Archivos a crear: `FavoriteButton.tsx`, `FavoriteButton.test.tsx`, `FavoriteFilter.tsx`, `FavoriteFilter.test.tsx`, `004_add_favorite_to_recipes.sql`*
> *Archivos a modificar: `Recipe.ts`, `recipeRepository.ts`, `RecipeCard.tsx`, `RecipeList.tsx`, `adr-001`*
> *Sin acoplamientos problemáticos: revisé feature-003 (tags) y feature-006 (búsqueda). Los filtros pueden combinarse con AND lógico sin conflicto.*

## Limitaciones

- La review depende de que el código existente esté legible y bien estructurado. En código legacy, identificar archivos a tocar puede ser exploratorio.
- En proyectos en fase de bootstrapping (poco código), la review es predictiva — el Architect sugiere estructura inicial.
- La skill no implementa; solo revisa. Si la review identifica que falta información, la feature debe volver a discovery o decomposition.
