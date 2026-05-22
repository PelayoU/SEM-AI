# Pivot a GitHub — plan para mañana

> **Status**: aprobado · 2026-05-22
> **Target**: ejecución mañana (sesión de ~3 días focused)
> **Decision**: retirar el backend SQLite + UI bespoke; convertir el framework en una capa de disciplina que vive **encima de GitHub** (existing tools), no al lado.

---

## TL;DR

Lo construido en los últimos 17 commits es una **reference implementation** que validó la disciplina del framework (parent-type rules · lifecycle state-machine · role × node-type jurisdiction · template sections · forbidden patterns · security cross-section · THRESHOLDS · FP auto-estimate · 11 node types · 81/81 tests verde). La disciplina funciona.

**Pero el framework no debería tener opinión sobre dónde vive el árbol.** El valor real es la metodología codificada (41 skills anchored a Cagan/Jones/Fagan/Humble/Patton/Gherkin) + los 6 role agents + las reglas mecánicas. Eso vive en `.claude/` y es portable.

GitHub ya tiene:
- Issues + sub-issues (nativos desde 2024) = el árbol
- Projects (Table / Board / Roadmap) = backlog · kanban · timeline
- Releases (tag + notes) = release nodes
- Discussions + `docs/adr/` = ADRs (Nygard convention)
- Pull Request Review = inspection node (Fagan-shaped nativo)
- Actions = CI + measurements + validators
- Labels + filters + search = clasificación + búsqueda
- Branch protection + PR-required = la "discovery → validation" mecánica que la vision promete

Construir todo eso nosotros fue ~3000 líneas TypeScript + ~3000 líneas React. **No las necesitábamos.** Lo que necesitamos es un runtime Python pequeño (~600 líneas) que enforce la disciplina en `PreToolUse` hooks de los MCPs existentes de GitHub.

---

## ¿Por qué pivotar ahora?

### Las observaciones que cristalizaron la decisión

1. **El graph view custom era un error operacional.** Visualmente saturado, navegación no obvia. Se sustituye por la **vista tree** (parent → children + related), que es lo que el framework realmente usa.

2. **El "graph" no es la abstracción del framework.** El framework opera sobre **árbol tipado** (parent_id backbone) + **cross-axis links** (related). El SQLite fue una implementación incidental.

3. **Existing MCPs ya cubren GitHub / Jira / Linear / Obsidian.** No tenemos que construir nada nuevo de transporte. La discusión es sólo: qué backend, y qué capa thin de validación.

4. **PR-forced workflow ES la materialización literal de la vision.** La vision dice: *"Human review on the AI's output collapses from discovery — searching for what drifted — to validation — confirming what was already recorded as compliant."* En SQLite eso era aspiracional (warn-level → drift posible). En GitHub con branch protection es **mecánico** (Action bloquea merge si validation falla).

5. **Branching de la intent es valioso y SQLite no podía.** Con git, dos arquitectos pueden explorar reorganizaciones alternativas del árbol de capabilities en branches paralelos. SQLite tenía UNA sola realidad del grafo.

6. **PR Review YA ES el inspection node-type del framework.** Fagan-shaped (3-6 reviewers, moderator, recorder, defects-found-by-severity). El framework no necesita inventarlo — sólo añadir la disciplina (verificar 3-6 reviewers, calcular DRE per pass de los comments).

7. **Una sola herramienta vs varias.** El usuario lo articuló bien: *"tener 1000 herramientas es justo lo que no queremos"*. GitHub solo cubre todo el lifecycle.

8. **Cero learning curve.** Cualquier developer ya sabe GitHub. El framework se siente como una convención + agentes, no una herramienta nueva.

### La vision lo pedía explícitamente

> *"the engineer inhabits the system"* — inhabita donde ya vive (GitHub), no donde le toca aprender a vivir.
>
> *"infrastructure that absorbs review cost, runs for one engineer or for a team"* — GitHub permissions cubren team-mode gratis (el Goal E que teníamos roadmap).
>
> *"the methodology each agent applies is encoded in audited bodies (Cagan, Jones, Fagan, Humble & Farley)"* — esto vive en `.claude/skills/`, intacto. No depende del storage.

