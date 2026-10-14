---
type: concept
title: TRISO Fuel Failure Mechanisms
status: draft
sources: 2
tags: [triso, fuel-performance, failure-mechanisms, fabrication]
updated: 2026-09-08
---

# TRISO Fuel Failure Mechanisms

**In one line** — Eleven documented ways a coated particle can fail or stop retaining fission products, of which most are governed by fabrication quality rather than by the operating conditions the particle was designed for.

## Mechanism

The eleven documented modes fall into three groups by driver, each detailed on [[Ch 08 — Fuel Failure Mechanisms]]:

| Group | Modes | What drives them |
|---|---|---|
| Stress-driven structural failure | overpressure; irradiation-induced IPyC (inner pyrocarbon) cracking; IPyC/SiC debonding; kernel-coating mechanical interaction | fission gas and CO pressure against pyrocarbon shrinkage, creep and interface strength |
| Chemical degradation | fission product attack (chiefly palladium); caesium attack above 1500 °C; CO corrosion of SiC; kernel migration | kernel chemistry, temperature gradient, time at temperature |
| Loss of retention without breakage | diffusion through intact layers; induced SiC permeability; PyC thermal creep; SiC thermal decomposition | temperature, burnup, fluence |

The chapter's own conclusion inverts the intuitive picture: in well-made fuel none of these is expected to be significant, and release is dominated instead by as-manufactured defects and by heavy metal contamination outside the SiC layer (p.77). These are largely a manufacturing quality problem wearing the costume of a physics problem.

One concrete as-manufactured defect, from a different source: **soot inclusion**, carbon soot swept into the bed and encapsulated within a coating layer during CVD (chemical vapor deposition). It is a fabrication-stage flaw rather than a thirteenth in-service mechanism — see [[TRISO Coating Reactor Design]].

## A twelfth route, from outside the particle

The eleven mechanisms above all originate inside the particle or in its coating. [[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] records one that does not: **transition metals attack SiC.** Metal sleeves have historically not been permitted to touch fuel elements in irradiation capsules because Fe, Cr and Ni were observed to attack the SiC layer; transport and corrosion rates remain unquantified, and 2–3 mm of graphite between fuel and any metallic component is the accepted mitigation (p.64).

This is a test-rig constraint in context, but the chemistry is not confined to test rigs — it bears on any in-core design in which metallic components sit near fuel, and it is part of why [[Ch 06 — In-Core Structural Materials and Components]] names ceramic composites rather than metals for control rod guide tubes and sheathing (p.61).

## How the dominant cause is measured

If as-manufactured defects dominate release, the defect fraction is the safety-relevant number, and it comes from burn-leach testing: particles burned to the SiC layer, residue leached in nitric acid, uranium assayed, defect count inferred from uranium per particle ([[Ch 04 — QA-QC and Characterization]] p.43). The test is destructive, so every quoted figure is a statistical statement about a lot. See [[Fuel Quality Control and Characterization]].

## Mitigations available at the particle level

- **UCO kernels** remove the CO chain that drives overpressure, kernel migration and SiC corrosion ([[Ch 01 — Introduction]] p.22). See [[UCO vs UO2 Kernels]].
- **UO₂\* particles** — a ZrC oxygen getter beneath the buffer — achieve the same objective by coating rather than kernel chemistry (p.22).
- **ZrC in place of SiC** is proposed specifically to minimise Pd attack, and its higher refractory properties could raise fuel temperature limits by roughly 200 °C; it requires significant development plus irradiation and accident simulation testing (p.23).

The fabrication parameters have a quantitative anchor too. SiC deposits at 0.2 µm/min against 5–10 µm/min for the pyrocarbon layers, at 1500 °C under hydrogen rather than 1250–1300 °C under argon (Table 2, [[Ch 02 — Manufacture of TRISO Coated Particles]] p.33) — see [[TRISO Coating Process]] for why the deposition parameters, rather than the design, decide whether a particle survives irradiation. The corresponding acceptance criteria — impermeable isotropic PyC, β-SiC above 3.19 Mg/m³ with few flaws, and PyC–SiC interfaces of sufficient strength (p.34) — map one to one onto the mechanisms above.

## Design implications for HTGRs

Prismatic geometry is penalised twice relative to pebble beds, on the same underlying quantities. [[Kernel Migration]] scales with thermal gradient, and prismatic cores run higher particle loadings and power densities. Fission product attack scales with time at temperature, and prismatic particles run hotter for longer ([[Ch 08 — Fuel Failure Mechanisms]] pp.73–74). Neither is a prohibition; both are arguments for tighter thermal design.

For irradiation testing, the chapter twice recommends limiting burnup or power acceleration to **no more than three times** the expected reactor condition, specifically to avoid inducing kernel migration and fission product attack that would not occur in service — false positives from over-accelerated tests (pp.73–74). [[Ch 07 — TRISO-Coated Particle Fuel Irradiations]] shows the recommendation being followed (ATR (Advanced Test Reactor) and HFR-Petten, both under 3×) and describes what happened when it was not, including US irradiations accelerated up to 10× (pp.61–63). It also complicates the fabrication story: the 1000× German/US gap in end-of-life fission gas release is confounded with that difference in acceleration. See [[Fuel Qualification Irradiation Testing]].

## Sources

- [[Ch 08 — Fuel Failure Mechanisms]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
- [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]]
