---
type: concept
title: PyC Layer Deposition
status: draft
sources: 5
tags: [triso, pyc, ipyc, opyc, buffer, cvd, density, anisotropy, porosity, permeability, conflict]
updated: 2026-10-14
---

# PyC Layer Deposition

**In one line** — The three pyrocarbon layers are grown by pyrolysing acetylene and propylene in argon; deposition temperature sets density and permeability, coating gas fraction sets rate and open porosity, and anisotropy — the property that governs whether the particle survives irradiation — follows neither cleanly.

Layer functions: [[TRISO Particle Architecture]]. Place in the sequence: [[TRISO Coating Process]]. The SiC counterpart: [[SiC Layer Deposition]]. Recipes across lines: [[TRISO Coating Parameters]]. Short forms below: Lowden et al. 2005 = [[Effects of Deposition Conditions on the Properties of Pyrolytic Carbon Deposited in a Fluidized Bed]]; Barnes and Marshall 2008 = [[FY 2008 Six-Inch Diameter Coater Test Report]].

## Chemistry

$\text{C}_2\text{H}_2 \rightarrow 2\text{C} + \text{H}_2$ and $\text{C}_3\text{H}_6 \rightarrow 3\text{C} + 3\text{H}_2$, in argon ([[Ch 02 — Manufacture of TRISO Coated Particles]] p.33). The buffer is deposited from acetylene at high coating gas fraction to give a porous, ~1.0 g/cm³ layer; the dense layers use a propylene/acetylene mixture, or propylene alone, at lower fraction (p.31; [[TRISO Coating Parameters]]).

**Coating gas fraction (CGF)** — the reactive fraction of the total gas flow — is the controlling variable alongside temperature, and is reported directly by the US lines while the German and INET lines give only gas identities.

## What each parameter controls

From a 17-run two-factor study on the IPyC (inner pyrocarbon) layer, 1170–1325 °C × CGF 0.15–0.45, all other conditions fixed (Lowden et al. 2005 p.7):

| Property | Dominant parameter | Direction |
|---|---|---|
| Deposition rate | CGF | rises with reactant concentration |
| Density | temperature | **falls** as temperature rises |
| Permeability to chlorine | temperature, through density | rises steeply |
| Open porosity | CGF, through coating rate | rises with CGF |
| Efficiency | both | — |
| Anisotropy | both | non-monotonic |

Density runs 1.978 g/cm³ at 1170 °C down to 1.746 at 1325 °C (p.34). The AGR (US Advanced Gas Reactor programme) specification of 1.90 g/cm³ therefore fixes the temperature: ~1265 °C bed in both a 2-inch and a 6-inch coater (Barnes and Marshall 2008 p.21).

## The chlorine barrier is a deposition parameter

The IPyC's job during fabrication is to keep the HCl released by SiC deposition away from the kernel ([[Ch 01 — Introduction]] p.22). Lowden et al. 2005 measured it: after 18 h of chlorination at 1500 °C, dispersed uranium in the carbon layers rose about twentyfold from the coldest to the hottest IPyC — 0.342 to 7.52 in their arbitrary units, with the jump between 1275 and 1300 °C (p.34).

![[lowden-p31-fig29-u-dispersion-vs-temperature.jpeg]]
*Uranium dispersion after chlorination, CGF 0.30, by deposition temperature — Lowden et al. 2005 p.31.*

The layer that best resists chlorine is therefore the dense, cold-deposited one — the same direction the density specification pushes, and the opposite of what low anisotropy wants at fixed CGF.

## Anisotropy is the awkward property

Anisotropy drives irradiation-induced shrinkage cracking ([[TRISO Fuel Failure Mechanisms]]), so it is the pyrocarbon property with a failure mechanism attached. It is also the one neither parameter controls cleanly: diattenuation spans 0.0031–0.0151 across the study with no monotonic trend, the most anisotropic layer coming from the coldest, leanest run (Lowden et al. 2005 p.34). Anisotropy falls with rising temperature and rising coating rate, and at any temperature in 1225–1275 °C there is a rate that minimises it, occurring at a CGF of roughly 0.32–0.35 — just above the 0.30 ± 0.03 specification, which Barnes and Marshall 2008 p.22 suggest widening on that basis.

## Scale

IPyC density against bed temperature transfers between a 2-inch and a 6-inch coater: same density at the same temperature, with a shallower slope in the larger vessel and so a wider operating window (Barnes and Marshall 2008 p.21).

![[bw-coater-p22-fig02-ipyc-density-vs-bed-temperature.jpeg]]
*IPyC density vs bed temperature, two coater sizes — Barnes and Marshall 2008 p.22.*

The buffer does not transfer as well. In the 6-inch coater the bed sweeps 1390–1540 °C during a 4–7 minute deposition at a fixed setpoint, where the 2-inch coater holds 1450 °C, and buffer density wandered 0.94–1.10 g/cm³ across runs with no deliberate change (p.19). That is the layer where this source reports the least control.

## IPyC and OPyC are not the same layer

Deposited from near-identical recipes, they end up different: OPyC (outer pyrocarbon) surface-connected porosity 0.4–0.8 ml/m² against IPyC 2.0–2.4 (Barnes and Marshall 2008 p.9), and the thermal-diffusivity and modulus differences recorded on [[TRISO Coating Process]]. The causes given are the higher IPyC coating rate and the annealing the IPyC receives while SiC is deposited over it.

## Contested / uncertain

> [!warning] Conflict — buffer deposition temperature
> US AGR lines coat the buffer at 1450 °C bed (2-inch) or 1390–1540 °C (6-inch, `p.19`) and ORNL at 1425 °C bed; the IAEA generic and INET lines give 1250–1260 °C ([[TRISO Coating Parameters]]). Both routes meet their density specifications. Not a measurement-position artefact — the US figures are bed temperatures. Unresolved.
> `#conflict`

> [!info] Inferred — the two density conventions may not be comparable
> Lowden et al. 2005 measured IPyC density on fragments cracked off coated particles, noting residual buffer may remain attached (p.7); [[Ch 04 — QA-QC and Characterization]] p.42 records that IPyC fragments cannot be recovered at all once SiC is deposited, which is why hot sampling exists. The Lowden samples were buffer+IPyC particles with no SiC, so the two sources are measuring the same layer by different routes with different contamination risks. Confirmation would need a line that measured both ways on one batch.
> `#inferred`

## Sources

- [[Effects of Deposition Conditions on the Properties of Pyrolytic Carbon Deposited in a Fluidized Bed]]
- [[FY 2008 Six-Inch Diameter Coater Test Report]]
- [[Ch 02 — Manufacture of TRISO Coated Particles]] · [[Ch 04 — QA-QC and Characterization]] · [[Ch 01 — Introduction]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
- Data: [[TRISO Coating Parameters]]
