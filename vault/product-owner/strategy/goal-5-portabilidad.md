---
type: goal
id: goal-5-portabilidad
title: "Portabilidad entre harnesses y proyectos"
parent: vision
also-relates-to: [goal-1-auto-sostenibilidad, goal-2-output-auditable-multirol]
depends-on: []
dimensions-affected: [product]
status: active
created: 2026-05-10
author: pelayo
nature: aspiracional
---

# Goal-5: Portabilidad entre harnesses y proyectos

## Resultado esperado

SEM-IA es portable entre **harnesses** (Claude Code en dogfooding hoy; OpenCode, Pi y otros como adapters multi-harness) y entre **tipos de proyecto** (greenfield, existing, consumer/B2C, B2B/enterprise). El framework sirve a cualquier proyecto que produzca software con IA, no solo a SEM-IA mismo.

## Métricas

- **Cumplimiento (controlable):** Adapter Claude Code funcional y publicado como `@sem-ia/cli` (target inicial).
- **Cumplimiento (controlable):** `src/universal/` con vault skeleton + governance defaults + schemas reutilizables independientes de harness.
- **Señal (aspiracional):** Nº de adapters multi-harness funcionales (≥ 2 a medio plazo).
- **Señal (aspiracional):** Nº de proyectos piloto adopters fuera de SEM-IA mismo (≥ 1 a corto plazo, ≥ 3 a medio plazo).

## Conexión con la visión

La visión habla de *"el trabajo con IA"* en general, no de SEM-IA específicamente. Sin portabilidad, SEM-IA queda como experimento privado. Con portabilidad, se convierte realmente en *"infraestructura organizacional"* aplicable a cualquier ingeniero que trabaje con IA.

## Naturaleza del goal

**Aspiracional** — la portabilidad técnica es controlable (yo construyo los adapters), pero la **adopción real depende de proyectos externos**. Marcado explícitamente como aspiracional para auditoría.

## Fundamento bibliográfico

- **Moore — *Crossing the Chasm*.** El chasm entre dogfooding y adopters externos.
- **Cagan — *Inspired*.** Visión durable requiere portabilidad para no quedar en nicho.
