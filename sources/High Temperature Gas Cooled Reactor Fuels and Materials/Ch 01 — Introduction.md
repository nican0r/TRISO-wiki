---
type: source-chapter
title: Ch 01 — Introduction
source: High Temperature Gas Cooled Reactor Fuels and Materials
pages: 11-23
ingested: 2026-08-25
status: draft
tags: [htgr, triso, passive-safety, uco, temperature-limits]
updated: 2026-08-25
---

# Ch 01 — Introduction

Part of [[High Temperature Gas Cooled Reactor Fuels and Materials]] · pp.11–23

**Gist** — Sets out what an HTGR is, why its safety case differs in kind from a water reactor's, and what a TRISO particle is made of and for. The technically load-bearing content is in §1.1.2 and §1.2: the three fuel temperature limits, the mechanism of passive decay heat removal, the function of each coating layer, and the rationale for UCO and other advanced kernel designs.

**Scope note.** Roughly a third of this chapter is programme history — the Magnox and British Advanced Gas-cooled Reactor (AGR) lineage, operating dates and parameters for DRAGON, AVR, Peach Bottom, THTR and Fort St. Vrain, and the status of PBMR, HTR-PM and NGNP (Next Generation Nuclear Plant). Per the wiki's skip-history rule, none of that is captured here. Note that **AGR is ambiguous in this document**: here it is the British Advanced Gas-cooled Reactor line, while chapters 5 and 7 use it for the US Advanced Gas Reactor fuel development programme. **Table 1 (pp.14–15), a per-reactor table of design and operating data for roughly twenty machines, is deliberately excluded** on the same grounds.

## Why the HTGR safety case differs in kind

Four properties, all structural rather than engineered (pp.12–13, p.18):

- The large mass of graphite moderator provides high heat capacity.
- Core materials are ceramic and usable at elevated temperature.
- Helium is single-phase and inert, so chemical interactions between fuel, moderator and coolant are avoided. The contrast is explicit: those same interactions are the primary concern in water-cooled reactors during transients, because water-zirconium reactions are exothermic at elevated temperature and become autocatalytic.
- HTGR cores are physically large, so power density is appreciably low.

The consequence is stated directly: **with low power density, decay heat can be removed passively from the core through the large graphite volume without radioactivity release** (p.18). See [[Passive Decay Heat Removal]].

## The three temperature limits

| Limit | Value | Meaning | Page |
|---|---|---|---|
| Highest normal operating fuel temperature | ≤ 1250 °C | should not be exceeded in service | p.18 |
| Accident fuel temperature limit | ~1600 °C, short period | keeps coated particles intact | p.18 |
| SiC containment function | preserved to ~1800 °C | layer's own capability | p.22 |

"Fuel failure rates are extremely low below these temperatures and increases rapidly at much higher temperatures" (p.18) — but the chapter adds that accident fuel performance depends on temperature progression, duration, burnup and fabrication quality, and must be demonstrated by irradiation experiments followed by out-of-reactor accident simulation (p.18), which is what [[Ch 09 — Accident Testing]] reports.

The 1250 °C figure is the one that was missing from the wiki. [[Ch 08 — Fuel Failure Mechanisms]] puts the onset of diffusive cesium release through *intact* coatings at approximately 1300 °C (p.75) — so the normal-operation limit sits roughly 50 °C below a release mechanism that involves no failure at all.

## Particle and element geometry

| Parameter | Value | Page |
|---|---|---|
| TRISO particle overall diameter | 500–1000 µm | p.18 |
| Fuel kernel diameter | 350–600 µm | p.18 |
| Typical enrichment | 8–20%, set by power rating and safety | p.18 |
| Kernel materials | UO₂, PuO₂, or UCO; thorium compounds alone or mixed | p.18 |
| Coated particles per HTGR core | > 10⁹ | p.19 |
| Tramp uranium + matrix contamination | ~10⁻⁵ of total uranium in the element | p.22 |
| Prismatic compact | ~13 mm diameter × 51 mm long | p.15 |
| Compacts per hexagonal fuel element | ~3200 | p.18 |
| GT-MHR block | 793 mm long × 360 mm across sides | p.15 |
| GT-MHR annular core | 10 layers × 102 hexagonal elements around an unfuelled graphite centre | p.15 |

