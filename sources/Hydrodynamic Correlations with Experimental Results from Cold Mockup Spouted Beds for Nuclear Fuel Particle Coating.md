---
type: source
title: Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating
authors: [Zhou, J., Bruns, D.D., Finney, C.E.A., Daw, C.S., Pannala, S., McCollum, D.L.]
org: University of Tennessee, Knoxville; ORNL
year: 2005
doc-id: none printed (year from PDF metadata; venue not stated)
pdf: "raw/pdf/Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating .pdf"
md: raw/md/hydrodynamic-correlations-with-experimental-results-from-cold-mockup-spouted-bed.md
pages: 19
ingested: 2026-10-11
status: draft
tags: [spouted-bed, coater, zro2, surrogate, minimum-spouting-velocity, pressure-fluctuation, geldart, conflict, inferred]
updated: 2026-10-11
---

# Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating
> University of Tennessee / ORNL (Oak Ridge National Laboratory), ~2005 (no date or venue printed; PDF created October 2005, cites a 2004 ORNL report). Conference-style paper, 19 pp. Funded by DOE-NERI (Nuclear Energy Research Initiative) and UT-Battelle.
> [PDF](../raw/pdf/Hydrodynamic%20Correlations%20with%20Experimental%20Results%20from%20Cold%20Mockup%20Spouted%20Beds%20for%20Nuclear%20Fuel%20Particle%20Coating%20.pdf) · [converted](../raw/md/hydrodynamic-correlations-with-experimental-results-from-cold-mockup-spouted-bed.md)

**Gist** — A room-temperature mockup of the 5 cm spouted-bed coater, run with ZrO₂ surrogate particles (300–650 µm, 6,050 kg/m³) in humidified air across three cone angles and four bed inventories. It measures minimum fluidisation and minimum spouting velocity, fits correlations for minimum spouting velocity and mean bed pressure drop, and characterises the pressure-drop fluctuations statistically and spectrally as regime indicators. The first spouted-bed data in the wiki at TRISO-surrogate density and size. Single group, no stated peer review; Eq. 2 is unusable as printed.

