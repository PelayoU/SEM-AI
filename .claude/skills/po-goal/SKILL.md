---
name: po-goal
description: "Crear, refinar y validar goals del proyecto bajo la visión. Un goal es un concepto de alto nivel que persigue valor para usuarios o negocio, materializa un aspecto concreto de la visión, y opera en horizonte intermedio entre visión (2-10 años) y release (2-9 meses). Use this skill when proposing a new goal, refining one, or reviewing whether existing goals serve the vision."
when_to_use: "El humano propone un goal, pide refinarlo, o quiere validar los goals existentes contra la visión."
---

# po-goal

## Propósito

Producir o evaluar goals que materialicen la visión en outcomes concretos. Segundo nivel del grafo SEM-IA — del enunciado abstracto y a largo plazo (visión) a resultados específicos perseguibles.

## Estructura del nodo

Estructura del archivo en `_obsidian/templates/goal.md`. Léelo antes de crear o editar.

## Definición operativa (canónica SEM-IA)

> *"Goals: High level concepts for achieve with the product (value to users, value to business o whatever)."*

Los goals están entre **visión** (2-10 años, futuro inspiracional) y **roadmap planning** (1-2 años, evolución del producto). Persiguen valor concreto para usuarios o negocio.

## Criterios formales

1. **Persigue valor concreto.** Para usuarios, negocio, o ambos. Si no aporta valor identificable, sobra. *"value to users, value to business o whatever"*.
2. **Materializa un aspecto de la visión.** Cita cuál. Si no puedes citarlo, el goal no está alineado.
3. **Es outcome, no actividad ni feature.** ❌ *"Implementar SSO"* (feature). ❌ *"Hacer 10 entrevistas"* (actividad). ✅ *"Que 50 proyectos externos adopten SEM-IA en su SDLC real"* (outcome).
4. **Específico, no vago.** ❌ *"Mejorar adopción"*. ✅ *"50 proyectos externos en producción"*.
5. **Medible.** El humano puede responder al final del período "¿se logró sí o no?". Sin métrica explícita, no es goal.
6. **Independent del resto.** Cada goal cubre una arista distinta de la visión. Goals que se solapan llevan a las mismas features → reagrupar.

## Cómo procedes

1. **Si el humano propone un goal**: aplica los 6 criterios. Veredicto por criterio. Reformulación si falla.
2. **Si refinas uno existente**: lees el nodo, identificas criterios fallados, propones edit.
3. **Si validas goals existentes**: cargas todos los `nodes/goal-*.md`, los pasas por los 6 criterios. Verificas Independent (no solapan) y cobertura conjunta de la visión.

Output al humano: veredicto + reformulación. Tras confirmación, aplicas el cambio leyendo `_obsidian/templates/goal.md` como base. Aplicas `shared-cross-link` si dos goals comparten outcome.

## Sobre el horizonte temporal

GISF distingue niveles de planning hierarchical:

- **Roadmap planning**: 1-2 años — Vision/Product evolution.
- **Release planning**: 2-9 meses — Best value within constraints.
- **Iteration planning**: 1-4 semanas — Features to deliver now.

Los goals típicamente operan en el rango **Roadmap → Release**: 3-12 meses. Horizonte más corto = release o iteration backlog, no goal.

## Trampas a evitar

- **Goal-feature**: *"Implementar SSO"* — eso es feature, no goal. Goal habla de outcome, no entregable concreto.
- **Goal-actividad**: *"Hacer 10 entrevistas"* — actividad sin outcome. Goal: *"Validar JTBD con 10 entrevistas para descartar/confirmar segmento Y"*.
- **Goal sin métrica**: *"Mejorar adopción"* — no medible. Sin métrica, no es goal.
- **Goals solapados**: dos goals que llevan a las mismas features. Reagrupar.

## Después de aplicar

Registra en documento-sesión:

```markdown
- Creado `nodes/goal-NN-<slug>.md` aplicando `po-goal`. Cita: 6 criterios SEM-IA + horizonte planning hierarchical GISF.
```
