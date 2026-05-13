---
type: research
id: borrador-skill-architect-adr-writing
title: "Borrador de skill: architect.adr-writing"
status: draft
created: 2026-04-30
author: pelayo
tags: [skill-borrador, architect, adr, happy-path]
dimensions-affected: [technical, product]
---

# Borrador de skill: architect.adr-writing

> **Estado: borrador.** Materialización en `.claude/skills/architect/adr-writing/SKILL.md`.

## Propósito

Escribir **Architecture Decision Records (ADRs)** siguiendo la plantilla canónica de Nygard adaptada al frontmatter SEM-IA. Cada ADR documenta una decisión arquitectónica significativa con su contexto, decisión y consecuencias, en lenguaje value-neutral en el contexto y voz activa en la decisión.

## Cuándo se invoca

- **Trigger principal:** decisión arquitectónica significativa surge durante `feature-viability-review`, `capability-viability-review`, o sesión de discovery con dimensión técnica.
- **Trigger secundario:** revisión de decisión existente que necesita supersession (= nueva ADR).
- **Trigger asistencial:** humano pide "documentar esta decisión técnica".

## Inputs

- Contexto de la decisión (qué fuerzas están en juego).
- Decisión propuesta (qué se va a decidir).
- Alternativas consideradas (con tradeoffs).
- ADRs existentes (para detectar supersession o relación).
- Estructura del nodo definida en `./SKILL.md` (sección "Estructura del nodo").
- Library: [[library-nygard-adr]], [[library-bass-software-architecture]].

## Proceso — 7 pasos

### Paso 1 — Verificar que la decisión amerita ADR
Heurística (Nygard):
- ✅ Decisión cross-cutting (afecta múltiples partes).
- ✅ Alternativa rechazada era razonable.
- ✅ Alguien futuro lo va a cuestionar sin contexto.
- ✅ Cambio de decisión previa (= nuevo ADR superseding).
- ❌ Decisión trivial o reversible barata.
- ❌ Detalle de implementación dentro de un módulo.
- ❌ Decisión puramente estilística.

Si NO amerita → no escribir ADR. Documentar en learning, comentario, o discovery note.

### Paso 2 — Asignar ID y título
- ID: `adr-NNN-slug`. NNN secuencial. slug descriptivo.
- Título: frase nominal corta. Ejemplo: *"ADR-005: Estrategia de export como JSON streaming"*.

### Paso 3 — Frontmatter
```yaml
---
type: adr
id: adr-NNN-slug
title: "ADR-NNN: descripción corta"
status: proposed
supersedes: null
superseded-by: null
related-features: [feature-N, ...]
related-capabilities: [cap-N-slug, ...]
dimensions-affected: [technical, ...]
created: YYYY-MM-DD
author: architect
---
```

### Paso 4 — Sección Context
Lenguaje value-neutral. Describe las fuerzas:
- Tecnológicas (qué tecnologías están en juego, qué constraints técnicos).
- De producto (qué objetivos del producto importan).
- Sociales / del equipo (quién va a operar esto, qué saben).
- Locales del proyecto (qué decisiones previas constriñen esta).

NO inclinar la decisión todavía. Solo describir el panorama.

### Paso 5 — Sección Decision
Voz activa. Frases completas. *"We will [verb] [object] using [approach]."*

Ser específico. "Usaremos JSON" es vago; "Usaremos JSON streaming con `oboe.js` para parseado incremental, no JSON completo en memoria" es decisión.

### Paso 6 — Sección Consequences
Tres categorías explícitas:
- **Positivas:** qué se vuelve más fácil, qué nuevas posibilidades se abren.
- **Negativas:** qué se vuelve más difícil, qué se renuncia.
- **Neutras:** qué cambia sin ser bueno ni malo.

Importante: las **negativas** son obligatorias. Toda decisión tiene tradeoffs. Si no se identifican negativas, el análisis es incompleto.

### Paso 7 — Sección Alternatives Considered (extensión SEM-IA sobre Nygard)
Listar alternativas evaluadas y rechazadas, con razón breve:
- Alternativa A: descripción. Rechazada porque [tradeoff].
- Alternativa B: descripción. Rechazada porque [tradeoff].

Esto NO es Nygard original — es extensión SEM-IA para auditabilidad.

## Output format

Archivo `vault/architect/adrs/adr-NNN-slug.md` con frontmatter completo y secciones Context, Decision, Consequences, Alternatives Considered.

Adicionalmente:
- Si supersede otro ADR → modificar el ADR previo a `status: superseded` con `superseded-by: adr-NNN-slug`.
- Si relacionado a features → añadir referencias bidireccionales (`related-adrs` en frontmatter de las features).

## Fundamento bibliográfico

- [[library-nygard-adr]] — plantilla canónica completa.
- [[library-bass-software-architecture]] — qué constituye decisión arquitectónica significativa.

## Ejemplo aplicado

**ADR para SEM-IA mismo:**

