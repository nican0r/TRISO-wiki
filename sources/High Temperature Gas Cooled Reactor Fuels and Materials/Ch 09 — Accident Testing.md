---
type: source-chapter
title: Ch 09 — Accident Testing
source: High Temperature Gas Cooled Reactor Fuels and Materials
pages: 78-93
ingested: 2026-08-25
status: draft
tags: [accident-testing, fission-product-release, kufa, triso, burnup]
updated: 2026-08-25
---

# Ch 09 — Accident Testing

Part of [[High Temperature Gas Cooled Reactor Fuels and Materials]] · pp.78–93

**Gist** — The empirical core of the passive safety argument. Post-irradiation heating tests in the Jülich cold finger apparatus (KÜFA) measured fission product release from irradiated fuel elements at 1600–1800 °C, simulating a depressurised loss of forced circulation. The result is a sharp threshold: across 221,840 particles heated at 1600 °C, zero failures; failures and release rise steeply at 1700 °C and above. The chapter also couples the allowable temperature limit to burnup, which is where its findings bear directly on design.

**All quantitative values below were read from the PDF pages, not the converted markdown** — marker misaligned several rows of Table 10 (see [[High Temperature Gas Cooled Reactor Fuels and Materials]]).

## Method

- The KÜFA (Cold Finger Apparatus) was developed at Forschungszentrum Jülich to test fission product release from whole fuel elements — pebbles or compacts — as well as individual particles, originally up to 1800 °C; the upgraded version at the Institute for Transuranium Elements, Karlsruhe, reaches 2000 °C (pp.78–79).
- The element sits on three pins inside a tantalum tube in a tantalum resistance furnace under flowing helium, with a W/Re thermocouple beside the specimen for measurement and furnace regulation (p.79).
- Fission gases are carried by the helium into cold traps where ⁸⁵Kr and ¹³³Xe are retained and measured continuously by on-line gamma spectrometry. A second trap confirms full retention in the first. ¹³³Xe is measurable only if the element's cooling period is under 4–8 weeks (p.80).
- Solid fission products are caught on a water-cooled cold finger with a replaceable condensation plate at 40–80 °C against a specimen at 1600–2000 °C, removable through an airlock without cooling the specimen and typically changed once or twice a day (pp.81–82).
- Gamma emitters (¹³⁷Cs, ¹³⁴Cs, ¹³¹I) are measured directly; ⁹⁰Sr, a beta emitter, requires chemical separation or ICP-MS on leached plates — the chapter notes the separation route "did not lead in the past to satisfactory results" (p.83).
- Detection floor: fractional releases down to 10⁻⁸ (p.83).

Relevant nuclides (Table 9, p.79): **¹³¹I**, 8-day half-life, "greatest significance for design and licensing"; **¹¹⁰ᵐAg**, 253 days, small inventory and short half-life, "important for maintenance."

## The temperature threshold

Peak core temperature in a depressurised loss of forced circulation reaches a maximum of **1620 °C in modern small HTRs** (p.78) — the design point sits deliberately just below the tested threshold.

| Condition | Particles | Failures | Failure level | 95% upper limit | Source |
|---|---|---|---|---|---|
| Isothermal 1600 °C, LEU UO₂ LTI TRISO | 221,840 | 0 | 0 | 1.35 × 10⁻⁵ | Table 12, p.91 |
| MODUL heatup to 1620 °C, 5 AVR GLE-3 elements | 82,000 | 5 | 6.10 × 10⁻⁵ | 1.28 × 10⁻⁴ | Table 12, p.91 |
| All heating tests below 1700 °C | 303,840 | 5 | 1.65 × 10⁻⁵ | 3.46 × 10⁻⁵ | Table 12, p.91 |

Selected KÜFA results (Table 10, pp.87–88; each element contains 16,400 particles):

| Element | Burnup %FIMA | Fast fluence 10²⁵ m⁻² | Test | Failures in heating | ⁸⁵Kr fractional release |
|---|---|---|---|---|---|
| AVR 71/22 | 3.5 | 0.9 | 1600 °C, 500 h | none | 4.0 × 10⁻⁷ |
| HFR-K3/1 | 7.7 | 3.9 | 1600 °C, 500 h | none | 1.8 × 10⁻⁶ |
| AVR 82/9 | 8.9 | 2.5 | 1600 °C, 500 h | none | 5.3 × 10⁻⁷ |
| AVR 74/11 | 6.2 | 1.6 | 1700 °C, 185 h | none | 3.0 × 10⁻⁵ |
| AVR 91/31 | 9.0 | 2.6 | 1700 °C, ~10 h | 18 | 1.2 × 10⁻³ |
| AVR 70/33 | 1.6 | 0.4 | 1800 °C, 175 h | 28 | 1.7 × 10⁻³ |
| FRJ2-K13/4 | 7.6 | 0.1 | 1800 °C, 100 h | 2 | 7.2 × 10⁻⁵ |
| HFR-K3/3 | 10.2 | 6.0 | 1800 °C, 100 h | ~12 | 6.5 × 10⁻⁴ |

