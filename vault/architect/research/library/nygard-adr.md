---
type: research
id: library-nygard-adr
title: "Michael Nygard — Architecture Decision Records (ADR)"
status: draft
created: 2026-04-30
author: pelayo
tags: [library, adr, documentation, architect]
applicable-roles: [architect]
---

# Michael Nygard — Architecture Decision Records (ADR)

## Datos bibliográficos

- **Autor:** Michael Nygard
- **Obra:** *"Documenting Architecture Decisions"* — blog post en Cognitect, 15 de noviembre de 2011.
- **URL canónica:** https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- **Estandarización posterior:** https://adr.github.io/ (template comunitario), Joel Parker Henderson — repositorio de plantillas.
- **Aplicabilidad SEM-IA:** dimensión `technical` — Architect cuando documenta decisiones arquitectónicas significativas.

## Tesis central

> *"Documenting architecture decisions is essential. We have all encountered code where the original developers left, and the rationale for important decisions has been lost. Without that context, modifications become risky."*

Cualquier decisión arquitectónica significativa debe tener su **registro escrito** con contexto, decisión, consecuencias. Esto:
- Preserva el **rationale** entre transiciones de equipo.
- Permite auditar decisiones después.
- Reduce el riesgo de modificaciones porque las razones originales son visibles.
- Soporta **conscious deviation** — si rompes una decisión, sabes qué estás rompiendo.

## La plantilla canónica de Nygard

Una ADR contiene exactamente 5 secciones:

### 1. Title
Frase nominal corta, numerada. Ejemplos:
- *"ADR 1: Deployment on Ruby on Rails 3.0.10"*
- *"ADR 9: LDAP for Multitenant Integration"*

### 2. Status
Estado de la decisión. Estados canónicos:
- **Proposed** — decisión propuesta, aún no acordada.
- **Accepted** — acordada por los stakeholders.
- **Deprecated** — la decisión ya no aplica (sin reemplazo).
- **Superseded** — reemplazada por otra ADR posterior. Debe **referenciar el ADR que la reemplaza**.

### 3. Context
> *"This section describes the forces at play, including technological, political, social, and project local. These forces are probably in tension, and should be called out as such. The language in this section is value-neutral. It is simply describing facts."*

Las fuerzas en juego antes de la decisión. Lenguaje neutro, descriptivo. Captura las tensiones sin tomar partido todavía.

### 4. Decision
> *"This section describes our response to these forces. It is stated in full sentences, with active voice."*

La decisión tomada. Frases completas, voz activa: *"We will use X..."*. No es opcional; es la respuesta a las fuerzas del Context.

### 5. Consequences
> *"This section describes the resulting context, after applying the decision."*

Lo que cambia después de aplicar la decisión. Incluye consecuencias **positivas, negativas, y neutras**. Lo que ahora es más fácil; lo que ahora es más difícil; lo que es nuevo.

## Principios

- **Una decisión = un ADR.** No agrupar varias decisiones aunque sean del mismo tema.
- **Inmutables tras aprobación.** Una ADR aprobada no se edita. Si la decisión cambia, se crea una **nueva ADR** que supersede la anterior.
- **Numeradas secuencialmente.** ADR-001, ADR-002, ... — el orden importa para reconstruir la historia del proyecto.
- **Versionadas con el código.** Viven en `vault/architect/adrs/` o equivalente, en el mismo repo. Pull request = decisión propuesta para discusión.

## Cuándo escribir un ADR

Heurísticas:
- Decisión que **afecta a múltiples partes del sistema** (cross-cutting).
- Decisión donde la **alternativa rechazada era razonable**.
- Decisión que **a alguien futuro le costará entender** sin contexto.
- Cambio en una decisión previa (= nueva ADR superseding la anterior).

NO escribir ADR para:
- Decisiones triviales o reversibles a bajo coste.
- Detalles de implementación dentro de un módulo concreto.
- Decisiones puramente estilísticas (formato de código, etc.) — esas viven en convenciones, no en ADRs.

## Aplicabilidad a SEM-IA

**Skill `architect.adr-writing`:** plantilla canónica de Nygard adaptada al frontmatter SEM-IA.

Plantilla SEM-IA (definida inline en `.claude/skills/architect/adr-writing/SKILL.md`, sección "Estructura del nodo"):

```yaml
---
type: adr
id: adr-NNN-slug
title: "ADR-NNN: descripción corta"
status: proposed   # proposed / accepted / superseded / deprecated
supersedes: null
superseded-by: null
related-features: [feature-N, ...]
dimensions-affected: [technical, ...]
created: YYYY-MM-DD
author: architect
---

# ADR-NNN: título

## Status
Proposed | Accepted | Superseded by ADR-MMM | Deprecated

## Context
...

## Decision
We will...

## Consequences
- Positivas: ...
- Negativas: ...
- Neutras: ...

## Alternatives considered
...
```

Adaptación SEM-IA (extensión sobre Nygard):
- **`Alternatives considered`** sección extra. Nygard no la incluye explícitamente; SEM-IA sí, para dejar registro de las opciones rechazadas con sus tradeoffs.
- **`related-features`** y **`dimensions-affected`** en frontmatter como cross-links del grafo.

## Citas que anclan decisiones

> *"A decision may be 'proposed' if the project stakeholders haven't agreed with it yet, or 'accepted' once it is agreed. If a later ADR changes or reverses a decision, it may be marked as 'deprecated' or 'superseded' with a reference to its replacement."*

Aplicable directamente al field `status` y a la convención `superseded-by` en el frontmatter de SEM-IA.

> *"The language in this section is value-neutral. It is simply describing facts."*

Aplicable a la sección Context: NO inclinar la decisión todavía, solo describir el panorama de fuerzas.

## Limitaciones

- Nygard no detalla qué nivel de detalle poner en Context. Demasiado poco → el lector futuro no entiende; demasiado → ADR pesado.
- "Una decisión = un ADR" puede producir muchos ADRs en proyectos grandes. SEM-IA mitiga con `related-features` para navegar el grafo.
- Nygard no contempla revisión periódica de ADRs aceptados. SEM-IA puede añadir un proceso opcional (skill `coherence-evaluation` revisa ADRs cuando un cambio nuevo los cuestiona).
