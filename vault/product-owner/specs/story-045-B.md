---
type: story
id: story-045-B
title: "Cada ruta cumple criterio de completitud mínima"
parent: feature-045-ruta-lectura-audiencia
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-045-B — Completitud mínima por ruta

## Narrativa

**Como** newcomer eligiendo una ruta,
**quiero** que cada ruta lleve a estado de orientación útil (no termine arbitrariamente),
**para** que tras leer la ruta sepa cómo seguir + el sistema haya cumplido progressive disclosure.

## Examples

1. **Ruta técnica completa**: path arranque (README sección modelo) + artefacto vault (workflows.md) + slash relevante (`/sessions`).
2. **Ruta académica completa**: path arranque (README tesis) + artefacto vault (library INDEX) + WA archivado como evidencia (`wa-2026-05-12-002.md`).
3. **Ruta adoptante completa**: path arranque (README cómo arrancar) + artefacto vault (CLAUDE.md) + slash relevante (`/status`).
4. **Ruta incompleta inválida**: ruta con 1 solo path "lee README". Insuficiente — newcomer queda sin saber qué hacer después.
5. **Tras leer ruta**: newcomer entiende qué hacer (adoptante → ejecutar `npm run sem`; académico → revisar WAs archivados; técnico → leer agent files).

## AC

- **AC-B1**: Cada ruta incluye mínimo: (a) path de arranque (sección README o archivo del vault), (b) ≥1 artefacto del vault (capability file, governance doc, library nota), (c) ≥1 slash command relevante.
- **AC-B2**: Tras leer la ruta, el newcomer sabe qué hacer (acción siguiente concreta).
- **AC-B3**: Las rutas NO son exhaustivas (no cubren TODO el repo) pero SÍ orientan a 60-70% del valor para su audiencia.

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
