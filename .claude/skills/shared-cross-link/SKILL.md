---
name: shared-cross-link
description: "Identificar y declarar las aristas cross-link del grafo SEM-IA en el frontmatter de un nodo: also-relates-to, depends-on, dimensions-affected. Skill transversal: el PO la invoca al crear o editar cualquier nodo; otros roles (cuando existan) también. Use this skill always when creating a new node or when reviewing an existing node with incomplete cross-links."
when_to_use: "Se ha creado o editado un nodo del grafo y hay que declarar sus aristas cross-link (no solo el parent jerárquico) para que el grafo en Obsidian sea navegable y las queries de las .base funcionen."
---

# shared-cross-link

## Propósito

Mantener el grafo declarativo navegable: cada nodo declara sus aristas explícitamente en frontmatter para que (a) Obsidian las visualice en graph view, (b) las bases las consulten, (c) el sistema detecte impactos cuando un nodo cambia.

## Tres tipos de aristas + dimensiones

Convención de campos detallada en CLAUDE.md raíz, sección "Cross-links":

- `parent` — espina dorsal jerárquica (siempre, excepto visión).
- `also-relates-to` — conexión horizontal no jerárquica.
- `depends-on` — dependencia operativa real (no funciona sin esto).
- `dimensions-affected` — lista de dimensiones tocadas (default `[product]`).

## Cómo procedes

1. **Lee el nodo recién creado o editado.**
2. **Verifica parent jerárquico** — si no es claro, problema upstream (revisa la skill de creación del nodo).
3. **Busca relaciones horizontales:**
   - ¿Trata el mismo tema que otro existente? → `also-relates-to`.
   - ¿Necesita que otro exista / esté `active` antes de operar? → `depends-on`.
4. **Identifica dimensiones tocadas.** Default `[product]`. Añade si:
   - Decisión técnica significativa → `+ technical`.
   - Cambia UX visible → `+ usability`.
   - Datos sensibles, auth, compliance → `+ security`, `+ business`.
   - Estrategia de test particular → `+ quality`.
   - Cambios de infra → `+ operations`.
5. **Edita el frontmatter** con los cross-links identificados.
6. **Verifica reciprocidad** — si declaras `also-relates-to: [B]` en A, edita B añadiendo A a SU `also-relates-to`.

## Trampas a evitar

- **Aristas implícitas en texto sin declarar en frontmatter.** Si en el cuerpo dices `[[feature-005]]` pero no está en `also-relates-to`, las bases no lo verán. Declara siempre.
- **Cross-links inflados.** Criterio: ¿alguien que abre este nodo necesita ver el otro para entenderlo o decidir? Si no, fuera.
- **Olvidar reciprocidad.** Si A relates-to B, B también. Si no actualizas B, hay drift.
- **`dimensions-affected` solo product.** Para nodos no triviales, casi siempre hay otra dimensión tocada. Pensar honestamente.
- **`depends-on` usado como "tiene que ver".** `depends-on` significa "no funciona sin esto". Si A puede existir sin B, es `also-relates-to`, no `depends-on`.

## Después de aplicar

Registra en documento-sesión:

```markdown
- Cross-links declarados en `nodes/<id>.md`: also-relates-to [<>], depends-on [<>], dimensions-affected [<>]. Aplicando `shared-cross-link`.
```
