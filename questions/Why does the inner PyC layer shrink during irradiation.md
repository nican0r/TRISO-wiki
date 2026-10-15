---
type: question
title: Why does the inner PyC layer of a TRISO particle shrink during irradiation
status: draft
sources: 5
tags: [triso, ipyc, pyc, irradiation, dimensional-change, prestress]
asked: 2026-08-26
updated: 2026-10-14
---

# Why does the inner PyC layer of a TRISO particle shrink during irradiation?

**Short answer** — Pyrocarbon is "a collection of imperfect graphite crystallites whose properties are highly anisotropic" ([[Ch 11 — Particle Modeling]] p.109). Each crystallite contracts and expands anisotropically under fast-neutron damage, so the layer's macroscopic dimensional change is set by how those crystallites are oriented — which deposition controls. Under irradiation PyC shrinks radially and tangentially, then turns over to radial swelling at ~2×10²⁵ n/m², with the crossover set by density, temperature and anisotropy ([[Ch 08 — Fuel Failure Mechanisms]] p.71). The shrinkage does not run away: it reaches a quasi-equilibrium against irradiation creep ([[Ch 11 — Particle Modeling]] p.107).

## What the wiki can answer

| Claim | Detail | Source |
|---|---|---|
| Macroscopic behaviour | PyC shrinks radially and tangentially at low fluence, then swells radially past ~2×10²⁵ n/m² | [[Ch 08 — Fuel Failure Mechanisms]] p.71 |
| Functional purpose | Where the IPyC (inner pyrocarbon) is well bonded to the SiC, its shrinkage puts the SiC into compression, offsetting the tensile load from fission gas and CO generated in the kernel | [[Ch 01 — Introduction]] p.18; [[Ch 08 — Fuel Failure Mechanisms]] p.71 |
| Failure mode when it goes wrong | Excess or uneven shrinkage strain (from insufficiently isotropic PyC, itself a consequence of too low a coating-gas concentration during deposition) puts the IPyC into tangential tension high enough to crack it, which stress-concentrates and can fail the SiC beneath | [[Ch 08 — Fuel Failure Mechanisms]] p.71 |
| Fabrication link | German fuel, coated at higher gas concentrations and coating rates than historical US fuel, does not show these shrinkage cracks; the US New Production Reactor–era irradiations did | [[Ch 08 — Fuel Failure Mechanisms]] p.71 |
| Layer design intent | Both PyC layers are specified as impermeable and isotropic partly *because* shrinkage behaviour is orientation-dependent | [[TRISO Particle Architecture]] |
| **Crystallite mechanism** | PyC is imperfect graphite crystallites, individually highly anisotropic; random orientation is required precisely "to avoid shrinkage rates in the tangential direction being so large that they cause fracture" | [[Ch 11 — Particle Modeling]] p.109 |
| **What bounds the shrinkage** | Shrinkage is restrained by the SiC and counter-balanced by irradiation creep in the PyC, reaching a quasi-equilibrium stress state | [[Ch 11 — Particle Modeling]] p.107 |
| **What it buys** | SiC sits in compression early in life at roughly −330 MPa, crosses into tension near 8 % burnup as gas pressure accumulates, and fails at 650 MPa near 13 % in the modelled example | [[Ch 11 — Particle Modeling]] p.109, Fig. 59 |
| **Deposition control, measured** | IPyC anisotropy spans 0.0031–0.0151 diattenuation across a 1170–1325 °C × 0.15–0.45 coating-gas-fraction study, varying non-monotonically in both | [[PyC Layer Deposition]]; [[Effects of Deposition Conditions on the Properties of Pyrolytic Carbon Deposited in a Fluidized Bed\|Lowden et al. 2005]] p.34 |
| **The failure chain, observed** | Buffer densification and shrinkage fractures the buffer, cracks the IPyC, and in rare cases the crack propagates through the SiC — the two AGR-1 particles that released caesium during irradiation came from the lower-density-IPyC variant lot | [[PIE on Five Irradiated AGR-1 Compacts\|Hunn et al. 2012]] p.4 |

See [[TRISO Particle Architecture]] for the full layer stack and [[TRISO Fuel Failure Mechanisms]] for where IPyC cracking sits among the eleven documented failure modes.

## What is missing

The qualitative mechanism is now answered; the quantitative link is not. No ingested source gives **a dimensional-change rate as a function of an anisotropy measurement** — the coefficient that would turn a measured diattenuation into a predicted shrinkage strain at a given fluence and temperature. [[Ch 11 — Particle Modeling]] states the form of the equations (strain = elastic + creep + thermal + irradiation-induced dimensional change, p.108) and supplies no coefficients for any of the terms, nor the fracture-stress distribution its Monte Carlo sampling needs.

Below the crystallite statement there is also no damage physics: nothing in the wiki describes basal-plane contraction and c-axis expansion, displacement cascades, or why crystallite dimensional change reverses sign with fluence.

[[Irradiation Damage in Nuclear Graphite]] documents an analogous shrink-then-swell, orientation-dependent response in *structural* graphite — but that page is explicit that matrix and block graphite are a different material from particle-coating PyC, so it should be read as a pattern match, not evidence for the coating layers.

**What would close the gap:**

- **Skerjanc & Collin, INL/EXT-18-44631**, "Assessment of Material Properties for TRISO Fuel Particles used in PARFUME" — PyC radial and tangential dimensional-change rate coefficients as functions of anisotropy, density and temperature, integrated over fast fluence, plus irradiation creep. Free from INL; this is the mapping the table above is missing.
- A graphite or pyrocarbon radiation-damage paper for the crystallite physics itself.

## Sources

- [[Ch 01 — Introduction]] · [[Ch 08 — Fuel Failure Mechanisms]] · [[Ch 11 — Particle Modeling]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
- [[Effects of Deposition Conditions on the Properties of Pyrolytic Carbon Deposited in a Fluidized Bed]] · [[PIE on Five Irradiated AGR-1 Compacts]]
- Concept pages: [[TRISO Particle Architecture]], [[TRISO Fuel Failure Mechanisms]], [[Irradiation Damage in Nuclear Graphite]], [[PyC Layer Deposition]]
