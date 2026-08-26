---
type: concept
title: Fission Product Retention
status: draft
sources: 1
tags: [triso, fission-product-release, sic, accident-testing]
updated: 2026-08-25
---

# Fission Product Retention

**In one line** — The TRISO particle's function is to hold fission products inside itself under normal operation and accident conditions, and the degree to which it does so is species-dependent, temperature-dependent, and sharply non-linear above about 1600 °C.

## Mechanism

Retention is layered, and each layer holds different species. The kernel binds some chemically; buffer and pyrocarbon impede gaseous transport; SiC is the primary pressure boundary and the strongest barrier to metallic fission products; in spherical fuel the graphitic matrix adds further delay. Retention therefore cannot be quoted as a single number — it is species- and temperature-dependent.

Two consequences shape everything else. **Above roughly 1800 °C the layering collapses**: neither kernel nor matrix delays release and SiC itself turns permeable ([[Ch 09 — Accident Testing]] p.89, which sets out the per-species hierarchy). And **retention can fail without any layer breaking** — diffusive release through intact coatings above ~1300 °C, and induced SiC permeability at high burnup and fluence ([[Ch 08 — Fuel Failure Mechanisms]] pp.75–76). A particle can be functionally failed while mechanically sound.

What the coating is worth shows in the contrast with bare fuel: exposed UO₂ kernels release silver, xenon, iodine and caesium at close to 100% during a 1600 °C test, while modern TRISO holds ¹³¹I release to 10⁻⁹–10⁻⁸ — four to five orders of magnitude ([[Ch 09 — Accident Testing]] pp.83–84).

## The limit that is not the accident limit

The 1600 °C threshold is the accident limit. The **highest normal operating fuel temperature should not be greater than 1250 °C** ([[Ch 01 — Introduction]] p.18) — and diffusive cesium release through wholly intact coatings becomes significant as temperatures approach 1300 °C ([[Ch 08 — Fuel Failure Mechanisms]] p.75). Normal operation is therefore bounded roughly 50 °C below a release mechanism that requires no failure of any kind. The SiC layer's own containment function is stated to hold to approximately 1800 °C ([[Ch 01 — Introduction]] p.22), so the three limits — 1250, 1600, 1800 °C — describe service, accident, and material capability respectively.

## What escapes regardless

About **10⁻⁵ of an element's uranium sits outside the SiC boundary by construction**: uranium trapped in the coating layers during coating ("tramp" uranium) plus impurities in the matrix material and in the PyC source material ([[Ch 01 — Introduction]] p.22). The modern manufactured defect fraction is the same order, below 10⁻⁵ ([[Ch 02 — Manufacture of TRISO Coated Particles]] p.23). Retention is therefore never total, and the floor is set in the factory — which is what [[Ch 09 — Accident Testing]] means when it attributes release to as-manufactured defects and heavy metal contamination rather than to in-service mechanisms.

## Evidence that the floor is manufactured, not operational

The attribution of release to as-manufactured defects is measured rather than inferred. On-line release-to-birth monitoring during irradiation separates the two by timing — release present from the start of an irradiation indicates initially failed particles or contamination outside the SiC layer, while release appearing later indicates failure occurring in service ([[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] p.69). See [[Fuel Qualification Irradiation Testing]].

## Quantitative anchors

| Quantity | Value | Conditions | Source |
|---|---|---|---|
| Particle failure fraction | 0 observed; 1.35 × 10⁻⁵ at 95% upper limit | 1600 °C isothermal, 221,840 particles | [[Ch 09 — Accident Testing]] p.91 |
| Particle failure fraction | 6.10 × 10⁻⁵ | 1620 °C MODUL heatup, 82,000 particles | p.91 |
| ⁸⁵Kr fractional release | 10⁻⁷ to 10⁻⁶ | 1600 °C, up to 500 h | Fig. 47, p.90 |
| ⁸⁵Kr fractional release | ~10⁻⁴ to 2 × 10⁻³ | 1800 °C | Fig. 47, p.90 |
| ¹³¹I fractional release, modern TRISO | 10⁻⁹ to 10⁻⁸ | 1600 °C heating test | p.84 |
| Onset of diffusive Cs release | ~1300 °C | normal operation, intact coatings | [[Ch 08 — Fuel Failure Mechanisms]] p.75 |
| Detection floor of the measurement | 10⁻⁸ fractional release | KÜFA (Cold Finger Apparatus) | [[Ch 09 — Accident Testing]] p.83 |

## Design implications for HTGRs

The passive safety case is built on the gap between the accident peak temperature and the temperature at which retention degrades. Modern small HTRs peak at 1620 °C in a depressurised loss of forced circulation ([[Ch 09 — Accident Testing]] p.78), and 1600 °C is where the zero-failure evidence sits. The margin is tens of degrees, and it is bounded by test data rather than by a physical discontinuity — the tests establish where release has been measured, not where it begins.

Burnup consumes that margin. Below 11% FIMA (fissions per initial metal atom) the limit may be higher than 1600 °C but has not been established; at 15% FIMA the temperature must be held at or below 1600 °C (p.91). Any decision to raise burnup is a decision about accident temperature.

## Contested / uncertain

> [!warning] 1700 °C behaviour is not characterised
> Two elements tested at 1700 °C gave opposite outcomes — 18 failures in ~10 h versus none in 185 h — with no explanation offered. See [[Ch 09 — Accident Testing]].
> `#conflict`

## Sources

- [[Ch 09 — Accident Testing]] · [[Ch 08 — Fuel Failure Mechanisms]] — both from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
