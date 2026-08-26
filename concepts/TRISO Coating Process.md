---
type: concept
title: TRISO Coating Process
status: draft
sources: 1
tags: [triso, cvd, fabrication, fluidised-bed, sic, pyc]
updated: 2026-08-25
---

# TRISO Coating Process

**In one line** — All four TRISO layers are deposited by chemical vapour decomposition onto kernels suspended in a fluidised bed, in one uninterrupted sequence in a single reactor, with the deposition parameters — not the design — determining whether the resulting particle survives irradiation.

## Mechanism

Kernels are suspended by flowing gas in a heated fluidised bed reactor. Coating gases are chosen to decompose at temperatures up to 1600 °C and deposit constituents on the kernel surfaces; the layers are called pyrolytic because they form by heat-driven chemical decomposition. All four layers are applied sequentially without interruption in the same reactor ([[Ch 02 — Manufacture of TRISO Coated Particles]] pp.30, 33).

| Layer | Gas | Carrier | T (°C) | Rate (µm/min) |
|---|---|---|---|---|
| Buffer | C₂H₂ | Argon | 1250 | 10 |
| IPyC | C₂H₂ + C₃H₆ | Argon | 1300 | 5 |
| SiC | CH₃SiCl₃ | Hydrogen | 1500 | 0.2 |
| OPyC | C₂H₂ + C₃H₆ | Argon | 1300 | 5 |

Table 2, [[Ch 02 — Manufacture of TRISO Coated Particles]] p.33. Reactions: $\text{C}_2\text{H}_2 \rightarrow 2\text{C} + \text{H}_2$; $\text{C}_3\text{H}_6 \rightarrow 3\text{C} + 3\text{H}_2$; $\text{CH}_3\text{SiCl}_3 \rightarrow \text{SiC} + 3\text{HCl}$.

**SiC is the outlier on every axis**: 25–50× slower than the pyrocarbon layers, 200 °C hotter, and under hydrogen rather than argon. It is the rate-limiting step of the sequence, and the HCl it liberates is the reason the IPyC (inner pyrocarbon) layer beneath it doubles as a chlorine barrier ([[Ch 01 — Introduction]] p.22).

## Why the parameters, not the recipe, decide the outcome

The source states it generally — "the conditions under which layer deposition takes place are very important as these deposition parameters determine the properties of the coated particle formed. Parameters such as temperature, pressure, gas composition and gas ratios all play an important role in fixing the coated particle properties" ([[Ch 02 — Manufacture of TRISO Coated Particles]] p.33) — and [[Ch 08 — Fuel Failure Mechanisms]] supplies the specific case. Pyrocarbon deposited at **low coating gas concentration and correspondingly low coating rate** comes out anisotropic, shrinks excessively under irradiation, cracks, and concentrates stress on the SiC. Deposited at higher concentration and rate, it comes out isotropic enough not to. The same divergence governs the IPyC/SiC interface: SiC deposited into a more porous IPyC surface bonds tightly, while a smoother, less porous IPyC gives a weaker bond that debonds under irradiation ([[Ch 08 — Fuel Failure Mechanisms]] p.72).

Two fuels built to the same drawing, from the same gases, differed in whether they failed — on parameters this table does not tolerance.

## Depositing SiC changes the layer beneath it

IPyC and OPyC (outer pyrocarbon) are deposited from the same gases, at the same temperature, to the same thickness — yet the finished layers differ measurably. Thermal diffusivity is 7.6 ± 3.2 mm²·s⁻¹ for IPyC against 3.6 ± 0.2 for OPyC, and Young's modulus 18 ± 1.1 GPa against 23 ± 1.4 ([[Ch 04 — QA-QC and Characterization]] Tables 5–6, pp.46–47). Both differences are attributed to the same cause: **the IPyC is annealed at roughly 1500–1600 °C while the SiC is being deposited on top of it**, which raises its diffusivity (pp.45, 47).

The SiC step also bonds the two layers permanently. SiC infiltrates the open porosity of the IPyC, producing an interface strong enough that free-standing IPyC fragments cannot be recovered from a fractured particle — IPyC density has to be measured by hot sampling or interrupted batches instead ([[Ch 04 — QA-QC and Characterization]] p.42). By contrast, OPyC fragments separate easily "because of the weak bonding between the SiC and OPyC layers." The interface asymmetry that [[Ch 08 — Fuel Failure Mechanisms]] identifies as decisive turns up here as a laboratory inconvenience.

## Acceptance criteria

- PyC layers: impermeable; isotropic texture.
- SiC layer: β-SiC, cubic structure; density > 3.19 Mg/m³; equiaxed microstructure, fine grains, as few flaws as possible.
- PyC–SiC interfaces: sufficient strength.

([[Ch 02 — Manufacture of TRISO Coated Particles]] p.34.) Each maps to a failure mechanism: permeability to diffusive release, anisotropy to shrinkage cracking, interface strength to debonding. Each is also measurable before irradiation — anisotropy by optical anisotropy factor, layer thickness by micro-radiography, SiC integrity by burn-leach. See [[Fuel Quality Control and Characterization]].

Finished particles are sieved for size and sorted on an inclined vibrating table, spherical particles rolling downhill while odd-shaped ones are vibration-transported perpendicular for recycling (p.34). Modern process control holds the defective fraction below 10⁻⁵ (p.23).

## Open questions

- Table 2 gives single-point setpoints with no tolerances, and no gas ratios, despite the text naming gas composition and ratios as decisive. The process window is not in this source.

## Sources

- [[Ch 02 — Manufacture of TRISO Coated Particles]] · [[Ch 08 — Fuel Failure Mechanisms]] · [[Ch 01 — Introduction]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
