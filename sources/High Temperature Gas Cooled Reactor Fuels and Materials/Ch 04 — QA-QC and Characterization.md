---
type: source-chapter
title: Ch 04 — QA-QC and Characterization
source: High Temperature Gas Cooled Reactor Fuels and Materials
pages: 38-47
ingested: 2026-08-25
status: draft
tags: [qa-qc, characterization, metrology, anisotropy, burn-leach, thermal-properties]
updated: 2026-08-25
---

# Ch 04 — QA-QC and Characterization

Part of [[High Temperature Gas Cooled Reactor Fuels and Materials]] · pp.38–47

**Gist** — How the properties that decide fuel performance are actually measured. Each test in this chapter exists to catch a specific failure mechanism: optical anisotropy for PyC shrinkage cracking, burn-leach for defective SiC and uncontained uranium, micro-radiography for layer thickness, density gradient columns for layer density. The chapter also reports measured thermal and elastic properties of the coating layers, and in doing so establishes that **the IPyC (inner pyrocarbon) is not the same material after the SiC has been deposited on top of it**.

## Quality assurance framework

Coated fuel particles for development and testing must be manufactured and controlled under a documented QA programme established to an appropriate standard — ASME NQA-1 is named (p.38). The programme must provide product and material specifications, sampling procedures and acceptance criteria, written manufacturing and test instructions, calibration and control of measuring equipment, identification and control of materials and product, and reporting to established formats with retained records (p.38).

On statistical QC the chapter's substantive point is that **sampling is the dominant error source**, not the test: "In the evaluation of a material there are always a multitude of possible errors present – sampling, being perhaps the most critical" (p.39). Test methods are validated per material type, uncertainty is quantified statistically, and confidence levels are set so that "the likelihood of unexpected failure is reduced to a remote probability which can be quantified and accepted in the design." Manufacturing is guided by trend analysis of the process (p.39).

## What is measured, and with what

**Kernel properties** (Table 3, p.40): enrichment by thermal ionisation mass spectrometry; equivalent boron content by plasma-source mass spectrometry; stoichiometry (O:U ratio) by thermogravimetric analysis; diameter and sphericity by particle size analyser; density geometrically via PSA; microstructure by microscopy on ceramographic sections.

**Coating properties** (Table 4, pp.40–41): layer thickness and symmetry by micro-radiography; buffer density geometrically via PSA and mass; other layer densities by gradient column (sink-float); IPyC and OPyC (outer pyrocarbon) anisotropy by optical anisotropy measurement or by the ORNL (Oak Ridge National Laboratory) Two-Modulator Generalized Ellipsometry Microscope; SiC layer integrity and uncontained uranium by burn-leach testing.

## Particle size and sphericity

The benchmark instrument is an automated optical particle analyser with pneumatic transport, developed by Seibersdorf for NUKEM. A particle crossing a light beam produces an intensity dip; for spherical particles a defined function of that dip is linear in diameter. Calibration uses standard steel balls. Throughput reaches about 50 particles per second, though feed rate is chosen to match required accuracy (p.39).

**Sphericity is measured, not assumed.** Defined as the ratio of a particle's maximum to minimum diameter, it is determined by cycling the *same* particle through the beam many times in random orientations before moving to the next (p.40). The rationale is structural — "spherical pressure vessels provide maximum strength" — so sphericity must stay within specified bounds.

One observation worth keeping: **particle sphericity tends to have a log-normal distribution**, which the chapter reads as indicating that "multiplicative accumulation of random errors conspire during manufacture to cause deviation from a perfect sphere" (p.40). The shape of the defect distribution is itself evidence about the process.

The shadowscope technique — particles in a monolayer on a transparent plate, imaged in bright-field transmitted light and analysed manually or automatically — gives accuracy equal to or better than PSA at lower throughput (p.40).

## Optical anisotropy: measuring the parameter that decides irradiation performance

Dense pyrocarbon behaves like a polycrystalline material in which each crystallite is inherently anisotropic in thermal expansion and fast-neutron-induced shrinkage, so macroscopic isotropy is what must be achieved (p.41). For bulk graphite, X-ray diffraction yields a Bacon Anisotropy Factor. Coating layers are far too small for that.

The workaround: the intensity of reflected polarised light depends on polarisation direction relative to the graphite crystal axes, so the ratio of reflected intensities for two perpendicular polarisations gives an **optical anisotropy factor (OAF)**, which relates consistently to the BAF and hence to expected anisotropy and fuel performance. Focused onto a polished section under a light microscope, it yields an OAF *profile across* a pyrocarbon layer (p.41).

The Seibersdorf instrument built for NUKEM is described as the primary standard for PyC anisotropy. ORNL's 2-MGEM ellipsometer determines the full polarisation effect with selectable spatial resolution down to a few micrometres (p.41).

This is the metrology that corresponds directly to the dominant failure mechanism in [[Ch 08 — Fuel Failure Mechanisms]] — anisotropic PyC shrinks excessively, cracks, and fails the SiC beneath it. OAF is how that property is controlled rather than discovered after irradiation.

## Density, and what sample preparation reveals

SiC and PyC densities are measured in density gradient columns: two liquids of differing density filled in varying ratio to create a linear gradient with height, calibrated by the zero-buoyancy position of standard floats (p.42).

### What sample preparation reveals

