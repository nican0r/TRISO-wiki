---
type: concept
title: SiC Layer Deposition
status: draft
sources: 6
tags: [triso, sic, cvd, mts, stoichiometry, microstructure, density, conflict, inferred]
updated: 2026-10-14
---

# SiC Layer Deposition

**In one line** — The TRISO SiC layer is grown by decomposing MTS (methyltrichlorosilane, CH₃SiCl₃) in a hydrogen-carrying fluidised bed. Deposition temperature is the one parameter known to control its stoichiometry, density and grain structure, and the other parameters are not reliably mapped.

Where SiC sits in the particle: [[TRISO Particle Architecture]]. Where it sits in the coating sequence: [[TRISO Coating Process]]. Nominal recipes and coater-by-coater conditions: [[TRISO Coating Parameters]]. Short form of the main source below: Hu et al. 2025 = [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production]].

## Chemistry

Overall: $\text{CH}_3\text{SiCl}_3(g) \rightarrow \text{SiC}(s) + 3\text{HCl}(g)$ (Hu et al. 2025 p.6; [[Ch 02 — Manufacture of TRISO Coated Particles]] p.31). MTS is the preferred precursor for its 1:1 Si:C ratio, availability, boiling point and stability (Hu et al. 2025 p.4). The weakest bond is C–Si at 290 kJ·mol⁻¹, against 338 for C–H and 359 for Si–Cl. MTS therefore splits first into a methyl radical and a chlorosilyl radical, which then deposit carbon and silicon by separate routes (p.6). Most SiC forms this indirect way, through intermediate species, rather than by MTS reacting directly on the surface (p.6).

Because the two routes run at different rates, Si and C can deposit out of balance. The hydrogen diluent speeds the Si-bearing route and slows the carbon route (p.9):

- low temperature and/or a high H₂ fraction gives free Si;
- H₂ starvation, or argon replacing H₂, gives free C (p.8).

The HCl released is why the IPyC (inner pyrocarbon) layer beneath the SiC doubles as a chlorine barrier ([[Ch 01 — Introduction]] p.22).

## Temperature sets the outcome

| Property | Behaviour with deposition temperature | Page (Hu et al. 2025) |
|---|---|---|
| Phase | β-SiC (cubic) below 1700 °C; α-SiC (hexagonal) above. Single-phase β between 1300 and 1700 °C in most studies | p.8 |
| Stoichiometry, H₂ diluent | Stoichiometric at 1500–1600 °C; free Si below, free C above | p.8 |
| Density | Peaks at 1500–1600 °C and falls above it; excess Si is the main cause of low density below it | p.12 |
| Cross-section | Striated fine grains at low temperature → crystal bands → micron-scale grains above 1500 °C | pp.9, 17 |
| Surface | Botryoidal ("cauliflower") at 1200 °C → faceted or dendritic by 1700 °C; porous polygonal surface above 1600 °C | p.9 |
| Coating efficiency | Generally rises with temperature; two datasets peak near 1500–1550 °C and then fall | p.16 |

On flat substrates the preferred crystal orientation switches from ⟨111⟩ at 1400 °C or below to ⟨220⟩ at 1500 °C or above. This is about the same temperature as the switch from Si-rich to C-rich deposits. Neither transition has been measured on fluidised spheres (p.9).

![[sic-review-p09-fig11-phase-diagram.jpeg]]
*Adding argon lowers the stoichiometric band, to ~1200 °C at 90 % Ar. From Liu et al. 2016, via Hu et al. 2025 p.9, Fig. 11.*

