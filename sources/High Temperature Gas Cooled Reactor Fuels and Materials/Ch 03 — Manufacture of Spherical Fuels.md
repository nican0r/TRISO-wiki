---
type: source-chapter
title: Ch 03 — Manufacture of Spherical Fuels
source: High Temperature Gas Cooled Reactor Fuels and Materials
pages: 34-38
ingested: 2026-08-25
status: draft
tags: [fabrication, graphite-matrix, overcoating, pebble-bed, compacts]
updated: 2026-08-25
---

# Ch 03 — Manufacture of Spherical Fuels

Part of [[High Temperature Gas Cooled Reactor Fuels and Materials]] · pp.34–38

**Gist** — The NUKEM process for pebble-bed fuel spheres: matrix powder preparation, particle overcoating, two-stage pressing, machining, carbonisation and high-temperature annealing. Geometrically this is pebble-bed-specific, but the matrix formulation and the overcoating principle are shared with prismatic compact fabrication — with three process divergences that matter, set out below.

## The sphere

A spherical fuel zone of **50 mm diameter** with TRISO particles homogeneously distributed in graphite matrix, surrounded by a fuel-free shell of matrix **5 mm thick** — 60 mm overall (p.34).

The matrix is carbonised organic binder plus nuclear-grade graphite, serving simultaneously as fission neutron moderator, heat transfer medium, and protection against external forces. Required properties (p.35): high density, high thermal conductivity, high mechanical strength, low thermal expansion, low anisotropy, low Young's modulus, good corrosion resistance, good dimensional stability under neutron irradiation, and low impurity concentration.

## Process

**Matrix powder** (p.36) — approximately **64% natural graphite, 16% electro-graphite, 20% phenolic resin binder**. Natural and electro-graphite are mixed 4:1 in a conical mixer; resin dissolved in alcohol is added in a kneading machine and homogenised; the paste is extruded through a punched screen into strings, cut, dried at ~100 °C, hammer-milled to the desired grain size, and homogenised.

**Overcoating** (p.37) — about **200 µm** of matrix material applied to TRISO particles in a rotating drum, with dry resinated matrix and solvent added simultaneously to maximise adherence and uniform thickness. Purpose: prevent direct particle-to-particle contact, which may crack the coating layers during sphere formation. Dried at ~80 °C, sieved to 1.1–1.5 mm, then run over an inclined vibrating table to remove oddly shaped, twin or non-spherical particles.

**Pressing** (pp.37–38) — quasi-isostatic, **at room temperature, in silicone rubber moulds**. Overcoated particles plus matrix powder are pre-pressed at approximately **5 MPa** to form the fuelled zone; that sphere is placed in the final mould between charges of matrix powder and pressed at about **300 MPa** to form the fuel-free shell.

**Machining and heat treatment** (p.38) — green spheres are lathed in two steps to final dimensions, carbonised at **800 °C in argon** to carbonise the phenolic binder for strength, then annealed under vacuum at **1900–1950 °C for one hour** to eliminate residual impurities in the matrix graphite.

## Does this carry over to prismatic compacts?

Checked against [[Ch 05 — Fabrication of Fuel Compacts]] (pp.47–57). **No contradictions** — but three divergences mean the sphere process cannot be treated as generic.

### What is shared

- **Matrix formulation is identical across all four processes.** 64% natural graphite / 16% electro- or synthetic graphite / 20% phenolic or thermosetting resin by weight, stated independently for spheres (p.36), the Japanese compact process (p.48) and the US Advanced Gas Reactor (AGR) fuel programme process (p.52).
- **Overcoat thickness of ~200 µm** is the same for spheres (p.37) and the Japanese compacts (p.48).
- **Overcoating serves the same purpose** — preventing particle-to-particle contact — and the sphere chapter's "solvent" is identified in Ch 5 as methanol, in the German-developed slow-rotating drum with methanol jets (p.52).
- **The two-stage heat treatment pattern** — carbonise the binder, then anneal under vacuum to remove impurities — is common to all four.

### Where they diverge

| | Spheres (Ch 3) | Compacts (Ch 5) |
|---|---|---|
| Pressing | quasi-isostatic, room temperature, silicone rubber moulds, 5 MPa then ~300 MPa | **warm-pressed in metallic dies** (Japanese, French, US); Ch 5 calls it a "low pressure compacting process" (p.56) |
| Carbonisation | 800 °C in argon | 800 °C in nitrogen (Japanese, French); **950 °C in helium** for one hour (US AGR) |
| Final anneal | **1900–1950 °C**, vacuum, 1 h | **1800 °C**, vacuum (all three compact processes) |

And one process omits overcoating entirely: **the French CERCA process uses no overcoating at all** — resinated graphite granulates and bare TRISO particles are fed into the die together to reach the specified packing fraction (p.50). So overcoating is a common practice, not a requirement of compact fabrication.

### Why the shared numbers are what they are

See [[Fuel Element Fabrication]] for the four processes side by side. Two points from [[Ch 05 — Fabrication of Fuel Compacts]] give the shared numbers their reason:

- The Japanese 200 µm overcoat is specified "in order to achieve a specified **30% TRISO fuel particle-to-total compact volume** after pressing and heat treatment" (p.48) — overcoat thickness is how packing fraction is controlled.
- The US process explains the 64/16 split: natural graphite is highly anisotropic but mills and re-forms into macroscopically isotropic matter and contributes compressibility; synthetic graphite is less anisotropic and contributes toughness; mixing them means **less binder is needed** (p.52). Graphite and resin candidates are also screened on impurity concentration specifically to avoid species that attack OPyC (outer pyrocarbon) or diffuse into SiC causing corrosion (p.52) — which is why the sphere chapter's bare requirement for "low concentration of impurities" is there.

## Figures kept

![[tecdoc1645-p35-fig13-spherical-fuel-element.jpeg]]
*Fig. 13, p.35 — spherical fuel element: 50 mm fuelled zone, 5 mm fuel-free shell.*

## Open questions raised

- Why does the sphere anneal run 100–150 °C hotter than every compact anneal? Both are described as impurity removal. Not addressed in either chapter.
- Room-temperature quasi-isostatic pressing at 300 MPa versus warm pressing at low pressure in dies are very different mechanical treatments for the same particle. Ch 5 reports no exposed kernels in any AGR-1 compact lot (p.56), so the compact route is evidently gentle enough — but no comparable particle-breakage figure is given for the 300 MPa sphere route.
