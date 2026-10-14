---
type: concept
title: Coater Process Monitoring
status: draft
sources: 8
tags: [triso, cvd, process-control, instrumentation, pressure-fluctuations, temperature-measurement, conflict]
updated: 2026-10-14
---

# Coater Process Monitoring

**In one line** — What can be known about a TRISO coating run while it is running: a wall or bed temperature of uncertain provenance, a bed pressure signal that carries more information than it is used for, and little else — with every layer property measured only after the run, on destroyed samples.

Equipment: [[TRISO Coating Reactor Design]]. Post-run measurement: [[Fuel Quality Control and Characterization]]. Bed behaviour the signals reflect: [[Spouted Bed Hydrodynamics]]. Short forms: Barnes and Marshall 2008 = [[FY 2008 Six-Inch Diameter Coater Test Report]]; Zhou et al. 2005 = [[Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating]].

## Temperature: three different measurements called one name

| Practice | Line | Source |
|---|---|---|
| Outer-wall thermocouple, offset from the bed | usual practice across 16 compiled coater studies | [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] p.3 |
| Control thermocouple, bed inferred or unmeasured | B&W 6-inch | Barnes and Marshall 2008 pp.21, 26 |
| Internal thermocouple in the bed | B&W 6-inch until early 2008; AGR-1 2-inch | pp.19, 21 |
| Handheld optical pyrometer through sight glass and prism | ORNL development coater | [[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] p.5 |
| Infrared pyrometer on the furnace, target unstated | INET | [[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] p.2 |
| No internal thermocouple, sight port or optical pyrometry; external wall-offset thermocouples only | INL production coater | [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.5 |

The gap between the first two and the rest is quantified once: **control 1600 °C corresponds to a bed temperature of 1430–1500 °C** during SiC deposition, and the AGR-2 variant's control 1550 °C to an estimated bed 1430–1450 °C (Barnes and Marshall 2008 pp.7, 26). Optical measurement carries its own offset — ORNL shifted reported temperatures by 25 °C after calibrating the sight glass and prism ([[Effects of Deposition Conditions on the Properties of Pyrolytic Carbon Deposited in a Fluidized Bed|Lowden et al. 2005]] p.6). Consequences for the recipe comparison: [[TRISO Coating Parameters#Conflicts]].

Bed temperature is not steady within a layer either: 1390 → 1540 °C across a 4–7 minute buffer deposition at a fixed setpoint (p.19).

## Drift is detected after the fact

Thermocouple drift pushed two series of runs off the IPyC (inner pyrocarbon) density specification — 1.78–1.86 g/cm³ against a 1.90 target — and was recognised only when characterization data returned, after the runs were complete (Barnes and Marshall 2008 p.21). The fix adopted was to review furnace power output after each run as a drift indicator; "evaluate alternative methods of measuring bed temperature or means of detecting thermocouple drift" remains on the recommendation list (p.51).

## Bed pressure is the one live signal

Pressure fluctuations arise from bubbles and bed movement, so they encode gas and particle state. On the B&W coater they are recorded at **400 Hz for 8 s at three points in every layer** — one minute in, mid-deposition, one minute before gas shutoff (p.40).

What has been pulled out of them:

- **Bed growth**: volume triples during buffer deposition; the dominant frequency shifts downward and the signal becomes more regular as the layer builds (p.40).
- **Pyrocarbon anisotropy**: multivariate regressions on Hurst exponents over several lag intervals, their standard deviations, and inlet-pressure differences predict IPyC and OPyC (outer pyrocarbon) diattenuation (pp.45–46). The authors do not claim a mechanism — the link may be direct or through a shared dependence on process conditions.
- **Particle aspect ratio**: a similar regression on Hurst-exponent standard deviations (p.47).
- **A vessel effect**: after an argon-variant SiC layer, the OPyC pressure signature is persistently different, attributed to differently shaped nozzle accretions rather than to the particles (p.44).

In cold mockups the same signal carries regime information: mean bed ΔP has a minimum at the minimum spouting velocity, and the dominant frequency falls from 21.4 to 17.4 Hz as flow drops from 2.3 to 1.3 $U_{ms}$ before jumping to an annulus-vibration peak (Zhou et al. 2005 pp.5–6, 12). Bed ΔP is described there as among the most easily obtained signals on hot coaters (p.2). Gamma-ray densitometry is a third candidate, demonstrated cold at a single height ([[Advancing the Fundamental Understanding and Scale-up of TRISO Fuel Coaters via Advanced Measurement and Computational Techniques|Biswas & Al-Dahhan 2012]] pp.5, 20).

> [!warning] Conflict — do surrogate kernels stand in for fuel kernels?
> Pressure-fluctuation regressions had to be fitted separately for coated ZrO₂ surrogates and coated NUCO (natural-enrichment uranium oxycarbide), with some coefficients of opposite sign, despite nearly identical particle diameter and density; the causes offered are differing rotational inertia and thermal diffusivity (Barnes and Marshall 2008 p.46). Yet surrogates are the standard development vehicle ([[TRISO Coating Process]]), and most compiled SiC studies used them ([[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] pp.5–6). Chemistry may transfer where hydrodynamics does not; no source tests that separation.
> `#conflict`

## Hot sampling

Buffer and IPyC properties cannot be measured on a finished particle, so a sample cup is lowered into the bed mid-run and withdrawn. It was used in nine 2008 tests plus two AGR-2 runs; the design could not take both a buffer and an IPyC sample in one run, and the recommendation list asks for a sturdier cup and larger capacity (Barnes and Marshall 2008 pp.7, 19, 51). It is the only direct sample of an intermediate layer anywhere in the wiki.

## What is still not measurable in-run

Layer density, anisotropy, thickness, porosity and defect fraction — every acceptance property — are post-run and destructive ([[Fuel Quality Control and Characterization]]). The pressure correlations above are the only route proposed to any of them during a run, and they are regressions on one coater, not a validated instrument.

## Sources

- [[FY 2008 Six-Inch Diameter Coater Test Report]]
- [[Effects of Deposition Conditions on the Properties of Pyrolytic Carbon Deposited in a Fluidized Bed]]
- [[Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating]] · [[Advancing the Fundamental Understanding and Scale-up of TRISO Fuel Coaters via Advanced Measurement and Computational Techniques]]
- [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] · [[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] · [[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels]] · [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production]]
