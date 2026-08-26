---
type: source-chapter
title: Ch 08 — Fuel Failure Mechanisms
source: High Temperature Gas Cooled Reactor Fuels and Materials
pages: 70-78
ingested: 2026-08-25
status: draft
tags: [triso, fuel-performance, failure-mechanisms, sic, pyc]
updated: 2026-08-25
---

# Ch 08 — Fuel Failure Mechanisms

Part of [[High Temperature Gas Cooled Reactor Fuels and Materials]] · pp.70–78

**Gist** — A catalogue of eleven mechanisms by which a TRISO particle can fail or stop retaining fission products, each with the reactor conditions and particle design parameters that control it. Two themes run through the chapter: most mechanisms are controlled by fabrication quality rather than being intrinsic to the design, and the German and US programmes diverged sharply on exactly those fabrication parameters. The chapter's own conclusion is that in well-made fuel, releases are dominated by as-manufactured defects rather than by any of these mechanisms (p.77).

## The mechanisms

### Overpressure · §8.1, p.70

Fission gas released into the porous buffer, plus CO and CO₂ formed when excess oxygen from UO₂ fission reacts with buffer carbon, exerts tensile stress on the SiC layer. Production of all three scales primarily with burnup and temperature. Nominal particles are sized with enough buffer void volume not to fail this way; failure is postulated to require an insufficient or missing buffer from the coating process, so fabrication specifications cap the number of particles produced with missing buffers.

### Irradiation-induced IPyC (inner pyrocarbon) cracking · §8.2, pp.71–72

Pyrocarbon shrinks radially and tangentially under irradiation, then begins swelling radially at around 2 × 10²⁵ n/m² depending on density, temperature and anisotropy. This puts the PyC into tangential tension; irradiation creep relieves it. Where PyC is strongly bonded to SiC, its shrinkage instead supplies a compressive stress that offsets kernel gas pressure — the mechanism works *for* the particle when the bond is good. In US irradiations including the DOE New Production Reactor programme of the early 1990s, shrinkage far exceeded expectation, cracking the PyC and concentrating stress enough to fail the SiC. Thicker PyC layers develop larger stresses and fail more readily.

### Debonding between IPyC and SiC · §8.3, p.72

Weakly bonded layers partially detach under IPyC shrinkage, generating tensile stress in the SiC at the remaining contact point — smaller than for a cracked IPyC, but Weibull calculations put SiC failure at "a low, but not insignificant, rate."

> [!info] The German/US divide
> Both cracking and debonding trace to the same fabrication choice. US IPyC was deposited at low coating gas concentration and correspondingly low coating rate, producing high anisotropy; German fuel used higher concentrations and rates, giving isotropy good enough to prevent excessive shrinkage (p.72). The interfaces differ too: German SiC deposits *into* a more porous IPyC surface, making a tighter bond, while the less porous US IPyC gives a smoother but weaker one (p.72). German TRISO never exhibits debonding under irradiation; US fuel debonds "quite frequently."
> The same pattern repeats for the outer layer: liquid graphitic matrix infiltrating OPyC (outer pyrocarbon) porosity plus dimensional change caused OPyC cracking and debonding in US fuel, limited by specification to ≤3% of OPyC layers, while German fuel's powdered matrix — difficult to infiltrate — and more isotropic OPyC avoided the mechanism entirely (§8.6, p.75).

### Kernel migration · §8.4, p.73

See [[Kernel Migration]].

### Fission product attack · §8.5, pp.73–75

Fission products migrate from kernel to the inner SiC surface and can damage or fail it. In LEU (low-enriched uranium) oxide kernels — both UO₂ and UCO — palladium is the important species, along with other noble fission products; UCO's oxycarbide chemistry ties up all but the noble products as carbides or oxides, limiting mobility, though Pd transport is still observed. Silver migrates through apparently intact particles (see [[Silver Release]]). Enrichment matters: the Ag and Pd fission yield difference between U and Pu is a factor of 25 to 50, so LEU fuel at end of life — where a significant share of fissions come from plutonium — carries much higher Ag and Pd concentrations than HEU (high-enriched uranium) fuel at similar burnup. Finite element calculations of notched SiC find low failure probability because so little of the layer is degraded, but complete penetration makes the particle functionally failed regardless of residual strength.

