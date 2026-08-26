---
type: source-chapter
title: Ch 07 — TRISO-Coated Particle Fuel Irradiations
source: High Temperature Gas Cooled Reactor Fuels and Materials
pages: 61-70
ingested: 2026-08-25
status: draft
tags: [irradiation-testing, qualification, acceleration, release-to-birth, instrumentation]
updated: 2026-08-25
---

# Ch 07 — TRISO-Coated Particle Fuel Irradiations

Part of [[High Temperature Gas Cooled Reactor Fuels and Materials]] · pp.61–70

**Gist** — How TRISO fuel is qualified by irradiation: choosing a test position in a water-moderated reactor that approximates a gas reactor spectrum without over-accelerating, designing a capsule whose temperature can be controlled and inferred without touching the fuel, irradiating enough particles for the statistics to mean anything, and monitoring fission gas release continuously so that the *timing* of release identifies what failed. It is a chapter about experimental method, and its most useful content is the set of constraints that method operates under.

**Not what Day 9 needs.** This chapter is about testing fuel, not operating a reactor. Its "gas control system" controls capsule temperature, not reactor power. There is nothing here on approach to critical, control rod worth, SCRAM, or reactor kinetics — that material is not in this document at all.

## Acceleration is the central experimental compromise

Design service burnup and fast fluence take roughly **1095 days (3 years)** to accumulate in service; irradiation tests compress that by factors of **two to ten** (p.61).

The compromise is that acceleration itself causes failures. [[Ch 08 — Fuel Failure Mechanisms]] recommends acceleration no greater than three times expected conditions, specifically so that kernel migration and fission product attack — both driven by thermal gradient and time at temperature — do not produce false positives (pp.73–74). This chapter records what happened when that was and was not observed:

*FRJ is the Jülich research reactor; HFIR, the High Flux Isotope Reactor at Oak Ridge National Laboratory (ORNL); NGNP, the US Next Generation Nuclear Plant.*

| Facility | Problem or result | Page |
|---|---|---|
| ATR large B positions (38 mm dia.), used for the US AGR programme | acceleration **< 3×** relative to NGNP — fast enough to be practical, slow enough "to avoid possible premature particle fuel failures similar to those experienced in past highly accelerated particle fuel tests" | p.62 |
| HFR-Petten | successful irradiations at **< 3×** | p.63 |
| FRJ (Jülich) | spectrum **too thermalised** — fuel received too little fast fluence to be prototypic of an HTGR | p.63 |
| HFIR (ORNL) | thermal flux **too high** — significant burnup acceleration during irradiation | p.63 |

Those two figures — a 3× ceiling and a roughly two-year irradiation against 1095 days of service exposure — only reconcile once the endpoints are distinguished: 1095 days is time to *design service* burnup and fluence, the two-year figure is time to *full* burnup under a high-burnup goal, and at 3× two years delivers about twice service exposure. Derived rather than stated; see [[How are fuel compacts irradiated in qualification testing]]. `#inferred`

Almost all material test reactors are water cooled and moderated, so the test position must be chosen for a spectrum most prototypic of a gas reactor, adequate flux to finish in reasonable time, and a fast-to-thermal ratio that does not over-accelerate. Neutron absorbers can suppress thermal flux and moderate heat generation where space allows (p.62). Full burnup in LEU (low-enriched uranium) TRISO commonly takes about two years even so (p.63).

## The German/US performance gap, quantified

**German fuel exhibits about a factor of 1000 lower end-of-life fission gas release-to-birth ratio than US fuel**, across a broad range of temperature, burnup and fluence (Fig. 29, p.62).

