---
name: po-vision
description: "Crear, refinar y validar la visión del proyecto aplicando criterios bibliográficos auditados (Cagan, Sinek, Rumelt, Christensen JTBD). La visión es customer-centric, durable 5-10 años, articula propósito (Why), ambiciosa pero anclada. Use this skill when proposing a new project vision, when refining an existing one, or when reviewing whether the current vision still serves after significant project evolution."
when_to_use: "El humano propone una visión, pide refinarla, o pregunta si la actual sigue siendo válida."
---

# po-vision

## Propósito

Producir o evaluar un enunciado de visión que cumpla criterios bibliográficos. La visión es el ancla estratégica del proyecto — todo lo demás (goals, capabilities, features) deriva de ella.

## Bibliografía aplicada

- `bibliography/cagan-product-vision.md` — Marty Cagan, *Inspired*. Principios de visión inspiracional: customer-centric, durable, ambiciosa, accionable.
- `bibliography/sinek-start-with-why.md` — Simon Sinek, Golden Circle. Why → How → What. La visión articula el **Why**.
- `bibliography/rumelt-good-strategy.md` — Richard Rumelt, *Good Strategy / Bad Strategy*. Diagnosis + guiding policy + coherent action. La visión expresa el diagnosis estratégico.
- `bibliography/christensen-jtbd.md` — Clayton Christensen, Jobs to be Done. La visión nombra el **job** que el producto resuelve para el usuario.

## Criterios formales (los 7 tests Cagan + Sinek + Rumelt + JTBD)

1. **Customer-centric.** La visión describe valor para el usuario, no capacidad técnica. ❌ *"Plataforma de microservicios escalable"*. ✅ *"Que cualquier desarrollador entregue producto sin perder coherencia a medida que el proyecto escala"*.
2. **Articula el Why (Sinek).** Responde "¿por qué existe esto?" antes que "¿qué hace?".
3. **Durable 5-10 años.** Una visión que envejece en 6 meses está mal calibrada. ❌ *"Adoptar React"*. ✅ *"Componer UIs reusables sin atarse a un framework"*.
4. **Ambiciosa pero anclada.** Inspira, pero no es delirio. *"Resolver toda la educación mundial"* es delirio; *"Que cualquier persona aprenda programación a su ritmo sin profesor"* es ambición ancla.
5. **Diagnosis claro (Rumelt).** Nombra el problema real que ataca, no síntomas. ¿Cuál es la *kindly described situation* que justifica el proyecto?
6. **Job nombrado (Christensen).** ¿Qué job hace el usuario contratando este producto? *"Cuando estoy desarrollando con IA, quiero <X>, para <outcome>."*
7. **Accionable.** Permite a un equipo derivar goals concretos. Si oyendo la visión nadie sabe qué hacer mañana, está mal escrita.

## Estructura del nodo `vision`

```yaml
---
category: vision
id: vision
status: active
created: <ISO date>
updated: <ISO date>
also-relates-to: []
dimensions-affected: [product]
---

# Visión del proyecto

## Enunciado
<1-3 frases. Customer-centric, Why-driven, durable.>

## Diagnosis (Rumelt)
<Qué problema real ataca. Situación del mundo que justifica el proyecto.>

## Job to be done (Christensen)
<Cuando _______, quiero _______, para _______.>

## No-meta (lo que esta visión NO promete)
<Limites explícitos. Qué queda fuera del scope.>

## Origen
<Quién, cuándo, qué motivó este enunciado.>
```

## Cómo procedes

1. **Si el humano propone una visión**: aplicas los 7 tests. Para cada criterio, das veredicto (✅ / ❌ / 🟡) con razón corta + cita bibliográfica. Si hay ❌, propones reformulación concreta.
2. **Si refinas una existente**: lees el nodo `nodes/vision.md`, identificas dónde falla los tests, propones edit.
3. **Si validas la actual**: aplicas los 7 tests al enunciado existente. Reportas estado.

## Output esperado

Propuesta concreta al humano:
- Veredicto por test (lista de 7).
- Reformulación sugerida (si aplica).
- Path del nodo a crear/editar: `nodes/vision.md`.
- Cross-links a declarar (típicamente ninguno — la visión es nodo raíz).

Aplicas `shared-cross-link` si emergen `also-relates-to` legítimos (raro al nivel visión, posible si conectas con manifestos externos).

## Trampas a evitar

- **Visión-eslogan**: *"Cambiar el mundo"* — no es visión, es marketing. Falla durable + accionable.
- **Visión-roadmap**: lista de features. Falla durable (los features cambian; la visión no).
- **Visión-tecnológica**: nombra stack. Falla customer-centric.
- **Visión-genérica**: aplicable a cualquier producto. Falla diagnosis (no nombra el problema concreto).

## Después de aplicar la skill

Registra el toque en el documento-sesión del día:
```markdown
- Creado/editado `nodes/vision.md` aplicando skill `po-vision`. Cita: 7 tests Cagan + Sinek + Rumelt + JTBD.
```