Seven further tests at ITU Karlsruhe on LEU (low-enriched uranium) UO₂ TRISO spherical elements at 1600 °C, and one at 1720 °C, produced **zero failed particles** across elements of 16,400, 14,580 and 9,560 particles (Table 11, p.89).

> [!warning] Unexplained scatter at 1700 °C
> AVR 91/31 (9.0% FIMA) suffered 18 particle failures in roughly 10 hours at 1700 °C, while AVR 74/11 (6.2% FIMA) survived 185 hours at the same temperature with none. The chapter offers no explanation; burnup and fluence differ, but so does test duration in the opposite direction to the result. Treat 1700 °C as poorly characterised rather than as a graded step between 1600 and 1800 °C.
> `#conflict`

## Burnup couples to the temperature limit

If maximum burnup is kept strictly below **11% FIMA (fissions per initial metal atom)**, as is typical for present HTR designs, the allowable fuel temperature limit "may be higher than 1600 °C and has to be established with new experiments." If UO₂ TRISO is irradiated to **15% FIMA**, fuel temperature "must be rigorously limited to ≤1600 °C" (p.91).

The two are one decision, not two constraints. Note also that the highest-burnup element actually tested here is HFR-K3/3 at 10.2% FIMA — the 15% FIMA statement is an extrapolation from the mechanisms in [[Ch 08 — Fuel Failure Mechanisms]], not from data in this chapter.

## Retention behaviour

Bare UO₂ kernels retain almost nothing at 1600 °C: silver, xenon, iodine and cesium approach 100% release, with significant release beginning during the 30-hour heatup phase and nearly the whole inventory gone after 50–100 hours at temperature. Only ⁹⁰Sr is strongly retained in oxide kernels — and not in carbide kernels (p.83).

¹³¹I release separates fuel into three classes (p.84): exposed UO₂ kernels at ~100%; elements contaminated in the AVR by old failed fuel from the 1960s–70s at the 10⁻⁵ level; modern TRISO at 10⁻⁹ to 10⁻⁸.

At 1600 °C there is full retention for the first hundred hours or more, with silver the exception (p.89):

- **Cesium** is retained by kernel, SiC and the A3 matrix, with SiC strongest — but only with modern high-quality coatings. At 1800 °C neither kernel nor matrix delays release, and SiC becomes more permeable to most fission products.
- **Krypton** is always released later than cesium, held back additionally by dense intact pyrocarbon.
- **Strontium** is retained better than cesium by oxide kernels and the sphere matrix, so its release comes later, although SiC retention of Sr may be weaker.
- **Silver** is already released at irradiation temperatures above 1100 °C even through high-quality modern SiC, approaching 100% in accident-condition heating tests.

## Figures kept

![[tecdoc1645-p90-fig47-kr85-release.jpeg]]
*Fig. 47, p.90 — ⁸⁵Kr fractional release versus heating time, by temperature. The 1600 °C curves stay flat between 10⁻⁷ and 10⁻⁶ out to 500 h; 1700 °C sits near 3 × 10⁻⁵; 1800 °C between 10⁻⁴ and 2 × 10⁻³; 2100 °C reaches 3 × 10⁻² within 30 h. Roughly five orders of magnitude across a 500 °C span.*

![[tecdoc1645-p92-fig48-cs-release.jpeg]]
*Fig. 48, p.92 — cesium release during accident simulation tests on irradiated LEU UO₂ TRISO spherical elements, 1600–2000 °C.*

![[tecdoc1645-p93-fig49-kr85-vs-burnup.jpeg]]
*Fig. 49, p.93 — ⁸⁵Kr release at 1600 °C from compacts at 11–14% FIMA compared with spherical elements at 3.5–9% FIMA. The comparison underlying the burnup/temperature coupling above.*

## Open questions raised

- What establishes the temperature limit below 11% FIMA? The chapter says new experiments are required and does not cite any.
- The failure statistics are dominated by German spherical fuel elements. What is the equivalent tested population for prismatic compacts, and does Fig. 49's compact data at 11–14% FIMA constitute it?
- Silver release approaching 100% at accident temperatures is stated without a corresponding source-term or dose consequence. What does that imply for a direct-cycle machine where the turbine is the cold surface?
