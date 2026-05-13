---
type: story
id: story-036-A
title: "Operador consulta criterio antes de arrancar sesión"
parent: feature-036-orientacion-rol
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-036-A — Operador consulta criterio antes de arrancar

## Narrativa

**Como** operador humano newcomer (o experimentado ante propuesta ambigua),
**quiero** consultar criterio de orientación en documentación accesible (CLAUDE.md raíz, `/sessions`, README sección "Cómo arrancar trabajo"),
**para** elegir la sesión correcta antes de ejecutar `npm run <rol>` sin retrasos ni elección errónea.

## Examples (discovery)

1. **Newcomer**: nuevo en el framework. Lee CLAUDE.md raíz sección "Cómo arrancar trabajo". Encuentra "Si dudas qué sesión arrancar: abre `npm run sem` (PO). El PO clasifica la propuesta."
2. **Propuesta ambigua "diseñar login"**: operador lee CLAUDE.md + tabla. Toca product + usability + security + technical. Criterio: si toca product → empezar por PO. PO Modo 1 paso 4 decide delegar o conducir.
3. **Trabajo puramente técnico**: operador con ADR puro sin contexto product. CLAUDE.md tabla declara "Para trabajo puramente técnico: `npm run arch`". Operador arranca Architect.
4. **/sessions output**: operador ejecuta `/sessions` (feature-034) y ve cuándo invocar cada rol con descripción 1-línea.
5. **README "Cómo arrancar trabajo"**: newcomer lee README onboarding y encuentra orientación.

## AC

- **AC-A1**: CLAUDE.md raíz sección "Cómo arrancar trabajo" incluye criterio "si dudas qué sesión arrancar" con default PO + casos especiales de trabajo puramente técnico/ops.
- **AC-A2**: Agent file PO Modo 1 paso 4 declara tabla "decide conduzco/delego" con criterios bibliográficamente anclados.
- **AC-A3**: `/sessions` output (feature-034) incluye columna "Para qué" con descripción cuándo invocar cada rol.

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
