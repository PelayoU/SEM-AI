---
type: spec
id: spec-010-entry-point-por-rol
title: "Spec Gherkin para feature-010: Entry point por rol vía atajos npm"
parent: feature-010-entry-point-por-rol
related-stories:
  - story-010-A
  - story-010-B
  - story-010-C
related-feature: feature-010-entry-point-por-rol
related-capability: cap-02-multirol-agentes-homologos
also-relates-to:
  - feature-035-ritual-inicio-po
  - feature-041-readme-onboarding
  - feature-009-catalogo-roles
  - feature-011-claude-md-raiz
related-adrs:
  - ADR-latente-001
  - ADR-latente-002
depends-on: []
dimensions-affected: [product, technical, usability]
status: ready-for-implementation
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
ac-count: 9
---

```gherkin
Feature: feature-010-entry-point-por-rol — Entry point por rol vía atajos npm
  Como operador humano o agente
  Quiero arrancar y cargar la identidad de un rol custodio con un único comando convencional (`npm run <atajo>`)
  Para entrar al framework SEM-IA por el rol apropiado sin teclear paths ni leer documentación previa

  Background:
    Given el repo SEM-IA está clonado
    And `node_modules` está instalado (npm install ejecutado al menos una vez)
    And el binario `claude` (Claude Code CLI) está en PATH

  # Scenarios de story-010-A: Arrancar sesión de rol vía atajo npm
  Scenario: AC-A1 — package.json declara los 9 scripts
    Given el operador inspecciona `package.json` raíz
    When ejecuta `cat package.json | jq '.scripts | keys'`
    Then la salida incluye los 9 atajos: ["sem", "po", "arch", "des", "biz", "sec", "qa", "dev", "ops"]
    And NO incluye atajos para roles inexistentes

  Scenario: AC-A2 — Cada script arranca Claude Code en el directorio del rol
    Given el operador ejecuta `npm run arch`
    When npm interpreta el script
    Then el comando subyacente cambia el directorio de trabajo a `vault/architect/`
    And ejecuta el binario `claude` desde ese directorio
    And el mecanismo CLAUDE.md jerárquico de Claude Code carga `vault/architect/CLAUDE.md` (wrapper)
    And el wrapper referencia `.claude/agents/architect.md` (identidad del rol)

  Scenario: AC-A3 — Identidad cargada verificable en sesión
    Given una sesión arrancada por `npm run sem`
    When el operador hace primer prompt al agente
    Then el agente opera como Product Owner extendido
    And en su respuesta cita su agent file (`.claude/agents/product-owner.md`)
    And ejecuta el ritual de inicio (Modo 1 paso 1) si el vault tiene contenido

    Given una sesión arrancada por `npm run arch`
    When el operador hace primer prompt
    Then el agente opera como Architect
    And en su respuesta cita Nygard / Bass / Ford según contexto (bibliografía del rol Architect)

  # Scenarios de story-010-B: Newcomer descubre scripts disponibles
  Scenario: AC-B1 — package.json declara los 9 scripts con nombres convencionales
    Given el operador inspecciona el repo
    When ejecuta `cat package.json | jq '.scripts'`
    Then la salida incluye los 9 atajos: sem, po, arch, des, biz, sec, qa, dev, ops
    And los nombres siguen convención corta (3-4 caracteres por rol)
    And el atajo `sem` es alias del entry-point principal (PO)

  Scenario: AC-B2 — README incluye tabla rol → atajo
    Given el newcomer abre `README.md` raíz
    When busca sección "Cómo arrancar trabajo"
    Then encuentra tabla con columnas Rol | Atajo | Para qué
    And la tabla declara los 8 roles + el alias sem

  Scenario: AC-B3 — CLAUDE.md raíz incluye tabla rol → atajo
    Given el operador (humano o agente) lee `CLAUDE.md` raíz
    When busca sección que liste atajos npm
    Then encuentra tabla con descripción "para qué" de cada rol
    And la tabla es consistente con la del README

  # Scenarios de story-010-C: Agente al arrancar carga identidad via wrapper jerárquico
  Scenario: AC-C1 — Wrapper por rol referencia explícitamente el agent file
    Given el operador inspecciona los wrappers
    When ejecuta `cat vault/product-owner/CLAUDE.md`
    Then el wrapper referencia explícitamente `.claude/agents/product-owner.md`
    And el wrapper declara "Antes de hacer cualquier cosa, lee .claude/agents/product-owner.md"

    Given el operador inspecciona `vault/architect/CLAUDE.md`
    When lee el wrapper
    Then el wrapper referencia `.claude/agents/architect.md`

    Given el wrapper de developer está pendiente
    When el operador ejecuta `ls vault/developer/CLAUDE.md`
    Then el archivo NO existe (gap menor declarado en feature-010 notas)

  Scenario: AC-C2 — Claude Code carga el wrapper automáticamente
    Given la sesión arranca con `npm run sem`
    And el script ejecuta `cd vault/product-owner/ && claude`
    When Claude Code arranca en el directorio
    Then el mecanismo CLAUDE.md jerárquico carga `vault/product-owner/CLAUDE.md` automáticamente
    And carga también `CLAUDE.md` raíz (parent jerárquico)
    And el agente tiene ambos contextos disponibles antes del primer prompt

  Scenario: AC-C3 — Agent file declara identidad completa
    Given el agent file de un rol está cargado
    When el operador inspecciona su contenido
    Then declara:
      | sección                                |
      | Identidad core (dimensión custodiada)   |
      | Bibliografía aplicable                  |
      | Modos de operación (1-4 según rol)      |
      | Reglas operativas                       |
      | Skills disponibles                      |
      | Lo que NO hace                          |
    And cada sección está poblada con contenido específico del rol
```

## Notas

- **Verificable vía**: ejecución real de `npm run <atajo>` en terminal + inspección de los 7 wrappers + 8 agent files + comportamiento del agente al arrancar + grep filesystem (`cat package.json`, `cat README.md`, `cat CLAUDE.md`).
- **Trazabilidad a tests futuros**: cuando exista `sem-ia check` validador o test E2E del bootstrap, anotará `// @ac-coverage: AC-A1..A3, AC-B1..B3, AC-C1..C3`.
- **Decisión arquitectónica**: ADR-latente-001 (Claude Code v1 como harness) + ADR-latente-002 (vault role-first como prereq de los wrappers).
- **Gap menor declarado**: wrapper developer pendiente. AC-C1 lo reconoce explícitamente (la spec no oculta el gap).

## Historia del refactor

Consolida spec-010-A, spec-010-B, spec-010-C en un único Gherkin POR FEATURE (Adzic literal). Refactor 2026-05-13.