> [!warning] Two explanations are offered and never separated
> The same paragraph notes that the programmes differed in two ways at once: the German programme concentrated on a single fuel type (UO₂ TRISO) from 1980 onward while the US examined many particle variants, **and** German acceleration factors were mostly under three while US factors reached ten (pp.61–62). [[Ch 08 — Fuel Failure Mechanisms]] attributes the performance difference to fabrication parameters — coating gas concentration, coating rate, matrix form. This chapter states that high acceleration itself causes premature failures. Both can be true, and the document does not attempt to apportion the 1000× gap between them. Treat "German fuel is a factor of 1000 better" as confounded by test conditions unless a source separates the two.
> `#conflict`

## Measuring temperature without touching the fuel

Thermocouples cannot be attached to the fuel, so **fuel temperature is always calculated**, from thermocouples placed elsewhere in the capsule and from three-dimensional physics and thermal analysis — now expected in capsule design (p.63).

The prohibition is chemical, not practical: **transition metals attack SiC.** Metal sleeves have historically not been allowed to touch fuel elements because Fe, Cr and Ni were observed to attack the SiC layer. Transport and corrosion rates are unknown quantitatively, but **2–3 mm of graphite between the fuel element and any metallic component has been found effective** at minimising interaction (p.64).

Graphite is therefore doing double duty in the capsule: encapsulating the fuel in a graphite sleeve or cup and inserting thermocouples into the graphite works well because graphite's high conductivity minimises the effect of irradiation-induced dimensional change on the calculated fuel temperature (p.64).

### Instrumentation limits

They are real and acknowledged. Commercial thermocouples (types K, N, C) have been used extensively, but with fuel temperatures pushed toward **1250 °C**, existing technologies may not survive a two-year qualification irradiation because of drift and de-calibration in-pile; past experiments had high uncertainties in element centreline temperature. INL (Idaho National Laboratory) developed refractory high-temperature thermocouples for the US Advanced Gas Reactor (AGR) programme. Redundancy is recommended given low reliability at high temperature in neutron fields, with melt wires as an inexpensive backup — though a melt wire records only that a peak temperature was reached, not when (p.64).

### Fluence wires

These measure thermal and fast fluence. Quartz encapsulation is not recommended at high temperature and high fluence; neutronically transparent refractories such as vanadium are preferred, filled with inert gas to prevent oxygen interaction. Fission chambers and self-powered neutron detectors, common elsewhere, may not be practical in space-constrained HTGR fuel capsules (p.65).

## Temperature control by gas blending

Each capsule sits inside an insulating gas jacket between the heat source — fission plus gamma heating of capsule materials — and the relatively cold test reactor coolant. Temperature is controlled by **varying the mixture ratio of two gases of differing thermal conductivity**, blended automatically by computer-controlled mass flow controllers on thermocouple feedback, which compensates for falling fission heat and changing thermal conductivity as burnup accumulates (pp.63, 66).

Helium and argon give a wide control band, **but argon cannot be used where on-line fission product monitoring is in play**: activated ⁴¹Ar (t½ = 1.8 h) reduces the detectability of the monitoring system. Helium and neon are used instead (p.66).

Practical safeguards the chapter records: automatic gas verification by thermal conductivity analyser, to prevent an insulator gas being connected to the conductor gas port and causing an uncontrollable temperature excursion; impurity cleanup for gas purity; tubing sized to minimise transit time both to the capsule and onward to the fission product monitors; alarms for temperature excursions and valve position errors; automatic helium purge to cool a capsule if temperature measurement or control is lost, with manual purge capability at the blending panel against computer failure; and separate continuous flow to each capsule (pp.66–67).

## How many particles the statistics demand

Binomial statistics set the sample size. **To demonstrate a failure probability of 2 × 10⁻⁵ at 95% confidence requires irradiating approximately 200,000 particles, assuming none fail** (Fig. 33, p.67).

That number explains the shape of the evidence elsewhere in this document — [[Ch 09 — Accident Testing]] reports 221,840 particles heated at 1600 °C with zero failures, giving a 95% upper limit of 1.35 × 10⁻⁵ (p.91), and [[Ch 05 — Fabrication of Fuel Compacts]] reports AGR-1 defect fractions as 95% upper limits over lots of ~120,000 particles. Demonstrating that TRISO is as good as it is claimed to be requires counting particles in the hundreds of thousands, every time.

