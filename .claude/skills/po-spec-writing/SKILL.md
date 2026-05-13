---
name: po-spec-writing
description: "Producir spec Gherkin canónica Adzic POR FEATURE (no por story): agrupa AC de todas las stories de una feature en un único archivo .md con bloque Feature Gherkin nombrado por la feature SEM-IA, Scenarios numerados (AC-A1, AC-A2, AC-B1...) con prefijo de letra correspondiente a la story origen para trazabilidad, y cada AC trazable a tests futuros vía @ac-coverage. Use this skill when a feature is approved (post-decomposition con stories + INVEST OK) and needs its formal contract Gherkin, when reviewing an outdated spec, or in retroactive mode when reading existing code to derive specs."
allowed-tools: Read Write Edit Glob Grep
materializes-feature: [feature-038-po-modo-1]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8 + refactor 2026-05-13): skill operativa invocada por PO Modo 1 cuando outcome-type = feature-design. Convención canónica POR FEATURE (1 spec agrupa stories) post-refactor de 2026-05-13 que corrigió alucinación bibliográfica anterior (1:1 story:spec).
---

# Skill: spec-writing (Product Owner)

## Quick reference

Skill compuesta que cubre **todo el camino de examples a spec ejecutable en un único archivo POR FEATURE** (Adzic literal):
- Filtrado de examples a AC formales por story (sub-skill absorbida desde la antigua `acceptance-criteria-definition`)
- Formato SMART
- Identificadores trazables (letra story + número secuencia)
- Escritura Gherkin agrupando Scenarios de todas las stories de la feature

**Convención canónica (Adzic literal, post-corrección 2026-05-13)**: 1 archivo `.md` por **feature SEM-IA**, NO por story. El bloque `Feature:` Gherkin agrupa N Scenarios cubriendo los AC de **todas las stories** de la feature, organizadas internamente con comentarios separadores `# Scenarios de story-NNN-X`. La spec queda como contrato ejecutable de comportamiento cohesivo entregable (Adzic — Specification by Example).

## When to invoke

- Feature aprobada con sus stories descompuestas (post `feature-decomposition` + INVEST OK por story) necesita su contrato formal Gherkin.
- Revisión de spec existente que ha quedado desactualizada.

## Inputs

- **Feature** aprobada (frontmatter + descripción + outcome JTBD).
- **Stories** descompuestas de la feature (formato Cohn).
- **Examples** generados durante discovery por story.
- ADRs aplicables.

## Process — 9 pasos

### Paso 1 — Lee contexto
Feature padre, todas las stories de la feature, capability ascendente, ADRs relevantes.

### Paso 2 — Recolecta examples por story
Por cada story de la feature, lista los examples generados durante discovery. Cada example = situación concreta del uso.

### Paso 3 — Clasifica cada example en categoría

| Categoría | Decisión | Ejemplo |
|---|---|---|
| **AC crítico** | Formalizar como Scenario | "¿Y si título vacío?" |
| **Decisión de producto** | Documentar sin AC | "Permitimos emojis" |
| **Trivial / no controlable** | Descartar con justificación | "¿Y sin batería?" |
| **Resuelto por ADR** | Referenciar ADR | "¿Cómo se serializa?" → adr-001 |
| **Diferido a próximo release** | Documentar como to-do | "¿Multi-idioma?" |

### Paso 4 — Para cada AC crítico, escribir en forma SMART
- **Specific**: ¿qué exactamente?
- **Measurable**: binario pasa/no pasa preferido.
- **Realistic**: comportamiento implementable.

Reformular AC que fallen.

### Paso 5 — Asignar identificadores únicos por story

`AC-A1`, `AC-A2`, ... para AC derivados de la primera story (story-NNN-A). `AC-B1`, `AC-B2`, ... para AC de story-NNN-B. Y así sucesivamente. `AC-S1`, `AC-S2` para AC de seguridad (típicamente añadidos por threat-modeling, transversales).

**La letra prefijo (A, B, C, D, ...) corresponde a la story de origen** — preserva trazabilidad story↔AC dentro del único archivo Gherkin por feature.

### Paso 6 — Frontmatter de la spec

```yaml
---
type: spec
id: spec-<feature-NNN>-<slug>
title: "Spec Gherkin para feature-<NNN>: <título>"
parent: feature-<NNN>-<slug>  # ← parent ES la feature, NO la story
related-stories: [story-<NNN>-A, story-<NNN>-B, story-<NNN>-C]  # ← stories agrupadas
related-feature: feature-<NNN>-<slug>
related-adrs: []
also-relates-to: []
depends-on: []
dimensions-affected: [<unión de dimensions de stories agrupadas>]
status: draft
created: <YYYY-MM-DD>
author: product-owner
ac-count: <N total>  # suma de AC across stories de la feature
---
```

En modo lectura: añadir `derived-from` con paths de los archivos leídos.

