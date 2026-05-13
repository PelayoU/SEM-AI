---
type: capability
id: cap-09-adopcion-retroactiva
title: "Adopción retroactiva desde proyecto pre-existente"

parent: goal-5-portabilidad

also-relates-to:
  - goal-6-articulacion-publica
  - goal-7-ciclo-vida-producto
depends-on:
  - cap-08-portabilidad-multi-harness  # adopción retroactiva requiere CLI distribuible para arrancar
dimensions-affected: [product, technical, security]
related-adrs: []  # vacío hoy

status: active   # transición aplicada por /verify del WA wa-2026-05-12-002 el 2026-05-12T05:30+02:00
operational-status: planned   # P1 del README, nada construido

fundamento-bibliografico:
  - Cagan — Inspired (adopters legacy + maduros como mercado distinto del greenfield)
  - Ford et al. — Building Evolutionary Architectures (archaeology de boundaries existentes)
  - Ousterhout — A Philosophy of Software Design (information hiding aplicado a denylist de paths sensibles)
  - Nygard — ADRs (retroactivos a partir de decisiones implícitas en el código)
  - Shostack — Threat Modeling (secret leakage como vector security crítico de esta capability)

qas-bass:
  - portability      # extender SEM-IA a tipos de proyecto pre-existentes
  - testability      # el walk de código debe ser auditable
  - security         # CRÍTICO — secret leakage es vector inherente
  - reliability      # archeology debe ser idempotente (re-derivar produce resultado equivalente)

tactics:
  - "Archeology walk: skill `architecture-archeology` (Architect) recorre código del adopter — inventario de módulos, boundaries, acoplamientos, decisiones técnicas implícitas"
  - "Read-only mode: skills existentes (`spec-writing`, `feature-decomposition`, `capability-derivation`) tienen modo lectura — leen artefactos pre-existentes en lugar de conversar"
  - "Denylist by default (Ousterhout information hiding aplicado a security): paths comunes con secrets (.env*, *.pem, *.key, credentials*, .aws/, .ssh/, secrets/) excluidos del walk por defecto"
  - "Pattern scanning: detección de patrones sensibles (AKIA, ghp_, sk-, PRIVATE KEY blocks) antes de citar fragmento en frontmatter o ADR retroactivo"
  - "Redacted-by-default: contenidos citados desde código del adopter son redactados; opt-in explícito por archivo para incluir fragmento literal"
  - "Derivación auditable: campo `derived-from` en frontmatter del nodo trazea a archivo+versión del adopter del que se derivó"

tradeoffs:
  - "Walk de código heterogéneo no-trivial — diferentes lenguajes, estructuras de proyecto, convenciones. Architect lo flagea como riesgo viability técnico significativo (testability + modifiability)"
  - "Secret leakage es riesgo crítico — sin diseño security-first, walk indiscriminado puede absorber secrets al vault SEM-IA y commitearlos al repo (duplicación de secrets en grafo)"
  - "ADR retroactivos pueden ser especulativos — derivar decisiones implícitas del código requiere interpretación del Architect; ADRs deben marcarse como `retroactive-inferred` para distinguir de ADRs propuestos en su momento"
  - "Idempotencia: re-derivar grafo desde código actualizado puede producir resultado distinto si el código cambió — vigilar como fitness function"

jtbd-outcome:
  quien: "Equipo con proyecto a medias (greenfield no aplica) — código + docs existentes, sin vault SEM-IA"
  job: "Adoptar SEM-IA como framework de gestión sin tener que reescribir el proyecto desde cero — derivando el grafo retroactivamente desde código + docs existentes"
  outcome-esperado: "El equipo ejecuta `/adopt <path>` (o equivalente CLI), Architect ejecuta archeology walk, las skills modo-lectura producen capability files / feature files / spec files retroactivos con `derived-from`, los secrets se redactan por defecto, y el grafo emerge poblado conformante. El adopter continúa con SEM-IA desde ese punto sin haber tenido que rehacer el código"
---

# CAP-09 · Adopción retroactiva desde proyecto pre-existente [PLANNED]

## Enunciado

El sistema permite a un equipo con **proyecto a medias** (código + docs ya existentes, sin vault SEM-IA) llevar el proyecto a SEM-IA **derivando el grafo retroactivamente**. Mecanismo (pendiente): slash `/adopt <path>` + skill `architecture-archeology` (Architect walk de código → inventario módulos/boundaries/coupling → ADRs retroactivos candidatos) + **modo "lectura"** en skills existentes (leen artefactos pre-existentes en lugar de conversar) + campo `derived-from` en frontmatter para trazabilidad de derivación retroactiva. **Security-by-default**: denylist + pattern scanning + redacted-by-default + opt-in por archivo.

## Por qué es capability fuerte (4 criterios)