---

## La arquitectura nueva

```
Claude Code agent (PM | Architect | Developer | QA | DevOps | Security)
  ↓
.claude/skills/ + .claude/agents/   (preloaded discipline)
  ↓
.claude/hooks/pretooluse-github.py  (intercepta mcp__github__* writes, valida, surface _warnings)
  ↓
sem_ai_runtime/  (Python ~600 líneas: validators + FP estimator + THRESHOLDS)
  ↓
mcp__github__* (existing official GitHub MCP — sin modificar)
  ↓
GitHub.com
  • Issues + Sub-issues
  • Projects (Table / Board / Roadmap views)
  • Releases (tag + notes)
  • Discussions + docs/adr/
  • Actions (CI + validators + measurements + TREE.md generator)
  • Branch protection (PR required to main; validators must pass)
```

**El árbol del framework es:**
- **Strategic spine (vision · goal · capability · adr)**: archivos markdown en el repo. Git-tracked. Branchable. PR-reviewable. Diffable.
- **Operational layer (feature · story · spec · defect)**: GitHub Issues. Kanban. Sub-issues. PR-linked.
- **Time axis (release)**: GitHub Releases nativos (git tag + release notes).
- **Quality axis (measurement · inspection)**: measurement = JSON artifact de Action o file en `sem-ai/measurements/`; inspection = PR Review.

---

## Mapping completo: 11 tipos → primitivas GitHub

| Tipo | Storage | Branchable | UX nativa |
|---|---|---|---|
| `vision` | `sem-ai/vision/001-slug.md` (singleton) | ✓ | Markdown render |
| `goal` | `sem-ai/goals/NNN-slug.md` con frontmatter `parent: vision-001` | ✓ | Markdown render + Milestone GitHub asociado |
| `capability` | `sem-ai/capabilities/NNN-slug.md` con frontmatter `parent: goal-NNN` | ✓ | Markdown render + section `## Features` auto-generada (lista issues label `cap:NNN-slug`) |
| `feature` | GitHub Issue con label `type:feature` + `cap:NNN-slug` | ✗ (Issues no branchables) | Sub-issue de capability-tracker / Project board |
| `story` | Sub-issue del feature con label `type:story` | ✗ | Tracked tasks panel |
| `spec` | Sub-issue del feature con label `type:spec` + body Gherkin | ✗ | Tracked tasks panel |
| `adr` | `docs/adr/NNN-slug.md` (Nygard convention) | ✓ | Markdown render + 7-topic section grep |
| `release` | GitHub Release (git tag + release notes) | n/a (tag = git object) | Releases page nativa |
| `measurement` | `sem-ai/measurements/NNN-period-type.json` o GitHub Action artifact | ✓ (files) | JSON parse en Actions / Quality dashboard workflow |
| `inspection` | **PR Review** (nativo) — comments + reviewers + resolution count | n/a (PR-bound) | GitHub PR UI nativo |
| `defect` | GitHub Issue con label `type:defect` + linked PR | ✗ | Issue UI + auto-close via "Fixes #NNN" en PR |

**Navegación tree** (sin UI bespoke):
- Cada archivo markdown tiene frontmatter `parent:` → click sube
- Cada archivo capability tiene sección `## Features` auto-generada → click baja a Issues
- Cada Issue tiene "Tracked by" (sube) + "Tracked tasks" (baja) nativos
- `TREE.md` regenerado por Action en cada push muestra el árbol entero, linkado
- GitHub Projects con hierarchy field da la vista tree alternativa

---

## Lo que se RETIRA

| Componente | LoC aprox | Acción |
|---|---|---|
| `mcp/src/schema.sql` + migrations + db.ts | ~200 | Retire — storage es GitHub |
| `mcp/src/tools/read.ts` + `write.ts` | ~700 | Retire — usamos `mcp__github__*` |
| `mcp/src/index.ts` (registro 18 tools) | ~150 | Retire |
| `mcp/src/viewer.ts` + HTTP server | ~100 | Retire |
| `mcp/scripts/seed-*.mjs` (scripts seed) | ~3000 | Retire — bootstrap será migration script |
| `mcp/dist/` | (build) | Retire |
| `ui/` completo (9 lentes + Quality + design system) | ~3000 | Retire — UX = GitHub.com |
| `.sem/graph.db` | (data) | **MIGRATE primero, retire después** |

