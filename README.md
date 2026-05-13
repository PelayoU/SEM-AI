# SEM-IA

**Ingeniería de Gestión de Software de IA.** Framework donde la IA mantiene la infraestructura documental del proyecto (grafo navegable de nodos con criterios bibliográficos auditados) y el humano es autor de las decisiones.

> *"El trabajo con IA requiere su propia infraestructura de gestión. La IA como infraestructura, el humano como autor."*

## Setup

Requiere [Claude Code](https://docs.claude.com/claude-code) instalado.

```bash
git clone <repo>
cd sem-ia
npm run sem
```

Arranca sesión con el Product Owner extendido (Cagan PM + Product Leader) como identidad principal.

## Cómo usar

Conversas con el PO. Le traes una propuesta, una duda, un trabajo a hacer. El PO:

1. Te pregunta lo que necesite para clarificar.
2. Aplica skills bibliográficas (Cagan, Patton, Cohn, Adzic, Nygard, etc.) sobre la propuesta.
3. Propone toques concretos al grafo: crear nodo, declarar cross-link, refinar nodo existente.
4. Tú confirmas, ajustas o descartas.
5. La conversación se registra en `sessions/YYYY-MM-DD-<tema>.md`.

## Visualización

Abre Obsidian sobre la raíz del repo. Las **bases** (`_obsidian/bases/*.base`) te dan vistas filtradas del grafo:

- `visions.base`, `goals.base`, `capabilities.base`, `features.base`, `stories.base`, `specs.base`, `adrs.base`
- `backlog.base` — features con status `ready-for-implementation`
- `in-flight.base` — stories en implementación
- `sessions.base` — conversaciones recientes
- `bibliography.base` — fuentes citadas por skills

Graph view de Obsidian muestra el grafo entero navegable por cross-links.

## Estructura

| Path | Contenido |
|---|---|
| `nodes/` | Todos los nodos del proyecto (plano, organizado por `category` en frontmatter) |
| `sessions/` | Documentos de conversación humano ↔ PO |
| `bibliography/` | 18+ fuentes auditadas (Cagan, Patton, Cohn, Adzic, Nygard, Bass, Ford, Martin, Ousterhout, Norman, etc.) |
| `_obsidian/bases/` | Vistas filtradas del grafo |
| `_obsidian/templates/` | Plantillas para crear nuevos nodos |
| `.claude/agents/product-owner.md` | Identidad del PO |
| `.claude/skills/po-*` | Skills bibliográficas del PO |

## Estado

Iteración 0 — modelo limpio post-reset. Solo PO con 6 skills mínimas. Otros roles (Architect, Designer, Security Officer, QA, Developer, DevOps) se añadirán incrementalmente cuando emerja la necesidad concreta.

## Licencia

Apache 2.0.
