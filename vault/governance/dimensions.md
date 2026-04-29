---
type: governance
id: dimensions-catalog
title: "Catálogo de dimensiones del producto holístico"
status: active
created: 2026-04-30
author: human
---

# Dimensiones del producto holístico

Cada dimensión tiene un custodio asignado. Los nodos del grafo declaran `dimensions-affected` para indicar qué dimensiones tocan, y el sistema usa este catálogo para derivar qué custodios invocar.

```yaml
dimensions:
  - id: strategy
    description: "Visión, goals, capabilities"
    custodian: coach

  - id: product
    description: "Alcance, fit con usuarios, prioridades"
    custodian: product-owner

  - id: technical
    description: "Arquitectura, código, infraestructura"
    custodian: architect

  - id: data
    description: "Modelo de datos, persistencia"
    custodian: dba

  - id: security
    description: "Vulnerabilidades, privacidad"
    custodian: security-officer

  - id: quality
    description: "Cobertura, testing, regresión"
    custodian: qa
```

## Extensión

Para proyectos específicos se añaden dimensiones del dominio. Cada dimensión nueva implica un custodio asignado. Ejemplos:

- `quant-validation` → quant (proyectos cuantitativos)
- `tokenomics` → tokenomics-designer (proyectos DeFi)
- `smart-contract-security` → smart-contract-auditor (proyectos DeFi)
- `ux` → product-designer (cuando hay diseñador dedicado)
