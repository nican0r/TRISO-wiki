---
type: source
title: PIE on Five Irradiated AGR-1 Compacts
aliases: [Hunn et al. 2012, ORNL/TM-2012/397, AGR-1 five-compact PIE]
authors: [Hunn, J.D., Morris, R.N., Baldwin, C.A., Montgomery, F.C., Silva, C.M.]
org: ORNL (Advanced Gas Reactor programme)
year: 2012
doc-id: ORNL/TM-2012/397
url: https://info.ornl.gov/sites/publications/Files/Pub139750.pdf
pdf: raw/pdf/PIE-of-five-compacts.pdf
md: raw/md/pie-of-five-compacts.md
pages: 31
ingested: 2026-10-14
status: draft
tags: [triso, agr-1, irradiation, pie, fission-product-release, silver, sic, fabrication-defect, conflict]
updated: 2026-10-14
---

# PIE on Five Irradiated AGR-1 Compacts
> ORNL, September 2012. ORNL/TM-2012/397. 31 pp. Page citations use the PDF page markers; printed page numbers are 3 lower (printed p.1 = PDF p.4).
> [PDF](../raw/pdf/PIE-of-five-compacts.pdf) · [converted](../raw/md/pie-of-five-compacts.md)

**Gist** — Post-irradiation examination of five AGR-1 (first US Advanced Gas Reactor irradiation) fuel compacts: three as-irradiated, two after 1600 °C safety testing. Each was deconsolidated and leached to measure fission products outside intact SiC, every particle was gamma-scanned to find those that had lost caesium, and selected particles were imaged by x-ray tomography and cross-sectioned. It is the first source in the wiki that measures what irradiated TRISO actually did, and the first that traces a specific in-service failure back to a coater condition. An interim report: one compact per fuel lot, trends explicitly provisional.

## Key findings

- **A coater defect that survived irradiation and failed in the accident test.** One particle in Compact 3-3-2 held only 40 % of its expected caesium after safety testing. X-ray tomography showed deformed, porous SiC: a fabrication defect "that occurs when a particle is over-fluidized in the coater, causing it to pick up carbon soot on the surface of the IPyC prior to SiC deposition". The layer held through three years of irradiation and cracked at 1600 °C; no ⁸⁵Kr escaped, so a pyrocarbon layer stayed intact — `pp.4, 22, 24`. This is the soot-inclusion defect on [[TRISO Coating Reactor Design]] with a measured consequence.
- **The other failure route runs through the buffer.** Buffer densification and shrinkage fractured the buffer, cracked some IPyC layers, and in rare cases the crack propagated through the SiC; the two particles that released caesium *during* irradiation (Compact 5-2-3, Variant 1, lower-density IPyC) failed this way — `p.4`.
- **Only three defective-SiC particles in ~20,000.** Across the five compacts, no significant ⁸⁵Kr release during irradiation or safety testing, and caesium retention averaged 99 % — `pp.4, 8`.
- **Silver, palladium and europium leave through intact SiC.** They are the fission products found outside the SiC in quantity, with silver the largest: 12 % of inventory from the Baseline compact — `pp.4, 7`.
- **Silver retention varies wildly between particles in the same compact**, from full calculated inventory to below detection, with no correlation to any visible radiation-induced change — `pp.4, 10`.
- **Particles that released more silver show palladium–uranium clusters deeper into the SiC** from the IPyC interface — `p.22`. The authors call for verification.
- **Thermal cycling released additional silver.** Power-supply failures cycled the 3-3-2 safety test; silver release followed, so two more cycles were added deliberately — `p.22`.
- **Variant 3 (argon-diluted, finer-grain SiC) retained the carbide-forming species better.** Its compact showed lower release of Sr, Ce, Sm, Eu and Pu; the authors attribute this tentatively to smaller grain size and more localised defects trapping diffusing species, and note the process "is now the baseline process for AGR-2 and beyond" — `pp.8, 25`. Bears on [[Silver Release]] and [[SiC Layer Deposition]].

## Data extracted

Deconsolidation-leach-burn-leach, fraction of compact inventory released outside intact SiC (equivalent exposed kernels in parentheses), Table 1 `p.7`:

