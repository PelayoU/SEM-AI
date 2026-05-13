---
type: governance
id: verification-matrix
title: "Guía orientativa de dimensiones por tipo de operación"
status: active
created: 2026-04-30
updated: 2026-05-04
author: human
materializes-feature: [feature-018-slash-scope-scan, feature-019-slash-verify]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): guía mnemotécnica consultada durante scope-scan (feature-018) y sign-off (feature-019).
---

# Guía orientativa de dimensiones por tipo de operación

> **Este archivo NO es algoritmo de verificación.** Es una **guía orientativa** para recepción al hacer scope-scan al crear un Working Agreement: ayuda a recordar qué dimensiones suelen aplicar a cada tipo de operación recurrente. La verificación al cierre del WA usa el algoritmo único: `verifiers = { custodian(d) : d ∈ dimensions-affected }` (ver `/verify`).

## Cómo se usa

Al crear un WA, recepción identifica el **tipo de operación** propuesto. Esta guía sugiere qué dimensiones típicamente aplican. Recepción puede:
1. **Aceptar la sugerencia** y añadirla al `dimensions-affected` del WA.
2. **Refinar** según contexto específico (añadir dimensiones que no aparezcan en la guía, omitir las que claramente no apliquen).
3. **Confirmar con scope-scan flat parallel** (recepción invoca a los 6 roles asesores en paralelo: product-owner, architect, designer, business-analyst, security-officer, qa; cada uno reporta dimensiones tocadas desde su ángulo; recepción consolida la unión).

La **fuente de verdad** de las dimensiones del WA es siempre el output del scope-scan, no esta guía. La guía es ayuda mnemotécnica.

## Catálogo de patrones recurrentes

```yaml
operation-type-patterns:
  - operation: vision-or-capabilities-change
    typical-dimensions: [product]
    rationale: "Cambios en niveles altos del subgrafo estratégico (visión/goals/capabilities) requieren coherencia con visión y propagación a features futuras. Custodio: PO (extendido)."

  - operation: significant-new-feature
    typical-dimensions: [product, technical, quality]
    rationale: "Features nuevas requieren outcome de usuario claro (product), viabilidad técnica (technical) y estrategia de tests (quality)"

  - operation: feature-with-ui
    typical-dimensions: [product, usability, technical, quality]
    rationale: "Features que tocan UI suman usability (cognitive load, accessibility, interaction patterns) — Cagan usability risk"

  - operation: feature-with-pricing-or-compliance
    typical-dimensions: [product, business, security, quality]
    rationale: "Features que tocan pricing/contratos/datos sensibles requieren business viability review (Cagan) + security overlap"

  - operation: architectural-decision
    typical-dimensions: [technical, security]
    rationale: "ADRs típicamente tocan arquitectura técnica y deben revisarse por implicaciones de seguridad"

  - operation: security-sensitive-change
    typical-dimensions: [security, technical, business]
    rationale: "Cambios que tocan auth, datos sensibles, cripto. Business añadido si compliance regulatorio aplica (GDPR/PCI/HIPAA)"

  - operation: spec-modification
    typical-dimensions: [product, quality]
    rationale: "Cambios en specs requieren coherencia de producto y revisión de cobertura de tests"

  - operation: deployment-or-infrastructure-change
    typical-dimensions: [operations, technical]
    rationale: "Pipelines, infra, despliegue tocan operativa y arquitectura"

  - operation: pricing-or-billing-change
    typical-dimensions: [business, product, technical]
    rationale: "Cambios de pricing o billing requieren business review (impacto financiero, legal), product (segmentación), technical (sistema de billing)"

  - operation: accessibility-audit
    typical-dimensions: [usability, quality]
    rationale: "Audits de accessibility requieren designer + QA para coverage de WCAG"

  - operation: minor-copy-or-config-change
    typical-dimensions: []
    rationale: "Cambios triviales que no requieren verificadores"
```

## Extensión

Cada proyecto añade patrones según su dominio. La guía se construye iterativamente con uso real. Si llega un cambio cuyo tipo de operación no está cubierto:

1. Recepción ejecuta scope-scan multi-rol para descubrir las dimensiones.
2. Tras varios casos similares, surge un patrón → se añade aquí como ayuda futura.

Ejemplos típicos de extensión:
- `database-migration` → `[data, technical]` (cuando el proyecto tiene DBA / dimensión `data`)
- `quant-model-change` → `[quant-validation, quality]` (proyectos cuantitativos)
- `incentive-mechanism-change` → `[tokenomics, quant-validation]` (DeFi)

## Diferencia con `dimensions.md`

- **`dimensions.md`** es la **fuente de verdad** del mapeo dimensión → custodio. Algoritmo.
- **`verification-matrix.md`** (este archivo) es **guía orientativa** del mapeo tipo-de-operación → dimensiones típicas. Mnemotécnica.

Si hay drift entre esta guía y la realidad de los WAs reales, la guía es la que se actualiza — no el comportamiento.
