---
type: source
title: Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method
authors: [Liu, M., Liu, R., Liu, B., Shao, Y.]
org: Institute of Nuclear and New Energy Technology (INET), Tsinghua University
year: 2015
doc-id: doi:10.1016/j.proeng.2015.01.328
journal: Procedia Engineering 102 (2015) 1890–1895 — 7th World Congress on Particle Technology (WCPT7)
pdf: raw/pdf/preparation-of-TRISO-FB-CVD-method.pdf
md: raw/md/preparation-of-triso-fb-cvd-method.md
pages: 6
ingested: 2026-09-21
status: draft
tags: [triso, cvd, spouted-bed, fabrication, reactor-design, gas-distributor, conflict]
updated: 2026-09-21
---

# Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method
> INET (Institute of Nuclear and New Energy Technology), Tsinghua University, 2015. doi:10.1016/j.proeng.2015.01.328. Conference paper, 6 pp. Page citations use the PDF page markers (p.1–6), not journal pages 1890–1895.
> [PDF](../raw/pdf/preparation-of-TRISO-FB-CVD-method.pdf) · [converted](../raw/md/preparation-of-triso-fb-cvd-method.md)

**Gist** — A short conference paper describing two equipment changes INET made to the fluidised bed–chemical vapour deposition (FB-CVD) coater on its automated TRISO production line: a furnace heated unevenly along its height so the hottest zone sits above the gas nozzle, and a gas distributor with several rings of inclined holes chosen by CFD (computational fluid dynamics) simulation. It reports one set of per-layer coating parameters from 3 kg UO₂ batches. Claims of improvement are qualitative — no accretion rates, defect fractions or product-variance figures are given — so its findings are single-source and soft.

## Key findings
- **Three ways coating fuel differs from ordinary fluidised beds**: depositing solids plug small orifices; kernels at 10.8 g/cm³ do not fluidise over a conventional perforated plate; the bed must capture depositing species efficiently to give uniform layers — `p.2`.
- **Pyrocarbon (PyC) layers deposit at about 1300 °C from ethyne and propene in argon; SiC at about 1600 °C from MTS (methyltrichlorosilane) vapour carried by hydrogen** — `p.2`.
- **Axially non-uniform heating moves the CVD zone off the nozzle.** The central heating element is partly thinned, so the high-temperature zone sits a set height above the nozzle and the nozzle runs cooler; deposition concentrates away from the nozzle and nozzle accretion falls "significantly" (unquantified). Heat loss is also reduced — `p.3`. See [[TRISO Coating Reactor Design]].
- **Secondary report of INL (Idaho National Laboratory) nozzle trials**: four geometries (original, concave, dome, hemisphere) tested; dome selected on product variance and nozzle accretion; spout-bed bottom slope increased; bed stagnation reduced by reducing nozzle radius and orifice angles — `pp.3–4`, citing an INL 2010 review presentation.
- **INET distributor choice**: traditional single-nozzle, modified single-nozzle, multi-nozzle, and multi-ring inclined-hole inlets compared by 3-D Euler–Euler CFD; the multi-ring inclined-hole inlet gave the most uniform fluidisation, especially at the bed bottom, and was selected and validated experimentally — `p.4`.
- **Production line**: automated, 3 kg UO₂ batches, all four layers coated continuously; the same line has coated ZrO₂ (5.8 g/cm³) and WC (12.8 g/cm³) particles; ZrC layers under study — `p.4`.
- **Particle dimensions**: 0.5 mm UO₂ kernel, 0.92 mm coated particle — `p.2`, Fig. 1. Consistent with the Table 1 thicknesses: 500 + 2 × (95 + 40 + 35 + 40) = 920 µm.

## Data extracted

Table 1, experimental coating parameters (p.5):

| Layer | Thickness (µm) | Density (g/cm³) | Coating time (min) | Reactant + fluidisation gas | Temperature (°C) |
|---|---|---|---|---|---|
| Buffer PyC | 95 | 0.9 | ~2.5 | Acetylene + argon | ~1260 |
| IPyC (inner PyC) | 40 | 1.9 | ~12.5 | Propylene + argon | ~1280 |
| SiC | 35 | 3.2 | ~150.0 | MTS + hydrogen | ~1600 |
| OPyC (outer PyC) | 40 | 1.9 | ~12.0 | Propylene + argon | ~1300 |

Compared with two other sources on [[TRISO Coating Parameters]].

> [!warning] Internal inconsistency
> The text gives "ethyne and propene" as the reactive gas for the PyC coating process (p.2); Table 1 lists acetylene (ethyne) for the buffer only and propylene (propene) alone for IPyC and OPyC (p.5). Read as: buffer from ethyne, dense PyC from propene — but the source does not say so.

## Figures kept

![[fbcvd-p02-fig01-coating-system-schematic.jpeg]]
*Fig. 1, p.2 — gas supply (Ar, C₂H₂, two H₂ lines, MTS bubbler), conical spouted-bed furnace with water cooling and an infrared pyrometer, and the particle geometry (0.5 mm kernel, 0.92 mm coated particle).*

![[fbcvd-p03-fig02-nozzle-accretion.jpeg]]
*Fig. 2, p.3 — accretion built up around the orifices of a multi-hole gas distributor; reproduced from a 2008 US AGR (Advanced Gas Reactor) fuel-programme paper.*

![[fbcvd-p03-fig03-vertical-temperature-profile.jpeg]]
*Fig. 3, p.3 — axial temperature profiles at 1200, 1400 and 1600 °C setpoints, with the hot zone marked between the dashed lines.*

![[fbcvd-p04-fig04-inl-gas-distributors.jpeg]]
*Fig. 4, p.4 — the four INL nozzle geometries: original, concave, dome, hemisphere.*

![[fbcvd-p04-fig05-inet-gas-distributors.jpeg]]
*Fig. 5, p.4 — the four INET inlet designs; (d) multi-ring inclined holes was selected.*

Skipped: Fig. 6 (p.5), a low-resolution SEM (scanning electron microscope) image of a sectioned particle.

## What this changes in the wiki

- Adds an axial-heating design lever to [[TRISO Coating Reactor Design]], and a second, independently selected distributor geometry.
- Corroborates the INL dome-nozzle selection already on [[TRISO Coating Reactor Design]], at second hand.
- Third per-layer parameter set; the three are consolidated on the new [[TRISO Coating Parameters]].
- Contradicts the SiC deposition temperature on [[TRISO Coating Process]] (~1600 °C vs 1500 °C) and the buffer deposition time on [[TRISO Coating Reactor Design]] (~2.5 min vs 5 min) — flagged on [[TRISO Coating Parameters]].
- Third design using the 95/40/35/40 µm layer thicknesses on [[TRISO Particle Architecture]] — identical to the German reference.
- Shows an infrared pyrometer on the coater, where [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] (p.5) says optical pyrometry is not used — noted on [[TRISO Coating Reactor Design]].

## Open questions raised
- What the Fig. 3 profiles were measured under — empty furnace, static bed, or fluidised bed. The text says the gradient decreases once the bed is fluidised (p.3), so the plotted profiles probably overstate the in-process gradient.
- Whether the pyrometer in Fig. 1 views the bed or the furnace wall.
- No quantified comparison of distributor designs is given here; the CFD study is in the paper's ref. [8] (Liu et al. 2014, Nucl. Eng. Des. 271:68–72).

## Pages updated on ingest
- [[TRISO Coating Parameters]] (new), [[TRISO Coating Reactor Design]], [[TRISO Coating Process]], [[TRISO Particle Architecture]], index
