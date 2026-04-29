---
type: governance
id: verification-matrix
title: "Matriz de verificación"
status: active
created: 2026-04-30
author: human
---

# Matriz de verificación

Define qué tipos de cambio requieren qué verificadores al cierre de un Working Agreement o al abrir un PR. Recepción consulta esta matriz para invocar verificadores en paralelo.

```yaml
verification-matrix:
  - change-type: vision-or-capabilities-change
    verifiers: [coach, product-owner]
    description: "Cambios en la pirámide alta propagan a niveles inferiores"

  - change-type: significant-new-feature
    verifiers: [architect, qa]
    description: "Features nuevas requieren coherencia técnica y estrategia de tests"

  - change-type: architectural-decision
    verifiers: [architect, security-officer]
    description: "ADRs nuevos o modificados requieren revisión técnica y de seguridad"

  - change-type: database-migration
    verifiers: [dba, architect]
    description: "Cambios en el modelo de datos requieren revisión de integridad"

  - change-type: security-sensitive-change
    verifiers: [security-officer, architect]
    description: "Cambios que tocan autenticación, autorización, datos sensibles"

  - change-type: spec-modification
    verifiers: [product-owner, qa]
    description: "Cambios en specs requieren coherencia de producto y cobertura"

  - change-type: minor-copy-or-config-change
    verifiers: []
    description: "Cambios menores de copy o configuración no requieren verificadores"
```

## Aplicación

1. Recepción identifica el `change-type` del WA que se cierra
2. Consulta esta matriz para obtener `verifiers`
3. Invoca a cada verificador como subagent en paralelo
4. Consolida hallazgos y presenta al humano
5. Si todos aprueban: luz verde. Si alguno objeta: el humano decide.

## Extensión

Cada proyecto añade change-types según su dominio. La matriz se construye iterativamente con uso real. Si llega un cambio no cubierto, recepción pregunta al humano qué verificadores invocar y sugiere añadir la regla.
