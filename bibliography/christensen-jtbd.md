---
category: bibliography-source
id: library-christensen-jtbd
title: "Clayton Christensen / Tony Ulwick — Jobs to Be Done (JTBD)"
status: draft
created: 2026-04-30
author: pelayo
tags: [library, jtbd, customer-needs, coach, product-owner]
applicable-roles: [coach, product-owner]
---

# Clayton Christensen / Tony Ulwick — Jobs to Be Done (JTBD)

## Datos bibliográficos

- **Pioneros:** Tony Ulwick (Strategyn, años 90 — Outcome-Driven Innovation), Clayton Christensen (Harvard Business School — popularizó JTBD).
- **Obras clave:**
  - Christensen — *"The Innovator's Solution"* (HBS Press, 2003)
  - Christensen — *"Competing Against Luck"* (HarperBusiness, 2016)
  - Ulwick — *"Jobs to Be Done: Theory to Practice"* (Idea Bite Press, 2016)
  - HBR — *"Know Your Customers' Jobs to Be Done"* (Sept 2016)
- **Aplicabilidad SEM-IA:** dimensión `strategy` y `product` — Coach al articular el problema que SEM-IA resuelve; Product Owner al definir features customer-centric.

## Tesis central

> *"Jobs to Be Done is a theory that helps innovators understand how and why people make decisions, revealing the circumstances—or forces—that drive people and organizations toward and away from decisions."*

Lo que el cliente compra no es un producto: es **progreso** hacia un job que está intentando hacer en una circunstancia particular. El producto es el "trabajador" que el cliente "contrata" temporalmente.

> *"People 'hire' products or services when 'jobs' arise in their lives."*

## Tres dimensiones de un Job

Cada job tiene tres dimensiones:

1. **Funcional:** la tarea pragmática que se está haciendo.
2. **Emocional:** cómo el cliente quiere sentirse haciendo el job.
3. **Social:** cómo el cliente quiere ser percibido por otros.

Ejemplo clásico (Christensen — milkshakes drive-through):
- Funcional: desayuno que se pueda comer al volante.
- Emocional: aliviar aburrimiento del trayecto.
- Social: no quedar como un "drive-by hambriento" — algo socialmente legítimo.

## Diferencia con marketing convencional

> *"While conventional marketing focuses on market demographics or product attributes, Jobs to Be Done Theory goes beyond superficial categories to expose the functional, social, and emotional dimensions that explain why people make the choices they do."*

JTBD reemplaza:
- "Mujeres 25-35 millennials urbanas" (demográfico) → con "personas que tienen este job en estas circunstancias" (job-based).
- "Nuestro producto tiene la feature X" (atributo) → con "nuestro producto hace este job mejor que las alternativas" (job-fit).

## Forma canónica de un Job Statement

> *"When [situation], I want to [motivation], so I can [expected outcome]."*

Ejemplo SEM-IA:
> *"When trabajo con IA en un proyecto serio, quiero que las dimensiones del producto (técnica, seguridad, calidad, etc.) estén verificadas estructuralmente, so I can entregar software con autoría humana sin pagar el coste multiplicado de revisar todo en paralelo."*

## Aplicabilidad a SEM-IA

**Skill `coach.vision-quality-check`:** JTBD ofrece un ángulo customer-centric para evaluar la visión.

Tests derivados:
1. ¿La visión articula un job que el cliente está intentando hacer?
2. ¿Las tres dimensiones (funcional, emocional, social) están presentes implícita o explícitamente?
3. ¿Es claro qué "competidores" (alternativas) intentan hacer ese mismo job? (Vibe coding, Cursor rules, Devin, no-AI workflows...)

**Skill `product-owner.feature-decomposition`:** cada feature debería poder articularse como "ayuda a hacer este job en estas circunstancias", no solo "agregar capacidad X al producto".

**Skill `product-owner.value-effort-estimation`:** el "valor" se mide por job-fit (cuánto mejor hace el job que las alternativas), no por número de features.

## Citas que anclan decisiones

> *"Customers don't want a quarter-inch drill. They want a quarter-inch hole."* — Theodore Levitt (precursor de JTBD)

Aplicable a `vision-quality-check`: ¿la visión describe el "drill" o el "hole"? Si describe el drill (producto), refactor hacia el hole (job).

> *"People hire products to make progress in specific circumstances."* — Christensen

Aplicable a `feature-decomposition`: cada feature responde a "qué progreso hace posible para qué cliente en qué circunstancia".

## Limitaciones del framework

- JTBD es originalmente para productos B2C / B2B con clientes externos. SEM-IA tiene "clientes" que son developers / equipos / empresas, lo cual exige adaptación.
- La articulación del job puede ser laboriosa. Para skills de día-a-día del PO, puede ser overhead — útil más en visión/estrategia que en cada feature menor.
- Combinarse con Torres OST (oportunidades como gaps en cubrir el job) y con Cohn user stories (formato narrativo más operativo).
