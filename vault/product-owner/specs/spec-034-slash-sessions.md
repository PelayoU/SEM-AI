---
type: spec
id: spec-034-slash-sessions
title: "Spec Gherkin para feature-034: Slash /sessions (catálogo roles + atajos npm)"
parent: feature-034-slash-sessions
related-stories:
  - story-034-A
related-feature: feature-034-slash-sessions
related-capability: cap-06-visibilidad-operativa
also-relates-to:
  - feature-009-catalogo-roles
related-adrs: []
depends-on: []
dimensions-affected: [product, usability]
status: ready-for-implementation
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
ac-count: 3
---

```gherkin
Feature: feature-034-slash-sessions — Slash /sessions (catálogo roles + atajos)
  Como operador humano
  Quiero ver tabla compacta de roles + atajos npm + cuándo invocar
  Para elegir sesión correcta sin abrir README ni package.json

  Background:
    Given el operador está en sesión Claude Code

  # Scenarios de story-034-A: Catálogo roles + atajos visible con /sessions
  Scenario: AC-A1 — Output con tabla de 4 columnas
    Given el operador ejecuta `/sessions`
    When el slash produce output
    Then incluye tabla con columnas:
      | columna             | contenido                                         |
      | Rol                  | nombre del rol custodio                            |
      | Atajo npm            | `npm run <atajo>` (sem/po/arch/des/biz/sec/qa/dev/ops) |
      | Dimensión custodiada | product / technical / usability / business / security / quality / operations |
      | Para qué             | 1 línea descriptiva del JTBD del rol               |

  Scenario: AC-A2 — Cobertura completa de 8 roles + alias
    Given el output produce la tabla
    When el operador la inspecciona
    Then incluye 9 filas:
      | rol               | atajo |
      | Product Owner     | sem (alias) o po |
      | Architect         | arch  |
      | Designer          | des   |
      | Business Analyst  | biz   |
      | Security Officer  | sec   |
      | QA                | qa    |
      | Developer         | dev   |
      | DevOps            | ops   |

  Scenario: AC-A3 — Coherente con role-catalog.md
    Given el operador inspecciona role-catalog.md
    When compara con el output de `/sessions`
    Then las filas coinciden (rol + atajo + dimensión)
    And NO hay contradicciones (`/sessions` deriva el contenido de role-catalog.md, no duplica)
```

## Notas

- **Verificable vía**: ejecución `/sessions` + comparación con `vault/shared/governance/role-catalog.md` + `package.json`.

## Historia del refactor

Feature con una sola story (story-034-A). Spec única migrada al nuevo naming canónico POR FEATURE. Refactor 2026-05-13.
