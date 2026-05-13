---
name: po-capability-derivation
description: "Derivar capabilities desde un goal aprobado usando Opportunity Solution Tree (Torres) más coherencia con guiding policy (Rumelt) y JTBD (Christensen). Genera lista priorizada de capabilities candidatas con parent, cross-links y dimensiones tentativas. Use this skill during inception (after goals are approved) or when a new goal needs its set of capabilities."
allowed-tools: Read Glob Grep
materializes-feature: [feature-038-po-modo-1]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): skill estratégica invocada por PO Modo 1 cuando outcome-type = capability-creation. También aplicada en WA-2026-05-12-002 archivado (modo batch reverse-engineering).
---

# Skill: capability-derivation (Product Owner — lado estratégico)

## Quick reference

Toma un goal aprobado y produce 3-7 capabilities candidatas mediante OST: outcome → oportunidades → soluciones (= capabilities). Filtra por coherencia con guiding policy y detecta overlaps con capabilities existentes.

## When to invoke

- Durante WA `capability-creation` (caso normal) — modo conversacional, después de aprobar goals.

- Cuando un goal nuevo se añade post-inception y necesita sus capabilities.

## Inputs

- Goal padre (frontmatter + resultado + métricas + conexión con visión).
- Visión completa (coherencia top-down).
- Capabilities ya existentes (evitar duplicación).

## Process — 7 pasos

1. **Reformula el goal en lenguaje OST** como outcome de negocio: *"Movemos [métrica] de X a Y"*.
2. **Identifica 3-7 oportunidades** (gaps / pains / necesidades del usuario / adopter). Forma: *"El [usuario] no puede / sufre / necesita X"*.
3. **Genera 2-3 soluciones por oportunidad** (no enamorarse de la primera idea — Torres). Cada solución es candidata a capability. Forma: *"El sistema tiene la habilidad de X"*.
4. **Filtra por coherencia con guiding policy** (Rumelt). Eliminar las que no contribuyen al kernel estratégico.
5. **Detecta overlap con capabilities existentes**. Si solapa → declarar cross-link en la existente, no crear nueva.
6. **Identifica cross-links a otros goals** (`also-relates-to` candidatos).
7. **Aplica `capability-quality-check`** a cada candidata superviviente.

## Output format

- Lista priorizada de capabilities candidatas con:
  - Enunciado (título)
  - Oportunidad que cubre
  - Parent (goal del que derivan)
  - Cross-links candidatos
  - Dimensiones tentativas
- Lista de cross-links a añadir a capabilities existentes.
- Razones explícitas de descarte (auditoría).

## Template del capability file

Cuando una capability candidata supera el filtro Rumelt y `capability-quality-check`, se materializa como nodo del grafo en `vault/product-owner/strategy/cap-NN-<slug>.md`. Esta sección define el **template canónico** del archivo — frontmatter + estructura del cuerpo — que toda capability debe respetar.

> **Por qué este template vive aquí**: `CLAUDE.md` raíz declara *"La estructura de cada tipo de nodo vive inline en la skill que lo crea"*. La skill `capability-derivation` produce nodos de tipo `capability`; por tanto su template vive en este SKILL.md, no en archivo separado. El template emergió como input del WA `wa-2026-05-12-002` (extracción bottom-up de las primeras 10 capabilities de SEM-IA) y se formalizó en `wa-2026-05-12-003` (procesamiento de gaps estructurales — Gap 2).

> **Filosofía del template**: **mínimo con extensiones opcionales**, no rígido. Los campos esenciales son obligatorios; los opcionales se omiten si no aplican. El template emerge de la práctica observada — los 10 capability files `cap-01-...md` a `cap-10-...md` en `vault/product-owner/strategy/` sirven como referencia bibliográfica.

### Frontmatter — campos esenciales

```yaml
type: capability                                  # siempre
id: cap-NN-<slug-corto-descriptivo>               # convención cap-NN- global incremental
title: "<frase clara del job que la capability cubre>"

# Espina dorsal jerárquica
parent: <goal-id-primario>                        # del catálogo de goals (vault/product-owner/strategy/goal-*.md)

# Cross-links del grafo (declarar con criterio, no llenar mecánicamente)
also-relates-to: [<goal-ids cross>]               # otros goals a los que sirve la capability
depends-on: [<cap-ids o feature-ids si aplica>]   # dependencias de otras capabilities (Martin Clean Architecture: dependency inversion)
dimensions-affected: [<lista honesta>]            # NO heredar mecánicamente [product] del goal padre; declarar las dimensiones realmente tocadas
related-adrs: []                                  # vacío hasta que existan ADRs aplicables

# Lifecycle del nodo
status: draft                                     # transición a active la aplica /verify del WA vía on-close
```

### Frontmatter — profundidad bibliográfica (obligatorio)

