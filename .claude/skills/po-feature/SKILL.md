---
name: po-feature
description: "Descomponer una capability en features (entregables de funcionalidad concreta) y cada feature en stories (formato Cohn, criterios INVEST). Una feature es una pieza de funcionalidad entregable que materializa una capability. Una story es un token para una conversación + criterios de aceptación. Use this skill when decomposing a capability into features, when breaking down a feature into stories, or when validating existing features/stories against criteria."
when_to_use: "El humano quiere descomponer una capability en features, descomponer una feature en stories, o validar features/stories existentes."
---

# po-feature

## Propósito

Descomponer una capability en **features** (pieces of deliverable product functionality) y cada feature en **stories** (cards for conversations, INVEST). Cuarto y quinto nivel del grafo SEM-IA.

## Estructura del nodo

Estructura del archivo en:
- `_obsidian/templates/feature.md` — para features.
- `_obsidian/templates/story.md` — para stories.

Léelos antes de crear o editar.

## Definición operativa (canónica SEM-IA literal)

> *"Features/stories: What is designed and implemented to deliver capabilities. Are pieces of deliverable product functionality."*

Features y stories están al MISMO nivel jerárquico en el grafo SEM-IA: ambos son **piezas entregables de funcionalidad**. La diferencia operativa:

- **Feature**: pieza de funcionalidad coherente del producto, suele agrupar varias stories.
- **Story**: thin slice ejecutable + token para conversación, criterios INVEST.

## Stories: formato y filosofía

> *"Stories are for telling. A story is a token for a conversation."* — Kent Beck (origen, late 1990s).

**Template canónico (Cohn)**:

```
As <user role>
I want to <goal>
So that <benefit>
```

**Filosofía Patton/Comakers**:
- Las stories no son spec completa; son **tokens para conversaciones** que producen shared understanding.
- *"Shared documents are NOT shared understanding."* — la documentación es memorando de la conversación, no reemplaza la conversación.
- Vacation Photos metaphor: los modelos/dibujos/notas son mementos para recordar la conversación.

## Criterios INVEST (literal Cohn/Wake)

Aplicables a cada story:

1. **Independent** — implementable sin depender de stories no construidas (relax si dependencia técnica real existe).
2. **Negotiable** — el detalle del cómo es negociable; el qué y por qué no.
3. **Valuable** — entrega valor a un stakeholder (usuario, negocio, equipo).
4. **Estimable** — el equipo puede estimar tamaño con razonable aproximación. Si no se puede estimar, falta discovery.
5. **Small** (sized appropriately) — cabe en una iteración corta. Si es muy grande → epic → descompone.
6. **Testable** — hay AC derivables. Si no es testeable, falta especificación.

## Criterios para features

1. **Entrega outcome experiencial**: la feature produce algo que el usuario percibe/usa. ❌ *"Capa de cache Redis"* (capa técnica). ✅ *"El dashboard carga en <1s"* (outcome perceptible).
2. **Cuelga de capability clara**: parent identificado.
3. **Tamaño razonable**: 2-7 stories aproximadamente. Si no, repartir o agrupar.
4. **Cross-links declarados**: `dimensions-affected`, `depends-on` cuando aplique.

## User Story Mapping (Patton)

Para descomponer una capability en features, el método canónico de Patton es **User Story Mapping**. Estructura:

```
Epic (Activity)  ←  Theme (Task)  ←  Story (Sub-task)
```

**Story Map Process (5 pasos)**:

1. **Frame** — short product/feature brief. What/Who/Why.
2. **Map the Big Picture** — "mile-wide, inch-deep". Backbone de activities y tasks, izquierda-derecha (narrative flow).
3. **Explore** — descompón tasks en subtasks. Blue sky, variations, exceptions, "wouldn't it be cool if".
4. **Slice Out Viable Releases** — thin slices que abarquen el flow completo. Walking Skeleton = release mínimo end-to-end.
5. **Slice Out Development Strategy** — opening game (walking skeleton), mid game (functionality), end game (refinement).

> *"The secret to prioritization is to prioritize outcomes and not features."*

## Splitting heuristics

- **"Think cake"**: cada story debe ser una "rebanada que se pueda probar". Whole features tienen menos valor para usuarios; varias stories suman a una feature completa.
- **Stories vs Delivery Tasks**: stories describen algo entregable y evaluable; tasks son "la receta" de cómo construir la story.

## Cómo procedes — descomponer capability en features

1. Lees `nodes/<capability>.md`.
2. Aplicas Story Map mentalmente: ¿cuál es el narrative flow del usuario para conseguir el outcome de la capability?
3. Identificas las features (slices coherentes del flow). Típicamente 2-5 por capability.
4. Para cada feature, validas los 4 criterios feature.

## Cómo procedes — descomponer feature en stories

1. Lees `nodes/<feature>.md`.
2. Identificas el thin slice más pequeño que entrega algún outcome del usuario.
3. Propones stories con frase Cohn ("As/I want/So that") + examples placeholder.
4. Validas INVEST en cada story.

Tras confirmación del humano, aplicas el cambio leyendo los templates como base. Aplicas `shared-cross-link` después.

## 5 Cs Cycle

Para mantener stories como tokens de conversación viva:

```
Card → Conversation → Confirmation → Construction → Consequences → (loop)
```

- **Card**: ideas en cards (una por card).
- **Conversation**: discuss con team, preguntas, soluciones ideales, shared understanding.
- **Confirmation**: agreement sobre qué construir + confirmation tests.
- **Construction**: developers/testers construyen con shared understanding.
- **Consequences**: working software → test con usuarios → learnings → next cycle.

## Trampas a evitar

- **Feature horizontal** (anti-pattern Patton): *"Toda la persistencia"* — es capa, no slice end-to-end.
- **Feature como tarea técnica**: *"Refactor del módulo X"* — eso es trabajo técnico que va a ADR o sprint backlog, no a feature de producto.
- **Story sin "so that"**: falta entender el benefit. La frase Cohn requiere las 3 partes.
- **Stories que rompen INVEST**: reagrupa si no Independent; profundiza discovery si no Estimable; descompone si no Small.
- **Spec por adelantado**: las stories no son contrato sellado, son tokens para conversación (Patton/Beck).

## Después de aplicar

Registra en documento-sesión:

```markdown
- Creadas N features bajo `cap-NN-<slug>` y M stories bajo `feature-NNN-<slug>` aplicando `po-feature`. Cita: definición canónica + Patton User Story Mapping + Cohn INVEST.
```
