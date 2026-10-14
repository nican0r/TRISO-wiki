---
type: question
title: Why does the inner PyC layer of a TRISO particle shrink during irradiation
status: draft
sources: 2
tags: [triso, ipyc, pyc, irradiation, dimensional-change, prestress]
asked: 2026-08-26
updated: 2026-08-26
---

# Why does the inner PyC layer of a TRISO particle shrink during irradiation?

**Short answer** — Under fast-neutron irradiation, pyrocarbon (PyC) shrinks in both the radial and tangential directions, then turns over to radial swelling at modest fluence (~2×10²⁵ n/m²), with the crossover point set by density, temperature and anisotropy ([[Ch 08 — Fuel Failure Mechanisms]] p.71). The wiki's ingested sources establish this behaviour and its structural role; they do not themselves give the crystallite-level mechanism behind it.

## What the wiki can answer

| Claim | Detail | Source |
|---|---|---|
| Macroscopic behaviour | PyC shrinks radially and tangentially at low fluence, then swells radially past ~2×10²⁵ n/m² | [[Ch 08 — Fuel Failure Mechanisms]] p.71 |
| Functional purpose | Where the IPyC (inner pyrocarbon) is well bonded to the SiC, its shrinkage puts the SiC into compression, offsetting the tensile load from fission gas and CO generated in the kernel | [[Ch 01 — Introduction]] p.18; [[Ch 08 — Fuel Failure Mechanisms]] p.71 |
| Failure mode when it goes wrong | Excess or uneven shrinkage strain (from insufficiently isotropic PyC, itself a consequence of too low a coating-gas concentration during deposition) puts the IPyC into tangential tension high enough to crack it, which stress-concentrates and can fail the SiC beneath | [[Ch 08 — Fuel Failure Mechanisms]] p.71 |
| Fabrication link | German fuel, coated at higher gas concentrations and coating rates than historical US fuel, does not show these shrinkage cracks; the US New Production Reactor–era irradiations did | [[Ch 08 — Fuel Failure Mechanisms]] p.71 |
| Layer design intent | Both PyC layers are specified as impermeable and isotropic partly *because* shrinkage behaviour is orientation-dependent | [[TRISO Particle Architecture]] |

See [[TRISO Particle Architecture]] for the full layer stack and [[TRISO Fuel Failure Mechanisms]] for where IPyC cracking sits among the eleven documented failure modes.

## What is missing

The ingested chapters state *that* PyC shrinks and swells, and quote the fluence at which the turnover happens, but do not explain *why* at the crystallite level — none of Ch 01 or Ch 08 discusses basal-plane structure, displacement damage, or the anisotropy metric (e.g. a Bacon Anisotropy Factor) that would quantify "how isotropic" a given deposition is. Ch 11 (Particle Modeling), pp.106–118 of this same source, not yet ingested, may carry a mechanistic or constitutive treatment.

[[Irradiation Damage in Nuclear Graphite]] documents an analogous shrink-then-swell, orientation-dependent response in *structural* graphite — but that page is explicit that matrix and block graphite are a different material from particle-coating PyC, so it should be read as a pattern match, not evidence for the coating layers.

**What would close the gap:** a source treating PyC/graphite radiation damage physics directly — crystallite reorientation and lattice contraction/expansion under fast-neutron displacement damage, and how deposition-condition-controlled anisotropy (BAF) maps to the onset fluence and magnitude of shrinkage. Chapter 11 of this document, or a dedicated pyrocarbon irradiation-damage paper, would fill it.

## Sources

- [[Ch 01 — Introduction]] · [[Ch 08 — Fuel Failure Mechanisms]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
- Concept pages: [[TRISO Particle Architecture]], [[TRISO Fuel Failure Mechanisms]], [[Irradiation Damage in Nuclear Graphite]]
