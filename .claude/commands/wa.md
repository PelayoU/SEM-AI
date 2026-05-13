---
description: "Detalle del Working Agreement activo en el contexto actual, con steps y status"
---

Lee el WA activo relevante para la sesión actual y preséntalo de forma estructurada con steps. Útil cuando estás trabajando en una sesión de rol y quieres recordar tu scope o saber en qué step estás.

## Pasos

1. **Identifica el contexto.**
   - Working directory actual.
   - Rol cargado por CLAUDE.md aplicable.

2. **Localiza el WA aplicable.**
   - Lista archivos `vault/shared/sessions/active/*.md`.
   - Si hay UN solo WA activo: ese es el aplicable.
   - Si hay varios: filtra por `steps` cuyo `active-role` con status `pending` o `in-progress` matchea el rol del directorio actual. Si hay varios candidatos, pregúntale al humano cuál.
   - Si no hay WAs activos: díselo al humano y termina.

3. **Lee el WA y presenta su contenido estructurado** (formato abajo).

## Output format

```
## Working Agreement · <id>

**Outcome-type:** <outcome-type> · **Fase SDLC:** <phase> · **Estado:** <status>
**Creado:** <created>

### Objetivo
<objective>

### Relacionado con
- Feature: <related-feature o "n/a">
- Capability: <related-capability o "n/a">
- Spec: <related-spec o "n/a">
- ADR: <related-adr o "n/a">

### Consume del backlog (si aplica)
<si el WA tiene `consumes`: "Nodo consumido: <node-id> · Status requerido: <required-status> · Verificado: <verified-at>">
<si no: "n/a (template no consume nodo del backlog)">

### Efectos al cierre (on-close)
<si el WA tiene `on-close`: lista de transiciones de status sobre nodos del grafo>
<si no: "Ninguno">

### Outcome-types válidos por fase
(Recordatorio del catálogo en `vault/shared/governance/workflows.md`)
- **discovery**: vision-creation | capability-creation | goal-definition
- **design**: feature-design | adr | threat-model
- **implementation**: feature-build | bugfix | refactor
- **operations**: pipeline-change | infra-decision | observability-instrument
- **meta**: doc-edit | trivial

### Dimensiones afectadas
<dimensions-affected>

### Participantes (aportaron en scope-scan)
<participants>

### Steps (workflow)

| # | Status | Active-role | Phase | Purpose |
|---|--------|-------------|-------|---------|
| 1 | <icon> | <rol> | <fase> | <purpose corto> |
| 2 | <icon> | <rol> | <fase> | <purpose corto> |
| ... |

(icon: ✓ done | → in-progress | ☐ pending)

**Step actual:** Step N — <rol> — <purpose>

### Scope autorizado
- <path 1>

### Scope prohibido
- <path 1>

### Cierre
- Verificadores requeridos al cierre: <verifiers-required>
- Closure-criteria:
  - [<check>] <criterio 1>
  - [<check>] <criterio 2>

### Progreso registrado
<contenido del WA en sección Progreso, si existe>

### Próxima acción
<si hay step pending: "Step N pending para <rol>. Abre: cd vault/<rol> && claude">
<si todos done: "Todos los steps completados. Vuelve a la sesión PO (modo recepción) para /verify — comando: npm run sem">
```

Para los `closure-criteria`, marca `[x]` los que **observas que ya están cumplidos** según el estado actual del vault (lectura focalizada — no inventes). Marca `[ ]` los pendientes. Si no puedes evaluar uno determinísticamente, marca `[?]` y explica por qué.

## Cuándo es útil

- Estás trabajando en una sesión de rol y necesitas releer tu step + scope sin abrir el archivo.
- Quieres saber qué viene después de tu step.
- Antes de tomar una decisión que podría salirse del scope.
- Para evaluar si el WA está listo para cierre (`/verify` después).
