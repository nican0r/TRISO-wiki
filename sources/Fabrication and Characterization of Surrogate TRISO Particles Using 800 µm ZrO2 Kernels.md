---
type: source
title: Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels
authors: [Jolly, B.C., Helmreich, G., Cooley, K., Dyer, J., Terrani, K.A.]
org: ORNL
year: 2016
doc-id: ORNL/LTR-2016/315 (M3FT-16OR020201065)
pdf: raw/pdf/fab-and-characterization-surrogate-triso-particles.pdf
md: raw/md/fab-and-characterization-surrogate-triso-particles.md
pages: 31
ingested: 2026-09-23
status: draft
tags: [triso, cvd, fabrication, surrogate, zro2, sic, pyc, argon, qa-qc, conflict, inferred]
updated: 2026-09-23
---

# Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels
> ORNL (Oak Ridge National Laboratory), 2016. ORNL/LTR-2016/315. Letter report, 12 pp. text + 19 pp. appendix data forms. Page citations use the PDF page markers (p.1–31); printed page numbers are 2 lower.
> [PDF](../raw/pdf/fab-and-characterization-surrogate-triso-particles.pdf) · [converted](../raw/md/fab-and-characterization-surrogate-triso-particles.md)

**Gist** — ORNL coated 800 µm yttria-stabilised ZrO₂ kernels with all four TRISO layers by FBCVD (fluidised bed chemical vapour deposition) to make uranium-free particles for FCM (fully ceramic microencapsulated) fuel development. Twenty-nine development runs set the conditions for a final batch, ZrX800-30T, for which the report gives complete per-layer gas flows, bed temperatures and times. Every property measured met the AGR-1 (US Advanced Gas Reactor programme, first irradiation) specification; IPyC density could not be measured. Single batch, one lab, internal report — the recipe is a demonstrated condition, not an optimum.

