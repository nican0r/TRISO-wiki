---
type: source
title: Advancing the Fundamental Understanding and Scale-up of TRISO Fuel Coaters via Advanced Measurement and Computational Techniques
authors: [Biswas, P., Al-Dahhan, M.H.]
org: Washington University in St. Louis; Missouri University of Science & Technology
year: 2012
doc-id: DE-FC07-07ID14822 (DOE-NERI final management report)
pdf: "raw/pdf/SCALE-UP OF TRISO FUEL COATERS VIA ADVANCED MEASUREMENT AND COMPUTATIONAL TECHNIQUES.pdf"
md: raw/md/scale-up-of-triso-fuel-coaters-via-advanced-measurement-and-computational-techni.md
pages: 142
ingested: 2026-10-10
status: draft
tags: [spouted-bed, scale-up, cfd, gamma-densitometry, computed-tomography, optical-probe, triso, coater, conflict, inferred]
updated: 2026-10-10
---

# Advancing the Fundamental Understanding and Scale-up of TRISO Fuel Coaters via Advanced Measurement and Computational Techniques
> Washington University in St. Louis / Missouri S&T (Missouri University of Science & Technology), 2012. DOE-NERI (Nuclear Energy Research Initiative) award DE-FC07-07ID14822, final management report, 142 pp. PIs P. Biswas, M. Al-Dahhan. Cited by PDF page markers; printed page numbers match.
> [PDF](../raw/pdf/SCALE-UP%20OF%20TRISO%20FUEL%20COATERS%20VIA%20ADVANCED%20MEASUREMENT%20AND%20COMPUTATIONAL%20TECHNIQUES.pdf) · [converted](../raw/md/scale-up-of-triso-fuel-coaters-via-advanced-measurement-and-computational-techni.md)

**Gist** — A grant report on spouted-bed scale-up for TRISO coaters, done entirely in cold air (298 K) with glass beads and steel shot in 0.152 m and 0.076 m beds, plus two-fluid CFD (computational fluid dynamics). It shows that matching the He et al. (1997) dimensionless groups reproduces global quantities but not radial profiles, proposes matching the radial gas-holdup profile instead, demonstrates gamma-ray densitometry as an external flow-regime monitor, and calibrates a CFD model. The TRISO-specific tasks (particle tracking, cold-flow mimics of the AGR coater, real-coater simulation) were not completed. Unreviewed, single-group, with many internal inconsistencies: all claims here are soft.

## Key findings

**Scale-up**
- **Matched dimensionless groups (He et al. 1997 cases A, B) gave similar global but dissimilar local hydrodynamics.** Global: spout diameter within 0.77 %, fountain height 15 %, maximum spoutable height 5.65 %. Local: solids holdup 26.5 % (H/D 1.1) and 15 % (H/D 1.8), fountain 23.7 %; particle velocity 31–46 % — `pp.33–38, 44–46`. CFD repeats it: 21 % holdup, 34 % velocity — `pp.103–105`. Differences sit in the spout; the annulus matches — `p.46`.
- **Proposed criterion: match the radial gas-holdup profile** — `p.47`. "Similar" condition: 4.1 % holdup, 3.5 % velocity, 13.4 % pressure profile; "non-similar": 55.8 %, 47.9 %, 29.1 % (pressure fluctuation) — `pp.48–55`. Correlations for $U/U_{ms}$ and $\varepsilon(r)/\varepsilon_0$ in $\rho_f/\rho_s$, $gd_p/U^2$, $\rho_s d_p U/\mu$ and $P/\Delta P$ — `p.57`, Eqs. 33–34. CFD reproduces the similarity — `pp.106–110`.

**Regimes and monitoring**
- **Stable spouting window is narrow**: 1 mm glass beads, onset 0.72 / 0.58 m/s and loss of stability 0.79 / 0.66 m/s in the 0.152 / 0.076 m beds — `p.20`.
- **Gamma-ray densitometry (GRD) identifies regime from count statistics** (mean, variance, variance/mean). Transitions agree with pressure-fluctuation measurement to 3.4 % and correlations to 7.8 % — `p.20`. Cs-137, 250 mCi, external; proposed for on-line use on real coaters — `pp.5, 8`. Demonstrated at one bed height only — `p.13`.
- Wall pressure fluctuations are largest in the conical section — `p.42`; wall transducers "cannot capture complete phenomena" — `p.19`.
- Optical probe vs gamma-ray CT (computed tomography): 9.6 % — `p.62`.

