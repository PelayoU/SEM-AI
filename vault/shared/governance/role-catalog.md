---
type: governance
id: role-catalog
title: "Catálogo de roles"
status: active
created: 2026-04-30
author: human
materializes-feature: [feature-010-entry-point-por-rol, feature-034-slash-sessions]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): catálogo de 8 roles + atajos npm + custodios consumido por feature-010 (entry-point) y feature-034 (/sessions).
---

# Catálogo de roles

Cada rol tiene un agente homólogo definido como markdown con frontmatter. Los agentes se descubren así:

- **Subagent definitions** en `.claude/agents/<rol>.md` — identidad cuando el rol es invocado vía Task tool por recepción u otro rol.
- **Sesiones dedicadas** en `vault/<subdir>/CLAUDE.md` — identidad cuando el humano abre sesión Claude Code en el subdirectorio del rol (PO extendido en `vault/product-owner/` — cubre `strategy/`, `specs/`, `discovery/`; Architect en `vault/architect/adrs/` o `vault/architect/research/`; etc.).
- **Skills del rol** en `.claude/skills/<rol>/<skill>/SKILL.md`.

Extensiones del proyecto (roles específicos del dominio) se añaden siguiendo el mismo patrón en `.claude/agents/` y `.claude/skills/`.

## Roles core (SEM-IA — alineado con los 4 risks de Cagan)

8 roles. **6 son asesores** (custodios de dimensiones, participan en scope-scan multi-rol). **2 son ejecutores** (developer, devops — implementan; sin dimensión propia salvo `operations` para DevOps).

| Rol | Modelo | Dimensión custodiada | Cagan risk | Agent file | Sesión dedicada (npm) |
|-----|--------|---------------------|------------|--------|-----|
| Product Owner (extendido) | Opus | product (strategy + operativo) | value-risk (íntegro) | `.claude/agents/product-owner.md` | `npm run po` (`vault/product-owner/`) |
| Architect | Opus | technical | viability-risk (technical) | `.claude/agents/architect.md` | `npm run arch` (`vault/architect/`) |
| Designer | Sonnet | usability | usability-risk | `.claude/agents/designer.md` | `npm run des` (`vault/designer/`) |
| Business Analyst | Sonnet | business | business-viability-risk | `.claude/agents/business-analyst.md` | `npm run biz` (`vault/business-analyst/`) |
| Security Officer | Opus | security | (transversal — overlap business compliance) | `.claude/agents/security-officer.md` | `npm run sec` (`vault/security-officer/`) |
| QA | Sonnet | quality | (transversal — coverage de risks) | `.claude/agents/qa.md` | `npm run qa` (`vault/qa/`) |
| Developer | Sonnet | (ejecutor, sin dimensión) | — | `.claude/agents/developer.md` | `npm run dev` (`src/` — wrapper pendiente) |
| DevOps | Sonnet | operations | (transversal — operational viability) | `.claude/agents/devops.md` | `npm run ops` (`vault/devops/` — wrapper pendiente) |

**Nota Cagan**: el rol "Coach" de Scrum no aparece en el modelo de Cagan; en *Inspired/Empowered* el Product Manager extendido cubre desde visión hasta features (escalando a Product Leader en empresas grandes). En SEM-IA el coach es el humano (Pelayo o equivalente) y el PO agente IA es su contraparte facilitadora en la dimensión `product` completa.

## Custodio principal por tipo de nodo

| Tipo de nodo | Custodio principal | Dimensión dominante |
|---|---|---|
| Visión | Product Owner | product |
| Goals | Product Owner | product |
| Capabilities | Product Owner | product |
| Features | Product Owner | product |
| Stories | Product Owner | product |
| Specs (Gherkin) | Product Owner | product |
| ADRs | Architect (típicamente) | technical |
| Usability audits | Designer | usability |
| Business reviews / Compliance maps | Business Analyst | business |
| Threat models | Security Officer | security |
| QA reports | QA | quality |
| Working Agreements | Recepción + humano | governance |
| Reviews | Custodio que revisa | varía |
| Learnings | Quien lo aprende | varía |

## Roles del proyecto

Cualquier proyecto puede crear roles adicionales en `.claude/agents/` (con sus skills en `.claude/skills/`) siguiendo el mismo patrón de markdown con frontmatter. Casos típicos:

- **Especialización del Developer:** `backend-dev`, `frontend-dev`, `mobile-dev`, `smart-contract-dev`. Sobreescriben `developer` cuando aplica.
- **Roles para dimensiones extra declaradas:** `dba` (si el proyecto declara dimensión `data`), `product-designer` (si declara `ux`), `quant` (si declara `quant-validation`), `tokenomics-designer`, `risk-analyst`, etc.
- **Roles propios del dominio:** `defi-protocol-researcher`, `market-researcher`, etc.

Cada rol nuevo declarado en el proyecto debe alinearse con una dimensión del catálogo de `vault/shared/governance/dimensions.md`. Si introduces un rol sin dimensión, es un rol de implementación (como `developer`).
