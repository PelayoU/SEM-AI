---
type: goal
id: goal-2-output-auditable-multirol
title: "Output auditable, coherente y verificado multi-rol"
parent: vision
also-relates-to: [goal-3-absorcion-coste-revision]
depends-on: []
dimensions-affected: [product]
status: active
created: 2026-05-10
author: pelayo
nature: controlable
---

# Goal-2: Output auditable, coherente y verificado multi-rol

## Resultado esperado

Cada decisión, artefacto y cambio en un proyecto SEM-IA es **auditable** (trazable hasta su origen), **coherente** con el resto del grafo (cross-links declarados, sin contradicciones silenciadas), y **verificado** por los custodios de las dimensiones que afecta antes de su cierre.

## Métricas

- **Cumplimiento:** 100 % de WAs cerrados con verificación multi-rol completa — todos los custodios de `dimensions-affected` aprueban.
- **Cumplimiento:** 100 % de nodos del grafo con cross-links coherentes (`parent`, `depends-on`, `also-relates-to`, `dimensions-affected`, `related-adrs` declarados).
- **Cumplimiento:** 100 % de AC con trazabilidad a tests vía `// @ac-coverage:`.
- **Cumplimiento:** Cero contradicciones detectadas vs ADRs aceptados sin arbitraje explícito declarado (`coherence-exception: adr-NNN`).

## Conexión con la visión

Materializa el contexto del enunciado: *"sobre esa memoria operan múltiples agentes IA, custodios de dimensiones distintas, que se revisan cruzadamente cada decisión y cada artefacto antes de cerrarlo"*. Sin auditabilidad real ni verificación cruzada operativa, la "capa estructural multi-rol" sería nominal.

## Fundamento bibliográfico

- **Doerr — *Measure What Matters*.** Métricas binarias y cuantitativas.
- **Doran — SMART.** Métricas verificables.
- **Cagan — *Inspired*.** Strong product team: cobertura multi-rol estructural.
