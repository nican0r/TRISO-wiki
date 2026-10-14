---
type: source
title: FY 2008 Six-Inch Diameter Coater Test Report
aliases: [Barnes and Marshall 2008, INL/EXT-08-14633, B&W six-inch coater]
authors: [Barnes, C.M., Marshall, D.W.]
org: INL (Next Generation Nuclear Plant Project); coater operated by Babcock & Wilcox
year: 2008
doc-id: INL/EXT-08-14633
url: https://inldigitallibrary.inl.gov/sites/sti/sti/7363961.pdf
pdf: raw/pdf/6-in-diam-coater-test-report.pdf
md: raw/md/6-in-diam-coater-test-report.md
pages: 53
ingested: 2026-10-14
status: draft
tags: [triso, cvd, fabrication, sic, pyc, scale-up, process-monitoring, pressure-fluctuations, conflict]
updated: 2026-10-14
---

# FY 2008 Six-Inch Diameter Coater Test Report
> INL / Babcock & Wilcox, September 2008. INL/EXT-08-14633. 53 pp. Page citations use the PDF page markers; printed page numbers are 16 lower (printed p.1 = PDF p.17).
> [PDF](../raw/pdf/6-in-diam-coater-test-report.pdf) · [converted](../raw/md/6-in-diam-coater-test-report.md)

**Gist** — Thirty coating runs in a 6-inch (15.2 cm) production-scale coater, done to set AGR-2 (second US Advanced Gas Reactor irradiation) coating conditions, to choose a variant SiC condition, and to test whether bed pressure fluctuations can serve as a real-time process signal. It is the only source in the wiki reporting both the control-thermocouple setpoint and the bed temperature for the same runs, and the only one with hot-coater hydrodynamic measurements on real kernels — 400 Hz pressure records at three points in every layer. Process development, not a controlled study: conditions move between runs and several results are explicitly uncertain.

## Key findings

### Temperature and its control