## Release-to-birth ratio, and why timing identifies the culprit

Sweep gas carries released fission gases to a fission product monitoring system. From the on-line concentration a **release-to-birth ratio (R/B)** is computed — the chapter calls it "a key parameter used in reactor fuel behavior studies" (p.69).

Its diagnostic power is temporal, not absolute:

- **Release from the start of the irradiation indicates initially failed particles, or contamination outside the SiC layer.**
- **Release appearing later indicates *in situ* particle failure.**

Failure timing can then be correlated with temperature, burnup and fluence, and combined with post-irradiation examination to identify the responsible mechanism (p.69). This is the on-line, non-destructive counterpart to burn-leach testing in [[Ch 04 — QA-QC and Characterization]], and it is the measurement that lets [[Ch 08 — Fuel Failure Mechanisms]] and [[Ch 09 — Accident Testing]] attribute release to as-manufactured defects rather than to service.

Monitoring practice (pp.67–69): on-line gross gamma monitoring catches dynamic failures through their instantaneous release, using sodium iodide scintillators in preference to ion chambers because greater sensitivity allows more standoff from the gas line — which matters when fission gas daughters plate out in the viewed region. Weekly grab samples give isotopic detail (⁸⁵ᵐKr, ⁸⁷Kr, ⁸⁸Kr, ¹³¹ᵐXe, ¹³³Xe, ¹³⁵Xe). On-line gamma spectroscopy on high-purity germanium (HPGe) is the most informative and most expensive option; transit time is minimised but held long enough (~2–3 min) for short-lived sweep-gas activation products to decay, which brings ⁸⁹Kr, ⁹⁰Kr, ¹³⁵ᵐXe, ¹³⁷Xe, ¹³⁸Xe and ¹³⁹Xe into range. Redundancy is recommended so one spectrometer failure does not cost a two-year experiment.

## Test capsule design

Multi-cell capsules — fuel tested in separate independent compartments under different temperature, burnup and fluence conditions — are described as offering "tremendous flexibility" and as actually saving time and money across a qualification programme (p.62). Current multi-capsule capability exists at IVV-2M (Russia), HFR-Petten (Europe) and the INL ATR (Advanced Test Reactor) (US).

## Figures kept

![[tecdoc1645-p62-fig29-rb-german-vs-us.jpeg]]
*Fig. 29, p.62 — end-of-life ⁸⁵ᵐKr release-to-birth ratio from historic German and US irradiations, the source of the factor-of-1000 gap.*

![[tecdoc1645-p67-fig33-failed-particle-statistics.jpeg]]
*Fig. 33, p.67 — sample size required as a function of failure fraction and number of failures expected. ~200,000 particles for 2 × 10⁻⁵ at 95% confidence with zero failures.*

![[tecdoc1645-p70-fig35-rb-after-failure.jpeg]]
*Fig. 35, p.70 — ⁸⁵ᵐKr R/B versus time after particle failure in the NPR-1A irradiation in the ATR.*

## Filed answers

- [[How are fuel compacts irradiated in qualification testing]] — the process end to end, and what this chapter does and does not establish about flux realism.

## Open questions raised

- Transport rates of Fe, Cr and Ni into fuel elements and their SiC corrosion rates are stated to be unknown (p.64), yet 2–3 mm of graphite is the accepted mitigation. On what basis was that thickness set?
- The 1000× German/US R/B gap is confounded by acceleration factor. Does the AGR-1 dataset — same fuel, acceleration under 3× — resolve it?
- Fuel temperatures are always calculated, never measured, and the chapter concedes past experiments had high centreline uncertainty. What uncertainty attaches to the 1600 °C and 1250 °C limits used everywhere else in this document?