**Movimiento**: a una rama `reference-local-backend` que queda taggeada como "v0.1 — kept for offline-only / regulated deployments". `main` queda limpio.

## Lo que se PORTA

| De | A | Notas |
|---|---|---|
| `mcp/src/validation.ts` (PARENT_TYPE_RULES, validateParent, validateSections, validateForbiddenMetrics, validateSecurityCrossSection) | `sem_ai_runtime/validators.py` | Mismo regex, mismo lógica, mismas warnings — Python en lugar de TS |
| `mcp/src/jurisdiction.ts` (ROLE_PERMISSIONS, OWNING_SKILL, canRoleWrite) | `sem_ai_runtime/jurisdiction.py` | Matrix idéntica |
| `mcp/src/lifecycle.ts` (TRANSITIONS, legalNext, canTransition) | `sem_ai_runtime/lifecycle.py` | State machine idéntico |
| `mcp/src/templates.ts` (TEMPLATE_SECTIONS, REQUIRED_FIELDS, FORBIDDEN_PATTERNS, SUMMARY_SECTION_PER_TYPE, THRESHOLDS, JONES_*, CAGAN_*, etc.) | `sem_ai_runtime/templates.py` | Constants + maps — Python dicts |
| `mcp/src/tools/read.ts::estimateFp` | `sem_ai_runtime/fp.py::estimate_fp(repo_path, gh_client)` | Recorre `sem-ai/**/*.md` + queries GitHub Issues vía gh CLI/API |
| `mcp/scripts/verify.mjs` (81 checks) | `sem_ai_runtime/test/test_*.py` (pytest) | Mismos casos test, contra fixtures markdown + mock GitHub data |

## Lo que se AÑADE nuevo

| Componente | Tamaño | Propósito |
|---|---|---|
| `.claude/hooks/pretooluse-github.py` | ~150 líneas | Intercepta `mcp__github__issue_write` / `create_or_update_file` / `sub_issue_write` / `add_label` / `create_pull_request` / `update_pull_request`. Llama validators. Inyecta `_warnings` como `additionalContext`. Si hard-reject, bloquea con `permissionDecision: deny`. |
| `.github/workflows/sem-ai-validate.yml` | ~80 líneas YAML | CI check en cada PR: corre validators contra los diffs de `sem-ai/**.md` + nuevos issues. Falla el job → merge bloqueado. |
| `.github/workflows/sem-ai-sync.yml` | ~100 líneas | On issue_opened/closed/labeled + push to `sem-ai/**`: regenera las secciones `## Features` auto-generadas en archivos capability. Commit + push idempotente. |
| `.github/workflows/sem-ai-tree.yml` | ~150 líneas | On push to main: regenera `TREE.md` (árbol entero, linkado). Commit. |
| `.github/workflows/sem-ai-quality.yml` | ~120 líneas | Schedule daily: lee measurements JSONs + Issues label `type:defect` + PR Reviews; computa DRE per release, defect-by-origin, FP per staff-month; escribe `QUALITY.md` o publica a Pages. |
| `.github/ISSUE_TEMPLATE/feature.yml` | ~30 líneas | Issue template tipado feature: parent capability (required), AC body section, INVEST check, etc. |
| `.github/ISSUE_TEMPLATE/spec.yml` | ~30 líneas | Issue template spec: AC numbered, Gherkin scenarios, Security AC section |
| `.github/ISSUE_TEMPLATE/defect.yml` | ~25 líneas | Issue template defect: Origin (Jones 5-category), Severity, Found-by, parent spec/story |
| `.github/ISSUE_TEMPLATE/story.yml` | ~25 líneas | Story template — INVEST, story-format |
| `sem-ai.yaml` (root) | ~60 líneas | Config: label conventions, branch protection requirements, Project board IDs, ADR directory, framework version |
| `docs/adr/0000-template.md` | ~40 líneas | Nygard template para nuevos ADRs |
| `migrate-graph-to-github.mjs` | ~300 líneas | One-shot: lee `.sem/graph.db` → emite via `gh` CLI/API: Milestones (goals), Issues con labels (capabilities/features/specs), sub-issue links, ADR files, Release. Idempotente. |
| `sem-ai-cli/` (opcional, CLI thin) | ~250 líneas Python | `sem-ai tree`, `sem-ai validate`, `sem-ai fp`, `sem-ai init` (instala labels + templates + project board) |
| `README.md` (rewrite) | ~150 líneas | Describe el framework + cómo se usa: `gh repo create + sem-ai init + claude --agent <role>` |

