---
name: shared-graph-cross-link-declaration
description: "Identificar y declarar las aristas cross-link del grafo SEM-IA en el frontmatter de un nodo: also-relates-to, depends-on, dimensions-affected, related-adrs. Skill compartida del Product Owner extendido (nivel estratégico + operativo) y también invocable por otros roles cuando crean nodos del grafo. Use this skill when creating a new node and needing to declare its graph edges, or when reviewing an existing node with incomplete or stale cross-links."
allowed-tools: Read Glob Grep
materializes-feature: [feature-001-vault-role-first]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): skill compartida invocada por cualquier rol al crear un nodo del grafo. La convención cross-link es parte de la organización role-first del grafo (feature-001).
---

# Skill: graph-cross-link-declaration (Shared — Product Owner (lado estratégico + operativo))

## Quick reference

Declara las aristas cross-link del grafo (`also-relates-to`, `depends-on`, `dimensions-affected`, `related-adrs`) en el frontmatter de un nodo. La espina dorsal jerárquica (`parent`) la decide el quality-check del nivel correspondiente; los cross-links los declara esta skill.

## When to invoke

- **PO (lado estratégico):** durante WAs de discovery al crear goals y capabilities; durante `strategy-review` (later).
- **PO:** durante `feature-decomposition` y `spec-writing`.
- **Cualquier rol:** al crear nodo del grafo (ADR, learning, etc.) que necesita cross-links.

## Inputs

- El nodo a procesar (frontmatter actual + contenido).
- Catálogo de dimensiones: `vault/shared/governance/dimensions.md`.
- Subgrafo relevante (lectura focalizada).

## Process — 7 pasos

1. **Verifica `parent`** está declarado (la skill NO lo decide; verifica que existe).
2. **Identifica `dimensions-affected`** razonando sobre el contenido. Heurística: ¿qué custodio querría participar en construir/verificar este nodo?
3. **Identifica `depends-on`** (dependencias duras): nodos que deben existir/cumplirse para que este nodo se implemente o cumpla.
4. **Identifica `also-relates-to`** (cross-links blandos): nodos conceptualmente relacionados sin ser dependencia dura.
5. **Identifica `related-adrs`** (cuando aplica a features, specs, stories, capabilities).
6. **Búsqueda focalizada para validar**: cada cross-link declarado apunta a nodo existente. Búsqueda focalizada por dimensiones (no leer todo el vault).
7. **Reporta al humano para validación**: el humano puede aprobar, añadir cross-links que el sistema no detectó, eliminar los rechazados. **El humano es la fuente última.**

## Output format

Frontmatter actualizado:
```yaml
parent: <ya existente>
also-relates-to: [...]
depends-on: [...]
dimensions-affected: [...]
related-adrs: [...]   # solo si aplica
```

Reporte al humano con justificación breve por cada cross-link propuesto.

## Bibliographic foundation

- `vault/shared/governance/repo-structure.md` — modelo grafo dirigido con espina dorsal jerárquica + cross-links, frontmatter y aristas.
- `vault/architect/research/library/anthropic-subagents.md` — formato de frontmatter.

## Full design

`./design.md` — incluye ejemplo aplicado a feature-009 (favoritos).

## Limitations

- Depende de lectura focalizada efectiva. En vaults grandes, la búsqueda puede ser incompleta — el humano valida.
- Cross-links a futuro (nodos por crear) no se declaran ahora. Marcar como to-do en discovery.
- La skill NO infiere `parent` — si está mal declarado, no lo corrige.

## Status lifecycle

Esta skill NO produce nodos nuevos — modifica frontmatter de nodos existentes (añade aristas cross-link). No altera el `status` del nodo.

## WA mapping

Skill compartida invocable desde **cualquier template** que cree o modifique nodos del grafo. Casos típicos:

- **`capability-creation`**, **`goal-definition`**, **`vision-creation`**: declarar cross-links del nodo nuevo.
- **`feature-design`**: invocada por `feature-decomposition` y `spec-writing` para declarar cross-links de features y specs.
- **`adr`**: invocada por `adr-writing` para declarar `related-features`, `related-capabilities`.
