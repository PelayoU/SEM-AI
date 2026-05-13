---
type: feature
id: feature-041-readme-onboarding
title: "README.md raíz como onboarding completo del framework"

jtbd-outcome: "Cuando el operador humano newcomer (ingeniero adoptador, evaluador académico, comunidad técnica) encuentra el repo SEM-IA por primera vez, quiere comprender el framework leyendo el README.md raíz: tesis filosófica, modelo conceptual (8 roles × 7 dimensiones × 14 templates), cómo arrancar, capabilities operant + planned, dual track, anclaje bibliográfico, posicionamiento Apache 2.0 y cautelas de privacidad para adopters, so I can decido informado si adoptar/evaluar/contribuir sin invocar al autor."

parent: cap-10-articulacion-publica

dimensions-affected: [product, usability, business, security]  # Nielsen #10 + GTM Moore + secret hygiene adopters

depends-on:
  - feature-011-claude-md-raiz  # NO Nivel 1; pero feature-041 referencia CLAUDE.md raíz
also-relates-to:
  - feature-044-glosario-publico  # README referencia glosario en primera aparición de términos
  - feature-045-ruta-lectura-audiencia  # README incluye sección "Cómo leer este repo"
related-adrs: []

status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005

fundamento-bibliografico:
  - Nielsen #10 Help and documentation
  - Moore — Crossing the Chasm (Early Adopters → Pragmatists)
  - Shostack — Threat Modeling (declarar threat surface honesto al adopter)
---

# feature-041 · README.md raíz como onboarding completo

## Problem

El operador newcomer encuentra el repo SEM-IA. Si el README es inadecuado (demasiado técnico / sin tesis / sin onboarding / sin glosario), el newcomer abandonará. Hay tres audiencias distintas: ingeniero adoptador, evaluador académico, comunidad técnica. Cada una busca cosas diferentes.

## Hypothesis

README estructurado con secciones canónicas que cubren las 3 audiencias + glosario referenciado + ruta de lectura por audiencia + cautelas de privacidad (secret hygiene para adopters).

## Stories

3 stories agrupadas:

- **story-041-A**: Newcomer lee README y comprende tesis + modelo conceptual + cómo arrancar
- **story-041-B**: Evaluador académico ve atribución bibliográfica explícita + corpus auditable
- **story-041-C**: Adopter externo ve cautelas de privacidad (vault público por diseño + secret hygiene)

## Piezas del bootstrap

- `/Users/pelayo/Developer/SEM-AI/README.md` (65 KB, ya construido).
