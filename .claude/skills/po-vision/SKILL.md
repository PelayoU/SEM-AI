---
name: po-vision
description: "Crear, refinar y validar la visión del proyecto aplicando los 10 principios de Cagan + el template de positioning. La visión es el ancla estratégica del proyecto: future state 2-10 años, customer-centric, articula propósito, ambiciosa pero ancla en realidad. Use this skill when proposing a new project vision, when refining an existing one, or when reviewing whether the current vision still serves after significant project evolution."
when_to_use: "El humano propone una visión, pide refinarla, o pregunta si la actual sigue siendo válida."
---

# po-vision

## Propósito

Producir o evaluar un enunciado de visión que cumpla criterios bibliográficamente auditados. La visión es el primer nivel del grafo SEM-IA — todo lo demás (goals, capabilities, features, stories, specs) deriva de ella.

## Estructura del nodo

La estructura del archivo vive en `_obsidian/templates/vision.md`. Léelo antes de crear o editar.

## Definición operativa (canónica SEM-IA)

> *"Vision: the statement that provides a high-level guiding direction for the product."*

La visión describe un **futuro** que el equipo intenta crear, típicamente **2-10 años** desde ahora. Su propósito principal: **comunicar ese futuro e inspirar** al equipo, stakeholders, inversores, partners, clientes potenciales. Puede que no sepas cómo (o si) podrás entregarla, pero a este nivel debe creerse que vale la pena perseguirla.

> *"Product Vision is Science Fiction."* — la visión vive años en el futuro.

## Los 10 Principios de Product Vision (Cagan literal)

Criterios canónicos para evaluar una visión:

1. **Start with WHY** — articula propósito antes que producto.
2. **Fall in love with the problem, not the solution** — la solución cambia; el problema permanece.
3. **Don't be afraid to think big, with vision** — *"if you could truly validate a vision, then your vision probably isn't ambitious enough"*.
4. **Don't be afraid to disrupt yourself** — la visión puede invalidar el producto actual.
5. **Product vision needs to inspire** — emocional, no solo lógica.
6. **Determine and adopt relevant and significant trends** — la visión vive en el contexto de tendencias.
7. **Skate where the puck is going, not where it was** — anticipa, no reacciones.
8. **Be stubborn in vision, but flexible in details** — el norte no cambia; el cómo se ajusta.
9. **Keep in mind that any product vision is an act of faith** — visión validable al 100% antes de empezar no es visión.
10. **Evangelize continuously and relentlessly** — *"no hay tal cosa como sobre-comunicar la visión"*.

## Vision positioning template

Aunque la visión NO es positioning statement, este template ayuda a expresarla con disciplina:

```
For       [target customer]
Who       [statement of need or opportunity]
The       [product name] is a [product category]
That      [key benefit, reason to buy]
Unlike    [primary competitive alternative]
Our product [statement of primary differentiation]
```

## Cómo crear visión (5 pasos)

1. **Set your future time horizon.** Típicamente 5-10 años.
2. **Describe the future** (sin pensar específicamente en tu producto — como sistema socio-técnico).
3. **Tell your future product story.**
4. **Communicate your story.**
5. **Write a product positioning statement** (usando el template).

## Cómo procedes

1. **Si el humano propone una visión nueva**: aplica los 10 principios. Para cada uno, veredicto (✅/❌/🟡) con razón corta. Identifica qué principios falla. Propones reformulación.
2. **Si refinas la existente**: lees `nodes/vision.md`, identificas principios fallados, propones edits puntuales.
3. **Si validas la actual**: aplicas los 10 principios al enunciado existente. Reportas estado.

Output al humano: veredicto por principio + reformulación sugerida si aplica. El humano confirma. Tú aplicas el cambio leyendo `_obsidian/templates/vision.md` como base.

Aplicas `shared-cross-link` después si emergen cross-links (raro al nivel visión).

## Trampas a evitar

- **Visión-eslogan**: *"Cambiar el mundo"* — sin diagnosis, sin diferenciación.
- **Visión-roadmap**: lista de features — falla "be flexible in details".
- **Visión-tecnológica**: nombra stack — falla customer-centric (Principio "fall in love with the problem").
- **Visión-genérica**: aplicable a cualquier producto — falla "think big with vision" + diferenciación.
- **Visión validada al 100%**: si puedes validar la visión antes de empezar, no es ambiciosa (Principio 3).

## Después de aplicar

Registra el toque en el documento-sesión del día:

```markdown
- Creado/editado `nodes/vision.md` aplicando skill `po-vision`. Cita: 10 principios Cagan + positioning template.
```
