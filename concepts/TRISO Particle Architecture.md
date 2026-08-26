---
type: concept
title: TRISO Particle Architecture
status: draft
sources: 1
tags: [triso, sic, pyc, buffer, particle-design]
updated: 2026-08-25
---

# TRISO Particle Architecture

**In one line** — A fuel kernel inside four coating layers, each of which performs several distinct functions, arranged so that the two pyrocarbon layers mechanically prestress the silicon carbide layer that does the actual containing.

## The layers and what each does

| Layer | Composition | Functions | Reference thickness |
|---|---|---|---|
| Kernel | UO₂, PuO₂, UCO; or thorium compounds | holds most fission products where they are produced | 350–600 µm dia. |
| Buffer | low-density PyC | sacrificial stop for energetic fission products, protecting IPyC from radiation damage; void volume for fission gas and kernel swelling | 95 µm |
| IPyC | dense isotropic PyC | barrier to gaseous fission product diffusion; barrier to chlorine gas generated during SiC deposition; keeps SiC in compression | 40 µm |
| SiC | β-SiC, cubic | main pressure boundary; retains metallic fission products; provides strength | 35 µm |
| OPyC | dense isotropic PyC | gaseous fission product barrier; reduces tensile stress on SiC; bonding surface for matrix or overcoating | 40 µm |

Functions from [[Ch 01 — Introduction]] p.22; thicknesses are the reference German LEU (low-enriched uranium) UO₂ design, [[Ch 02 — Manufacture of TRISO Coated Particles]] p.34. Overall particle diameter 500–1000 µm; typical enrichment 8–20%, set by power rating and safety considerations ([[Ch 01 — Introduction]] p.18).

## Why the layering works

The SiC is the containment, but it is not self-supporting against the pressure it must hold. The pyrocarbon layers on either side of it shrink under irradiation, and where they are well bonded that shrinkage supplies compressive prestress that offsets the tensile load from fission gas and CO inside ([[Ch 01 — Introduction]] p.18, [[Ch 08 — Fuel Failure Mechanisms]] p.71). The architecture is therefore only as good as the PyC's isotropy and the PyC–SiC interface strength — which is why the acceptance criteria in [[Ch 02 — Manufacture of TRISO Coated Particles]] p.34 name impermeable, isotropic PyC and "sufficient strength" at the interfaces, and why the failures in [[Ch 08 — Fuel Failure Mechanisms]] cluster on exactly those two properties.

The IPyC (inner pyrocarbon)'s chlorine function is a fabrication artefact made permanent: SiC is deposited by decomposing CH₃SiCl₃, which liberates HCl ([[Ch 02 — Manufacture of TRISO Coated Particles]] p.31), and the IPyC is what stops that reaching the kernel during coating.

## Measured layer properties

| Property | Inner PyC | Outer PyC | Buffer |
|---|---|---|---|
| Thermal diffusivity (mm²·s⁻¹) | 7.6 ± 3.2 | 3.6 ± 0.2 | 5.2 ± 0.5 dense parts; 4 homogenised |
| Young's modulus (GPa) | 18 ± 1.1 | 23 ± 1.4 | — |

[[Ch 04 — QA-QC and Characterization]] pp.46–47, at room temperature. The IPyC/OPyC (outer pyrocarbon) asymmetry is not a design choice: both layers are deposited identically, and the difference comes from the IPyC being annealed at 1500–1600 °C during SiC deposition. The stack is therefore not symmetric about the SiC even though the process treats it as if it were.

## BISO and why it was superseded

BISO was a porous buffer plus a dense pyrocarbon layer — two layers, no SiC. Both BISO and TRISO retain *gaseous* fission products, but BISO use was limited to low temperature and low burnup. Only TRISO retains *metallic* fission products at operational, transient and design accident temperatures, which is what made it the requirement for reduced release, extended burnup and higher fuel temperature. From the 1980s onward only TRISO has met modern HTGR fuel quality and performance requirements ([[Ch 01 — Introduction]] pp.19–20).

## Variants

- **UO₂\*** — dense PyC seal coat plus thin ZrC directly on the kernel, acting as an oxygen getter to limit CO and retard kernel migration; showed superior performance in HRB irradiations at 860–1210 °C and 19–29% FIMA (fissions per initial metal atom) ([[Ch 01 — Introduction]] p.22).
- **ZrC in place of SiC** — proposed to minimise Pd attack, with higher refractory properties potentially raising fuel temperature limits by ~200 °C; requires significant development and testing (p.23).

## The scale that makes quality control the whole problem

A typical HTGR core contains **more than 10⁹ coated particles** ([[Ch 01 — Introduction]] p.19), and the modern defect fraction is below 10⁻⁵ ([[Ch 02 — Manufacture of TRISO Coated Particles]] p.23). Even at that fraction, a core holds on the order of 10⁴ defective particles by construction — which is why [[Ch 09 — Accident Testing]] finds release dominated by as-manufactured defects rather than by any in-service mechanism.

## Sources

- [[Ch 01 — Introduction]] · [[Ch 02 — Manufacture of TRISO Coated Particles]] · [[Ch 08 — Fuel Failure Mechanisms]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
