---
type: feature
id: feature-019-slash-verify
title: "Slash `/verify` con algoritmo declarativo `verifiers = {custodian(d)}`"

jtbd-outcome: "Cuando el humano necesita cerrar un Working Agreement al completar todos sus steps, quiere ejecutar `/verify` y que el PO derive mecánicamente verificadores (algoritmo `verifiers = {custodian(d) : d ∈ dimensions-affected}`), los invoque en paralelo, consolide hallazgos, aplique on-close transitions y archive el WA, so I can el sign-off es algoritmo declarativo auditable y no juicio caso-a-caso del PO."

parent: cap-04-verificacion-multirol-cruzada

dimensions-affected: [product, quality]

depends-on:
  - feature-009-catalogo-roles  # mapping custodian(d) → rol
  - feature-018-slash-scope-scan  # paralelización subagentes
also-relates-to:
  - cap-01-grafo-declarativo-persistente  # on-close transita estados canónicos
  - cap-03-working-agreements-sdlc  # consume on-close del WA
depends-on-harness:
  - claude-code-task-tool

related-adrs:
  - ADR-latente-010  # Algoritmo declarativo verifiers
  - ADR-latente-009  # Tres checkpoints uniformes (sign-off es el tercero)

status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005

fundamento-bibliografico:
  - Cagan — Inspired (strong PM: algoritmo declarativo, no juicio mecánico ad-hoc)
  - Nygard — Documenting Architecture Decisions (algoritmo verifiers como decisión arquitectónica con alternatives)
  - Anthropic Claude Code docs (Task tool + paralelización)
---

# feature-019 · Slash `/verify` con algoritmo declarativo

## Problem

Al cerrar un Working Agreement (todos los steps completados), el sign-off debe ser:
1. **Reproducible**: el mismo WA con las mismas dimensiones produce los mismos verificadores.
2. **Auditable**: el algoritmo es declarativo y trazable a `dimensions.md` (mapping dimensión → custodio).
3. **Mecánico**: NO depende de juicio caso-a-caso del PO sobre "a quién pregunto".

Sin un slash command con algoritmo declarativo, el sign-off sería juicio ad-hoc — el PO debería recordar qué dimensiones declaró + a qué custodio invocar + en qué orden + qué transitions aplicar al cierre.

## Hypothesis

Si proveemos slash `/verify` que aplica algoritmo declarativo:

```
verifiers = {custodian(d) : d ∈ wa.dimensions-affected}
```

donde `custodian(d)` es lookup en `vault/shared/governance/dimensions.md`, entonces:

1. La lista de verificadores es derivada mecánicamente del frontmatter del WA.
2. La invocación es flat parallel (heredada de feature-018).
3. Las transiciones `on-close` se aplican mecánicamente (lookup en frontmatter del WA + Edit en cada path declarado).
4. El archivado mueve el WA de `active/` a `archive/` deterministicamente.

## Expected outcome (JTBD)

*Cuando el humano ejecuta `/verify` al cierre de un WA, el PO aplica algoritmo declarativo: deriva verifiers → invoca paralelo → consolida → aplica on-close → archiva. Sign-off auditable + reproducible.*

## Stories

4 stories descomponen feature-019:

- **story-019-A**: Como humano, ejecuto `/verify` y el PO comprueba closure-criteria mecánicamente
- **story-019-B**: Como PO al /verify, derivo verifiers aplicando algoritmo declarativo desde dimensions-affected
- **story-019-C**: Como PO al /verify, invoco verificadores en paralelo y consolido hallazgos
- **story-019-D**: Como PO al /verify, aplico on-close transitions y archivo el WA (incluyendo transición de specs Gherkin `draft → ready-for-implementation` que alimenta el backlog emergente)

## Piezas del bootstrap que materializan esta feature

- Documentación de `/verify` en CLAUDE.md raíz sección "Slash commands"
- `vault/shared/governance/dimensions.md` (mapping dimensión → custodio)
- `vault/shared/sessions/active/` y `vault/shared/sessions/archive/` (rutas de WA pre/post archive)
- Aplicado en práctica visible en: WA-002 (/verify aprobado, capabilities transitaron a active), WA-003 (/verify aprobado, 10 gaps procesados), próximamente WA-005 al cierre.

## Notas

- **AC adicional absorbido de feature-005 reclasificada**: AC-D2 del spec-019-D declara explícitamente que on-close de un WA `feature-design` transita specs Gherkin `draft → ready-for-implementation`, alimentando el backlog query emergente. Esto es lo que story-005-C iba a cubrir antes de reclasificación.
- **Three uniform checkpoints**: `/verify` es el **tercer** checkpoint del WA lifecycle (los otros dos son cubiertos por feature-018 `/scope-scan`: discovery review al crear + post-step checkpoint).
