---
type: concept
title: Spouted Bed Hydrodynamics
status: draft
sources: 5
tags: [spouted-bed, fluidization, scale-up, cfd, coater, inferred, conflict]
updated: 2026-10-11
---

# Spouted Bed Hydrodynamics

**In one line** — A spouted bed circulates coarse particles up a central gas jet, out through a fountain and down a slowly moving annulus; its stable-spouting window is reported anywhere from ~10 % to ~90 % above minimum spouting velocity, its scale-up does not follow from matched dimensionless groups alone, and it is the bed type every TRISO coater in the wiki uses.

General theory of gas–solid beds: [[Fluidization]]. Coater equipment built on it: [[TRISO Coating Reactor Design]]. Short form of the main source: Biswas & Al-Dahhan 2012 = [[Advancing the Fundamental Understanding and Scale-up of TRISO Fuel Coaters via Advanced Measurement and Computational Techniques]] — cold-flow, unreviewed grant report; its numbers are soft.

## Zones and circulation

Gas enters as a jet at the cone apex and carries solids up the **spout**; at the bed surface they form a **fountain** and fall onto the **annulus**, which moves down and inward as a loose packed bed and feeds solids back into the spout (Biswas & Al-Dahhan 2012 pp.28–29). Spout solids holdup rises with height as the jet loses velocity; annulus holdup stays near loose packing at every height (p.29). Cold-flow CFD shows the spout is not straight but necks near the top, and solids cross from annulus to spout mainly at the inlet and at the neck (pp.121–122).

![[triso-scaleup-p122-fig118-spout-neck-crossflow.jpeg]]
*Spout neck and the two cross-flow zones (CFD, 0.152 m bed). Biswas & Al-Dahhan 2012 p.122, Fig. 118.*

