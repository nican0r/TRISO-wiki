---
type: source-chapter
title: Ch 02 — Manufacture of TRISO Coated Particles
source: High Temperature Gas Cooled Reactor Fuels and Materials
pages: 23-34
ingested: 2026-08-25
status: draft
tags: [triso, fabrication, sol-gel, cvd, uco, kernels]
updated: 2026-08-25
---

# Ch 02 — Manufacture of TRISO Coated Particles

Part of [[High Temperature Gas Cooled Reactor Fuels and Materials]] · pp.23–34

**Gist** — The reference fabrication route, start to finish: uranyl nitrate to sintered kernel by sol-gel, then kernel to finished particle by chemical vapour deposition in a fluidised bed. The chapter states plainly that the coating technology described is the German process and that it is "the reference coating technology for modern HTGR fuel development programs" (p.30), so this is a specification rather than a historical account.

**Scope note.** §2.1's programme chronology — UKAEA dates, the German HEU (high-enriched uranium)-to-LEU cycle change, HOBEG production and the 1988 termination — is not captured here, per the skip-history rule. What is kept from that section is the process lineage that defines today's standard and the quality benchmark it set.

## The quality benchmark

**The proportion of defective particles in modern HTGR coated particle fabrication is less than 10⁻⁵**, achieved by adherence to strict process controls and product specifications (p.23). German LEU (low-enriched uranium) UO₂ TRISO reached defect levels at the 10⁻⁵ level with similar U_free/U_total contamination levels, and that fuel is characterised as "near defect free" (p.24). This is the number that makes the safety case work — it is the same order as the tramp uranium fraction in [[Ch 01 — Introduction]] and the failure fractions in [[Ch 09 — Accident Testing]].

## Kernel fabrication — UO₂ by external gelation

The reference process for LEU UO₂ kernels is sol-gel **external gelation**, also called gel-precipitation or drip-casting (p.24). Powder agglomeration preceded it but liquid routes give control of composition, pore-size distribution and density that powder routes cannot (p.24).

The chemistry (pp.26–28):

- Dissolve U₃O₈ in nitric acid: $3\text{U}_3\text{O}_8 + 20\text{HNO}_3 \rightarrow 9\text{UO}_2(\text{NO}_3)_2 + 10\text{H}_2\text{O} + 2\text{NO}$
- Pre-neutralise with dilute ammonium hydroxide to just short of precipitation.
- Add polyvinyl alcohol and tetrahydrofurfuryl alcohol to set surface tension and viscosity — these control droplet formation and later uniform shrinkage and crystal growth.
- Cast into a column of concentrated ammonium hydroxide. Precipitation forms ammonium diuranate: $2\text{UO}_2(\text{NO}_3)_{1.5}(\text{OH})_{0.5} + 2\text{NH}_4\text{OH} \rightarrow (\text{NH}_4)_2\text{U}_2\text{O}_7 + \text{NH}_4\text{NO}_3 + \text{H}_2\text{O}$
- Age at 80 °C to complete conversion and initiate crystal growth; wash with water then isopropyl alcohol; dry at 80 °C under vacuum.
- Calcine in air to 430 °C, cracking off remaining organics; above 300 °C ADU converts to UO₃.
- Reduce under hydrogen at 450–650 °C: $\text{UO}_3 + \text{H}_2 \rightarrow \text{UO}_2 + \text{H}_2\text{O}$, then sinter at 1600 °C.
- Sieve for size, then sort on an inclined vibrating table where spheres roll downhill and odd-shaped particles are transported perpendicular for recycling.

Two details carry the process. **Sphericity is established in free fall**: droplets are shaken from 4–6 nozzles at ~100 per second by a vibrator, take spherical shape in air by surface tension, then pass through an ammonia atmosphere that precipitates ADU as a protective skin on the surface — so the droplet does not deform when it hits the liquid (p.26). And **the kernel shrinks by a factor of 3.6 in diameter** across the process:

| Stage | Diameter | Page |
|---|---|---|
| Cast gelled sphere | ~1.8 mm | p.26 |
| Dried ADU kernel | ~1 mm | p.28 |
| Calcined kernel | ~750 µm | p.28 |
| Sintered UO₂ kernel | 500 µm | p.28 |

Final density is just below the theoretical 10.96 Mg/m³ (p.28).

## Kernel fabrication — UCO by internal gelation

UCO uses **internal gelation** instead (pp.28–30). The broth is acid-deficient uranyl nitrate with fine carbon black and hexamethyltetramine as an ammonia donor. Droplets are ejected through a vibrating orifice into a heated trichloroethylene column containing a surfactant: interfacial tension spheroidises them while the TCE's heat decomposes the HMTA, releasing ammonia that gels the droplet from within.

Thermal processing is where the carbide forms:

