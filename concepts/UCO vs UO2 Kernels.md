---
type: concept
title: UCO vs UO2 Kernels
status: draft
sources: 2
tags: [uco, uo2, kernels, burnup, co, kernel-migration]
updated: 2026-10-14
---

# UCO vs UO₂ Kernels

**In one line** — UO₂ kernels release excess oxygen when they fission, which becomes CO and drives three separate failure mechanisms; UCO carries enough carbon to consume that oxygen inside the kernel, which is why it is the route to high burnup.

## The mechanism, in one chain

Fission of UO₂ releases oxygen that the remaining lattice cannot hold. That oxygen reacts with carbon from the buffer layer to form CO and CO₂ ([[Ch 08 — Fuel Failure Mechanisms]] p.70). From there:

- **Overpressure** — CO and CO₂ add to fission gas in loading the SiC in tension (p.70).
- **Kernel migration** — the C/UO₂/CO/CO₂ equilibrium differs across a thermal gradient, driving carbon transport and apparent kernel movement (p.73). See [[Kernel Migration]].
- **SiC corrosion** — CO reaching the SiC through permeable or cracked IPyC (inner pyrocarbon) can convert it to gaseous SiO at low CO partial pressure (p.76).

All three scale with burnup, and worsen faster than burnup does: at high burnup an increasing fraction of fissions come from plutonium, which releases more oxygen per fission than uranium (p.76).

**UCO breaks the chain at the source.** It is a stoichiometric two-phase mixture of UO₂ and UC₂; the carbon present in the kernel consumes the excess oxygen internally, "preventing CO buildup thereby eliminating kernel migration (or the 'amoeba effect') and excess internal pressures at high burnups" ([[Ch 01 — Introduction]] p.22). Table 8 records the consequence as a one-line disposition: CO generation is **"UO₂ only. Not important for UCO"** ([[Ch 08 — Fuel Failure Mechanisms]] p.77).

UCO also limits fission product mobility by a second route: the oxycarbide form ties up all but the noble fission products as carbides or oxides. Palladium transport is still observed, and so is silver migration (p.74) — so UCO addresses the oxygen problem, not the noble-metal problem. See [[Silver Release]].

## What it costs

| | UO₂ | UCO |
|---|---|---|
| Gelation route | external (gel-precipitation) | internal, with carbon black and HMTA (hexamethyltetramine) in the broth |
| Thermal schedule | calcine 430 °C, reduce 450–650 °C, sinter 1600 °C | calcine 550 °C in H₂, carbothermic reduction 1680 °C, densify 1890 °C |
| Atmosphere control | H₂ for reduction | H₂ to protect carbon, then Ar, then CO/Ar — three stages, each protecting the carbon budget |
| Composition control | stoichiometric UO₂ | 65–85 mol% UO₂ / 0–27 UC₂ / 0–35 UC, specified as O/U and C/U ratios |

From [[Ch 02 — Manufacture of TRISO Coated Particles]] pp.26–30. UCO is a materially harder kernel to make: the whole process is organised around carrying carbon through steps that would otherwise consume it, and the product is a controlled three-phase mixture rather than a single compound. See [[Fuel Kernel Fabrication]].

## The intermediate option

**UO₂\*** puts a thin ZrC layer, with a dense pyrocarbon seal coat, directly on a conventional UO₂ kernel. The ZrC acts as an oxygen getter, limiting CO production and retarding kernel migration — the same objective as UCO, achieved by a coating rather than by kernel chemistry. Tested side by side with UO₂, UC₂ and UCO in the ORNL (Oak Ridge National Laboratory) HFIR (High Flux Isotope Reactor) HRB series at 860–1210 °C, 19–29% FIMA (fissions per initial metal atom), 3.7–6.5 × 10²⁵ n/m², with superior performance in irradiation and post-irradiation annealing ([[Ch 01 — Introduction]] p.22).

## Design implications for HTGRs

The stated motivation for UCO is achieving higher operating temperature *and* increased discharge burnup for better uranium utilisation at the same time ([[Ch 01 — Introduction]] p.22). Both goals push against the same constraints — [[Ch 09 — Accident Testing]] couples the allowable accident temperature to burnup, requiring ≤1600 °C at 15% FIMA — and the CO chain is a large part of why. A design targeting high burnup with UO₂ kernels is accepting overpressure, kernel migration and SiC corrosion as burnup rises; the same design with UCO is not.

Note that the accident-testing evidence base in [[Ch 09 — Accident Testing]] is almost entirely **LEU (low-enriched uranium) UO₂** TRISO, with the highest-burnup element tested at 10.2% FIMA. The argument for UCO at high burnup is mechanistic, and the irradiation data supporting it (US Advanced Gas Reactor (AGR) programme, HRB series) sits in chapters not yet ingested.

## What the pressure costs

Modelled internal pressure in a UO₂ LTI (low-temperature isotropic) TRISO reference particle at 10 % FIMA (fissions per initial metal atom): 4.0 MPa total at 900 °C, of which CO is 0.1; 21.5 MPa at 1200 °C, of which CO is 5.8 ([[Ch 11 — Particle Modeling]] Table 14, p.110). A 300 °C rise multiplies the load on the SiC more than fivefold, and turns CO from negligible into a quarter of it — the quantitative case for the kernel chemistry on this page.

## Sources

- [[Ch 01 — Introduction]] · [[Ch 02 — Manufacture of TRISO Coated Particles]] · [[Ch 08 — Fuel Failure Mechanisms]] · [[Ch 09 — Accident Testing]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
