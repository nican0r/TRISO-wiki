---
type: concept
title: TRISO Coating Process
status: draft
sources: 5
tags: [triso, cvd, fabrication, fluidised-bed, sic, pyc, surrogate, conflict, inferred]
updated: 2026-09-23
---

# TRISO Coating Process

**In one line** — All four TRISO layers are deposited by chemical vapour decomposition onto kernels suspended in a fluidised bed, in one uninterrupted sequence in a single reactor, with the deposition parameters — not the design — determining whether the resulting particle survives irradiation.

## Mechanism

Kernels are suspended by flowing gas in a heated fluidised bed reactor. Coating gases are chosen to decompose at temperatures up to 1600 °C and deposit constituents on the kernel surfaces; the layers are called pyrolytic because they form by heat-driven chemical decomposition. All four layers are applied sequentially without interruption in the same reactor ([[Ch 02 — Manufacture of TRISO Coated Particles]] pp.30, 33).

Buffer from C₂H₂ in argon at 1250 °C; IPyC (inner pyrocarbon) and OPyC (outer pyrocarbon) from C₂H₂ + C₃H₆ in argon at 1300 °C; SiC from CH₃SiCl₃ in hydrogen at 1500 °C (Table 2, [[Ch 02 — Manufacture of TRISO Coated Particles]] p.33). Per-layer temperatures, times, densities and rates from three sources, with their disagreements: [[TRISO Coating Parameters]]. Reactions: $\text{C}_2\text{H}_2 \rightarrow 2\text{C} + \text{H}_2$; $\text{C}_3\text{H}_6 \rightarrow 3\text{C} + 3\text{H}_2$; $\text{CH}_3\text{SiCl}_3 \rightarrow \text{SiC} + 3\text{HCl}$.

**SiC is the outlier on every axis**: 25–50× slower than the pyrocarbon layers (0.2 against 5–10 µm/min), 200 °C hotter, and under hydrogen rather than argon (p.33). It is the rate-limiting step of the sequence, and the HCl it liberates is the reason the IPyC layer beneath it doubles as a chlorine barrier ([[Ch 01 — Introduction]] p.22). How temperature, diluent and MTS supply set its stoichiometry, density and grain structure: [[SiC Layer Deposition]].

Two production lines give comparable recipes. The US line deposits all four layers in one batch sequence across 1230–1550 °C ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.2); the INET (Institute of Nuclear and New Energy Technology, Tsinghua) line runs PyC at ~1260–1300 °C and SiC at ~1600 °C ([[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] p.5). A development line at ORNL (Oak Ridge National Laboratory), coating ZrO₂ surrogates, runs IPyC/OPyC at 1265/1290 °C and both buffer and SiC at 1425 °C, the SiC in 1:1 Ar–H₂ rather than hydrogen alone ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] p.5); it is the only line with published gas flows. The SiC temperature is a four-way disagreement, flagged on [[TRISO Coating Parameters]]. Reactor engineering behind the recipe: [[TRISO Coating Reactor Design]].

## Why the parameters, not the recipe, decide the outcome

The source states it generally — "the conditions under which layer deposition takes place are very important as these deposition parameters determine the properties of the coated particle formed. Parameters such as temperature, pressure, gas composition and gas ratios all play an important role in fixing the coated particle properties" ([[Ch 02 — Manufacture of TRISO Coated Particles]] p.33) — and [[Ch 08 — Fuel Failure Mechanisms]] supplies the specific case. Pyrocarbon deposited at **low coating gas concentration and correspondingly low coating rate** comes out anisotropic, shrinks excessively under irradiation, cracks, and concentrates stress on the SiC. Deposited at higher concentration and rate, it comes out isotropic enough not to. The same divergence governs the IPyC/SiC interface: SiC deposited into a more porous IPyC surface bonds tightly, while a smoother, less porous IPyC gives a weaker bond that debonds under irradiation ([[Ch 08 — Fuel Failure Mechanisms]] p.72).

Two fuels built to the same drawing, from the same gases, differed in whether they failed — on parameters Table 2 does not tolerance.

## Depositing SiC changes the layer beneath it

IPyC and OPyC are deposited from the same gases, at the same temperature, to the same thickness — yet the finished layers differ measurably. Thermal diffusivity is 7.6 ± 3.2 mm²·s⁻¹ for IPyC against 3.6 ± 0.2 for OPyC, and Young's modulus 18 ± 1.1 GPa against 23 ± 1.4 ([[Ch 04 — QA-QC and Characterization]] Tables 5–6, pp.46–47). Both differences are attributed to the same cause: **the IPyC is annealed at roughly 1500–1600 °C while the SiC is being deposited on top of it**, which raises its diffusivity (pp.45, 47).

