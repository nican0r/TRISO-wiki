---
type: concept
title: Irradiation Damage in Nuclear Graphite
status: draft
sources: 1
tags: [graphite, materials, irradiation, prismatic, qualification]
updated: 2026-08-25
---

# Irradiation Damage in Nuclear Graphite

**In one line** — Neutron irradiation changes the mechanical and physical properties of nuclear graphite substantially, in a way that depends on the specific coke source and manufacturing process, so damage behaviour cannot be transferred between grades and must be qualified for each one.

## Mechanism

Nuclear grade graphite experiences radiation-induced creep and dimensional change: it shrinks and then swells, at different rates along different crystallographic orientations ([[Ch 06 — In-Core Structural Materials and Components]] p.60). The anisotropy of the response follows from the anisotropy of the material, which in turn follows from how it was made — extruded needle-coke graphite has properties that differ parallel and perpendicular to the extrusion axis.

Because the response depends on source carbon and process rather than on composition alone, **irradiation damage testing is required for each reactor's specific graphite type prior to deployment** (p.60). This is a qualification requirement, not a design calculation: there is no way to compute the behaviour of a new grade from an old one's data.

## Where the damage accumulates

Fuel blocks and reflector blocks have different service lives and therefore different damage exposure. Hexagonal fuel blocks are inspected periodically during refuelling and may be reusable if the compacts can be removed easily. Unfuelled hexagonal blocks in the reflector region may be required to remain in service over many years, and accumulate higher damage as a result — they are replaced when required ([[Ch 06 — In-Core Structural Materials and Components]] p.60).

## Grade history

| Grade | Character | Use | Source |
|---|---|---|---|
| GLCC H-327 | extruded needle-coke, anisotropic; high density, good strength, good dimensional stability under irradiation | Fort St. Vrain initial core and first reload segment | p.60 |
| GLCC H-451 | more isotropic in structure | FSV subsequent reload segments; reference grade for fuel element and reflector components in later GA Modular Helium Reactor designs | p.60 |

H-327, from the Great Lakes Carbon Company (GLCC), was chosen at an early stage of development despite its anisotropy, on the strength of its density, strength and dimensional stability — the isotropic grade followed once available.

## Design implications for HTGRs

Graphite is simultaneously moderator, reflector, structural material and fuel host, which means irradiation-induced dimensional change is a structural problem as well as a neutronic one: the blocks that must stay aligned to keep coolant and control rod passages clear are the same blocks that are shrinking and swelling anisotropically.

The qualification requirement has a practical consequence beyond engineering. A new prismatic design cannot inherit H-451's irradiation database unless it uses H-451; the grade actually procured has to be tested. Both grades named here were manufactured by a company and process from the 1960s–70s.

Note also that the block dimensions themselves were historically constrained by graphite manufacture — FSV's width across flats was capped by the largest nuclear-grade graphite log obtainable at the time ([[Ch 06 — In-Core Structural Materials and Components]] p.59).

## Matrix graphite is a separate material with its own requirements

The graphite that binds TRISO particles into a fuel element is not the same material as the structural block graphite above. Its required properties are high density, high thermal conductivity, high mechanical strength, low thermal expansion, low anisotropy, low Young's modulus, good corrosion resistance, good dimensional stability under neutron irradiation, and low impurity concentration ([[Ch 03 — Manufacture of Spherical Fuels]] p.35).

Isotropy is manufactured rather than selected: natural graphite is highly anisotropic but mills and re-forms into macroscopically isotropic matter, and mixing it with less-anisotropic synthetic graphite yields compressibility from the former and toughness from the latter, so less binder is needed. The reference formulation is 64% natural graphite, 16% electro- or synthetic graphite, 20% phenolic resin by weight ([[Ch 03 — Manufacture of Spherical Fuels]] p.36).

The impurity requirement has a specific target: graphite and resin candidates are screened to avoid chemical species that may attack the outer pyrolytic carbon layer or diffuse into the SiC layer causing corrosion — so matrix purity is a fuel-integrity requirement, not a neutronic one.

## What this page does not yet cover

Graphite's thermal mass and its role in passive decay heat removal — the property most often cited for HTGR safety — is not covered by Ch 06 and is not yet in the wiki. It belongs to §1.1.2 (pp.12–19), not yet ingested.

## Sources

- [[Ch 06 — In-Core Structural Materials and Components]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
