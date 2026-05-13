---
name: po-capability
description: "Derivar, refinar y validar capabilities bajo un goal aprobado aplicando criterios bibliográficos auditados (Torres OST, Rumelt coherent action, Christensen JTBD, Cagan). Una capability es una HABILIDAD del producto — no feature ni actividad. Decomponible en features. Use this skill when deriving capabilities from an approved goal, when proposing a new capability, or when reviewing existing ones."
when_to_use: "El humano quiere derivar capabilities bajo un goal aprobado, propone una capability nueva, o pide validar capabilities existentes."
---

# po-capability

## Propósito

Derivar o evaluar capabilities — el tercer nivel del grafo. Una capability es una **habilidad del producto** que materializa parcialmente un goal. Es decomponible en features pero NO es feature (más abstracta, más durable).

## Bibliografía aplicada

- `bibliography/torres-continuous-discovery.md` — Teresa Torres, *Continuous Discovery Habits*. Opportunity Solution Tree: del outcome (goal) a oportunidades, de oportunidades a soluciones.
- `bibliography/rumelt-good-strategy.md` — Rumelt, *coherent action*. Las capabilities son las "acciones coherentes" que el equipo desplegará para alcanzar el goal.
- `bibliography/christensen-jtbd.md` — JTBD. Cada capability resuelve un sub-job dentro del job principal nombrado en la visión.
- `bibliography/cagan-product-vision.md` — Cagan. Coherencia capability ↔ visión.

## Criterios formales (6 tests Rumelt + Torres + Cagan)

1. **Es habilidad, no feature ni actividad.** ❌ *"Login con OAuth"* (feature). ❌ *"Hacer onboarding"* (actividad). ✅ *"Que el usuario inicie sesión con identidad propia"* (habilidad — admite N features).
2. **Parent claro.** Cuelga de un goal concreto. Si no tienes goal padre, es síntoma de que falta nivel intermedio o el goal está mal cortado.
3. **Alineada con guiding policy (Rumelt).** Coherente con el "cómo" estratégico del proyecto. No contradice la visión ni otras capabilities.
4. **No solapa con otras capabilities.** Cada capability cubre una habilidad distinta. Si dos se pisan, fusiona o re-recorta.
5. **Cross-links explícitos.** Capabilities suelen relacionarse entre sí (`also-relates-to`) o depender unas de otras (`depends-on`). Declarar.
6. **Decomponible en features.** Si no puedes imaginar 2-5 features bajo esta capability, está mal cortada (demasiado abstracta o demasiado concreta).

## Estructura del nodo `capability`

```yaml
---
category: capability
id: cap-NN-<slug>
parent: goal-XX-<slug>
status: active
created: <ISO date>
also-relates-to: []
depends-on: []
dimensions-affected: [product, ...]
---

# Capability NN — <Título corto>

## Habilidad (qué hace el producto)
<1-2 frases en presente: "El producto permite/sabe/garantiza ___".>

## Sub-job (Christensen)
<Cuando _______, el usuario quiere _______, para _______.>

## Anclaje en goal padre
<Qué KR del goal se mueve por tener esta capability.>

## Features previstas (placeholder, no exhaustivo)
<Lista tentativa de 2-5 features candidatas. Solo orientativa — se materializan con po-feature después.>

## No-meta
<Lo que esta capability NO cubre.>
```

## Cómo procedes — modo single (1 capability)

1. Lees `nodes/<goal>.md` (el padre).
2. Aplicas los 6 tests al enunciado propuesto.
3. Propones nodo + cross-links.

## Cómo procedes — modo batch (derivar varias capabilities bajo un goal)

1. Lees el goal.
2. Aplicas Opportunity Solution Tree (Torres): outcome del goal → oportunidades (sub-jobs) → para cada oportunidad propones una capability.
3. Verificas Independent (no solapan) y cobertura (juntas materializan el goal).
4. Propones lista al humano para confirmación una por una.

## Output esperado

Propuesta al humano:
- Lista de capabilities con veredicto por test.
- Paths a crear: `nodes/cap-NN-<slug>.md`.
- `parent: goal-XX-<slug>` declarado.
- Cross-links entre capabilities si aplica.

Aplicas `shared-cross-link` para los `also-relates-to`/`depends-on`.

## Trampas a evitar

- **Capability-feature**: confundir habilidad con entregable. *"Implementar dashboard de admin"* es feature; *"Que el admin gestione usuarios y permisos"* es capability.
- **Capability-actividad**: *"Hacer discovery con usuarios"* — actividad interna, no habilidad del producto.
- **Capability-tecnología**: *"Usar PostgreSQL"* — decisión técnica, no habilidad. Va a ADR, no a capability.
- **Bootstrap-anchor (Torres trampa)**: derivar capabilities desde features que ya tienes en mente, no desde el goal. Resultado: el grafo "encaja" pero no materializa estratégicamente. Empieza siempre desde el outcome del goal.

## Después de aplicar la skill

Registra en documento-sesión:
```markdown
- Creadas N capabilities bajo `goal-XX-<slug>` aplicando `po-capability`. Cita: Torres OST + Rumelt coherent action + JTBD.
```
