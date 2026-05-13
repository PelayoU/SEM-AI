---
category: feature
id: feature-<NNN>-<slug>
parent: "[[cap-NN-slug]]"
status: draft
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
also-relates-to: []
depends-on: []
dimensions-affected: [product]
priority:
---

# Feature <NNN> — <Título>

## Outcome experiencial (Patton)

> 1-3 frases. Qué experiencia/resultado concreto obtiene el usuario al usar esta feature. *"The secret to prioritization is to prioritize outcomes and not features."* Si no puedes resumirlo así, la feature está mal delimitada.

## Progreso JTBD (Christensen)

> Qué progreso habilita para el usuario en qué circunstancia. *"People hire products to make progress in specific circumstances."* Si solo "agrega capacidad X", repensar.

## Thin slice (Patton)

> Esta feature, ¿es un slice vertical end-to-end (atraviesa todas las capas hasta producir outcome)? ¿O es una "capa" horizontal? Patton: los slices verticales entregan valor; las capas no.

## Stories (descomposición INVEST — Cohn)

> Lista de stories hijas con frase Cohn. Cada story se materializa con el template `story.md` y debe pasar los 6 criterios INVEST.

- `[[story-NNN-A-slug]]` — As <role>, I want <action>, so that <benefit>.
- `[[story-NNN-B-slug]]` —
- `[[story-NNN-C-slug]]` —

## Spec

> Wikilink al spec.md con el contrato Gherkin que agrega AC de todas las stories de esta feature (convención Adzic: 1 spec por feature, no por story). Se materializa con la skill `po-spec`.

- `[[spec-NNN-slug]]`

## Notas

> Contexto adicional, decisiones tomadas durante la conversación, dudas abiertas, edge cases conocidos.
