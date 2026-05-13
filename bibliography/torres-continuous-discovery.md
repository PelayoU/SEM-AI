---
category: bibliography-source
id: library-torres-continuous-discovery
title: "Teresa Torres — Continuous Discovery Habits (Opportunity Solution Tree)"
status: draft
created: 2026-04-30
author: pelayo
tags: [library, discovery, opportunity-solution-tree, coach, product-owner]
applicable-roles: [coach, product-owner]
---

# Teresa Torres — Continuous Discovery Habits (Opportunity Solution Tree)

## Datos bibliográficos

- **Autora:** Teresa Torres
- **Obra:** *"Continuous Discovery Habits: Discover Products that Create Customer Value and Business Value"* (Product Talk, 2021)
- **Recursos:** producttalk.org
- **Aplicabilidad SEM-IA:** dimensión `strategy` y `product` — Coach al derivar capabilities desde goals; Product Owner al facilitar discovery de features.

## Concepto

Discovery NO es una fase única antes de implementación; es un **hábito continuo**. El equipo está constantemente:
1. Conversando con clientes / usuarios.
2. Detectando oportunidades (necesidades, problemas, deseos).
3. Generando soluciones potenciales.
4. Probando supuestos antes de construir nada significativo.

## Opportunity Solution Tree (OST)

Estructura visual con 4 niveles:

```
                    [OUTCOME]                  ← lo que quieres mover (KR)
                       │
        ┌──────────────┼──────────────┐
        │              │              │
   [Opportunity]  [Opportunity]  [Opportunity]   ← unmet needs / pains
        │              │              │
   ┌────┴────┐    ┌────┴────┐    ┌────┴────┐
   │         │    │         │    │         │
 [Sol]     [Sol] [Sol]    [Sol] [Sol]    [Sol]   ← potential solutions
   │
 [Test]                                            ← assumption tests
```

### 1. Outcome (Resultado de negocio)
- Lo que quieres MOVER. Métrica de negocio.
- Se mapea al **Key Result** en lenguaje OKR.
- Ej.: "Reducir tiempo de revisión por PR".

### 2. Opportunities (Oportunidades)
- **Insights aprendidos hablando con usuarios** sobre necesidades no satisfechas, pains, deseos.
- NO son soluciones. Son problemas / deseos del usuario.
- Ej.: "El developer no tiene contexto para validar la dimensión X mientras codea".

### 3. Solutions (Soluciones)
- **Posibles maneras de abordar la oportunidad.**
- Múltiples por oportunidad (3+ recomendado).
- Ej.: "Subagent custodio de la dimensión X", "checklist en CLAUDE.md", "linter automático".

### 4. Assumption Tests
- **Cada solución es una pila de supuestos.** Identifícalos y testéalos antes de construir.
- *"Every idea is a stack of assumptions, and building the full solution before you test those assumptions wastes time if any core belief is false."*
- Test la **más arriesgada** primero.

## Tipos de assumption tests

Torres propone categorías:
- **Desirability:** ¿el usuario lo querrá?
- **Viability:** ¿es viable para el negocio?
- **Feasibility:** ¿es técnicamente viable?
- **Usability:** ¿se podrá usar?
- **Ethical:** ¿es ético?

## Hábitos centrales

1. **Conversaciones semanales con usuarios.** No "investigaciones grandes". Cadencia continua.
2. **Mapear oportunidades visualmente.** El OST en una pizarra física o digital.
3. **Generar múltiples soluciones por oportunidad.** Evitar enamorarse de la primera idea.
4. **Identificar y testear supuestos.** Antes de construir.
5. **Decidir basado en evidencia.** Iterar el OST con lo aprendido.

## Aplicabilidad a SEM-IA

**Skill `coach.capability-derivation`:** el OST estructura la derivación desde goals (outcomes) hasta capabilities (soluciones a oportunidades).

- Goal de SEM-IA = Outcome.
- Oportunidades = aspectos del producto holístico que necesitan custodio (= dimensiones).
- Capabilities = posibles maneras de cubrir la dimensión.
- Assumption tests = se ejecutan al implementar (validan que la capability efectivamente cubre la oportunidad).

**Skill `product-owner.discovery-facilitation`:** las prácticas de Torres aplican directamente cuando el PO facilita conversaciones de discovery alrededor de una feature candidata. Generar examples (Adzic) es complementario a generar oportunidades (Torres).

**Skill `product-owner.example-elicitation`:** los hábitos de Torres (conversaciones frecuentes, múltiples ideas, identificación de supuestos) estructuran cómo el PO obtiene examples del equipo durante discovery.

## Citas que anclan decisiones

> *"Every idea is a stack of assumptions, and building the full solution before you test those assumptions wastes time if any core belief is false."*

Aplicable a `feature-quality-check`: antes de implementar una feature, identificar los supuestos más riesgosos y diseñar tests baratos.

> *"Generate multiple solutions per opportunity."*

Aplicable a `capability-derivation`: para cada goal, considerar múltiples capabilities posibles antes de comprometerse a una. Evitar el primer instinto.

## Limitaciones del framework

- Torres está orientada a productos B2C / B2B-SaaS con usuarios accesibles. SEM-IA es framework para developers — la "conversación con usuarios" es más asíncrona (issues, PRs, retrospectivas).
- El OST puede crecer mucho. Mantener disciplinadamente top-3 oportunidades y top-3 soluciones por oportunidad para evitar parálisis.
