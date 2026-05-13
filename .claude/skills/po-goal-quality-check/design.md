---
type: research
id: borrador-skill-po-strategy-goal-quality-check
title: "Borrador de skill: product-owner.strategy.goal-quality-check"
status: draft
created: 2026-04-30
author: pelayo
tags: [skill-borrador, product-owner, strategy, goal-validation, quality-check, happy-path]
---

# Borrador de skill: product-owner.strategy.goal-quality-check

> **Estado: borrador refinado.** Versión inicial creada durante el primer pase de inception. Refinada como parte del bootstrap manual de skills core. Materialización en `.claude/skills/product-owner/strategy/goal-quality-check/SKILL.md` durante Fase 5.

## Propósito

Evaluar si un goal concreto cumple los criterios de calidad establecidos por la literatura sobre product management adaptados al modelo SEM-IA: si es resultado medible, si materializa la visión, si es controlable, si tiene altitud correcta y si es distinto de los demás goals.

## Cuándo se invoca

- **Trigger principal:** durante `inception-orchestration`, paso 3, sobre cada goal candidato.
- **Trigger secundario:** durante `strategy-review` periódico para detectar derivas.
- **Trigger asistencial:** cuando un descubrimiento bottom-up cuestiona un goal (entrada a `vision-realignment`).

## Inputs

- El nodo del goal a evaluar: `vault/product-owner/strategy/goal-N.md` (frontmatter + Resultado esperado + Métricas + Conexión con la visión).
- Visión padre: `vault/product-owner/strategy/vision.md` (enunciado, contexto, horizonte).
- Goals hermanos: los demás goals del vault para verificar distinción.
- Library: [[library-doerr-okrs]], [[library-doran-smart]], [[library-cagan-product-vision]].

## Proceso — los 6 tests

### Test 1: ¿Resultado o actividad? (SMART · Specific)
- **Resultado:** describe un estado del mundo cuando el goal se cumple.
- **Actividad:** describe acciones a hacer.
- ✅ "El framework se sostiene operativamente"
- ❌ "Construir SEM-IA usando SEM-IA"

### Test 2: ¿Es medible? (SMART · Measurable; OKR · Key Results)
- Hay métrica explícita o derivable.
- La métrica tiene baseline, referencia o criterio binario.
- Las métricas pueden ser de **cumplimiento** (controlable) o de **señal** (aspiracional, ver Test 4).
- ✅ "% del desarrollo bajo SEM-IA ≥ 90%"
- ❌ "El framework es bueno"

### Test 3: ¿Materializa la visión? (Cagan)
- El goal debe ser derivable de un aspecto específico de la visión.
- Pregunta: *"¿Qué afirmación de la visión se vuelve verificable cuando este goal se cumple?"*

### Test 4: ¿Controlable o aspiracional? (Lean)
- **Controlable:** depende de las acciones del propio framework.
- **Aspiracional:** depende de factores externos (mercado, comunidad, tiempo).
- Las dos categorías son legítimas pero **deben marcarse explícitamente** porque tienen métricas distintas.

### Test 5: ¿Altitud correcta? (Pyramid model SEM-IA)
| Altitud | Indicador | Acción |
|---|---|---|
| Demasiado alto | Repite la visión o expresa valor abstracto | Subir contenido a visión, eliminar goal |
| Demasiado bajo | Describe habilidad del producto | Bajar a capability |
| Demasiado bajo | Actividad concreta con fecha | Bajar a milestone del roadmap |
| ✅ Correcta | Resultado intermedio entre visión y capability | Mantener |

### Test 6: ¿Distinto de los demás goals? (No solapamiento)
- Comparar con goals hermanos.
- Si solapa significativamente → fundir, redefinir, o eliminar redundante.

## Outputs

Para cada test: ✅ pass / ⚠️ frontera / ❌ fail + diagnóstico breve.

**Recomendación final** entre seis:

1. **Mantener tal cual.**
2. **Reformular el enunciado** (cambia redacción, mantiene goal y posición).
3. **Mover a milestone del roadmap** (era actividad).
4. **Mover a capability** (era habilidad del producto).
5. **Fundir con otro goal** (solapamiento detectado).
6. **Eliminar** (no aporta valor diferenciado o no materializa la visión).

## Fundamento bibliográfico

- [[library-doerr-okrs]] — Objectives + Key Results, formato y target.
- [[library-doran-smart]] — SMART criteria original (1981).
- [[library-cagan-product-vision]] — alineación con visión durable.

## Ejemplo aplicado a goal-1 (versión iterada con el usuario)

**Goal evaluado:** *"SEM-IA es operativamente auto-sostenible"*

| Test | Veredicto | Diagnóstico |
|---|---|---|
| 1. Resultado o actividad? | ✅ | "Es operativamente auto-sostenible" describe propiedad, no acción. |
| 2. Medible? | ✅ | "% desarrollo bajo SEM-IA" + binario "estabilización funcional alcanzada". |
| 3. Materializa visión? | ✅ | Sin auto-sostenibilidad operativa, "infraestructura por defecto" no es defendible. |
| 4. Controlable? | ✅ | Depende solo del propio desarrollo. |
| 5. Altitud correcta? | ✅ | Resultado del producto, ni visión ni feature. |
| 6. Distinto? | ✅ | No solapa con goal-2, 3, 4. |

**Recomendación:** Mantener tal cual.

## Ejemplo negativo

**Goal candidato:** *"Tener documentación buena"*

| Test | Veredicto |
|---|---|
| 1. Resultado o actividad? | ⚠️ frontera — "tener" es resultado pero "buena" es ambiguo |
| 2. Medible? | ❌ "buena" no es métrica |
| 3. Materializa visión? | ⚠️ posiblemente, vía CAP-7 articulación pública |
| 4. Controlable? | ✅ |
| 5. Altitud correcta? | ⚠️ podría ser sub-goal o capability |
| 6. Distinto? | ✅ |

**Recomendación:** Reformular como goal medible (ej. *"Documentación pública completa antes de defensa TFM, suficiente para que un equipo externo pueda adoptar SEM-IA"*) o mover a capability bajo goal-3.

## Limitaciones

- Los tests no son ortogonales — fallar uno suele implicar fallar otros.
- La frontera entre "controlable" y "aspiracional" puede ser difusa. Forzar la decisión y marcarla explícitamente.
- La skill rechaza pero no inventa goals. Si rechaza, devuelve la conversación al humano para reformular o regenerar.
