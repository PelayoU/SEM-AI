---
description: "Snapshot del estado actual del proyecto SEM-IA"
---

Lee el estado del proyecto y preséntalo al humano de forma compacta. NO improvises información — todo viene de leer archivos del vault.

## Pasos

1. **Working directory y rol cargado.**
   - Identifica desde qué directorio se ejecuta el comando (raíz o `vault/<subdir>/`).
   - Indica qué rol está cargado según el subdirectorio donde se arrancó la sesión: **PO** (modalidad recepción incluida) si `npm run sem`/`npm run po` (`vault/product-owner/`); **Architect** si `npm run arch` (`vault/architect/`); **Designer** si `npm run des`; **Business Analyst** si `npm run biz`; **Security Officer** si `npm run sec`; **QA** si `npm run qa`; etc. No existe sesión separada de "recepción" al root — el `CLAUDE.md` raíz es guía estática del proyecto.

2. **Working Agreements activos — agrupados por Dual Track (Cagan/Patton).**
   - Lista archivos en `vault/shared/sessions/active/`.
   - Por cada WA: lee frontmatter y muestra `id`, `outcome-type`, **`phase`**, `objective` (corto), step actual (`active-role` del primer step pending o in-progress), número de steps done / total, `created`. Si tiene `consumes`, indica el nodo consumido.
   - **Agrupa los WAs por track** según la fase del template:
     - **Discovery track** (build the right product): WAs con `phase: discovery` o `phase: design` → vision-creation, goal-definition, capability-creation, feature-design, adr, threat-model.
     - **Delivery track** (build the product right): WAs con `phase: implementation` → feature-build, bugfix, refactor.
     - **Operations track**: WAs con `phase: operations` → pipeline-change, infra-decision, observability-instrument.
     - **Meta**: WAs con `phase: meta` → doc-edit, trivial.
   - **Salud del Dual Track**: si solo hay WAs en Delivery y backlog vacío → riesgo de quedarse sin work futuro (avisar al humano que conviene alimentar Discovery). Si solo hay WAs en Discovery y nada en Delivery → riesgo de parálisis por análisis (avisar que conviene mover items del backlog a build).
   - Si no hay WAs activos: indícalo explícitamente.

3. **Backlog (query emergente).**
   - Lista nodos del vault con `status: ready-for-implementation` (output de WAs de fase `design` ya cerrados, esperando ser consumidos por WAs de fase `implementation`).
   - Búsqueda focalizada en `vault/product-owner/specs/`, `vault/architect/adrs/`, `vault/security-officer/audits/`.
   - Por cada nodo: id, tipo, fecha en que entró al backlog (cuando se setteo el status).
   - Si está vacío: indícalo. Es señal útil — no hay diseño pendiente de implementar.

4. **Estado del subgrafo estratégico.**
   - Comprueba `vault/product-owner/strategy/vision.md`: ¿existe? ¿status del frontmatter?
   - Cuenta archivos `goal-*.md` en `vault/product-owner/strategy/` y muestra cuántos hay con sus IDs.
   - Cuenta archivos `cap-*.md` en `vault/product-owner/strategy/` y muestra cuántos hay con sus IDs.
   - ¿Existe `vault/product-owner/strategy/roadmap.md`?

5. **Specs por status.**
   - Lista archivos en `vault/product-owner/specs/feature-*.md`.
   - Por cada feature: lee frontmatter y agrupa por `status` (draft, ready-for-implementation, in-implementation, implemented, deprecated).

6. **ADRs activos.**
   - Lista archivos en `vault/architect/adrs/adr-*.md`.
   - Cuenta por status (proposed, accepted, superseded, deprecated).

## Output format

```
## SEM-IA · Status

**Working directory:** <path>
**Rol cargado:** <rol o "recepción">

### Working Agreements activos — Dual Track (Cagan/Patton)

**🔍 Discovery track** (build the right product) · <N> WAs activos
- <id> · <outcome-type> · phase: <discovery|design> · steps <N done>/<N total> · current: <active-role> — <objective>
  ... o "Sin WAs activos en Discovery."

**⚙️ Delivery track** (build the product right) · <N> WAs activos
- <id> · <outcome-type> · phase: implementation · steps <N done>/<N total> · current: <active-role> — <objective>
  ... o "Sin WAs activos en Delivery."

**🚀 Operations track** · <N> WAs activos
- <id> · <outcome-type> · phase: operations · ...

**Adoption / Meta**: <N> WAs activos (si los hay)

**Salud Dual Track**: <"OK" | "Riesgo: solo Discovery, nada en Delivery — considera mover items del backlog a build" | "Riesgo: solo Delivery, backlog vacío — alimenta Discovery">

### Subgrafo estratégico
- Visión: <presente/ausente> (<status>)
- Goals: <N> — <lista de IDs>
- Capabilities: <N> — <lista de IDs>
- Roadmap: <presente/ausente>

### Features
- ready: <N>
- in-progress: <N>
- blocked: <N>
- draft: <N>

### ADRs
- accepted: <N>
- proposed: <N>
- superseded: <N>
```

Si algún directorio está vacío, dilo explícitamente con "vacío" o "sin contenido". No inventes nodos que no existen.

## Cuándo es útil

- Mid-sesión cuando quieres re-evaluar estado sin escribir párrafos.
- Al volver a un proyecto después de tiempo y querer entender dónde está.
- Antes de proponer un nuevo WA, para no duplicar trabajo activo.