### Non-retentive SiC — diffusive release · §8.7.1, p.75

Effective diffusion coefficients from heating test data indicate that if normal-operation fuel temperatures approach 1300 °C, fission products normally retained by the coating — cesium in particular — will diffuse out during normal operation and contribute to the source term.

### Non-retentive SiC — induced permeability · §8.7.2, p.76

Spherical elements taken to higher fluence (4–6 × 10²⁵ n/m²) and higher burnup (14% FIMA (fissions per initial metal atom)) released more cesium in heating tests than similar spheres inside the German operating envelope (8–9% FIMA, 2–4 × 10²⁵ n/m²). Two candidate mechanisms, neither resolved: cesium vapour attack of SiC, demonstrated by Coen in the 1970s above 1500 °C and showing pitting rather than simple diffusion, with kinetics correlating reasonably with the timing of cesium release from the German spheres; and CO corrosion, where CO generated from UO₂ kernels reaches SiC through permeable or cracked IPyC and converts it to gaseous SiO at low CO partial pressure. Reaction kinetics are unknown; thermodynamics permits it. Expected to matter most at high burnup in UO₂ TRISO, because the large plutonium fission fraction at high burnup releases more oxygen per fission than uranium.

### Creep failure of PyC · §8.8, p.76

Thermal creep thins and fails PyC in post-irradiation heating tests above ~2000 °C at long times. Has not led to SiC failure.

### SiC thermal decomposition · §8.9, p.76

Above ~2000 °C, confirmed by thermodynamics and German furnace heating tests. Has not played a major role at accident temperatures of 1600–1800 °C.

### Kernel-coating mechanical interaction · §8.10, pp.76–77

At sufficiently high burnup the kernel swells until all gas gaps close, and models predict SiC failure shortly after onset. Never reported experimentally — possibly because a gap always reopens on cooldown, the kernel having the higher thermal expansion coefficient, so post-irradiation examination would not see it. Flagged as potentially important as burnup targets rise.

## Controlling variables (Table 8, p.77)

The summary table maps each mechanism to reactor service conditions and particle design parameters. Recurring conditions: temperature, burnup, fast fluence, temperature gradient, and time at temperature. Recurring design parameters: layer thicknesses, PyC density and anisotropy, interfacial strength, SiC strength and microstructure, buffer void volume, and kernel type. Two of the table's comments are worth extracting verbatim in substance:

- CO generation and its consequences are **"UO₂ only. Not important for UCO."**
- Diffusive release is **"more important at higher temperatures (> 1200 °C) where existing data suggest diffusion will contribute to the source term."**

The Table 8 conversion is badly mangled (cells merged across rows); the mechanism-by-mechanism content above is taken from the body text, which is intact.

## Figures kept

![[tecdoc1645-p73-fig38-sic-ipyc-interface.jpeg]]
*Fig. 38, p.73 — SiC/IPyC interface in German (left) and US (right) fuel. Contrast differs between the two images because of lighting technique, per the caption.*

![[tecdoc1645-p75-fig40-fp-attack-sic.jpeg]]
*Fig. 40, p.75 — photomicrograph of fission product attack on the SiC layer.*

## Open questions raised

- Is the Cs-attack or the CO-corrosion mechanism responsible for induced SiC permeability at high burnup? The chapter states plainly that no additional experiments followed Coen's 1970s work and that CO reaction kinetics are unknown (p.76).
- KCMI has never been observed but is predicted; if the proposed explanation (gap reopening on cooldown) is right, post-irradiation examination is structurally incapable of detecting it. What measurement would?
- Which of the German fabrication parameters are actually necessary, and which are historical accident? The chapter attributes success to coating gas concentration, coating rate and powdered matrix, but gives no process window.
