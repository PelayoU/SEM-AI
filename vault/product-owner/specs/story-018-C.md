---
type: story
id: story-018-C
title: "Orquestador consolida outputs y aplica Filtro PO"
parent: feature-018-slash-scope-scan
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-018-C — Orquestador consolida outputs y aplica Filtro PO

## Narrativa

**Como** operador agente orquestador (típicamente PO),
**quiero** consolidar los 5 (o 6) outputs `scope-scan-output` recibidos en paralelo aplicando algoritmo declarativo + Filtro PO regla 12 con artefacto declarativo obligatorio,
**para** producir DECISIONES PO + preguntas filtradas para el humano (no agregación bruta).

## Examples (discovery)

1. **Consolidación de dimensions**: el PO calcula `dimensions-affected = unión(advisor.dimensions-detected) + product`. Resultado: lista de dimensiones a declarar en el WA.
2. **Consolidación de flags**: agregación bruta de flags de los 5 advisors con su rol emisor preservado. Antes de presentar al humano, aplica Filtro PO regla 12.
3. **Test load-bearing aplicado**: para cada flag clasificado provisionalmente como cat-1, aplica las 3 preguntas (¿aporta valor?, ¿la ausencia degrada?, ¿está en scope?). Si alguno NO → reclasifica a cat-2 con razón fuerte.
4. **Auto-audit numérica**: cuenta `cat-1 / total flags`. Si > 60% → high suspicion → revisar fila por fila. Si > 80% → invocar subagente PO focal como peer review.
5. **Artefacto declarativo obligatorio**: escribe `vault/product-owner/discovery/filtro-po-<wa-id>-<step-id>.md` con tabla por flag (cat inicial / test load-bearing / razón fuerte / veredicto final).
6. **Presentación al humano**: tras Filtro PO aplicado, presenta DECISIONES (cat-1 aplicadas) + DESCARTOS (cat-2 con razón) + APARCADOS (cat-3 diferidos) + PREGUNTAS REALES (cat-4 — solo categoría que va al humano).

## Acceptance Criteria

- **AC-C1**: Tras recibir los 5 (6) outputs paralelos, el PO consolida `dimensions-affected = unión + product` + agrega flags con rol emisor preservado.
- **AC-C2**: Aplica Filtro PO regla 12 obligatoriamente: test de load-bearing por flag + auto-audit numérica + artefacto declarativo escrito en `vault/product-owner/discovery/filtro-po-<wa-id>-<step-id>.md`.
- **AC-C3**: La presentación al humano incluye solo categoría 4 (decisiones humanas reales). Categorías 1-3 quedan documentadas en el artefacto declarativo + entrada Progreso del WA.

## Cross-links

- **depends-on**: feature-023 protocolo Filtro PO (Nivel 3 ya formalizado en agent file PO regla 12).
- **also-relates-to**: feature-019 /verify — el sign-off es el tercer checkpoint donde se aplica scope-scan + Filtro PO consolidado.

## Test mecánico Adzic SbE

✅ 6 examples concretos.
✅ 3 AC SMART verificables.
✅ Spec Gherkin descendible.

Test mecánico **PASA**.
