---
type: source
title: A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production
aliases: [Hu et al. 2025, SiC FB-CVD review]
authors: [Hu, L., Turner, J., Buckley, J., Abram, T.]
org: Nuclear Fuel Centre of Excellence, University of Manchester
year: 2025
doc-id: doi:10.1016/j.pnucene.2025.105762
journal: Progress in Nuclear Energy 185 (2025) 105762 — review article, open access (CC BY 4.0)
url: https://doi.org/10.1016/j.pnucene.2025.105762
pdf: raw/pdf/review-of-sic-coating-properties.pdf
md: raw/md/review-of-sic-coating-properties.md
pages: 19
ingested: 2026-09-22
status: draft
tags: [triso, sic, cvd, fabrication, mts, stoichiometry, microstructure, density, conflict]
updated: 2026-09-22
---

# A Review on Properties Required for FB-CVD Fabricated SiC for TRISO Fuel Production
> University of Manchester, 2025. doi:10.1016/j.pnucene.2025.105762. Review, 19 pp. Part 1 of 2 (part 2 covers PyC — not yet in the wiki).
> [PDF](../raw/pdf/review-of-sic-coating-properties.pdf) · [converted](../raw/md/review-of-sic-coating-properties.md) · [saved abstract page](../raw/pdf/review-of-sic-coating-properties.html)

**Gist** — A literature review of how fluidised bed–chemical vapour deposition (FB-CVD) parameters set the properties of the TRISO SiC layer, compiling data from 16 studies (Table 1, 1968–2019; coaters 2.4–15.24 cm diameter) and re-plotting density, deposition rate and coating efficiency against temperature and H₂/MTS (hydrogen to methyltrichlorosilane) ratio. Deposition temperature is the one parameter the literature agrees on: 1500–1600 °C in pure hydrogen gives stoichiometric, peak-density SiC. The effects of H₂/MTS ratio, gas flow and fluidisation regime are contested or unmeasured, and the compiled data scatter widely. Every finding is second-hand — the review generates no new measurements — so claims carry the weight of the underlying study, cited here as "citing X".

## Key findings

- **Stoichiometric window 1500–1600 °C in H₂**; below it free Si co-deposits, above it free C — `p.8`. Exact boundaries differ between coaters; one study (Cromarty 2012) saw no effect on Si content above 1250 °C, attributed to its temperature distribution and particle circulation — `p.9`.
- **Argon lowers the window.** In Ar–H₂ diluent the stoichiometric temperature falls as Ar fraction rises, to ~1200 °C at 90 % Ar; pure Ar gives carbon-rich SiC — `p.9`, Fig. 11 (citing Liu et al. 2016). The review notes the low-H₂ carbon co-deposition has not been replicated — `p.8`.
- **H₂/MTS effect on stoichiometry is contested**: free C eliminated above H₂/MTS = 30 (citing Minato and Fukuda 1987) vs negligible influence of MTS and H₂ flux on Si content (citing Cromarty 2012) — `p.9`.
- **Density peaks at 1500–1600 °C** and falls above it — `p.12` — but compiled data (Fig. 19) show high-density SiC outside that range and low-density SiC inside it; SiC deposited at nominally 1550 °C ranges 3.0–3.2 g/cm³ across studies, possibly from differing temperature measurement — `p.12`.
- **Deposition rate is linear in MTS flux**, consistent across four coaters — `pp.13, 15`, Fig. 20. Rate vs temperature and H₂/MTS shows no clear trend in pooled data — `p.17`.
- **Coating efficiency** generally rises with temperature, but two datasets peak near 1500–1550 °C and then fall — `p.16`. It rises with batch charge: 41 % → 97 % for 10 → 200 g (citing Gulden 1968) — `p.16`.
- **Grain size vs retention is contested**: finer-grained SiC retained fission products better (citing Petti et al. 2003) but released more silver at elevated temperature (citing Gerczak et al. 2016) — `p.2`. See [[Silver Release]].
- **Measurement is a confounder**: bed temperature is normally measured on the furnace outer wall, since internal thermocouples disturb flow and get coated — `p.3`; layer density methods (titration, liquid gradient column) are poorly documented, and some compiled values exceed theoretical density — `pp.12–13`.
- **H₂/MTS is an indirect variable.** Without MTS flux and total gas flow reported alongside it, datasets cannot be compared — `pp.16–17`. Most coaters are bespoke, so the review identifies each by internal diameter only — `p.4`.

## Data extracted

| Parameter | Value | Conditions | Page |
|---|---|---|---|
| Stoichiometric SiC density | 3.2 g/cm³ | ideal | p.2 |
| "High density" threshold used in conclusion | > 3.1 g/cm³ | — | p.17 |
| β-SiC (cubic) formation | < 1700 °C | α-SiC (hexagonal) above | p.8 |
| Single-phase β-SiC deposition | 1300–1700 °C | most cases | p.8 |
| Stoichiometric window, H₂ diluent | 1500–1600 °C | pooled TRISO studies | p.8 |
| Stoichiometric temperature, 90 % Ar | ~1200 °C | Ar:(Ar+H₂) = 90 % | p.9 |
| Preferred orientation ⟨111⟩ → ⟨220⟩ | ≤ 1400 °C → ≥ 1500 °C | flat substrates, static CVD | p.9 |
| Finer grains | H₂/MTS < 10 or > 199 vs 60–80 | — | p.9 |
| Bond energies C–Si / C–H / Si–Cl | 290 / 338 / 359 kJ·mol⁻¹ | why MTS splits at C–Si first | p.6 |
| Rate vs MTS flux gradient | 3.5, 3.94, 4.51, 4.22 | 3.49, 4.45, 6.35 cm (Federer) and 12.7 cm (Stinton and Lackey) coaters; µm/min per cm³·min⁻¹·cm⁻² | p.15, Fig. 20 |
| Coating efficiency, 25 g charge | ~80 % | 3.81 cm coater, T and flow varied | p.16 |
| Coating efficiency vs charge | 41 % → 97 % | 10 → 200 g | p.16 |
| Batch size | 20 g lab to 3 kg industrial | — | p.2 |
| Buffer density | ~1.1 g/cm³ | "half of the following PyC layer" | p.2 |
| Buffer thickness | ~100 µm | — | p.2 |
| Manchester coater | 5 cm ID × 30 cm; showerhead nozzle, 1 mm holes; annular Ar slots | — | p.4, Fig. 7 |