The SiC step also bonds the two layers permanently. SiC infiltrates the open porosity of the IPyC, producing an interface strong enough that free-standing IPyC fragments cannot be recovered from a fractured particle — IPyC density has to be measured by hot sampling or interrupted batches instead ([[Ch 04 — QA-QC and Characterization]] p.42). By contrast, OPyC fragments separate easily "because of the weak bonding between the SiC and OPyC layers." The interface asymmetry that [[Ch 08 — Fuel Failure Mechanisms]] identifies as decisive turns up here as a laboratory inconvenience.

> [!warning] Conflict — OPyC separation
> [[Ch 04 — QA-QC and Characterization]] p.42 says OPyC separates easily because the SiC/OPyC bond is weak. On 800 µm ZrO₂ surrogates, ORNL could remove OPyC only by gluing the particle down and picking the layer off with tweezers ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] p.7). The authors hypothesise flatter interfaces on the larger kernel, and possibly a rougher SiC surface (pp.7, 9); neither is tested. Different kernels and coaters — unresolved.
> `#conflict`

## Surrogate kernels

Uranium-free kernels let coating development, separate-effects tests and consolidation work proceed without fissile material ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] p.3). Of 16 SiC coater studies compiled by [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]], five coated uranium compounds; the rest used ZrO₂, Al₂O₃ or PyC-coated microspheres, or did not say (pp.5–6). INET's production line has coated ZrO₂ (5.8 g/cm³) and WC (12.8 g/cm³) ([[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] p.4).

A recipe does not carry over between kernels. Starting from AGR-1 (US Advanced Gas Reactor programme) UCO conditions, ORNL needed 29 development runs to reach specification on ZrO₂, citing differences in size, density and thermal properties (Jolly et al. 2016 p.3, Table 1):

| | AGR-1 UCO | ZrO₂ surrogate |
|---|---|---|
| Diameter (µm) | 350 | 800 |
| Density (g/cm³) | 10.92 | 6.0 |
| Specific heat (J/g·K) | > 0.3 | 0.45–0.65 |
| Thermal conductivity (W/m·K) | < 5 | < 4 |

Resulting recipe: [[TRISO Coating Parameters#Gas flows (ORNL)]]. Surrogates also change how the finished particle behaves under characterization: see the separation conflict above.

> [!info] Inferred — per-kernel mass differs ~6.5×
> An 800 µm ZrO₂ kernel weighs 1.592 mg (Jolly et al. 2016 p.7, measured); a 350 µm, 10.92 g/cm³ AGR-1 kernel computes to ~0.245 mg (p.3 values, sphere assumed). The surrogate is about half as dense but ~6.5× heavier per particle, so neither density nor mass is matched. Which governs the fluidisation change is not stated; the development-run report (ORNL/LTR-2015/432) might say.
> `#inferred`

## Acceptance criteria

- PyC layers: impermeable; isotropic texture.
- SiC layer: β-SiC, cubic structure; density > 3.19 Mg/m³; equiaxed microstructure, fine grains, as few flaws as possible.
- PyC–SiC interfaces: sufficient strength.

([[Ch 02 — Manufacture of TRISO Coated Particles]] p.34.) Each maps to a failure mechanism: permeability to diffusive release, anisotropy to shrinkage cracking, interface strength to debonding. Each is also measurable before irradiation — anisotropy by optical anisotropy factor, layer thickness by micro-radiography, SiC integrity by burn-leach. See [[Fuel Quality Control and Characterization]].

Finished particles are sieved for size and sorted on an inclined vibrating table, spherical particles rolling downhill while odd-shaped ones are vibration-transported perpendicular for recycling (p.34). Modern process control holds the defective fraction below 10⁻⁵ (p.23).

## Open questions

- Table 2 gives single-point setpoints with no tolerances, and no gas ratios, despite the text naming gas composition and ratios as decisive. The two production-line sources since ingested give nominal values only, too. One development line (ORNL) now supplies gas flows, coating gas fractions and AGR-1 tolerances ([[TRISO Coating Parameters]]). For SiC, a process window is now in the wiki (1500–1600 °C in H₂, [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] p.8; experimental ranges on [[TRISO Coating Parameters]]). For the PyC layers it is still missing.

## Sources

- [[Ch 02 — Manufacture of TRISO Coated Particles]] · [[Ch 08 — Fuel Failure Mechanisms]] · [[Ch 01 — Introduction]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
- [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]]
- [[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]]
- [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production]] · [[SiC Layer Deposition]]
- [[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels]]
- Data: [[TRISO Coating Parameters]]
