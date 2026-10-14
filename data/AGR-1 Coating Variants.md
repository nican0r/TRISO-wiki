---
type: data
title: AGR-1 Coating Variants
status: draft
sources: 3
tags: [triso, agr-1, fabrication, irradiation, sic, ipyc, fission-product-release, inferred]
updated: 2026-10-14
---

# AGR-1 Coating Variants

The AGR-1 (first US Advanced Gas Reactor irradiation) experiment coated four fuel lots to the same design and deliberately changed one deposition condition per variant, then irradiated them together. It is the wiki's only case where a coating parameter and a measured in-reactor outcome sit on the same page. Coating physics: [[SiC Layer Deposition]], [[PyC Layer Deposition]]. Recipes: [[TRISO Coating Parameters]].

## How the sources' coverage differs

| Key | Source | What it supplies |
|---|---|---|
| **PIE** | [[PIE on Five Irradiated AGR-1 Compacts\|Hunn et al. 2012]] | Variant descriptions and measured release, one compact per lot |
| **B&W** | [[FY 2008 Six-Inch Diameter Coater Test Report\|Barnes and Marshall 2008]] | The AGR-2 successor conditions and the argon-variant rationale |
| **Review** | [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production\|Hu et al. 2025]] | The AGR-1-era coater conditions compiled from Hunn and Lowden 2006 |

The per-lot fabrication data reports (ORNL/TM-2006/019–022) are **not ingested**, so as-fabricated densities, anisotropies and defect fractions for each variant are not in the wiki. The table below is what the ingested sources state.

## The variants

| Lot | What was changed | Resulting layer property | Source |
|---|---|---|---|
| Baseline | designed to replicate high-performance German TRISO coatings | — | PIE p.6 |
| Variant 1 | IPyC (inner pyrocarbon) deposition condition | lower IPyC density | PIE p.6 |
| Variant 2 | not examined in this source | — | — |
| Variant 3 | alternate SiC deposition process, argon added to the hydrogen diluent | smaller SiC grain size; more small localised defects | PIE pp.6, 8 |

Coater conditions compiled for the same campaign: baseline, V1 and V2 SiC at 1500 °C in H₂ with MTS (methyltrichlorosilane) at 1.11–1.23 % of flow; V3 at 1425 °C in 1:1 Ar–H₂ with MTS at 1.92–2.01 % (Review p.5, citing Hunn and Lowden 2006, 5.08 cm coater). Those are the AGR-1 SiC variants in [[TRISO Coating Parameters#SiC across coaters]].

## What irradiation measured

Fraction of compact inventory found outside intact SiC after ~3 years, one compact per lot (PIE p.7; equivalent exposed kernels in parentheses):

| | Baseline (6-1-1) | Variant 3 (4-4-2) | Variant 1 (5-2-3) |
|---|---|---|---|
| ¹¹⁰ᵐAg | 1.2 × 10⁻¹ (486) | 2.3 × 10⁻² (94) | 3.3 × 10⁻³ (14) |
| ⁹⁰Sr | 6.0 × 10⁻⁴ (2.5) | 1.7 × 10⁻⁵ (0.07) | 3.1 × 10⁻³ (13) |
| ¹⁴⁴Ce | 6.9 × 10⁻⁴ (2.9) | 1.3 × 10⁻⁵ (0.05) | 1.6 × 10⁻³ (6.3) |
| ¹⁵⁴Eu | 1.4 × 10⁻² (54) | 6.1 × 10⁻⁴ (2.5) | 6.3 × 10⁻³ (26) |
| ¹⁵²Sm | 9.4 × 10⁻⁴ (3.9) | 9.4 × 10⁻⁵ (0.39) | 4.7 × 10⁻³ (20) |
| ¹⁰⁵Pd | 1.1 × 10⁻² (47) | 1.1 × 10⁻² (47) | 2.1 × 10⁻² (86) |
| ¹³⁷Cs | 8.0 × 10⁻⁵ (0.33) | 3.0 × 10⁻⁵ (0.12) | 6.7 × 10⁻⁵ (0.28) |

Particle failures: two particles in the Variant 1 compact released caesium during irradiation, through SiC cracks propagated from the IPyC after buffer fracture (PIE p.4). No ⁸⁵Kr release from any compact.

## Reading it

The authors' own conclusion is cautious and one-directional: the results indicate "a possible reduction of fission product release associated with the finer grain microstructure achieved using argon as a diluent", and that process "is now the baseline process for AGR-2 and beyond" (PIE p.25). Variant 3 is lowest for every carbide-forming species — Sr, Ce, Sm, Eu — by one to two orders of magnitude.

Silver does not follow that order: Variant 1 is lowest and Baseline highest. The authors qualify it — the Variant 1 figure is "possibly due to greater release from the compact during irradiation" (p.7), and this method counts only what stayed in the compact. Treat the silver row as not comparable across lots.

> [!info] Inferred — what the variant comparison can and cannot support
> One compact per lot, and the lots differ in more than the named parameter (each was a separate coater campaign). The source says additional compacts per lot are needed (p.25). So: the argon/finer-grain SiC result is suggestive and was acted on programmatically; the Variant 1 IPyC result is a failure mechanism observed in two particles, not a release statistic. Confirmation would need the per-lot fabrication reports (ORNL/TM-2006/019–022) and the AGR-1 PIE final report, neither ingested.
> `#inferred`

## Bearing on the open conflicts

- **Fine-grain SiC** — [[Silver Release]] carries a conflict between finer grain improving retention (Petti 2003) and increasing silver release (Gerczak 2016). This source adds a third data point: finer grain, lower release of everything except silver, with silver unmeasurable by this route.
- **Argon dilution** — [[SiC Layer Deposition]] records argon as a way to hit density at lower temperature. Here the same choice is credited with a performance improvement and promoted to baseline, which is the strongest reason in the wiki for preferring it.

## Sources
- [[PIE on Five Irradiated AGR-1 Compacts]]
- [[FY 2008 Six-Inch Diameter Coater Test Report]]
- [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production]]
