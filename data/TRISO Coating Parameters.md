---
type: data
title: TRISO Coating Parameters
status: draft
tags: [triso, cvd, fabrication, pyc, sic, conflict, inferred]
sources: 7
updated: 2026-10-14
---

# TRISO Coating Parameters

Per-layer coating conditions for the four TRISO layers, from four coating lines, plus experimental SiC conditions from 16 coater studies. Process context: [[TRISO Coating Process]]; SiC parameter–property map: [[SiC Layer Deposition]]; PyC parameter–property map: [[PyC Layer Deposition]]; equipment: [[TRISO Coating Reactor Design]]; layer functions: [[TRISO Particle Architecture]].

## How the sources' conditions differ

| Key | Source | Line / basis | Kernel |
|---|---|---|---|
| **IAEA** | [[Ch 02 — Manufacture of TRISO Coated Particles]] | Generic process table (Table 2, p.33); thicknesses are the German LEU (low-enriched uranium) UO₂ reference design (p.34) | 500 µm UO₂ (p.28) |
| **INL** | [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] | Nominal values for the US AGR (Advanced Gas Reactor) fuel programme coater, 15.2 cm HEU (highly-enriched uranium)-licensed retort (pp.4–5) | 425 µm, 11.1 g/cm³ (p.5) |
| **INET** | [[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] | Experimental parameters, Tsinghua INET (Institute of Nuclear and New Energy Technology) automated line, 3 kg UO₂ batches (p.4) | 500 µm UO₂, 10.8 g/cm³ (p.2) |
| **ORNL** | [[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] | Final batch ZrX800-30T after 29 development runs, Oak Ridge; bed temperature by optical pyrometer (pp.3, 5) | 814 µm ZrO₂ surrogate, 6.0 g/cm³ (pp.3, 7) |

IAEA, INL and INET give single nominal values with no tolerances; INET's are approximate ("~"). ORNL gives measured batch means against the AGR-1 (US Advanced Gas Reactor programme) specification tolerances, and is the only line that states gas flows — [[#Gas flows (ORNL)]]. The ranges in [[#SiC across coaters]] come from a review, not from any of these three lines.

## Parameters

| Layer | Source | Thickness (µm) | Density (g/cm³) | Time (min) | Temp. (°C) | Reactant + carrier | Rate (µm/min) | Page |
|---|---|---|---|---|---|---|---|---|
| Buffer | IAEA | 95 | — | — | 1250 | C₂H₂ + Ar | 10 | pp.33–34 |
| | INL | 100 | 1.00 | 5 | — | — | — | p.5 |
| | INET | 95 | 0.9 | ~2.5 | ~1260 | C₂H₂ + Ar | — | p.5 |
| | ORNL | 98.7 | 1.01† | 1.15 | 1425 | C₂H₂ + Ar | — | pp.5, 8 |
| IPyC (inner pyrocarbon) | IAEA | 40 | — | — | 1300 | C₂H₂ + C₃H₆ + Ar | 5 | pp.33–34 |
| | INL | 40 | 1.90 | 12 | — | — | — | p.5 |
| | INET | 40 | 1.9 | ~12.5 | ~1280 | C₃H₆ + Ar | — | p.5 |
| | ORNL | 41.3 | not measured | 8.6 | 1265 | C₂H₂ + C₃H₆ + Ar | — | pp.5, 8 |
| SiC | IAEA | 35 | — | — | 1500 | CH₃SiCl₃ + H₂ | 0.2 | pp.33–34 |
| | INL | 35 | 3.20 | 100 | — | — | — | p.5 |
| | INET | 35 | 3.2 | ~150 | ~1600 | CH₃SiCl₃ (MTS) + H₂ | — | p.5 |
| | ORNL | 32.9 | 3.1983 | 123.87 | 1425 | MTS + H₂ + Ar (1:1) | — | pp.5, 8 |
| OPyC (outer pyrocarbon) | IAEA | 40 | — | — | 1300 | C₂H₂ + C₃H₆ + Ar | 5 | pp.33–34 |
| | INL | 40 | 1.90 | 13 | — | — | — | p.5 |
| | INET | 40 | 1.9 | ~12.0 | ~1300 | C₃H₆ + Ar | — | p.5 |
| | ORNL | 43.1 | 1.8937 | 7.6 | 1290 | C₂H₂ + C₃H₆ + Ar | — | pp.5, 8 |

ORNL values are measured batch means, not targets. † From buffer-only run ZrX800-11B under the same buffer conditions; buffer density cannot be measured once IPyC covers it (p.7).

Buffer density is given as ~1.1 g/cm³, about half that of dense PyC, by [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] p.2 — a third value alongside INL's 1.00 and INET's 0.9. INL gives no per-layer temperatures, only the whole-sequence envelope 1230–1550 °C (p.2). IAEA also records IPyC and OPyC deposited from propylene alone (p.31), so INET's propylene-only dense PyC is a recognised variant, not a disagreement. The SiC acceptance criterion is density > 3.19 Mg/m³ ([[Ch 02 — Manufacture of TRISO Coated Particles]] p.34); both nominal values sit at 3.2.

## Gas flows (ORNL)

Batch ZrX800-30T, sccm ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] p.5, Table 2). CGF (coating gas fraction) = precursor flow ÷ total flow; CGR (coating gas ratio) = C₃H₆ ÷ C₂H₂.

