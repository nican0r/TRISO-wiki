---
type: synthesis
title: Overview
status: draft
sources: 11
tags: [triso, fabrication, cvd, spouted-bed, sic, synthesis, conflict]
updated: 2026-10-14
---

# Overview

The evolving synthesis. Eleven sources: one handbook covering coated particle fuel as a whole ([[High Temperature Gas Cooled Reactor Fuels and Materials]], 9 of 14 chapters), nine on how the particle is made and the machine that makes it, and one measuring what the finished particle did in reactor. This page follows that weighting — fabrication at the centre, fuel behaviour as the reason it matters. Page catalog: [[index]].

## Why the coater carries the safety case

A core holds more than 10⁹ coated particles ([[Ch 01 — Introduction]] p.19) and process control holds the defective fraction below 10⁻⁵ ([[Ch 02 — Manufacture of TRISO Coated Particles]] p.23) — of order 10⁴ defective particles per core by construction. In well-made fuel none of the eleven in-service failure mechanisms is expected to be significant; release is dominated instead by as-manufactured defects and heavy-metal contamination outside the SiC ([[Ch 08 — Fuel Failure Mechanisms]] p.77). [[TRISO Fuel Failure Mechanisms]] states the consequence: most of what looks like fuel physics is manufacturing quality in costume. Post-irradiation examination of AGR-1 fuel bears it out particle by particle — three defective-SiC particles in ~20,000, one of them carrying soot picked up in the coater, which held through three years of irradiation and failed at 1600 °C ([[PIE on Five Irradiated AGR-1 Compacts|Hunn et al. 2012]] pp.4, 22).

The weight therefore falls on deposition conditions rather than the drawing: pyrocarbon deposited at low gas concentration and low rate comes out anisotropic, shrinks under irradiation and cracks, and the IPyC/SiC bond strength turns on the same conditions ([[Ch 08 — Fuel Failure Mechanisms]] p.72). The reference recipe gives single setpoints and no tolerances ([[TRISO Coating Process]]).

## The process, in brief

All four layers are deposited in one uninterrupted sequence in a single spouted-bed CVD reactor ([[Ch 02 — Manufacture of TRISO Coated Particles]] pp.30, 33). SiC is the outlier: 25–50× slower than the pyrocarbon layers, ~200 °C hotter, under hydrogen rather than argon (p.33), and ~100 of the ~130 minutes ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.5). Particle diameter roughly doubles over a run and envelope density falls from 11 to 3 g/cm³ (p.2), so the bed never reaches steady state (p.4). Recipes from four lines, with their disagreements: [[TRISO Coating Parameters]]. Chemistry and parameter effects: [[SiC Layer Deposition]]. Equipment: [[TRISO Coating Reactor Design]]. Bed behaviour: [[Spouted Bed Hydrodynamics]], [[Fluidization]].

## What the sources agree on