## Key findings
- **u_mf of ZrO₂ follows the Wen–Yu correlation** across 0.2–0.65 mm — `pp.4–5`, Figs. 3–4. See [[Fluidization#Onset of fluidisation]].
- **Minimum spouting velocity from the bed-ΔP minimum**: lowering flow, ΔP falls to a minimum at $U_{ms}$ and rises sharply below it; particles visibly stop at a slightly higher velocity — `pp.5–6`, Fig. 5. Said to be more reproducible than visual observation.
- **$U_{ms}$ correlation for dense particles**: $Re_{ms} = 0.0015\,Ar^{0.86}(H_0/D_c)^{1.59}\tan(\gamma/2)^{0.87}$, regression coefficient 0.98, error 8–13 % for $H_0/D_c \le 1$ — `p.6`, Eq. 1. Literature correlations, built on particles ≤ ~3,000 kg/m³, are said to err by 12–60 % at best — `p.6`. $U_{ms}$ rises with cone angle — `p.8`.
- **Stable spouting from 1.0 to 1.9 $U/U_{ms}$**; below 1 spouting stops, above 2 it is unstable and particles are carried out — `p.4`.
- **Mean ΔP**: log ΔP linear in log tan(γ/2) and in log($H_0/D_c$); rises with $D_p$; cubic in $U/U_{ms}$ — `pp.8–10`. Correlation Eq. 2: 273 points, r² 0.93, error < 15 % — `p.10` (but see inconsistencies).
- **Spectral signature**: dominant ΔP frequency (bubble formation) falls from 21.4 to 17.4 Hz as flow drops from 2.3 to 1.3 $U_{ms}$; at 1.2 $U_{ms}$ it splits and an annulus-vibration peak up to 25.3 Hz dominates — `p.12`, Figs. 11–12. Frequency rises with $D_p$, $H_0/D_c$ and cone angle; 0.5 mm particles give the sharpest peak — `pp.14–15`.
- **Moments**: standard deviation, skewness and kurtosis of ΔP mostly rise as flow approaches $U_{ms}$ (exceptions: 0.5 mm std. dev., 0.65 mm skewness) — `p.17`.
- **Bed ΔP is available on hot coaters**, "one of the most easily obtained process signals from mockup coaters and hot coaters"; cold-mockup signals are being compared with hot-coater signals to infer coater status — `p.2`.
- Context, single-source: coaters run at 1200–1800 °C; then-current coaters were 5 cm experimental units; optical observation of hot coaters is impossible because of the opaque carbon wall and soot — `p.2`. Particles classed **Geldart Group B** — `p.4`.

## Data extracted

| Parameter | Value | Page |
|---|---|---|
| Column diameter $D_c$ | 0.05 m (quartz column, aluminium cone) | p.3 |
| Inlet throat $D_i$ | 0.004 m | p.3 |
| Cone angles | 45°, 60°, 75° | p.3 |
| ZrO₂ sizes; density | 300, 400, 500, 650 µm; 6,050 kg/m³ | p.3 |
| Static bed height $H_0/D_c$ | 0.50, 0.55, 0.60, 0.65 | p.1 |
| Gas | humidified air, 70–79 °F (21–26 °C), ~740 mmHg (~98.7 kPa) | p.3 |
| ΔP sampling | 1,000 Hz for 1 min | p.3 |
| $U_{ms}$, 0.5 mm, 60°, 53.9 g | 12 L/min | p.6 |

$U_{ms}$, 0.5 mm, 45° (Table 1, p.6):

| $H_0/D_c$ | Measured (m/s) | Eq. 1 (m/s) |
|---|---|---|
| 0.5 | 0.0450 | 0.0393 |
| 0.6 | 0.0586 | 0.0525 |
| 0.8 | 0.0874 | 0.0829 |
| 1.0 | 0.1290 | 0.1182 |

> [!info] Inferred — Table 1 mixes velocity bases
> Literature methods 1–4 in Table 1 predict 3.78–35.4 m/s against measured 0.045–0.129 m/s (p.6). Scaling the measured column-based 0.045 m/s by the area ratio $(D_c/D_i)^2 = (50/4)^2 = 156$ gives ~7.0 m/s at the inlet, against method 1's 7.43 m/s. Methods 1–4 are most likely inlet-velocity correlations, so the paper's large reported errors for them are mainly a basis mismatch. Eq. 1 itself checks out: with air at 298 K from [[Advancing the Fundamental Understanding and Scale-up of TRISO Fuel Coaters via Advanced Measurement and Computational Techniques|Biswas & Al-Dahhan 2012]] p.123 (μ ≈ 1.84 × 10⁻⁵ Pa·s, ρ ≈ 1.18 kg/m³) and the standard Archimedes number, it gives $U_{ms}$ ≈ 0.045 m/s at $H_0/D_c$ 0.5, 45°. Confirmation: the cited method papers.
> `#inferred`

> [!warning] Conflict — Geldart group
> This source classes all four ZrO₂ sizes as Geldart Group B (p.4). [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] p.2 classes TRISO kernels as Group D, and the wiki's reading of the Geldart chart ([[Fluidization#Geldart classification]], `#inferred`) puts these particles at 0.57× (300 µm), 1.0× (400 µm), 1.6× (500 µm) and 2.7× (650 µm) the B/D boundary — B, borderline, D, D. Different classifications of overlapping particles; boundaries are not sharp ([[Introduction to Fluidization|Cocco et al. 2014]] p.4). Unresolved.
> `#conflict`

## Figures kept

![[zrO2-spouted-p05-fig04-umf-wen-yu.jpeg]]
*Fig. 4, p.5 — measured u_mf of ZrO₂ against the Wen–Yu prediction.*

![[zrO2-spouted-p06-fig05-ums-dp-minimum.jpeg]]
*Fig. 5, p.6 — bed ΔP vs gas flow; the minimum marks $U_{ms}$ (12 L/min). 0.5 mm, 60°, 53.9 g.*

![[zrO2-spouted-p11-fig12-main-frequency.jpeg]]
*Fig. 12, p.11 — dominant ΔP frequency vs $U/U_{ms}$: falls with flow above 1.3, jumps to the annulus-vibration peak at 1.2.*

Skipped: photographs (Figs. 1–2), ΔP trend plots (Figs. 6–10), per-size spectra and moment plots (Figs. 13–22).

## Internal inconsistencies
- **Eq. 2 (p.10) gives negative ΔP**: its polynomial $56.38x^3 - 179.6x^2 + 110.01x - 74.35$ is −87.6 at $x = U/U_{ms} = 1$ and −123 at 1.5, negative across the stated 1–1.9 range, while the multiplying power terms are positive. Checked against the PDF render. A sign or coefficient is wrong; trends are kept, the equation is not usable.
- Inlet throat 0.04 cm in the abstract (p.1) vs 0.004 m in the text (p.3).
- Nomenclature gives $U$ and $U_{ms}$ in m³/s and $D_p$ in mm (p.19); Table 1 uses m/s.
- The Archimedes number is defined without $\rho_g$ (p.19).
- The text cites "figure 5 and figure 6" for the $D_p$ effect (p.10); the relevant figures are 9 and 10.
- Fig. 7 (p.8) shows four $H/D_c$ series for a fixed 53.9 g bed.
- PDF metadata title says "Advanced Fuel Particle Coating"; page title used here.

## What this changes in the wiki
- First spouted-bed data at surrogate density and size — [[Spouted Bed Hydrodynamics]].
- Contradicts the narrow stable-spouting window from Biswas & Al-Dahhan 2012 — conflict on [[Spouted Bed Hydrodynamics]].
- Contradicts the Group D classification — conflict on [[Fluidization]] and here.
- Validates Wen–Yu on ZrO₂ — [[Fluidization]].
- Adds bed ΔP as an external signal on hot coaters — [[TRISO Coating Reactor Design]], [[Fuel Quality Control and Characterization]].

## Open questions raised
- The hot-coater ΔP comparison and the simulation validation (ref. [16], ORNL/CF-04/11) are not reported here.
- Whether the dominant-frequency signature holds at coater temperature and with kernels at ~10,800 kg/m³.

## Pages updated on ingest
- [[Spouted Bed Hydrodynamics]], [[Fluidization]], [[TRISO Coating Reactor Design]], [[Fuel Quality Control and Characterization]], index