### Paso 7 — Header Gherkin + Background

```gherkin
Feature: feature-<NNN>-<slug> — <Título descriptivo>
  Como [tipo de usuario primario]
  Quiero [capacidad cohesiva entregable]
  Para [outcome JTBD que conecta con la capability]

  Background:
    Given [contexto común a TODOS los scenarios de TODAS las stories, mantener corto]
```

El `Feature:` nombra la **feature SEM-IA** (no la story). El bloque Como/Quiero/Para narra el outcome general de la feature (no de una story individual).

### Paso 8 — Scenarios agrupados por story origen

Dentro del Gherkin, agrupar Scenarios por story con comentarios separadores:

```gherkin
  # Scenarios de story-<NNN>-A: <título story A>
  Scenario: AC-A1 — <título del AC>
    Given <precondición>
    When <acción>
    Then <resultado esperado>

  Scenario: AC-A2 — <título del AC>
    Given <precondición>
    When <acción>
    Then <resultado esperado>

  # Scenarios de story-<NNN>-B: <título story B>
  Scenario: AC-B1 — <título del AC>
    Given <precondición>
    When <acción>
    Then <resultado esperado>

  Scenario: AC-B2 — <título del AC>
    Given <precondición>
    When <acción>
    Then <resultado esperado>
```

Cada AC = un Scenario. Forma Given/When/Then estricta — sin narrativa libre.

### Paso 9 — Validación + anotación para tests

- Cada AC tiene exactamente un Scenario.
- **Todos los AC de todas las stories de la feature** están presentes en el archivo (sin gaps).
- Ningún Scenario refiere a estado fuera del Background o su Given.
- Identificadores `AC-XN` consistentes (letra = story, número = secuencia dentro de la story).
- Comentarios `# Scenarios de story-NNN-X` separan visualmente los grupos.
- `dimensions-affected` completo (unión de las dimensiones de las stories agrupadas).
- `related-stories` en frontmatter lista todas las stories agrupadas.
- Anotación para tests futuros: `// @sem-ia: <spec-id>` + `// @ac-coverage: AC-A1, AC-B2` en archivos de test.
- En modo lectura: si tests existentes ya cubren algunos AC, anotar `// @ac-coverage` sobre esos tests.

## Estructura del nodo

Archivo único `vault/product-owner/specs/spec-<feature-NNN>-<slug>.md` por feature, con bloque Gherkin embebido agrupando todos los Scenarios de todas las stories.

Las stories padre (`vault/product-owner/specs/story-<NNN>-<X>.md`) mantienen su archivo individual — la narrativa Cohn se mantiene por story; lo que se consolida es solo la **spec Gherkin formal**.

## Output format

1 archivo `vault/product-owner/specs/spec-<feature-NNN>-<slug>.md` POR FEATURE SEM-IA (no por story).

## Bibliographic foundation

- `vault/architect/research/library/adzic-specification-by-example.md` — 7 patrones SbE, Gherkin canónico, living documentation. **Convención canónica corregida 2026-05-13**: 1 archivo Gherkin = 1 feature (agrupa stories).
- `vault/architect/research/library/cohn-user-stories-invest.md` — formato de stories agrupadas.

## Full design

`./design.md` — incluye ejemplo completo.

## Limitations

- Gherkin es verboso. Para AC trivial puede ser overhead.
- **Convención canónica Adzic (post-corrección 2026-05-13)**: 1 spec Gherkin POR FEATURE agrupando stories. La regla anterior "una story = una spec" era interpretación SEM-IA estricta no canónica Adzic; corregida tras detección humana.
- La spec describe comportamiento (what), no implementación (how). Si emerge implementación, refactorizar.

## Status lifecycle

**Esta skill produce el spec con `status: draft`.** **NO** setees el status final desde aquí. La transición a `ready-for-implementation` la aplica recepción al ejecutar `/verify` del WA, leyendo el campo `on-close` del frontmatter del WA.

| Status | Cuándo |
|---|---|
| `draft` | Output inicial de esta skill (durante el step) |
| `ready-for-implementation` | Tras /verify del WA `feature-design` aprobado (entra al backlog) |
| `in-implementation` | Step 1 del WA `feature-build` lo marca al consumir |
| `implemented` | Tras /verify del WA `feature-build` aprobado |
| `deprecated` | Spec ya no aplica (decisión consciente vía WA apropiado) |

## WA mapping

Esta skill se invoca dentro del template **`feature-design`** (fase `design`, ahora con `mode-flag` formal — ver workflows.md). Se invoca después de `feature-decomposition` (que produce features + stories) y antes de `feature-quality-check` (que valida la feature completa con su spec).

**Nota histórica**: esta skill absorbió el contenido de la antigua `acceptance-criteria-definition` (que fue eliminada) — los pasos 3-5 vienen de allí. En el modelo Adzic SbE, definir AC y escribir spec son la misma actividad.