- **SiC deposition temperature is the one well-mapped parameter.** In hydrogen, 1500–1600 °C gives stoichiometric, peak-density, β-SiC; below it free silicon, above it free carbon ([[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] pp.8, 12).
- **Argon shifts that window down**, to ~1200 °C at 90 % Ar (p.9), which is how ORNL meets the density specification at 1425 °C in 1:1 Ar–H₂ ([[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels|Jolly et al. 2016]] p.8).
- **Deposition rate is linear in MTS flux** across four coaters (Hu et al. 2025 p.15), and coating efficiency rises with batch charge — 41 % at 10 g to 97 % at 200 g (p.16).
- **The single central gas orifice is abandoned everywhere.** INL and INET reached multi-orifice designs independently, each fixing nozzle accretion ([[TRISO Coating Reactor Design]]).
- **Pyrocarbon density is set by deposition temperature and falls as it rises**, from 1.978 g/cm³ at 1170 °C to 1.746 at 1325 °C, which is what pins the IPyC layer near 1265 °C ([[PyC Layer Deposition]]).

## What is not established

- **Pyrocarbon anisotropy** — the property that governs shrinkage cracking — follows neither temperature nor gas fraction cleanly, and is the one pyrocarbon property still unmapped ([[PyC Layer Deposition]]).
- **H₂/MTS effects are contested** on stoichiometry, density and grain size alike; the ratio means little without the MTS flux and total flow beside it, which most studies omit (Hu et al. 2025 p.17).
- **Only one line publishes gas flows** ([[TRISO Coating Parameters#Gas flows (ORNL)]]).
- **Where temperature is measured differs by line**, and the gap is large: a 1600 °C control setpoint is a 1430–1500 °C bed, and a bed can swing 150 °C within one layer ([[Coater Process Monitoring]]). That reconciles the SiC temperatures across four lines and leaves each line's own offset unknown.
- **All hydrodynamic data are cold.** Air with glass or ZrO₂; nothing at coating temperature with dense kernels ([[Spouted Bed Hydrodynamics]]).

## The coater is run blind

No sight ports, internal thermocouples or optical pyrometry on the production line — smoke blocks optical access, a hanging probe cannot be positioned — so temperature is held by wall-offset thermocouples and gas flows, and the product is checked only after the run ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.5). Two in-run signals are proposed: bed pressure drop, already measured on hot coaters and tracking regime in cold flow ([[Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating|Zhou et al. 2005]] pp.2, 12), and external gamma densitometry, demonstrated cold at one height ([[Advancing the Fundamental Understanding and Scale-up of TRISO Fuel Coaters via Advanced Measurement and Computational Techniques|Biswas & Al-Dahhan 2012]] pp.5, 20); neither on a hot coater. Acceptance meanwhile rests on destructive post-run tests, chiefly burn-leach ([[Fuel Quality Control and Characterization]]).

## Nothing transfers for free

Setpoints need re-optimising at each retort diameter, because gas residence time and wall-area-to-flow both fall as the bed grows ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] pp.4, 6), and matched dimensionless groups reproduce global quantities between two cold beds while leaving radial profiles 15–46 % apart ([[Spouted Bed Hydrodynamics#Scale-up]]). Recipes do not transfer between kernels either: 29 development runs to move AGR-1 conditions onto ZrO₂ surrogates (Jolly et al. 2016 p.3).

## Open conflicts

| Disagreement | Where |
|---|---|
| Buffer deposition temperature, US ~1450 °C vs German/INET ~1255 °C | [[PyC Layer Deposition]] |
| Do surrogate kernels reproduce coater hydrodynamics | [[Coater Process Monitoring]] |
| Buffer deposition time and rate, ~4× spread | [[TRISO Coating Parameters#Conflicts]] |
| High-density SiC outside the "optimum" window | [[SiC Layer Deposition]] |
| Fine-grained SiC: better retention or more silver release | [[Silver Release]] |
| OPyC separates easily, or not at all on large kernels | [[TRISO Coating Process]] |
| Stable-spouting window, 1.1× vs 1.9× onset | [[Spouted Bed Hydrodynamics#Regimes]] |
| Kernels as Geldart Group B or D | [[Fluidization#Geldart classification]] |
| Predicted peak accident fuel temperature | [[TRISO Coating Reactor Design]] |

Two earlier disagreements have closed: the four SiC deposition temperatures and INL's own 1600 vs 1550 °C turned out to be control setpoints read against bed temperatures ([[TRISO Coating Parameters#Conflicts]]).

## What would move this furthest

The AGR-1 PIE final report and the per-lot fabrication reports (ORNL/TM-2006/019–022), which would turn [[AGR-1 Coating Variants]] from three compacts into the full variant comparison; the AGR-2 PIE final report; and hot-bed hydrodynamic measurement, still absent — the 400 Hz pressure records on one production coater ([[Coater Process Monitoring]]) are the closest thing in the wiki.
