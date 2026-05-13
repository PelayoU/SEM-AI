# SEM-IA

**Tesis:** la IA como infraestructura, el humano como autor. SEM-IA es la maquinaria que mantiene el grafo navegable del proyecto (nodos, cross-links, dimensiones, criterios bibliográficos) para que el desarrollo escale sin perder coherencia.

Este archivo es **guía estática del proyecto**, no identidad de agente. Se carga automáticamente cuando se abre Claude Code en la raíz.

---

## Cómo arrancar

```bash
npm run sem    # equivalente a: claude --agent product-owner
npm run po     # idéntico
```

Arranca sesión Claude Code con el Product Owner extendido como identidad principal. El PO es la entrada única al sistema: conversa con el humano, mantiene el grafo, aplica skills bibliográficas, declara cross-links.

## Estructura del repo

```
SEM-IA/
├── .claude/                    Infraestructura Claude Code
│   ├── agents/product-owner.md
│   ├── skills/                 Skills del PO (po-*, shared-*)
│   └── settings.json
├── nodes/                      Grafo del proyecto (plano, organizado por category)
├── sessions/                   Documentos-sesión (conversación humano ↔ PO)
├── bibliography/               Fuentes auditadas que las skills citan
├── _obsidian/
│   ├── bases/                  Vistas filtradas del grafo (queries)
│   └── templates/              Plantillas para crear nuevos nodos
├── CLAUDE.md                   Este archivo
├── README.md
└── package.json
```

## Convención del grafo

Todo nodo del proyecto vive plano en `nodes/` con frontmatter YAML que declara su `category`:

```yaml
---
category: vision | goal | capability | feature | story | spec | adr | session | library-source | skill | agent
id: <id-único>
parent: <id-del-padre o null>
status: <estado>
created: <ISO date>
also-relates-to: []
depends-on: []
dimensions-affected: []
---
```

Las **bases de Obsidian** (`_obsidian/bases/*.base`) filtran nodos por `category` y producen vistas (backlog, in-flight, sin-spec, etc.). El backlog no es un archivo: es una query sobre `status: ready-for-implementation`.

## Filosofía operativa

- **Humano dirige; IA mantiene.** El PO propone toques al grafo, el humano confirma. Autoría siempre del humano.
- **Sin ceremonia.** No hay Working Agreements, scope-scans automáticos, ni fases de verify. La calidad emerge de aplicar skills bibliográficas en cada toque.
- **Documento-sesión sustituye a contrato.** Cada conversación significativa se registra en `sessions/YYYY-MM-DD-<tema>.md` con: contexto, decisiones, toques al grafo. Auditable sin overhead.
- **Obsidian es la UI.** El humano abre Obsidian sobre el repo entero y navega el grafo con graph view + bases + backlinks.
