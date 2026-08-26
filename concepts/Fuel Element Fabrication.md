---
type: concept
title: Fuel Element Fabrication
status: draft
sources: 1
tags: [fabrication, compacts, spheres, overcoating, packing-fraction, graphite-matrix]
updated: 2026-08-25
---

# Fuel Element Fabrication

**In one line** — Getting coated particles into a fuel element means embedding them in a graphite matrix and consolidating it without breaking them, which four documented processes solve differently while agreeing on the matrix itself.

## The two forms

**Compact** — cylindrical, roughly 13 mm diameter × 51 mm long, with approximately 3200 loaded into a hexagonal graphite block ([[Ch 01 — Introduction]] pp.15, 18). The HTTR (High Temperature Engineering Test Reactor) variant is annular, held in a graphite sleeve as a fuel rod that drops into a bored hole — the pin-in-block arrangement ([[Ch 05 — Fabrication of Fuel Compacts]] p.47).

**Sphere** — 50 mm fuelled zone inside a 5 mm fuel-free shell, 60 mm overall ([[Ch 03 — Manufacture of Spherical Fuels]] p.34).

## What all four processes share

**Matrix formulation.** 64% natural graphite, 16% electro- or synthetic graphite, 20% phenolic or thermosetting resin by weight — stated independently for spheres ([[Ch 03 — Manufacture of Spherical Fuels]] p.36), Japanese compacts ([[Ch 05 — Fabrication of Fuel Compacts]] p.48) and US compacts (p.52). The reasoning is only given in the US section: natural graphite mills and re-forms into macroscopically isotropic matter and contributes compressibility, synthetic graphite contributes toughness, and mixing them means less binder is needed (p.52).

**Two-stage heat treatment.** Carbonise the resin binder for strength, then anneal under vacuum to remove impurities.

**Impurity control as a fuel-integrity requirement.** Graphite and resin are screened for species that could attack the OPyC (outer pyrocarbon) or diffuse into the SiC and corrode it ([[Ch 05 — Fabrication of Fuel Compacts]] p.52) — not a neutronic requirement but a coating-protection one.

## Where they diverge

| | Spheres | Japanese | French (CERCA) | US (AGR) |
|---|---|---|---|---|
| Overcoating | yes, ~200 µm | yes, ~200 µm | **none** | yes, centrifugal |
| Pressing | quasi-isostatic, room temp, rubber moulds, 5 → ~300 MPa | warm-pressed, metallic dies | warm-pressed, metallic dies | warm-pressed, metallic dies, methanol-soaked first |
| Carbonisation | 800 °C, argon | 800 °C, nitrogen | 200 °C polymerise, then 800 °C nitrogen | 950 °C, helium, 1 h |
| Final anneal | 1900–1950 °C, vacuum, 1 h | 1800 °C, vacuum | 1800 °C, vacuum | 1800 °C, vacuum, 1 h |

Sources: [[Ch 03 — Manufacture of Spherical Fuels]] pp.36–38; [[Ch 05 — Fabrication of Fuel Compacts]] pp.48–55.

The French process is the instructive outlier: resinated graphite granulates and **bare** TRISO particles are metered into the die together to reach the specified packing fraction (p.50). Overcoating is therefore a common technique, not a requirement of compact fabrication.

## Overcoating does two jobs

The stated purpose is preventing particle-to-particle contact, which would crack coating layers during consolidation ([[Ch 03 — Manufacture of Spherical Fuels]] p.37). The second job is quantitative: **overcoat thickness sets the packing fraction.** The Japanese 200 µm overcoat is specified to achieve 30% TRISO-particle-to-total-compact volume after pressing and heat treatment ([[Ch 05 — Fabrication of Fuel Compacts]] p.48), and the US process states the requirement generally — the overcoat must give "the proper outer diameter required to meet the fuel particle packing fraction requirement, after compacting, pressing, and heat treatment" (p.54).

Packing fraction in turn sets power per particle and thermal gradient across the particle, which is what drives [[Kernel Migration]].

The ORNL (Oak Ridge National Laboratory) centrifugal method, developed for the smaller UCO particles, is an engineering answer to a ratio problem: pre-mix particles and matrix in a set ratio so no excess matrix can clump, spin the mixture against the wall so the ratio holds during processing, then spray it off the wall through a methanol mist so adhesion happens at the moment the ratio is correct — ensuring matrix bonds to the OPyC rather than to itself (pp.53–54).

## Consolidation without breakage

The two consolidation routes are mechanically very different — quasi-isostatic pressing at room temperature to about 300 MPa for spheres, against warm pressing in dies at what the US section calls a "low pressure compacting process" ([[Ch 05 — Fabrication of Fuel Compacts]] p.56).

Only the compact route reports a breakage figure, and it is clean: **no exposed kernels were detected in any AGR-1 compact lot**, with 95% upper limits between 3.1 × 10⁻⁵ and 1.4 × 10⁻⁴ (p.56). The US Advanced Gas Reactor (AGR) methanol soak exists to serve this — saturating overcoated particles before pressing lets the overcoat flow into inter-particle voids instead of leaving the pitted surface that unsoaked particles produce (pp.54–56).

## Open questions

- Why the sphere anneal runs 100–150 °C hotter than every compact anneal, when both are described as impurity removal, is not addressed in either chapter.
- Packing fraction is quoted only for HTTR (30%). No figure is given for the French or US compacts, or for spheres.
- No particle-breakage figure exists for the 300 MPa sphere route or for the French no-overcoat route.

## Sources

- [[Ch 03 — Manufacture of Spherical Fuels]] · [[Ch 05 — Fabrication of Fuel Compacts]] · [[Ch 01 — Introduction]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
