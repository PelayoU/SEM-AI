---
type: feature
id: feature-018-slash-scope-scan
title: "Slash `/scope-scan` para reunión multi-rol flat parallel on-demand"

jtbd-outcome: "Cuando el operador agente orquestador (típicamente PO al draftar WA, o cualquier rol mid-trabajo con duda cross-dominio) necesita perspectivas de otros roles sobre una propuesta o artefacto, quiere convocar reunión flat parallel multi-rol (5 advisors en paralelo desde sus ángulos dimensionales) ON-DEMAND con un solo comando, so I can materializar Cagan principio 2 (give-and-take) en formato AI-ejecutable sin ritual ceremonioso."

parent: cap-04-verificacion-multirol-cruzada

dimensions-affected: [product, technical]

depends-on: []
also-relates-to:
  - cap-02-multirol-agentes-homologos  # los 5 advisors existen por CAP-B
depends-on-harness:
  - claude-code-task-tool  # mecanismo de invocación de subagentes
  - paralelizacion-tool-use-blocks  # un mensaje del orquestador con múltiples tool_use

related-adrs:
  - ADR-latente-001  # Claude Code harness primario que provee Task tool
  - ADR-latente-009  # Tres checkpoints uniformes WA lifecycle (scope-scan inicial es uno de ellos)

status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005

fundamento-bibliografico:
  - Cagan — Inspired (principio 2: products are defined and designed collaboratively, rather than sequentially)
  - Anthropic Claude Code docs (Task tool + paralelización via múltiples tool_use blocks)
---

# feature-018 · Slash `/scope-scan` para reunión multi-rol flat parallel on-demand

## Problem

El orquestador de un WA (típicamente PO en Modo 1) necesita perspectivas multi-rol sobre una propuesta antes de comprometer scope. Sin un mecanismo declarativo, el orquestador debería:

1. Recordar manualmente qué 5 advisors existen (architect, designer, business-analyst, security-officer, qa).
2. Construir 5 prompts uno-a-uno con contexto repetitivo.
3. Invocar 5 Task tool calls secuencialmente (no flat parallel).
4. Consolidar outputs sin protocolo.

Esto introduce overhead operativo + riesgo de olvidar advisors + secuencialización innecesaria + Filtro PO manual no formalizado.

## Hypothesis

Si proveemos un **slash command `/scope-scan "<propuesta>"`** que:

1. **Convoca a los 5 advisors restantes en paralelo** (un solo mensaje del orquestador con 5 tool_use blocks).
2. **Cada advisor recibe identidad cargada + propuesta + paths a leer + instrucción focal** desde su ángulo dimensional.
3. **Consolida outputs** aplicando algoritmo declarativo + Filtro PO (feature-023 regla 12).

Entonces el operador orquestador convoca reunión multi-rol con un comando + el algoritmo es uniforme + el resultado es auditable.

## Expected outcome (JTBD)

*Cuando el orquestador necesita perspectivas multi-rol, ejecuta `/scope-scan "<propuesta>"` y recibe 5 outputs paralelos + consolidación + Filtro PO aplicado.*

## Stories

3 stories descomponen feature-018:

- **story-018-A**: Como PO al draftear WA (o cualquier orquestador mid-WA), ejecuto `/scope-scan` y convoco 5 advisors en flat parallel
- **story-018-B**: Como advisor invocado (architect/designer/business-analyst/security-officer/qa), recibo prompt focal + leo paths + devuelvo `scope-scan-output` estructurado
- **story-018-C**: Como orquestador, consolido los 5 outputs aplicando algoritmo + Filtro PO regla 12

## Piezas del bootstrap que materializan esta feature

- Documentación de `/scope-scan` en CLAUDE.md raíz sección "Slash commands"
- Mecanismo Task tool de Claude Code (depends-on-harness)
- Agent files de los 5 advisors (`.claude/agents/architect.md` etc.)
- Aplicado en práctica visible en: WA-002 (capability-creation), WA-003 (doc-edit), WA-004 (aborted-reference), WA-005 (este — scope-scan inicial al draftearse + post-step scope-scan tras steps 2a..2h).

## Notas

- **Three uniform checkpoints** (CAP-D ADR-latente-009): `/scope-scan` aplica en 3 momentos del WA lifecycle: (1) discovery review al crear WA, (2) post-step checkpoint, (3) sign-off via `/verify`. La feature cubre (1) y (2) como invocación on-demand. (3) es feature-019 /verify.
- **Filtro PO regla 12** (protocolo Nivel 3, ya formalizado en agent file PO): tras consolidar outputs, el orquestador aplica el filtro con artefacto declarativo `filtro-po-<wa-id>-<step>.md` obligatorio. La feature-018 NO duplica el protocolo; lo invoca como dependencia.
