---
type: capability
id: cap-07-inception-greenfield
title: "Inception greenfield protocol-compliant desde vault vacío"

parent: goal-1-auto-sostenibilidad

also-relates-to:
  - goal-5-portabilidad
  - goal-7-ciclo-vida-producto
depends-on:
  - cap-03-working-agreements-sdlc  # inception se materializa via cadena de WAs usando templates de CAP-03
dimensions-affected: [product, technical, usability]
related-adrs: []  # vacío hoy

status: active   # transición aplicada por /verify del WA wa-2026-05-12-002 el 2026-05-12T05:30+02:00
operational-status: operant

fundamento-bibliografico:
  - Cagan — Inspired (visión + goals + capabilities como cadena estratégica)
  - Norman — Design of Everyday Things (modelo conceptual del proceso de inception para el operador)
  - Patton — User Story Mapping (cadena ordenada top-down desde visión)
  - Christensen — JTBD (inception como job: arrancar proyecto desde nada)
  - Ousterhout — A Philosophy of Software Design (protocolo uniforme inception ↔ mantenimiento como deep module)

qas-bass:
  - learnability     # operador greenfield aprende el sistema mientras lo usa
  - predictability   # el flujo de inception es el mismo que el de mantenimiento (uniformidad)
  - modifiability    # cadena de WAs adaptable según gaps detectados
  - portability      # mismo protocolo aplicable a SEM-IA y a adopters externos greenfield

tactics:
  - "Uniform protocol (Ousterhout deep module): los mismos workflow templates de CAP-03 sirven para inception y para mantenimiento — sin protocolos paralelos"
  - "Conversational guidance: PO Modo 1 (Entrada al sistema) detecta vault vacío y conduce vía 10 pasos declarados"
  - "Cadena ordenada top-down: vision-creation → goal-definition × N → capability-creation × M → feature-design × K como propuesta por gaps detectados (no rígida, adapta a contexto)"
  - "Affordance ergonómica: `npm run sem` es punto de entrada único + bajo cognitive load; PO conduce el resto"

tradeoffs:
  - "Inception via cadena de WAs es más lenta que script — mitigación: el valor estructural (auditabilidad + cobertura multi-rol desde el primer minuto) justifica el coste"
  - "Aspect mind no apto para impacientes — adopter que busca '5-minute setup' encontrará SEM-IA verbose; público target es ingeniero que aprecia estructura"
  - "Inception conducida por PO depende de skills estratégicas del PO (vision-quality-check, goal-quality-check, capability-derivation) — si están mal aplicadas, la inception genera grafo incoherente"
  - "El gap 3 del WA-002 expone que el template `capability-creation` no contemplaba batch ni bottom-up — la propia inception de SEM-IA fue caso límite (mejorable)"

jtbd-outcome:
  quien: "Humano autor de proyecto greenfield (autor de SEM-IA hoy; adopter externo en futuro)"
  job: "Arrancar un proyecto SEM-IA desde vault vacío usando los mismos protocolos que el mantenimiento — sin protocolos paralelos, sin atajos ad-hoc, con auditabilidad desde el primer minuto"
  outcome-esperado: "El humano entra con `npm run sem` y el PO conduce inception. La experiencia: el operador sabe dónde está (Nielsen #1), entiende el modelo conceptual del proceso (Norman: cuántos WAs vendrán, cuándo puede parar) y termina con grafo del proyecto estructuralmente sano (visión + goals + capabilities iniciales)"
---

# CAP-07 · Inception greenfield protocol-compliant desde vault vacío

## Enunciado

El humano arranca un proyecto SEM-IA desde **vault vacío** vía `npm run sem`. El **PO en Modo 1 (Entrada al sistema)** detecta el estado del vault y propone **cadena de WAs ordenada top-down** (`vision-creation → goal-definition × N → capability-creation × M → feature-design × K`) usando los **mismos workflow templates** que en fase mature. **Sin protocolos paralelos** ni atajos ad-hoc. **Convergencia inception ↔ dogfooding ↔ mantenimiento** bajo los mismos templates indexados por fase SDLC. El operador experimenta el sistema mientras lo construye — aprendizaje progresivo (Norman: modelo conceptual emergente).

## Por qué es capability fuerte (4 criterios)

