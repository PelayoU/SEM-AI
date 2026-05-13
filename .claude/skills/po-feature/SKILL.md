---
name: po-feature
description: "Descomponer una capability aprobada en features (slices de outcome) y cada feature en stories (thin slices INVEST) aplicando criterios bibliográficos auditados (Patton Story Map, Cohn INVEST, Christensen JTBD). Una feature entrega outcome experiencial concreto al usuario. Una story es slice ejecutable. Use this skill when decomposing a capability into features, when breaking down a feature into stories, or when validating existing features/stories against criteria."
when_to_use: "El humano quiere descomponer una capability en features, descomponer una feature en stories, o validar features/stories existentes."
---

# po-feature

## Propósito

Descomponer una capability en **features** (slices de outcome coherente) y cada feature en **stories** (thin slices INVEST ejecutables). Cuarto y quinto nivel del grafo.

## Bibliografía aplicada

- `bibliography/patton-user-story-mapping.md` — Jeff Patton, *User Story Mapping*. Narrative flow + thin slices. Las features son slices verticales que entregan outcome experiencial.
- `bibliography/cohn-user-stories-invest.md` — Mike Cohn, *User Stories Applied*. INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable.
- `bibliography/christensen-jtbd.md` — JTBD. Cada feature avanza el job principal.

## Criterios formales — feature

1. **Outcome experiencial.** La feature entrega algo que el usuario puede percibir/usar. ❌ *"Capa de cache Redis"*. ✅ *"Que el dashboard cargue en <1s"*.
2. **Slice vertical (Patton).** Atraviesa todas las capas del stack (UI + lógica + datos) para producir outcome. No es "una capa", es un corte fino end-to-end.
3. **Cuelga de capability clara** (`parent: cap-XX`).
4. **Tamaño razonable.** Si no puedes imaginar 2-7 stories bajo esta feature, está mal cortada.
5. **Cross-links declarados.** Features suelen tocar varias dimensiones (`dimensions-affected`) y depender de otras features (`depends-on`).

## Criterios formales — story (INVEST de Cohn)

1. **Independent.** Cada story implementable sin esperar a otra (relax si dependencias técnicas reales).
2. **Negotiable.** El "cómo" es conversable; el "qué" y el "por qué" no.
3. **Valuable.** Para el usuario (no para el dev). Si solo aporta valor técnico, repensar.
4. **Estimable.** El equipo puede estimar esfuerzo grueso. Si nadie sabe estimar, falta info — discovery primero.
5. **Small.** Cabe en un sprint / iteración corta. Si no, parte.
6. **Testable.** AC futuros pueden derivarse. Si no, falta claridad de outcome.

## Estructura del nodo `feature`

```yaml
---
category: feature
id: feature-NNN-<slug>
parent: cap-NN-<slug>
status: draft  # draft | decomposed | ready-for-implementation | in-implementation | implemented
created: <ISO date>
also-relates-to: []
depends-on: []
dimensions-affected: [product, ...]
priority: <number>  # opcional, para sort en backlog.base
---

# Feature NNN — <Título>

## Outcome
<1-3 frases. Qué experiencia/resultado obtiene el usuario al usar esta feature.>

## Stories (descomposición INVEST)
- `[[story-NNN-A-<slug>]]` — As <role> I want <action> so that <benefit>.
- `[[story-NNN-B-<slug>]]` — ...
- `[[story-NNN-C-<slug>]]` — ...

## Spec
- `[[spec-NNN-<slug>]]` — contrato Gherkin agregando AC de todas las stories (se genera con `po-spec`).

## Notas
<Contexto adicional, decisiones, dudas abiertas.>
```

## Estructura del nodo `story`

```yaml
---
category: story
id: story-NNN-X-<slug>   # X = letra A, B, C... para trazabilidad con AC
parent: feature-NNN-<slug>
status: draft  # draft | ready | in-implementation | done
created: <ISO date>
also-relates-to: []
depends-on: []
dimensions-affected: []
---

# Story NNN-X — <Título>

## Frase Cohn
As **<role>**, I want **<action>**, so that **<benefit>**.

## Examples (Adzic — alimentan AC)
- Ejemplo 1: <escenario concreto>
- Ejemplo 2: <variación>
- Ejemplo 3: <edge case>

## INVEST self-check
- Independent: <✅/❌/🟡 con razón>
- Negotiable: ...
- Valuable: ...
- Estimable: ...
- Small: ...
- Testable: ...
```

## Cómo procedes — descomponer capability en features

1. Lees `nodes/<capability>.md`.
2. Aplicas Story Map (Patton) mentalmente: ¿cuál es el narrative flow del usuario para conseguir el outcome de la capability? Las features son los pasos coherentes del flow.
3. Propones lista de features (típicamente 2-5 por capability) con outcome de cada una.
4. Para cada feature, validas con los 5 criterios feature.

## Cómo procedes — descomponer feature en stories

1. Lees `nodes/<feature>.md`.
2. Identificas el thin slice más pequeño que entrega *algún* outcome de la feature (Cohn small).
3. Propones stories con frase Cohn + examples placeholder.
4. Validas INVEST por story.

## Output esperado

Propuesta al humano:
- Lista de features/stories con veredicto.
- Paths a crear: `nodes/feature-NNN-<slug>.md`, `nodes/story-NNN-X-<slug>.md`.
- Cross-links: feature `parent: cap-NN`; story `parent: feature-NNN`.

Aplicas `shared-cross-link` para los demás cross-links.

## Trampas a evitar

- **Feature-tarea técnica**: *"Refactor del módulo X"* — no es feature de producto, es trabajo técnico. Va a ADR o a un nodo de tarea interna.
- **Feature horizontal (Patton trampa)**: *"Toda la persistencia"* — capa, no slice. Patton anti-pattern.
- **Story sin "so that"**: si no puedes nombrar el benefit, falta entender el JTBD.
- **Stories que se contradicen INVEST**: si una story depende de otra (no Independent), reagrupa. Si nadie puede estimar (no Estimable), discovery falta.

## Después de aplicar la skill

Registra en documento-sesión:
```markdown
- Creadas N features bajo `cap-NN-<slug>` y M stories bajo `feature-NNN-<slug>` aplicando `po-feature`. Cita: Patton Story Map + Cohn INVEST + JTBD.
```
