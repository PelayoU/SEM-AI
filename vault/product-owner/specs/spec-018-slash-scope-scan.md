---
type: spec
id: spec-018-slash-scope-scan
title: "Spec Gherkin para feature-018: Slash /scope-scan (flat parallel advisors + Filtro PO)"
parent: feature-018-slash-scope-scan
related-stories:
  - story-018-A
  - story-018-B
  - story-018-C
related-feature: feature-018-slash-scope-scan
related-capability: cap-04-verificacion-multirol-cruzada
also-relates-to:
  - feature-010-entry-point-por-rol
  - feature-024-contrato-filesystem-changes
  - feature-019-slash-verify
related-adrs:
  - ADR-latente-001
  - ADR-latente-009
depends-on:
  - feature-010-entry-point-por-rol
dimensions-affected: [product, technical, quality]
status: ready-for-implementation
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
ac-count: 9
---

```gherkin
Feature: feature-018-slash-scope-scan — Slash command /scope-scan (flat parallel advisors + Filtro PO)
  Como operador agente orquestador (PO Modo 1 paso 5, o cualquier rol mid-WA)
  Quiero convocar advisors restantes en paralelo, recibir scope-scan-outputs estructurados, consolidar con Filtro PO
  Para producir verificación cross-rol coherente sin secuencialización innecesaria ni contaminación del PO

  Background:
    Given el orquestador conduce un step de WA (o draftea uno nuevo)
    And `vault/shared/governance/role-catalog.md` declara los 8 roles
    And los 5 advisors (architect, designer, business-analyst, security-officer, qa) son invocables vía Task tool
    And la regla 12 del agent file PO declara mecanismos preventivos del Filtro

  # Scenarios de story-018-A: Orquestador convoca 5 advisors en flat parallel
  Scenario: AC-A1 — Invocación en único mensaje con múltiples tool_use blocks
    Given el PO en Modo 1 paso 5 necesita scope-scan inicial al draftar WA
    When construye un mensaje con N=5 tool_use blocks Task (uno por advisor)
    Then Claude Code ejecuta los 5 Task calls en paralelo (flat parallel)
    And NO en secuencia (anti-patrón)

    Given un orquestador no-PO (ej. Architect en WA `adr` puro)
    When construye mensaje con N=6 tool_use blocks (incluye PO entre los advisors)
    Then los 6 corren paralelos

  Scenario: AC-A2 — Cada Task tool call con subagent_type correcto
    Given el PO está construyendo los 5 prompts
    When asigna subagent_type a cada Task tool call
    Then asigna explícitamente:
      | rol              | subagent_type      |
      | Architect        | architect          |
      | Designer         | designer           |
      | Business Analyst | business-analyst   |
      | Security Officer | security-officer   |
      | QA               | qa                 |
    And el harness Claude Code carga el agent file correspondiente al subagent_type

  Scenario: AC-A3 — Prompt focal por advisor con contexto curado
    Given el PO construye el prompt para `architect`
    When el prompt está completo
    Then incluye:
      | sección                                       |
      | Identidad rol (referencia .claude/agents/architect.md) |
      | Propuesta del humano (texto completo)         |
      | Paths del vault a leer (capability padre, ADRs)|
      | Instrucción: devolver scope-scan-output estructurado |
    And cada otro advisor recibe prompt análogo desde su ángulo dimensional

  # Scenarios de story-018-B: Advisor produce scope-scan-output estructurado
  Scenario: AC-B1 — Advisor carga identidad al inicio
    Given el advisor (cualquier rol) recibe el prompt
    When ejecuta su primer Read action
    Then lee `.claude/agents/<su-rol>.md` para cargar identidad
    And el agent file declara: dimensión custodiada, bibliografía, skills, modos de operación
    And el advisor aplica esa identidad en su análisis posterior

  Scenario: AC-B2 — Output estructurado YAML scope-scan-output
    Given el advisor completó su análisis focal
    When devuelve respuesta al orquestador
    Then la respuesta incluye bloque YAML etiquetado `scope-scan-output:`
    And el bloque declara campos mínimos:
      | campo                  | contenido                                   |
      | rol                    | <su-rol>                                     |
      | dimensions-detected    | lista (honestamente vacía si no aplica)      |
      | flags                  | lista con severity y razón                   |
      | questions-for-human    | lista (vacía si no aplica)                  |
      | veredicto              | viable / viable-con-condiciones / no-viable |
    And campos adicionales por rol (ej. architect declara adrs-latentes-detectables; security declara vectores-STRIDE)

  Scenario: AC-B3 — Advisor NO cascadea ni edita salvo declaración explícita
    Given el advisor está produciendo su scope-scan-output
    When detecta que necesita perspectiva de otro rol
    Then NO invoca a otros advisors vía Task tool
    And reporta la necesidad en `questions-for-human` o `flags`
    And el orquestador (típicamente PO) decide si invocar al otro advisor en otro turn

    Given el step del advisor declara `modality: subagente` con autoridad de edición
    When el advisor edita archivos (ej. produce audit en su carpeta)
    Then al cerrar el step DEBE incluir bloque `filesystem-changes` (Gap 9)

  # Scenarios de story-018-C: Orquestador consolida outputs y aplica Filtro PO
  Scenario: AC-C1 — Consolidación de dimensions + flags
    Given el orquestador inspecciona los N outputs
    When consolida dimensions
    Then `dimensions-affected = unión(advisor.dimensions-detected) ∪ {product}` (product asumido por PO)
    And `participants = roles que aportaron algo no vacío`
    And `flags` agregados con rol emisor preservado en cada entrada

  Scenario: AC-C2 — Filtro PO regla 12 obligatorio
    Given los flags están agregados
    When el PO aplica Filtro
    Then clasifica cada flag en una de 4 categorías Cagan:
      | categoría | significado                          |
      | 1         | Acepto y aplico yo (con criterio)    |
      | 2         | Descarto con razón fuerte            |
      | 3         | Difiero a WA futuro                  |
      | 4         | Requiere decisión humana real        |
    And aplica test load-bearing (3 preguntas) sobre cada flag pre-cat-1
    And ejecuta auto-audit numérica:
      | ratio cat-1 / total | acción                                   |
      | > 60%               | high-suspicion → revisar fila por fila   |
      | > 80%               | casi-mecánico → invocar subagente PO     |
    And escribe artefacto declarativo `vault/product-owner/discovery/filtro-po-<wa-id>-<step-id>.md` con tabla por flag

  Scenario: AC-C3 — Presentación al humano solo cat-4
    Given el Filtro PO está completo con artefacto escrito
    When el orquestador presenta resultado al humano
    Then incluye: DECISIONES cat-1 (resumen), DESCARTOS cat-2 (con razón), APARCADOS cat-3 (lista), PREGUNTAS cat-4 (al humano)
    And el humano responde solo a cat-4
    And cat-1, cat-2, cat-3 quedan documentadas en artefacto + entrada Progreso del WA
```

## Notas

- **Verificable vía**: inspección del mensaje del orquestador (N tool_use blocks) + paralelización real Claude Code + outputs YAML estructurados + artefacto `filtro-po-*.md` poblado + Progreso del WA.
- **Aplicado en práctica**: WA-002, WA-003, WA-004, WA-005 — flat parallel + scope-scan-output + Filtro PO con artefacto.
- **Anclaje aprendizaje**: incidente Filtro PO contaminado WA-004 → regla 12 PO.

## Historia del refactor

Consolida spec-018-A/B/C en Gherkin único por feature (Adzic literal). Refactor 2026-05-13.
