---
name: arch-adr-writing
description: "Escribir Architecture Decision Records (ADRs) siguiendo plantilla canónica de Nygard adaptada al frontmatter SEM-IA. Cada ADR documenta una decisión arquitectónica significativa con Context (value-neutral), Decision (active voice), Consequences (positive + negative + neutral), y Alternatives Considered. Use this skill when a significant architectural decision emerges (cross-cutting, reasonable alternatives, future readers will question it), or when superseding a previous ADR."
allowed-tools: Read Write Edit Glob Grep
materializes-feature: []
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): NO feature Nivel 1 directa cubre el comportamiento "Architect escribe ADR" — el outcome-type `adr` es feature del workflow no cubierta como feature Nivel 1 del WA-005. Skill se invocará en Lote B de WAs `adr` posteriores que aflorarán los 15-16 ADRs latentes identificados durante WA-005.
---

# Skill: adr-writing (Architect)

## Quick reference

Aplica 7 pasos para producir un ADR completo. Plantilla canónica de Nygard (1981) extendida con Alternatives Considered para SEM-IA.

## When to invoke

- Decisión arquitectónica significativa surge durante `feature-viability-review` o `capability-viability-review`.
- Revisión de decisión existente requiere supersession (= nuevo ADR).
- Humano pide "documentar esta decisión técnica".

## Inputs

- Contexto de la decisión.
- Decisión propuesta.
- Alternativas consideradas.
- ADRs existentes (detectar supersession o relación).

## Process — 7 pasos

### Paso 1 — Verificar que amerita ADR (heurística Nygard)

✅ Cross-cutting · alternativa rechazada razonable · alguien futuro lo va a cuestionar · cambio de decisión previa.
❌ Decisión trivial o reversible barata · detalle de implementación · estilística pura.

Si NO amerita → no ADR. Documentar en learning, comentario, o discovery note.

### Paso 2 — Asignar ID y título

`adr-NNN-slug`. NNN secuencial. Título: frase nominal corta.

### Paso 3 — Frontmatter

```yaml
---
type: adr
id: adr-NNN-slug
title: "ADR-NNN: descripción corta"
status: proposed
supersedes: null
superseded-by: null
related-features: [...]
related-capabilities: [...]
dimensions-affected: [technical, ...]
created: YYYY-MM-DD
author: architect
---
```

### Paso 4 — Sección Context
Lenguaje **value-neutral**. Describe fuerzas: tecnológicas, de producto, sociales/equipo, locales del proyecto. NO inclinar la decisión todavía.

### Paso 5 — Sección Decision
**Voz activa**, frases completas. *"We will [verb] [object] using [approach]."* Específico, no genérico.

### Paso 6 — Sección Consequences
Tres categorías obligatorias:
- **Positivas**
- **Negativas** (obligatorias — toda decisión tiene tradeoffs)
- **Neutras**

### Paso 7 — Sección Alternatives Considered (extensión SEM-IA)
Listar alternativas evaluadas y rechazadas, con razón breve. Auditabilidad.

## Estructura del nodo

```markdown
---
type: adr
id: adr-<NNN>-<slug>
title: "ADR-<NNN>: <descripción corta>"
status: proposed   # proposed | accepted | superseded | deprecated
supersedes: null
superseded-by: null
related-features: []
related-capabilities: []
dimensions-affected: [<lista>]
created: <YYYY-MM-DD>
author: architect
---

# ADR-<NNN>: <Título>

## Contexto

<Fuerzas tecnológicas, de producto, sociales/equipo, locales del proyecto. Lenguaje value-neutral.>

## Decisión

<Voz activa: "We will [verb] [object] using [approach]." Específico.>

## Consecuencias

### Positivas
- <...>

### Negativas
- <...>

### Neutras
- <...>

## Alternativas evaluadas

- **<Alternativa A>** — <razón de descarte>.
- **<Alternativa B>** — <razón de descarte>.
```

## Output format

Archivo `vault/architect/adrs/adr-NNN-slug.md` completo. Si supersede otro ADR → modificar el ADR previo a `status: superseded` con `superseded-by: adr-NNN-slug`. Si relacionado a features → cross-references bidireccionales.

## Bibliographic foundation

- `vault/architect/research/library/nygard-adr.md` — plantilla canónica completa.
- `vault/architect/research/library/bass-software-architecture.md` — qué constituye decisión arquitectónica significativa.

## Full design

`./design.md` — incluye ejemplo completo de ADR-001 sobre ubicación de skills en SEM-IA mismo.

## Limitations

- "Decisión arquitectónica significativa" es subjetivo. Heurísticas ayudan pero no eliminan juicio.
- ADRs requieren disciplina para mantener actualizados.
- ADRs antiguos pueden volverse irrelevantes sin que nadie los marque como `deprecated` — considerar revisión periódica.

## Status lifecycle

**Esta skill produce el ADR con `status: proposed`** (convención Nygard). **NO** setees el status final desde aquí. La transición a `accepted` la aplica recepción al ejecutar `/verify` del WA, leyendo el campo `on-close` del frontmatter del WA. Lifecycle completo del ADR:

| Status | Cuándo |
|---|---|
| `proposed` | Output inicial de esta skill (durante el step) |
| `accepted` | Tras /verify del WA `adr` aprobado |
| `superseded` | Cuando un nuevo ADR lo reemplaza (modificación manual del ADR previo + `superseded-by`) |
| `deprecated` | ADR ya no aplica pero no fue reemplazado |

ADRs **NO entran al backlog** (no tienen status `ready-for-implementation`) — son decisiones, no work items.

## WA mapping

Esta skill se invoca dentro del template **`adr`** (fase `design`). También se invoca como step opcional dentro de templates como `feature-design`, `infra-decision`, `refactor` cuando emerge una decisión arquitectónica significativa durante el WA.
