---
type: source-chapter
title: Ch 11 — Particle Modeling
source: High Temperature Gas Cooled Reactor Fuels and Materials
pages: 106-110
ingested: 2026-10-14
status: draft
tags: [triso, modeling, stress, irradiation, pyc, sic, crystallite, failure-fraction]
updated: 2026-10-14
---

# Ch 11 — Particle Modeling

Part of [[High Temperature Gas Cooled Reactor Fuels and Materials]] · pp.106–110

**Gist** — How particle failure is predicted rather than measured. The chapter sets out the mechanical model of a coated particle under irradiation: tangential stresses in the three load-bearing layers, driven by internal gas pressure and by the pyrocarbon layers' attempt to shrink, computed over successive neutron-dose steps. It is short and self-describing as a sketch rather than a specification, but it supplies two things the rest of the wiki lacks — the mechanism by which pyrocarbon shrinkage is anisotropic, and the path from single-particle mechanics to a population failure fraction.

## The mechanical picture

- The kernel swells and the buffer shrinks, so the two decouple mechanically early in irradiation and the buffer may crack. Either way its porosity lets fission gas reach the inner surface of the IPyC (inner pyrocarbon), so **the only mechanical load on the three load-bearing layers is that gas pressure** (pp.106–107).
- Without the pyrocarbon layers, that pressure would act on the SiC alone. The PyC layers shrink under irradiation, are restrained by the SiC, and so pull inward on it — turning part of the SiC's tensile load into compression (p.107).
- That shrinkage does not run away: **it reaches a quasi-equilibrium against irradiation creep** in the PyC (p.107).
- SiC carries the load because its elastic modulus is at least an order of magnitude above PyC's, and its own dimensional change and creep strains are comparatively very small (p.107).

## Why anisotropy is the property that matters

> "In simple terms, PyC may be regarded as a collection of imperfect graphite crystallites whose properties are highly anisotropic. To make their macroscopic properties as isotropic as possible the PyC layers must be manufactured with these crystallites in random orientations. This is necessary to avoid shrinkage rates in the tangential direction being so large that they cause fracture." (p.109)

This is the link between deposition and failure stated at the crystallite level: the crystallites are intrinsically anisotropic, deposition controls their orientation distribution, and orientation sets the tangential shrinkage rate. The chapter also names PyC property variability as a major source of modelling uncertainty, "strongly dependent on the manufacturing procedure" (p.109). Measured anisotropy against deposition conditions: [[PyC Layer Deposition]].

## How the calculation runs

Irradiation history is split into neutron-dose steps; within each, three sets of equations per layer (p.107–108):

1. **Displacement** — total strain change = elastic + irradiation creep + thermal + irradiation-induced dimensional change, in radial and tangential directions, e.g. $\varepsilon_1 = g_1 + K(1-\nu)\sigma_1 - K\nu\sigma_1$ with $g$ the creep rate, $K$ the creep constant and $\nu$ Poisson's ratio.
2. **Compatibility** — $\varepsilon_1 = u/x$, $\varepsilon_3 = u'$, relating radial displacement to strain in spherical geometry.
3. **Equilibrium** — $\sigma_1 = \sigma_3 + \tfrac{1}{2}x\sigma_3'$.

Five simultaneous equations per layer reduce to one second-order differential equation; boundary conditions impose continuity of radial displacement and stress at interfaces. If a radial stress exceeds the de-bonding stress, the step is re-run with modified boundary conditions; if a tangential stress exceeds a layer's fracture stress, that layer is failed by driving its stress to zero and setting its tangential compliance very high for later steps (p.108). The model therefore continues past the failure of one or two layers, which matters because a particle retains some containment after losing one.

![[tecdoc1645-p109-fig59-layer-stresses.jpeg]]
*Fig. 59, p.109 — stresses in the three load-bearing layers against neutron dose and burnup. SiC starts compressive at roughly −330 MPa, crosses zero near 40 × 10²⁴ n·m⁻² (~8 % burnup) as gas pressure accumulates, and fails at its 650 MPa fracture stress near 60 × 10²⁴ (~13 %). IPyC relaxes from about +190 MPa; OPyC sits near +100 MPa throughout. Values read off the plot.*

## From one particle to a failure fraction

Particles do not all fail at one burnup, for two stated reasons: the layers are brittle, so fracture stress varies particle to particle, and the particles themselves vary in geometry and properties (p.108). The population failure fraction is therefore obtained by **Monte Carlo** — running the single-particle code many times over specifications sampled from the measured statistical variations, and recording the burnup at which each fails (p.109). Simple analytical models, which assume stress does not deform the SiC, are kept as a check for gross errors in the full codes (p.109).

## Data extracted

| Quantity | Value | Conditions | Page |
|---|---|---|---|
| SiC fracture stress | 650 MPa | the modelled example | p.108 |
| SiC/PyC elastic modulus ratio | ≥ 10× | — | p.107 |
| Acceptance level, failure fraction | 2 × 10⁻⁵ to 6 × 10⁻⁵ | Fig. 60 caption | p.110 |
| Gas pressure at 10 % FIMA (fissions per initial metal atom), 900 °C | 3.9 MPa fission gas + 0.1 CO = 4.0 total | UO₂ LTI (low-temperature isotropic) TRISO reference particle, Table 14 | p.110 |
| Gas pressure at 10 % FIMA, 1200 °C | 15.7 + 5.8 = 21.5 MPa | same | p.110 |

The 300 °C temperature rise multiplies total internal pressure by more than five, most of it fission gas, with CO rising from negligible to a quarter of the total — the pressure-side case for [[UCO vs UO2 Kernels]].

## What this changes in the wiki

- Gives [[Why does the inner PyC layer shrink during irradiation]] its crystallite-level answer and the creep balance that bounds the shrinkage.
- Adds the stress history behind the prestress argument on [[TRISO Particle Architecture]].
- Supplies the modelling counterpart to the measured failure modes on [[TRISO Fuel Failure Mechanisms]], including why failure fractions are distributions rather than thresholds.

## Open questions raised

- The chapter gives the form of the dimensional-change and creep terms but no coefficients, and no mapping from an anisotropy measurement to a shrinkage rate. A material-property compilation (PARFUME's, for instance) would close that.
- Fracture stress is used as a single number in the worked example while the text says it is variable; the distribution used in the Monte Carlo is not given.