```yaml
# Madurez operativa del producto (ortogonal al status del nodo)
operational-status: operant | planned             # operant = piezas técnicas ya construidas; planned = capability documentada/aprobada pero sin construir todavía

# Quality attributes implicados (Bass)
qas-bass:
  - <qa-1>     # ej. modifiability, auditability, usability, portability, security, etc.
  - <qa-2>

# Tactics arquitectónicos / de diseño (Bass)
tactics:
  - "<descripción concreta de cómo el sistema implementa el QA>"

# Tradeoffs conscientes — qué se gana, qué se pierde
tradeoffs:
  - "<tradeoff explícito, honesto>"

# Fitness functions Ford — OPCIONAL pero recomendado
# Formalizan los tradeoffs en métricas observables y testables
fitness-functions:
  - "<métrica observable + umbral + cómo se mide>"

# JTBD outcome (Christensen) — formulación del job real del usuario
jtbd-outcome:
  quien: "<persona/rol que tiene el job>"
  job: "<el trabajo concreto que necesita hacer>"
  outcome-esperado: "<resultado que satisface el job>"

# Bibliografía base
fundamento-bibliografico:
  - <autor> — <obra> (<aspecto que aplica>)
```

### Cuerpo del archivo — secciones esenciales

Todo capability file incluye estas secciones, en este orden:

1. **# CAP-NN · `<title>`** — heading principal con id + title.
2. **## Enunciado** — descripción narrativa de qué hace la capability (1-3 párrafos). Lenguaje accesible a lector no-practicante de SEM-IA (legibilidad externa estándar).
3. **## Por qué es capability fuerte (4 criterios)** — aplicar explícitamente los 4 criterios:
   - (a) Habilidad diferenciada del sistema (no feature/actividad).
   - (b) Sirve a goals con métrica clara.
   - (c) Cohesión interna (no colección heterogénea).
   - (d) No es trivialmente subcapability de otra.
4. **## Piezas del bootstrap que la materializan** (si `operational-status: operant`) o **## Piezas previstas (PLANNED — todas/algunas pendientes)** (si `operational-status: planned`) — tabla con columnas `Pieza | Path | Rol en la capability`.
5. **## Relación con goals** — explicación de por qué la capability sirve al parent y a los also-relates-to.
6. **## Criterio observable para futuros `/verify`** — qué debe cumplirse para que una feature descompuesta de esta capability sea verificable objetivamente.

### Cuerpo del archivo — secciones opcionales

Se incluyen si aplican; se omiten si no:

- **## Features candidatas (preview — decomposition completa en WA `feature-design` posterior)** — lista 3-7 bloques naturales de features futuras; NO es decomposition formal (esa la hace `feature-decomposition` en WA dedicado).
- **## Notas / gaps operativos conocidos** — gaps que NO bloquean el cierre como `active` pero quedan documentados para WAs futuros.
- **## Tradeoffs explicados narrativamente** — si los `tradeoffs:` del frontmatter requieren más contexto.

### Reglas de aplicación

1. **Dimensions-affected honesto**: NO heredar mecánicamente `[product]` del goal padre. Si la capability toca `technical`, `usability`, `business`, `security`, `quality`, `operations` realmente, declararlo. Flag clave del Architect en el WA-002: *"capabilities derivadas DEBEN declarar dimensions-affected honestamente"*. Anclaje: Ford fitness functions + Bass QAs aplicados al ámbito real.
2. **Status inicial `draft`**: la transición a `active` la aplica `/verify` del WA `capability-creation` vía `on-close`. NO setees `active` desde la skill.
3. **`operational-status` ortogonal al `status`**: `status` es lifecycle del nodo (draft/active); `operational-status` es madurez operativa del producto (operant/planned). Capability nueva planned se cierra como `status: active` + `operational-status: planned` — está aprobada formalmente pero sin construir.
4. **Capabilities cross-goal**: si una capability sirve a varios goals, declarar `parent: <primario>` + `also-relates-to: [<secundarios>]`. NO duplicar en archivos por cada goal.
5. **Legibilidad estándar**: lenguaje accesible a lector no-practicante (evaluador académico, adopter externo, contributor nuevo). Evitar jerga interna sin glosa al primer uso.

## Bibliographic foundation

- `vault/architect/research/library/torres-continuous-discovery.md` — OST + multiplicidad de soluciones.
- `vault/architect/research/library/rumelt-good-strategy.md` — coherencia con guiding policy.
- `vault/architect/research/library/christensen-jtbd.md` — articulación de oportunidades como jobs.

## Full design

`./design.md` — incluye ejemplo aplicado a goal-1 de SEM-IA + ejemplo de detección de cross-link.

## Limitations

- Generación de oportunidades depende de conocer al usuario. Si especulativo, marcar como assumption test pendiente.
- 2-3 soluciones × 3-7 oportunidades = 9-21 candidatas. Filtrar agresivamente.
- No garantiza completitud — la revisión humana es la red de seguridad.

## Status lifecycle

**Esta skill produce capabilities candidatas con `status: draft`** al escribirlas en el vault. **NO** setees el status final desde aquí. La transición a `status: active` la aplica recepción al `/verify` del WA vía `on-close`.

## WA mapping

Esta skill se invoca dentro del template **`capability-creation`** (fase `discovery`).