## Lo que se MANTIENE intacto

| Componente | Por qué |
|---|---|
| `.claude/skills/` (41 SKILL.md, 2 universales + 39 method) | La IP del framework. Sin cambios. |
| `.claude/agents/` (6 agent.md) | Sin cambios estructurales. Sólo se actualizan las tool-lists en `## Node graph` para usar `mcp__github__*` en lugar de `mcp__sem-graph__*`. |
| `.claude/hooks/session-start.py` | Sin cambios. Sigue inyectando el at-minimum project map; ahora lee de GitHub vía API en lugar de SQLite. (~30 líneas modificadas internamente.) |
| `.claude/hooks/pretooluse-task.py` | Sin cambios estructurales. Lee del mismo origen que session-start. |
| `.claude/hooks/pretooluse-edit.py` | Sin cambios — sigue siendo code-edit complexity-ceiling reminder. |
| `.claude/hooks/user-prompt-submit.py` | Sin cambios. |
| `.claude/settings.json` (Anthropic security-guidance plugin) | Sin cambios. |

---

## Plan de ejecución — ~24h focused, 3 días

### Día 1 (~8h) — Foundation: runtime Python + hooks

| # | Tarea | Tiempo | Output |
|---|---|---|---|
| 1.1 | Portar `templates.ts::THRESHOLDS` + `JONES_*` + `CAGAN_*` + `TEMPLATE_SECTIONS` + `REQUIRED_FIELDS` + `FORBIDDEN_PATTERNS` + `SUMMARY_SECTION_PER_TYPE` + `OWNING_SKILL` a Python | ~2h | `sem_ai_runtime/templates.py` |
| 1.2 | Portar `validation.ts` (validateParent · validateSections · validateRequiredFields · validateForbiddenMetrics · validateSecurityCrossSection) a Python | ~2h | `sem_ai_runtime/validators.py` |
| 1.3 | Portar `lifecycle.ts` (TRANSITIONS · legalNext · canTransition) a Python | ~30min | `sem_ai_runtime/lifecycle.py` |
| 1.4 | Portar `jurisdiction.ts` (ROLE_PERMISSIONS · canRoleWrite · OWNING_SKILL) a Python | ~1h | `sem_ai_runtime/jurisdiction.py` |
| 1.5 | Portar `estimateFp` — adaptar para que recorra archivos markdown + GitHub Issues vía `gh` CLI | ~1.5h | `sem_ai_runtime/fp.py` |
| 1.6 | Portar `verify.mjs` (81 checks) a `pytest` con fixtures markdown + mock GitHub responses | ~1h | `sem_ai_runtime/test/` |

**Gate Día 1**: `pytest` corre 81+ checks verde. Mismas validations que verificó la versión TS.

### Día 2 (~8h) — Integration: hooks + GitHub actions + templates

