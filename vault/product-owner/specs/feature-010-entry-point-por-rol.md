---
type: feature
id: feature-010-entry-point-por-rol
title: "Entry-point por rol vía atajos npm + wrappers CLAUDE.md jerárquicos"

jtbd-outcome: "Cuando el operador humano necesita arrancar una sesión de un rol custodio, quiere ejecutar un comando único (`npm run sem|arch|des|biz|sec|qa|dev|ops`) que cargue identidad bibliográfica + zona de trabajo + skills del rol sin teclear paths ni recordar convenciones, so I can cambiar entre roles operativamente barato."

parent: cap-02-multirol-agentes-homologos

dimensions-affected: [product, usability]  # Nielsen #7 flexibility + efficiency of use

depends-on: []
also-relates-to:
  - cap-06-visibilidad-operativa  # cada sesión presenta panorámica via ritual de inicio
depends-on-harness:
  - claude-code-mecanismo-CLAUDE-md-jerarquico  # Claude Code carga CLAUDE.md desde el dir donde arranca
  - npm-runtime  # ejecuta scripts del package.json

related-adrs:
  - ADR-latente-001  # Claude Code v1 como harness primario
  - ADR-latente-002  # Vault role-first (los wrappers viven en vault/<rol>/CLAUDE.md)

status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005

fundamento-bibliografico:
  - Nielsen 10 heurísticas (heurística #7 Flexibility and efficiency of use)
  - Cooper — About Face (waypoints: el operador sabe siempre cómo arrancar)
  - Anthropic Claude Code docs (CLAUDE.md jerárquico carga al arrancar sesión)
---

# feature-010 · Entry-point por rol vía atajos npm + wrappers CLAUDE.md jerárquicos

## Problem

SEM-IA tiene 8 roles custodios. Cada rol opera con identidad bibliográfica anclada (agent files en `.claude/agents/<rol>.md`) y zona de trabajo específica (`vault/<rol>/`). Sin un mecanismo de arranque ergonómico, el operador humano debería:

1. Recordar el path del rol (`cd vault/<rol>/`).
2. Recordar cómo arrancar Claude Code en ese directorio (`claude`).
3. Asegurar que el agent file del rol se carga correctamente (mecanismo CLAUDE.md jerárquico).

Esto introduce recall cognitive (Nielsen #6) + fricción operativa (Nielsen #7) al cambiar entre roles, especialmente en flujos multi-rol donde el operador alterna entre 4-6 sesiones por WA.

## Hypothesis

Si proveemos:
1. **Scripts npm en `package.json`** con atajos cortos por rol (`sem` para PO, `arch` para Architect, etc.).
2. **Wrappers `vault/<rol>/CLAUDE.md`** que se cargan al arrancar `claude` desde ese directorio (mecanismo nativo Claude Code).

Entonces el operador humano arranca cualquier rol con **un comando único**: `npm run <atajo>`. El wrapper carga identidad + zona de trabajo + skills automáticamente.

## Expected outcome (JTBD)

*Cuando el operador humano necesita arrancar una sesión de un rol custodio, ejecuta `npm run <atajo>` y recibe sesión con identidad cargada lista para operar.*

## Stories

Esta feature se descompone en 3 stories candidatas:

- **story-010-A**: Como operador humano, ejecuto `npm run <rol>` y arranca sesión Claude Code con identidad del rol cargada
- **story-010-B**: Como operador humano newcomer, inspecciono `package.json` y veo los 9 scripts disponibles para los 8 roles + el alias `sem`
- **story-010-C**: Como operador agente al arrancar, leo mi wrapper `vault/<mi-rol>/CLAUDE.md` + mi agent file `.claude/agents/<mi-rol>.md` y cargo identidad

## Piezas del bootstrap que materializan esta feature

- `package.json` raíz con 9 scripts: `sem, po, arch, des, biz, sec, qa, dev, ops`
- 7 wrappers `vault/<rol>/CLAUDE.md` (developer pendiente — gap menor declarado)
- Los 8 agent files `.claude/agents/<rol>.md` (artefactos Nivel 4, dependencia de esta feature)

## Notas

- **Borderline absorbe**: feature-008 (identidad por rol vía agent files) NO es feature aparte — los 8 agent files son artefactos curados Nivel 4 que feature-010 consume al arrancar sesión. La identidad cargada es comportamiento de feature-010.
- **Gap menor declarado**: wrapper `vault/developer/CLAUDE.md` está pendiente de creación. Es deuda menor que NO bloquea esta feature (la convención está documentada, falta el archivo concreto).
- **ADRs latentes apuntados**: ADR-latente-001 (Claude Code v1 harness primario) y ADR-latente-002 (Vault role-first como organización física, prereq de los wrappers) — ambos a aflorar en Lote B WAs `adr` posteriores.
