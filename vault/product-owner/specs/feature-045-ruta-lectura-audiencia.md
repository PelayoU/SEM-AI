---
type: feature
id: feature-045-ruta-lectura-audiencia
title: "Ruta de lectura diferenciada por audiencia (técnica / académica / adoptante)"

jtbd-outcome: "Cuando el operador humano newcomer accede al repo, quiere identificar su ruta de lectura óptima según audiencia (ingeniero adoptante / evaluador académico / contribuyente técnico) en sección 'Cómo leer este repo' del README, so I can no leer 65 KB linealmente — progressive disclosure Nielsen #10 + Cooper."

parent: cap-10-articulacion-publica

dimensions-affected: [product, usability, business]  # Nielsen #10 + Cooper + GTM Moore

depends-on:
  - feature-041-readme-onboarding
also-relates-to:
  - feature-044-glosario-publico
related-adrs: []

status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# feature-045 · Ruta de lectura por audiencia

## Problem

README de 65 KB. Tres audiencias distintas (adoptante / académica / contribuyente) buscan cosas diferentes. Lectura lineal completa = alto coste para todos.

## Hypothesis

Sección "Cómo leer este repo" en README con ≥3 rutas diferenciadas. Cada ruta incluye path de arranque + ≥1 artefacto del vault + ≥1 slash command relevante.

## Stories

2 stories:

- **story-045-A**: README incluye sección "Cómo leer este repo" con ≥3 rutas por audiencia
- **story-045-B**: Cada ruta cumple criterio de completitud mínima (path arranque + artefacto + slash)

## Notas

- Materialización: pending WA feature-build futuro. WA-005 produce spec; el README no se modifica en este WA.
