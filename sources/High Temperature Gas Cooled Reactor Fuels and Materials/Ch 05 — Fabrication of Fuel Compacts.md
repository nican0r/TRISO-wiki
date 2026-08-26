---
type: source-chapter
title: Ch 05 — Fabrication of Fuel Compacts
source: High Temperature Gas Cooled Reactor Fuels and Materials
pages: 47-57
ingested: 2026-08-25
status: draft
tags: [compacts, prismatic, fabrication, overcoating, packing-fraction, agr-1]
updated: 2026-08-25
---

# Ch 05 — Fabrication of Fuel Compacts

Part of [[High Temperature Gas Cooled Reactor Fuels and Materials]] · pp.47–57

**Gist** — Three independent routes to the cylindrical fuel compact that goes into a prismatic block: Japanese, French and US. They agree on matrix formulation and on the carbonise-then-anneal sequence, and diverge on whether particles are overcoated at all. The US section is the most useful of the three because it explains the reasoning behind each step rather than only listing it, and it reports measured defect fractions for the AGR-1 test articles.

**This is the prismatic-relevant fabrication chapter.** [[Ch 03 — Manufacture of Spherical Fuels]] covers the pebble-bed equivalent and carries a comparison of the two.

## What a compact is

Cylindrical fuel forms placed into hexagonal graphite blocks (p.47). The Japanese case is the exception: HTTR (High Temperature Engineering Test Reactor) compacts are **annular**, contained in a graphite sleeve to form a fuel rod, and the rods are inserted into vertical holes bored in the block — the "pin-in-block" arrangement — which is why the Japanese process differs significantly from the French and US ones (p.47).

## The three processes

**Japanese (HTTR)** — pp.48–49. Overcoat TRISO particles with matrix material (16% electro-graphite, 64% natural graphite, 20% phenolic resin by weight, milled to specified grain size); warm-press in metallic dies to form annular compacts; carbonise at ~800 °C in nitrogen; heat-treat at 1800 °C under vacuum to remove impurities and de-gas.

**French (CERCA, subsidiary of AREVA NP)** — pp.50–51. **Uses no overcoating.** Resinated graphite powder is agglomerated into granulates by spraying alcohol onto a graphite/phenolic-resin mixture in a rotating drum, then dried and sieved. Dry granulates and *bare* TRISO particles are pushed together into the die to reach the specified packing fraction and a uniform particle distribution, then warm-pressed. Three heat treatments follow: polymerise the resin at 200 °C, carbonise and de-gas at 800 °C in nitrogen, harden the matrix and de-gas further at 1800 °C under vacuum. The chapter notes these temperatures are "directly linked with dimensional change behavior of the compacts, final physical properties, structure, and density of the graphite matrix" (p.51).

**US (US Advanced Gas Reactor (AGR) programme)** — pp.51–56. Overcoated particles, warm-pressed, with a methanol soaking step added; carbonise at **950 °C in helium for one hour**; anneal at 1800 °C under vacuum for one hour.

## Why the matrix is formulated the way it is

The US section supplies the reasoning that the other two omit (p.52). Natural graphite, synthetic graphite and thermosetting resin in **64 : 16 : 20 by weight**:

- Natural graphite is highly anisotropic, but mills to fine particle size and re-forms into macroscopically isotropic matter; it contributes **compressibility**.
- Synthetic graphite is less anisotropic and likewise mills and re-forms isotropically; it contributes **toughness**.
- Mixing the two means **less binder is needed**. The resin provides adhesion, helps the matrix stick to the TRISO particles during overcoating, and hardens into a solid during carbonisation.

Material selection is also a fuel-integrity decision: graphite and resin candidates must be screened on impurity concentration "to avoid chemical species that may attack the outer pyrolytic layer or diffuse into the SiC layer causing corrosion" (p.52).

## Overcoating, and what it controls

Overcoating prevents particle-to-particle contact during pressing. Beyond that, **overcoat thickness is how packing fraction is set**: the Japanese 200 µm overcoat is specified "in order to achieve a specified **30% TRISO fuel particle-to-total compact volume** after pressing and heat treatment processes" (p.48). The US section states the requirement generally — the method "must produce overcoated particles with the proper outer diameter required to meet the fuel particle packing fraction requirement, after compacting, pressing, and heat treatment" (p.54).

The German-developed method slowly rotated particles and matrix in a large steel drum with methanol jets misting the bed to help the matrix adhere (p.52). The AGR programme replaced it with **centrifugal overcoating**, developed at ORNL (Oak Ridge National Laboratory) for the smaller UCO particles (pp.53–54):

1. Particles and matrix are **pre-mixed in a set ratio**, so there is essentially no excess matrix that could form clumps.
2. The mixture is spun fast enough to pin it to the overcoater wall, which holds that ratio constant during the process.
3. An agitator arm sprays the mixture off the wall through a fine methanol mist delivered by syringe pump and ultrasonic atomiser.

