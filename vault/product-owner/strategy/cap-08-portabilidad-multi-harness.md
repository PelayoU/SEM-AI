---
type: capability
id: cap-08-portabilidad-multi-harness
title: "Portabilidad multi-harness y distribución como `@sem-ia/cli`"

parent: goal-5-portabilidad

also-relates-to:
  - goal-1-auto-sostenibilidad
  - goal-7-ciclo-vida-producto
depends-on: []
dimensions-affected: [product, technical, operations, business, security]
related-adrs: []  # vacío hoy. Latentes aplicables (step-3): ADR-latente-001 (Claude Code primario), ADR-latente-006 (src/ vs .claude/ vs vault/)

status: active   # transición aplicada por /verify del WA wa-2026-05-12-002 el 2026-05-12T05:30+02:00
operational-status: planned   # esqueleto vacío en src/, documentación operativa en src/README.md + sección Pendientes del README raíz

fundamento-bibliografico:
  - Bass — Software Architecture in Practice (portability como QA + adapter pattern)
  - Martin — Clean Architecture (dependency inversion: universal contenido vs harness format)
  - Ford et al. — Building Evolutionary Architectures (deployability + evolvability)
  - Moore — Crossing the Chasm (distribución a adopters más allá del dogfooding)
  - Anthropic — Claude Code (harness target inicial)

qas-bass:
  - portability      # CRÍTICO — capability central
  - deployability    # adapters renderizables sin intervención manual
  - modifiability    # añadir adapters nuevos sin tocar universal/
  - security         # supply chain + filesystem mutation + parsing del frontmatter ajeno

tactics:
  - "Adapter pattern: cada harness target tiene su adapter en `src/adapters/<harness>/` que renderiza el contenido universal al formato del harness"
  - "Dependency inversion (Martin): `src/universal/` contiene contenido agnóstico de harness; los adapters dependen de universal/, no al revés"
  - "Schema-based validation: `src/universal/schemas/` define JSON schemas para validar frontmatter de nodos del vault (sem-ia validate)"
  - "Cross-link integrity check: `sem-ia check` valida que cross-links del grafo no estén rotos"
  - "AC coverage tool: `sem-ia check coverage` valida trazabilidad AC ↔ tests vía `// @ac-coverage:`"
  - "Safe defaults en CLI: parser YAML safe-load, path sanitization en `init`, confirmación antes de sobrescribir archivos existentes"

tradeoffs:
  - "Adapter overhead vs harness-native: mantener múltiples adapters es coste, mitigado por contenido universal compartido"
  - "Multi-harness multiplica maintenance — cada harness target = adapter + tests + docs específicas"
  - "Supply chain risk (npm): el paquete `@sem-ia/cli` puede ser vector de typosquatting / dependency confusion / comprometido upstream — mitigación: scope namespace registrado + pin de versiones + tests de integridad"
  - "Filesystem mutation en `sem-ia init` debe sanitizar paths y confirmar sobrescritura — vector de path traversal mitigable"
  - "YAML parsing en `validate` / `check` debe usar safe-load (no permissive eval) — vector RCE mitigable"

jtbd-outcome:
  quien: "Adopter externo greenfield (ingeniero individual o equipo) + dogfooding propio cuando distribuya"
  job: "Adoptar SEM-IA como framework de gestión de su proyecto, instalando vía npm y arrancando con un comando — sin necesitar entender la implementación interna ni el harness destino específico"
  outcome-esperado: "El adopter ejecuta `npm install -D @sem-ia/cli` + `npx sem-ia init --harness=<X>` y recibe estructura conforme. A partir de ahí opera SEM-IA exactamente como SEM-IA opera sobre sí mismo (CAP-01 a CAP-07 + CAP-10 disponibles). Comandos `validate`, `check`, `coverage` proveen herramientas de auditoría del grafo del adopter"
---

# CAP-08 · Portabilidad multi-harness y distribución como `@sem-ia/cli` [PLANNED]

## Enunciado

El framework es **portable entre harnesses** (Claude Code v1, OpenCode/Pi futuros) y **distribuible vía npm** como `@sem-ia/cli`. Adopter ejecuta `npx sem-ia init --harness=<X>` y recibe estructura conforme (`.claude/` o equivalente + vault skeleton + governance defaults + CLAUDE.md raíz). CLI provee bin scripts ergonómicos: `init`, `validate` (frontmatter contra schemas JSON), `check` (integridad de cross-links del grafo), `coverage` (AC ↔ tests). **Adapters por harness** hacen el "render" del contenido universal al formato del harness destino.

## Por qué es capability fuerte (4 criterios)

