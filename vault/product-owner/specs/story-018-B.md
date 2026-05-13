---
type: story
id: story-018-B
title: "Advisor produce scope-scan-output estructurado"
parent: feature-018-slash-scope-scan
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-018-B — Advisor produce scope-scan-output estructurado

## Narrativa

**Como** advisor invocado vía Task tool (architect, designer, business-analyst, security-officer, qa),
**quiero** recibir prompt focal + leer paths del vault declarados + producir `scope-scan-output` estructurado en YAML,
**para** que el orquestador pueda consolidar 5 outputs uniformes sin ambigüedad de formato.

## Examples (discovery)

1. **Architect recibe scope-scan**: lee `.claude/agents/architect.md` para cargar identidad + lee capability padre + propuesta humano + ADRs aplicables. Aplica skills (`coupling-detection`, `coherence-evaluation`, `feature-viability-review` preview). Devuelve `scope-scan-output` con dimensions-detected, cross-links-suggested, ADRs-latentes-detectables, flags (severity bloqueante/mayor/menor), questions-for-human, veredicto-viability.
2. **Designer recibe scope-scan**: aplica Nielsen + Cooper + Norman. Devuelve `scope-scan-output` con capabilities-con-usability-latente, features-usability-candidatas, cross-links, flags, questions.
3. **Business-analyst recibe scope-scan**: aplica Moore + Osterwalder + compliance regulatorio. Devuelve `scope-scan-output` con capabilities-con-business-latente, impacto-deadline-academico, features-business-candidatas, flags.
4. **Security-officer recibe scope-scan**: aplica STRIDE + Shostack. Devuelve `scope-scan-output` con capabilities-con-security-latente (vectores STRIDE), threat-models-candidatos-a-aflorar, AC-S-preview-sugeridos, flags.
5. **QA recibe scope-scan**: aplica Cohn INVEST + Adzic AC coverage + verificabilidad. Devuelve `scope-scan-output` con verificabilidad-del-output-propuesto, necesidad-step-qa, patrón-AC-recomendado, coherencia-catalogo, cobertura-piezas, flags.
6. **Advisor sin contenido relevante**: si el advisor desde su ángulo no detecta nada (dimensiones, flags, cross-links), devuelve listas vacías honestamente — NO infla output para parecer útil.

## Acceptance Criteria

- **AC-B1**: Al recibir prompt, el advisor lee primero su agent file `.claude/agents/<su-rol>.md` para cargar identidad (instrucción explícita en cada agent file).
- **AC-B2**: El advisor devuelve **bloque YAML estructurado** etiquetado `scope-scan-output` con frontmatter mínimo: `rol`, `dimensions-detected`, `flags`, `questions-for-human`, `veredicto`. Campos adicionales por rol.
- **AC-B3**: El advisor **NO cascadea** a otros roles (el orquestador es quien invoca paralelo). NO **edita archivos** (es scope-scan read-only, salvo cuando explícitamente declarado como step de WA con autoridad de edición → en ese caso aplica Gap 9 filesystem-changes).

## Cross-links

- **also-relates-to**: feature-024 (contrato filesystem-changes Gap 9) — los advisors con autoridad de edición deben reportar.

## Test mecánico Adzic SbE

✅ 6 examples concretos (5 advisors + caso vacío honesto).
✅ 3 AC SMART verificables.
✅ Spec Gherkin descendible.

Test mecánico **PASA**.
