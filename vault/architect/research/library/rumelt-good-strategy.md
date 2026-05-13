---
type: research
id: library-rumelt-good-strategy
title: "Richard Rumelt — Good Strategy / Bad Strategy (Kernel)"
status: draft
created: 2026-04-30
author: pelayo
tags: [library, strategy, kernel, coach]
applicable-roles: [coach, architect]
---

# Richard Rumelt — Good Strategy / Bad Strategy (Kernel)

## Datos bibliográficos

- **Autor:** Richard P. Rumelt (UCLA Anderson School of Management)
- **Obra:** *"Good Strategy / Bad Strategy: The Difference and Why It Matters"* (Crown Business, 2011)
- **Aplicabilidad SEM-IA:** dimensión `strategy` — Coach al evaluar coherencia estratégica; Architect cuando una decisión técnica afecta a la estrategia.

## Tesis central

> *"Good strategy is coherent action backed by analysis of the actual challenge, while bad strategy replaces analysis with buzzwords, confuses goals with strategy, and avoids the hard choice of what not to do."*

La mayoría de "estrategias" en la práctica son **bad strategy**: listas de aspiraciones, slogans, evitan la pregunta dura. La buena estrategia es **identificación honesta del problema + cómo se va a abordar + qué se va a hacer concretamente**.

## El Kernel — los 3 elementos

> *"A good strategy has a logical structure called the kernel, which contains three essential elements: a diagnosis, a guiding policy, and a set of coherent actions."*

### 1. Diagnosis
**Identifica el desafío central**, simplifica la complejidad.

- *"Simplifies complexity by identifying certain aspects as critical and others as secondary."*
- *"The most common cause of bad strategy is a weak diagnosis."*
- Es honestidad sobre dónde está el problema real, no donde es cómodo decir que está.

### 2. Guiding Policy
**Cómo abordar el desafío** identificado en el diagnóstico, sin definir aún qué se hace concretamente.

- Crea ventaja:
  - Anticipando acciones y reacciones de otros.
  - Reduciendo complejidad y ambigüedad.
  - Concentrando esfuerzo en aspectos pivotales.
  - Haciendo que las acciones sean coherentes (que se refuercen, no se cancelen).

### 3. Coherent Actions
**Pasos coordinados** que implementan la guiding policy.

- Coherentes entre sí (no contradicen).
- Concentradas (no dispersas).
- Reflejan las elecciones difíciles (qué se hace y qué se decide NO hacer).

## Características de Bad Strategy

Rumelt identifica los 4 hallmarks de la mala estrategia:

1. **Fluff (palabrería).** Lenguaje pomposo y vacío que disfraza ausencia de pensamiento.
2. **Failure to face the challenge.** No identifica el desafío. No hay diagnóstico real.
3. **Mistaking goals for strategy.** Confunde "queremos crecer 30%" con tener una estrategia.
4. **Bad strategic objectives.** Listas de aspiraciones desconectadas en lugar de objetivos focalizados que sirven a la guiding policy.

## Aplicabilidad a SEM-IA

**Skill `coach.strategy-review`:** el Kernel es el lente principal para evaluar coherencia estratégica del subgrafo (visión → goals → capabilities).

Tests derivados:

1. **¿Hay un diagnóstico claro?** En SEM-IA, el diagnóstico vive en el contexto de la visión: *"la SEM clásica no absorbe el coste específico que la IA introduce... el coste se multiplica en cascada"*. ✅
2. **¿Hay guiding policy?** *"absorber ese coste estructuralmente, manteniendo la autoría humana, convirtiendo la coherencia en propiedad del sistema"*. ✅
3. **¿Las acciones (capabilities) son coherentes con la guiding policy?** Cada capability debe servir a la guiding policy, no a aspiraciones desconectadas. Test: para cada capability, preguntar "¿esta capability sirve a la guiding policy del contexto?".
4. **¿Las capabilities son coherentes entre sí?** ¿Se refuerzan o se contradicen?
5. **¿Hay elecciones explícitas de "qué NO hacer"?** En SEM-IA: *"NO sustituye humanos, NO es un harness, NO es Cucumber, NO es un IDE..."* (sección 28 boceto inicial). ✅

**Skill `coach.capability-prioritization`:** Rumelt invita a concentrar esfuerzo en aspectos pivotales. Las capabilities deben priorizarse por su contribución a la guiding policy, no por orden de aparición.

## Citas que anclan decisiones

> *"The most common cause of bad strategy is a weak diagnosis."*

Aplicable cuando alguien propone goals o capabilities sin haber establecido el diagnóstico. Bloquear y volver al diagnóstico.

> *"Strategy is at least as much about what an organization does not do as it is about what it does."*

Aplicable a `capability-prioritization` y a `feature-quality-check`. Si todo es prioritario, nada es prioritario.

> *"A good strategy works by harnessing power and applying it where it will have the greatest effect."*

Aplicable al roadmap: la secuencia de capabilities debe concentrar esfuerzo donde el efecto es mayor.

## Limitaciones del framework

- Rumelt es analítico, no inspiracional. Combinar con Sinek y Cagan para la dimensión motivacional.
- Útil para **diagnóstico estratégico**. Menos útil para la articulación táctica de features (eso es PO).