1. **Habilidad diferenciada**: distribuir el framework como producto consumible es habilidad distinta de operarlo (CAP-01 a CAP-07). Sin CAP-08, SEM-IA queda como experimento de un solo autor; con CAP-08, es framework adoptable.
2. **Sirve a goals con métrica clara**: goal-5 declara como métrica controlable *"adapter Claude Code funcional y publicado como `@sem-ia/cli`"*. Métrica directa.
3. **Cohesión interna**: adapters + universal + cli + package.json publishable — comparten el job *"distribuir el framework a adopters externos"*.
4. **No es trivialmente subcapability**: no es feature de CAP-07 (inception greenfield existiría para el dogfooding sin CLI distribuido). Es la **capa de distribución** del framework como producto.

## Piezas del bootstrap que la materializan (PLANNED — todas pendientes)

| Pieza | Path | Estado |
|---|---|---|
| `src/adapters/claude-code/` — bundled `.claude/` + CLAUDE.md raíz formato Claude Code | `src/adapters/claude-code/` | esqueleto vacío |
| `src/adapters/opencode/`, `src/adapters/pi/` — adapters futuros | `src/adapters/*/` | placeholder arquitectónico |
| `src/universal/` — contenido agnóstico de harness (vault skeleton + governance defaults + schemas JSON) | `src/universal/` | esqueleto vacío |
| `src/cli/` — bin scripts (`init`, `validate`, `check`, `coverage`) | `src/cli/` | esqueleto vacío |
| `package.json` publicable como `@sem-ia/cli` | raíz del proyecto, futura distribución | `package.json` actual es internal-only (npm scripts del dogfooding) |
| `src/README.md` | `src/README.md` | DOCUMENTADO — describe arquitectura prevista y build step desde adapters al dogfooding |

## Relación con goals

- **Goal-5 (portabilidad entre harnesses y proyectos)** — parent primario. Métrica controlable de goal-5: *"adapter Claude Code funcional y publicado como `@sem-ia/cli` (target inicial)"*.
- **Goal-1 (auto-sostenibilidad)** — adopters externos demuestran que el framework funciona más allá del dogfooding del propio autor.
- **Goal-7 (ciclo de vida producto)** — adopters externos sostienen producto con ciclo de vida en proyectos no-SEM-IA.

## Criterio observable para futuros `/verify`

Una feature descompuesta de CAP-08 es verificable si cumple:
- `npx @sem-ia/cli init --harness=claude-code` sobre directorio vacío produce estructura conforme (`.claude/`, `vault/`, `CLAUDE.md` raíz, `package.json`).
- `sem-ia validate <path-frontmatter>` retorna OK/FAIL según schema JSON.
- `sem-ia check` detecta cross-links rotos en el vault del adopter.
- `sem-ia check coverage` calcula cobertura AC ↔ tests cuando existen archivos `// @ac-coverage:`.
- El paquete publicado tiene LICENSE Apache 2.0 + `package.json` con author/license/repository declarados.
- Tests de integridad del paquete pasan en CI antes de publish.

## Features candidatas (preview)

1. **Adapter Claude Code** — bundled `.claude/` + CLAUDE.md raíz format. Sync desde `src/adapters/claude-code/` al dogfooding del repo SEM-IA via build step.
2. **Universal contenido agnóstico de harness** — vault skeleton, governance defaults (los 5 archivos canónicos), schemas JSON para validación de frontmatter.
3. **CLI bin `init`** — bootstrap en repo del adopter, sanitiza paths, confirma sobrescritura.
4. **CLI bin `validate`** — valida frontmatter contra schemas JSON.
5. **CLI bin `check`** — valida integridad de cross-links del grafo.
6. **CLI bin `check coverage`** — cobertura AC ↔ tests.
7. **Build step mecanismo** — sync de `src/adapters/claude-code/` al dogfooding del propio SEM-IA, sin duplicación (decisión pendiente: build script vs symlinks vs single source).
8. **Adapter OpenCode / Pi** — futuro, depende de demanda real de adopters externos.

## Notas / gaps operativos conocidos

- **Capability planned con esqueleto + docs**: el primer step será un WA `feature-design` para descomponer CAP-08 en features priorizadas (probablemente adapter Claude Code + CLI `init` como features iniciales críticas).
- **Decisión arquitectónica pendiente** (ADR latente — mecanismo de distribución desde adapters al dogfooding sin duplicación). Architect orquestará el ADR cuando se llegue a feature-design.
- **Vectores security desde el enunciado** (declarados arriba en tactics + tradeoffs): supply chain + path traversal + YAML parsing + template injection. Cuando CAP-08 se descomponga, threat-modeling formal con Security Officer.
- **LICENSE Apache 2.0**: sin riesgo viral, compatible con redistribución y forks comerciales. Compliance npm publishing: pendiente registrar scope `@sem-ia` + declarar dependencias compatibles + NOTICE file si aplicable.
- **GTM latente**: el catálogo de capabilities (este documento) será product tour para adopters externos al descubrirse el framework.