The tramp uranium figure matters beyond fabrication: a small amount of uranium becomes trapped in the coating layers during coating, and further uranium impurity exists in the matrix and in the PyC source material. Together about 10⁻⁵ of the element's uranium sits *outside* the SiC boundary and is free to release fission products regardless of particle integrity (p.22). This is the same order as the modern defect fraction, and explains why [[Ch 09 — Accident Testing]] finds release dominated by as-manufactured defects and contamination.

## Layer functions

Each layer does more than one job (p.22):

- **Buffer** (low-density PyC) — sacrificial layer that stops energetic fission products, protecting IPyC (inner pyrocarbon) from radiation damage; provides void volume for fission gases and kernel swelling.
- **IPyC** — barrier against gaseous fission product diffusion, *and* against chlorine gas generated during SiC deposition infiltrating the kernel; helps keep SiC in compression.
- **SiC** — main pressure boundary, retains metallic fission products, provides strength.
- **OPyC (outer pyrocarbon)** — gaseous fission product barrier, reduces tensile stress on SiC, forms the bonding surface for overcoating or matrix material.

The chlorine function is only intelligible alongside [[Ch 02 — Manufacture of TRISO Coated Particles]]: SiC is deposited by decomposing methyltrichlorosilane, CH₃SiCl₃ → SiC + 3HCl (p.31). The IPyC is protecting the kernel from a by-product of depositing the layer above it.

Pyrocarbon on both sides of the SiC provides prestressing that helps accommodate internal pressure (p.18). See [[TRISO Particle Architecture]].

## BISO and TRISO

BISO was two pyrocarbon layers — a porous buffer surrounded by dense PyC — around the kernel. Both retain gaseous fission products, but **BISO use was limited to low temperature and low burnup**, whereas TRISO retains *metallic* fission products at operational, transient and design accident temperatures. From the 1980s only TRISO has met the quality and performance required for modern HTGRs (pp.19–20).

## Advanced kernels

### UCO

(p.22) — a stoichiometric two-phase mixture of UO₂ and UC₂. Sufficient carbon atoms in the kernel consume the excess oxygen atoms internally, preventing CO buildup and thereby "eliminating kernel migration (or the 'amoeba effect') and excess internal pressures at high burnups." This is the stated route to higher outlet temperature *and* higher discharge burnup simultaneously. See [[UCO vs UO2 Kernels]].

### UO₂\*

(p.22) — a dense pyrocarbon seal coat plus a thin ZrC layer applied directly onto a UO₂ kernel, then conventional TRISO coatings. The ZrC acts as an oxygen getter, limiting CO production and retarding kernel migration. Irradiated side by side with UO₂, UC₂ and UCO kernels in the ORNL (Oak Ridge National Laboratory) HFIR (High Flux Isotope Reactor) reactor (HRB-15A, HRB-15B, HRB-16) at 860–1210 °C, reaching 19–29% FIMA (fissions per initial metal atom) and fast fluences of 3.7–6.5 × 10²⁵ n/m² (E > 29 fJ). UO₂\* showed superior performance in irradiation and in post-irradiation annealing.

> [!info] Reading the 19–29% FIMA figure
> This is far above the 11% and 15% FIMA thresholds discussed in [[Ch 09 — Accident Testing]] p.91, and should not be read as contradicting them. The HRB tests were irradiations at 860–1210 °C, not accident-condition heating tests, and they used a different particle design. The Ch 09 thresholds concern the fuel temperature limit permissible *in an accident* at a given burnup.

### ZrC replacing SiC

(p.23) — proposed particularly for mixed oxide Pu and minor actinide fuel, to minimise Pd attack. ZrC's higher refractory properties could raise fuel temperature limits by roughly 200 °C. Requires significant development plus extensive irradiation and accident simulation testing.

## Figures kept

![[tecdoc1645-p19-fig05-biso-triso.jpeg]]
*Fig. 5, p.19 — BISO and TRISO coated fuel particles (General Atomics).*

![[tecdoc1645-p23-fig07-uo2star-particle.jpeg]]
*Fig. 7, p.23 — cross-section of the UO₂\* coated fuel particle, with seal coat and ZrC oxygen getter between kernel and buffer.*

## Open questions raised

- The 1250 °C normal-operation limit is stated without derivation. Given diffusive Cs release begins around 1300 °C, is 1250 °C set by that mechanism, and what margin does it represent?
- ZrC-for-SiC would raise temperature limits by ~200 °C and reduce Pd attack, and has been proposed since at least this document. What has been done since?
