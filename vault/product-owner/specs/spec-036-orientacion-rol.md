---
type: spec
id: spec-036-orientacion-rol
title: "Spec Gherkin para feature-036: Orientación + recovery por rol"
parent: feature-036-orientacion-rol
related-stories:
  - story-036-A
  - story-036-B
related-feature: feature-036-orientacion-rol
related-capability: cap-06-visibilidad-operativa
also-relates-to:
  - feature-011-claude-md-raiz
  - feature-034-slash-sessions
related-adrs: []
depends-on: []
dimensions-affected: [product, usability]
status: ready-for-implementation
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
ac-count: 6
---

```gherkin
Feature: feature-036-orientacion-rol — Orientación + recovery por rol
  Como operador humano newcomer o experimentado ante propuesta ambigua
  Quiero consultar criterio de orientación accesible + recibir recovery cuando estoy en sesión equivocada
  Para elegir sesión correcta sin retrasos y recuperar sin perder tiempo (Nielsen #9)

  Background:
    Given el repo SEM-IA está clonado
    And `vault/shared/governance/role-catalog.md` declara roles + atajos

  # Scenarios de story-036-A: Operador consulta criterio antes de arrancar
  Scenario: AC-A1 — CLAUDE.md raíz incluye criterio "si dudas"
    Given el operador abre CLAUDE.md raíz
    When busca sección "Cómo arrancar trabajo"
    Then encuentra:
      | criterio                                            | acción                              |
      | Por defecto (cualquier propuesta product/estratégica)| `npm run sem`                       |
      | Trabajo puramente técnico (ADR puro, refactor)      | `npm run arch`                      |
      | Trabajo puramente operativo (pipeline, infra)       | `npm run ops`                       |
      | Trabajo security focal (threat-model standalone)    | `npm run sec`                       |
      | Trabajo design focal (audit usability standalone)   | `npm run des`                       |
    And el criterio termina con "Si dudas: arranca `npm run sem`, el PO clasifica"

  Scenario: AC-A2 — Agent file PO declara tabla decisión conduzco/delego
    Given el operador inspecciona `.claude/agents/product-owner.md`
    When busca sección Modo 1 paso 4
    Then encuentra tabla "TÚ CONDUCES si..." vs "DELEGAS si..."
    And la tabla cita bibliografía aplicable (Cagan principio decision rights)

  Scenario: AC-A3 — /sessions output incluye descripción cuándo invocar
    Given el operador ejecuta `/sessions`
    When inspecciona la columna "Para qué"
    Then cada rol tiene descripción 1-línea concreta del JTBD del rol
    And el operador puede decidir cuál abrir leyendo solo esa columna

  # Scenarios de story-036-B: Recovery cuando operador en sesión equivocada
  Scenario: AC-B1 — Rol detecta scope ajeno
    Given el operador arrancó `npm run arch` (Architect)
    And trae propuesta "diseñar feature de login (product)"
    When Architect lee la propuesta
    Then aplica criterio de su agent file sección "Lo que NO haces" + "Cuándo eres invocado"
    And detecta que el scope es product (no technical puro)
    And NO procede a draftar WA `feature-design` (eso es PO)

  Scenario: AC-B2 — Comunica recovery al humano
    Given Architect detectó scope ajeno
    When responde al humano
    Then incluye:
      | componente del mensaje                                   |
      | Reconocimiento: "Esta no es decisión de mi dominio"      |
      | Razón corta: "Es propuesta de producto (no ADR puro)"     |
      | Sugerencia: "Sal y abre `npm run sem`"                   |
      | Explicación: "PO clasificará. Si emerge dimensión technical, me invocará como subagente en scope-scan."  |
    And el mensaje es claro + no condescendiente

  Scenario: AC-B3 — Rol NO ejecuta acciones del dominio ajeno
    Given Architect comunicó recovery
    When el humano confirma o cierra la sesión
    Then Architect NO drafta WA `feature-design`
    And NO produce artefactos en `vault/architect/`
    And espera al humano (que cierra sesión arch y arranca sem)

    Given el operador trae propuesta legítima del dominio del rol
    When el rol detecta scope propio
    Then procede normalmente (no aplica recovery)
```

## Notas

- **Verificable vía**: inspección de CLAUDE.md raíz + agent file PO + ejecución `/sessions` + sesión real con rol equivocado.
- **Anclaje en agent files**: cada agent file declara sección "Lo que NO haces" + "Cuándo eres invocado" que activa el recovery.

## Historia del refactor

Consolida spec-036-A/B en Gherkin único. Refactor 2026-05-13.