| # | Tarea | Tiempo | Output |
|---|---|---|---|
| 2.1 | Escribir `pretooluse-github.py` hook — intercepta `mcp__github__issue_write` + `sub_issue_write` + `create_or_update_file` + `add_label` + `create_pull_request` | ~2h | `.claude/hooks/pretooluse-github.py` + entry en `.claude/settings.json` |
| 2.2 | Escribir `.github/workflows/sem-ai-validate.yml` — corre validators en cada PR contra los diffs de `sem-ai/**.md` y los nuevos issues | ~2h | Action workflow + Python entry point `sem-ai-runtime validate-pr` |
| 2.3 | Escribir `.github/workflows/sem-ai-sync.yml` — regenera secciones `## Features` en capability files | ~1.5h | Action workflow + script |
| 2.4 | Escribir `.github/workflows/sem-ai-tree.yml` — regenera `TREE.md` en cada push | ~1h | Action workflow + tree-generator script |
| 2.5 | Crear los 5 `.github/ISSUE_TEMPLATE/*.yml` (feature · story · spec · defect · adr-proposal) | ~1h | Templates |
| 2.6 | Crear `sem-ai.yaml` con la config canónica (labels, branch protection, project board structure) + `docs/adr/0000-template.md` | ~30min | Config file + ADR template |

**Gate Día 2**: en un repo dummy nuevo, `gh repo create + sem-ai init` instala labels + templates + actions. Un PR de prueba se valida via Action. Discipline en hooks funciona.

### Día 3 (~8h) — Migration + cleanup + docs

| # | Tarea | Tiempo | Output |
|---|---|---|---|
| 3.1 | Escribir `migrate-graph-to-github.mjs` — lee `.sem/graph.db`, emite vía `gh` CLI: 6 Milestones (goals), 27 Issues (capabilities), 56 sub-issues (features), 13 sub-sub-issues (specs), 9 archivos `docs/adr/`, 1 Release v0.1.0 | ~3h | Migration script |
| 3.2 | Correr migration sobre el repo target. Verificar manual que los 114 nodos se transfirieron correctamente + labels + frontmatter + parent-id en sub-issues | ~1.5h | GitHub repo poblado |
| 3.3 | Actualizar las 6 `agent.md` — tool lists: `mcp__sem-graph__*` → `mcp__github__*`. Workflow examples reflejan `create_issue` en lugar de `create_node` | ~1.5h | 6 agent.md actualizados |
| 3.4 | Actualizar `framework/SKILL.md` y `node-templates/SKILL.md` — describen storage como GitHub (files-for-spine + issues-for-work). Mantienen toda la disciplina | ~1h | 2 SKILL.md actualizados |
| 3.5 | Crear branch `reference-local-backend`, mover `mcp/` + `ui/` + `.sem/graph.db` allí. `main` queda con sólo `.claude/`, `sem_ai_runtime/`, `.github/`, `docs/`, `sem-ai.yaml`, README | ~30min | Branch + main limpio |
| 3.6 | Reescribir `README.md` — describe SEM-AI como discipline-layer sobre GitHub. Quick start: `gh repo create + sem-ai init + claude --agent product-manager`. ADR-010 documenta el pivot | ~30min | README + ADR-010 |

**Gate Día 3** (los 4 agent-dispatch tests del framework, ahora en el flow GitHub):

1. `claude --agent qa` → *"record DRE 87% for v0.1 release"* — debe crear archivo `sem-ai/measurements/001-v0.1-DRE-90day.json` (NOT improvise) en una branch + open PR
2. `claude --agent developer` → *"static analysis found boundary-check defect in src/foo.ts"* — debe abrir un Issue label `type:defect` + `origin:coding` + `found-by:static-analysis`, no escribir prosa
3. `claude --agent architect` → *"add ADR for Stripe Connect decision"* — debe crear archivo en `docs/adr/NNN-stripe-connect.md` con 7 topics, en una branch + PR
4. **Negative**: `claude --agent product-manager` → *"create a measurement node"* — debe rechazar con jurisdiction violation surfaced via `_warnings` del hook

Si los 4 pasan → pivot completo y operacional.

---

## Riesgos aceptados (con sus mitigaciones)

