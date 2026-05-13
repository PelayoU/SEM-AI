---
type: research
id: borrador-skill-po-strategy-vision-quality-check
title: "Borrador de skill: product-owner.strategy.vision-quality-check"
status: draft
created: 2026-04-30
author: pelayo
tags: [skill-borrador, product-owner, strategy, vision, quality-check, happy-path]
---

# Borrador de skill: product-owner.strategy.vision-quality-check

> **Estado: borrador.** Materialización en `.claude/skills/product-owner/strategy/vision-quality-check/SKILL.md` durante Fase 5.

## Propósito

Evaluar si un enunciado de visión cumple criterios de calidad establecidos por la literatura de product management adaptados al modelo SEM-IA: customer-centricity, durabilidad, articulación del propósito, ambición anclada, distinción entre WHY y WHAT.

## Cuándo se invoca

- **Trigger principal:** durante `inception-orchestration`, paso 2, sobre cada enunciado candidato de visión.
- **Trigger secundario:** durante `vision-realignment` (skill later), cuando un descubrimiento bottom-up cuestiona la visión actual.
- **Trigger asistencial:** humano pide revisión explícita: *"revisa la visión actual"*.

## Inputs

- Enunciado de visión a evaluar (string).
- Opcional: `vault/product-owner/strategy/vision.md` actual completo (con contexto y horizonte).
- Library: [[library-cagan-product-vision]], [[library-sinek-start-with-why]], [[library-rumelt-good-strategy]], [[library-christensen-jtbd]].

## Proceso — los 7 tests

### Test 1: Customer-centricity (Cagan)
- ¿La visión describe **un cambio en la vida del usuario / cliente / adopter**, o describe el producto?
- ✅ "Hacer que producir software con IA sea tan riguroso como sin ella" (cliente-centric).
- ❌ "Construir un framework con agentes" (producto-centric).

### Test 2: Magnitud (Cagan)
- ¿Es **lo suficientemente grande para importar**? Una mejora incremental NO es visión.
- Pregunta operativa: ¿el equipo se entusiasma o suena a tarea?

### Test 3: Inspiracional / emocional (Sinek + Cagan)
- ¿Conecta con un **propósito** (Why)?
- ¿Toca lo emocional (no solo lógico)?
- Pregunta: ¿alguien se uniría al proyecto por leerla, o solo entendería qué se hace?

### Test 4: Durabilidad (Cagan)
- ¿Tiene **horizonte de 5-10 años**? Si la visión expira en 1 año, es goal disfrazado.
- Si los detalles tecnológicos cambian, ¿la visión sigue siendo relevante?

### Test 5: Ambición anclada (Cagan)
- *"If you could truly validate a vision, then your vision probably isn't ambitious enough."*
- ¿Es **stretch goal pero no fantasía**?
- Pregunta: ¿hay path plausible aunque difícil?

### Test 6: Why ≠ What (Sinek)
- ¿La visión articula el **propósito** o solo el producto?
- Una visión 100% What es débil. Una visión que combina Why + comprime el cómo es fuerte.
- Si solo dice qué se construye sin el por qué, falla.

### Test 7: Job articulado (JTBD - opcional)
- ¿Se identifica el **job que el cliente está intentando hacer** y que la visión habilita?
- Útil pero no obligatorio para visión a nivel cúspide.

## Outputs

Para cada test: ✅ pass / ⚠️ frontera / ❌ fail + diagnóstico de una línea.

**Recomendación final** entre cinco:

1. **Aprobar.** Pasa todos los tests críticos.
2. **Reformular** (cambia redacción, mantiene espíritu).
3. **Profundizar contexto** (la visión está bien pero el contexto necesita articular el WHY).
4. **Rehacer** (no captura el propósito; volver a paso 2 de inception-orchestration).
5. **Subir altitud** (lo que se ofrece es goal, no visión; está demasiado bajo).

## Fundamento bibliográfico

- [[library-cagan-product-vision]] — principio guía. 10 principios de Cagan + 6 características de visión sana.
- [[library-sinek-start-with-why]] — Golden Circle como criterio de articulación.
- [[library-rumelt-good-strategy]] — la visión debe servir como diagnosis del kernel estratégico.
- [[library-christensen-jtbd]] — opcional, articulación del job del cliente.

## Ejemplos

### Ejemplo positivo
*"SEM-IA es la infraestructura organizacional por defecto para producir software con IA."*

| Test | Veredicto |
|---|---|
| Customer-centric | ✅ implícito (mejora la vida de equipos / desarrolladores) |
| Magnitud | ✅ "infraestructura por defecto" es ambicioso |
| Inspiracional | ⚠️ frontera — funcional pero el contexto recupera el por qué |
| Durabilidad | ✅ 5-10 años plausibles |
| Ambición anclada | ✅ ambicioso pero validable |
| Why ≠ What | ⚠️ enunciado lee más What; contexto compensa |
| JTBD | ✅ implícito (job: producir software con IA con rigor) |

**Recomendación:** Aprobar con observación — el enunciado es operativo y sólido, pero el WHY queda en el contexto, no en el enunciado mismo. Aceptable como cúspide; el contexto compensa.

### Ejemplo negativo (visión floja)
*"Construir un framework con agentes para usar IA mejor."*

| Test | Veredicto |
|---|---|
| Customer-centric | ❌ producto-centric |
| Magnitud | ❌ "usar IA mejor" es vago |
| Inspiracional | ❌ no inspira nada |
| Durabilidad | ⚠️ podría durar pero no marca dirección |
| Ambición anclada | ❌ es tarea, no visión |
| Why ≠ What | ❌ todo What |
| JTBD | ❌ ningún job articulado |

**Recomendación:** Rehacer. Volver al paso 2 de inception-orchestration con preguntas Sinek (Why → How → What).

## Limitaciones

- Los 7 tests no son ortogonales — fallar uno suele implicar fallar otros relacionados. La recomendación debe sintetizar, no listar mecánicamente.
- "Inspiracional" tiene componente subjetivo. El humano del proyecto es el juez último.
- La skill no inventa visiones. Solo evalúa. Si rechaza, devuelve la conversación al humano para reformular.
