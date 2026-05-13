---
type: story
id: story-038-D
title: "PO presenta WA al humano + confirma + indica próximo paso"
parent: feature-038-po-modo-1
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-038-D — PO presenta WA + confirma + handoff

## Narrativa

**Como** PO tras draftear el WA,
**quiero** presentar el WA al humano en forma legible + confirmar antes de marcar `status: active` + indicar próximo paso (Modo 2 si PO conduce step-1, handoff a otro rol si no),
**para** que el humano valide scope/steps antes de comprometer el WA + sepa qué sigue inmediatamente.

## Examples (discovery)

1. **Presentación legible**: PO muestra outcome-type + fase + dimensiones detectadas + flags relevantes + lista compacta de steps con active-role.
2. **Humano confirma**: humano responde "OK, arranca". PO marca WA `status: active` + procede.
3. **Humano pide ajuste**: humano dice "añade step Security". PO edita el WA antes de marcar active. Re-presenta.
4. **Step-1 PO → arranca Modo 2 inmediato**: si step-1 tiene `active-role: product-owner`, PO procede a Modo 2 sin cambio de sesión.
5. **Step-1 otro rol → handoff verbal**: si step-1 tiene `active-role: architect`, PO indica "Step-1 pending para Architect. Sal de esta sesión y arranca `npm run arch`."

## AC

- **AC-D1**: PO presenta WA en formato legible con outcome-type + fase + dimensions + flags + lista steps + active-role por step.
- **AC-D2**: PO espera confirmación del humano antes de marcar `status: active`. Si humano pide ajustes, PO los aplica antes de cerrar el draft.
- **AC-D3**: Tras confirmación, PO indica próximo paso: arranca Modo 2 si conduce step-1, o handoff verbal con atajo npm si delega.

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