The design intent is stated explicitly: delivering methanol at the moment the correct particle-to-matrix ratio is present ensures "the matrix will adhere to the OPyC (outer pyrocarbon) layers of the particles, and not to itself," and the mist coats particles evenly for uniform thickness (p.54). Particle count, overcoating material quantity, methanol volume, overcoater size, angle and speed must all be determined experimentally at each scale — bench, pilot and commercial (p.54).

## The methanol soak

The AGR compacting process adds a step absent from the Japanese and French routes: **overcoated particles are saturated with methanol before compacting, to improve material flow into open spaces under pressure** (p.54). The chapter illustrates the difference directly — a compact pressed from unsoaked particles shows pits and open spaces where the overcoat failed to flow into inter-particle voids, while a compact from methanol-saturated particles has a smooth, uniform surface because the overcoat was malleable enough to fill them (pp.55–56).

## Measured quality

Characterisation is partly destructive — leach-burn-leach destroys the compact and removes all uranium with acids — so only statistical sampling can establish conformance within a tolerance (p.56). See [[Ch 04 — QA-QC and Characterization]] for the method.

AGR-1 included a baseline with "German-type" TRISO coatings plus three variants differing in coating process parameters. 95% confidence upper limits on defect fractions per compact lot (Table 7, pp.56–57):

| | Baseline | Variant 1 | Variant 2 | Variant 3 |
|---|---|---|---|---|
| Exposed kernel fraction | ≤ 3.1 × 10⁻⁵ | ≤ 4.1 × 10⁻⁵ | ≤ 1.4 × 10⁻⁴ | ≤ 6.1 × 10⁻⁵ |
| Defective SiC before compacting | ≤ 2.5 × 10⁻⁵ (0/120688) | ≤ 4.0 × 10⁻⁵ (1/121117) | ≤ 9.5 × 10⁻⁵ (1/50265) | ≤ 4.0 × 10⁻⁵ (1/120660) |

Values in parentheses are measured defects over particles analysed. **No exposed kernels were detected in any compact lot**, and "there was no other indication that this low pressure compacting process will break particles" (p.56). No defective SiC was detected in Variants 1 and 3; the baseline showed two defective particles and Variant 2 showed one.

The Japanese process reports comparable quality on a commercial scale: for the second HTTR core loading, average through-coatings defect fraction 2 × 10⁻⁶ and SiC defective fraction 1.7 × 10⁻⁴, across first and second core loadings totalling 2 tonnes of uranium (p.49).

> [!warning] Conflicting defect-fraction figures are not comparable as printed
> The HTTR "SiC defective fraction 1.7 × 10⁻⁴" (p.49) is a measured average; the AGR-1 SiC figures (≤2.5–9.5 × 10⁻⁵) are 95% confidence *upper limits* from lots where at most one defect was found. They are different statistics and should not be read as one process outperforming the other.
> `#conflict`

## Figures kept

![[tecdoc1645-p47-fig18-httr-pin-in-block.jpeg]]
*Fig. 18, p.47 — pin-in-block prismatic fuel element for the HTTR: annular compacts in a graphite sleeve forming a fuel rod, inserted into the block.*

![[tecdoc1645-p51-fig21-matrix-impurities.jpeg]]
*Fig. 21, p.51 — impurity content in ppm of the natural graphite, synthetic graphite and thermosetting resin used for AGR-1 matrix.*

![[tecdoc1645-p54-fig25-centrifugal-overcoating.jpeg]]
*Fig. 25, p.54 — schematic of the ORNL centrifugal overcoating process, developed for the smaller UCO particles.*

![[tecdoc1645-p55-fig26-compact-without-methanol.jpeg]]
*Fig. 26, p.55 — compact surface pressed from particles not exposed to methanol: pits and open spaces where the overcoat did not flow into inter-particle voids.*

![[tecdoc1645-p56-fig27-compact-with-methanol.jpeg]]
*Fig. 27, p.56 — compact surface from methanol-saturated particles: complete compression, smooth and uniform.*

## Source-document defects

The in-text references in this chapter call the AGR-1 defect table "Table 3" twice; its caption is **Table 7** (p.56). The chapter also directs the reader to "Chapter 8 (TRISO-Coated Particle Fuel Irradiations)" for AGR-1 irradiation details, but that material is **Chapter 7** — see [[Ch 07 — TRISO-Coated Particle Fuel Irradiations]]; Chapter 8 is Fuel Failure Mechanisms. See the table-numbering warning on [[Ch 04 — QA-QC and Characterization]].

## Open questions raised

- The French process reaches packing fraction without overcoating, by metering granulates and bare particles into the die. What does that cost in particle breakage? No exposed-kernel figure is given for CERCA compacts.
- Packing fraction is stated as 30% for HTTR. No figure is given for the French or US compacts, and packing fraction bears directly on power per particle and hence on kernel migration ([[Kernel Migration]]).
