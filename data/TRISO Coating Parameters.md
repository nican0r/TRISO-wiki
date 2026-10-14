---
type: data
title: TRISO Coating Parameters
status: draft
tags: [triso, cvd, fabrication, pyc, sic, conflict, inferred]
sources: 5
updated: 2026-09-23
---

# TRISO Coating Parameters

Per-layer coating conditions for the four TRISO layers, from four coating lines, plus experimental SiC conditions from 16 coater studies. Process context: [[TRISO Coating Process]]; SiC parameter–property map: [[SiC Layer Deposition]]; equipment: [[TRISO Coating Reactor Design]]; layer functions: [[TRISO Particle Architecture]].

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

> [!warning] Conflict — SiC deposition temperature
> [[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] gives ~1600 °C (pp.2, 5); [[Ch 02 — Manufacture of TRISO Coated Particles]] gives 1500 °C (p.33); [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] gives a whole-process maximum of 1550 °C (p.2). None states where the temperature is measured — setpoint, wall, or bed — and a furnace with a strong axial gradient ([[TRISO Coating Reactor Design]]) makes that difference material. A fourth line, ORNL, deposits SiC at 1425 °C, measured in the bed by optical pyrometer, in 1:1 Ar–H₂ ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] p.5). Unresolved.
> `#conflict`

> [!info] Inferred — all three sit inside the stoichiometric window
> All three values fall within the 1500–1600 °C window that [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] p.8 identifies as giving stoichiometric SiC in H₂. The same review notes that temperature is typically measured on the furnace outer wall (p.3), and it gives differing temperature measurement as one explanation for density scatter between studies (p.12). The disagreement may therefore be partly about where the temperature is measured, not the process itself. The values still differ, so the conflict above stays open. Confirmation would need each line's measurement position.
>
> ORNL's 1425 °C falls below the H₂ window but is the one bed-measured value, and is run in 50 % Ar. On the Ar–H₂ phase map (Hu et al. 2025 p.9, Fig. 11, citing Liu et al. 2016) a 1430 °C, 50 % Ar point is marked stoichiometric, near the band's upper edge (read off the plot; different coater). Argon, not measurement position, is the likelier explanation for this one. It met density ≥ 3.19 g/cm³ ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] p.8), consistent with that reading; stoichiometry was not measured.
> `#inferred`

> [!warning] Conflict — INL SiC temperature
> [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] Table 1 (p.5, citing Barnes and Marshall 2008) lists the INL 15.24 cm coater at 1600 °C in H₂–MTS. [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] gives 1550 °C as the maximum for the whole coating sequence on the same line (p.2). The 2008 figure may be a test condition rather than a production setpoint — the review does not say. Unresolved.
> `#conflict`

> [!warning] Conflict — buffer deposition time and rate
> For a buffer of near-identical thickness, INET gives ~2.5 min for 95 µm (p.5), INL 5 min for 100 µm (p.5), and IAEA a rate of 10 µm/min (p.33), which would take ~9.5 min. ORNL deposits 98.7 µm in 1.15 min, at 1425 °C and CGF 0.58 ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] pp.5, 8) — where IAEA and INET give ~1250–1260 °C. Spread ≈ 9× in rate. Density does not track rate: the fastest buffer (ORNL, 1.01 g/cm³, from a proxy run) is denser than INET's (0.9). No source links rate, temperature and density. Unresolved.
> `#conflict`

## Sources
- [[Ch 02 — Manufacture of TRISO Coated Particles]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
- [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]]
- [[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]]
- [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production]]
- [[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels]]
