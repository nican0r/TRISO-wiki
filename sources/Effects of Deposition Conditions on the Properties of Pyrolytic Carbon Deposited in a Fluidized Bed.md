---
type: source
title: Effects of Deposition Conditions on the Properties of Pyrolytic Carbon Deposited in a Fluidized Bed
aliases: [Lowden et al. 2005, ORNL/TM-2005/533]
authors: [Lowden, R.A., Hunn, J.D., Nunn, S.D., Kercher, A.K., Price, J.R., Menchhofer, P.A., Jellison, G.E.]
org: ORNL
year: 2005
doc-id: ORNL/TM-2005/533
url: https://info.ornl.gov/sites/publications/files/Pub595.pdf
pdf: raw/pdf/effects of deposition conditions on properties of pyrolytic carbon.pdf
md: raw/md/effects-of-deposition-conditions-on-properties-of-pyrolytic-carbon.md
pages: 35
ingested: 2026-10-14
status: draft
tags: [triso, pyc, ipyc, cvd, fabrication, density, anisotropy, permeability, porosity]
updated: 2026-10-14
---

# Effects of Deposition Conditions on the Properties of Pyrolytic Carbon Deposited in a Fluidized Bed
> ORNL, September 2005. ORNL/TM-2005/533. 35 pp. Page citations use the PDF page markers.
> [PDF](../raw/pdf/effects%20of%20deposition%20conditions%20on%20properties%20of%20pyrolytic%20carbon.pdf) · [converted](../raw/md/effects-of-deposition-conditions-on-properties-of-pyrolytic-carbon.md)

**Gist** — A two-factor designed experiment on the IPyC (inner pyrocarbon) layer: 17 coating runs on 346–347 µm NUCO (natural-enrichment uranium oxycarbide) kernels in the ORNL 2-inch coater, varying only deposition temperature (1170–1325 °C) and coating gas fraction (0.15–0.45) with all gas flows tabulated. Each run's layer was measured for density, anisotropy, open porosity and permeability to chlorine. It is the first parameter→property map for pyrocarbon in the wiki, and the counterpart to [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] for SiC. Written as a data report: no discussion section, no uncertainty analysis beyond the tabulated standard deviations.

## Key findings

- **Each property has one dominant parameter** — `p.7`:

  | Property | Controlled by |
  |---|---|
  | Deposition rate | coating gas fraction (reactant concentration) |
  | Density | deposition temperature |
  | Permeability | deposition temperature, through density |
  | Open porosity | coating gas fraction, through coating rate |
  | Efficiency | both |
  | Anisotropy | both, non-monotonically |

- **Density falls as temperature rises**, 1.978 g/cm³ at 1170 °C to 1.746 at 1325 °C, monotonic across the range — `p.34`, Table 2.
- **Permeability rises ~20× over the same span**: uranium dispersion after 18 h of chlorination at 1500 °C goes from 0.342 (×10⁻²) at 1170 °C to 7.52 at 1325 °C — `p.34`. This is a direct test of the IPyC's function as a barrier to the HCl released during SiC deposition ([[TRISO Particle Architecture]]).
- **Open porosity rises with coating gas fraction**: 0.83 ml/m² at CGF 0.15 to 1.85 at 0.45, at 1275 °C — `p.34`. Porosity governs how well SiC keys into the IPyC ([[TRISO Coating Process]]).
- **Anisotropy is the awkward one.** Diattenuation ranges 0.0031–0.0151 with no monotonic trend in either variable; the lowest-temperature, lowest-CGF run (1225 °C, 0.15) is the most anisotropic at 0.0151 — `p.34`.
- **The fixed conditions matter for comparison**: buffer always 1275 °C, CGF 0.60, 7,500 sccm, 5 min; IPyC always propylene/acetylene 0.85 at 8,500 sccm total, with time adjusted to hold thickness — `p.5`.
- **Reported temperatures were shifted by 25 °C** after recalibration of the sight glass and prism used for the optical pyrometer — `p.6`. See [[Coater Process Monitoring]].

## Data extracted

