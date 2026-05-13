---
name: arch-coherence-evaluation
description: "Evaluar si un cambio propuesto (capability, feature, ADR nuevo) es coherente con los ADRs existentes y la arquitectura acordada. Si detecta contradicción, presenta tres opciones operativas (descartar / modificar nivel superior / documentar excepción) — modo arbitraje SEM-IA. Use this skill within feature-viability-review or capability-viability-review when checking against existing ADRs, when SEM-IA enters arbitration mode, or for periodic drift detection."
allowed-tools: Read Glob Grep
materializes-feature: [feature-018-slash-scope-scan, feature-019-slash-verify]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): skill Architect invocada como advisor en scope-scan (feature-018) y sign-off (feature-019). Aplicada en step-3 del WA-005 actual.
---

# Skill: coherence-evaluation (Architect)

## Quick reference

Aplica 5 pasos para evaluar coherencia. Output: reporte de coherencia + recomendación. Si hay contradicción, **NO decide** — presenta 3 opciones al humano (modo arbitraje sec. 11 boceto inicial).

## When to invoke

- Dentro de `feature-viability-review` paso 3.
- Dentro de `capability-viability-review` paso 4.
- **Modo arbitraje** SEM-IA cuando un cambio rompe coherencia.
- Revisión periódica de ADRs vs. estado actual del código (drift detection).

## Inputs

- Cambio propuesto (capability, feature, ADR nuevo, modificación).
- ADRs existentes en `vault/architect/adrs/` (lectura focalizada por dimensiones).
- Subgrafo relevante.

## Process — 5 pasos

### Paso 1 — Identificar ADRs aplicables
Lectura focalizada por dimensiones afectadas.

### Paso 2 — Para cada ADR aplicable, categorizar relación
- **Conforme** — respeta la decisión.
- **Extensión** — añade detalle sin contradecir.
- **Contradicción** — rompe lo decidido. Triggers arbitraje.
- **Supersession** — reemplaza la decisión. Requiere nuevo ADR.

### Paso 3 — Evaluar fitness functions afectadas (Ford)
¿La fitness function sigue cumplible? ¿Hay que añadir fitness function nueva?

### Paso 4 — Si contradicción, presentar las 3 opciones (arbitraje)
Conforme a sec. 11 boceto inicial:

1. **Descartar el cambio.** ADR existente prevalece.
2. **Modificar nivel superior y propagar.** ADR existente obsoleto/erróneo; escribir ADR superseding.
3. **Documentar excepción consciente.** Cambio rompe coherencia con razón válida; documentar en frontmatter (`coherence-exception: adr-NNN`) + ADR breve explicando.

### Paso 5 — Producir reporte estructurado

## Output format

```markdown
## Coherencia evaluada — [cambio]

### ADRs evaluados
- adr-001: ✅ Conforme
- adr-005: ⚠️ Extensión (sugerir actualizar adr-005)
- adr-012: ❌ Contradicción

### Fitness functions afectadas
- ...

### Recomendación
**Para adr-012:** activar arbitraje. 3 opciones presentadas.
```

**Recomendación final**:
1. **Cambio coherente.**
2. **Cambio coherente con extensión sugerida.**
3. **Activar arbitraje.**
4. **Cambio incoherente, no viable.**

## Bibliographic foundation

- `vault/architect/research/library/nygard-adr.md` — estados de ADR (`accepted`, `superseded`, `deprecated`).
- `vault/architect/research/library/martin-clean-architecture.md` — Dependency Rule como regla de coherencia.
- `vault/architect/research/library/ford-evolutionary-architecture.md` — fitness functions como mecanismo de coherencia automatizada.

## Full design

`./design.md` — incluye ejemplo aplicado (feature que requiere API externa sin caché violando ADR-007).

## Limitations

- Detección depende de ADRs bien redactados.
- En proyectos sin ADRs, la skill es predictiva (evalúa contra principios generales: Clean Architecture, Ousterhout).
- Coherence drift requiere revisión activa que vault-cli puede automatizar parcialmente.

## Status lifecycle

Si esta skill produce un report formal: `status: draft` inicial → `active` vía `on-close`. Si emite veredicto inline (caso common dentro de viability-review), output se integra en el review padre sin lifecycle propio.

## WA mapping

Esta skill se invoca dentro de:
- **`feature-design`** (paso 3 de `feature-viability-review`).
- **`capability-creation`** (paso 4 de `capability-viability-review`).
- **Modo arbitraje** SEM-IA: cuando recepción detecta posible contradicción con grafo durante scope-scan o post-step scope-scan, esta skill ayuda a evaluar antes de presentar las 3 opciones al humano.
- On-demand desde sesión Architect para revisión periódica de drift.