| Layer | Ar | H₂ | C₂H₂ | C₃H₆ | MTS | Total | CGF | CGR |
|---|---|---|---|---|---|---|---|---|
| Buffer | 4,620 | — | 6,380 | — | — | 11,000 | 0.58 | — |
| IPyC | 10,625 | — | 1,014 | 861 | — | 12,500 | 0.15 | 0.85 |
| SiC | 7,500 | 7,500 | — | — | 71 | 15,071 | 0.0047 | — |
| OPyC | 14,025 | — | 1,338 | 1,137 | — | 16,500 | 0.15 | 0.85 |

Derived for SiC: Ar:(Ar+H₂) = 50 %, H₂/MTS ≈ 106. Temperature and diluent match the AGR-1 "V3" variant in [[#SiC across coaters]] (1425 °C, Ar–H₂ 1:1), but the MTS fraction is about a quarter of V3's 1.92–2.01 %. OPyC is run 25 °C hotter than IPyC; AGR-1 work found the two densities within 0.0052 g/cm³ under that offset (p.7). Coater diameter and charge mass are not given, so flows cannot be normalised to bed area.

## AGR-1 specification tolerances

As applied to the ORNL batch ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] p.8, citing the AGR-1 product specification).

| Property | Buffer | IPyC | SiC | OPyC |
|---|---|---|---|---|
| Thickness (µm) | 90 ± 15 (ORNL; AGR-1 target 100) | 40 ± 4 | 35 ± 3 | 40 ± 4 |
| Density (g/cm³) | 1.03 ± 0.15 | 1.90 ± 0.05 | ≥ 3.19 | 1.90 ± 0.05 |
| Anisotropy (BAFo) | — | ≤ 1.035 | — | ≤ 1.035 |

## Derived deposition rates

> [!info] Inferred — rates from thickness ÷ time
> Derived here from the table above; INL, INET and ORNL state no rate.
>
> | Layer | IAEA (stated) | INL (derived) | INET (derived) | ORNL (derived) |
> |---|---|---|---|---|
> | Buffer | 10 | 20 | ~38 | 86 |
> | IPyC | 5 | 3.3 | ~3.2 | 4.8 |
> | SiC | 0.2 | 0.35 | ~0.23 | 0.27 |
> | OPyC | 5 | 3.1 | ~3.3 | 5.7 |
>
> µm/min. Assumes the stated time is pure deposition time at constant rate; if it includes gas switching or ramps, derived rates are underestimates. Dense PyC agrees between INL and INET to within 5 %; ORNL's runs 45–85 % faster, at CGF 0.15. The buffer and SiC disagree across all lines. Confirmation would need a source stating rate directly, or gas concentration and flow per layer.
> `#inferred`

## IPyC conditions from a two-factor study

[[Effects of Deposition Conditions on the Properties of Pyrolytic Carbon Deposited in a Fluidized Bed|Lowden et al. 2005]] varied only IPyC temperature and coating gas fraction on one coater, with all gas flows stated (ORNL 2-inch, 346–347 µm NUCO kernels, 62.25 g charge, propylene/acetylene 0.85, 8,500 sccm total):

