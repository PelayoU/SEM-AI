---
type: goal
id: goal-7-ciclo-vida-producto
title: "Sostener productos de software a escala con ciclo de vida completo"
parent: vision
also-relates-to: [goal-2-output-auditable-multirol, goal-4-rigor-multirol-individual, goal-5-portabilidad]
depends-on: []
dimensions-affected: [product]
status: active
created: 2026-05-10
author: pelayo
nature: aspiracional
---

# Goal-7: Sostener productos de software a escala con ciclo de vida completo

## Resultado esperado

Un producto desarrollado con SEM-IA puede sostener **miles de features**, **años de evolución**, **refactorings**, **pivots de visión**, **gestión de bugs** y **mantenimiento continuo** sin perder coherencia ni trazabilidad. El producto es realmente *real* — no script, no MVP efímero, no vibe coding — y su ciclo de vida completo (discovery → maduro → evolución → deprecación) está cubierto por la infraestructura.

Es la promesa final de SEM-IA: lo que diferencia *trabajar con IA en una infraestructura de gestión* de *prompts ad-hoc* es la capacidad de sostener producto a escala y a lo largo del tiempo.

## Métricas

- **Cumplimiento (controlable, demostrable con SEM-IA mismo):** SEM-IA construido y sostenido con SEM-IA durante ≥ 1 año, acumulando ≥ 100 features sin pérdida de coherencia, con historia trazable de ADRs (incluyendo `superseded` y `deprecated`) y WAs archivados sin gaps.
- **Cumplimiento:** Cobertura del ciclo SDLC completo en templates: `discovery` (vision/goal/capability) + `design` (feature-design/adr/threat-model) + `implementation` (feature-build/bugfix/refactor) + `operations` (pipeline/infra/observability) + `meta` — todas las fases tienen template aplicable.
- **Cumplimiento:** Estados canónicos del nodo cubren ciclo de vida completo: `draft → ready-for-implementation → in-implementation → implemented → deprecated` (+ ADRs: `proposed → accepted → superseded → deprecated`).
- **Señal (aspiracional):** Casos pilot de adopters externos con producto significativo (≥ 100 features, ≥ 1 año de uso continuo).

## Conexión con la visión

Materializa el lema final del enunciado — *"para construir productos reales con ciclo de vida completo"* — y el tercer párrafo del contexto:

> *"Esta infraestructura permite construir productos reales con ciclo de vida completo — miles de features, años de evolución, refactorings, pivots de visión y mantenimiento, sostenibles porque cada decisión es trazable y cada cambio verificable."*

Sin este goal, el resto de goals describen propiedades operativas (auditabilidad, rigor, portabilidad) pero la promesa última de SEM-IA queda implícita. Con este goal, el alcance es explícito: SEM-IA es para productos *reales* con vida larga, no para experimentos puntuales.

## Naturaleza del goal

**Aspiracional** — la portabilidad técnica del marco que sostiene el ciclo de vida es controlable (templates, estados, cross-links están construidos), pero la **demostración real** requiere tiempo (≥ 1 año) y adopción de pilots externos. Las métricas se separan en cumplimiento (controlable) y señal (depende de tiempo + adopción).

## Fundamento bibliográfico

- **Cagan — *Inspired*.** Visión durable 5-10 años requiere goals que articulen el alcance del producto, no solo de los componentes.
- **Ford et al. — *Building Evolutionary Architectures*.** Fitness functions y arquitectura evolutiva como fundamento de productos sostenibles a años vista.
- **Nygard — ADRs.** Trazabilidad histórica de decisiones técnicas como condición de productos con ciclo de vida largo (ADRs `superseded` documentan la evolución).
- **Patton — *User Story Mapping*.** Slicing por release y narrative flow como estructura para productos que crecen continuamente.
