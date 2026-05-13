---
type: research
id: borrador-skill-po-feature-quality-check
title: "Borrador de skill: product-owner.feature-quality-check"
status: draft
created: 2026-04-30
author: pelayo
tags: [skill-borrador, product-owner, feature, quality-check, happy-path]
---

# Borrador de skill: product-owner.feature-quality-check

> **Estado: borrador.** Materialización en `.claude/skills/product-owner/feature-quality-check/SKILL.md` durante Fase 5.

## Propósito

Validar que una feature está completa y consistente antes de cerrarla / aprobarla para implementación. Aplica:
- **INVEST a las stories** (Cohn) que componen la feature.
- **Cobertura de AC** (cada AC tiene Scenario en spec; Adzic).
- **Coherencia con la capability padre y los goals ascendentes.**
- **Cross-links declarados** (depends-on, related-adrs, dimensions-affected).
- **Trazabilidad operativa** (frontmatter completo, código a modificar identificado).

## Cuándo se invoca

- **Trigger principal:** el PO va a cerrar el WA de discovery / spec-writing y necesita validación final.
- **Trigger secundario:** revisión retrospectiva de una feature antes de empezar implementación.
- **Trigger en CI:** automatizable parcialmente vía vault-cli (campos del frontmatter, links válidos, AC tienen Scenario).

## Inputs

- Feature node: `vault/product-owner/specs/feature-N.md` con frontmatter completo.
- Spec(s) de Gherkin asociadas.
- Stories embebidas o referenciadas.
- Capability padre y goals ascendentes (para coherencia top-down).
- Library: [[library-cohn-user-stories-invest]], [[library-adzic-specification-by-example]], [[library-doran-smart]].

## Proceso — los 7 tests

### Test 1: ¿Frontmatter completo y válido?
- `type`, `id`, `title`, `parent` (capability), `dimensions-affected`, `status`, `created`, `author`.
- `also-relates-to`, `depends-on`, `related-adrs` declarados (pueden estar vacíos pero deben existir).
- Pasa validación de schema.

### Test 2: ¿Stories cumplen INVEST?
Por cada story de la feature, aplicar los 6 tests INVEST:
- **I**ndependent
- **N**egotiable
- **V**aluable
- **E**stimable
- **S**mall
- **T**estable

Si alguna story falla → reformular o descomponer.

### Test 3: ¿Cobertura de AC?
- ¿Cada story tiene su spec en Gherkin?
- ¿Cada AC declarado tiene un Scenario asociado?
- ¿Los identificadores `AC-NX` son consistentes y trazables?

### Test 4: ¿Coherencia con capability padre?
- La feature materializa una pieza concreta de la capability.
- No solapa con otras features de la misma capability (si solapa, fundir).
- No contradice la guiding policy de la visión (Rumelt).

### Test 5: ¿Cross-links coherentes?
- Cada `depends-on` apunta a feature/capability existente.
- Cada `related-adrs` apunta a ADR existente y aplicable.
- `dimensions-affected` está completo: si la feature claramente toca security pero no lo declara, falla.

### Test 6: ¿Trazabilidad operativa?
- ¿Si toca código existente, hay anotación de qué se modificará?
- ¿Si requiere ADR nuevo, está identificado y referenciado?

### Test 7: ¿Tamaño razonable?
- ¿La feature cabe en 1-3 sprints / Working Agreements de implementación?
- Si es mayor → descomponer en sub-features.
- Si es trivial → considerar fusionar con feature hermana.

## Outputs

Para cada test: ✅ pass / ⚠️ frontera / ❌ fail + diagnóstico.

**Recomendación final** entre cinco:

1. **Aprobar para implementación.** Pasa todos los tests críticos.
2. **Refinar puntos específicos.** Pasa la mayoría pero requiere arreglos puntuales (cross-links incompletos, una story no INVEST, etc.).
3. **Volver a discovery.** Faltan AC críticos o examples no se exploraron.
4. **Descomponer.** La feature es demasiado grande para un único ciclo.
5. **Fundir / eliminar.** Solapa con otra feature o no aporta valor diferenciado.

## Fundamento bibliográfico

- [[library-cohn-user-stories-invest]] — INVEST aplicado a stories.
- [[library-adzic-specification-by-example]] — cada AC con Scenario, living documentation.
- [[library-doran-smart]] — los AC individuales pasan SMART.

## Ejemplo aplicado

**Feature:** `feature-skills-po-goal-quality-check` (futura, durante bootstrapping progresivo de SEM-IA mismo)

| Test | Veredicto |
|---|---|
| 1. Frontmatter | ✅ todos los campos presentes y válidos |
| 2. INVEST stories | ✅ las 3 stories pasan (1 ya fue ejemplo en `cohn-user-stories-invest`) |
| 3. Cobertura AC | ⚠️ frontera — Story-A tiene 4 AC, Story-B solo 2 (revisar si suficientes) |
| 4. Coherencia con capability | ✅ cuelga claramente de cap-1-custodios-homologos |
| 5. Cross-links | ✅ depends-on=[feature-base-po], related-adrs=[adr-skill-format] |
| 6. Trazabilidad | ✅ código a modificar identificado |
| 7. Tamaño | ✅ cabe en 2 sprints |

**Recomendación:** Refinar puntos específicos — completar AC de Story-B. Pasa los tests críticos; los warnings son de bookkeeping.

## Limitaciones

- Tests 1, 5, 6 son automatizables vía vault-cli. Tests 2, 3, 4, 7 requieren juicio. La skill consolida ambos.
- "Tamaño razonable" depende del equipo. Lo que es 2 sprints para un equipo es 5 días para otro.
- La skill rechaza pero no completa el trabajo. Si rechaza en Test 3, devuelve a discovery; si rechaza en Test 7, devuelve a feature-decomposition.
