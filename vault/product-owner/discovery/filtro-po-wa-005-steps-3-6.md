---
type: filtro-po
id: filtro-po-wa-005-steps-3-6
status: active
related-wa: wa-2026-05-13-005
related-step: steps-3-4-5-6 (post-step scope-scan consolidado)
created: 2026-05-13T06:30:00+02:00
author: product-owner
---

# Filtro PO consolidado — Steps 3-6 paralelos del WA-005

## Veredictos recibidos

| Asesor | Veredicto | Flags |
|---|---|---|
| Architect | apto-con-correcciones-menores | 3 cross-link cat Media; 4 cat Baja |
| Designer | apto-con-correcciones | 4 flags medios cross-link YAML; 3 bajos |
| Business-analyst | apto | 0 críticos; flags scheduling aparcados |
| Security-officer | aprobado | 0 críticos; 3 ADRs latentes recomendados |

## Conteo flags

- **Total flags recibidos**: ~14 (3+4+4+3+0 según severidad media/baja)
- **Cat-1 confirmadas tras test load-bearing**: 3
- **Ratio cat-1 / total**: 3/14 = **21%** → NO high-suspicion mecánico (umbral 60%).

Auto-audit: **OK** — pelea fuerte aplicada honestamente, mayoría descartada con razón fuerte.

## Tabla por flag

| # | Flag (resumen) | Advisor | Cat inicial | Test load-bearing | Razón fuerte | Veredicto final |
|---|---|---|---|---|---|---|
| 1 | feature-018 +`also-relates-to: feature-010` | Architect | 1 | (1) NO — `depends-on: feature-010` ya declarado en frontmatter es coupling más fuerte. (2) NO degrada. (3) Out-of-scope. | Coupling transitivo over-declarado. depends-on cubre el caso. | **cat-2 descartado** |
| 2 | feature-036 +`also-relates-to: feature-034` | Architect | 1 | (1) SÍ — feature-034 /sessions es uno de los mecanismos que cubre el JTBD orientación. (2) Sí degrada (gap navegación). (3) Sí en scope CAP-F. | Aporta navegación entre features de orientación. Load-bearing. | **cat-1 aplico** |
| 3 | feature-038 ↔ feature-019 bidireccional | Architect | 1 | (1) NO — PO Modo 1 (feature-038) NO incluye /verify (eso es Modo 3). (2) NO degrada. (3) Out-of-scope. | feature-038 cubre Modo 1; /verify es Modo 3 — coupling artificial. | **cat-2 descartado** |
| 4 | feature-033 +cross-links a cap-03/feature-035/018/019 | Designer | 1 | (1) NO — feature-033 lee WAs (Nivel 2 ADR via feature-014 transitivo). (2) NO degrada. (3) Out-of-scope coupling transitivo. | Coupling transitivo. depends-on: feature-014 (Nivel 2 declarado) cubre. | **cat-2 descartado** |
| 5 | feature-035 ↔ feature-038 relación bidireccional rota | Designer | 1 | (1) SÍ — feature-038 declara depends-on:feature-035 pero feature-035 no tiene cross-link back a feature-038. (2) Sí degrada navegación bidireccional grafo. (3) Sí en scope. | Coupling apropiado bidireccional Ford. | **cat-1 aplico** |
| 6 | feature-032 +`also-relates-to: cap-01` | Designer | 1 | (1) SÍ — feature-032 AC-A4 (backlog query) consume convención CAP-A estados canónicos. (2) Sí degrada navegación. (3) Sí en scope. | Load-bearing para auditabilidad backlog query. | **cat-1 aplico** |
| 7 | feature-033 sin `also-relates-to: cap-03` | Designer | 1 | (1) NO — transitivo via feature-014 Nivel 2. (2) NO. (3) Out. | Mismo razonamiento que #4. | **cat-2 descartado** |
| 8 | ADR-secret-hygiene candidato adicional | Security | 1 | (1) SÍ — convención secret hygiene NO está en lista heredada (15). (2) Sí degrada visibilidad. (3) Sí. | Aporta candidato genuino para Lote B no duplicado. | **cat-1 aplico** (añadir a lista Lote B) |
| 9 | ADR-filesystem-changes-audit candidato | Security | 1 | (1) NO — duplica con feature-024 Nivel 3 protocolo (Gap 9 ya formalizado). NO es decisión arquitectónica nueva. | Protocolo ya documentado. NO ADR. | **cat-2 descartado** |
| 10 | ADR-security-trans candidato | Security | — | Ya está en lista heredada (12 architect + 3 emergentes = 15). | Confirma uno ya identificado. | **cat-3 ya diferido** (incluido en Lote B) |
| 11 | feature-038 PO Modo 1 denso (informativo) | Designer | 3 | Diferido conscientemente. | feature-038 borderline grande pero descomponible. NO sub-dividir ahora. | **cat-3 aparcado** |
| 12 | Artefactos físicos README/glosario/ruta a WA feature-build posterior | Designer | 3 | Decisión humana confirmada (aceptar conscientemente). | Scheduling consciente — ya documentado. | **cat-3 aparcado** |
| 13 | Gap Pragmatists (features 044/045 no materializadas) | Business | 3 | Idem #12. | Decisión humana. | **cat-3 aparcado** |
| 14 | Requerimiento WA feature-build feature-041 antes 2026-05-22 | Business | 4 | **Decisión humana real** sobre prioridad post-WA-005. | Compromiso operativo del humano. | **cat-4 humano** |

## Decisiones cat-1 aplicadas (3)

1. feature-036 — añadir `also-relates-to: feature-034-slash-sessions`
2. feature-035 — añadir `also-relates-to: feature-038-po-modo-1` (bidireccional al `depends-on` de feature-038)
3. feature-032 — añadir `also-relates-to: cap-01-grafo-declarativo-persistente`

Más: ADR-secret-hygiene añadido a lista Lote B (ahora 16 candidatos: 15 architect + 1 security nuevo).

## Decisiones cat-2 descartadas (5)

Razones fuertes documentadas arriba en tabla. Patrón común: coupling transitivo over-declarado (Cohn INVEST `I = Independent` requiere coupling mínimo declarado, NO máximo).

## Decisiones cat-3 diferidas (3)

- Granularidad feature-038 borderline: aceptable, no sub-dividir ahora.
- Scheduling artefactos físicos features 044/045: decisión humana confirmada.
- Gap Pragmatists: idem.

## Decisión cat-4 humana (1)

Requerimiento operativo: arrancar WA `feature-build` de feature-041 antes del 2026-05-22 para cumplir GISF. **Decisión post-WA-005 del humano**, NO bloqueante para `/verify` del WA-005 actual.

## Lecciones aplicadas (regla 12 PO agent file)

- Test load-bearing aplicado fila por fila.
- Auto-audit numérica: 21% cat-1 — NO high-suspicion.
- Artefacto declarativo escrito (este archivo) antes de aplicar cambios al filesystem.
- Pelea fuerte: 5 flags descartados con razón bibliográfica (Cohn INVEST `I` + Ford appropriate coupling + Ousterhout deep modules).
