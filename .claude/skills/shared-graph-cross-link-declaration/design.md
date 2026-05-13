---
type: research
id: borrador-skill-shared-graph-cross-link-declaration
title: "Borrador de skill: shared.graph-cross-link-declaration"
status: draft
created: 2026-04-30
author: pelayo
tags: [skill-borrador, shared, product-owner, graph, cross-link, happy-path]
---

# Borrador de skill: shared.graph-cross-link-declaration

> **Estado: borrador.** Skill compartida del Product Owner (lado estratégico + operativo) — usada también por otros roles cuando crean nodos del grafo. Materialización en `.claude/skills/shared/graph-cross-link-declaration/SKILL.md` durante Fase 5. Es la fusión de las skills propuestas inicialmente como `po-strategy.cross-link-analysis` y `po.dependency-mapping`.

## Propósito

Identificar y declarar las **aristas cross-link** del grafo SEM-IA en el frontmatter de un nodo: `also-relates-to`, `depends-on`, `dimensions-affected`, y para nodos específicos `related-adrs`. La espina dorsal jerárquica (`parent`) la decide el quality-check del nivel correspondiente; los cross-links los declara esta skill.

Operativa al **crear** un nodo nuevo y al **revisar** uno existente que tiene cross-links incompletos o desactualizados.

## Cuándo se invoca

- **Trigger PO (lado estratégico):** durante `vision-creation`/`goal-definition`/`capability-creation` al crear goals y capabilities; durante `strategy-review` periódico.
- **Trigger PO:** durante `feature-decomposition` y `spec-writing` al crear features y stories.
- **Trigger general:** cualquier rol cuando crea un nodo del grafo (ADR, learning, etc.) y necesita declarar sus aristas.

## Inputs

- El nodo a procesar (frontmatter actual + contenido).
- Catálogo de dimensiones del proyecto: `vault/shared/governance/dimensions.md`.
- Subgrafo relevante del vault (lectura focalizada — ver `vault/shared/governance/repo-structure.md` sobre el modelo grafo).
- Library: [[library-anthropic-subagents]] (formato).

## Proceso

### Paso 1 — Identificar `parent` (espina dorsal)
La espina dorsal jerárquica ya está decidida por el quality-check del tipo de nodo:
- Goal → `parent: vision`
- Capability → `parent: goal-N`
- Feature → `parent: cap-N-slug`
- Story → puede vivir embebida en feature; si es nodo propio: `parent: feature-N`
- Spec → `parent: feature-N`
- ADR → puede no tener `parent` único (ADRs cruzan el grafo).

Esta skill NO decide `parent`. Solo verifica que está declarado.

### Paso 2 — Identificar `dimensions-affected`
Razonando sobre el contenido del nodo, identificar qué dimensiones del producto holístico toca. Consultar el catálogo `vault/shared/governance/dimensions.md` para opciones disponibles.

Heurística: ¿qué custodio querría participar en construir / verificar este nodo? Si el security-officer querría participar → `security` está afectada.

Forma:
```yaml
dimensions-affected: [product, ux, technical, data, security]
```

### Paso 3 — Identificar `depends-on` (dependencias duras)
Otros nodos que **deben existir o estar resueltos** para que este nodo pueda implementarse / cumplirse.

Tipos:
- Goal depends-on otro goal (poco común; ejemplo: `goal-4` valida empíricamente, requiere `goal-1` y `goal-2` para tener data).
- Capability depends-on otra capability (común; ejemplo: `cap-3` Working Agreements depende de `cap-2` Memoria compartida).
- Feature depends-on feature (muy común; F2 requiere endpoint de F1).
- Feature depends-on ADR (la feature implementa decisión técnica documentada).

Forma:
```yaml
depends-on: [cap-2-memoria-compartida, feature-001]
```

### Paso 4 — Identificar `also-relates-to` (cross-links blandos)
Nodos que **no son dependencia dura** pero están **conceptualmente relacionados**:
- Una capability sirve a múltiples goals (cross-link a goals secundarios).
- Una feature comparte patrón con otra feature (no la requiere, pero hay sinergia).
- Una story usa convenciones de otra story.