Coater-by-coater conditions (Table 1, pp.5–6) are on [[TRISO Coating Parameters]].

> [!warning] Internal inconsistencies
> - Coater sizes: the text gives 2.4–13 cm as the range reviewed (p.4), but Table 1 includes a 15.24 cm coater (p.5), and the text also cites a 24 cm Stinton and Lackey coater (p.16), while Table 1 lists Stinton and Lackey as 13 cm (p.5) and Fig. 20 as 12.7 cm (p.15). Gulden (1968) is 2.5 cm in Table 1 (p.5) and 3.81 cm in the text (p.16).
> - Fig. 22(c), efficiency vs H₂/MTS, is described in the text (p.16) but the figure has only two panels (p.16). The text says 1550 and 1575 °C points were selected; the caption says 1500–1600 °C.
> - The MTS formula is printed "CH₃SiCl" (p.4); correct is CH₃SiCl₃, as in Eq. 1 (p.6).
> - Hancke et al. is dated 2012 in the text and 2011 in figure legends (p.15).
> `#conflict`

## Figures kept

![[sic-review-p09-fig11-phase-diagram.jpeg]]
*Fig. 11, p.9 — deposit phase (SiC+Si / SiC / SiC+C) vs temperature and Ar:(Ar+H₂); the stoichiometric band slopes down as Ar rises (Liu et al. 2016).*

![[sic-review-p11-fig13-cross-sections.jpeg]]
*Fig. 13, p.11 — SiC cross-sections 1200–1600 °C: striated fine grains at low temperature, crystal bands and then micron-scale grains at high temperature.*

![[sic-review-p15-fig19-density-vs-temperature.jpeg]]
*Fig. 19, p.15 — compiled SiC density vs temperature, H₂/MTS 10–45 (left) and 46–100 (right); plateau near 3.2 g/cm³ above ~1450 °C with wide scatter below.*

![[sic-review-p15-fig20-rate-vs-mts-flux.jpeg]]
*Fig. 20, p.15 — deposition rate vs MTS flux, four coaters, linear fits.*

![[sic-review-p16-fig22-efficiency-vs-temperature.jpeg]]
*Fig. 22, p.16 — coating efficiency vs temperature by H₂/MTS band.*

Skipped: Figs. 1–6, 8–10, 14 (generic schematics, prior-art reactor drawings, crystallography); Figs. 12, 15–18 (surface micrographs — conclusions are captured in text); Fig. 21 (rate vs temperature; no trend).

## What this changes in the wiki

- New concept page [[SiC Layer Deposition]] — deposition chemistry and the parameter–property map.
- Places all three nominal SiC temperatures on [[TRISO Coating Parameters]] (1500, ~1600, ≤ 1550 °C) inside the 1500–1600 °C stoichiometric window, and names temperature measurement location as the review's explanation for cross-coater spread — the conflict stays open, with an `#inferred` note.
- New conflict: INL 15.24 cm coater run at 1600 °C in H₂–MTS (Table 1, p.5, citing Barnes and Marshall 2008) vs the 1550 °C whole-process maximum for the same line in [[Spouted Bed Design Considerations for Coated Nuclear Fuel Particles]] p.2.
- Adds a lower-temperature Ar–H₂–MTS SiC variant from the same US campaign: baseline, V1 and V2 at 1500 °C in H₂, V3 at 1425 °C in Ar–H₂ (5.08 cm coater, citing Hunn and Lowden 2006) — `p.5`.
- Buffer density ~1.1 g/cm³ (p.2) against 1.00 (INL) and 0.9 (INET) — a third value on [[TRISO Coating Parameters]].
- Corroborates wall-mounted temperature measurement on [[TRISO Coating Reactor Design]] and adds a density-method caveat to [[Fuel Quality Control and Characterization]].
- Adds the grain-size/silver contradiction to [[Silver Release]].

## Open questions raised

- Which grain size the wiki should treat as desirable, given the Petti/Gerczak disagreement and the review's own recommendation of argon "to produce fine-grain SiC to prevent fission product migration" (p.17).
- Where each coater's reported temperature is measured; none of the compiled datasets is normalised for it.
- Part 2 (PyC layers) — needed to extend [[TRISO Coating Parameters]] beyond SiC.

## Pages updated on ingest

- [[SiC Layer Deposition]] (new), [[TRISO Coating Parameters]], [[TRISO Coating Process]], [[TRISO Coating Reactor Design]], [[TRISO Particle Architecture]], [[Silver Release]], [[Fuel Quality Control and Characterization]], index, log, assets (5 figures)
