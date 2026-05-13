---
type: story
id: story-036-B
title: "Operador en sesión equivocada recibe recovery del rol activo"
parent: feature-036-orientacion-rol
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-036-B — Recovery cuando operador en sesión equivocada

## Narrativa

**Como** operador humano que YA está en sesión de rol equivocado (ej. abrió `npm run arch` pero su propuesta es product/estratégica),
**quiero** que el rol activo detecte el scope ajeno y me comunique recovery ("esta no es decisión de mi dominio; sal y abre `npm run <rol-correcto>`"),
**para** recuperar sin perder tiempo + sin frustración (Nielsen #9 error recovery).

## Examples (discovery)

1. **Humano en arch, propuesta product**: ejecuta `npm run arch`. Trae propuesta "quiero diseñar feature de login". Architect detecta scope product. Comunica: "Esta es decisión de producto. Sal y abre `npm run sem` (PO). Yo no me meto en su dominio. Si emerge implicación arquitectónica en el WA del PO, me invocará como subagente."
2. **Humano en des, propuesta technical**: ejecuta `npm run des`. Trae propuesta "diseñar ADR de estructura del grafo". Designer detecta scope technical. Comunica recovery a `npm run arch`.
3. **Humano en biz, propuesta cross-cutting**: trae propuesta que toca product + business + technical. Business detecta scope cross-cutting. Comunica "Esto es decisión product + cross-cutting. Sal y abre `npm run sem`. PO clasificará y me invocará en scope-scan si business tiene flags."
4. **Humano en sec, propuesta válida security**: trae propuesta "threat-model standalone de feature-007". Security NO comunica recovery — esto SÍ es su dominio. Procede.
5. **Anti-patrón evitado**: NO hay magia de "redirección automática" — el rol activo NO arranca otra sesión. Solo comunica al humano cuál es la correcta + el humano cierra y arranca la nueva manualmente.

## AC

- **AC-B1**: Cada rol custodio al recibir propuesta detecta si el scope cae dentro de su dominio o es ajeno. Aplica criterio declarado en su agent file (sección "Lo que NO haces" + "Cuándo eres invocado").
- **AC-B2**: Si el scope es ajeno, el rol comunica recovery al humano con: (a) reconocimiento que NO es su dominio + razón corta + (b) sugerencia del rol correcto + atajo npm + (c) opcional: explicación de por qué (give-and-take Cagan).
- **AC-B3**: El rol activo NO ejecuta acciones del dominio ajeno. NO drafta WA, NO produce artefactos. Solo comunica y espera al humano.

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
