---
type: story
id: story-033-B
title: "Agente al continuar step usa /wa para reorientarse"
parent: feature-033-slash-wa
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-033-B — Agente reorientación al continuar step

## Narrativa

**Como** operador agente (cualquier rol) que arranca su sesión para conducir un step de un WA en curso,
**quiero** ejecutar `/wa` al arrancar (o leer el WA directamente) para reorientarme: qué step me toca, qué inputs tengo del step anterior (Progreso entry), qué scope me autoriza,
**para** arrancar mi step con contexto cargado, no a ciegas.

## Examples (discovery)

1. **Architect arranca su step**: `npm run arch` arranca sesión. Architect ejecuta `/wa` (o lee WA directamente). Identifica step actual con `active-role: architect`. Lee Progreso entry del PO (step anterior) para inputs concretos. Lee scope-allowed para saber qué puede editar.
2. **Developer continúa step interrumpido**: sesión nueva, ejecuta `/wa`. Identifica su step in-progress (no done). Lee Progreso parcial + bloque `filesystem-changes` si aplica. Continúa.
3. **QA al final del WA**: ejecuta `/wa`. Identifica step-7 QA pending. Lee Progreso de steps 3-6 (Architect/Designer/Business/Security) para tener inputs cross-rol antes de su verificabilidad-review.
4. **Briefing por step**: el WA contiene sección "Briefing por step" (Gap 10) con bloques curados por PO. El agente lee ese briefing como parte del onboarding al step.
5. **Múltiples WAs**: el agente está en sesión de un rol específico pero hay varios WAs con steps de ese rol. `/wa` pregunta cuál.

## AC

- **AC-B1**: Agente al arrancar su step lee el WA (vía `/wa` o directamente). Lee Progreso entries de steps previos para inputs.
- **AC-B2**: Agente lee Briefing por step del WA (Gap 10, 4 bloques canónicos) si su rol tiene briefing escrito por el orquestador.
- **AC-B3**: Si modality del step es `subagente` con autoridad de edición, agente registra `filesystem-changes` al cerrar (cumple Gap 9).

## Cross-links

- **also-relates-to**: feature-024 contrato `filesystem-changes` (Gap 9 ya formalizado Nivel 3).
- **depends-on**: feature-014 estructura WA (Nivel 2 ADR latente).

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