| T (°C) | CGF | Rate (µm/min) | Density (g/cm³) | Diattenuation N | Open porosity (ml/m²) |
|---|---|---|---|---|---|
| 1170 | 0.30 | 2.3 | 1.978 | 0.0099 | 0.71 |
| 1225 | 0.30 | 2.6 | 1.962 | 0.0078 | 1.10 |
| 1250 | 0.30 | 2.9 | 1.909 | 0.0048 | 1.32 |
| 1275 | 0.30 | 3.2 | 1.829 | 0.0038 | — |
| 1300 | 0.30 | 2.9 | 1.831 | 0.0052 | — |
| 1325 | 0.30 | 3.5 | 1.773 | 0.0040 | — |
| 1275 | 0.15 | 1.5 | 1.813 | 0.0075 | 0.83 |
| 1275 | 0.45 | 4.7 | 1.873 | 0.0050 | 1.85 |

Lowden et al. 2005 p.34; full 17-run table on the source page. Note the direction: **density falls as temperature rises**, so the 1.90 g/cm³ specification pins IPyC deposition near 1265 °C bed ([[FY 2008 Six-Inch Diameter Coater Test Report|Barnes and Marshall 2008]] p.21).

## SiC across coaters

Experimental ranges, not nominal recipes. Condensed from Table 1 of [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] pp.5–6, which compiles the underlying studies (the "Study" column). Coaters are identified by internal diameter. "—" means not given.

| Study | Diameter (cm) | Charge | Diluent | Temp. (°C) | Dilution ratio | Total flow |
|---|---|---|---|---|---|---|
| Gulden 1968 | 2.5 | 25 g UC₂; 20–1000 g batch study | H₂ | 1200–1800 | — | — |
| Voice and Lamb 1969 | 5.5 | 150–400 g | H₂ | 1250–1750 | H₂/MTS 4–49 | — |
| Thomas 1972 | 7.62 | 1000 g UO₂ | H₂ | 1300–1750 | H₂/MTS 11.5–49 | — |
| Gyarmati and Nickel 1972 | 5.5; 7.2 | — | H₂; Ar–H₂; Ar | 1400–1700 | H₂/MTS 49–99 | ~11 L/min |
| Federer 1977a | 3.49; 4.45; 6.35 | 34–479 g | H₂ | 1225–1775 | H₂/MTS 5–45 | 2.4–44.5 L/min |
| Stinton and Lackey 1977 | 13 | — | H₂ | 1405–1785 | H₂/MTS 11–79 | — |
| Lauf et al. 1979 | 2.5 | 0.5 g + 13.9 g | H₂ | 1500–1700 | H₂/MTS 75–90 | — |
| Minato and Fukuda 1987–88 | 2.4 | 8 g | H₂; Ar–H₂; Ar | 1150–1700 | H₂/MTS 239–1028 | 2.5–9.4 L/min |
| Xu et al. 1995 | 5.08 | 80 g | Ar–H₂ | 1450–1650 | (Ar+H₂)/MTS 99 | 500 L/h |
| Hunn and Lowden 2006; Barnes and Marshall 2008 | 5.08 | 1250–1750 g UCO | H₂ (baseline, V1, V2) | 1500 | MTS/(H₂+MTS) 1.11–1.23 % | ~16.9 slm |
| | 5.08 | | Ar–H₂ 1:1 (V3) | 1425 | MTS/total 1.92–2.01 % | ~10.6 slm |
| | 15.24 | | H₂; Ar–H₂ | 1600 (H₂); 1348–1599 (Ar–H₂, 20–35.5 % Ar) | H₂/MTS 36–86 | — |
| López-Honorato 2008 | 3.5 | 30 g Al₂O₃ | H₂ | 1250–1500 | H₂/MTS 10–277 | 5–13 L/min |
| Kim et al. 2009 | 2.5 | ZrO₂ | Ar–H₂ | 1400–1600 | (Ar+H₂)/MTS 100 | — |
| Hancke et al. 2012 | 12 | 750 g UO₂ | H₂ | 1460–1560 | H₂/MTS 53–104 | 75–105 L/min |
| Cromarty 2012 | 5 | 20–60 g ZrO₂ | H₂ | 1200–1500 | H₂/MTS 39–199 | — |
| Liu et al. 2016 | 5 | 20 g ZrO₂ | Ar–H₂ (0–100 % Ar) | 1200–1650 | — | H₂ 10–17.5 slm |
| Yang et al. 2019a | — | ZrO₂ | Ar–H₂ | 1200–1600 | — | — |