It carries an unintended finding. **Free-standing OPyC fragments are easy to pick out of fractured coatings "because of the weak bonding between the SiC and OPyC layers." Free-standing IPyC fragments usually cannot be obtained after SiC deposition "because of the infiltration of SiC into the open porosity of the IPyC, which results in a strong interface"** — so IPyC density must be measured by hot sampling or interrupted batches (p.42). Free-standing SiC is obtained by heating multi-layer fragments in air to about 850 °C to burn away attached PyC.

That is independent confirmation, from a laboratory procedure rather than from post-irradiation examination, of the interface asymmetry that [[Ch 08 — Fuel Failure Mechanisms]] identifies as decisive: SiC infiltrates porous IPyC and bonds strongly; the SiC/OPyC bond is weak.

### Kernel and buffer

These need different methods. No suitable gradient liquids span kernel density, and liquid penetration of the buffer returns skeletal rather than envelope density. Instead PSA gives mean geometric kernel density from summed volume over sample mass; buffer density follows by subtracting mean kernel volume from mean total volume. The error propagation is severe — **the relative standard deviation in kernel density is amplified roughly six-fold** in the derived buffer density for nominal TRISO particles, "which places a strict upper limit on the required accuracy and precision of kernel density determination" (p.42). Mercury porosimetry is the alternative, better for non-spherical shapes.

## Layer thickness

PSA-derived thickness becomes progressively imprecise for outer layers through error propagation, so X-ray micro-radiography is used across 100–200 particles: a single layer of particles laid directly on high-resolution photographic emulsion (~1 µm) with the X-ray source about 300 mm away, which gives sharp projected layer images without needing a fine-focus source. Distinguishing buffer from adjacent pyrocarbon requires low-energy X-rays and exposure in vacuum. Metallographic cross-sections imaged in bright-field reflected light achieve comparable ~1 µm resolution (pp.42–43).

## Burn-leach: the measurement behind the defect fraction

A statistically significant sample of particles is burned down to the SiC layers; the remaining particles and ash are leached under reflux in nitric acid for an extended period; the solution is preconcentrated by rotary evaporation and analysed for uranium by fluorimetry, mass spectrometry, or delayed neutron counting after reactor activation (p.43).

**With no defective SiC coatings, the result is the uncontained uranium content** — the tramp uranium of [[Ch 01 — Introduction]] p.22. The number of broken particles or defective SiC layers follows from dividing total uranium concentration by the expected contribution per particle. The intrusion method (including mercury porosimetry) offers an alternative route to defect or failure fraction.

This is the single measurement that produces the sub-10⁻⁵ defect fractions quoted throughout the document. It is destructive, which is why [[Ch 05 — Fabrication of Fuel Compacts]] reports AGR-1 (a US Advanced Gas Reactor programme irradiation) results as 95% confidence upper limits from sampled lots rather than as counts.

## Thermal and elastic properties

"The most important property for predicting the in-reactor fuel temperature is the thermal conductivity" (p.43). The fuel element is measured by laser flash; the coating layers by thermo-reflectance microscopy — a modulated pump laser heats the surface, a probe laser reads the resulting reflectance change, contactlessly and at micrometre resolution. Conductivity follows as $K = \rho \alpha C_p$ (eq. 4.1, p.43), with diffusivity from the thermal-wave phase slope to a precision "often better than 5%" (p.45). Moduli come from nanoindentation, thirty indentations per layer on a polished equatorial cross-section (p.47).

| Property, room temperature | Inner PyC | Outer PyC | Buffer |
|---|---|---|---|
| Thermal diffusivity (mm²·s⁻¹) | 7.6 ± 3.2 | 3.6 ± 0.2 | 5.2 ± 0.5 dense parts; 4 homogenised |
| Young's modulus (GPa) | 18 ± 1.1 | 23 ± 1.4 | — |

Tables 5–6, pp.46–47.

> [!info] The IPyC changes when the SiC is deposited
> IPyC and OPyC are deposited from the same gases at the same temperature to the same thickness, yet differ measurably in both diffusivity and modulus. The chapter attributes both to **annealing of the IPyC at around 1500–1600 °C during SiC deposition** (pp.45, 47), which raises its diffusivity. The IPyC in a finished particle is not the material that was deposited. Anything modelling IPyC irradiation behaviour from as-deposited properties is modelling the wrong material.

> [!warning] Table numbering in this document is unreliable
> The body text of this chapter refers to "Tables 4 and 5" for the tables captioned **Table 3** and **Table 4**, to "Table 6" for the table captioned **Table 5**, and to "Table 7" for the one captioned **Table 6**. [[Ch 05 — Fabrication of Fuel Compacts]] refers twice to "Table 3" for a table captioned **Table 7**. The captions form a consistent sequence across the document; the in-text references do not. **Cite by caption number.**
> `#conflict`

## Figures kept

*(none — this chapter's figures are instrument schematics and a phase-fit plot, which carry no information the text does not.)*

## Open questions raised

- Diffusivity values are quoted at room temperature, with tests to 1500 °C "currently in progress" (p.46). In-reactor temperature prediction — the stated purpose — needs the high-temperature values.
- IPyC diffusivity carries ±42% scatter (7.6 ± 3.2) against ±6% for OPyC. Whether that reflects genuine IPyC variability or measurement difficulty on a layer that cannot be freed from the SiC is not addressed.
