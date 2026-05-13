---
name: po-goal
description: "Crear, refinar y validar goals del proyecto bajo la visión aplicando criterios bibliográficos auditados (Doerr OKR, Doran SMART, Cagan alineación). Un goal es resultado medible que materializa la visión en horizonte de 3-12 meses, controlable por el equipo, distinto de los demás goals. Use this skill when proposing a new goal, refining one, or reviewing whether existing goals serve the vision."
when_to_use: "El humano propone un goal, pide refinarlo, o quiere validar los goals existentes contra la visión."
---

# po-goal

## Propósito

Producir o evaluar goals que materialicen la visión en horizonte temporal medible. Los goals son el segundo nivel del grafo — del enunciado abstracto (visión) a outcomes verificables.

## Bibliografía aplicada

- `bibliography/doerr-okrs.md` — John Doerr, *Measure What Matters*. Objectives + Key Results. Goal = Objective ambicioso + KRs medibles.
- `bibliography/doran-smart.md` — George Doran (1981). SMART: Specific, Measurable, Achievable, Relevant, Time-bound.
- `bibliography/cagan-product-vision.md` — Cagan. Goal materializa visión en horizonte controlable.

## Criterios formales (6 tests Doerr + Doran)

1. **Specific (Doran S).** El goal dice qué cambia, no es vago. ❌ *"Mejorar adopción"*. ✅ *"Que 50 proyectos externos usen SEM-IA en su SDLC real"*.
2. **Measurable (Doran M, Doerr KR).** Tiene métrica o conjunto de Key Results. Si no puedes medir si lo lograste, no es goal.
3. **Achievable (Doran A).** Stretch goal sí (Doerr); imposible no. Achievable bajo restricciones reales del equipo y horizonte.
4. **Relevant (Doran R, Cagan).** Materializa una parte de la visión. Si no aporta a la visión, sobra.
5. **Time-bound (Doran T).** Horizonte explícito (3-12 meses típicamente). Sin fecha, es deseo.
6. **Independent del resto.** Cada goal cubre una arista distinta de la visión. Goals que se solapan son síntoma de mal recorte.

## Estructura del nodo `goal`

```yaml
---
category: goal
id: goal-NN-<slug>
parent: vision
status: active
created: <ISO date>
horizon: <ej. "Q3-Q4 2026">
also-relates-to: []
depends-on: []
dimensions-affected: [product]
---

# Goal NN — <Título corto>

## Objective (Doerr O)
<Frase ambiciosa que materializa la visión.>

## Key Results (Doerr KR — 2-4)
- KR1: <métrica concreta + número + fecha>
- KR2: ...
- KR3: ...

## Anclaje en visión
<Cita el aspecto de la visión que este goal materializa.>

## No-meta
<Lo que este goal NO persigue (para evitar scope creep).>
```

## Cómo procedes

1. **Si el humano propone un goal**: aplicas los 6 tests. Veredicto + cita por criterio. Si falla algún test, propones reformulación.
2. **Si refinas uno existente**: lees el nodo, identificas tests fallados, propones edit.
3. **Si validas goals existentes**: cargas todos los `nodes/goal-*-*.md`, los pasas por los 6 tests, además verificas Independent (no solapan) y cobertura de visión (juntos cubren los aspectos relevantes).

## Output esperado

Propuesta al humano:
- Veredicto por test.
- Reformulación si aplica.
- Path del nodo: `nodes/goal-NN-<slug>.md`.
- `parent: vision` declarado.
- Cross-links (típicamente ninguno entre goals; si dos goals comparten KR, declara `also-relates-to`).

Aplicas `shared-cross-link` para los cross-links.

## Trampas a evitar

- **Goal-feature**: *"Implementar autenticación SSO"* — no es goal, es feature. Goal habla de outcome de usuario, no entregable.
- **Goal-actividad**: *"Hacer 10 entrevistas de usuario"* — actividad sin outcome. Goal: *"Validar JTBD con 10 entrevistas para descartar/confirmar segmento Y"*.
- **Goal-eslogan**: sin KRs medibles. Si no hay número + fecha, no es goal.
- **Goals solapados**: dos goals que llevan a hacer las mismas features. Reagrupa.

## Después de aplicar la skill

Registra en documento-sesión:
```markdown
- Creado `nodes/goal-NN-<slug>.md` aplicando `po-goal`. Cita: 6 tests Doerr OKR + Doran SMART.
```
