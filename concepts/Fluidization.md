---
type: concept
title: Fluidization
status: draft
sources: 5
tags: [fluidization, fluidised-bed, spouted-bed, geldart, gas-distributor, attrition, entrainment, inferred]
updated: 2026-10-11
---

# Fluidization

**In one line** — A particle bed fluidises when upward gas drag equals bed weight; above that point extra gas passes as bubbles, and particle size and density (the Geldart group) decide how the bed behaves — which for TRISO kernels is the large, dense Group D that is usually spouted rather than fluidised.

General gas–solid theory. Its application to coaters: [[TRISO Coating Reactor Design]]. Short form of the main source: Cocco et al. 2014 = [[Introduction to Fluidization]], a chemical-engineering tutorial not written for coaters or for 1200–1600 °C.

## Onset of fluidisation

Pressure drop rises with superficial gas velocity $u_o$ through a packed bed (Ergun regime) until drag equals bed weight, at the minimum fluidisation velocity $u_{mf}$. Beyond it ΔP stays at the bed weight, so ΔP gives the bed inventory (Cocco et al. 2014 p.2):

$$\Delta P_{bed} = H_{bed}\,\frac{g}{g_c}\,\rho_{bulk}$$

$H_{bed}$ fluidised bed height, $g_c$ force–weight conversion factor, $\rho_{bulk}$ bulk density; gas density is neglected (p.2).

$u_{mf}$ for spheres, Wen–Yu correlation (p.2, Eqs. 2–4), with $d_p$ the Sauter mean diameter and $\mu$ gas viscosity:

$$Ar = \frac{\rho_g d_p^3(\rho_p-\rho_g)g}{\mu^2},\qquad Ar = 1650\,Re_{p,mf} + 24.5\,Re_{p,mf}^2,\qquad Re_{p,mf} = \frac{\rho_g u_{mf} d_p}{\mu}$$

Measured $u_{mf}$ of ZrO₂ surrogates (0.2–0.65 mm, 6,050 kg/m³) follows Wen–Yu closely ([[Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating|Zhou et al. 2005]] pp.4–5, Fig. 4).

![[fluidization-p02-fig01-umf-curve.jpeg]]
*ΔP (red) plateaus at $u_{mf}$ while bed height (blue) rises. Cocco et al. 2014 p.2, Fig. 1.*

## Gas flow above minimum fluidisation

Two-phase theory: gas up to $u_{mf}$ flows through the dense (emulsion) phase; the excess flows as bubbles, which bypass the solids (p.2):

$$Q_{bed} = A_{bed}u_{mf} + A_{bed}(u_o - u_{mf})$$

Corrected for smooth fluidisation below the minimum bubbling velocity $u_{mb}$ and for gas exchange with bubbles, $Y$ being the bubble gas fraction (p.3):

$$Q_{bed} = (1-Y)A_{bed}u_{mb} + YA_{bed}(u_o - u_{mb})$$

Larger bubbles rise faster, so bubble size governs gas–solid contact (p.2).

## Regimes

Packed → smooth (small or light particles only) → bubbling → turbulent (elongated voids, diffuse bed surface) → fast fluidisation (all particles entrained) → conveying (p.3). Slugging occurs when bubbles exceed ~⅔ of the bed diameter and the walls stabilise them (p.3).

![[fluidization-p03-fig03-regimes.jpeg]]
*Cocco et al. 2014 p.3, Fig. 3.*