| Fission product | 6-1-1 (Baseline) | 4-4-2 (Variant 3) | 5-2-3 (Variant 1) |
|---|---|---|---|
| ⁹⁰Sr | 6.0 × 10⁻⁴ (2.5) | 1.7 × 10⁻⁵ (0.07) | 3.1 × 10⁻³ (13) |
| ¹⁰⁵Pd | 1.1 × 10⁻² (47) | 1.1 × 10⁻² (47) | 2.1 × 10⁻² (86) |
| ¹¹⁰ᵐAg | 1.2 × 10⁻¹ (486) | 2.3 × 10⁻² (94) | 3.3 × 10⁻³ (14) |
| ¹³⁷Cs | 8.0 × 10⁻⁵ (0.33) | 3.0 × 10⁻⁵ (0.12) | 6.7 × 10⁻⁵ (0.28) |
| ¹⁴⁴Ce | 6.9 × 10⁻⁴ (2.9) | 1.3 × 10⁻⁵ (0.05) | 1.6 × 10⁻³ (6.3) |
| ¹⁵²Sm | 9.4 × 10⁻⁴ (3.9) | 9.4 × 10⁻⁵ (0.39) | 4.7 × 10⁻³ (20) |
| ¹⁵⁴Eu | 1.4 × 10⁻² (54) | 6.1 × 10⁻⁴ (2.5) | 6.3 × 10⁻³ (26) |
| ²³⁵U | 5.1 × 10⁻⁵ (0.21) | 4.1 × 10⁻⁵ (0.16) | 5.9 × 10⁻⁵ (0.24) |

One compact per lot, so lot-to-lot comparison is indicative only (`p.25`). Variant-by-variant reading: [[AGR-1 Coating Variants]].

> [!warning] Internal inconsistency
> Table 1 gives ²³⁹Pu for Compact 4-4-2 as pre-burn 1.4 × 10⁻⁵ (0.06) plus post-burn 2.4 × 10⁻⁵ (0.10), total **3.8 × 10⁻⁶ (0.16)** — verified against the PDF render, `p.7`. The parenthesised kernel equivalents add up; the fraction does not. Read as 3.8 × 10⁻⁵.

Low silver in the Variant 1 compact is qualified by the authors: it is "possibly due to greater release from the compact during irradiation" (`p.7`), i.e. silver that left the compact entirely is not counted by this method.

## Figures kept

![[agr1-pie-p24-fig24-porous-sic-tomograph.jpeg]]
*Fig. 24, p.24 — x-ray tomograph of the abnormal particle from Compact 3-3-2; the porous SiC arc is soot picked up on the IPyC before SiC deposition.*

![[agr1-pie-p22-fig22-pd-clusters-vs-silver.jpeg]]
*Fig. 22, p.22 — back-scattered electron images of SiC from two particles of Compact 6-4-3: average silver retention (a) and silver below detection (b). Bright spots are Pd–U clusters, deeper into the layer in the low-retention particle.*

Skipped: DLBL flow chart (p.5), the ¹³⁷Cs and ¹¹⁰ᵐAg histograms (Figs. 2–6), the safety-test release curves (Figs. 18, 23) and the materialography of irradiated buffers (Figs. 25–26).

## What this changes in the wiki

- First measured fabrication→performance link in the wiki; the gap named on [[overview]].
- Soot inclusion stops being a fabrication curiosity: [[TRISO Coating Reactor Design]] and [[TRISO Fuel Failure Mechanisms]].
- Gives [[Silver Release]] particle-level data, the Pd-silicide correlation and the thermal-cycling effect.
- New page [[AGR-1 Coating Variants]] holds the variant-by-variant comparison.
- Adds measured release-through-intact-SiC figures to [[Fission Product Retention]].

## Open questions raised

- The mechanism of silver transport through intact SiC is still open; the authors suggest single-particle furnace tests with varied thermal profiles (`p.25`).
- Whether finer-grain SiC genuinely improves retention needs more compacts per lot (`p.25`).
- Particles most likely to have defective SiC were removed by gamma sorting before burn-leach, so the leach figures understate defective-SiC particles by design (`p.7`).

## Pages updated on ingest
- [[AGR-1 Coating Variants]] (new), [[Silver Release]], [[TRISO Fuel Failure Mechanisms]], [[Fission Product Retention]], [[TRISO Coating Reactor Design]], [[SiC Layer Deposition]], index, log, assets (2 figures)