```markdown
---
type: adr
id: adr-001-skills-location
title: "ADR-001: Ubicación de skills en .claude/skills/<rol>/<skill>/SKILL.md"
status: accepted
supersedes: null
superseded-by: null
related-features: []
related-capabilities: [cap-1-custodios-homologos]
dimensions-affected: [technical, product]
created: 2026-04-30
author: architect
---

# ADR-001: Ubicación de skills en .claude/skills/<rol>/<skill>/SKILL.md

## Status
Accepted

## Context
Las skills de los agentes SEM-IA tienen que vivir en una ubicación que (a) Claude Code descubra nativamente, (b) permita organización por rol, (c) soporte directorio con archivos auxiliares (referencias, ejemplos), (d) sea consistente con el boceto inicial sec. 23.

Anthropic establece dos ubicaciones para skills: `.claude/skills/<skill-name>/SKILL.md` (proyecto) y `~/.claude/skills/<skill-name>/SKILL.md` (usuario). El estándar Agent Skills (agentskills.io) usa la misma estructura.

SEM-IA tiene 9+ roles y cada uno tendrá ~10 skills. Sin sub-organización, `.claude/skills/` se vuelve denso (90+ directorios).

## Decision
Las skills SEM-IA se organizan en subdirectorios por rol:
- `.claude/skills/product-owner/strategy/<skill>/SKILL.md`
- `.claude/skills/product-owner/<skill>/SKILL.md`
- `.claude/skills/architect/<skill>/SKILL.md`
- ... etc.
- `.claude/skills/shared/<skill>/SKILL.md` para skills compartidas entre roles.

Esta estructura es legible, navegable, y compatible con descubrimiento nativo de Claude Code (que busca recursivamente).

## Consequences

**Positivas:**
- Organización clara por rol. `.claude/skills/product-owner/strategy/` muestra todas las skills estratégicas del PO.
- Compatible con la convención de Anthropic.
- Soporta archivos auxiliares dentro de cada `<skill>/`.
- Permite naming corto en cada skill (no requiere prefijar `coach-`).

**Negativas:**
- Skills compartidas requieren decisión sobre dónde viven (resuelta con `shared/`).
- Más profundidad de directorios — paths más largos.

**Neutras:**
- Algunos sistemas de listing alfabético van a poner `shared` después de roles específicos. No problemático.

## Alternatives Considered
- **Skills planas en `.claude/skills/<rol>-<skill>/SKILL.md`:** rechazada. Pérdida de organización; nombres largos; menos navegable.
- **Skills por rol en `.claude/agents/<rol>/skills/`:** rechazada. Anthropic establece skills en su propia raíz, no anidadas en agentes.
- **Skills en `vault/architect/research/skills/`:** rechazada. El vault no se descubre por Claude Code; las skills no se invocarían como tales.

## ACTUALIZACIÓN 2026-05-13 — Decisión superseded por verificación empírica

La suposición *"Claude Code busca recursivamente"* (sección Decision arriba) **fue refutada empíricamente** al verificar el harness real: las 14 skills SEM-IA materializadas con nesting `.claude/skills/<rol>/<skill>/SKILL.md` y `.claude/skills/<rol>/<categoría>/<skill>/SKILL.md` **NO se descubrieron** por Claude Code. El PO en sesión dedicada listaba las descriptions de slash commands (`.claude/commands/`, planos) pero no las de las skills bibliográficas (anidadas), y al preguntarle racionalizaba post-hoc *"se cargan perezosamente"* — alucinación frente al hecho de que las descriptions de skills descubiertas SÍ están visibles desde session start (verificado contra `skills.md` oficial: *"Claude uses skill descriptions at session start"*).

**Nueva estructura adoptada**: skills planas con prefijo de rol (la alternativa que este mismo ADR había rechazado por "pérdida de organización"):
- `.claude/skills/po-<skill>/SKILL.md`
- `.claude/skills/arch-<skill>/SKILL.md`
- `.claude/skills/sec-<skill>/SKILL.md`
- `.claude/skills/shared-<skill>/SKILL.md`

Tras el flatten, las 14 skills se descubrieron inmediatamente con sus descriptions visibles al PO.

**Lección Nygard aplicada**: los ADRs registran decisiones tomadas con información de su momento. Cuando la realidad refuta una suposición, no se reescribe el ADR original — se documenta el supersede con razón empírica. Las "Negativas" enumeradas en la decisión rechazada (paths más largos, navegabilidad) eran reales pero menores frente al hecho irrefutable de que la decisión original convertía las skills en código muerto operativo.
```

## Limitaciones

- ADRs requieren disciplina para mantener actualizados. ADR aceptado pero no respetado en código es deuda arquitectónica oculta.
- "Decisión arquitectónica significativa" es subjetivo. Diferentes Architects van a documentar a niveles distintos. Heurísticas ayudan pero no eliminan juicio.
- ADRs antiguos pueden volverse irrelevantes sin que nadie los marque como `deprecated`. Considerar revisión periódica vía `coherence-evaluation`.
