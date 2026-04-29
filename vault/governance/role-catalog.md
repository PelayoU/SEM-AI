---
type: governance
id: role-catalog
title: "Catálogo de roles"
status: active
created: 2026-04-30
author: human
---

# Catálogo de roles

Cada rol tiene un agente homólogo definido como markdown con frontmatter. El launcher busca roles en este orden:

1. `.sem-ia/roles/` (proyecto) — sobreescribe cualquier core
2. `.sem-ia/agents/` (core SEM clásica) — siempre disponible

## Roles core (SEM clásica)

| Rol | Modelo | Dimensión custodiada | Agente |
|-----|--------|---------------------|--------|
| Coach | Opus | strategy | `.sem-ia/agents/coach.md` |
| Product Owner | Opus | product | `.sem-ia/agents/product-owner.md` |
| Architect | Opus | technical | `.sem-ia/agents/architect.md` |
| Developer | Sonnet | (implementa, sin dimensión) | `.sem-ia/agents/developer.md` |
| QA | Sonnet | quality | `.sem-ia/agents/qa.md` |
| Security Officer | Opus | security | `.sem-ia/agents/security-officer.md` |
| DevOps | Sonnet | operations | `.sem-ia/agents/devops.md` |

## Custodio principal por tipo de nodo

| Tipo de nodo | Custodio principal | Dimensión dominante |
|---|---|---|
| Visión | Coach | strategy |
| Goals | Coach | strategy |
| Capabilities | Coach | strategy |
| Features | Product Owner | product |
| Stories | Product Owner | product |
| Specs (Gherkin) | Product Owner | product |
| ADRs | Architect (típicamente) | technical |
| Working Agreements | Recepción + humano | governance |
| Reviews | Custodio que revisa | varía |
| Learnings | Quien lo aprende | varía |

## Roles del proyecto

Cualquier proyecto puede crear roles adicionales en `.sem-ia/roles/` siguiendo el mismo patrón de markdown con frontmatter. Casos típicos:

- **Especialización del Developer:** `backend-dev`, `frontend-dev`, `mobile-dev`, `smart-contract-dev`. Sobreescriben `developer` cuando aplica.
- **Roles para dimensiones extra declaradas:** `dba` (si el proyecto declara dimensión `data`), `product-designer` (si declara `ux`), `quant` (si declara `quant-validation`), `tokenomics-designer`, `risk-analyst`, etc.
- **Roles propios del dominio:** `defi-protocol-researcher`, `market-researcher`, etc.

Cada rol nuevo declarado en el proyecto debe alinearse con una dimensión del catálogo de `vault/governance/dimensions.md`. Si introduces un rol sin dimensión, es un rol de implementación (como `developer`).
