---
type: source
title: Introduction to Fluidization
authors: [Cocco, R., Karri, S.B.R., Knowlton, T.]
org: Particulate Solid Research, Inc. (PSRI)
year: 2014
doc-id: CEP November 2014, pp.21–29, "Back to Basics"
journal: CEP (Chemical Engineering Progress), AIChE
pdf: raw/pdf/intro-to-fluidization.pdf
md: raw/md/intro-to-fluidization.md
pages: 9
ingested: 2026-10-02
status: draft
tags: [fluidization, fluidised-bed, geldart, gas-distributor, attrition, entrainment, tutorial]
updated: 2026-10-02
---

# Introduction to Fluidization
> PSRI (Particulate Solid Research, Inc.), 2014. CEP (Chemical Engineering Progress), November 2014, pp.21–29. Tutorial article, 9 pp. Page citations use the PDF page markers (p.1–9); journal pages are p.N + 20.
> [PDF](../raw/pdf/intro-to-fluidization.pdf) · [converted](../raw/md/intro-to-fluidization.md)

**Gist** — A chemical-engineering tutorial on gas–solid fluidised beds: the onset of fluidisation and the Wen–Yu estimate of minimum fluidisation velocity, two-phase (bubble/emulsion) gas flow, the regime sequence, Geldart particle classification, and design rules for distributors, attrition and entrainment. Written for industrial catalytic and combustion beds, not for coaters; nothing in it was derived for TRISO particles or for 1200–1600 °C operation. Treat it as general background and its rules of thumb as soft when applied to [[TRISO Coating Reactor Design]].

## Key findings
- **Fluidised-bed pressure drop equals bed weight** above minimum fluidisation, so bed inventory follows from ΔP — `p.2`, Eq. 1.
- **Minimum fluidisation velocity** from the Wen–Yu correlation via the Archimedes number; "the most popular" of several correlations — `p.2`, Eqs. 2–4.
- **Two-phase theory**: gas above $u_{mf}$ passes as bubbles that bypass the bed; corrected form adds a minimum bubbling velocity and bubble-gas fraction — `pp.2–3`, Eqs. 5–6.
- **Geldart classification applies only at ambient temperature and pressure**; pressure can shift a powder between groups and group boundaries are not sharp — `pp.3–4`.
- **Group D powders need large gas flows, form very large bubbles and slug, and are sometimes processed in spouted beds**, which need less gas — `p.4`.
- **Distributor pressure-drop rules**: per-orifice ΔP ≥ ⅓ ΔP_bed for beds > 0.3 m; ≥ ΔP_bed for shallow beds; never below 2,500 Pa. Too little ΔP lets the bed's own hydrodynamics set where gas goes — `p.5`, Eqs. 7–8.
- **Jet penetration correlations are unreliable for large or non-spherical particles** — `p.6`.
- **Entrainment correlations can differ by two orders of magnitude** for particles < 50 µm; measure first for a new particle type — `p.7`.

## Data extracted

| Parameter | Value | Conditions | Page |
|---|---|---|---|
| Group A size; density | 30–125 µm; ~1,500 kg/m³ | ambient | p.3 |
| Group A maximum bubble size | typically ≤ 20 cm | | p.3 |
| Group A bed expansion | ≥ 100 % | high pressure | p.3 |
| Group B size | 150–1,000 µm | $u_{mb} \approx u_{mf}$ | p.3 |
| Group C size | typically < 30 µm | cohesive | p.3 |
| Slugging onset | bubble > ⅔ bed diameter | | p.3 |
| Bed height | 0.3–0.5 m dryers/heat treaters; 1–10 m reactors | | p.4 |
| Minimum distributor ΔP | 2,500 Pa | | p.5 |
| Distributor jet velocity | > 30 m/s (100 ft/s) | | p.6 |
| Particle velocity in jet | > 15 m/s (50 ft/s) | | p.6 |
| Jet–wall / jet–jet collision speed | ≥ 13 m/s (30 mph); > 27 m/s (60 mph) | | p.6 |
| Bubbling-bed natural frequency | 1–5 Hz | | p.6 |
| Fines (attrition product) | < 40 µm | | p.6 |

Equations are on [[Fluidization]].

## Figures kept

![[fluidization-p02-fig01-umf-curve.jpeg]]
*Fig. 1, p.2 — pressure drop (red) and bed height (blue) against superficial gas velocity; ΔP plateaus at $u_{mf}$.*

![[fluidization-p03-fig03-regimes.jpeg]]
*Fig. 3, p.3 — regime sequence with increasing gas velocity.*

![[fluidization-p03-fig04-geldart-chart.jpeg]]
*Fig. 4, p.3 — Geldart chart: particle − fluid density against Sauter mean diameter. Ambient conditions only.*

![[fluidization-p04-fig06-distributor-types.jpeg]]
*Fig. 6, p.4 — grid plates (bubble-cap, slit-nozzle, perforated) and spargers (treed, ringed, orthogonal).*

![[fluidization-p05-fig07-shrouds.jpeg]]
*Fig. 7, p.5 — shrouded vs unshrouded bubble caps and sparger orifices; weeped solids in an unshrouded sparger.*

![[fluidization-p06-fig08-tdh.jpeg]]
*Fig. 8, p.6 — solids volume fraction above a bubbling bed; TDH (transport disengagement height). Height axis units not given.*

Skipped: Fig. 2 (two-phase cartoon), Fig. 5 (generic reactor), Figs. 9–10 (cyclones). Cyclone design (pp.7–9) and the industrial history (p.1) are not ingested, per Nelson and rule 10.

## Errors in the source
- "A skydiver's terminal velocity is about 120 mph (155 km/sec)" (p.6): 120 mph is ~193 km/h.
- Eq. 1 prints the bed-weight term as $\rho_p(1-\varepsilon)-\rho_g$ (p.2); the usual form is $(\rho_p-\rho_g)(1-\varepsilon)$. Immaterial here because $\rho_g$ is then neglected.

## What this changes in the wiki
- New concept page [[Fluidization]].
- First source for the Geldart chart itself; [[TRISO Coating Reactor Design]] previously had Geldart D only via [[A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production|Hu et al. 2025]] p.2. Corroborates Group D → spouted bed.
- First quantitative rule behind the weeping and flow-reversal concerns in the nozzle redesign on [[TRISO Coating Reactor Design]] — for grid plates, applicability to spouted-bed nozzles unestablished.
- General mechanism (bubble eruption into the freeboard) consistent with the soot-ejection path on [[TRISO Coating Reactor Design]].

## Open questions raised
- Does ΔP across a spouted coater bed track bed mass as Eq. 1 does for a fluidised bed? If so it is an in-process diagnostic none of the coater sources mention. Needs a spouted-bed source.
- $u_{mf}$ for kernels in Ar or H₂ at 1200–1600 °C: Eqs. 2–4 can compute it, but need sourced gas density and viscosity at temperature.

## Pages updated on ingest
- [[Fluidization]] (new), [[TRISO Coating Reactor Design]], index
