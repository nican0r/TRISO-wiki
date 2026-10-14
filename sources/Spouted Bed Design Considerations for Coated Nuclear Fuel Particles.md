---
type: source
title: Spouted Bed Design Considerations for Coated Nuclear Fuel Particles
authors: [Marshall, D.W.]
org: Idaho National Laboratory (Battelle Energy Alliance)
year: 2017
doc-id: INL/CON-15-36799
pdf: raw/pdf/spouted-bed-design-considerations.pdf
md: raw/md/spouted-bed-design-considerations.md
pages: 10
ingested: 2026-09-08
status: draft
tags: [triso, cvd, spouted-bed, fabrication, reactor-design, fluidization]
updated: 2026-09-08
---

# Spouted Bed Design Considerations for Coated Nuclear Fuel Particles
> Idaho National Laboratory (Battelle Energy Alliance), 2017. INL/CON-15-36799. Preprint for Fluidization XV.
> [PDF](../raw/pdf/spouted-bed-design-considerations.pdf) · [converted](../raw/md/spouted-bed-design-considerations.md)

**Gist** — A conference preprint by Douglas W. Marshall (Idaho National Laboratory) documenting the mechanical and process design of the spouted-bed CVD (chemical vapor deposition) reactor that deposits all four TRISO coating layers, as used in the US DOE-funded Advanced Gas Reactor (AGR) Fuel Development and Qualification program. It covers the criticality-safety constraint on retort diameter, the fluidization regime the process actually operates in, the multi-orifice gas distributor nozzle and curvilinear converging-section geometry that replaced earlier single-orifice conical designs, and the near-total absence of in-bed instrumentation. Its value is a first-hand equipment-design account, not test data — no irradiation or QC results appear here, only fabrication engineering.

## Key findings
- **Retort diameter is set by criticality safety, not process optimisation.** The HEU (highly-enriched uranium)-licensed coater discussed is held to 15.2 cm internal diameter to remain critically safe by geometry even if HEU were used inadvertently; LEU (low-enriched uranium) equipment elsewhere has used retorts up to 24 cm — `p.4`.
- **All four layers deposit in one concatenated batch sequence, 1230–1550 °C**, during which mean particle diameter doubles, bed volume grows 8-fold, and particle envelope density falls from 11 g/cm³ (kernel) to 3 g/cm³ (finished particle) — `p.2`.
- **No internal instrumentation is used at all**: no sight ports, no internal thermocouples (a top-hung probe's radial position can't be controlled, and the radial temperature profile makes a single internal reading useless anyway), no optical pyrometry (blocked by opaque black smoke during pyrocarbon deposition). Control is entirely by external, wall-offset thermocouples and gas-flow parameters, checked only after the run — `p.5`.
- **The process falls entirely outside the standard mapped region for spouted beds.** High temperature and small particle diameter push it off the Grace/Kunii regime chart; stable spouting is not achieved, only a pulsatory spouted-bed mode, confirmed by pressure-fluctuation sensing and CPFD Barracuda VR® modelling — `p.6`.
- **A multi-orifice domed gas distributor nozzle replaced a single-orifice design** that formed volcano-shaped accretions trapping particles between the accretion and the retort wall — `p.6–7`.
- **A curvilinear converging section (continuously variable slope, 22° at the top, ~116° at the base) replaced standard single-angle conical sections (45–60°)**, to combine spout stability with full bed circulation — `p.7–8`.
- **Soot inclusions — carbon soot swept from the fountain back into the bed and encapsulated in a coating layer — are a fabrication-stage defect**, frequent in a 5 cm lab-scale single-orifice coater, infrequent in the 15 cm production coater once the nozzle, converging section, and a dual gas path diverting some inert gas through an annular orifice were combined — `p.8–9`.
- **Scale-up is not a simple linear extrapolation.** At constant linear deposition rate, gas flow scales with bed mass (∝ diameter³) while gas velocity scales with diameter, so residence time falls as the retort grows — lab-scale temperature setpoints are stated to be inaccurate at larger diameters as a result — `p.4, 6`.
- **This coater design is in current use by the US AGR Fuel Development and Qualification program** — `p.9`.

## Data extracted

Table 1, nominal TRISO particle layer dimensions with a 425 µm kernel (p.5):

| Material | Layer thickness (µm) | Layer density (g/cm³) | Particle diameter (µm) | Particle density (g/cm³) | Relative mass | Relative volume | Δ time (min) |
|---|---|---|---|---|---|---|---|
| Kernel | — | — | 425 | 11.1 | 1.00 | 1.00 | — |
| Buffer | 100 | 1.00 | 625 | 4.18 | 1.20 | 3.18 | 5 |
| IPyC | 40 | 1.90 | 705 | 3.49 | 1.43 | 4.56 | 12 |
| Silicon carbide | 35 | 3.20 | 775 | 3.42 | 1.87 | 6.06 | 100 |
| OPyC | 40 | 1.90 | 855 | 3.03 | 2.22 | 8.14 | 13 |

