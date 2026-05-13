---
type: research
id: borrador-skill-architect-coherence-evaluation
title: "Borrador de skill: architect.coherence-evaluation"
status: draft
created: 2026-04-30
author: pelayo
tags: [skill-borrador, architect, coherence, adr, happy-path]
---

# Borrador de skill: architect.coherence-evaluation

> **Estado: borrador.** Materialización en `.claude/skills/architect/coherence-evaluation/SKILL.md`.

## Propósito

Evaluar si un cambio propuesto (capability, feature, ADR nuevo) es **coherente con los ADRs existentes** y con la arquitectura acordada del proyecto. Si detecta incoherencia, presenta tres opciones operativas (descartar / modificar nivel superior / documentar excepción) — alineado con el modo arbitraje de SEM-IA.

## Cuándo se invoca

- **Trigger principal:** dentro de `feature-viability-review` paso 3 — verificación contra ADRs.
- **Trigger principal:** dentro de `capability-viability-review` paso 4 — verificación de coherencia con arquitectura existente.
- **Trigger secundario:** modo **arbitraje** (sec. 11 boceto inicial) cuando un cambio rompe coherencia detectada.
- **Trigger asistencial:** revisión periódica de ADRs vs. estado actual del código (drift detection).

## Inputs

- Cambio propuesto (capability, feature, ADR nuevo, o modificación de nodo existente).
- Todos los ADRs existentes en `vault/architect/adrs/` (lectura focalizada por dimensiones afectadas).
- Subgrafo relevante del vault (capability ascendente, features hermanas si aplica).
- Library: [[library-nygard-adr]], [[library-martin-clean-architecture]], [[library-ford-evolutionary-architecture]].

## Proceso — 5 pasos

### Paso 1 — Identificar ADRs aplicables
Lectura focalizada de ADRs por dimensiones declaradas en el cambio propuesto. Heurística: si el cambio toca dimensión `data`, leer ADRs con `dimensions-affected: [data, ...]`.

### Paso 2 — Para cada ADR aplicable, verificar coherencia
Cuatro categorías de relación posible:

| Relación | Significado |
|---|---|
| **Conforme** | El cambio respeta la decisión del ADR. Sigue el patrón establecido. |
| **Extensión** | El cambio añade detalle al ADR sin contradecirlo. ADR sigue vigente. |
| **Contradicción** | El cambio rompe lo decidido en el ADR. **Triggers arbitraje.** |
| **Supersession** | El cambio reemplaza la decisión del ADR. **Requiere nuevo ADR superseding.** |

### Paso 3 — Evaluar fitness functions afectadas (Ford et al.)
Si el cambio toca propiedades arquitectónicas protegidas por fitness functions:
- ¿La fitness function sigue siendo cumplible después del cambio?
- ¿Hay que añadir fitness function nueva para proteger una propiedad nueva?

### Paso 4 — Si hay contradicción, presentar las 3 opciones (modo arbitraje)
Conforme a sec. 11 boceto inicial:

1. **Descartar el cambio.** El ADR existente prevalece. El cambio se rechaza.
2. **Modificar nivel superior y propagar.** El ADR existente está obsoleto o erróneo; se escribe ADR superseding y se propagan consecuencias a todos los nodos afectados.
3. **Documentar excepción consciente.** El cambio rompe la coherencia con razón válida; se documenta como excepción explícita en el frontmatter del nodo (`coherence-exception: adr-NNN`) y en un nuevo ADR breve que explica por qué.

### Paso 5 — Producir reporte
Estructura:

```markdown
## Coherencia evaluada — [cambio propuesto]

### ADRs evaluados
- adr-001: ✅ Conforme
- adr-005: ⚠️ Extensión (sugerir actualizar adr-005 con nuevo detalle)
- adr-012: ❌ Contradicción

### Fitness functions afectadas
- vault check coverage: sigue cumplible
- ningún acoplamiento problemático detectado

### Recomendación
**Para adr-012:** activar arbitraje con humano. Tres opciones presentadas.
**Para adr-005:** sugerir actualización (no requiere arbitraje, es extensión).
```

## Output format

Reporte estructurado anterior + (si hay arbitraje) presentación clara de las 3 opciones al humano. La skill **NO toma la decisión** — la presenta y espera respuesta del humano.

**Recomendación final** entre cuatro:
1. **Cambio coherente** — todos los ADRs conformes o extensiones.
2. **Cambio coherente con extensión sugerida** — actualizar ADR existente.
3. **Activar arbitraje** — contradicción detectada, presentar 3 opciones.
4. **Cambio incoherente, no viable** — requiere revisar capability/feature antes de continuar.

## Fundamento bibliográfico

- [[library-nygard-adr]] — estados de ADR (`accepted`, `superseded`, `deprecated`).
- [[library-martin-clean-architecture]] — Dependency Rule como regla de coherencia operativa.
- [[library-ford-evolutionary-architecture]] — fitness functions como mecanismo de coherencia automatizada.

## Ejemplo aplicado

**Cambio propuesto:** feature nueva que requiere conexión externa a una API de terceros, sin caché.

ADRs aplicables:
- adr-007: "Toda dependencia externa pasa por capa de adapter con caché de 5 min mínimo".

| ADR | Relación | Diagnóstico |
|---|---|---|
| adr-007 | ❌ Contradicción | Feature propone API call directo sin caché. Viola la decisión. |

**Recomendación:** Activar arbitraje con humano. Presentar 3 opciones:

1. **Descartar:** rechazar la feature como está. PO la reformula con caché.
2. **Modificar adr-007:** la API de este caso es de tiempo real (no se puede cachear); revisar adr-007 para incluir excepción a APIs de tiempo real, escribir ADR superseding.
3. **Documentar excepción consciente:** mantener adr-007 vigente para todo lo demás; documentar esta feature como excepción explícita con razón en su frontmatter.

## Limitaciones

- La detección de contradicción depende de leer y entender ADRs. ADRs mal redactados producen ambigüedad.
- Para proyectos sin ADRs (recién bootstrapeados), la skill devuelve "no hay ADRs aplicables" y la coherencia se evalúa contra principios generales (Clean Architecture, Ousterhout). Predictivo más que descriptivo.
- Coherence drift (= ADRs aceptados que ya nadie respeta en código) requiere revisión activa que vault-cli puede automatizar parcialmente, pero no exhaustivamente.