## Key findings
- **Full gas recipe for all four layers** — flows of Ar, H₂, C₂H₂, C₃H₆ and MTS (methyltrichlorosilane), coating gas fraction and propylene/acetylene ratio — `p.5`, Table 2. Reproduced on [[TRISO Coating Parameters]].
- **SiC at 1425 °C in 1:1 Ar–H₂** met density ≥ 3.19 g/cm³ (3.1983) and the grain-size standard — `pp.5, 8–10`. Below the 1500–1600 °C H₂ window on [[SiC Layer Deposition]]; argon plausibly accounts for it (see that page).
- **Bed temperature measured directly** with a handheld optical pyrometer through a top sight glass and prism, corrected for measured attenuation — `p.5`. Contrasts with the wall-thermocouple practice on [[TRISO Coating Reactor Design]].
- **Buffer at 1425 °C, 1.15 min for 98.7 µm** — the fastest buffer in the wiki and 165–175 °C hotter than the other lines — `pp.5, 8`.
- **Processing conditions had to be redeveloped for the surrogate** because ZrO₂ differs from UCO in size, density and thermal properties — `p.3`, Table 1. See [[TRISO Coating Process#Surrogate kernels]].
- **Layer separation for density measurement failed or needed workarounds.** IPyC would not separate from the buffer; OPyC had to be picked off glued particles. The authors hypothesise flatter interfaces on 800 µm kernels versus 350 µm AGR-1 kernels — `p.7`. Contradicts [[Ch 04 — QA-QC and Characterization]] p.42 on OPyC; flagged on [[TRISO Coating Process]].
- **Engineered weak buffer/IPyC interface**: standard buffer, then +100 °C for 5 s, giving a thin lower-density outer band. Barely eased separation and was dropped; noted as potentially useful because a weak buffer/IPyC bond lets the buffer debond without tearing the IPyC in service — `p.11`.
- **SiC outer surface rougher than AGR-1 particles**; roughness is not in the specification and its performance effect is unknown — `p.9`.
- AGR-1 particles showed no fission product release detected after 19.5 %FIMA (fissions per initial metal atom) — `p.3`. Cited as the reason for adopting the AGR-1 specification.

## Data extracted

**Kernels** (Table 1 p.3; measured lot ZrX800-K, Table 3 p.7):

| Property | AGR-1 UCO | UN (uranium nitride) | ZrO₂ surrogate | ZrX800-K measured |
|---|---|---|---|---|
| Diameter (µm) | 350 | 800 | 800 | 813.7 ± 25.0 |
| Density (g/cm³) | 10.92 | 12.53 | 6.0 | 6.032 ± 0.030 |
| Specific heat (J/g·K) | > 0.3 | 0.25 | 0.45–0.65 | — |
| Thermal conductivity (W/m·K) | < 5 | 15.5 (literature, 1000 °C) | < 4 | — |
| Ellipticity (Dmax/Dmin) | — | — | — | 1.015 |
| Mass per kernel (mg) | — | — | — | 1.592 |

Composition 95 % ZrO₂, 5 % Y₂O₃ (Tosoh YTZ grinding media) — `p.6`.

**Coating conditions, ZrX800-30T** (Table 2, p.5):

| Parameter | Buffer | IPyC | SiC | OPyC |
|---|---|---|---|---|
| Time (min) | 1.15 | 8.6 | 123.87 | 7.6 |
| Temp. (°C) | 1425 | 1265 | 1425 | 1290 |
| Ar (sccm) | 4,620 | 10,625 | 7,500 | 14,025 |
| H₂ (sccm) | — | — | 7,500 | — |
| C₂H₂ (sccm) | 6,380 | 1,014 | — | 1,338 |
| C₃H₆ (sccm) | — | 861 | — | 1,137 |
| MTS (sccm) | — | — | 71 | — |
| Total (sccm) | 11,000 | 12,500 | 15,071 | 16,500 |
| CGF (precursor ÷ total) | 0.58 | 0.15 | 0.0047 | 0.15 |
| CGR (C₃H₆ ÷ C₂H₂) | — | 0.85 | — | 0.85 |

**Characterization vs AGR-1 specification** (Table 4, p.8):

| Property | Specification | ZrX800-30T | Page |
|---|---|---|---|
| Buffer thickness (µm) | 90 ± 15 (reduced from 100) | 98.7 | p.8 |
| IPyC thickness (µm) | 40 ± 4 | 41.3 | p.8 |
| SiC thickness (µm) | 35 ± 3 | 32.9 | p.8 |
| OPyC thickness (µm) | 40 ± 4 | 43.1 | p.8 |
| Buffer density (g/cm³) | 1.03 ± 0.15 | 1.01 (from buffer-only run ZrX800-11B, same conditions) | p.8 |
| IPyC density (g/cm³) | 1.90 ± 0.05 | not measured | p.8 |
| SiC density (g/cm³) | ≥ 3.19 | 3.1983 (SD 0.0021, 42 fragments) | pp.8, 28 |
| OPyC density (g/cm³) | 1.90 ± 0.05 | 1.8937 (SD 0.0354, 29 fragments) | pp.8, 29 |
| IPyC anisotropy (BAFo) | ≤ 1.035 | 1.0149 | pp.8, 30 |
| OPyC anisotropy (BAFo) | ≤ 1.035 | 1.0153 | pp.8, 31 |
| SiC grain size | AGR-1 visual standard | smaller than maximum | pp.8–10 |

> [!info] Inferred — OPyC density passes on the mean only
> The p.29 data form shows two fragment populations: 6 of 29 at 1.824–1.830 g/cm³, below the 1.85 lower limit, and 23 at 1.900–1.926. The mean (1.8937) passes. The report does not comment. Whether the low group is a second density population in the layer or a fragment-preparation artefact would need the fragment source or a repeat measurement.
> `#inferred`

## Figures kept

![[ornl-surrogate-p04-fig01-fbcvd-furnace.jpeg]]
*Fig. 1, p.4 — ORNL FBCVD furnace: conical graphite coating chamber, resistively heated graphite element, water-cooled gas injector, sight glass on top.*

![[ornl-surrogate-p09-fig03-triso-cross-section.jpeg]]
*Fig. 3, p.9 — optical cross-section of a ZrX800-30T particle.*

![[ornl-surrogate-p10-fig04-05-sic-grain-size.jpeg]]
*Figs. 4–5, p.10 — backscatter SEM (scanning electron microscope) of the ZrX800-30T SiC (top; note the rough outer edge) against the AGR-1 visual standard for maximum allowable grain size (bottom).*

![[ornl-surrogate-p11-fig06-modified-buffer.jpeg]]
*Fig. 6, p.11 — run ZrX800-19I, showing the thin lower-density outer band of the modified buffer.*

Skipped: Fig. 2 (bare kernels, p.6) and Figs. 7–25 (run sheets, gas certificates and data report forms, pp.13–31; the numbers are used above).

## Internal inconsistencies
- Fig. 1 is captioned as the furnace "used for TRISO coating of UN kernels" (p.4) in a report about ZrO₂ coating; presumably the same furnace.
- Table 3 labels kernel-weight and volume scatter "Std. Dev." (p.7); the data forms give these as standard errors in the mean (pp.26–27).
- Table 4 reports anisotropy as BAFo (p.8); the 2-MGEM (two-modulator generalised ellipsometry microscope) data forms report OPTAF (optical anisotropy factor) = (1+N)/(1−N) from diattenuation N (pp.30–31).

## What this changes in the wiki
- First per-layer gas flows and coating gas fractions in [[TRISO Coating Parameters]]; fourth line added, plus AGR-1 tolerances.
- Adds a sub-window SiC temperature (1425 °C) that meets density spec in Ar–H₂ — [[SiC Layer Deposition]], SiC temperature conflict on [[TRISO Coating Parameters]].
- Widens the buffer-rate conflict from ~4× to ~9×, and adds a buffer-temperature disagreement — [[TRISO Coating Parameters]].
- First bed-temperature measurement by optical pyrometer — [[TRISO Coating Reactor Design]], [[Fuel Quality Control and Characterization]].
- Contradicts easy OPyC separation ([[Ch 04 — QA-QC and Characterization]] p.42) — [[TRISO Coating Process]].
- New section on surrogate kernels — [[TRISO Coating Process#Surrogate kernels]].
- Fourth buffer thickness and the weak buffer/IPyC interface — [[TRISO Particle Architecture]].

## Open questions raised
- Coater diameter and batch mass are not given; the gas flows cannot be converted to superficial velocity or MTS flux per bed area without them. Ref. [7] (Jolly et al., ORNL/LTR-2015/432) may have them.
- Whether this recipe carries over to UN kernels, which are 800 µm like the surrogate but twice as dense (12.53 vs 6.0 g/cm³, p.3).
- The 29 development runs are reported elsewhere (ref. [7]); that report would show which parameters were moved to reach this recipe.

## Pages updated on ingest
- [[TRISO Coating Parameters]], [[TRISO Coating Process]], [[SiC Layer Deposition]], [[TRISO Coating Reactor Design]], [[Fuel Quality Control and Characterization]], [[TRISO Particle Architecture]], index
