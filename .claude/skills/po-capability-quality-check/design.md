---
type: research
id: borrador-skill-po-strategy-capability-quality-check
title: "Borrador de skill: product-owner.strategy.capability-quality-check"
status: draft
created: 2026-04-30
author: pelayo
tags: [skill-borrador, product-owner, strategy, capability, quality-check, happy-path]
---

# Borrador de skill: product-owner.strategy.capability-quality-check

> **Estado: borrador.** Materialización en `.claude/skills/product-owner/strategy/capability-quality-check/SKILL.md` durante Fase 5.

## Propósito

Evaluar si una capability cumple los criterios de calidad: es habilidad (no feature ni actividad), sirve a goals concretos (parent y cross-links bien declarados), no solapa con otras capabilities, y es coherente con la guiding policy estratégica de la visión.

## Cuándo se invoca

- **Trigger principal:** durante `inception-orchestration`, paso 4, sobre cada capability candidata.
- **Trigger secundario:** durante `strategy-review` periódico.
- **Trigger asistencial:** cuando se propone una capability nueva fuera de inception.

## Inputs

- Capability candidata (frontmatter + descripción + justificación).
- `vault/product-owner/strategy/vision.md` (para evaluar coherencia con guiding policy).
- `vault/product-owner/strategy/goal-N.md` (para evaluar parent y cross-links).
- Otras capabilities ya existentes (para detectar solapamientos).
- Library: [[library-rumelt-good-strategy]], [[library-torres-continuous-discovery]], [[library-cagan-product-vision]].

## Proceso — los 6 tests

### Test 1: ¿Habilidad o feature/actividad?
- **Capability:** habilidad de alto nivel del producto. Forma típica: *"El sistema puede X"*.
- **Feature:** materialización concreta de una habilidad. Forma típica: *"Endpoint Y", "botón Z"*.
- **Actividad:** acción a hacer. Forma típica: *"Construir X"*.
- ✅ Habilidad: "Memoria compartida humano-agentes en grafo declarativo".
- ❌ Feature: "vault-cli con comando vault validate".
- ❌ Actividad: "Implementar el vault".

### Test 2: ¿Tiene parent claro?
- ¿El goal padre está identificado y existe?
- ¿La capability sirve genuinamente a ese goal, o cuelga ahí por conveniencia?
- Pregunta operativa: si el goal padre se eliminara, ¿esta capability seguiría siendo necesaria? Si no → bien colocada. Si sí → reconsiderar parent.

### Test 3: ¿Sirve a la guiding policy de la visión? (Rumelt)
- La capability debe contribuir al kernel estratégico (diagnosis → guiding policy → coherent actions).
- Pregunta: ¿esta capability es una "coherent action" alineada con la guiding policy, o una idea desconectada?

### Test 4: ¿Distinta de otras capabilities? (No solapamiento)
- Comparar con capabilities hermanas y de otras goals.
- Si solapa significativamente → fundir, redefinir scope, o eliminar redundante.
- Pregunta: ¿hay otra capability que cubra el mismo terreno conceptual?

### Test 5: ¿Cross-links explícitos?
- ¿Tiene `also-relates-to` declarando a qué otros goals sirve?
- ¿Tiene `dimensions-affected` declarando qué dimensiones del producto holístico toca?
- Si las cross-links están vacías y la capability claramente toca varias dimensiones, falta declaración (= grafo incompleto).

### Test 6: ¿Decomponible en features tangibles?
- ¿Se pueden imaginar 2-5 features concretas que materialicen esta capability?
- Si no → demasiado vaga o demasiado abstracta. Reconsiderar.

## Outputs

Para cada test: ✅ pass / ⚠️ frontera / ❌ fail + diagnóstico.

**Recomendación final** entre seis:

1. **Aprobar tal cual.**
2. **Reformular el enunciado** (cambia redacción, mantiene scope).
3. **Mover a feature** (era una feature, no una capability).
4. **Mover a goal** (subió de altitud, debería ser goal o sub-goal).
5. **Fundir con capability X** (solapamiento detectado).
6. **Eliminar.**

## Fundamento bibliográfico

- [[library-rumelt-good-strategy]] — capability como "coherent action" del kernel estratégico.
- [[library-torres-continuous-discovery]] — capability como nodo en Opportunity Solution Tree (oportunidad → solución).
- [[library-cagan-product-vision]] — capability debe alinear con visión durable.

## Ejemplos

### Ejemplo positivo
**Capability:** "Custodios homólogos por dimensión con catálogo extensible"
**Parent:** goal-1 (auto-sostenibilidad)
**also-relates-to:** [goal-2, goal-3, goal-4]
**dimensions-affected:** [strategy, technical]

| Test | Veredicto |
|---|---|
| Habilidad? | ✅ "El sistema tiene custodios por dimensión" |
| Parent claro? | ✅ goal-1 — sin custodios el framework no se sostiene |
| Sirve a guiding policy? | ✅ "absorber el coste estructuralmente" requiere custodios |
| Distinta? | ✅ no solapa con CAP-2 (memoria), CAP-3 (WAs), etc. |
| Cross-links? | ✅ declarados a goal-2 (extensibilidad → portabilidad), goal-3 (formulación canónica), goal-4 (custodios = absorción de coste) |
| Decomponible? | ✅ features: catálogo de roles core, mecanismo de extensión, integración con Claude Code, prompts robustos, etc. |

**Recomendación:** Aprobar tal cual.

### Ejemplo negativo
**Capability candidata:** "Implementar vault-cli para CI"

| Test | Veredicto |
|---|---|
| Habilidad? | ❌ es una feature concreta (una herramienta CLI específica) |
| Parent claro? | ⚠️ podría colgar de varios goals |
| Sirve a guiding policy? | ⚠️ apoya pero no materializa |
| Distinta? | ⚠️ probablemente parte de CAP-4 governance estructural |
| Cross-links? | n/a |
| Decomponible? | ❌ ya es la feature; no hay sub-features |

**Recomendación:** Mover a feature dentro de CAP-4 governance estructural.

## Limitaciones

- La distinción capability / feature es la más resbaladiza del modelo. Algunas capabilities pueden parecer features grandes — usar el test "decomponible en 2-5 features" para resolver dudas.
- El ✅ en "no solapamiento" requiere comparar con TODAS las capabilities existentes — el coste sube linealmente con el tamaño del proyecto. En grafos densos, la skill puede pedir lectura focalizada solo a capabilities que toquen dimensiones similares.
