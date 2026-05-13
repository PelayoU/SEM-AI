---
type: spec
id: spec-019-slash-verify
title: "Spec Gherkin para feature-019: Slash /verify (closure-criteria + derivación verifiers + sign-off + on-close)"
parent: feature-019-slash-verify
related-stories:
  - story-019-A
  - story-019-B
  - story-019-C
  - story-019-D
related-feature: feature-019-slash-verify
related-capability: cap-04-verificacion-multirol-cruzada
also-relates-to:
  - feature-009-catalogo-roles
  - feature-018-slash-scope-scan
  - feature-001-vault-role-first
related-adrs:
  - ADR-latente-001
  - ADR-latente-004
  - ADR-latente-008
  - ADR-latente-010
depends-on:
  - feature-009-catalogo-roles
  - feature-018-slash-scope-scan
dimensions-affected: [product, technical, quality]
status: ready-for-implementation
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
ac-count: 12
---

```gherkin
Feature: feature-019-slash-verify — Slash command /verify (cierre canónico de WA)
  Como operador humano al cierre de un WA
  Quiero ejecutar /verify y que el PO comprueba closure-criteria, derive verifiers, invoque sign-off paralelo, consolide y aplique on-close
  Para finalizar el lifecycle del WA con verificación cross-rol auditable y backlog alimentado deterministicamente

  Background:
    Given un WA activo en `vault/shared/sessions/active/wa-NNN.md`
    And el WA declara `closure-criteria`, `dimensions-affected`, `on-close` en frontmatter
    And `vault/shared/governance/dimensions.md` declara mapping dimensión → custodio

  # Scenarios de story-019-A: Humano ejecuta /verify, PO comprueba closure-criteria
  Scenario: AC-A1 — Comprobación previa de steps done
    Given el humano ejecuta `/verify` sobre el WA
    When PO inspecciona el frontmatter de steps[]
    Then verifica que cada step tiene `status: done`
    And si alguno NO, presenta lista de steps incompletos al humano
    And NO procede a derivar verifiers

  Scenario: AC-A2 — Comprobación mecánica de closure-criteria observables
    Given los steps están todos done
    When PO procesa cada entrada de `closure-criteria`
    Then aplica verificación mecánica por entrada:
      | criterio enumerable                         | verificable vía                       |
      | "Todos los steps en status: done"            | inspección frontmatter steps[]         |
      | "Por cada capability operant: ≥1 feature"   | grep features/ + match con cap-list     |
      | "Tabla cobertura sin gaps"                  | inspección discovery doc                |
      | "Cada AC con identificador único"            | grep en specs/                         |
      | "filesystem-changes registrado en Progreso" | grep en cuerpo del WA                  |
    And solo criterios mecánicamente verificables (no subjetivos)

  Scenario: AC-A3 — Falla informativa con ubicación
    Given algún closure-criterion falla
    When PO termina la comprobación
    Then presenta al humano:
      | criterio que falla            |
      | ubicación de la falla         |
      | acción sugerida para resolver |
    And NO invoca verifiers
    And el humano resuelve y re-ejecuta `/verify`

  # Scenarios de story-019-B: PO deriva verifiers desde dimensions-affected
  Scenario: AC-B1 — Algoritmo declarativo verifiers = {custodian(d)}
    Given el WA frontmatter declara `dimensions-affected: [product, technical, quality]`
    When PO aplica algoritmo
    Then consulta dimensions.md y obtiene:
      | dimensión  | custodio        |
      | product    | product-owner   |
      | technical  | architect       |
      | quality    | qa              |
    And lista de verifiers = {product-owner, architect, qa}

    Given el WA frontmatter declara las 6 dimensiones [product, technical, usability, business, security, quality]
    When PO aplica algoritmo
    Then verifiers = {product-owner, architect, designer, business-analyst, security-officer, qa}
    And lista de 6 custodios

  Scenario: AC-B2 — Override explícito de verifiers-required
    Given el WA frontmatter declara `verifiers-required: [product-owner, architect]` (override consciente)
    And `dimensions-affected` declara [product, technical, quality]
    When PO procesa /verify
    Then respeta `verifiers-required` declarado
    And NO invoca a qa automáticamente
    And el override es decisión consciente del PO al draftar (auditable en frontmatter)

  Scenario: AC-B3 — Lista deduplicada
    Given el WA hipotético tiene `dimensions-affected` con dos dimensiones que comparten custodio
    When PO deriva verifiers
    Then la lista resultante NO repite custodios
    And cada custodio aparece una sola vez

  # Scenarios de story-019-C: PO invoca verificadores en paralelo y consolida
  Scenario: AC-C1 — Invocación flat parallel en único mensaje
    Given N verifiers derivados (ej. 6 para WA con todas las dimensiones)
    When PO invoca el sign-off
    Then construye **un único mensaje** con N tool_use blocks Task
    And cada Task con subagent_type correspondiente al custodio
    And Claude Code los ejecuta en paralelo

  Scenario: AC-C2 — Prompt focal por verifier
    Given PO construye prompts
    When asigna prompt a cada verifier
    Then incluye:
      | sección                                       |
      | Identidad del rol custodio                    |
      | WA completo (frontmatter + cuerpo + Progreso) |
      | Paths del vault relevantes a su dimensión      |
      | Tarea: verificar artefactos producidos en su dimensión |
      | Output esperado: aprobado / objeción menor / objeción bloqueante con razón |

  Scenario: AC-C3 — Consolidación clasificada
    Given los N outputs recibidos en paralelo
    When PO consolida
    Then clasifica los hallazgos:
      | clasificación        | acción del PO                                |
      | Todos aprueban       | Procede a on-close (story-019-D)             |
      | Objeción bloqueante  | WA vuelve a status: active + indica humano    |
      | Objeción menor       | Presenta al humano 3 opciones: resolver / aparcar / aceptar |
    And aplica Filtro PO regla 12 sobre objeciones (test load-bearing por objeción)

  # Scenarios de story-019-D: PO aplica on-close y archiva WA
  Scenario: AC-D1 — Aplicación secuencial de on-close transitions
    Given el WA tiene N entradas de on-close
    When PO procesa cada entrada
    Then por cada entrada:
      | acción del PO                                |
      | Lee el archivo en el path declarado          |
      | Verifica status actual = status-inicial      |
      | Si NO matchea → presenta al humano antes de aplicar |
      | Si matchea → modifica frontmatter status = status-final via Edit |
    And procesa las N entradas secuencialmente
    And cero archivos modificados si alguno NO matchea (transaccional)

  Scenario: AC-D2 — Specs Gherkin transitan a ready-for-implementation (backlog)
    Given WA `feature-design` con specs Gherkin formales producidos
    And el on-close declara `vault/product-owner/specs/spec-*.md: draft → ready-for-implementation`
    When PO aplica on-close
    Then cada spec Gherkin transita `draft → ready-for-implementation`
    And el backlog query emergente `find vault/ -name "spec-*.md" | xargs grep -l "status: ready-for-implementation"` incluye estos specs

    Given el mismo WA `feature-design` con features y stories (sin Gherkin formal por sí mismos — Gherkin vive en specs)
    When on-close transita features y stories
    Then transita `draft → active` (NO `ready-for-implementation`)
    And features/stories NO entran al backlog query
    And solo specs Gherkin formales con AC son los nodos del backlog para futuros WAs `feature-build`

  Scenario: AC-D3 — Archivado del WA + metadata + confirmación
    Given todas las on-close transitions aplicadas
    When PO archiva el WA
    Then mueve `vault/shared/sessions/active/wa-NNN.md` a `vault/shared/sessions/archive/wa-NNN.md`
    And actualiza frontmatter del WA archivado:
      | campo         | valor                                    |
      | status        | archived                                 |
      | archived-at   | ISO datetime de cierre                   |
      | verified-at   | ISO datetime de aprobación verifiers     |
      | verified-by   | lista de roles que aprobaron             |
    And presenta al humano confirmación final:
      | resumen                                                 |
      | Lista de transiciones aplicadas (path + transición)     |
      | Path del WA archivado                                   |
      | Lista de verifiers que aprobaron                        |
```

## Notas

- **Verificable vía**: ejecución `/verify` real + inspección filesystem (WA en archive/) + grep nodos transitados + frontmatter WA archivado con metadata completa.
- **Aplicado en práctica**: WA-002 (2026-05-12T05:30, 10 capabilities), WA-003 (2026-05-12T09:10), WA-005 (transitará ~30-50 specs `ready-for-implementation`).
- **Backlog query emergente**: cubierto por AC-D2. NO es feature aparte — propiedad declarativa del algoritmo on-close.

## Historia del refactor

Consolida spec-019-A/B/C/D (4 specs) en Gherkin único por feature. Refactor 2026-05-13.
