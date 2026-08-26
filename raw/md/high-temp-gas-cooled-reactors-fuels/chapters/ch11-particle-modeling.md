---
type: source-chapter
chapter: 11
title: Particle Modeling
pages: 106-110
source_md: high-temp-gas-cooled-reactors-fuels.md
---

# **11. PARTICLE MODELING**

Mathematical modeling of the mechanical behavior of fuel in a nuclear reactor during the course of its irradiation is a useful tool, both as a guide for the manufacturer and also at the pre- and post-irradiation stages of in-reactor studies. At the fabrication stage, modeling can assist in optimizing the fuel design and in identifying permissible tolerances. For the purpose of planning test irradiations, modeling can assist in identifying appropriate fuel specifications and irradiation conditions. Modeling predictions may also be compared with the irradiation results. If they agree, then further extension of the calculations can check, with reasonable certainty, which a satisfactory irradiation was not on the brink of some catastrophic occurrence. If, on the other hand, they disagree, then the assumptions and/or limitations in the calculations have to be examined - a classic way by which scientific progress is made. One advantageous feature of modeling, which is why it should be used to the full, is that many calculations can be performed quickly and cheaply, in contrast with in-reactor irradiation experiments. In short, modeling studies are a way of gaining a scientific understanding of what is occurring when fuel is being irradiated - which is required by researchers, industry, utilities, and especially regulators.

To model the mechanical performance of coated particles it is necessary to calculate the tangential stresses within each of the three load bearing layers – the IPyC, the SiC and the OPyC - over the course of the irradiation. This enables one to explore whether at any stage the fracture stress in any of the layers has been exceeded. Therefore, we need to consider the various factors which affect these stresses.

During irradiation the kernel will release a proportion of the fission gases generated. If the kernel is uranium oxide, oxygen will also be released, which then reacts with pyrocarbon to form mainly CO and CO2.This is not the case for UCO fuel kernels until very high burnup are achieved and the UC2 phase is consumed.

The irradiation causes the kernel to swell and the buffer layer to shrink, thereby modifying the internal void volume available to the fission and reaction gases. Because of differential dimensional changes, from the early stages of the irradiation, the kernel and buffer layer are both mechanically uncoupled and in some cases the buffer layer may be cracked. Regardless if the crack occurs, the high porosity of the buffer layer implies that fission gases can 

<!-- page 107 -->

penetrate to the inner surface of the IPyC layer. As a result, the only force impinging on the three load bearing layers is the gas pressure on this surface.

If the IPyC and OPyC were absent, the gases produced in the fission process would simply stress the SiC layer and, if the pressure were high enough, cause it to fail. However, these tangential stresses are reduced by the presence of the two PyC layers because; under unrestrained conditions they would shrink during irradiation. Since this shrinkage will be largely restrained by the SiC layer, tangential stresses will be generated in both PyC layers and radial, inward acting forces imposed on the two surfaces of the SiC layer. In practice, these tangential stresses in the two PyC layers will attain a quasi-equilibrium stress state because their shrinkage is counter-balanced by irradiation creep. The SiC elastic modulus is at least an order of magnitude greater than that of PyC. During irradiation, dimensional changes and creep strains of SiC are comparatively much smaller than for PyC.

In short, modeling involves calculating stresses in the three load bearing layers created by the restraints due to attempted changes in the layer dimensions and also by the gas pressure exerted on the inner surface of the IPyC layer. This requires knowledge of various properties of the particle's constituent materials and also the manner in which these values vary over the course of the irradiation. The model must also be able to handle details of the irradiation history. Because a measure of protection from fission product release is obtained even after two of the three load bearing layers have failed, it is desirable to be able to model the fracture of one layer and then to continue the calculation up to the failure of all three layers. Moreover, a model must also be able to deal with gaps that may develop between the layers. Apart from the kernel-buffer and buffer-IPyC gaps, there is the possibility that in its attempt to shrink during the irradiation the IPyC will de-bond from the SiC layer. A description of a model that meets these requirements is presented below.

The whole irradiation history is divided into a sequence of consecutive finite neutron dose (or time, or burnup) steps. Values of stresses and strains in each layer are known at the beginning of each step (and assumed to be zero at the start of the calculation). It is, therefore, required to calculate changes in stresses and strains in each layer over the current neutron dose step which then enables stresses and strains to be up-dated for the start of the next step. The manner in which these stress and strain changes are calculated is as follows:

