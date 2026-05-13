---
type: story
id: story-010-C
title: "Agente al arrancar carga identidad via wrapper CLAUDE.md jerárquico"
parent: feature-010-entry-point-por-rol
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-010-C — Agente al arrancar carga identidad via wrapper CLAUDE.md jerárquico

## Narrativa

**Como** operador agente (cualquier rol custodio) al arrancar mi sesión,
**quiero** leer mi wrapper `vault/<mi-rol>/CLAUDE.md` (carga jerárquica nativa Claude Code) + mi agent file `.claude/agents/<mi-rol>.md`,
**para** cargar identidad bibliográfica anclada + zona de trabajo + skills disponibles antes del primer prompt del humano.

## Examples (discovery)

1. **PO arrancando**: sesión `npm run sem` arranca en `vault/product-owner/`. Claude Code carga `vault/product-owner/CLAUDE.md` (wrapper) automáticamente, que referencia `.claude/agents/product-owner.md` (identidad). Antes del primer prompt, el agente conoce: Cagan + Sinek + Rumelt + Doerr + Christensen + Patton + Cohn + Adzic, modos 1-4, reglas operativas 1-12.
2. **Architect arrancando**: sesión `npm run arch` carga `vault/architect/CLAUDE.md` + `.claude/agents/architect.md`. Identidad: Nygard + Bass + Ford + Martin + Ousterhout.
3. **Wrapper ausente (developer)**: `vault/developer/CLAUDE.md` está pendiente (gap menor). Al ejecutar `npm run dev`, Claude Code carga solo el CLAUDE.md raíz (sin wrapper específico). El agent file `.claude/agents/developer.md` se carga vía Task tool si se invoca como subagente, pero al arrancar sesión directa, identidad cargada es parcial.
4. **Cambio de directorio mid-sesión**: el operador agente activo NO cambia de directorio (cd) mid-sesión. La identidad cargada al arrancar persiste durante toda la sesión.
5. **Identidad declarada en ritual de inicio**: el PO (Modo 1 paso 1) al arrancar lee `vault/product-owner/CLAUDE.md` + identidad + estado del vault, y presenta panorámica al humano antes del primer prompt.

## Acceptance Criteria

- **AC-C1**: Para cada rol custodio existe (o existe gap declarado) `vault/<rol>/CLAUDE.md` (wrapper) que referencia explícitamente `.claude/agents/<rol>.md` (agent file).
- **AC-C2**: Al arrancar sesión `npm run <rol>`, Claude Code carga el wrapper automáticamente vía mecanismo CLAUDE.md jerárquico nativo del harness.
- **AC-C3**: El agent file cargado declara identidad: dimensión custodiada + bibliografía aplicable + modos de operación + reglas operativas + skills disponibles + lo que NO hace.

## Cross-links

- **also-relates-to**: feature-035 (ritual inicio PO) — el PO al arrancar ejecuta ritual.
- **also-relates-to**: feature-011 (CLAUDE.md raíz como guía estática) — el CLAUDE.md raíz es padre jerárquico del wrapper.
- **depends-on-harness**: claude-code-mecanismo-CLAUDE-md-jerarquico.

## Test mecánico Adzic SbE

✅ 5 examples concretos.
✅ 3 AC SMART verificables (incluyendo el gap declarado del wrapper developer).
✅ Spec Gherkin descendible.

Test mecánico **PASA**.
