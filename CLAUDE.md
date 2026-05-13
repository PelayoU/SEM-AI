# SEM-IA

Infraestructura para mantener un proyecto de software a escala — desde la visión hasta el código, con trazabilidad completa. El humano toma roles (Product Owner, ...) y cada rol puede invocar a otros como subagentes para revisión cruzada. El proyecto entero vive como **grafo navegable de nodos markdown** en `nodes/`.

Este archivo es contrato técnico compartido por todos los roles. Visión completa del proyecto: `nodes/vision.md`. Identidad de cada rol: `.claude/agents/<rol>.md`.

---

## Roles

| Rol           | Custodia                                                          | Agent file                        |
| ------------- | ----------------------------------------------------------------- | --------------------------------- |
| Product Owner | `product` — visión, goals, capabilities, features, stories, specs | `.claude/agents/product-owner.md` |


## Estructura del repo

```
SEM-IA/
├── .claude/                    Infraestructura Claude Code
│   ├── agents/<rol>.md         Identidad de cada rol (system prompt)
│   ├── skills/<skill>/SKILL.md Skills bibliográficas (planas, con prefijo de rol)
│   └── settings.json
├── nodes/                      Grafo del proyecto (todo plano, organizado por category)
├── sessions/                   Documentos-sesión (conversación humano ↔ rol)
├── bibliography/               Fuentes auditadas que las skills citan
├── _obsidian/
│   ├── bases/                  Vistas filtradas del grafo (queries)
│   └── templates/              Plantillas para crear nuevos nodos
└── CLAUDE.md                   Este archivo
```

**Vault de Obsidian = repo entero.** Obsidian se abre en la raíz y todo el contenido `.md` con frontmatter aparece en bases, graph view y backlinks.

---

## El grafo

vision → goals → capabilities → features → stories → specs
                                         ↘ adrs


Jerarquía dorsal. Los cross-links horizontales (no jerárquicos) se declaran en el frontmatter de 
cada nodo — ver sección Cross-links abajo.

---

## Templates de nodo

Cada tipo de nodo tiene su template en `_obsidian/templates/<tipo>.md` con frontmatter completo + apartados con descripción inline:

- `_obsidian/templates/vision.md`
- `_obsidian/templates/goal.md`
- `_obsidian/templates/capability.md`
- `_obsidian/templates/feature.md`
- `_obsidian/templates/story.md`
- `_obsidian/templates/spec.md`
- `_obsidian/templates/adr.md`
- `_obsidian/templates/session.md`

**El template es source of truth de la estructura del nodo.** El humano lo aplica vía Templater (Obsidian); los agentes IA lo leen vía Read tool y copian la estructura, sustituyen placeholders, escriben en `nodes/<tipo>-<id>-<slug>.md` (o `sessions/<fecha>-<tema>.md` para sesiones).

Convención de naming general (detalle por tipo en cada template):

```
nodes/<tipo>-<id>-<slug>.md          <tipo> ∈ {vision, goal, cap, feature, story, spec, adr}
sessions/YYYY-MM-DD-<tema-slug>.md
```

Stories incluyen letra (A, B, C...) en `<id>` para trazabilidad con AC en el spec hermano: `story-007-A-password-step.md` → AC-A1, AC-A2...

---

## Estados canónicos

| Estado | Significado | Aplicable a |
|---|---|---|
| `draft` | En construcción durante una sesión | Todos los nodos |
| `active` | Completado y vigente | vision, goal, capability |
| `ready-for-implementation` | En backlog, listo para que un Developer lo agarre | feature |
| `in-implementation` | Developer/equipo trabajando en ello | feature, story |
| `implemented` | Todas las stories done, spec cumplida, tests pasan | feature, story |
| `deprecated` | Decisión consciente de retirar (ya no aplica) | Todos los nodos |
| `superseded` | ADR reemplazado por otro ADR (mantener `superseded-by`) | adr |

**Backlog = query, no archivo.** Es el filtro de `_obsidian/bases/backlog.base` sobre `category: feature AND status: ready-for-implementation`. Cambiar el `status:` cambia el backlog automáticamente.

---

## Cross-links