**Mechanism**
- **Spout necks near the top of the bed**; annulus-to-spout solids cross-flow concentrates at the inlet and at the neck, negligible elsewhere (CFD) — `pp.121–122`.
- **Bed pressure drop is balanced by bed weight and wall shear** — `p.92`. CFD ΔP 2.19–3.45 kPa as wall specularity goes 1 → 0 — `p.91`, Table 10.
- **"Flat" slugs above the gas inlet impair circulation and cause non-spherical particles, coating flaws and missing layers** — `pp.7, 123`. Uncited in the report; single-source.
- Solids velocity highest at a 45° cone, lower at 30° and 60° — `p.114`.

**Temperature (CFD)**
- Maximum spouted height rises from 293 K to 1293 K for 0.5 mm, 2,500 kg/m³ glass in air — `p.124`, Fig. 119. Air viscosity $\mu_g = 1.46\times10^{-6}T^{1.504}/(T+120)$, density $\rho_g = 1.2\cdot293/T$ — `p.123`, Eqs. 85–86; 1.8 × 10⁻⁵ Pa·s at 293 K, 4.94 × 10⁻⁵ at 1293 K — `p.124`.

**Correlations (cold flow)**
- Stable-spouting geometry: $D_i/d_p < 25$–$30$, $D_c/D_i > 3$–$12$, $H < H_m$ — `p.19`, Eqs. 18–20.
- Maximum spoutable height peaks at $d_p$ ≈ 1–2 mm; falls with larger inlet and higher gas flow; McNab–Bridgwater deviates "largely" — `pp.63–66`.
- Spout diameter: solids density, bed height, particle size, gas velocity, inlet diameter all significant; regression 2.1 % error, stable spouting only — `pp.67–71`.
- Gas mean residence time 0.87 s, 0.152 m bed (CFD, He tracer) — `p.78`.

**CFD model (summary)** — Fluent 6.3 two-fluid model, kinetic theory of granular flow, Gidaspow drag, Schaeffer friction, dispersed k–ε; Johnson–Jackson wall condition, specularity 0.05 and particle–wall restitution 0.9 chosen; 2D axisymmetric within 3.5 % of 3D; velocity vs optical probe 9.15 % (spout), 15.3–15.4 % (annulus, fountain) — `pp.80–117`. Restitution coefficient matters little; specularity mainly changes ΔP and annulus flow — `pp.97–99`.

## Data extracted

| Parameter | A (ref.) | B (matched) | Similar | Non-similar | Page |
|---|---|---|---|---|---|
| $D_c$ (m) | 0.152 | 0.076 | 0.076 | 0.076 | pp.27, 47 |
| Particles | glass 2.18 mm | steel 1.09 mm | steel 1.09 mm | glass 1.09 mm | pp.27, 48 |
| $U$ (m/s) | 1.08 | 0.75 | 0.64 | 1.04 | pp.27, 48 |
| $D_s/D_c$ | 0.27 | 0.257 | 0.28 | 0.277 | pp.45, 56 |
| $H_F/D_c$ | 0.89 | 0.75 | 0.78 | 0.58 | pp.45, 56 |
| $H_m/D_c$ | 2.6 | — | 2.56 | 3.15 | p.56 |

Common to all: 298 K, $H/D_c$ = 2.1, $D_c/D_i$ = 8 (pp.27, 48).

| Regime transition (1 mm glass, 2,450 kg/m³) | 0.152 m bed | 0.076 m bed | Page |
|---|---|---|---|
| Stable spouting onset | 0.72 m/s | 0.58 m/s | p.20 |
| Stable → unstable | 0.79 m/s | 0.66 m/s | p.20 |

> [!info] Inferred — the "similar" condition does not match He's groups
> The "similar" condition is He's case B (steel, 1.09 mm, $\rho_f$ 3.71 kg/m³) with gas velocity cut from 0.75 to 0.64 m/s (pp.27, 48). By the report's own Table 5 its groups differ from the reference: $\rho_f d_p U/\mu$ 297 vs 157, $U^2/gd_p$ 38.3 vs 54.5 (p.48). Matching profiles therefore required departing from the group-matching rule, which the report does not state. Confirmation: the authors' trial-run record.
> `#inferred`