1. **Habilidad diferenciada**: arrancar un proyecto desde vault vacío **respetando el protocolo desde el primer turno** es habilidad propia, distinta de "coordinar trabajo en general" (CAP-03). El "cómo empezar desde nada" tiene cohesión propia (detección vault vacío + cadena ordenada + conducción PO Modo 1).
2. **Sirve a goals con métrica clara**: goal-1 declara *"inception desde vault vacío sin intervención manual al protocolo"* — métrica directa. Goal-5 (portabilidad) depende de CAP-07 para que adopters externos puedan greenfield.
3. **Cohesión interna**: PO Modo 1 + ritual de inicio + detección vault vacío + propuesta cadena de WAs + workflows uniformes — comparten el job *"arrancar proyecto desde cero"*.
4. **No es trivialmente subcapability de CAP-03**: aunque CAP-07 USA los workflow templates de CAP-03, la inception es habilidad cohesiva por sí misma (Architect lo defendió como tal). Coupling de implementación documentado en `depends-on`; no fusión conceptual.

## Piezas del bootstrap que la materializan

| Pieza | Path | Rol en la capability |
|---|---|---|
| PO Modo 1 (Entrada al sistema) — 10 pasos | `.claude/agents/product-owner.md` sección "Protocolo del Modo 1" | Conducción de inception |
| Ritual de inicio del PO | `vault/product-owner/CLAUDE.md` + agent file PO | Lectura del vault al arrancar + panorámica al humano |
| Detección de vault vacío + propuesta cadena de WAs | parte de PO Modo 1 paso 3 (clasifica outcome) | Reconoce greenfield y propone vision-creation → goal-definition → ... |
| Workflows uniformes greenfield/mature | `vault/shared/governance/workflows.md` | Mismos templates en ambas fases |
| Atajo `npm run sem` | `package.json` | Punto de entrada único |

## Relación con goals

- **Goal-1 (auto-sostenibilidad)** — parent primario. *"Inception desde vault vacío sin intervención manual al protocolo"* es métrica explícita.
- **Goal-5 (portabilidad)** — adopters externos arrancan con el mismo protocolo.
- **Goal-7 (ciclo de vida producto)** — la inception es la primera fase del lifecycle.

## Criterio observable para futuros `/verify`

Una feature descompuesta de CAP-07 es verificable si cumple:
- `npm run sem` sobre vault vacío arranca sesión PO en Modo 1.
- El PO detecta el vault vacío y propone cadena de WAs (no asume contexto previo).
- La cadena propuesta es ordenada top-down (vision → goals → capabilities → features).
- Cada WA de la cadena usa template de `workflows.md` (no protocolo paralelo).
- Al cerrar la inception, el vault tiene grafo estructuralmente sano (visión active, goals active, capabilities active iniciales).

## Features candidatas (preview)

1. **PO Modo 1 — Protocol de 10 pasos** declarado en agent file. Posiblemente formalizar como skill `inception-orchestration` (pending en `_pending-later.md`).
2. **Detección del estado del vault** — heurística para clasificar greenfield / partial / mature.
3. **Propuesta de cadena de WAs** — algoritmo basado en gaps detectados (visión faltante → propone vision-creation; goals incompletos → propone goal-definition; etc.).
4. **Ritual de inicio del PO** — protocolo declarado por convención.
5. **Conducción conversacional de inception** — UX del PO en cada WA de la cadena.

## Notas / gaps operativos conocidos

- **Gap 3 del WA-002** (template `capability-creation` no contempla batch ni bottom-up): expuesto durante la propia inception de SEM-IA. Mejorable como feature futura.
- **Para adopters externos (greenfield real)** el approach es claro pero no ha sido testado por adopter no-autor todavía. Goal-5 lo exige a medio plazo.
- **Designer flag** sobre experiencia del operador durante inception (Norman: modelo conceptual emergente): el operador debería saber cuántos WAs vendrán, cuándo puede parar, dónde está. CAP-07 declara visibility como uno de sus tactics, pero la UX detallada se materializa en features de CAP-07 + CAP-06 conjuntamente.
- **Inception conducida por PO depende de skills estratégicas del PO**: si vision-quality-check o capability-derivation se aplican mal, el grafo emerge incoherente. El own WA-001 abortado fue ejemplo de esto.
