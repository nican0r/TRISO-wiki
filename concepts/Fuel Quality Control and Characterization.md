---
type: concept
title: Fuel Quality Control and Characterization
status: draft
sources: 1
tags: [qa-qc, metrology, defect-fraction, anisotropy, burn-leach]
updated: 2026-08-25
---

# Fuel Quality Control and Characterization

**In one line** — Every property that determines whether a TRISO particle survives irradiation has a corresponding measurement, and because the fuel's safety case rests on as-manufactured defect fractions rather than on in-service margins, those measurements are the safety case.

## Why measurement carries the weight here

[[Ch 08 — Fuel Failure Mechanisms]] concludes that in well-made fuel none of the eleven failure mechanisms are expected to be significant, and that release is instead dominated by as-manufactured defects and by heavy metal contamination outside the SiC layer (p.77). [[Ch 09 — Accident Testing]] then finds zero particle failures across 221,840 particles at 1600 °C (p.91). Both statements are claims about *manufacture*, and both are only as good as the metrology behind them.

## Each test maps to a failure mechanism

| Measured property | Method | Mechanism it guards against |
|---|---|---|
| PyC anisotropy | optical anisotropy factor (OAF); ORNL 2-MGEM ellipsometry | irradiation-induced shrinkage cracking of IPyC |
| PyC–SiC interface | inferred from fracture behaviour during density sampling | IPyC/SiC debonding |
| SiC integrity, uncontained uranium | burn-leach | defective SiC; tramp uranium release |
| Layer thickness and symmetry | X-ray micro-radiography; metallographic cross-section | overpressure margin; stress distribution |
| Layer density | density gradient column (sink-float); PSA for kernel and buffer | buffer void volume; SiC strength |
| Diameter, sphericity | particle size analyser; shadowscope | pressure-vessel strength |
| Thermal diffusivity | thermo-reflectance microscopy; laser flash for elements | in-reactor temperature prediction |
| Elastic modulus | nanoindentation | stress modelling of the coating stack |

All from [[Ch 04 — QA-QC and Characterization]] pp.39–47, Tables 3 and 4 (pp.40–41). IPyC (inner pyrocarbon) and OPyC are the inner and outer pyrocarbon layers; HTTR is Japan's High Temperature Engineering Test Reactor; ORNL is Oak Ridge National Laboratory.

## Anisotropy is the measurement that matters most

Dense pyrocarbon behaves like a polycrystalline material whose crystallites are individually anisotropic in thermal expansion and in fast-neutron-induced shrinkage, so macroscopic isotropy has to be achieved and verified ([[Ch 04 — QA-QC and Characterization]] p.41). Bulk graphite is characterised by X-ray diffraction as a Bacon Anisotropy Factor; coating layers are too small for that, so the optical anisotropy factor is used instead — the ratio of reflected intensities for light polarised in two perpendicular directions, relatable to the BAF and hence to expected fuel performance, and measurable as a profile *across* a layer on a polished section.

This is the parameter that separated German from US fuel ([[Ch 08 — Fuel Failure Mechanisms]] p.72), and it is measurable before irradiation. The failure mode was not undetectable; it was a specification problem. See [[TRISO Coating Process]].

## Burn-leach produces the number everything else rests on

A statistically significant sample is burned down to the SiC layers, the residue leached under reflux in nitric acid, the solution preconcentrated and analysed for uranium by fluorimetry, mass spectrometry or delayed neutron counting. With no defective SiC, the result is the **uncontained uranium content**; dividing total uranium by the expected contribution per particle gives the number of broken particles or defective SiC layers ([[Ch 04 — QA-QC and Characterization]] p.43).

It is destructive, so conformance is always a statistical statement about a lot, never a count of the particles actually loaded ([[Ch 05 — Fabrication of Fuel Compacts]] p.56).

## Quantitative anchors

| Quantity | Value | Source |
|---|---|---|
| Modern coated-particle defect fraction | < 10⁻⁵ | [[Ch 02 — Manufacture of TRISO Coated Particles]] p.23 |
| Tramp uranium + matrix contamination | ~10⁻⁵ of element uranium | [[Ch 01 — Introduction]] p.22 |
| AGR-1 (a US Advanced Gas Reactor programme irradiation) exposed kernel fraction | ≤ 3.1 × 10⁻⁵ to ≤ 1.4 × 10⁻⁴ (95% upper limits) | [[Ch 05 — Fabrication of Fuel Compacts]] p.56 |
| AGR-1 defective SiC before compacting | ≤ 2.5 × 10⁻⁵ to ≤ 9.5 × 10⁻⁵ (95% upper limits) | p.57 |
| HTTR 2nd core through-coatings defect fraction | 2 × 10⁻⁶ | p.49 |
| HTTR 2nd core SiC defective fraction | 1.7 × 10⁻⁴ | p.49 |
| Buffer-density error amplification from kernel density | ~6× | [[Ch 04 — QA-QC and Characterization]] p.42 |
| Thermal diffusivity precision | often better than 5% | p.45 |

Measured and upper-limit figures above are different statistics and are not directly comparable — see the callout on [[Ch 05 — Fabrication of Fuel Compacts]].

## The non-destructive complement

Burn-leach counts defects in a sacrificed sample before irradiation. **Release-to-birth ratio** watches the irradiated population continuously, and discriminates by timing: release from the start of an irradiation indicates initially failed particles or contamination outside the SiC, while release appearing later indicates *in situ* failure ([[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] p.69). The two together are what justify attributing release to manufacture rather than to service.

Sample size is set by binomial statistics, and it is large: **~200,000 particles irradiated with zero failures to demonstrate 2 × 10⁻⁵ at 95% confidence** (p.67). See [[Fuel Qualification Irradiation Testing]].

## Sampling, not testing, is the limiting error

The chapter is explicit that among the errors present in evaluating a material, "sampling [is] perhaps the most critical" ([[Ch 04 — QA-QC and Characterization]] p.39). Test methods are validated per material, uncertainty is quantified statistically, confidence levels are set so residual failure probability can be quantified and accepted in the design, and manufacturing is steered by trend analysis rather than by pass/fail on individual lots. The framework standard named is ASME NQA-1 (p.38).

A second-order version of the same point: the buffer density derivation amplifies the relative standard deviation of kernel density about sixfold, which sets a hard accuracy requirement on kernel density measurement that has nothing to do with kernels (p.42).

## Sources

- [[Ch 04 — QA-QC and Characterization]] · [[Ch 05 — Fabrication of Fuel Compacts]] · [[Ch 02 — Manufacture of TRISO Coated Particles]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
