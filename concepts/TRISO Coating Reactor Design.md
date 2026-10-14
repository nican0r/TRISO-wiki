---
type: concept
title: TRISO Coating Reactor Design
status: draft
sources: 7
tags: [triso, cvd, spouted-bed, fabrication, reactor-design, fluidization, gas-distributor, conflict]
updated: 2026-10-11
---

# TRISO Coating Reactor Design

**In one line** — All four TRISO layers are deposited in one spouted-bed CVD reactor whose retort diameter, gas-injection geometry and converging-section profile are constrained as much by nuclear criticality safety and by a fabrication defect (soot inclusion) as by coating chemistry.

## Mechanism

The reactor is a spouted bed: kernels are lifted by a central gas jet, fall back through an annular descending bed, and are coated in flight and in the bed by CVD (chemical vapor deposition) gases decomposing at 1230–1550 °C ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.2). Retort internal diameter is fixed by nuclear criticality safety rather than by process optimisation: the design discussed is licensed for HEU (highly-enriched uranium) and held to 15.2 cm so the geometry alone stays critically safe if HEU were used inadvertently, against LEU (low-enriched uranium) equipment elsewhere running retorts up to 24 cm (p.4).

At the particle sizes and process temperatures involved, the whole deposition falls **outside** the standard mapped region for spouted beds on a dimensionless particle-diameter vs. dimensionless gas-velocity chart (the Grace/Kunii classification). Stable, coherent spouting is not achieved; the bed instead fluidizes in a pulsatory spouted-bed mode, confirmed by pressure-fluctuation sensing and CPFD Barracuda VR® simulation (p.6).

The coating problem differs from ordinary fluidised beds in three ways: depositing solids plug small orifices, dense kernels (10.8 g/cm³) do not fluidise over a conventional perforated plate, and the bed must capture the depositing species efficiently enough to give uniform layers ([[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] p.2).

## Equipment that grew out of two fabrication defects

The redesigns below are documented as direct fixes for observed defects — nozzle accretion and soot inclusion — not generic improvements:

- **Gas distributor nozzle.** A single gas orifice in an early 5 cm lab-scale coater formed volcano-shaped accretions that trapped particles between the accretion and the retort wall. It was replaced with a domed, multi-orifice nozzle with a serrated flange, sized to prevent particle weeping and gas-flow reversal at individual orifices ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] pp.6–7). The general rule for grid plates is a per-orifice pressure drop of at least ⅓ of the bed's, and never below 2,500 Pa ([[Introduction to Fluidization|Cocco et al. 2014]] p.5); whether it carries over to a spouted-bed nozzle is not established — see [[Fluidization#Distributors]]. A secondary account of the INL (Idaho National Laboratory) trials names four candidate geometries — original, concave, dome, hemisphere — with the dome selected on product variance and accretion, and bed stagnation reduced by reducing nozzle radius and orifice angles ([[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] pp.3–4).
- **Converging section.** Standard spouted-bed converging sections use a single conical angle (45–60°); a narrow angle risks lifting the whole bed and slugging, a wide angle stabilises the spout but impairs bed circulation. The reference design instead uses a curvilinear profile of continuously variable slope — 22° at the cylindrical junction, ~116° at the base (p.7–8).
- **Dual gas paths.** Part of the inert diluent gas is routed through an annular orifice beneath the nozzle rather than through the nozzle itself, which widens the spout and lowers the fountain height (p.9).

## Gas distributor — a second, independent solution

