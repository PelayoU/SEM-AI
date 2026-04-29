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

## Catálogo core (SEM clásica)

```yaml
dimensions:
  - id: strategy
    description: "Visión, goals, capabilities"
    custodian: coach

  - id: product
    description: "Alcance, fit con usuarios, prioridades"
    custodian: product-owner

  - id: technical
    description: "Arquitectura, código, infraestructura técnica, modelo de datos"
    custodian: architect

  - id: security
    description: "Vulnerabilidades, privacidad, control de acceso"
    custodian: security-officer

  - id: quality
    description: "Cobertura, testing, regresión"
    custodian: qa

  - id: operations
    description: "Despliegue, CI/CD, observabilidad, fiabilidad"
    custodian: devops
```

## Extensión

Cada proyecto añade dimensiones según sus necesidades. Cada dimensión nueva implica un custodio asignado, definido en el catálogo de roles del proyecto. Ejemplos posibles:

- `data` → DBA (cuando el proyecto justifica un rol dedicado al modelo de datos)
- `ux` → product-designer (cuando hay diseñador dedicado)
- `quant-validation` → quant (proyectos cuantitativos)
- `tokenomics` → tokenomics-designer (proyectos DeFi)
- `smart-contract-security` → smart-contract-auditor (proyectos DeFi)

Si el proyecto no declara una dimensión específica, el custodio del core la absorbe (por ejemplo, si no hay DBA, los temas de modelo de datos los lleva el architect dentro de `technical`).