A spouted bed (zones, regimes and scale-up: [[Spouted Bed Hydrodynamics]]) is a fluidised bed in which gas moves mainly up the centre; it needs less gas than a standard fluidised bed (p.4). At coater temperatures and particle sizes the INL (Idaho National Laboratory) coater lies outside the mapped spouted-bed regions and runs pulsatory rather than stable spouting ([[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.6).

## Geldart classification

Behaviour predicted from Sauter mean diameter and particle − fluid density (Cocco et al. 2014 p.3, Fig. 4). **Valid at ambient temperature and pressure only**; pressure can move a powder between groups, and boundaries are not sharp (pp.3–4).

| Group | Size | Behaviour | Page |
|---|---|---|---|
| C — cohesive | < 30 µm | channelling, clustering; needs vibration, pulsing or added coarse particles | pp.3–4 |
| A — aeratable | 30–125 µm, ~1,500 kg/m³ | smooth fluidisation before bubbling; bubbles ≤ 20 cm | p.3 |
| B — sand-like | 150–1,000 µm | bubbles at onset, $u_{mb} \approx u_{mf}$; can slug | p.3 |
| D — spoutable | largest/densest | large gas demand, very large bubbles, slugging; often spouted | p.4 |

![[fluidization-p03-fig04-geldart-chart.jpeg]]
*Cocco et al. 2014 p.3, Fig. 4.*

> [!info] Inferred — where TRISO particles sit on the chart
> The B/D boundary read off Fig. 4 follows $(\rho_p-\rho_f)\,d_p^2 \approx 9.5\times10^{5}$ g·cm⁻³·µm² ≈ 1 × 10⁻³ kg/m (two points: ~350 µm at ~8 g/cm³, ~2,200 µm at ~0.19 g/cm³). Ratio of each particle's $\rho_p d_p^2$ to that value:
>
> | Particle | $d_p$ (µm) | $\rho_p$ (g/cm³) | × boundary | Basis |
> |---|---|---|---|---|
> | AGR-1 UCO kernel | 350 | 10.92 | 1.4 | [[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels\|Jolly et al. 2016]] p.3 |
> | INL kernel | 425 | 11.1 | 2.1 | [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.5 |
> | INET UO₂ kernel | 500 | 10.8 | 2.8 | [[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]] p.2 |
> | ORNL ZrO₂ surrogate | 814 | 6.03 | 4.2 | Jolly et al. 2016 p.7 |
> | INL coated particle, end of run | ~850 | ~3 | 2.3 | diameter "roughly doubles" from 425 µm, ~3 g/cm³ (Spouted Bed p.2) |
>
> All are Group D throughout coating, matching [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] p.2. For the INL line the coating run barely moves the particle (2.1 → 2.3): the fall in density and the rise in diameter roughly cancel. Caveat: the chart is ambient-only and coaters run at 1200–1600 °C; gas density is negligible either way, but the chart does not capture viscosity. Confirmation would need a high-temperature classification or measured $u_{mf}$.
> `#inferred`

> [!warning] Conflict — Group B or Group D
> [[Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating|Zhou et al. 2005]] p.4 classes 300, 400, 500 and 650 µm ZrO₂ (6,050 kg/m³) as Geldart Group B. By the boundary read above they sit at 0.57×, 1.0×, 1.6× and 2.7× — B, borderline, D, D — and [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] p.2 classes kernels as Group D. Group boundaries are not sharp (Cocco et al. 2014 p.4). Unresolved.
> `#conflict`

## Distributors

The distributor's ΔP must dominate the bed's, or bed hydrodynamics choose the gas path (Cocco et al. 2014 p.5):

| Bed | Rule | Page |
|---|---|---|
| Tall (> 0.3 m) | $\Delta P_{orifice} \ge \tfrac{1}{3}H_{bed}\tfrac{g}{g_c}\rho_{bulk}$ | p.5, Eq. 7 |
| Shallow (dryers, heat treaters) | $\Delta P_{orifice} \ge H_{bed}\tfrac{g}{g_c}\rho_{bulk}$ | p.5, Eq. 8 |
| Any | ≥ 2,500 Pa | p.5 |

Adequate orifice ΔP also limits weeping of solids into the plenum or sparger; bubble caps and shrouds reduce it further (pp.4–5). Jets exceed 30 m/s (100 ft/s), and must not reach walls, internals or each other; published penetration correlations hold for Group A and B but scatter widely for large, non-spherical or high-pressure systems (p.6). Distributors must survive bed slump on power loss and thermal expansion (conical and convex plates are used), and avoid resonance with the bubbling frequency of 1–5 Hz (p.6).

![[fluidization-p04-fig06-distributor-types.jpeg]]
*Grid plates and spargers. Cocco et al. 2014 p.4, Fig. 6.*

![[fluidization-p05-fig07-shrouds.jpeg]]
*Shrouds limit particle entrainment into jets and weeping. p.5, Fig. 7.*

## Attrition

Two modes: fragmentation (parent breaks into daughters) and abrasion (edges and protrusions removed, producing fines < 40 µm) (Cocco et al. 2014 p.6). Sources are distributor jets — particles in them exceed 15 m/s (50 ft/s), and jet–wall and jet–jet impacts reach ≥ 13 m/s (30 mph) and > 27 m/s (60 mph) — and cyclones (p.6). Crush strength does not predict attrition, which is dynamic; it is tested by ball mill, jet impact, immersed jet, or most often jet cup (p.6). Mitigation: attrition-resistant particles, jets that do not intersect or impinge, and shrouds (p.6).

## Entrainment

A particle leaves the bed when local gas velocity exceeds its terminal velocity, but entrainment starts well below the single-particle terminal velocity: local velocities exceed $u_o$, size distributions are wide (elutriation), and bursting bubbles eject particles into the freeboard (pp.6–7). Larger particles fall back below the TDH (transport disengagement height); only fines remain entrained above it (p.7). Entrainment correlations disagree by up to two orders of magnitude for particles < 50 µm, partly because fines form clusters; measure entrainment for a new particle before trusting a correlation or CFD (computational fluid dynamics) model (p.7).

![[fluidization-p06-fig08-tdh.jpeg]]
*Solids fraction above a bubbling bed; TDH marked. Height units not given. Cocco et al. 2014 p.6, Fig. 8.*

## Design implications for HTGR fuel coaters

- Kernels are Group D, which is why coaters are spouted, not grid-fluidised — see [[TRISO Coating Reactor Design]].
- The distributor ΔP rules are the general form of the weeping and flow-reversal constraints on coater nozzles; they are written for grid plates and spargers, and the source warns its jet correlations do not hold for large particles (p.6).
- Freeboard ejection is the general mechanism for the soot-inclusion route on [[TRISO Coating Reactor Design]], where bed ejecta carries soot back into the bed.

## Contested / uncertain

- Whether Eq. 1 holds for a spouted bed, which would make bed ΔP an in-process measure of bed mass on coaters that otherwise run without internal instrumentation ([[Fuel Quality Control and Characterization]]). Partly answered: in a spouted bed ΔP balances bed weight **and wall shear**, and in cold-flow CFD it varies 2.19–3.45 kPa with wall friction alone ([[Advancing the Fundamental Understanding and Scale-up of TRISO Fuel Coaters via Advanced Measurement and Computational Techniques|Biswas & Al-Dahhan 2012]] pp.91–92), so Eq. 1 does not hold as written. No coater source reports bed ΔP.
- $u_{mf}$ of kernels at coating temperature: computable from the Wen–Yu equations above once gas properties at 1200–1600 °C are sourced. Air is now sourced — $\mu_g = 1.46\times10^{-6}T^{1.504}/(T+120)$, $\rho_g = 1.2\cdot293/T$ ([[Advancing the Fundamental Understanding and Scale-up of TRISO Fuel Coaters via Advanced Measurement and Computational Techniques|Biswas & Al-Dahhan 2012]] p.123) — but coaters run in Ar and H₂.

## Sources
- [[Introduction to Fluidization]]
- [[Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating]]
- [[Advancing the Fundamental Understanding and Scale-up of TRISO Fuel Coaters via Advanced Measurement and Computational Techniques]] · spouting: [[Spouted Bed Hydrodynamics]]
- [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]]
- [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production]]
- Particle data for the inferred table: [[Fabrication and Characterization of Surrogate TRISO Particles Using 800 µm ZrO2 Kernels]] · [[Preparation of the Coated Nuclear Fuel Particle Using the FB-CVD Method]]
