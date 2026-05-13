---
name: arch-coupling-detection
description: "Identificar acoplamientos entre features, capabilities, módulos de código o nodos del grafo. Distinguir acoplamiento apropiado (deseado, alineado con dominio) de acoplamiento problemático (oculto, fuera de boundaries, information leakage). Use this skill during feature-viability-review, when reviewing repo for architectural debt, or when the user explicitly asks to check coupling."
allowed-tools: Read Glob Grep
materializes-feature: [feature-018-slash-scope-scan, feature-019-slash-verify]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): skill Architect invocada como advisor en scope-scan (feature-018) y sign-off (feature-019). Aplicada en step-3 del WA-005 actual.
---

# Skill: coupling-detection (Architect)

## Quick reference

Aplica 5 pasos para inventariar y categorizar acoplamientos. Output: reporte estructurado con acoplamientos categorizados + recomendación.

## When to invoke

- Durante `feature-viability-review` paso 5.
- Revisión periódica de deuda arquitectónica.
- Humano pide "ver acoplamientos".

## Inputs

- Feature / capability / módulo a revisar.
- Otras features / módulos del proyecto.
- ADRs existentes (algunos declaran acoplamientos permitidos / prohibidos).

## Process — 5 pasos

1. **Inventariar acoplamientos declarados** en frontmatter: `depends-on`, `also-relates-to`, `related-adrs`. Estos son visibles.
2. **Detectar acoplamientos NO declarados visibles en código**: imports/referencias entre módulos. Estos son los más problemáticos.
3. **Evaluar contra Dependency Rule (Martin)**: dependencias apuntan hacia adentro? Si apuntan hacia afuera → violación.
4. **Detectar information leakage (Ousterhout)**: conocimiento (implementación, datos, lógica) en múltiples lugares. Solución: extraer a módulo común.
5. **Categorizar cada acoplamiento**:
   - Apropiado declarado → aceptar
   - Apropiado no declarado → pedir declaración en frontmatter
   - Problemático declarado → refactorizar (puede requerir ADR)
   - Problemático no declarado → refactorizar urgente

## Output format

```markdown
## Acoplamientos detectados — [feature/módulo]

### Apropiados declarados
- ...

### Apropiados no declarados
- ...

### Problemáticos declarados
- ...

### Problemáticos no declarados
- ...
```

**Recomendación final**:
1. **Aprobar** — solo apropiados.
2. **Aprobar con declaraciones pendientes** — añadir cross-links faltantes.
3. **Refactorizar antes de implementar.**
4. **Escalar a ADR** — patrón es decisión arquitectónica significativa.

## Bibliographic foundation

- `vault/architect/research/library/ousterhout-philosophy-software-design.md` — information leakage.
- `vault/architect/research/library/martin-clean-architecture.md` — Dependency Rule, SOLID.
- `vault/architect/research/library/ford-evolutionary-architecture.md` — appropriate vs. inappropriate coupling.

## Full design

`./design.md` — incluye ejemplo aplicado a feature-009 (favoritos).

## Limitations

- "Apropiado" depende del dominio.
- Detección automatizada de coupling de código requiere parsing — vault-cli inicial no lo cubre. Skill semi-manual con Architect leyendo código.
- En proyectos en bootstrap, la skill es predictiva.

## Status lifecycle

Si esta skill produce un report estructurado en `vault/architect/research/`: `status: draft` inicial. Transición a `active` vía `on-close` del WA al `/verify`. Si solo emite veredicto inline (caso common dentro de feature-viability-review), no aplica lifecycle — el output se integra en el review padre.

## WA mapping

Esta skill se invoca dentro de:
- **`feature-design`** (paso 5 de `feature-viability-review`).
- **`refactor`** (step de architect proposal).
- On-demand desde sesión Architect cuando humano pide "ver acoplamientos".
