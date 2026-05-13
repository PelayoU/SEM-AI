---
category: story
id: story-<NNN>-<X>-<slug>
parent: "[[feature-NNN-slug]]"
status: draft
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
also-relates-to: []
depends-on: []
dimensions-affected: []
---

# Story <NNN>-<X> — <Título>

> La letra X (A, B, C...) traza los AC en el spec hermano (`spec-NNN-slug`). Los AC se numeran AC-X1, AC-X2, AC-X3...
>
> *"User stories are placeholders for conversations."* — Cohn. La frase es punto de partida, no contrato cerrado.

## Frase Cohn

> As **<role>**, I want **<action>**, so that **<benefit>**.
>
> - **Role**: del catálogo de roles SEM-IA o usuario externo del framework.
> - **Action**: capacidad concreta.
> - **Benefit**: resultado que conecta con la feature padre y, a través de ella, con la capability.

## Examples (Adzic — alimentan AC)

> Ejemplos concretos en lenguaje real (no técnico) que iluminan el comportamiento esperado. 2-5 ejemplos por story incluyendo edge cases. Estos ejemplos alimentan los AC en el spec hermano. *"Examples are bridges that connect business and technical perspectives."*

- Ejemplo 1:
- Ejemplo 2:
- Ejemplo 3:

## INVEST self-check (Cohn / Wake)

> Veredicto por criterio (✅ / ❌ / 🟡) con razón corta. Si falla algún criterio, repensar la story.

- **Independent**: ¿se puede construir/entregar sin depender de stories no construidas?
- **Negotiable**: ¿no está sobreespecificada? El detalle emerge en discovery.
- **Valuable**: ¿qué valor concreto entrega y a quién?
- **Estimable**: ¿el equipo puede estimar tamaño con razonable aproximación?
- **Small**: ¿cabe en un Working Agreement / iteración corta?
- **Testable**: ¿se pueden formular AC en Gherkin a partir de ella?
