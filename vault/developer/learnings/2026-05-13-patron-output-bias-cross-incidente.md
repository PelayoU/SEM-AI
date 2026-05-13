---
type: learning
id: learning-2026-05-13-patron-output-bias-cross-incidente
title: "Patrón meta cross-incidente del PO: bypass del test load-bearing por presión de estructura formal (output bias)"
status: active
created: 2026-05-13
author: product-owner
related-incidents:
  - learning-2026-05-12-filtro-po-contaminado  # Trampa 1
  - wa-2026-05-12-004-aborted-reason  # Trampa 2 stop-too-early
related-rules-applied:
  - regla-operativa-12  # Filtro PO con artefacto declarativo
  - regla-operativa-13  # NUEVA — output bias en pasadas largas
related-criteria-applied:
  - adzic-sbe-1-6  # Test mecánico de granularidad en discovery docs
dimensions-affected: [product, quality]
bibliography:
  - Cagan — Inspired (principio 1: solve problems, not features = output. Strong PM decides, doesn't aggregate)
  - Ousterhout — A Philosophy of Software Design (deep modules, simple interfaces — no inflar)
  - Cohn — User Stories Applied (INVEST `S = Small` aplicado a granularidad)
  - Adzic — Specification by Example (test mecánico de granularidad: si no descende a Given/When/Then, no es feature)
---

# Patrón meta cross-incidente del PO

## Contexto del análisis

Tras 2 incidentes del PO en < 48h (2026-05-12 mañana + 2026-05-12 tarde) y resoluciones estructurales aplicadas (regla 12 + criterio Adzic SbE 1.6), emerge la pregunta meta: **¿hay un patrón común que merezca intervención estructural propia, más allá de las correcciones específicas de cada incidente?**

Análisis bibliográfico cross-incidente cierra el compromiso humano pendiente "después de arreglarlo vamos a hablar tú y yo de por qué te has contaminado". Resultado: sí, hay patrón meta robusto; merece **regla operativa 13** + **sección "Trampas operativas conocidas"** consolidada en el agent file PO. Aplicado a pelo en este mismo día.

## Los 2 incidentes lado a lado

### Incidente 1 — Filtro PO contaminado (mañana 2026-05-12, WA-004 step-1 post-step scope-scan)

- **Contexto**: PO consolidando outputs de 5 advisors en post-step scope-scan multi-rol del WA-004.
- **Estructura formal**: Filtro PO con 4 categorías Cagan (acepto / descarto con razón / difiero / decisión humana). Bibliográficamente correcto.
- **Operación mecánica**: clasifiqué 13 de 14 flags como cat-1 ("aplico yo") sin pelear con criterio fuerte.
- **Síntoma detectado por humano**: "los subagentes están para darte info, no para contaminarte tú eres el que sabes de features".
- **Resolución estructural**: regla operativa 12 + extensión del Modo 1 paso 6b con 3 mecanismos obligatorios (test load-bearing fila por fila + auto-audit numérica + artefacto declarativo). Learning capturado en `2026-05-12-filtro-po-contaminado-anti-patron.md`.

### Incidente 2 — Stop-too-early espina dorsal (tarde 2026-05-12, WA-004 step-1 producción 46 features)

- **Contexto**: PO produciendo features bottom-up desde 8 capabilities operant en WA-004 reverse-engineering batch.
- **Estructura formal**: reverse-engineering batch como mode improvisado del template `feature-design` (paralelo al patrón ya formalizado en `capability-creation`). Approach correcto.
- **Operación mecánica**: produje 46 "features" donde cada pieza candidata del bootstrap se etiquetó feature, sin descender a stories + examples + AC + Gherkin formal. Mezcla sistemática de 5 niveles arquitectónicos (features Nivel 1 / ADRs latentes / protocolos operativos / docs/governance / artefactos curados) bajo el rótulo "feature".
- **Síntoma detectado por humano**: "hay que distinguir entre features y stories, spec etc.. a ver si la granularidad no es la correcta".
- **Resolución estructural**: abortar WA-004 (Protocolo Gap 4) + reformular en WA-005 con descenso completo hasta Gherkin formal + integrar test mecánico Adzic SbE como criterio 1.6 obligatorio en discovery docs heredable a futuros WAs batch.

## Patrón común diagnosticado

### Diagnóstico bibliográfico

Los dos incidentes comparten **bypass del test load-bearing por presión de estructura formal**. En ambos:

1. **La estructura formal era correcta bibliográficamente** (4 categorías Cagan / espina dorsal SEM-IA + reverse-engineering batch). No hay fallo de diseño bibliográfico.

2. **Operé la estructura mecánicamente** (clasificar todo en cat-1 / extraer feature por cada pieza). La estructura ejecutó sin que yo aplicara criterio fuerte.

3. **NO peleé con criterio bibliográfico de "esto aporta valor load-bearing?"** hasta que el humano me llamó la atención. Hubo señales internas (mi propio "debatible" en spec post-step, marca de borderline) pero las suprimí.

4. **El humano detectó el patrón vía señales output-volumen**: en ambos casos lo que disparó la crítica fue **demasiado output sin valor proporcional** (13 cat-1 confirmadas / 46 features producidas).

### La causa raíz: presión de output sobre presión de decisión

Cagan principio 1 (*Inspired*) lo nombra exactamente: *"Strong product teams solve problems for customers; weak teams ship features (= output)"*.

Ambos incidentes son operación bajo presión de output:
- Más cat-1 = más cosas "absorbidas activamente" = sensación de productividad del PO.
- Más features = más volumen visible = sensación de completitud del catálogo.

Pero en ambos casos, output sin criterio = noise + inflación + degradación de auditabilidad. La señal de "progreso" es falsa.

### La causa raíz bibliográfica más profunda: la estructura formal no protege

**La estructura formal (4 categorías Cagan / espina dorsal SEM-IA) es scaffolding NECESARIO pero INSUFICIENTE.**

Es necesario: sin las 4 categorías, no hay forma de organizar Filtro PO. Sin espina dorsal, no hay forma de descomponer producto.

Pero es insuficiente: el PO puede aplicar la estructura mecánicamente sin aplicar criterio bibliográfico fuerte. La estructura no detecta operación mecánica — solo el criterio aplicado conscientemente lo hace.

Cagan strong PM: *"opinions are informed by data but decisions are own"*. La estructura es "data" (input organizador). La decisión SIEMPRE es del PO. No puede delegarla a la estructura.

## Resolución estructural meta aplicada (2026-05-13)

### Regla operativa 13 añadida al agent file PO

```
13. NO operes en pasadas largas sin auto-audit ("output bias"). Al producir artifacts en
    serie (features/stories/specs durante step-2x de un WA batch, ediciones masivas,
    transiciones de status), aplica pause obligatoria de auto-audit cada N≥10 artifacts
    producidos: test load-bearing + muestreo bibliográfico + reclasificación si ambiguo.
```

### Sección nueva "Trampas operativas conocidas" en agent file PO

Agrupa los 3 anti-patrones detectados empíricamente como categoría coherente con disparadores numéricos + resoluciones estructurales + incidentes formativos + learnings capturados:

- **Trampa 1**: Filtro PO contaminado.
- **Trampa 2**: Stop-too-early en espina dorsal.
- **Trampa 3**: Output bias en pasadas largas (categoría general que cubre 1 y 2).

Razón de agrupar: cuando un PO arranque sesión futura, leer una sección consolidada de trampas + sus disparadores es más eficiente que descubrir 3 reglas dispersas en distintos sitios del agent file.

### Heurística meta-meta documentada

*"La estructura formal correcta NO protege contra operación mecánica. El PO siempre aplica criterio bibliográfico fuerte SOBRE la estructura, no SIGUIENDO ciegamente la estructura."*

## Aplicabilidad future

Este learning aplica preventivamente a futuros incidentes que compartan el patrón. Si emerge:

- PO recibe output multi-rol y clasifica mecánicamente → Trampa 1 detectada → aplicar regla 12.
- PO produce en serie sin descender a granularidad bibliográfica → Trampa 2 detectada → aplicar Adzic SbE 1.6.
- PO produce artifacts > N=10 sin auto-audit → Trampa 3 detectada → aplicar regla 13.

Si emerge un patrón nuevo con causa raíz "estructura formal correcta + operación mecánica + bypass criterio fuerte" → añadirlo como Trampa 4 + crear su learning + actualizar reglas operativas con disparador propio. La sección "Trampas operativas conocidas" del agent file PO es extensible.

## Anclaje del compromiso humano cerrado

El humano declaró 2026-05-12T23:59 (tras fix Filtro PO contaminado): *"después de arreglarlo vamos a hablar tú y yo de por qué te has contaminado porque no puede ser. Hay que arreglarlo ya, sin wa sin nada lo arreglamos tú y yo a pelo inmediatamente"*.

Y 2026-05-13 tras cierre WA-005 mencioné el compromiso pendiente: *"Análisis cross-incidente del error bestia — patrón meta cross-incidente del PO"*.

Este learning + regla 13 + sección "Trampas operativas conocidas" del agent file PO cierran el compromiso. Análisis aplicado a pelo bajo autorización humana explícita ("Vale, continuemos"), análogo al fix Filtro PO contaminado de ayer.

## Referencias

- `vault/developer/learnings/2026-05-12-filtro-po-contaminado-anti-patron.md` — Trampa 1 origen.
- `vault/shared/sessions/archive/wa-2026-05-12-004.md` — Trampa 2 origen (aborted-reason documentado).
- `vault/shared/sessions/archive/wa-2026-05-13-005.md` — WA successor que aplicó la resolución estructural completa de Trampa 2 (test Adzic SbE 1.6).
- `.claude/agents/product-owner.md` — agent file PO con regla 12 + regla 13 + sección "Trampas operativas conocidas" + Modo 1 paso 6b extendido.
