---
name: shared-cross-link
description: "Identificar y declarar las aristas cross-link del grafo SEM-IA en el frontmatter de un nodo: also-relates-to, depends-on, dimensions-affected. Skill transversal: el PO la invoca al crear o editar cualquier nodo; otros roles (cuando existan) también. Use this skill always when creating a new node or when reviewing an existing node with incomplete cross-links."
when_to_use: "Se ha creado o editado un nodo del grafo y hay que declarar sus aristas cross-link (no solo el parent jerárquico) para que el grafo en Obsidian sea navegable y las queries de las .base funcionen."
---

# shared-cross-link

## Propósito

Mantener el grafo declarativo navegable: cada nodo declara sus aristas explícitamente en frontmatter para que (a) Obsidian las visualice en graph view, (b) las bases las consulten, (c) el sistema detecte impactos cuando un nodo cambia.

## Tres tipos de aristas

| Campo | Significado | Cuándo declarar |
|---|---|---|
| `parent` | Espina dorsal jerárquica | Siempre (excepto visión, que es raíz) |
| `also-relates-to` | Conexión horizontal no jerárquica | Cuando un nodo se relaciona conceptualmente con otro fuera de su línea de herencia |
| `depends-on` | Dependencia operativa | Cuando este nodo no puede materializarse / activarse sin que otro esté primero |
| `dimensions-affected` | Lista de dimensiones tocadas | Siempre — al menos `[product]`; añadir `[technical, security, usability, ...]` cuando aplique |

## Catálogo de dimensiones

| Dimensión | Significado |
|---|---|
| `product` | Decisiones de producto, alcance, fit con usuario. Default para todo nodo del grafo. |
| `technical` | Arquitectura, código, fitness functions. Activar cuando el nodo implica decisión técnica significativa. |
| `usability` | UX, accesibilidad, flujo de usuario. Activar cuando el nodo cambia cómo el usuario percibe / interactúa. |
| `business` | Pricing, compliance regulatorio, contratos, GTM. Activar para nodos con implicación comercial / legal. |
| `security` | Auth, datos sensibles, threat surface. Activar al tocar zonas de riesgo. |
| `quality` | Estrategia de tests, regresión. Activar cuando el nodo necesita cobertura especial. |
| `operations` | Infra, pipelines CI/CD, observabilidad. Activar para nodos operacionales. |

(Iteración 0 solo tiene PO custodiando `product`. Otras dimensiones se activarán cuando se añadan los roles correspondientes.)

## Cómo procedes

1. **Lee el nodo recién creado o editado.**
2. **Identifica el parent jerárquico.** ¿Es claro? Si no, problema upstream (revisa la skill de creación del nodo).
3. **Busca relaciones horizontales:**
   - ¿Este nodo trata el mismo tema que otro existente? → `also-relates-to`.
   - ¿Este nodo necesita que otro exista / esté `active` antes de operar? → `depends-on`.
4. **Identifica las dimensiones tocadas.** Default `[product]`. Añade si:
   - El nodo describe decisión técnica significativa → `+ technical`.
   - El nodo cambia UX visible → `+ usability`.
   - El nodo toca datos sensibles, auth, compliance → `+ security`, `+ business`.
   - El nodo requiere estrategia de test particular → `+ quality`.
   - El nodo implica cambios de infra → `+ operations`.
5. **Edita el frontmatter** del nodo con los cross-links identificados.
6. **(Si el nodo era nuevo) verifica reciprocidad:** si declaraste `also-relates-to: [other-id]`, edita `nodes/<other-id>.md` añadiendo este nodo a SU `also-relates-to` (las aristas son bidireccionales en el grafo declarativo).

## Output esperado

Edición del frontmatter del nodo (y del recíproco si aplica):

```yaml
---
category: <...>
id: <...>
parent: <...>
status: <...>
also-relates-to: [<id-1>, <id-2>]
depends-on: [<id-3>]
dimensions-affected: [product, technical]
---
```

## Trampas a evitar

- **Aristas implícitas en texto sin declarar en frontmatter.** Si en el cuerpo del nodo mencionas `[[feature-005]]` pero no está en `also-relates-to`, las bases no lo verán. Declara siempre.
- **Cross-links inflados.** No metas un nodo en `also-relates-to` solo porque "tiene que ver tangencialmente". El criterio: ¿alguien que abre este nodo necesita ver el otro para entenderlo o decidir sobre él? Si no, fuera.
- **Olvidar reciprocidad.** Si A relates-to B, B también relates-to A. Si no actualizas B, hay drift.
- **Dimensions-affected solo product.** Para nodos no triviales, casi siempre hay otra dimensión tocada. Pensar honestamente — no declarar es bug latente.
- **depends-on usado como "tiene que ver".** `depends-on` significa "no funciona sin esto". Si A puede existir sin B, no es depends-on; es `also-relates-to`.

## Después de aplicar la skill

Registra en documento-sesión:
```markdown
- Cross-links declarados en `nodes/<id>.md`: also-relates-to [<>], depends-on [<>], dimensions-affected [<>]. Aplicando `shared-cross-link`.
```
