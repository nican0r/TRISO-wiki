---
type: concept
title: Passive Decay Heat Removal
status: draft
sources: 2
tags: [passive-safety, graphite, power-density, helium, decay-heat]
updated: 2026-09-08
---

# Passive Decay Heat Removal

**In one line** — An HTGR core is large, low-power-density and mostly graphite, so decay heat after a loss of cooling is absorbed and conducted away by the core's own thermal mass rather than by any system that has to work.

## Mechanism

Four properties combine, none of which is an engineered safety system ([[Ch 01 — Introduction]] pp.12–13, 18):

- **The large mass of graphite moderator provides high heat capacity.** The core is a heat sink before it is anything else.
- **Core materials are ceramic** and remain usable at elevated temperature, so absorbing that heat does not destroy the structure.
- **HTGR cores are physically large, so power density is appreciably low** — meaning the decay heat generated per unit of thermal mass is small.
- **Helium is single-phase and inert**, so there are no chemical interactions between fuel, moderator and coolant to add heat or hydrogen to the event.

The conclusion the source draws: "With their low power density, the HTGR can accommodate decay heat removal passively from the reactor core by means of the large graphite volume without causing any radioactivity release" (p.18).

## The contrast that gives it force

The same paragraph names what this replaces. In water-cooled reactors, chemical interaction between fuel, moderator and coolant is the primary concern during transients, "especially since water-zirconium reactions are exothermic at elevated temperatures and such reactions become autocatalytic" ([[Ch 01 — Introduction]] pp.12–13). The HTGR does not have a better answer to that problem; it does not have the problem, because helium does not react with graphite or with the coating layers and does not change phase.

## Where the heat has to stop

Passive removal is only a safety case if the temperature it settles at is below where fuel stops retaining fission products. That is the connection to the rest of the wiki:

| Quantity | Value | Source |
|---|---|---|
| Highest normal operating fuel temperature | ≤ 1250 °C | [[Ch 01 — Introduction]] p.18 |
| Accident fuel temperature limit, short period | ~1600 °C | p.18 |
| Peak temperature reached, depressurised loss of forced circulation, modern small HTRs | 1620 °C | [[Ch 09 — Accident Testing]] p.78 |
| Measured particle failures at 1600 °C, 221,840 particles | 0 | [[Ch 09 — Accident Testing]] p.91 |

The margin between what the transient produces and what the fuel tolerates is tens of degrees, and it is established by test rather than by calculation. See [[Fission Product Retention]].

> [!warning] Conflict — a lower peak-temperature claim elsewhere in the wiki
> [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] states peak centerline core temperatures during postulated accidents "safely remain 200–300 °C below fuel fabrication temperatures" (p.3), and fabrication runs up to 1550 °C (p.2) — implying a predicted peak near 1250–1350 °C, well below the 1620 °C figure above. The two sources do not name the same reactor design or accident scenario; flagged on [[TRISO Coating Reactor Design]], not resolved here.
> `#conflict`

## Design implications for HTGRs

Low power density is not a free property — it is the price paid for this mechanism, and it sets core size, and therefore capital cost, for a given output. The passive safety case and the economics are the same design variable read in two directions.

The graphite that provides the thermal mass is also the moderator, the reflector and the structural material, and it is being dimensionally changed by irradiation throughout ([[Irradiation Damage in Nuclear Graphite]]). Thermal mass is not itself degraded by that, but the geometry that delivers the conduction path is.

## What this page does not yet cover

The heat transfer path itself — conduction through the graphite to the reflector and vessel, and rejection from there — is not described in the ingested chapters. Neither is any quantitative graphite heat capacity or thermal conductivity value. This page currently states the mechanism qualitatively because that is what the source supports.

## Sources

- [[Ch 01 — Introduction]] · [[Ch 09 — Accident Testing]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
- [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]]
