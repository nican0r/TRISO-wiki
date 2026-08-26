---
type: question
title: How are fuel compacts irradiated in qualification testing
status: draft
sources: 1
tags: [irradiation-testing, qualification, neutron-flux, acceleration, agr]
asked: 2026-08-25
updated: 2026-08-25
---

# How are fuel compacts irradiated in qualification testing?

**Short answer** — Compacts are loaded into instrumented multi-cell capsules and irradiated in a position of a water-moderated material test reactor chosen to approximate a gas reactor spectrum, at an acceleration factor under three, for roughly two years, with capsule temperature controlled by gas blending and fission gas release monitored continuously. The US reference case is the Advanced Gas Reactor programme in the INL (Idaho National Laboratory) Advanced Test Reactor.

**The sub-question is only partly answerable from the wiki as it stands.** See [Flux realism](#how-realistic-is-the-neutron-flux) below.

---

## The process

Full detail on [[Ch 07 — TRISO-Coated Particle Fuel Irradiations]]; the sequence in brief:

*Acronyms used below: KÜFA, the Cold Finger Apparatus; NGNP, the US Next Generation Nuclear Plant; LEU, low-enriched uranium; ORNL, Oak Ridge National Laboratory.*

| Step | Constraint that shapes it |
|---|---|
| **Position selection** | Test reactors are water-moderated, so the position must approximate a gas reactor's fast-to-thermal ratio. US Advanced Gas Reactor (AGR) programme uses the Advanced Test Reactor (ATR) large B positions, 38 mm diameter (p.62). |
| **Multi-cell capsule** | Independent compartments at separate temperature, burnup and fluence; 3D physics and thermal analysis before irradiation (pp.62–63). |
| **Thermal control** | Blending two gases of differing conductivity across an insulating jacket, adjusted automatically as fission heat falls. Helium/neon rather than helium/argon whenever fission products are monitored, since activated ⁴¹Ar (t½ = 1.8 h) swamps detection (pp.63, 66). |
| **Instrumentation** | Thermocouples never touch the fuel — Fe, Cr and Ni attack SiC — so temperature is *calculated* from thermocouples in a graphite sleeve with 2–3 mm standoff (p.64). |
| **Duration** | ~2 years at under 3× acceleration (pp.61–63). |
| **Monitoring** | Continuous release-to-birth ratio (R/B) from sweep gas; timing discriminates initial defects from *in situ* failure (p.69). |
| **Scale** | ~200,000 particles with zero failures for 2 × 10⁻⁵ at 95% confidence (p.67). |
| **After** | Post-irradiation examination and accident simulation heating — [[Ch 09 — Accident Testing]]. |

## Does 3× acceleration square with a two-year irradiation?

**Yes — because the two figures describe different endpoints.** The 1095-day figure is time to reach *design service* burnup and fast fluence ([[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] p.61). The two-year figure is time to reach *full burnup* under "the goal to achieve high burnups with these fuels" (p.63). Qualification deliberately overshoots service conditions to establish margin, so the second endpoint is further away than the first.

### The arithmetic

| Quantity | Value | Source |
|---|---|---|
| Time to design service burnup and fast fluence, in service | ~1095 days (3 years) | [[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] p.61 |
| Acceleration ceiling in a well-chosen test position | < 3× | pp.61–63 |
| Implied time to *service-equivalent* exposure under test | ~365 days | derived |
| Observed time to *full* burnup, LEU TRISO | ~2 years (~730 days) | p.63 |
| Implied test target, as a multiple of service exposure | **~2×** | derived |

At 3×, two years of irradiation delivers roughly twice the service-design exposure. The ceiling and the duration are consistent once the endpoint is read correctly; the apparent 1.5× is an artefact of comparing a test target against a service target.

### The wiki corroborates the implied overshoot

The inference predicts test burnups around twice service burnup. That prediction is independently supported by burnup figures already in the wiki:

| Population | Burnup | Source |
|---|---|---|
| Service design, present HTR designs | strictly below 11% FIMA | [[Ch 09 — Accident Testing]] p.91 |
| Spheres showing induced SiC permeability | 14% FIMA | [[Ch 08 — Fuel Failure Mechanisms]] p.76 |
| HRB irradiation series (UO₂\*, UO₂, UC₂, UCO) | 19–29% FIMA | [[Ch 01 — Introduction]] p.22 |
| Highest-burnup element in KÜFA accident testing | 10.2% FIMA | [[Ch 09 — Accident Testing]] p.88 |

Service below 11% against test articles at 19–29% is roughly the factor of two the arithmetic requires. Note also the asymmetry in the last row: the *irradiation* programme pushes well past service burnup, while the *accident-testing* population tops out near service burnup — which is why [[Ch 09 — Accident Testing]]'s statement that 15% FIMA (fissions per initial metal atom) demands ≤1600 °C is an extrapolation rather than a measured result.

> [!info] This is a wiki inference, not a statement in the source
> The document quotes both figures two pages apart and never reconciles them. The reconciliation above is derived here from the difference in wording between "design service burnup" (p.61) and "full burnup … high burnups" (p.63), and corroborated against burnup figures elsewhere in the document. Both source figures are generic — "for most of these fuels" and "it is not uncommon" — so this is order-of-magnitude reasoning, not a derivation from a specific campaign.
> `#inferred`

### Residual uncertainty

The endpoint explanation does not exclude three secondary factors, each of which would shift the implied overshoot:

- **"Less than three" is an inequality, not a value** (p.62). If the true factor is nearer 2, the implied test target falls to about 1.3× service rather than 2×.
- **Calendar time is not at-power time.** Acceleration is a rate ratio applied to integrated at-power exposure, while a campaign's elapsed duration includes outages between reactor cycles — which the chapter confirms happen, recommending xenon measurements "during reactor outages" (p.69), and which is the sense in which it discusses thermocouple survival over "the long (two years) fuel qualification irradiations" (p.64).
- **Burnup and fast fluence do not accelerate together** (p.61). In a water-moderated reactor the two axes decouple — the FRJ and HFIR (High Flux Isotope Reactor) failure modes on p.63 are exactly this — so a campaign ends when the slower target is met, and a 3× figure on one axis is not 3× on the other.

**Practical consequence: an acceleration factor is underspecified unless its basis is stated** — burnup or fast fluence, test target or service target, at-power or calendar time. This document states neither figure's basis. When recording an acceleration factor from any source, record the basis with it, or the number will not be comparable across programmes. That also bears on the confounded German/US comparison in [[Fuel Qualification Irradiation Testing]], where ≤3× and 10× may not have been measured the same way.

**What would confirm it:** the AGR-1 and AGR-2 irradiation reports state as-run acceleration alongside target and achieved burnup and fluence, and at-power days against calendar days.

---

## How realistic is the neutron flux?

The wiki can answer this for **spectrum and rate**. It cannot answer it for **flux distribution within a compact**.

### What the source does establish

**Spectral realism is a position-selection problem, and the failure modes are documented in both directions.** A test reactor position can be wrong by being too thermal or too fast relative to a gas reactor:

| Facility | Outcome | Page |
|---|---|---|
| FRJ (Jülich) | spectrum **too thermalised** — fuel received too little fast fluence to be prototypic of an HTGR | p.63 |
| HFIR (ORNL) | thermal flux **too high** — significant burnup acceleration during irradiation | p.63 |
| ATR large B positions | acceleration **< 3×** relative to NGNP conditions | p.62 |
| HFR-Petten | successful irradiations at **< 3×** | p.63 |

The two errors are distinct. A too-thermal spectrum under-delivers fast fluence, so coating damage mechanisms driven by fast neutrons — pyrocarbon shrinkage and swelling, which begins around 2 × 10²⁵ n/m² ([[Ch 08 — Fuel Failure Mechanisms]] p.71) — are under-represented relative to burnup. A too-high thermal flux over-delivers burnup for the fluence accumulated, distorting the ratio the other way. **Realism here means the fast-to-thermal ratio, not the absolute flux.**

**Thermal flux can be shaped.** Neutron absorbers placed around the capsule suppress thermal flux and moderate heat generation where space allows (p.62) — the direct lever for correcting a too-thermal position.

**Conditions are calculated first and measured afterwards.** Three-dimensional physics analysis establishes the expected burnup and fluence distribution before irradiation (p.63), and the capsule carries instrumentation to measure temperature, burnup and fast fluence **at multiple locations in the test train** (p.64), with thermal and fast fluence wires as the measurement (p.65).

**Acceleration is itself a realism constraint, not just a schedule one.** Because [[Kernel Migration]] responds to thermal gradient and fission product attack to time at temperature, an over-accelerated test produces failures that would not occur in service — the source calls these false positives and recommends the 3× ceiling specifically to avoid them ([[Ch 08 — Fuel Failure Mechanisms]] pp.73–74).

### What is missing

The ingested chapters say nothing about flux uniformity *inside* a compact. Specifically absent:

- **Self-shielding within the particle bed.** A compact is a dispersion of ~500 µm high-density kernels in graphite at roughly 30% packing fraction ([[Ch 05 — Fabrication of Fuel Compacts]] p.48). Whether outer particles shadow inner ones, and by how much, is not discussed.
- **Radial and axial flux depression across a compact.** Compacts are ~13 mm diameter × 51 mm long ([[Ch 01 — Introduction]] p.15) sitting in a 38 mm test position. No flux gradient across that dimension is quoted.
- **Resulting burnup spread between particles in one compact.** Failure fractions are reported per compact lot as single numbers; the distribution of burnup across particles within a compact is not given.
- **Axial flux profile along the test train.** Instrumentation is stated to exist at multiple locations, but no profile or peak-to-average figure appears.

This matters because every failure mechanism in [[TRISO Fuel Failure Mechanisms]] is a function of local burnup, local fluence and local thermal gradient. A lot-average burnup of 10% FIMA with an undisclosed spread is a different statement from a uniform 10%.

### What would close the gap

- **AGR programme irradiation reports** (AGR-1, AGR-2 final reports, INL) — these carry as-run physics analyses with per-compact and often per-capsule burnup and fluence distributions. [[Ch 05 — Fabrication of Fuel Compacts]] points to the AGR-1 irradiation results, and [[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] describes the capsule but not its as-run neutronics.
- **Ch 11 (Particle Modeling)** and **Ch 12 (Fission Product Transport Modeling)** of this same document, pp.106–143, not yet ingested — Ch 12.6 covers a prismatic HTR-GT example including temperature maps, which may carry the intra-element gradient treatment.
- An ATR irradiation position characterisation, for the spectrum in the large B positions specifically.

---

## Sources

- [[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] · [[Ch 05 — Fabrication of Fuel Compacts]] · [[Ch 08 — Fuel Failure Mechanisms]] · [[Ch 01 — Introduction]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
- Concept pages: [[Fuel Qualification Irradiation Testing]], [[Fuel Quality Control and Characterization]]