> [!info] Inferred — stable spouting spans ~10–14 % of velocity
> From p.20: 0.79/0.72 = 1.10 and 0.66/0.58 = 1.14. Cold glass beads only.
> `#inferred`

## Figures kept

![[triso-scaleup-p22-fig15-grd-regime-indicator.jpeg]]
*Fig. 15, p.22 — GRD variance/mean vs gas velocity, 0.152 m bed: I packed, II stable spouting, III unstable.*

![[triso-scaleup-p49-fig52-gas-holdup-similar.jpeg]]
*Fig. 52, p.49 — gas holdup, "similar" condition: 0.152 m and 0.076 m profiles coincide.*

![[triso-scaleup-p49-fig53-gas-holdup-non-similar.jpeg]]
*Fig. 53 (H/D 1.1 and 1.8 panels), p.49 — "non-similar" condition: the spout diverges, the annulus matches.*

![[triso-scaleup-p122-fig118-spout-neck-crossflow.jpeg]]
*Fig. 118, p.122 — CFD solids fraction showing the spout neck (a) and velocity vectors with the two cross-flow zones (b).*

![[triso-scaleup-p124-fig119-temperature.jpeg]]
*Fig. 119, p.124 — CFD solids fraction at 293 K (a) and 1293 K (b); taller fountain when hot.*

Skipped: detector electronics, CT and RPT (radioactive particle tracking) hardware (pp.8–18, 72–77), per-level profile plots, factorial and correlation fits, appendix calibration rigs (pp.126–137).

## Internal inconsistencies
- Table 5 (pp.47–48): printed groups do not follow from the listed inputs — "non-similar" (glass 1.09 mm, 1.04 m/s) gives $\rho_f d_p U/\mu$ ≈ 76 and $U^2/gd_p$ ≈ 101 against printed 154 and 55.2; "similar" gives ≈ 143 against 297. Its $\rho_f$ of 3.71 kg/m³ fits ~312 kPa, not the 364 kPa listed. Non-similar $D_i$ printed as "9.5" m.
- Table 16 (p.106) repeats five rows and omits pressure and particle type.
- Case A spout diameter: 0.0395 m (p.45) vs 0.045 m (pp.56, 100). Case A maximum spoutable height 0.390 m (p.46) vs "396" (p.56, labelled m, evidently mm).
- Table 15 "simulated" fountain heights (p.105) equal the experimental Table 3 values (p.45) to three digits.
- Wall-condition fit: φ = 0.05 declared best (p.98), but its CFD fountain height, 0.584 m (p.91), is against a measured 0.25 m; only ΔP agrees (3.04 vs 3.00 kPa).
- Specularity meaning reversed between p.91 (φ = 0 free slip) and p.92 (φ = 0 "no-slip").
- p.124 labels viscosity as $\rho_g$ and attributes the temperature effect to solid-phase viscosity, which p.123 says was not modelled.
- PDF filename and cover title differ; cover title used here.

## What this changes in the wiki
- New concept page [[Spouted Bed Hydrodynamics]].
- Quantifies why scale-up needs re-optimisation on [[TRISO Coating Reactor Design]]; adds flat-slug circulation as a second fabrication-defect route.
- Adds an external monitoring method (GRD) to the "controlled blind" point on [[Fuel Quality Control and Characterization]] — proposed, cold-demonstrated only.
- Partly answers two [[Fluidization]] open questions: spouted-bed ΔP is weight plus wall shear, not weight alone; a hot-gas viscosity correlation (air only).

## Open questions raised
- The deferred tasks — cold-flow mimics of the AGR coater and real-coater CFD — were promised for 2013. A follow-up report or thesis would be the TRISO-specific result.
- Hot simulation used 2,500 kg/m³ glass in air; kernels are ~10,800 kg/m³ in Ar/H₂. Whether the temperature trend survives is untested.
- Whether GRD could see through a graphite retort and furnace at coater temperature; not addressed.

## Pages updated on ingest
- [[Spouted Bed Hydrodynamics]] (new), [[TRISO Coating Reactor Design]], [[Fluidization]], [[Fuel Quality Control and Characterization]], index
