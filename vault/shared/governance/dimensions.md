---
type: governance
id: dimensions-catalog
title: "Catálogo de dimensiones del producto holístico"
status: active
created: 2026-04-30
author: human
materializes-feature: [feature-018-slash-scope-scan, feature-019-slash-verify]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): catálogo de 7 dimensiones + custodios consumido por feature-018 (/scope-scan dimensions-detected) y feature-019 (algoritmo verifiers = {custodian(d)}).
---

# Dimensiones del producto holístico

Cada dimensión tiene un custodio asignado. Los nodos del grafo declaran `dimensions-affected` para indicar qué dimensiones tocan, y el sistema usa este catálogo para derivar qué custodios invocar.

## Catálogo core (SEM-IA — alineado con los 4 risks de Cagan)

```yaml
dimensions:
  - id: product
    description: "Continuum completo: visión, goals, capabilities (lado estratégico) + features, stories, specs, AC (lado operativo). Alcance, fit con usuarios, prioridades."
    custodian: product-owner
    cagan-risk-related: value-risk (íntegro — alineación estratégica + fit con usuarios)

  - id: technical
    description: "Arquitectura, código, infraestructura técnica, modelo de datos"
    custodian: architect
    cagan-risk-related: viability-risk (technical)

  - id: usability
    description: "UI/UX, flujos de usuario, accessibility (WCAG/ADA), cognitive load"
    custodian: designer
    cagan-risk-related: usability-risk

  - id: business
    description: "Pricing, billing, contratos, ToS, compliance regulatorio (GDPR/PCI/HIPAA/SOC2), GTM impact, licensing"
    custodian: business-analyst
    cagan-risk-related: business-viability-risk

  - id: security
    description: "Vulnerabilidades, privacidad, control de acceso"
    custodian: security-officer
    cagan-risk-related: (transversal — overlap con business compliance)

  - id: quality
    description: "Cobertura, testing, regresión"
    custodian: qa
    cagan-risk-related: (transversal — coverage de los risks anteriores)

  - id: operations
    description: "Despliegue, CI/CD, observabilidad, fiabilidad"
    custodian: devops
    cagan-risk-related: (transversal — operational viability)
```

**Mapeo a los 4 risks de Cagan** (*Inspired*):

| Cagan risk | Dimensión SEM-IA | Custodio |
|---|---|---|
| Value risk | product (íntegro — strategy + product) | product-owner |
| Usability risk | usability | designer |
| Viability technical | technical | architect |
| Business viability | business | business-analyst |

Los 4 risks tienen custodio explícito en el catálogo core. **El Product Owner extendido** custodia value-risk completo (sigue el modelo Cagan de PM continuum, sin rol Coach separado). `security`, `quality`, `operations` son transversales — abordan facetas no capturadas en los 4 risks pero esenciales (security risk, regression risk, operational risk).

## Extensión

Cada proyecto añade dimensiones según sus necesidades. Cada dimensión nueva implica un custodio asignado, definido en el catálogo de roles del proyecto. Ejemplos posibles:

- `data` → DBA (cuando el proyecto justifica un rol dedicado al modelo de datos)
- `quant-validation` → quant (proyectos cuantitativos)
- `tokenomics` → tokenomics-designer (proyectos DeFi)
- `smart-contract-security` → smart-contract-auditor (proyectos DeFi)
- `marketing` → marketing-lead (proyectos consumer con go-to-market complejo, separa GTM de business pure)

Si el proyecto no declara una dimensión específica, el custodio del core la absorbe (por ejemplo, si no hay DBA, los temas de modelo de datos los lleva el architect dentro de `technical`).
