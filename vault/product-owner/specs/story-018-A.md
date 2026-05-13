---
type: story
id: story-018-A
title: "Orquestador convoca 5 advisors en flat parallel"
parent: feature-018-slash-scope-scan
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-018-A — Orquestador convoca 5 advisors en flat parallel

## Narrativa

**Como** operador agente orquestador (típicamente PO al draftar WA en Modo 1 paso 5, o cualquier rol mid-WA con duda cross-dominio),
**quiero** ejecutar `/scope-scan "<propuesta>"` y convocar a los 5 advisors restantes en paralelo (un solo mensaje con 5 Task tool calls),
**para** que cada advisor produzca su `scope-scan-output` simultáneamente sin secuencialización innecesaria.

## Examples (discovery)

1. **PO en Modo 1 paso 5 al draftear WA**: ejecuta `/scope-scan` sobre la propuesta del humano. Invoca a architect + designer + business-analyst + security-officer + qa.
2. **Architect en WA `adr` puro orquestador**: invoca a los 6 advisors incluyendo PO (cuando Architect es el orquestador, él NO es uno de los 5 — invoca a 6 incluyéndose o como el "sexto implícito").
3. **PO post-step scope-scan**: tras cerrar un step, ejecuta `/scope-scan` sobre el artefacto producido. Mismo formato, distinto momento del lifecycle.
4. **Orquestador con duda cross-dominio mid-step**: el rol activo en su step ejecuta `/scope-scan` ad-hoc sobre una duda concreta. Cagan give-and-take encouraged.
5. **Paralelización real**: un solo mensaje del orquestador contiene 5 (o 6) tool_use blocks Task — Claude Code los ejecuta en paralelo, no en secuencia.
6. **Anti-patrón a evitar**: 5 mensajes secuenciales con un Task tool cada uno. Eso NO es flat parallel — es secuencial. La feature-018 EXIGE un solo mensaje con N tool_use blocks.

## Acceptance Criteria

- **AC-A1**: El orquestador invoca a los advisors restantes (5 cuando es PO; 6 cuando es otro orquestador) en **un único mensaje** con múltiples tool_use blocks Task.
- **AC-A2**: Cada Task tool call recibe `subagent_type` correspondiente al rol del advisor (architect | designer | business-analyst | security-officer | qa).
- **AC-A3**: Cada prompt al advisor incluye: identidad del rol (referencia a `.claude/agents/<rol>.md`), propuesta del humano (texto completo), paths del vault a leer (capability padre, ADRs aplicables, etc.), instrucción de devolver `scope-scan-output` estructurado.

## Cross-links

- **depends-on**: feature-010 (entry-point por rol) — los advisors están cargados como agent files cargables por subagent_type.
- **also-relates-to**: feature-023 protocolo Filtro PO — consume los 5 outputs del scope-scan.

## Test mecánico Adzic SbE

✅ 6 examples concretos (3 momentos del lifecycle + paralelización + anti-patrón).
✅ 3 AC SMART verificables.
✅ Spec Gherkin descendible.

Test mecánico **PASA**.