Forma:
```yaml
also-relates-to: [goal-3, feature-003, cap-5-distribucion-limpia]
```

### Paso 5 — Identificar `related-adrs` (cuando aplica)
Aplica a features, specs, stories, y a veces capabilities. ADRs cuya decisión afecta al nodo:

```yaml
related-adrs: [adr-001-recipe-data-model, adr-005-export-strategy]
```

### Paso 6 — Búsqueda focalizada para validar
Para cada cross-link declarado, verificar que el nodo target existe y está accesible. Búsqueda focalizada según las dimensiones del nodo (evitar leer todo el vault — ver master doc sec. 7).

### Paso 7 — Reportar al humano para validación
Presentar al humano la lista de cross-links propuestos. El humano puede:
- Aprobar tal cual.
- Añadir cross-links que el sistema no detectó (conocimiento de dominio).
- Eliminar cross-links que el sistema propuso pero el humano sabe que no aplican.

El humano es la **fuente última** de cross-links — la skill propone, el humano valida.

## Outputs

- Frontmatter actualizado con cross-link fields completos:
  ```yaml
  parent: <ya existente>
  also-relates-to: [...]
  depends-on: [...]
  dimensions-affected: [...]
  related-adrs: [...]   # solo si aplica
  ```
- Reporte al humano con justificación breve por cada cross-link propuesto.
- Lista de cross-links rechazados (con razón) para auditoría.

## Fundamento bibliográfico

- `vault/shared/governance/repo-structure.md` — modelo grafo dirigido con espina dorsal jerárquica + cross-links + frontmatter.
- [[library-anthropic-subagents]] — formato de frontmatter para herramientas que parsean.
- (No requiere bibliografía externa — es operativa de la convención SEM-IA, no de literatura general.)

## Ejemplo aplicado

**Nodo:** `feature-009` (favoritos) — ejemplo ilustrativo de feature con dimension `product` + dependencias.

**Inputs leídos por la skill:**
- `vault/product-owner/strategy/cap-2-organize.md` (parent declarado)
- `vault/product-owner/strategy/cap-3-search.md` (relacionada porque la feature toca búsqueda)
- `vault/product-owner/specs/feature-003.md` (tags — patrón similar)
- `vault/product-owner/specs/feature-001.md` (formulario — dependencia)
- `vault/product-owner/specs/feature-002.md` (guardado SQLite — dependencia)
- `vault/architect/adrs/adr-001-recipe-data-model.md`

**Cross-links propuestos:**

```yaml
parent: cap-2-organize
also-relates-to: [feature-003, cap-3-search]
depends-on: [feature-001, feature-002]
related-adrs: [adr-001-recipe-data-model]
dimensions-affected: [product, ux, technical, data]
```

**Justificación al humano:**
- `parent: cap-2-organize` — confirmado por feature-decomposition.
- `also-relates-to: feature-003` — patrón visual y operativo similar a tags.
- `also-relates-to: cap-3-search` — el filtro por favoritas toca búsqueda.
- `depends-on: feature-001, feature-002` — necesita formulario y guardado funcionando.
- `related-adrs: adr-001` — afecta al modelo Recipe (campo `favorite`).
- `dimensions-affected: [product, ux, technical, data]` — no toca security ni quality específicamente.

**Validación humana:** humano confirma; añade `also-relates-to: feature-006` (búsqueda) que el sistema marcó como cap-link pero conviene también a nivel feature.

## Limitaciones

- La skill depende de **lectura focalizada efectiva**. En vaults grandes, si la búsqueda focalizada falla, los cross-links propuestos serán incompletos. Mitigación: el humano valida.
- Cross-links a futuro (nodos que se crearán después) no se pueden declarar ahora. Marcar como to-do en discovery: "feature-X creará dependencia hacia este nodo".
- La skill NO infiere `parent` — eso lo hace el quality-check del tipo de nodo. Si `parent` está mal declarado, la skill no lo corrige.