## Figures kept

![[spouted-bed-p03-fig01-sectioned-triso-particle.jpeg]]
*Figure 1 (source's own numbering), p.3 — polished cross-section of a finished TRISO particle showing all four coating layers around the kernel, 200 µm scale bar.*

![[spouted-bed-p06-fig02-fluidization-regime-map.jpeg]]
*Captioned "Figure 1" in the source (p.6) — confirmed against the PDF as a genuine duplicate caption, not a conversion artefact; this is the second, unrelated figure captioned "Figure 1." Dimensionless particle diameter vs. dimensionless gas velocity, showing each TRISO layer's start/end point falling outside the standard mapped region for spouted beds.*

![[spouted-bed-p07-fig03-gas-distributor-nozzle.jpeg]]
*Figure 2, p.7 — the multi-orifice domed gas distributor nozzle with serrated flange that replaced the single-orifice design.*

![[spouted-bed-p08-fig04-converging-section.jpeg]]
*Figure 3, p.8 — rendered cross-section of the curvilinear converging section, 22° included angle at the cylindrical junction widening to ~116° at the base.*

![[spouted-bed-p08-fig05-soot-inclusion.jpeg]]
*Captioned "Figure 4" in the source (p.8) but referred to as "Figure 5" in the body text two lines above the caption — confirmed against the PDF. Micrograph of a soot inclusion encapsulated within the SiC layer, 50 µm scale bar.*

## Defects in the source document

> [!warning] Duplicate figure numbering
> Two unrelated figures are both captioned "Figure 1" — the sectioned TRISO particle micrograph (p.3) and the dimensionless fluidization regime map (p.6). The remaining figures are numbered 2–4, but the soot-inclusion micrograph is called "Figure 5" in the body text one line above its own "Figure 4" caption (p.8). Confirmed against the PDF, not a conversion artefact. Cite by page and description, not by the source's figure number.
> `#conflict`

## What this changes in the wiki

- Refines [[TRISO Coating Process]]: corroborates the per-layer 1250–1500 °C setpoints with an independent source's stated overall envelope (1230–1550 °C), and adds per-layer deposition time and bed mass/volume growth that TRISO Coating Process's Table 2 does not carry.
- Adds an equipment-design layer beneath [[TRISO Coating Process]] that no ingested chapter of [[High Temperature Gas Cooled Reactor Fuels and Materials]] covers at this depth — retort geometry, gas injector, converging section — as the new page [[TRISO Coating Reactor Design]].
- Extends [[Fuel Quality Control and Characterization]]: the coating step itself runs with no internal instrumentation at all, checked only after the fact — the existing page covers post-run metrology but not this "flown blind" character of the run producing what gets measured.
- Adds a fabrication-stage defect (soot inclusion) that is not one of the eleven service mechanisms on [[TRISO Fuel Failure Mechanisms]] — those describe a correctly built particle degrading in reactor; this is a particle built with the flaw already in it.
- Gives a second reference-design data point for [[TRISO Particle Architecture]]'s layer-thickness table: a US HEU-line 425 µm-kernel design with a 100 µm buffer layer, next to the existing 95 µm German LEU reference — different fabrication lines, not a disagreement.

## Open questions raised

> [!warning] Conflict — predicted peak accident fuel temperature
> This source states peak centerline core temperatures during postulated accidents "safely remain 200–300 °C below fuel fabrication temperatures" (p.3); fabrication runs up to 1550 °C (p.2), implying a predicted peak near 1250–1350 °C. [[Passive Decay Heat Removal]] gives a peak of 1620 °C for a depressurised loss-of-forced-circulation event in modern small HTRs ([[Ch 01 — Introduction]] p.18, [[Ch 09 — Accident Testing]] p.78). The two sources do not name the same reactor design or accident scenario, and this source gives no scenario detail to reconcile them — flagged, not resolved.
> `#conflict`

- Whether the 100 µm vs. 95 µm buffer-layer difference reflects a genuine US/German design divergence, or just a different nominal reference point, is not resolvable from either source alone.

## Pages updated on ingest

- [[TRISO Coating Reactor Design]] (new), [[TRISO Coating Process]], [[TRISO Particle Architecture]], [[Fuel Quality Control and Characterization]], [[Passive Decay Heat Removal]], index