There are three sets of basic equations for each of the layers and the kernel [\[154\]](#page-175-5):

- 1. The displacement equations, state that the overall change in strain during a neutron dose step is the sum of the strain changes due to stress changes (elastic), irradiation creep, temperature change and irradiation induced dimensional changes. Because spherical symmetry is assumed, there are two equations, referring to the radial and tangential directions respectively.

$$\boldsymbol{\varepsilon}_1 = g_1 + K(1-\nu)\boldsymbol{\sigma}_1 - K\nu\boldsymbol{\sigma}_1$$

$$\mathcal{E}_3 = g_3 + K\sigma_3 - 2Kv\sigma_1$$

where <sup>ε</sup> , *g* , <sup>ν</sup> , and *K* are strain rate, creep rate, Poisson's ratio, and creep constant, respectively. σ1 and <sup>σ</sup> 3 are radial and tangential stresses.

<!-- page 108 -->

- 2. The compatibility equations (again two equations) are in spherical geometry which relate radial displacements to strains.

$$\mathcal{E}_1 = \frac{u}{x}, \quad \mathcal{E}_3 = u'$$

Where *u* is the radial displacement along the radial direction *x* and the prime denotes differentiation with respect to *x*.

- 3. The equation of equilibrium (only one equation) between tangential and radial stresses. Thus five simultaneous equations are derived for each layer.

$$\sigma_1 = \sigma_3 + \frac{1}{2} x \sigma_3'$$

From these a second order differential equation in one of the unknowns (e.g., changes in the radial displacement) is obtained by a process of elimination.

The solution has two constants of integration; these are evaluated from a set of simultaneous equations which define the boundary conditions for each of the layers (e.g. continuity of radial displacements and radial stresses at the interfaces). If the radial stress between two layers is found to exceed the de-bonding stress, the step is repeated with the boundary conditions suitably modified. If, on the other hand, the tangential stress in a layer is found to exceed the material's fracture stress, it is reduced to zero by a sequence of pseudo thermal creep time steps, thereby simulating failure; in subsequent neutron dose steps the tangential compliance constants of this failed layer are set extremely high.

Figure 59 illustrates the evolution of stresses in the three load bearing layers. Initially stresses in the SiC layer are compressive due to the attempted shrinkage of the two PyC layers, but as the gas pressure increases they become tensile until failure occurs at the fracture stress of 650 MPa. Material properties assumed for the two PyC layers were the same. However while stresses in the OPyC varied little during the course of the irradiation, they will decrease in the IPyC layer because of an increasing compressive component from the gas pressure.

So far only the endurance of an individual coated particle has been considered. However, in practice one is only concerned if some fraction, say 10-5-10-4, of particles from the whole population have failed (fracture of the SiC layer). Not all particles will fail at the same burnup value for two reasons. First, because the layers are considered to be brittle materials, their fracture stresses will be variable from particle to particle. This implies that as the tangential stress increases during irradiation so also will the fraction which has failed. The second reason why particles will not all fail at one burnup value is because of the statistical variations in the characteristics of individual particles.

<!-- page 109 -->

![](../_page_108_Figure_0.jpeg)

*Fig.59.. Example of stresses in the three load-bearing layers during irradiation.*

One way to calculate particle failure fractions as a function of the burnup is to employ Monte Carlo methods. Essentially this involves running the single particle computer code many times on a large number of particles, the specifications of each having been selected in accordance with the statistical variations of the various components. The burnup at which each particle fails is recorded, thereby enabling failure fractions as a function of burnup to be evaluated.

Uncertainties in some of the input data are a major source of uncertainties in the modeling results. In particular the properties of PyC can be highly variable, being strongly dependent on the manufacturing procedure. In simple terms, PyC may be regarded as a collection of imperfect graphite crystallites whose properties are highly anisotropic. To make their macroscopic properties as isotropic as possible the PyC layers must be manufactured with these crystallites in random orientations. This is necessary to avoid shrinkage rates in the tangential direction being so large that they cause fracture.

Along with computer codes, simple analytical models, which make the reasonable approximation that stress does not cause deformation of the SiC layer, enable identification of the most significant material properties affecting particle endurance. These models provide a useful, quick way of checking for gross errors in the more sophisticated computer codes.

Modeling is an invaluable tool for understanding the behavior of coated fuel particles during irradiation and further developments are in progress. More experimental work on material properties is necessary to reduce uncertainties in the input constituent materials property data. There needs to be a continual interaction between modelers and experimenters to ensure that what is observed is also being modeled. On the other hand, modeling may predict features (e.g., a failure mechanism) not previously observed which could be worth investigating experimentally.

<!-- page 110 -->

Figure 60 is an example of the application of a simple model to predict SiC failure fraction as a function of temperature and burnup. The gas pressure at 10% FIMA used in generating this figure are given in Table 14.

![](../_page_109_Figure_1.jpeg)

*Fig. 60. Predicted failure fractions for irradiations at 900° and 1200°C up to 20% FIMA (German contribution to CRP6 normal operations benchmark calculations, Ref Phélip Mayeul). The acceptance level is in the range 2x10-5 to 6x10-5.* 

Table 14. PREDICTED GAS PRESSURES (MPA) AT 10% FIMA IN UO2 LTI TRISO REFERENCE PARTICLE

| Temperature | Fission Mark   | CO             | Total          |  |
|-------------|----------------|----------------|----------------|--|
|             | Pressure (MPa) | Pressure (MPa) | Pressure (MPA) |  |
| 900°C       | 3.9            | 0.1            | 4.0            |  |
| 1200°C      | 15.7           | 5.8            | 21.5           |  |