INET (Institute of Nuclear and New Energy Technology, Tsinghua) compared four inlets — traditional single-nozzle, modified single-nozzle, multi-nozzle, and multi-ring inclined holes — by 3-D Euler–Euler CFD (computational fluid dynamics), and selected the **multi-ring inclined-hole** inlet for the most uniform fluidisation at the bed bottom, then validated it experimentally ([[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] p.4). INL arrived at a domed multi-orifice nozzle by a different route (above). Both abandon the single central orifice; neither source quantifies the improvement.

![[fbcvd-p04-fig05-inet-gas-distributors.jpeg]]
*INET inlet designs; (d) was selected — [[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] p.4.*

## Axial heating profile — keeping deposition off the nozzle

INET thins the central heating element over part of its length so the hot zone sits a set height above the nozzle and the nozzle runs cooler. Deposition concentrates in the hot region, and nozzle accretion falls "significantly" (unquantified); heat loss also drops ([[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] p.3). Read from the source's Fig. 3, the hot zone lies roughly 30–60 cm above the nozzle, and at a 1600 °C setpoint the nozzle level is roughly 300 °C cooler. The source notes the gradient is smaller once the bed is fluidised and mixed (p.3), and does not say what conditions the plotted profiles were measured under.

![[fbcvd-p03-fig03-vertical-temperature-profile.jpeg]]
*Axial temperature at 1200, 1400, 1600 °C setpoints; dashed lines bound the hot zone — [[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] p.3.*

## Flat-slug circulation — a second fabrication-stage defect route

A "flat" slug forming above the gas inlet impairs bed circulation and is said to produce non-spherical particles, coating flaws and missing coating layers ([[Advancing the Fundamental Understanding and Scale-up of TRISO Fuel Coaters via Advanced Measurement and Computational Techniques|Biswas & Al-Dahhan 2012]] pp.7, 123; stated without citation, single-source). The stable-spouting window that avoids slugging is narrow in cold flow — see [[Spouted Bed Hydrodynamics#Regimes]].

## Soot inclusion — a fabrication-stage defect

Carbonaceous soot generated during buffer (carbon) layer deposition accumulates above the bed fountain and on the cylindrical retort wall; ejecta from the bed occasionally carries a loosely adherent soot layer back in (the general mechanism — bursting bubbles throwing particles into the freeboard — is on [[Fluidization#Entrainment]]), where it becomes encapsulated within the coating layer being deposited. It is frequently observed in particles from a 5 cm lab-scale coater with a single gas inlet at the cone apex, and infrequently observed in the 15 cm production coater once the multi-orifice nozzle, curvilinear converging section and dual gas paths above are combined ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.8–9).

This is a distinct failure route from the eleven service mechanisms on [[TRISO Fuel Failure Mechanisms]] — those describe how a correctly built particle degrades in reactor; soot inclusion is a particle built with a flaw already in it, the kind of as-manufactured defect that page and [[Fuel Quality Control and Characterization]] both point to as the dominant real-world release driver.

## Bed growth through the coating sequence

| Stage | Particle diameter (µm) | Particle density (g/cm³) |
|---|---|---|
| Kernel | 425 | 11.1 |
| + Buffer | 625 | 4.18 |
| + IPyC | 705 | 3.49 |
| + SiC | 775 | 3.42 |
| + OPyC | 855 | 3.03 |

Nominal, 425 µm kernel ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.5). Mean particle diameter roughly doubles, bed volume grows ~8-fold, and envelope density falls from 11 to 3 g/cm³ (p.2) — too fast for the bed to reach steady state at any point in the run (p.4). SiC takes about 100 of the ~130 total minutes (p.5). Per-layer thickness, density, time and temperature across three lines: [[TRISO Coating Parameters]].

## Process control without seeing inside the bed

No sight ports, internal thermocouples or optical pyrometers are used: a hanging thermocouple's radial position can't be controlled or maintained, the radial temperature profile makes any single internal reading unreliable, and opaque black smoke from pyrocarbon deposition blocks optical access. Temperature is held by external, wall-offset thermocouples and gas-flow parameters alone, and the result is checked only after the run — by metallographic cross-section and, for defect fraction, by burn-leach ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.5). See [[Fuel Quality Control and Characterization]] for what that post-run measurement covers.

A review of 16 coater studies gives outer-wall measurement as the usual practice, because an internal thermocouple both disturbs the gas flow and gets coated ([[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] p.3). It also names differing temperature measurement as one likely reason SiC deposited at nominally the same temperature varies in density between coaters (p.12).

INET's coater schematic shows an infrared pyrometer on the furnace ([[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] p.2, Fig. 1); whether it views the bed or the wall is not stated. Different practice on a different line — not reconciled.

ORNL's (Oak Ridge National Laboratory) development coater does look inside: a handheld optical pyrometer reads the bed through a sight glass and prism in the furnace top, with the measured attenuation of the glass and prism corrected for ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] p.5). This is the practice [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.5 rules out because of pyrocarbon smoke; the ORNL report does not mention smoke. The furnace is a conical graphite chamber inside a resistively heated graphite element, fed through a water-cooled injector; kernels load from the top under argon and drain through the injector after cool-down (p.4). It is the only line in the wiki whose stated temperatures are bed temperatures — see [[TRISO Coating Parameters#Conflicts]].

![[ornl-surrogate-p04-fig01-fbcvd-furnace.jpeg]]
*ORNL FBCVD furnace, sight glass at top. Jolly et al. 2016 p.4, Fig. 1.*

Bed pressure drop needs no internal access and is described as one of the most easily obtained signals on hot coaters; ORNL-linked work was comparing hot-coater ΔP signals with cold-mockup results to infer coater state ([[Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating|Zhou et al. 2005]] p.2). Its mean and spectrum track the spouting regime in cold flow — see [[Spouted Bed Hydrodynamics#Measurement]].

## Scale-up is not linear

At constant linear deposition rate, gas flow scales with bed mass (∝ retort diameter³) while superficial gas velocity scales with the retort's cross-sectional area (∝ diameter), so gas residence time falls as the retort gets larger — and the wall-surface-area-to-gas-flow ratio driving external temperature control falls with it. Laboratory-scale temperature setpoints are stated to be inaccurate at larger diameters as a direct result, requiring re-optimisation at each production scale rather than simple extrapolation ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] pp.4, 6). Cold-flow work shows why matched dimensionless groups are not enough: between a 0.152 m and a 0.076 m bed they reproduced spout diameter and fountain height but left spout holdup and particle velocity 15–46 % apart; matching the radial gas-holdup profile is proposed instead ([[Advancing the Fundamental Understanding and Scale-up of TRISO Fuel Coaters via Advanced Measurement and Computational Techniques|Biswas & Al-Dahhan 2012]] pp.33–51; soft). Detail: [[Spouted Bed Hydrodynamics#Scale-up]].

## Coater size and batch charge

Research coaters are bespoke, with no standard design. The review therefore identifies them by internal diameter, from 2.4 to 15.24 cm; cone angle matters too but is seldom reported ([[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] pp.4–5). Batch sizes run from 20 g in lab coaters to 3 kg in industrial ones (p.2). Coating efficiency rises with charge, because a small charge does not fill the reaction zone: 41 % at 10 g to 97 % at 200 g in a 3.81 cm coater (p.16, citing Gulden 1968). Efficiency also rises with coater size (p.16). A bigger charge lowers the SiC deposition rate in µm/min (p.15). Compiled results: [[SiC Layer Deposition]], [[TRISO Coating Parameters]].

The review classifies kernels as Geldart Group D (large, dense) particles, which expand poorly as a bed. This is why conical spouted beds are used instead of flat-grid fluidised beds (pp.2–3). The general classification agrees: Group D needs large gas flows and slugs, and is often spouted because spouting needs less gas ([[Introduction to Fluidization|Cocco et al. 2014]] p.4). Every kernel and coated particle in the wiki plots in Group D on the ambient-condition Geldart chart — see [[Fluidization#Geldart classification]] (`#inferred`). The review calls stable spouting the preferred regime (p.2, citing Marshall 2017), whereas [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.6 reports that the INL coater does not achieve it and runs in a pulsatory mode. The two statements are compatible — one is about which regime is preferred, the other about what one coater achieves.

## Contested / uncertain

> [!warning] Conflict — predicted peak accident fuel temperature
> [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] states peak centerline core temperatures during postulated accidents "safely remain 200–300 °C below fuel fabrication temperatures" (p.3); fabrication runs up to 1550 °C (p.2), implying a predicted peak near 1250–1350 °C. [[Passive Decay Heat Removal]] gives a peak of 1620 °C for a depressurised loss-of-forced-circulation event in modern small HTRs ([[Ch 01 — Introduction]] p.18, [[Ch 09 — Accident Testing]] p.78). The two sources do not name the same reactor design or accident scenario, and this source gives no scenario detail to reconcile them.
> `#conflict`

> [!warning] Conflict — SiC deposition temperature
> ~1600 °C at INET ([[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] pp.2, 5) against a 1550 °C whole-process maximum here ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.2) and 1500 °C in [[Ch 02 — Manufacture of TRISO Coated Particles]] (p.33). None of those three says where the temperature is measured, which matters given the axial gradient above. ORNL, measuring in the bed, deposits SiC at 1425 °C in 1:1 Ar–H₂ ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] p.5). Details on [[TRISO Coating Parameters]].
> `#conflict`

## Sources

- [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]]
- [[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]]
- [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production]]
- [[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels]]
- [[Introduction to Fluidization]] · theory: [[Fluidization]]
- [[Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating]]
- [[Advancing the Fundamental Understanding and Scale-up of TRISO Fuel Coaters via Advanced Measurement and Computational Techniques]] · [[Spouted Bed Hydrodynamics]]
- Data: [[TRISO Coating Parameters]]
