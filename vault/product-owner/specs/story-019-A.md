---
type: story
id: story-019-A
title: "Humano ejecuta /verify, PO comprueba closure-criteria mecánicamente"
parent: feature-019-slash-verify
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-019-A — Humano ejecuta /verify, PO comprueba closure-criteria

## Narrativa

**Como** operador humano al cierre de un Working Agreement,
**quiero** ejecutar `/verify` y que el PO compruebe mecánicamente los `closure-criteria` del WA antes de invocar verificadores,
**para** evitar invocar custodios si algún criterio observable falla (señal de WA incompleto).

## Examples (discovery)

1. **WA completo**: humano ejecuta `/verify`. PO lee frontmatter del WA + verifica que todos los steps están `status: done` + comprueba cada criterio enumerable de `closure-criteria`. Todos pasan → procede a derivar verifiers (story-019-B).
2. **Step incompleto**: humano ejecuta `/verify`. PO detecta que step-3 está `status: in-progress`. PO indica al humano: "step-3 incompleto. Completar antes de /verify."
3. **Closure-criterion observable falla**: humano ejecuta `/verify`. PO comprueba "por cada capability operant: ≥1 feature genuina" — descubre que CAP-G tiene 0 features producidas (gap). PO indica al humano qué falta.
4. **Closure-criterion subjetivo**: el PO NO juzga criterios subjetivos en este paso. Solo criterios mecánicamente verificables vía inspección del filesystem o estado del WA.
5. **PO confirma a humano antes de continuar**: tras pasar closure-criteria, PO presenta resumen al humano (qué criterios pasaron, qué dimensions-affected, qué verifiers va a invocar) antes de proceder a story-019-B.

## Acceptance Criteria

- **AC-A1**: Al ejecutar `/verify`, PO comprueba primero que todos los steps del WA tienen `status: done`. Si alguno NO, presenta al humano qué falta y NO procede.
- **AC-A2**: PO comprueba cada criterio de `closure-criteria` del frontmatter mecánicamente (vía inspección filesystem + frontmatter de nodos referenciados). Solo criterios observables.
- **AC-A3**: Si algún closure-criterion falla, PO indica al humano qué criterio + ubicación de la falla. NO procede a invocar verifiers hasta resolución.

## Cross-links

- **also-relates-to**: feature-017 (closure-criteria + on-close transitions declarativas, Nivel 2 ADR latente) — los criterios viven en frontmatter del WA por convención declarada en feature-014 (estructura WA Nivel 2 ADR latente).

## Test mecánico Adzic SbE

✅ 5 examples concretos.
✅ 3 AC SMART verificables.
✅ Spec Gherkin descendible.

Test mecánico **PASA**.
