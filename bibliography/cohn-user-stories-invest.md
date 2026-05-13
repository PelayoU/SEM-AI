---
category: bibliography-source
id: library-cohn-user-stories-invest
title: "Mike Cohn — User Stories Applied + INVEST"
status: draft
created: 2026-04-30
author: pelayo
tags: [library, user-stories, invest, product-owner]
applicable-roles: [product-owner]
---

# Mike Cohn — User Stories Applied + INVEST

## Datos bibliográficos

- **Autor:** Mike Cohn (Mountain Goat Software)
- **Obra principal:** *"User Stories Applied: For Agile Software Development"* (Addison-Wesley, 2003)
- **Acrónimo INVEST:** propuesto originalmente por **Bill Wake** (2003), popularizado por Cohn en User Stories Applied (Capítulo 2).
- **Aplicabilidad SEM-IA:** dimensión `product` — Product Owner al escribir stories y al evaluar features candidatas.

## Formato de user story (Cohn)

> *"Como [tipo de usuario], quiero [acción / capacidad] para [beneficio]."*

Tres partes que responden:
- **Quién** — el rol o persona del usuario.
- **Qué** — la capacidad o acción deseada.
- **Por qué** — el beneficio que el usuario obtiene.

Ejemplos:
- *"Como developer, quiero invocar un custodio de seguridad para que valide mi PR sin tener que pedir review humano cada vez."*
- *"Como Product Owner, quiero que la spec de una feature sea ejecutable como tests, para que los AC nunca diverjan del código."*

## INVEST — Criterios para una user story sana

Acrónimo: **I**ndependent · **N**egotiable · **V**aluable · **E**stimable · **S**mall · **T**estable

### I — Independent
- La story debería poder construirse y entregarse independientemente de otras.
- Si dos stories están fuertemente acopladas, fundir o reordenar.
- Razón: independence permite priorización flexible.

### N — Negotiable
- La story NO es un contrato cerrado. Es punto de partida para conversación.
- Los detalles emergen en discovery (Adzic, Torres) — no se escriben todos de antemano.
- Razón: negociabilidad permite ajuste durante implementación sin "scope creep" descontrolado.

### V — Valuable
- La story entrega valor a un stakeholder (usuario, negocio, equipo). 
- Si nadie la valora, no debería construirse.
- Razón: valor es la justificación de existencia.

### E — Estimable
- El equipo puede estimar el tamaño con razonable aproximación.
- Si no se puede estimar, está mal definida o falta conocimiento → discovery más profunda.
- Razón: estimabilidad permite priorización y planificación.

### S — Small
- Cabe en un sprint / iteración.
- Si es muy grande → "epic" → se descompone en múltiples stories más pequeñas.
- Razón: small = entrega frecuente = feedback rápido.

### T — Testable
- Hay AC que permiten verificar cumplimiento.
- Si no es testeable, falta especificación.
- Razón: testabilidad cierra el loop entre intent y verificación.

## Stories vs. Use Cases vs. Specs

- **Use case:** descripción detallada de interacciones, paso a paso.
- **Story (Cohn):** breve, punto de partida para conversación, formato narrativo.
- **Spec (Adzic-style en Gherkin):** la story formalizada con AC ejecutables.

En SEM-IA, las stories son nodos del grafo (frontmatter + breve narrative). Las specs son archivos Gherkin asociados.

## Aplicabilidad a SEM-IA

**Skill `product-owner.story-writing`:** formato Cohn como standard.

Plantilla:
```
Como [rol del catálogo de roles SEM-IA o usuario externo del framework]
Quiero [capacidad concreta]
Para [resultado / beneficio que conecta con la capability padre]
```

**Skill `product-owner.feature-decomposition`:** una feature se descompone en N stories. Cada story pasa los 6 tests INVEST.

Tests INVEST como sub-skill `product-owner.story-quality-check`:

1. **I:** ¿esta story depende de otras no construidas todavía? Si sí, reordenar.
2. **N:** ¿está sobreespecificada? La spec viene después.
3. **V:** ¿qué valor concreto entrega? ¿A quién?
4. **E:** ¿el architect puede estimar (high-level) tras leerla?
5. **S:** ¿cabe en un Working Agreement de implementación de una sesión / unas pocas?
6. **T:** ¿se pueden formular AC en Gherkin a partir de ella?

## Citas que anclan decisiones

> *"User stories are not requirements documents. They are placeholders for conversations."* — espíritu de Cohn

Aplicable a `discovery-facilitation`: la story es punto de partida, no contrato.

> *"INVEST in good stories, and SMART tasks."* — Bill Wake (origen del acrónimo)

INVEST a nivel story; SMART a nivel task / AC. Complementarios.

## Limitaciones del framework

- INVEST es checklist heurístico, no ley. Algunas stories válidas pueden romper "Independent" temporalmente y eso es aceptable si está documentado.
- "Small" depende del equipo. Lo que es 1 día para un equipo es 1 semana para otro.
- Cohn enfatiza conversación > documentación, pero SEM-IA documenta con frontmatter porque la auditoría estructural lo exige. Los dos no son incompatibles: la story puede ser breve Y registrarse en el grafo.
