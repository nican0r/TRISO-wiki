---
type: concept
title: Silver Release
status: draft
sources: 2
tags: [triso, fission-product-release, silver, maintenance, direct-cycle, conflict]
updated: 2026-09-22
---

# Silver Release

**In one line** — Silver migrates through apparently intact TRISO coatings at temperatures well below any failure threshold, making it the standing exception to the claim that modern TRISO retains its fission products.

## Mechanism

Silver is one of the noble fission products whose transport is not arrested by the oxycarbide chemistry that ties up other species in UCO kernels, and it is observed to migrate through particles that are structurally sound ([[Ch 08 — Fuel Failure Mechanisms]] p.74). Release begins at **irradiation temperatures above 1100 °C even through the high-quality SiC of modern TRISO coatings**, and release fractions approach 100% in accident-condition heating tests ([[Ch 09 — Accident Testing]] p.89).

The mechanism of migration through intact SiC has been the subject of dedicated study but is not settled in this source; it is described as a function of time at temperature, burnup and temperature gradient, in the same family as palladium attack of SiC (p.74).

Silver's inventory is small and ¹¹⁰ᵐAg's half-life is 253 days, so it is not a licensing-driving nuclide the way ¹³¹I is. Table 9 classifies it as "important for maintenance" rather than for design and licensing ([[Ch 09 — Accident Testing]] p.79).

## Why it matters operationally

Released silver deposits on cold surfaces. In a direct-cycle gas reactor those surfaces are in the turbine, "which has important maintenance and worker dose implications" ([[Ch 08 — Fuel Failure Mechanisms]] p.74). The consequence is not a release to the environment but a contaminated power conversion system that people have to work on.

Enrichment and burnup make it worse. The fission yield of silver and palladium differs between uranium and plutonium by a factor of **25 to 50**. In LEU (low-enriched uranium) fuel, where a significant fraction of end-of-life fissions come from plutonium, silver and palladium concentrations can be far higher than in HEU (high-enriched uranium) fuel at comparable burnup (p.74).

## Quantitative anchors

| Quantity | Value | Conditions | Source |
|---|---|---|---|
| Onset of release through intact SiC | > 1100 °C | irradiation temperature, modern TRISO | [[Ch 09 — Accident Testing]] p.89 |
| Release fraction | approaching 100% | accident-condition heating tests | p.89 |
| ¹¹⁰ᵐAg fractional release | 9.0 × 10⁻⁴ to 2.7 × 10⁻² | 1600 °C, 500 h, various elements | Table 10, p.87 |
| ¹¹⁰ᵐAg fractional release | 2.1 × 10⁻¹ to 8.1 × 10⁻¹ | 1800 °C | Table 10, pp.87–88 |
| ¹¹⁰ᵐAg half-life | 253 d | — | Table 9, p.79 |
| Ag/Pd yield ratio, Pu vs U fission | 25–50× | — | [[Ch 08 — Fuel Failure Mechanisms]] p.74 |

Note that even in the zero-failure 1600 °C tests, silver release is measurable at 10⁻³–10⁻² while krypton sits at 10⁻⁷–10⁻⁶ — four to five orders of magnitude apart in the same test.

## Design implications for HTGRs

Silver breaks the otherwise clean story that fission products stay inside the particle until the accident threshold. It escapes during **normal operation**, at temperatures a high-outlet-temperature design deliberately runs at, through coatings that are working as designed. A design targeting outlet temperatures above 900 °C is by construction operating in the regime where this occurs.

## Contested / uncertain

> [!warning] Conflict — does fine-grained SiC help or hurt?
> Finer-grained SiC gave better fission product retention in Petti et al. (2003) but higher silver release at elevated temperature in Gerczak et al. (2016). Both are cited second-hand in [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] p.2, which does not resolve them. It nonetheless recommends argon dilution "to produce fine-grain SiC to prevent fission product migration" (p.17). Fine grains are also a SiC acceptance criterion ([[Ch 02 — Manufacture of TRISO Coated Particles]] p.34). How deposition sets grain size: [[SiC Layer Deposition]]. Unresolved; the primary papers are not in the wiki.
> `#conflict`

## Sources

- [[Ch 08 — Fuel Failure Mechanisms]] · [[Ch 09 — Accident Testing]] — both from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
- [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production]]
