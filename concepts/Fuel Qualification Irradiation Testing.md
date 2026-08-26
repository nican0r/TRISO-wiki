---
type: concept
title: Fuel Qualification Irradiation Testing
status: draft
sources: 1
tags: [qualification, irradiation-testing, acceleration, release-to-birth, statistics]
updated: 2026-08-25
---

# Fuel Qualification Irradiation Testing

**In one line** — Demonstrating that TRISO fails at rates below 10⁻⁵ requires irradiating hundreds of thousands of particles in a reactor that is the wrong kind of reactor, faster than reality, at a temperature nobody can measure directly — and the discipline consists of bounding each of those compromises.

## Four constraints

### The test reactor is water-moderated

Almost all material test reactors are water cooled and moderated, so a position must be chosen that approximates a gas reactor spectrum while still delivering enough flux to finish in reasonable time. Get the fast-to-thermal ratio wrong and the test is unrepresentative in one of two directions: the FRJ reactor at Jülich was too thermalised, so fuel received too little fast fluence to be prototypic; HFIR (High Flux Isotope Reactor) at Oak Ridge had thermal flux too high, causing significant burnup acceleration ([[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] p.63). Neutron absorbers can suppress thermal flux where space allows (p.62).

### Time must be compressed, but not too much

Service burnup and fluence accumulate over about 1095 days; tests accelerate by factors of two to ten (p.61). Acceleration is not free — it induces failures that would not occur in service, because [[Kernel Migration]] responds to thermal gradient and fission product attack to time at temperature, both of which acceleration distorts. The convergent recommendation across chapters is **acceleration no greater than 3×** ([[Ch 08 — Fuel Failure Mechanisms]] pp.73–74; [[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] pp.62–63). The ATR (Advanced Test Reactor) large B positions and HFR-Petten both operate under that limit; full burnup still takes roughly two years.

### Fuel temperature cannot be measured

Thermocouples must not touch the fuel, because transition metals attack SiC — Fe, Cr and Ni are named, with transport and corrosion rates unknown, and 2–3 mm of graphite between fuel and any metallic component found to be effective mitigation ([[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] p.64). Temperature is therefore calculated from thermocouples elsewhere in the capsule plus three-dimensional thermal and physics analysis. Capsules are controlled by blending two gases of differing thermal conductivity across an insulating jacket, compensating automatically for falling fission heat as burnup accumulates (pp.63, 66).

Instrumentation is at its limit: with fuel temperatures pushed toward 1250 °C, conventional thermocouples may not survive a two-year irradiation without drift or de-calibration, and past experiments carried high uncertainty in centreline temperature (p.64).

> [!info] Reading the 3× ceiling against the two-year duration
> These reconcile once the endpoints are distinguished: 1095 days is time to *design service* burnup and fluence, while the two-year figure is time to *full* burnup under a high-burnup goal. At 3×, two years delivers roughly twice service-design exposure — consistent with test articles at 19–29% FIMA (fissions per initial metal atom) against service below 11%. An acceleration factor is nonetheless underspecified unless its basis is stated (burnup or fluence, test or service target, at-power or calendar time), and this document states neither. Derived here, not stated in the source — see [[How are fuel compacts irradiated in qualification testing]].
> `#inferred`

### The statistics demand scale

Binomial statistics govern sample size: **approximately 200,000 particles must be irradiated with zero failures to demonstrate a failure probability of 2 × 10⁻⁵ at 95% confidence** ([[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] p.67, Fig. 33). Every low failure fraction quoted anywhere in this literature is a statement of this kind — see the 221,840 particles behind the 1600 °C result in [[Ch 09 — Accident Testing]] and the ~120,000-particle lots behind AGR-1 (a US Advanced Gas Reactor programme irradiation) in [[Ch 05 — Fabrication of Fuel Compacts]].

## Release-to-birth ratio

R/B is the on-line measurement of fission gas release from fuel under irradiation, computed from sweep-gas concentration. Its value is diagnostic rather than merely quantitative, because it is available as a continuous time history ([[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] p.69):

| When release appears | What it means |
|---|---|
| From the start of irradiation | initially failed particles, or contamination outside the SiC layer |
| Later in the irradiation | *in situ* particle failure |

Failure timing correlates against temperature, burnup and fluence, and combined with post-irradiation examination identifies the mechanism responsible. This is what allows the claim, made throughout, that release is dominated by as-manufactured defects rather than by service — it is measured, not assumed. It complements the destructive burn-leach test in [[Fuel Quality Control and Characterization]]: burn-leach counts defects in a sacrificed sample before irradiation, R/B watches the actual irradiated population continuously.

Practical constraint worth noting: argon cannot be used as the temperature-control gas when on-line fission product monitoring is in use, because activated ⁴¹Ar (t½ = 1.8 h) swamps detectability. Helium and neon are used instead ([[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] p.66).

## What the historical record can and cannot tell us

German fuel shows roughly **1000× lower end-of-life R/B than US fuel** across a broad range of conditions ([[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] p.62, Fig. 29).

> [!warning] The gap is confounded
> The two programmes differed simultaneously in fabrication practice — coating gas concentration, coating rate, matrix form ([[Ch 08 — Fuel Failure Mechanisms]] pp.72, 75) — and in test acceleration, German factors mostly under three against US factors up to ten ([[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] pp.61–62). Since the same chapter states that high acceleration causes premature failures, some unknown share of the 1000× is a test artefact rather than a fuel property. No source here separates them.
> `#conflict`

## What this does not establish

Position selection controls the **spectrum** reaching the capsule and the **rate** at which burnup and fluence accumulate. It says nothing about how flux is distributed *within* a compact — self-shielding across a bed of kernels at ~30% packing fraction, radial or axial depression across a 13 mm × 51 mm compact, or the resulting spread of burnup between particles that are reported under a single lot-average figure. Since every mechanism in [[TRISO Fuel Failure Mechanisms]] responds to *local* burnup, fluence and thermal gradient, that spread is not a detail. See [[How are fuel compacts irradiated in qualification testing]].

## Design implications for HTGRs

Qualification is the schedule. A single campaign runs about two years of irradiation on hundreds of thousands of particles, preceded by capsule design with 3D physics and thermal analysis and followed by post-irradiation examination and accident simulation heating. Multi-cell capsules — independent compartments at different temperature, burnup and fluence — exist because they compress that schedule by testing several conditions in one campaign (p.62).

Any change to the fuel restarts some part of it. That is the practical weight behind the observations in [[TRISO Coating Process]] that deposition parameters determine performance, and in [[Irradiation Damage in Nuclear Graphite]] that each graphite grade needs its own irradiation testing.

## Filed answers

- [[How are fuel compacts irradiated in qualification testing]]

## Sources

- [[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] · [[Ch 08 — Fuel Failure Mechanisms]] · [[Ch 09 — Accident Testing]] · [[Ch 05 — Fabrication of Fuel Compacts]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