1. **Habilidad diferenciada**: adopción retroactiva es habilidad distinta de inception greenfield (CAP-07). El job es distinto: greenfield = arrancar desde nada; retroactiva = mapear lo ya construido. Mismo target (adopter) pero contexto distinto.
2. **Sirve a goals con métrica clara**: goal-5 declara como aplicabilidad *"greenfield + existing"* — el "existing" requiere CAP-09. Sin ella, SEM-IA queda excluido de proyectos no-greenfield.
3. **Cohesión interna**: `/adopt` + skill `architecture-archeology` + modo lectura de skills + `derived-from` + security defaults — comparten el job *"importar grafo retroactivamente desde código existente"*.
4. **No es trivialmente subcapability**: no es feature de CAP-07 (greenfield no contempla código pre-existente) ni de CAP-08 (CLI distribuible no implica adoptar legacy). Es habilidad propia.

## Piezas (TODAS PLANNED — nada construido)

| Pieza | Estado |
|---|---|
| Slash `/adopt <path>` | planned (P1 del README) |
| Skill `architecture-archeology` (Architect) | planned (pending en `_pending-later.md`) |
| Modo "lectura" en `spec-writing`, `feature-decomposition`, `capability-derivation` | planned (modificación de skills existentes) |
| Campo `derived-from` en frontmatter | declarado como opcional en `workflows.md`, sin uso activo hoy |
| Fase SDLC `adoption` nueva (opcional) | planned (decisión pendiente: ¿fase nueva o se acomoda en `discovery`?) |
| Template `adopt` con steps | planned |
| Security defaults (denylist + pattern scanning + redacted) | planned (decisión arquitectónica + threat-model formal por Security Officer) |

## Relación con goals

- **Goal-5 (portabilidad a tipos de proyecto: greenfield + existing)** — parent primario.
- **Goal-6 (articulación pública)** — adopters externos con proyectos legacy refuerzan articulación del framework.
- **Goal-7 (ciclo de vida producto)** — el framework cubre lifecycle también para proyectos no-greenfield (legacy con años de evolución pueden adoptar).

## Criterio observable para futuros `/verify`

Cuando CAP-09 sea operant, una feature descompuesta es verificable si cumple:
- `/adopt <path>` arranca archeology walk del directorio destino sin tocar nada fuera de él.
- Walk respeta denylist por defecto (no lee `.env`, `*.pem`, credenciales, `.aws/`, `.ssh/`, `secrets/`).
- Walk escanea patrones sensibles (AKIA, ghp_, sk-, PRIVATE KEY) antes de citar fragmento.
- Frontmatter de cualquier nodo derivado incluye `derived-from` con path+versión.
- Contenidos citados desde código del adopter están redactados por defecto.
- Threat-model formal del walk existe y AC-S* derivados están en spec.

## Features candidatas (preview)

1. **Slash `/adopt`** y template SDLC `adopt`.
2. **Skill `architecture-archeology`** (Architect) — walk + inventario + boundaries + ADRs retroactivos candidatos.
3. **Modo lectura en skills existentes** — `capability-derivation`, `feature-decomposition`, `spec-writing` operan sobre artefactos pre-existentes.
4. **Campo `derived-from`** activo + parsing/visualización.
5. **Security defaults completos** — denylist + pattern scanning + redacted-by-default + opt-in.
6. **Validación del walk** — idempotencia (re-derivar produce resultado equivalente), límites de profundidad, exclusión de binarios.

## Notas / gaps operativos conocidos

- **Flag Architect (viability-review step-3)**: dimensions-affected potencialmente debería incluir `business` cuando se descomponga — licensing del adopter en el código sometido a archeology walk podría tener implicaciones (Apache 2.0 vs GPL del proyecto adopter). PO defiere a feature-design (no añade en capability file hoy: licensing es marginal porque CAP-09 lee, no redistribuye).
- **Capability planned con NADA construido** (solo documentada en README sección "Pendientes — capability 'Adopción retroactiva'"). Su construcción requiere: feature-design dedicado + threat-model formal del walk + ADR(s) sobre decisiones técnicas (qué walker, cómo parsear lenguajes, etc.).
- **Architect viability flag** (post-step scope-scan WA-002): walk de código heterogéneo es no-trivial técnicamente. Riesgo viability significativo — Architect debe declarar QAs Bass `testability` + `modifiability` con tradeoffs explícitos cuando se descomponga.
- **Security vector crítico**: secret leakage al replicar al vault. Diferenciado de CAP-04 (verificación) y de CAP-08 (supply chain): aquí el vector emerge del walk del código del adopter, no del framework mismo. Threat-model formal obligatorio antes de implementar.
- **Dependencia técnica de CAP-08**: probablemente el `/adopt` se invoca desde el CLI `@sem-ia/cli` distribuible. Sin CAP-08, no hay CLI donde implementar `/adopt`.
