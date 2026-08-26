---
type: concept
title: Kernel Migration
status: draft
sources: 1
tags: [triso, failure-mechanisms, thermal-gradient, uo2]
updated: 2026-08-25
---

# Kernel Migration

**In one line** — Movement of the fuel kernel through its coating along a thermal gradient, driven by carbon transport rather than by any motion of the kernel itself; if excessive, the kernel penetrates the coating and the particle fails.

## Mechanism

The name is a misnomer, and the document says so. Inside the kernel an equilibrium exists between C, UO₂, CO and CO₂. A thermal gradient across the particle makes that equilibrium different on the hot and cold sides, and the imbalance drives net mass transport of **carbon up the temperature gradient**. In photomicrographs the result appears as the kernel moving *down* the gradient — hence the name, and hence also the older label "amoeba effect" ([[Ch 08 — Fuel Failure Mechanisms]] p.73).

The dependence is strongly on the temperature *gradient*, with secondary dependence on absolute temperature and on burnup. Because the driving equilibrium involves CO and CO₂, the mechanism belongs to the UO₂ kernel chemistry and is not expected for UCO — Table 8 lists it as "UO₂ only. Not important for UCO" (p.77).

## Observational status

Kernel migration has only been observed in German irradiation tests where conditions were deliberately designed to induce it. No indication of it appeared during AVR or THTR operation, which the chapter attributes to the low thermal gradients in a pebble bed ([[Ch 08 — Fuel Failure Mechanisms]] p.73). It is therefore a predicted-and-demonstrable mechanism rather than an observed service problem — but the service experience that establishes this is pebble-bed experience.

## Design implications for HTGRs

This is one of the two mechanisms the source identifies as specifically worse for prismatic cores: "In prismatic HTGR cores with UO₂ fuel, where particle loadings and power densities are greater, the potential for kernel migration is greater" (p.73). The lever is thermal gradient across the particle, which follows from power per particle and from the coolant-hole to fuel-hole geometry of the block.

It also constrains how fuel qualification tests may be designed. Because the mechanism responds to gradient rather than to burnup alone, an over-accelerated irradiation produces failures that would never occur in service. The chapter's recommendation is explicit: limit thermal gradient or power per particle to values typical of the reactor application, and keep burnup/power acceleration to **no greater than three times** the expected rate (p.73).

## Prevention

Two routes, both aimed at the excess oxygen rather than at the gradient:

- **UCO kernels.** The stoichiometric UO₂/UC₂ mixture carries enough carbon to consume excess oxygen inside the kernel, preventing the CO buildup that drives the equilibrium — described as "eliminating kernel migration (or the 'amoeba effect') and excess internal pressures at high burnups" ([[Ch 01 — Introduction]] p.22). See [[UCO vs UO2 Kernels]].
- **UO₂\* particles.** A thin ZrC layer with a dense pyrocarbon seal coat applied directly onto a conventional UO₂ kernel acts as an oxygen getter, limiting CO production and retarding kernel migration. Tested in the ORNL (Oak Ridge National Laboratory) HFIR (High Flux Isotope Reactor) HRB series at 860–1210 °C and 19–29% FIMA (fissions per initial metal atom) with superior performance ([[Ch 01 — Introduction]] p.22).

The third route is thermal: limit the gradient. That is a core design decision rather than a fuel one.

## Figures

![[tecdoc1645-p74-fig39-kernel-migration.jpeg]]
*Fig. 39, p.74 — photomicrograph of kernel migration.*

## Open questions

- What thermal gradient, quantitatively, separates safe from unsafe? The source gives the dependence but no threshold value.
- Does the UCO exemption hold at high burnup, where plutonium fission raises oxygen release?

## Sources

- [[Ch 08 — Fuel Failure Mechanisms]] — from [[High Temperature Gas Cooled Reactor Fuels and Materials]]
