---
type: governance
id: role-catalog
title: "Catálogo de roles"
status: active
created: 2026-04-30
author: human
---

# Catálogo de roles

Cada rol tiene un agente homólogo definido en `.sem-ia/agents/`. El launcher busca roles primero en `.sem-ia/roles/` (proyecto) y después en el catálogo core.

## Roles core

| Rol | Modelo | Dimensión custodiada | Agente |
|-----|--------|---------------------|--------|
| Coach | Opus | strategy | `.sem-ia/agents/coach.md` |
| Product Owner | Opus | product | `.sem-ia/agents/product-owner.md` |
| Architect | Opus | technical | `.sem-ia/agents/architect.md` |
| Backend-dev | Sonnet | (implementación) | `.sem-ia/agents/backend-dev.md` |
| Security Officer | Opus | security | `.sem-ia/agents/security-officer.md` |
| QA | Sonnet | quality | `.sem-ia/agents/qa.md` |
| DBA | Sonnet | data | `.sem-ia/agents/dba.md` |
| Quant | Opus | quant-validation | `.sem-ia/agents/quant.md` |

## Custodio principal por tipo de nodo

| Tipo de nodo | Custodio principal | Dimensión dominante |
|---|---|---|
| Visión | Coach | strategy |
| Goals | Coach | strategy |
| Capabilities | Coach | strategy |
| Features | Product Owner | product |
| Stories | Product Owner | product |
| Specs (Gherkin) | Product Owner | product |
| ADRs | Architect | technical |
| Working Agreements | Recepción + humano | governance |
| Reviews | Custodio que revisa | varía |
| Learnings | Quien lo aprende | varía |

## Extensión

Cada proyecto puede crear roles adicionales en `.sem-ia/roles/` siguiendo el mismo patrón de markdown con frontmatter. Ejemplos para dominios específicos:

- Tokenomics-designer, Smart-contract-auditor, DeFi-protocol-researcher (DeFi)
- Risk-analyst, Market-researcher (Fintech)
- Product-designer (UX dedicado)