- **Control temperature is not bed temperature.** A control setpoint of 1600 °C corresponds to a bed temperature of 1430–1500 °C for SiC, and the AGR-2 argon variant is specified as control 1550 °C, "estimated to correspond to a bed temperature of 1430–1450 °C" — `pp.7, 26`. A 100–170 °C gap. See [[TRISO Coating Parameters#Conflicts]].
- **Bed temperature is not even constant within a layer.** During the 4–7 minute buffer deposition the bed runs from ~1390 °C to ~1540 °C at a fixed 1470 °C control setpoint, where a small coater holds 1450 °C throughout — `p.19`.
### Layers and specifications

- **SiC density falls with MTS (methyltrichlorosilane) concentration**; above ~2.0 mol% MTS in hydrogen it drops below the 3.19 g/cm³ specification. Adding 20–30 % argon restores density at 2.78–3.17 % MTS and a lower setpoint, which is how the AGR-2 variant was chosen — `p.26`.
- **IPyC density is set by bed temperature, and that relation survives scale-up**: ~1.90 g/cm³ at ~1265 °C in both the ORNL 2-inch and the B&W 6-inch coater, though the slope is shallower in the larger one, giving a wider operating window — `p.21`.
- **Thermocouple drift put two run series off specification** — pyrocarbon densities fell to 1.78–1.86 g/cm³ against a 1.90 target — and was only discovered when characterization data came back, after the runs — `p.21`.
- **Buffer density wandered 0.94–1.10 g/cm³ across runs in which nothing was deliberately changed** — `p.19`. The cause is unexplained and a dedicated study is recommended.
- **SiC defect fraction correlates with no coating parameter** the report measured, varying over two orders of magnitude (<0.2 to 67 defects per 50,000 particles). It does correlate with layer thickness: of batches at ≥34.5 µm mean SiC, 13 of 15 passed; below that, 2 of 10. The report recommends moving the thickness specification from 35 ± 3 µm to ≥ 37 ± 3 µm — `p.27`.
### Bed behaviour

- **Pressure fluctuations carry particle-property information.** Multivariate regressions on Hurst exponents and inlet pressures predict IPyC and OPyC diattenuation and final particle aspect ratio — `pp.45–47`. Detail on [[Coater Process Monitoring]].
- **Coated ZrO₂ surrogates do not reproduce the bed hydrodynamics of coated NUCO (natural-enrichment uranium oxycarbide)** even at matched particle diameter and density: the regressions have to be fitted separately and some coefficients come out with opposite signs. Candidate causes offered are rotational inertia (mass distributed differently within the particle) and thermal diffusivity — `p.46`.
- **Argon-variant SiC changes the nozzle, not just the layer**: accretions are shorter but more occluded, attributed to the lower gas flow sweeping less heat from the nozzle; the OPyC pressure signature afterwards is persistently different, which the authors read as a vessel effect rather than a particle effect — `p.44`.
- **IPyC and OPyC come out different from near-identical recipes**: OPyC surface-connected porosity 0.4–0.8 ml/m² against IPyC 2.0–2.4, attributed partly to the higher IPyC coating rate and partly to the IPyC being annealed during SiC deposition — `pp.8–9`.

## Data extracted

| Parameter | Value | Conditions | Page |
|---|---|---|---|
| Control → bed temperature, SiC | 1600 → 1430–1500 °C | 18 hydrogen-only runs | p.26 |
| Control → bed temperature, AGR-2 variant | 1550 → 1430–1450 °C (estimated) | 30 % argon | p.7 |
| Buffer control / bed temperature | 1470 °C / 1390–1540 °C | during 4–7 min deposition | p.19 |
| Buffer density range | 0.94–1.10 g/cm³ | CGF (coating gas fraction) 0.54–0.61, 1.3–1.5 kg charge | p.19 |
| Buffer coating rate | 15.8–24.4 µm/min | same runs | p.19 |
| AGR-1 buffer (2-inch coater) | 1450 °C bed, 1.08–1.11 g/cm³ | constant-temperature control | p.19 |
| IPyC density at ~1265 °C bed | 1.90 g/cm³ | both 2-inch and 6-inch coaters | p.21 |
| MTS limit, hydrogen only | < 2.0 mol% | control 1600 °C, to hold ≥ 3.19 g/cm³ | p.26 |
| MTS with argon | 2.78–3.17 % at 20–30 % Ar | control 1550 °C, density above spec | p.26 |
| H₂/MTS to avoid free carbon | > ~30 | cited, not measured here | p.26 |
| SiC coating rate, baseline | < 0.3 µm/min | ~2 h for a 35 µm layer | p.26 |
| Coating-time saving, argon variant | ~10 % | total gas flow cut ~36 % to hold fluidisation | p.26 |
| SiC defect fraction spread | <0.2 to 67 per 50,000 particles | 22 runs + 4 AGR-2 runs | p.27 |
| Kernel charge | 1.3–1.5 kg | NUCO, LEU UCO, ZrO₂ | pp.7, 19 |
| Pressure sampling | 400 Hz, 8 s, three times per layer | reduced from 500 Hz / 5 s | p.40 |
| Bed volume growth during buffer | ~3× | — | p.40 |

Per-layer conditions sit alongside the other lines on [[TRISO Coating Parameters]].

## Figures kept

![[bw-coater-p22-fig02-ipyc-density-vs-bed-temperature.jpeg]]
*Fig. 2, p.22 — IPyC density against bed temperature for the 2-inch (ORNL) and 6-inch (B&W) coaters. Same density at the same temperature; shallower slope in the larger coater.*

![[bw-coater-p27-fig08-sic-density-vs-mts.jpeg]]
*Fig. 8, p.27 — SiC density against MTS concentration. Hydrogen-only runs fall below 3.19 g/cm³ above ~2 % MTS; the argon runs sit above it at ~3 %.*

Skipped: the pressure-fluctuation traces and STFT plots (Figs. 21–23, pp.40–43), the strange-attractor plots (Figs. 26–27, p.44) and the regression scatter plots (Figs. 28–30, pp.45–47) — the quantitative content is in the text and on [[Coater Process Monitoring]].

## What this changes in the wiki

- Supplies the control-versus-bed temperature offset that reframes the SiC temperature conflict on [[TRISO Coating Parameters]] from a process disagreement to a measurement-position one.
- New page [[Coater Process Monitoring]] — this is the only in-run instrumentation evidence in the wiki.
- Second half of the PyC parameter→property map on [[PyC Layer Deposition]], at production scale.
- Qualifies "nothing transfers for free" on [[TRISO Coating Reactor Design]]: IPyC density vs bed temperature does transfer between 2-inch and 6-inch coaters.
- Hardens the surrogate-kernel caution on [[TRISO Coating Process]] with a hydrodynamic, not just chemical, reason.
- New conflict on buffer deposition temperature (below).

> [!warning] Conflict — buffer deposition temperature
> This line coats the buffer at a 1470 °C setpoint with the bed at 1390–1540 °C (`p.19`), and the AGR-1 2-inch coater at a constant 1450 °C bed. [[TRISO Coating Parameters]] records 1250 °C (IAEA generic), ~1260 °C (INET) and 1425 °C (ORNL, bed) for the same layer. The ORNL and US AGR figures are bed temperatures, so the ~200 °C gap to the German/INET lines is not a measurement-position artefact. Both produce acceptable buffer density. Unresolved.
> `#conflict`

## Open questions raised

- The internal thermocouple was removed from the B&W coater in early 2008, so most 2008 bed temperatures are inferred from IPyC density rather than measured (`pp.21, 51`); reinstating it is the first recommendation in the conclusions.
- No bed temperature at all is known for the argon-codilution runs (`p.26`), which are the ones that became the AGR-2 variant.
- Whether the internal thermocouple itself causes SiC defects is posed and unanswered (`p.51`).
- B&W and ORNL porosimeters disagree on OPyC surface-connected porosity; the instruments differ in model (`p.9`).

## Pages updated on ingest
- [[Coater Process Monitoring]] (new), [[PyC Layer Deposition]] (new), [[TRISO Coating Parameters]], [[TRISO Coating Reactor Design]], [[SiC Layer Deposition]], [[TRISO Coating Process]], [[Fuel Quality Control and Characterization]], index, log, assets (2 figures)