Conditions, Table 1 `p.5` (CGF = coating gas fraction; balance argon; total 8,500 sccm):

| CGF | Ar (sccm) | C₂H₂ (sccm) | C₃H₆ (sccm) |
|---|---|---|---|
| 0.15 | 7,225 | 690 | 585 |
| 0.30 | 5,950 | 1,375 | 1,175 |
| 0.45 | 4,675 | 2,065 | 1,760 |

Results, Table 2 `p.34`, selected runs (density ±, diattenuation ± and thickness ± omitted; permeability in arbitrary units ×10⁻² proportional to dispersed-uranium density; porosity at 250–10,000 psi):

| Run | T (°C) | CGF | Rate (µm/min) | Density (g/cm³) | Diattenuation N | Permeability | Porosity (ml/m²) |
|---|---|---|---|---|---|---|---|
| 13 | 1170 | 0.30 | 2.3 | 1.978 | 0.0099 | 0.540 | 0.71 |
| 3 | 1225 | 0.30 | 2.6 | 1.962 | 0.0078 | 0.342 | 1.10 |
| 6 | 1225 | 0.15 | 1.1 | 1.962 | 0.0151 | 0.588 | — |
| 8 | 1225 | 0.45 | 4.0 | 1.958 | 0.0083 | 0.661 | 1.45 |
| 20 | 1250 | 0.30 | 2.9 | 1.909 | 0.0048 | 0.555 | 1.32 |
| 4 | 1275 | 0.15 | 1.5 | 1.813 | 0.0075 | 0.760 | 0.83 |
| 1 | 1275 | 0.30 | 3.2 | 1.829 | 0.0038 | 0.932 | — |
| 7 | 1275 | 0.45 | 4.7 | 1.873 | 0.0050 | 0.727 | 1.85 |
| 11 | 1300 | 0.30 | 2.9 | 1.831 | 0.0052 | 3.32 | — |
| 2 | 1325 | 0.30 | 3.5 | 1.773 | 0.0040 | 4.48 | — |
| 5 | 1325 | 0.15 | 1.7 | 1.746 | 0.0047 | 7.52 | 1.28 |
| 9 | 1325 | 0.45 | 6.6 | 1.765 | 0.0031 | 6.56 | — |

Full 17-run table, including buffer and IPyC thicknesses and fast-axis standard deviations, is in the converted markdown. Consolidated against other lines: [[TRISO Coating Parameters]].

## Figures kept

![[lowden-p31-fig29-u-dispersion-vs-temperature.jpeg]]
*Fig. 29, p.31 — x-ray images of uranium dispersed into the carbon layers after 18 h chlorination at 1500 °C, CGF 0.30, by deposition temperature. The darkening at 1300–1325 °C is the permeability rise made visible.*

Skipped: the cross-section and SEM micrographs (Figs. 2–21, pp.9–28) and the response surfaces (Figs. 22–27, 31–32, pp.29–33), whose content is in the table and the findings above.

## What this changes in the wiki

- Fills the pyrocarbon process window that [[TRISO Coating Process]] records as missing — new page [[PyC Layer Deposition]].
- First wiki source measuring IPyC permeability, and the first evidence that the chlorine-barrier function degrades with deposition temperature.
- Adds a fourth IPyC temperature/density pairing to [[TRISO Coating Parameters]], from a line that reports gas flows.
- Supplies the 2-inch-coater half of the density-vs-temperature comparison in [[FY 2008 Six-Inch Diameter Coater Test Report|Barnes and Marshall 2008]].

## Open questions raised

- Density is reported from a liquid density-gradient column on fragments cracked off the particle; the authors note residual buffer may still be attached and could bias the result (`p.7`). No bias estimate is given.
- Permeability is in arbitrary units, so it cannot be compared with any other source.
- The study covers IPyC only. Buffer and OPyC (outer pyrocarbon) conditions were held fixed.

## Pages updated on ingest
- [[PyC Layer Deposition]] (new), [[TRISO Coating Parameters]], [[TRISO Coating Process]], [[Coater Process Monitoring]] (new), [[TRISO Particle Architecture]], index, log, assets (1 figure)
