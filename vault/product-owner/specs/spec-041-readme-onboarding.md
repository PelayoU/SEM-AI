---
type: spec
id: spec-041-readme-onboarding
title: "Spec Gherkin para feature-041: README onboarding (tesis + corpus bibliográfico + cautelas privacidad)"
parent: feature-041-readme-onboarding
related-stories:
  - story-041-A
  - story-041-B
  - story-041-C
related-feature: feature-041-readme-onboarding
related-capability: cap-10-articulacion-publica
also-relates-to: []
related-adrs: []
depends-on: []
dimensions-affected: [product, usability, business, security]
status: ready-for-implementation
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
ac-count: 9
---

```gherkin
Feature: feature-041-readme-onboarding — README onboarding público
  Como newcomer / evaluador académico / adopter externo
  Quiero leer README.md y comprender tesis + modelo + arranque + atribución bibliográfica + cautelas de privacidad
  Para decidir informado si adoptar, evaluar rigor académico, o proteger información sensible antes de adoptar

  Background:
    Given README.md raíz existe en el repo

  # Scenarios de story-041-A: Newcomer comprende tesis + modelo + arranque
  Scenario: AC-A1 — Tesis filosófica en primeras 50 líneas
    Given newcomer abre README
    When lee las primeras 50 líneas
    Then encuentra tesis filosófica: "El trabajo con IA requiere su propia infraestructura de gestión..."
    And la tesis conecta con el horizonte (5-10 años vigencia estratégica)

  Scenario: AC-A2 — Modelo conceptual con diagrama
    Given newcomer continúa leyendo
    When llega a sección "Modelo conceptual"
    Then encuentra:
      | elemento                                       |
      | Flujo espina dorsal (Visión → Goals → ... → Artifacts) |
      | 8 roles custodios + dimensión por rol         |
      | 7 dimensiones del producto holístico          |
      | 14 workflow templates indexados por fase SDLC  |
      | Cagan dual track Discovery/Delivery           |

  Scenario: AC-A3 — Cómo arrancar trabajo
    Given newcomer quiere usar el framework
    When busca sección "Cómo arrancar trabajo"
    Then encuentra tabla rol → atajo npm
    And ejemplo "Para arrancar: `npm run sem`"
    And criterio de delegación si propuesta es de otro dominio

  # Scenarios de story-041-B: Evaluador académico ve atribución bibliográfica
  Scenario: AC-B1 — Citas inline en formato breve
    Given el README menciona conceptos clave
    When evaluador busca citas
    Then encuentra patrones `(Autor, Año, Obra)`:
      | concepto             | cita esperada                                  |
      | Dual Track            | (Cagan, Inspired; Patton, User Story Mapping)  |
      | INVEST                | (Cohn, User Stories Applied)                   |
      | Specification by Example | (Adzic, Specification by Example)           |
      | ADRs                  | (Nygard)                                        |

  Scenario: AC-B2 — Sección "Anclaje bibliográfico" con corpus
    Given evaluador busca sección dedicada
    When encuentra "Anclaje bibliográfico"
    Then la sección lista:
      | elemento                                                |
      | 18 notas en vault/architect/research/library/           |
      | Referencia a INDEX.md                                   |
      | Referencia a bootstrap-summary.md (16 decisiones + 8 lecciones) |

  Scenario: AC-B3 — LICENSE Apache 2.0 declarada
    Given evaluador busca LICENSE info
    When encuentra sección LICENSE en README
    Then declara "Apache 2.0"
    And justifica brevemente ("sin riesgo viral; permite fork comercial + comunitaria")

  # Scenarios de story-041-C: Cautelas de privacidad para adopters
  Scenario: AC-C1 — Sección dedicada visible
    Given adopter lee README
    When busca cautelas de privacidad
    Then encuentra sección con encabezado visible (ej. "Cautelas para adopters" o "Privacy considerations")
    And la sección NO está oculta al final del documento

  Scenario: AC-C2 — Explica blast radius del vault + qué NO commitear
    Given adopter lee la sección
    When inspecciona el contenido
    Then la sección declara:
      | declaración                                              |
      | El vault es ground truth público por diseño              |
      | Si el repo se abre o se filtra, vault entero queda público |
    And lista qué NO commitear:
      | NO commitear                                |
      | Credenciales en frontmatter                  |
      | Tokens en Progreso entries                   |
      | Datos de clientes en specs                   |
      | Información comercial sensible en discovery  |

  Scenario: AC-C3 — Honestidad Shostack: vectores STRIDE declarados
    Given adopter sofisticado lee las cautelas
    When busca vectores específicos
    Then encuentra mención explícita:
      | vector | explicación                                  |
      | I      | /status agrega vault completo — secrets accidentales en frontmatter expuestos en output |
      | R      | Progreso entries auto-reportadas — sin trazabilidad criptográfica nativa |
    And la sección declara honestamente "SEM-IA opera con honest-agent assumption explícita; NO protege contra agente desalineado con write access"
```

## Notas

- **Verificable vía**: inspección de `README.md` raíz + grep de secciones canónicas + comparación con threat-model preview (step-6 security del WA-005).
- **Anclaje**: Shostack — declarar threat surface real, no aparentar protección inexistente.

## Historia del refactor

Consolida spec-041-A/B/C en Gherkin único. Refactor 2026-05-13.