| Riesgo | Mitigación |
|---|---|
| **Lock-in a GitHub** | Las primitivas (Issue + Milestone + Release + Project + Discussion) son standard PM tools. Portable a GitLab/Linear via adapter pattern si en 3 años cambia el panorama. |
| **Disciplina sólo se aplica con Claude Code en el loop** | Aceptable — la vision dice *"working with AI is the default mode of software development"*; el framework asume agente. Branch protection + `sem-ai-validate.yml` CI check cubre los casos sin agente (un humano editando issues a mano sigue chocando contra el Action si rompe parent-type rules). |
| **Casos regulados / offline / classified** | El branch `reference-local-backend` queda como backend SQLite+UI para esos casos. Modo `--backend=local`. No se tira; se etiqueta. |
| **Pérdida temporal de productividad durante la migración** | 3 días. Se hace en sesión focused, no incremental. |
| **Branchability de specs/features** | Aceptado: los issues no son branchables. La estrategia (vision/goal/capability/adr) sí lo es, que es donde la branchability importa para exploration de intent. Los specs/features son operacionales, fast iteration via PRs sobre el código que los implementa. |
| **El usuario tiene que aprender GitHub Issues** | No es learning curve nueva — GitHub es ubicuo. Más bien: dejamos de tener UI propia que el usuario tenía que aprender. |

---

## Por qué esta decisión es la correcta — anclaje en la vision

Cita literal del vision body:

> *"SEM-AI is the materialization of that infrastructure. It is a Software Engineering Management discipline for working with AI ... the methodology each agent applies is not improvised: it is encoded in audited bodies (Cagan for product, Jones for measurement and discipline, Fagan for inspection, Humble & Farley for deployment)."*

**El framework = la disciplina codificada (skills + agents + rules).** Eso queda intacto.

> *"The engineer does not invoke the system — the engineer inhabits it. Intent, decisions, scope, quality posture, security posture, and the code that satisfies them all live in one connected substrate that the human is the author of and the agents maintain."*

**El substrate cambia: SQLite custom → GitHub.** Las dos cumplen "one connected substrate". GitHub lo cumple mejor porque el ingeniero ya lo habita.

> *"Human review on the AI's output collapses from discovery — searching for what drifted — to validation — confirming what was already recorded as compliant."*

**PR-forced workflow + Actions + branch protection = esa frase hecha mecánica.** Era aspirational en SQLite (sin gate); ahora es enforced (Action falla → merge bloqueado).

> *"the same infrastructure works for a team (each human paired with their role-agent) and for one engineer (the same human, multi-role, alternating). The human composition flexes around an unchanged infrastructure."*

**GitHub permissions + teams + repo roles = team-mode cubierto gratis.** El Goal E que teníamos como roadmap (multi-user collab layer) ya no hay que construirlo — viene incluido.

> *"the multi-human collaboration layer at server scale (shared DB, RBAC, cross-user sync) is acknowledged as an additional layer reached within this horizon, not its premise."*

Exactamente — y ese layer **ES GitHub**. Sin construir nada.

---

## Lo que NO cambia (importante para no perder el sueño)

- **Los 41 skills.** La IP. Misma estructura, misma anclación a fuentes settled. Cero cambios.
- **Los 6 agent.md.** Sólo se actualiza la sección `## Node graph` (read/write tool names). Identidad de rol, jurisdicción, anchor sources — todo intacto.
- **Las 11 categorías de node-type.** vision/goal/capability/feature/story/spec/adr/release/measurement/inspection/defect. Mismas semánticas, mismas reglas de parent-type, misma jurisdiction. Sólo cambia DÓNDE viven (markdown files vs Issues vs Release tags).
- **Los thresholds y la anclación a Jones.** FP-based architecture tiers, DRE bands, Fagan participants 3-6, churn rate band, CR re-estimation trigger — todo se mantiene como reglas en `sem_ai_runtime/`.
- **El FP auto-estimate.** Misma fórmula `Σ(specs)×4 + Σ(unspecced features)×8 + Σ(data-ADRs)×10`. Sólo cambia la fuente de datos (markdown files + Issues en lugar de SQL queries).
- **Los 4 hooks Claude Code existentes.** SessionStart project-map injection, PreToolUse Task, PreToolUse Edit, UserPromptSubmit — todos se mantienen; sólo cambian internamente la fuente de la que leen.

