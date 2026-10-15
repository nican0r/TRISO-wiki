---
type: source-chapter
title: Ch 12 — Fission Product Transport Modeling
source: High Temperature Gas Cooled Reactor Fuels and Materials
pages: 110-143
ingested: 2026-10-14
status: draft
tags: [fission-product-release, modeling, diffusion, source-term, prismatic, temperature-distribution, uncertainty]
updated: 2026-10-14
---

# Ch 12 — Fission Product Transport Modeling

Part of [[High Temperature Gas Cooled Reactor Fuels and Materials]] · pp.110–143

**Gist** — How a plant's radiological source term is calculated from the fuel outward: three independent release sources, diffusion through each successive material, sorption at the graphite–helium boundary, and uncertainty treatment. Two worked examples close it — a pebble-bed (PBMR) case and a prismatic (HTR-GT) case, the latter carrying temperature distributions within the compact and the graphite block. The longest chapter in the document and the one that sets what a design has to predict rather than measure.

## Three release sources, three path lengths

Release is modelled from three independent origins, each with a different distance to the coolant (p.114, Fig. 62):

1. **Uranium and thorium contamination** in the OPyC (outer pyrocarbon) and in the matrix — fission products need only cross the OPyC and matrix.
2. **Defective and failed particles** — no coating resistance assumed; products start in the matrix.
3. **Intact particles** — everything must cross all coatings. For gases this is effectively a closed door: the diffusion coefficient for gaseous fission products through PyC is ~2 × 10⁻¹⁸ m²/s, so PyC "can be considered impervious to fission gases" and the gaseous source term from intact particles is ignored (p.128).

Recoil is treated separately and is temperature-independent, a geometric fraction set by recoil range against kernel radius (Eq. 12.4, p.116).

The metals are the problem, not the gases — the same conclusion [[Fission Product Retention]] reaches from measurement, here as a modelling assumption.

## Diffusion is the model, with a stated caveat

Metallic transport is modelled as transient Fickian diffusion through each material in series, solved numerically with continuity of concentration and flux at interfaces (pp.116–122). The chapter says plainly that the real transport of Cs, Ag, Sr and Eu "is undoubtedly much more complicated than classical Fickian diffusion", and that kernel speciation shifts with burnup — especially in UCO as the oxygen potential changes — altering the mobility of oxide formers. Silver is the exception, staying elemental across compositions and burnups of interest (p.116).

Diffusion coefficients for Cs, Sr and Ag in UO₂, buffer, PyC, SiC and matrix graphite are tabulated as Arrhenius pairs (Table 15, pp.122–123). **The converted table is badly mangled; read it from the PDF before quoting any value.**

At the graphite–helium boundary the transfer is modelled by sorption isotherms rather than diffusion, with an example for caesium on H-451 graphite (Fig. 77, p.137).

## The prismatic example

The HTR-GT case (§12.6, pp.135–143) is the one that bears on prismatic designs:

- **Assumed defect populations**: particles with a failed SiC layer at 5 × 10⁻⁴ of the population, and fully exposed kernels at 2 × 10⁻⁵ (p.136). Both are inputs taken from a reference, not results.
- **Temperature maps**, from AREVA NP analyses: across a TRISO particle (Fig. 80, p.140), through the fuel compact and hexagonal block (Fig. 81, p.141), and against core height for helium, compacts and graphite (Fig. 82, p.141). The block map's legend gives a local range of 761–1326 K within one column — read off the figure.
- A one-dimensional finite-difference code solves the diffusion equation in three geometries at once: Cartesian for the block, spherical for the particle, cylindrical for the compact (Eqs. 12.8a–c, p.142).
- **Result**: ¹³⁷Cs released to the coolant after 450 days, 11.25 × 10¹² Bq (AREVA NP) against 15.84 × 10¹² Bq (JAEA) using nearly the same hypotheses (Table 17, p.142) — a ~40 % spread between two analyses of one design.

![[tecdoc1645-p141-fig82-temperature-vs-core-height.jpeg]]
*Fig. 82, p.141 — helium, compact and graphite temperature against core height, HTR-GT. Compacts run hottest, roughly 780 K at the inlet to about 1300 K, with the sawtooth marking block boundaries.*

## Uncertainty is treated explicitly

Named uncertain inputs: diffusion coefficients derived from irradiation experiments; the fuel specification's limits on uncontained uranium and thorium contamination; the sorption isotherm, varied by a factor of four in partial pressure; thermal-hydraulic properties feeding fuel temperature; and the statistical limits of the German irradiation set, which cannot exclude growing failure fractions above 5 % FIMA (fissions per initial metal atom); plus cross sections and fluxes (pp.133–134).

Three methods are offered, with their trade-offs stated: **stacked** (every parameter at its design value — most conservative, easiest to defend), **Monte Carlo** (sample distributions, take the upper 95 % confidence limit — quick, good for comparing core designs), and **least squares** (parameters evaluated separately then combined — most informative, most expensive) (p.134).

## Data extracted

| Quantity | Value | Conditions | Page |
|---|---|---|---|
| Gas diffusion coefficient in PyC | ~2 × 10⁻¹⁸ m²/s | basis for ignoring gas release from intact particles | p.128 |
| Failed-SiC particle fraction (assumed) | 5 × 10⁻⁴ | HTR-GT modelling input | p.136 |
| Exposed-kernel fraction (assumed) | 2 × 10⁻⁵ | same | p.136 |
| Uncontained uranium fraction, spec limit | 6 × 10⁻⁵ | PBMR fuel specification | p.133 |
| Derived upper limits | 5.6 × 10⁻⁵ failed particles; 4.0 × 10⁻⁶ U contamination; 6.0 × 10⁻⁶ Th (effective) | from that spec | pp.133–134 |
| In-block temperature range | 761–1326 K | HTR-GT graphite column, read off Fig. 81 | p.141 |
| ¹³⁷Cs released to coolant, 450 days | 11.25 × 10¹² Bq (AREVA NP) vs 15.84 × 10¹² (JAEA) | HTR-GT, near-identical hypotheses | p.142 |
| Fission rate, 600 MWth plant | ~2 × 10¹⁹ fissions/s; ~5 × 10²⁸ fission product atoms over 40 years | — | p.110 |

## What this changes in the wiki

- Supplies the intra-element thermal gradient that [[How are fuel compacts irradiated in qualification testing]] records as missing on the temperature side, while leaving the flux and burnup side open.
- Gives [[Fission Product Retention]] the modelling frame — three sources, metals not gases — behind its measured figures.
- Records the defect fractions a prismatic source-term calculation assumes, against the measured ones on [[Fuel Quality Control and Characterization]].

## Open questions raised

- Table 15's diffusion coefficients are the quantitative core of the chapter and did not survive conversion; they need reading from the PDF before use.
- The 40 % spread between two analyses of the same design, using the same hypotheses, is not explained in the chapter.
- The defect fractions used are assumptions from a reference, more than an order of magnitude above the modern as-manufactured defect fraction of < 10⁻⁵ given in [[Ch 02 — Manufacture of TRISO Coated Particles]] p.23; the chapter does not reconcile them.