| Campo | Significado | Cuándo |
|---|---|---|
| `parent` | Espina dorsal jerárquica | Siempre (excepto visión) |
| `also-relates-to` | Conexión horizontal no jerárquica | Cuando este nodo se relaciona con otro fuera de su línea de herencia |
| `depends-on` | Dependencia operativa real | Cuando este nodo no puede materializarse sin que otro esté primero |
| `dimensions-affected` | Lista de dimensiones tocadas | Siempre — default `[product]` |

**Reciprocidad:** las aristas son bidireccionales en el grafo declarativo. Si A declara `also-relates-to: [B]`, B también debe declarar `also-relates-to: [A]`.

### Dimensiones (catálogo)

`product` (PO) · `technical` (Architect) · `usability` (Designer) · `business` (Business Analyst) · `security` (Security Officer) · `quality` (QA) · `operations` (DevOps).

En la iteración actual solo existe el rol PO (custodio de `product`). Otras dimensiones se activan cuando se añade su rol correspondiente.

---

## Wikilinks `[[id]]`

Para referencias internas en el contenido de un nodo, usar wikilinks de Obsidian:

```markdown
Esta feature deriva de [[cap-03-multirol-agentes]] y produce el spec [[spec-007-login-multifactor]].
```

Esto activa backlinks en Obsidian (ves desde un nodo qué otros nodos lo mencionan) y graph view conectado.

Los wikilinks del cuerpo del nodo **no sustituyen** la declaración explícita en frontmatter (`parent`, `also-relates-to`, etc.). Frontmatter = aristas formales del grafo. Wikilinks del cuerpo = referencias narrativas.

---

## Bibliografía

`bibliography/` contiene fichas auditadas de fuentes que las skills citan:

- Cagan (*Inspired*, *Empowered*) — visión, value risk.
- Sinek (*Start with Why*) — Golden Circle.
- Rumelt (*Good Strategy / Bad Strategy*) — diagnosis + guiding policy + coherent action.
- Doerr (*Measure What Matters*) — OKRs.
- Doran (1981) — SMART.
- Torres (*Continuous Discovery Habits*) — Opportunity Solution Tree.
- Christensen — Jobs to be Done.
- Patton (*User Story Mapping*) — narrative flow + thin slices.
- Cohn (*User Stories Applied*) — INVEST.
- Adzic (*Specification by Example*) — Gherkin AC trazables.
- Nygard — ADR template.
- Bass — Software Architecture in Practice (Quality Attributes).
- Ford — Evolutionary Architecture (fitness functions).
- Ousterhout — Philosophy of Software Design (deep modules).
- Martin — Clean Architecture (Dependency Rule).
- Anthropic — Skills + Subagents (técnico de Claude Code).

Índice navegable: `bibliography/INDEX.md`.

Las skills citan paths concretos. Cualquier rol puede abrir una ficha cuando necesite precisar criterio.

---

## Sesiones

Cada conversación significativa con un rol se registra en `sessions/YYYY-MM-DD-<tema-slug>.md`. Estructura completa en `_obsidian/templates/session.md`. Sin steps numerados, sin verify ceremonioso, sin archivado obligatorio. Auditable sin overhead.

---

## Filosofía operativa

- **Humano dirige; IA mantiene.** El rol activo propone toques al grafo; el humano confirma. Autoría siempre del humano.
- **Anclaje bibliográfico, no improvisación.** Cuando un rol aplica criterio, cita la fuente. *"INVEST falla en el criterio Independent porque..."*, no *"esto no es buena story"* sin anclaje.
- **Cross-links siempre declarados.** El grafo solo funciona si las aristas son explícitas en frontmatter.
- **Obsidian es la UI viva.** El humano abre Obsidian sobre la raíz del repo y navega el grafo con graph view + bases + backlinks. Las bases filtran nodos por `category` y producen vistas (backlog, in-flight, sin-spec...).

---

## Preferencias personales del humano

Si quieres preferencias locales (sandbox URLs, atajos personales, instrucciones que no aplican al equipo), créalas en `CLAUDE.local.md` (gitignored). Se carga después de este archivo, con prioridad local.