A bed-measured production condition inside the argon-shifted band: ORNL (Oak Ridge National Laboratory) deposits SiC at 1425 °C in 1:1 Ar–H₂ with MTS at 0.47 % of total flow (H₂/MTS ≈ 106, derived), temperature read by optical pyrometer in the bed. It reached 3.1983 g/cm³ and passed the AGR-1 (US Advanced Gas Reactor programme) grain-size standard ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] pp.5, 8–10). Fig. 11 marks a 1430 °C, 50 % Ar point stoichiometric (read off the plot); ORNL did not measure stoichiometry. Its outer SiC surface was rougher than on AGR-1 particles — a property no specification covers (p.9). Full recipe: [[TRISO Coating Parameters#Gas flows (ORNL)]].

## MTS concentration is limited by density

At a 1600 °C control setpoint in hydrogen alone, SiC density falls as MTS concentration rises and drops below the 3.19 g/cm³ specification above about **2.0 mol% MTS** ([[FY 2008 Six-Inch Diameter Coater Test Report|Barnes and Marshall 2008]] p.26). Adding 20–30 % argon holds density above specification at 2.78–3.17 % MTS and a 1550 °C setpoint — the trade that produced the AGR-2 variant condition. The throughput gain is smaller than it looks: coating time fell only ~10 %, because total gas flow was cut ~36 % to keep the bed fluidising the same way (p.26).

![[bw-coater-p27-fig08-sic-density-vs-mts.jpeg]]
*SiC density vs MTS concentration, hydrogen-only against argon-diluted runs — Barnes and Marshall 2008 p.27.*

Defect fraction does not follow the same levers: across 26 batches it varied from <0.2 to 67 per 50,000 particles with no correlation to any coating parameter measured, while thicker SiC layers passed more often — 13 of 15 batches at ≥ 34.5 µm against 2 of 10 below it (p.27).

## Finer grain, measured in reactor

Argon dilution gives finer grain ([[TRISO Coating Parameters]]), and AGR-1's Variant 3 used it. Its compact released one to two orders of magnitude less Sr, Ce, Sm and Eu than the Baseline compact, which [[PIE on Five Irradiated AGR-1 Compacts|Hunn et al. 2012]] attributes tentatively to smaller grains and more localised trapping defects; the process became the baseline for AGR-2 and beyond (pp.8, 25). One compact per lot — see [[AGR-1 Coating Variants]] for what that supports, and [[Silver Release]] for why silver is the exception.

## What is not settled

- **H₂/MTS ratio.** One study found free carbon eliminated above a ratio of 30. Another found MTS and H₂ flux had negligible effect on Si content (p.9). Individual studies report a link between the ratio and density, but the compiled data show none (p.12, Fig. 19). Grain size is finer at very low (< 10) or very high (> 199) ratios than at 60–80 (p.9). The review's own diagnosis: the ratio is an indirect variable, and without MTS flux and total flow reported alongside it, datasets cannot be compared (p.17).
- **Gas flow and fluidisation regime.** Both are rarely reported. Only one coater's flow-rate series is available, and it shows no clear trend (p.10). How the bed moves matters: particles coated while stationary came out porous and of poor quality under otherwise similar settings (p.9).
- **Grain size.** Fine grains are the acceptance criterion ([[Ch 02 — Manufacture of TRISO Coated Particles]] p.34); irradiation evidence now favours them for most species but not for silver ([[AGR-1 Coating Variants]], [[Silver Release]]).

## Rate and throughput

Deposition rate rises linearly with MTS flux on all four coaters where it has been reported, with gradients of 3.5–4.5 µm/min per cm³·min⁻¹·cm⁻² (Hu et al. 2025 p.15, Fig. 20). Larger kernel batches lower the rate in µm/min, and a multi-inlet "frit" distributor kept density high at a high rate (p.15). The review's conclusion is that 1500–1600 °C combined with a low MTS concentration gives the desired properties below the maximum possible rate. Industrial scale therefore needs a trade-off, not a pure rate maximum (p.14). At ~0.2–0.35 µm/min, SiC is already the slowest step in the sequence ([[TRISO Coating Parameters]]).

## Contested / uncertain

> [!warning] Conflict — density within the "optimum" window
> Hu et al. 2025 compile data in which SiC deposited at nominally 1550 °C ranges from 3.0 to 3.2 g/cm³, and high-density SiC appears below 1500 °C — e.g. Cromarty at 1400 °C (p.12). Candidate causes offered: unreported gas flows, distributor design and fluidisation mode; differing temperature measurement; and density methods (titration misreads open porosity near 1450 °C, pp.12–13). ORNL's 3.1983 g/cm³ at 1425 °C ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] p.8) is another high-density result below 1500 °C, though in 50 % Ar rather than H₂. Unresolved.
> `#conflict`

> [!info] Inferred — the three nominal SiC temperatures all sit inside the window
> The nominal SiC temperatures on [[TRISO Coating Parameters]] — 1500 °C (IAEA), ≤ 1550 °C (INL), ~1600 °C (INET) — all fall within the 1500–1600 °C stoichiometric window. Hu et al. 2025 note that temperature is normally measured on the furnace outer wall (p.3). Together these suggest the spread is at least partly a difference in where each line measures temperature, not a real difference in process. Confirmation would need each line's thermocouple position, or a bed-temperature calibration. A fourth line, ORNL at 1425 °C, sits below the window but measures in the bed and runs 50 % Ar; for it, argon rather than measurement position is the likelier explanation ([[TRISO Coating Parameters#Conflicts]]).
> `#inferred`

## Sources

- [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production]]
- [[Ch 02 — Manufacture of TRISO Coated Particles]] · [[Ch 01 — Introduction]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
- [[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels]]
- [[FY 2008 Six-Inch Diameter Coater Test Report]] · [[PIE on Five Irradiated AGR-1 Compacts]]
- Data: [[TRISO Coating Parameters]]