Five of the 16 coated uranium compounds; the rest used surrogates (ZrO₂, Al₂O₃, PyC-coated microspheres) or did not state the kernel material (pp.5–6). The dilution ratio is reported in four different forms, so the column is not comparable across rows; the review makes the same point (p.17). Parameter effects: [[SiC Layer Deposition]].

## Conflicts

> [!info] Resolved by measurement position — SiC deposition temperature
> The four nominal SiC temperatures in this wiki are not four processes. [[FY 2008 Six-Inch Diameter Coater Test Report|Barnes and Marshall 2008]] states the offset directly: a **control-thermocouple setpoint of 1600 °C corresponds to a bed temperature of 1430–1500 °C**, and the AGR-2 variant's control 1550 °C to an estimated bed 1430–1450 °C (pp.7, 26). On that scale, 1500 °C ([[Ch 02 — Manufacture of TRISO Coated Particles]] p.33), ≤ 1550 °C ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.2) and ~1600 °C ([[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] pp.2, 5) are consistent with a bed at roughly 1430–1500 °C, which is where ORNL's bed-measured 1425 °C ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] p.5) already sat. Optical measurement carries its own offset: ORNL shifted its reported temperatures by 25 °C after calibrating the sight glass and prism ([[Effects of Deposition Conditions on the Properties of Pyrolytic Carbon Deposited in a Fluidized Bed|Lowden et al. 2005]] p.6).
>
> What remains open is per-line, not global: no source states where the IAEA generic or INET figures are measured, so each line's offset is unknown rather than wrong. Retagged from `#conflict` to `#inferred` — this was a comparison of unlike measurements, not a disagreement between sources. Confirmation would need each line's thermocouple position or a bed calibration. Practice across lines: [[Coater Process Monitoring]].
> `#inferred`

> [!info] Resolved — INL SiC temperature
> [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] Table 1 lists the INL 15.24 cm coater at 1600 °C in H₂–MTS (p.5), against a 1550 °C whole-process maximum in [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.2. The primary source for that coater is now in the wiki: 1600 °C is its **control setpoint**, corresponding to a bed temperature of 1430–1500 °C ([[FY 2008 Six-Inch Diameter Coater Test Report|Barnes and Marshall 2008]] p.26). The two figures are a setpoint and a process limit on different scales, not a disagreement.
> `#inferred`

> [!warning] Conflict — buffer deposition time and rate
> For a buffer of near-identical thickness, INET gives ~2.5 min for 95 µm (p.5), INL 5 min for 100 µm (p.5), and IAEA a rate of 10 µm/min (p.33), which would take ~9.5 min. ORNL deposits 98.7 µm in 1.15 min, at 1425 °C and CGF 0.58 ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] pp.5, 8) — where IAEA and INET give ~1250–1260 °C. Spread ≈ 9× in rate. Density does not track rate: the fastest buffer (ORNL, 1.01 g/cm³, from a proxy run) is denser than INET's (0.9). No source links rate, temperature and density. Unresolved.
> `#conflict`

> [!warning] Conflict — buffer deposition temperature
> The US lines coat the buffer hot: 1450 °C bed in the AGR-1 2-inch coater and 1390–1540 °C bed across a single 4–7 minute deposition in the 6-inch coater ([[FY 2008 Six-Inch Diameter Coater Test Report|Barnes and Marshall 2008]] p.19), with ORNL at 1425 °C. The IAEA generic and INET lines give 1250–1260 °C. Unlike the SiC case above this is not a measurement-position artefact — the US figures are bed temperatures — and both routes meet their buffer density specifications. Unresolved. See [[PyC Layer Deposition]].
> `#conflict`

## Sources
- [[Ch 02 — Manufacture of TRISO Coated Particles]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
- [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]]
- [[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]]
- [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production]]
- [[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels]]