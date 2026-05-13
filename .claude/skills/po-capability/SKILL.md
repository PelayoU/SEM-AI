---
name: po-capability
description: "Derivar, refinar y validar capabilities bajo un goal aprobado. Una capability da a los stakeholders la habilidad de lograr algún goal o cumplir alguna tarea, sin implicar una implementación particular. NO es feature ni actividad ni tecnología. Decomponible en features. Use this skill when deriving capabilities from an approved goal, when proposing a new capability, or when reviewing existing ones."
when_to_use: "El humano quiere derivar capabilities bajo un goal aprobado, propone una capability nueva, o pide validar capabilities existentes."
---

# po-capability

## Propósito

Derivar o evaluar capabilities — tercer nivel del grafo SEM-IA. Habilidad del producto que materializa parcialmente un goal sin implicar implementación concreta.

## Estructura del nodo

Estructura del archivo en `_obsidian/templates/capability.md`. Léelo antes de crear o editar.

## Definición operativa (canónica SEM-IA literal)

> *"Capability: Gives stakeholders the ability to achieve some goal or fulfill some task, regardless of implementation. Don't imply a particular implementation."*

Una capability:
- **Da habilidad**: al usuario/stakeholder de hacer algo.
- **Independiente de implementación**: no nombra tecnología ni feature concreta.
- **Sirve a un goal**: cuelga jerárquicamente de un goal padre.
- **Decomponible en features**: las features son las implementaciones concretas que entregan la capability.

## Criterios formales

1. **Es habilidad, no feature ni actividad ni tecnología.**
   - ❌ *"Login con OAuth"* (feature concreta).
   - ❌ *"Hacer onboarding de usuarios"* (actividad interna).
   - ❌ *"Usar PostgreSQL"* (tecnología — va a ADR, no capability).
   - ✅ *"Que el usuario inicie sesión con identidad propia"* (habilidad agnóstica de cómo).

2. **Parent claro**: cuelga jerárquicamente de un goal concreto.

3. **Sirve a goal padre**: la capability mueve un outcome del goal. Si no aporta al goal, repensar el árbol.

4. **No solapa con otras capabilities** del mismo goal. Cada una cubre una habilidad distinta.

5. **Decomponible en features**: si no puedes imaginar 2-5 features bajo ella, está mal cortada (demasiado abstracta o demasiado concreta).

6. **Coherente con visión y otras capabilities**: las capabilities como conjunto deben funcionar juntas, no contradecirse.

## Capability dentro del Dual Track

Según GISF, las capabilities se filtran en el ciclo Discovery → Delivery:

```
Discovery → Capability List → [Go/No-Go filter] → MVP (Minimum Viable Product)
```

La capability se descubre durante Discovery; el filtrado decide cuáles entran al MVP y cuáles se descartan o aplazan.

## Cómo procedes

**Modo single** (1 capability):
1. Lees el goal padre (`nodes/goal-XX-...md`).
2. Aplicas los 6 criterios al enunciado propuesto.
3. Propones el nodo con cross-links.

**Modo batch** (derivar varias capabilities bajo un goal):
1. Lees el goal.
2. Identificas las habilidades que el producto necesita para mover el outcome del goal.
3. Propones lista (típicamente 2-5 capabilities por goal).
4. Verificas Independent + cobertura conjunta (juntas, las capabilities aseguran el goal).
5. Presentas lista al humano para confirmación una por una.

Tras confirmación, aplicas el cambio leyendo `_obsidian/templates/capability.md` como base. Aplicas `shared-cross-link` después.

## Trampas a evitar

- **Capability-feature**: confundir habilidad con entregable concreto. La capability NO nombra cómo se implementa.
- **Capability-actividad**: *"Hacer discovery con usuarios"* — actividad interna del equipo, no habilidad del producto para el usuario.
- **Capability-tecnología**: decisiones técnicas van a ADR, no a capability.
- **Bootstrap-anchor**: derivar capabilities desde features que ya tienes en mente, no desde el goal. Resultado: el grafo "encaja" pero no materializa estratégicamente. Empieza siempre desde el outcome del goal.

## Después de aplicar

Registra en documento-sesión:

```markdown
- Creadas N capabilities bajo `goal-XX-<slug>` aplicando `po-capability`. Cita: definición canónica SEM-IA + 6 criterios.
```