- Calcine at 550 °C in 100% hydrogen — dehydrates, decomposes uranium oxyhydroxide to UO₃, reduces UO₃ to UO₂. The hydrogen atmosphere is deliberate: it suppresses $2\text{UO}_3 + \text{C} \rightarrow 2\text{UO}_2 + \text{CO}_2$, which would otherwise strip substantial carbon, and suppresses the gas shift reaction $\text{C} + \text{H}_2\text{O} \rightarrow \text{CO} + \text{H}_2$ by hydrogen overpressure.
- Carbothermic reduction: ramp to 1680 °C in argon, then hold at 1680 °C in mixed CO/Ar. $\text{UO}_2 + 4\text{C} \rightarrow \text{UC}_2 + 2\text{CO}$ and $\text{UO}_2 + 3\text{UC}_2 \rightarrow 4\text{UC} + 2\text{CO}$.
- Densify at 1890 °C for one hour under CO-Ar, the atmosphere chosen to minimise UC formation during sintering.

| Composition | Typical | Specification range | Page |
|---|---|---|---|
| UO₂ | 74 mol% | 65–85 mol% | p.30 |
| UC₂ | 12 mol% | 0–27 mol% | p.30 |
| UC | 14 mol% | 0–35 mol% | p.30 |

The specification is expressed as limits on O/U and C/U ratios rather than on phases (p.30). The whole carbon budget of the UCO process — protecting it during calcination, converting it during reduction, limiting UC during sintering — exists to deliver the excess-oxygen sink described in [[UCO vs UO2 Kernels]].

## Coating — CVD in a fluidised bed

All four layers are deposited in one uninterrupted sequential process in the same fluidised bed reactor, with flowing gas suspending the kernels and coating gases decomposing onto them at temperatures up to 1600 °C (pp.30, 33).

| Layer | Decomposition gas | Carrier | Temperature (°C) | Rate (µm/min) | Reference thickness (µm) |
|---|---|---|---|---|---|
| Buffer (low-density PyC) | C₂H₂ | Argon | 1250 | 10 | 95 |
| IPyC (dense isotropic) | C₂H₂ + C₃H₆ | Argon | 1300 | 5 | 40 |
| SiC (dense isotropic) | CH₃SiCl₃ | **Hydrogen** | 1500 | **0.2** | 35 |
| OPyC (dense isotropic) | C₂H₂ + C₃H₆ | Argon | 1300 | 5 | 40 |

Process parameters from Table 2, p.33; thicknesses are the reference German LEU UO₂ design, p.34. Reactions: $\text{C}_2\text{H}_2 \rightarrow 2\text{C} + \text{H}_2$, $\text{C}_3\text{H}_6 \rightarrow 3\text{C} + 3\text{H}_2$, $\text{CH}_3\text{SiCl}_3 \rightarrow \text{SiC} + 3\text{HCl}$. IPyC (inner pyrocarbon) and OPyC (outer pyrocarbon) have also been deposited from propylene alone (p.31).

**SiC deposits 25 to 50 times more slowly than the pyrocarbon layers**, at higher temperature and under a different carrier gas. It is the rate-limiting step of the whole coating sequence, and the HCl it liberates is what the IPyC layer shields the kernel from ([[Ch 01 — Introduction]] p.22).

The chapter is explicit that "the conditions under which layer deposition takes place are very important as these deposition parameters determine the properties of the coated particle formed. Parameters such as temperature, pressure, gas composition and gas ratios all play an important role" (p.33) — which is the general form of the specific finding in [[Ch 08 — Fuel Failure Mechanisms]] that coating gas concentration and rate determined whether PyC came out isotropic enough to survive irradiation.

## Material requirements (p.34)

- **PyC layers**: must be impermeable; must have isotropic texture.
- **SiC layer**: β-SiC with cubic structure; density > 3.19 Mg/m³; equiaxed microstructure with fine grains and as few flaws as possible.
- **PyC–SiC interfaces**: must be of sufficient strength.

The last of these is the acceptance criterion corresponding directly to the debonding failure mechanism in [[Ch 08 — Fuel Failure Mechanisms]].

## Figures kept

![[tecdoc1645-p25-fig08-uo2-kernel-production.jpeg]]
*Fig. 8, p.25 — UO₂ kernel production flow, external gelation route.*

![[tecdoc1645-p29-fig10-uco-kernel-flow.jpeg]]
*Fig. 10, p.29 — block flow diagram of the UCO kernel fabrication process, internal gelation route.*

![[tecdoc1645-p33-fig12-fluidised-bed-coater.jpeg]]
*Fig. 12, p.33 — schematic of the high-temperature fluidised bed coating reactor.*

## Open questions raised

- Table 2 gives single-point values for temperature and rate but no tolerances or gas ratios, and the text says gas composition and ratios are decisive. The actual process window is not in this document.
- Both kernel routes are described for 500 µm UO₂ and for UCO, but the particle diameter range in [[Ch 01 — Introduction]] is 350–600 µm. How do the shrinkage chain and casting parameters scale across that range?