---

## Checklist mañana — orden literal de tareas

```
Día 1
[ ] 1.1 Portar templates.ts → sem_ai_runtime/templates.py
[ ] 1.2 Portar validation.ts → sem_ai_runtime/validators.py
[ ] 1.3 Portar lifecycle.ts → sem_ai_runtime/lifecycle.py
[ ] 1.4 Portar jurisdiction.ts → sem_ai_runtime/jurisdiction.py
[ ] 1.5 Portar estimateFp → sem_ai_runtime/fp.py
[ ] 1.6 Portar verify.mjs → sem_ai_runtime/test/*.py (pytest)
[ ] GATE: pytest verde

Día 2
[ ] 2.1 .claude/hooks/pretooluse-github.py + settings.json wire
[ ] 2.2 .github/workflows/sem-ai-validate.yml
[ ] 2.3 .github/workflows/sem-ai-sync.yml
[ ] 2.4 .github/workflows/sem-ai-tree.yml
[ ] 2.5 .github/ISSUE_TEMPLATE/{feature,story,spec,defect,adr-proposal}.yml
[ ] 2.6 sem-ai.yaml + docs/adr/0000-template.md
[ ] GATE: dummy repo + gh repo create + sem-ai init funciona

Día 3
[ ] 3.1 migrate-graph-to-github.mjs
[ ] 3.2 Migration corrida + verificación manual de los 114 nodos
[ ] 3.3 Actualizar 6 agent.md
[ ] 3.4 Actualizar framework/SKILL.md + node-templates/SKILL.md
[ ] 3.5 Crear branch reference-local-backend; main limpio
[ ] 3.6 README rewrite + ADR-010
[ ] GATE: 4 agent-dispatch tests verdes
```

---

## Decisión: si algo falla en la migración

**Rollback de la migración** = `git checkout reference-local-backend`. El SQLite + UI sigue funcional. La migración es destructiva sobre `main` PERO el backend SQLite vive en la otra rama intacto. Cero risk-of-data-loss.

**Aceptar warnings durante la migración**: el `_warnings` channel del hook es no-bloqueante por design. Si la migración trae nodos con bodies que disparan warns, está bien — se limpian en sesión post-migración.

**Si los 4 agent-dispatch tests no pasan**: NO se considera el pivot completo. Se itera en el hook + skill markdown hasta que los agentes usen las primitivas correctas (Issue / sub-issue / file / Release / PR Review) sin prompt explícito.

---

## Anclaje meta — qué dice esto sobre la trayectoria del framework

Lo construido en `mcp/` + `ui/` **no es waste**. Fue:

1. La prueba de que la disciplina (parent-type · lifecycle · jurisdiction · sections · forbidden patterns · security cross-section · thresholds · FP estimate) **funciona** — 81/81 tests verde, 17 commits coherentes, validation en cada write.
2. La validación de que las 11 categorías de node-type son las correctas (no faltan, no sobran).
3. La validación de que el FP-estimate por structure es viable (no necesita IFPUG counter humano).
4. La validación de que los 4 Claude Code hooks (SessionStart + PreToolUse + UserPromptSubmit) son el sitio correcto para enforcement.

Sin construir `mcp/` no habríamos sabido si las reglas eran correctas hasta meterlas en GitHub Actions y rezar. Ahora sabemos que son correctas; sólo cambiamos el medio.

Lo que tiramos a la rama `reference-local-backend` no es código muerto. Es la **referencia ejecutable de la disciplina del framework**, en una forma autocontenida. Si alguien quiere usar SEM-AI sin GitHub (offline, regulated, classified), el modo `--backend=local` está ahí, validado, funcionando.

**El framework v0.2** = la disciplina sobre GitHub. **El framework v0.1** = la disciplina sobre SQLite. Misma IP, dos backends. La v0.2 es la primary; la v0.1 queda disponible.

---

*Documento generado por la sesión del 2026-05-22. Aprobado para ejecución mañana. Referencia: turns 78-91 de la conversación del loop.*