Spouting suits Geldart Group D particles and needs less gas than conventional fluidisation ([[Introduction to Fluidization|Cocco et al. 2014]] p.4); TRISO kernels are classed Group D ([[Fluidization#Geldart classification]]), though a ZrO₂-surrogate study classes its 300–650 µm particles as Group B — see the conflict there.

## Regimes

Packed bed → stable spouting → unstable spouting (swirling, pulsating spout); bubbling and slugging also occur (Biswas & Al-Dahhan 2012 p.19). For 1 mm glass beads:

| Bed | Stable spouting onset | Stable → unstable | Page |
|---|---|---|---|
| 0.152 m | 0.72 m/s | 0.79 m/s | p.20 |
| 0.076 m | 0.58 m/s | 0.66 m/s | p.20 |

That is a window of ~10–14 % above onset (`#inferred`, ratio of the values above). A 5 cm mockup with 300–650 µm ZrO₂ at 6,050 kg/m³ reports stable spouting from 1.0 to 1.9 $U/U_{ms}$, unstable with particle carry-over above 2 ([[Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating|Zhou et al. 2005]] p.4).

> [!warning] Conflict — width of the stable-spouting window
> Biswas & Al-Dahhan 2012 p.20: stable spouting ends at 1.10–1.14 × onset (1 mm glass, 2,450 kg/m³, 0.076–0.152 m beds, `#inferred` ratio). Zhou et al. 2005 p.4: stable to 1.9 $U_{ms}$ (0.3–0.65 mm ZrO₂, 6,050 kg/m³, 0.05 m bed, $D_c/D_i$ = 12.5). Different particles, bed sizes and regime criteria (count statistics vs visual/ΔP). Unresolved; the window for real kernels at coater temperature is unknown.
> `#conflict`

Geometry for stable spouting: $D_i/d_p < 25$–$30$, $D_c/D_i > 3$–$12$, bed height below the maximum spoutable height $H_m$ (p.19).

The INL (Idaho National Laboratory) coater lies outside the mapped spouting regions at coating temperature and runs pulsatory, not stable ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.6), although stable spouting is the preferred regime ([[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] p.2).

## Characteristic quantities

| Quantity | Behaviour (cold flow) | Page |
|---|---|---|
| Minimum spouting velocity $U_{ms}$ | onset of spouting; used to non-dimensionalise particle velocity | p.37 |
| $U_{ms}$, dense particles | $Re_{ms} = 0.0015\,Ar^{0.86}(H_0/D_c)^{1.59}\tan(\gamma/2)^{0.87}$ for ZrO₂, 8–13 % error, $H_0/D_c \le 1$; rises with cone angle | Zhou et al. 2005 pp.6, 8 |
| $U_{ms}$ measurement | minimum of bed ΔP on a falling-flow sweep; ΔP rises sharply below it | Zhou et al. 2005 pp.5–6 |
| Spout diameter $D_s$ | ~0.26–0.28 $D_c$ in the cases tested; depends on solids density, bed height, $d_p$, $U$ and inlet diameter | pp.45, 67–71 |
| Fountain height $H_F$ | most sensitive global quantity to mismatched conditions (−46 % to +70 %) | p.45 |
| Maximum spoutable height $H_m$ | peaks at $d_p$ ≈ 1–2 mm; falls with larger inlet and higher gas flow; McNab–Bridgwater fits poorly | pp.63–66 |

## Pressure drop

Bed pressure drop is balanced by bed weight **and** wall shear (Biswas & Al-Dahhan 2012 p.92), so the fluidised-bed relation ΔP = bed weight ([[Fluidization#Onset of fluidisation]]) does not carry over directly. In CFD the bed ΔP spans 2.19–3.45 kPa on wall friction alone (p.91, Table 10). Wall pressure fluctuations are largest in the conical section (p.42).

With ZrO₂ surrogates, mean ΔP rises log-linearly with tan(γ/2) and with $H_0/D_c$, rises with particle size, and is cubic in $U/U_{ms}$ ([[Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating|Zhou et al. 2005]] pp.8–10). Its fitted correlation (Eq. 2) gives negative ΔP as printed and is not usable (source page).

![[zrO2-spouted-p06-fig05-ums-dp-minimum.jpeg]]
*Bed ΔP minimum marks $U_{ms}$. Zhou et al. 2005 p.6, Fig. 5.*

## Scale-up

Matching the He et al. (1997) dimensionless groups between a 0.152 m and a 0.076 m bed reproduced global quantities — spout diameter within 0.77 %, fountain height 15 %, $H_m$ 5.65 % — but not radial profiles: solids holdup 15–26.5 %, particle velocity 31–46 %, the differences confined to the spout (Biswas & Al-Dahhan 2012 pp.33–46; CFD agrees, pp.103–105). The report proposes matching the radial gas-holdup profile instead: 4.1 % holdup and 3.5 % velocity difference for its "similar" condition, against 55.8 % and 47.9 % for a "non-similar" one (pp.47–51).

![[triso-scaleup-p49-fig52-gas-holdup-similar.jpeg]]
*Gas holdup, "similar" condition, two bed sizes. p.49, Fig. 52.*

![[triso-scaleup-p49-fig53-gas-holdup-non-similar.jpeg]]
*"Non-similar" condition: the spout diverges, the annulus matches. p.49, Fig. 53.*

The "similar" condition itself departs from He's groups (`#inferred`, see source page), so the proposal is a target to search for — by trial or CFD — not a rule that sets conditions. This is consistent with INL's finding that coater setpoints need re-optimising at each retort diameter ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] pp.4, 6).

## Temperature

In CFD with 0.5 mm, 2,500 kg/m³ glass in air, maximum spouted height rose from 293 K to 1293 K, attributed to air viscosity rising from 1.8 × 10⁻⁵ to 4.94 × 10⁻⁵ Pa·s and so to higher drag (Biswas & Al-Dahhan 2012 p.124; correlation p.123, Eq. 85). Air only; particle density ~¼ of a UO₂ kernel's.

![[triso-scaleup-p124-fig119-temperature.jpeg]]
*293 K (a) vs 1293 K (b). p.124, Fig. 119.*

## Measurement

- **Gamma-ray densitometry** — external Cs-137 source and NaI detector; regime read from count variance/mean; transitions within 3.4 % of pressure-fluctuation results (Biswas & Al-Dahhan 2012 p.20). Proposed for on-line coater monitoring; demonstrated cold, one height (pp.5, 13).
- **Gamma-ray CT** — time-averaged cross-sectional holdup; optical probe within 9.6 % of it (p.62).
- **Optical fibre probe** — local holdup and velocity; invasive (p.19).
- **Wall pressure transducers** — regime from fluctuations; wall-only view (p.19).
- **Bed ΔP spectrum** — dominant frequency (bubble formation) falls from 21.4 to 17.4 Hz as flow drops from 2.3 to 1.3 $U_{ms}$, then jumps to an annulus-vibration peak (up to 25.3 Hz) at 1.2 $U_{ms}$; std. dev., skewness and kurtosis mostly rise toward $U_{ms}$ ([[Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating|Zhou et al. 2005]] pp.12, 17). Bed ΔP is already measured on hot coaters (p.2).

![[zrO2-spouted-p11-fig12-main-frequency.jpeg]]
*Dominant ΔP frequency vs $U/U_{ms}$, 0.5 mm ZrO₂. Zhou et al. 2005 p.11, Fig. 12.*

![[triso-scaleup-p22-fig15-grd-regime-indicator.jpeg]]
*GRD variance/mean marks packed (I), stable (II) and unstable (III) spouting. p.22, Fig. 15.*

## Modelling

Two-fluid CFD with kinetic theory of granular flow and Gidaspow drag reproduced cold-flow particle velocity to 9.15 % in the spout and ~15 % in annulus and fountain; 2D axisymmetric runs came within 3.5 % of 3D (Biswas & Al-Dahhan 2012 pp.89, 114–117). The wall friction (specularity) coefficient changes ΔP and annulus flow strongly; particle–wall restitution barely matters (pp.97–99). Model details: source page.

## Design implications for HTGR fuel coaters

- A "flat" slug over the gas inlet impairs circulation and is said to cause non-spherical particles, coating flaws and missing layers (Biswas & Al-Dahhan 2012 pp.7, 123; uncited there, single-source) — a fabrication-defect route alongside soot inclusion on [[TRISO Coating Reactor Design]].
- Cone angle matters: solids velocity peaked at 45° among 30°, 45°, 60° (p.114); INL replaced single-angle cones with a curvilinear profile ([[TRISO Coating Reactor Design]]).
- Cold-flow scale-up results transfer to coaters only through the mimic conditions the report did not complete (p.125).

> [!info] Inferred — inlet size for a kernel bed
> Applying $D_i/d_p < 25$–$30$ (p.19) to the 425 µm INL kernel gives a single inlet below ~11–13 mm; at the end of coating (~850 µm) below ~21–26 mm. INL uses a multi-orifice nozzle, so the criterion may not apply as written. Derived here, not stated by any source.
> `#inferred`

## Contested / uncertain

- All hydrodynamic data are cold air with glass or steel; none at coater temperature with dense kernels in Ar or H₂.
- The source's tables carry several internal inconsistencies (source page); the qualitative results are firmer than the percentages.

## Sources
- [[Advancing the Fundamental Understanding and Scale-up of TRISO Fuel Coaters via Advanced Measurement and Computational Techniques]]
- [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]]
- [[Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating]]
- [[Introduction to Fluidization]]
- [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production]]
