---
type: source-chapter
chapter: 12
title: Fission Product Transport Modeling
pages: 110-143
source_md: high-temp-gas-cooled-reactors-fuels.md
---

#### **12. FISSION PRODUCT TRANSPORT MODELING**

For all modern nuclear reactor designs, safety is the most important consideration. The safety of a nuclear reactor design is measured by its ability to mitigate possible detrimental side effects of reactor operation from the public and operating staff under all foreseeable conditions. The main safety considerations for an HTGR power plant are radioactive material escaping from the fuel elements.

The source of radioactive materials is the large inventory of fission and activation products built up in the reactor fuel. A typical HTGR power plant design generates thermal power up to 600 MW, or ~2×1019 fissions per second. In a reactor's 40 yr operational lifetime, ~5x1028 fission product atoms along with a large inventory of activation products are created. Fortunately most of the fission products have very short half-lives and decay quickly (in terms of a fuel element core residence time of three years), or form stable oxide compounds in the fuel kernel [16], [155]. Due to adequate shielding around the reactor core and spent fuel containers, fission products in the fuel elements pose no threat to either plant personnel or the nearby population.

<!-- page 111 -->

The safety of a high temperature gas cooled nuclear power plant is therefore dependent on its fuel elements ability to retain fission products under all expected reactor operating conditions. The reactor design must be such that the fuel elements are never exposed to conditions in excess of their design qualification. Similarly, fuel designs must be such that fuel elements can be manufactured economically in large quantities, while maintaining fuel quality and integrity during manufacture and subsequent irradiation [16]. In modern HTGR reactors, the principal containment barrier is the TRISO coated particle, which has proven effective during various irradiation tests and real-time experiments.

Even under the best manufacturing conditions, a small fraction of coated fuel particles will be defective, which together with contamination in the fuel materials, are potential sources of fission product release into the coolant gas. Furthermore under abnormally high temperatures and power surges, coated fuel particles may start to fail and release fission products. Condensable radionuclides released from the core plate out in the cooler regions of the main power system causing radiation dangers to operating personnel, and if released from the closed coolant circuit, also to the public. It is therefore imperative to be able to predict, with a reasonable level of certainty, fission product release from the fuel elements and the plant under any expected operating or accident conditions. This is exactly the role of fission product release analyses.

#### **12.1. Production**

# *12.1.1. Sources*

In a nuclear reactor, fissile fuel atoms (233U, 235U, 239Pu, 241Pu) capture thermal neutrons and undergo fission reactions that produce fission products, energy (~200 MeV or ~32 pJ per event in the form of heat, kinetic energy and radiation) and more neutrons to sustain a chain reaction. When these fissile nuclides undergo nuclear fission a large variety of fission products are formed. The probability of a specific fission product being formed during a fission reaction is known as its fission yield and is different for the various fissile nuclides. These differences may be quite significant; e.g. the yield of stable 109Ag, the precursor of 110mAg, is an order of magnitude higher in 239Pu fission than from 235U fission. Thermal neutron fission product yields for 233U, 235U and 239Pu are shown in Fig. 61.

Because nearly all fission fragments are produced neutron rich, they undergo successive radioactive decay by β-particle emission (β-decay) leading to the characteristic chains of radioactive decay products for a specific mass level. Thus, a large collection of fission product nuclides is created in a nuclear reactor by the fission of uranium and plutonium. Fortunately, most or the fission products have very short half-lives, and many others form chemically stable oxide compounds in the fuel kernel. Therefore, they are of little interest for fission product release analysis.

<!-- page 112 -->

![](../_page_111_Figure_0.jpeg)

*Fig. 61. Fission yield as a function of fission product mass number for 233U fissions, 235U fissions, 239Pu fissions (Ref: Wikipedia 2009).* 

The fission product source term S*i* (production from fission) for a specific isotope *i* can be calculated by the relationship

| $S_i = P_f \cdot t \cdot Y_i$ | (12.1) |
|-------------------------------|--------|
|-------------------------------|--------|

where Pf is the fission power output of the fuel element (W),

t is the duration of each time step (decay corrected) (s), and

Y*i* is the cumulative fission yield of the fission product.

The fact that one fission event results is the liberation of ~200 MeV of energy can be used to show the equivalency of 1 W of power to 3.12 x1010 fissions/s.

Activation products are formed when a fission product captures a neutron to form a new nuclide. Some of these activation products are very important for HTGR maintenance and safety, for example 134Cs and 110mAg. The 110mAg production and decay chain is shown below:

Ag m110 47 Pd Ag <sup>109</sup> 47 109 β <sup>46</sup> ⎯⎯→⎯ − Ag <sup>110</sup> 47 βγ n,γ n,γ Cd <sup>110</sup> 48

![Diagram of the process of polymerization of poly(phenylene acrylate) (PPA) to poly(phenylene acrylate diacrylate) (PPAdAc). The reaction is shown with the initial conditions: Pd at 109/46, Pd at 109/47, and Pd at 109/48. The reaction is shown with the following conditions: n, γ at 109/47, n, γ at 109/48, and n, γ at 109/47. The resulting polymers are PPAdAc at 109/48 and PPA at 109/47.]()

The activation product source term SAP (production from activation) can then be calculated by the effective decay constants of the activation and mother products as follows:

$$S_{AP} = S_{MP} \cdot \frac{Y_{CUM}}{Y_{DIR}} \cdot R_{Br} \left[ e^{-\lambda_{MP}t} - e^{-\lambda_{AP}t} \right] \cdot \left[ \frac{\lambda_{AB}}{\lambda_{AB} - \lambda_{MP}} \right], \quad (12.2)$$

where SAP is the activation product's source term (production from fission), SMP is the mother product's source term (production from fission),

<!-- page 113 -->

 YCUM is the cumulative fission yield of the mother product, YDIR is the direct fission yield of the mother product, RBr is the branching ratio, (the fraction activation product formed), λAP is the effective decay constant of the activation product, λMP is the effective decay constant of the mother product.

The effective decay constants are calculated from the average neutron flux (Φth), and the neutron capture cross-section (σth) according to:

$$\lambda_{eff} = \lambda + \sigma_{th} \Phi_{th}. \quad (12.3)$$

# **12.2. Radionuclide selection**

Since it is impractical (and unnecessary) to evaluate production, transport and release of all the fission and activation products generated in a nuclear reactor, only the most significant radiological nuclides are analyzed. Key radionuclides are selected based on the combination of their radiological hazard level, fission yield, and their transport and release properties.

Because radiological decay occurs during fission product transport and diffusion through the ceramic layers of a coated fuel particle, the radiologically important fission products released from fuel elements are divided into two groups: the relatively short-lived gaseous fission products, and the long-lived metallic fission products. Different theoretical models and sets of transport parameters (e.g. diffusion coefficients, correlations) describe both these two fission product group's behavior.

These models are applied in software codes that use the different sets of transport parameters to describe fission product behavior in fuel elements. A simple steady-state code can adequately describe gaseous fission product release during normal operation, but a transient code is needed to describe metallic fission product release. Although all the iodine, bromine, krypton and xenon fission products could be calculated, only six key nuclides from these four elements are necessary to provide the significance of the radiological risk. These six key radiological short-lived fission product nuclides are:

131I, 133I (especially accident conditions, heat-up during loss of forced coolant events),

88Kr, 138Xe, 133Xe (normal conditions, leaking from main power system),

90Kr, 137Xe (as precursors for 90Sr and 137Cs, respectively) and

132Te (although a metal, its behavior and inventory is calculated very similar to that of iodine and xenon).

The inventory of any metallic fission or activation product can be calculated as long as the transport parameters of the nuclide are available. Currently six long-lived metallic fission and activation products have been identified as radiologically significant:

137Cs, 111Ag (normal operation and accident conditions),

134Cs, 136Cs, 110mAg (normal operation) and to a lesser extent,

90Sr (principally formed by 90Kr decay in the primary circuit).

<!-- page 114 -->

The inventories of all twelve nuclides identified above are calculated for normal operation conditions, but only four of these nuclides are significant for off-normal event conditions: 90Sr, 131I, 137Cs and 111Ag. A fifth important nuclide 133I is chemically the same as 131I and the same release fractions are used for both nuclides. The list of radiologically significant nuclides is continuously reviewed and updated, and more nuclides may be added depending on the expected fuel conditions.

#### **12.3. Transport modeling**

There are three distinct and independent sources of fission product release from fuel elements. Fission products produced from each source have a different pathway to the surface of the fuel. The fission product transport route is graphically shown in Fig. 62.

- **Uranium and thorium contamination in the fuel constituent materials.** This contamination is both in the oPyC layer and in the matrix material of the fuel element. Fission products created by fission of this contamination only have to diffuse through the oPyC and the matrix material.
- **Defective and failed coated particles.** Even under the best manufacturing conditions, a small fraction of coated fuel particles will be defective. Furthermore, under abnormally high temperatures and power surges, some small fraction of the normal coated fuel particles may begin to fail. It is assumed that fission products from failed and defective particles do not have to travel through the particle's coating layers, but are released directly from the fuel kernel to the matrix material.
- **Intact TRISO coated particles.** Fission products formed in fully intact TRISO particles have to be transported through all the coating layers before they can diffuse through the matrix material. Diffusion parameters for krypton and xenon gases in the PyC coatings are very small. Therefore, the transport rates of gaseous fission products are extremely slow, and release fractions from intact coated particles are negligible. Consequently, only metallic fission product transport through intact coated particle layers needs to be considered.

<!-- page 115 -->

![](../_page_114_Diagram_0.jpeg)

*Fig.62. Fission product transport diagram.* 

<!-- page 116 -->

#### *12.3.1. Fission product recoil*

Recoil refers to the distance, fission products travel after birth before they are stopped in the surrounding material. The recoil stopping range for each fission product nuclide is dependent on its mass, its kinetic energy and the material through which it penetrates. Initially, fission products have high kinetic energies and travel a finite distance before being stopped by the surrounding material. As a result, some of the fission products formed near the surface of a fuel kernel are released directly into the buffer region because of recoil.

Similarly, some fission products formed in the grains of the graphite matrix (because of heavy metal contamination) escape the grains directly without diffusion. Also, some of the fission products formed in the oPyC layer (due to uranium contamination) escape directly from the coating layer. Finally, some of the fission products generated by heavy metal contamination in the outer 5 mm-thick fuel-free zone of the spherical element can be released directly into the coolant without diffusion.

Fission products recoiling from fission sites may knock-out other imbedded fission products from the fuel materials. However, this mechanism only plays a role at very low temperatures, and is negligible at the normal operational temperatures of modern HTGRs.

The recoil fraction *FR* released by fission in the fuel kernel into the neighboring buffer layer is calculated from geometrical considerations and is temperature independent [\[156\]](#page-175-6):

$$F_R = \frac{3}{4} \frac{r_0}{R_a} \left[ 1 - \frac{1}{12} \left( \frac{r_0}{R_a} \right)^2 \right], \quad (12.4)$$

where *FR* is the recoil fraction into the matrix material, *ro* is the mean recoil range in the buffer layer,  *Ra* is the kernel radius.

#### *12.3.2. Fission product release*

The transport of fission metals through the fuel constituent materials is modeled as a transient diffusion process. The transient diffusion equation is typically solved numerically with appropriate boundary and interface conditions [\[157\]](#page-175-7). The transport of mobile fission metals, including Cs, Ag, Sr and Eu isotopes, is undoubtedly much more complicated than classical Fickian diffusion. These apparent migration coefficients are generally structure sensitive which indicates that their transport process is not a simple diffusion process but likely a combination of lattice diffusion, grain boundary diffusion, pore diffusion, etc., complicated further by effects like irradiation-enhanced trapping and adsorption. Consequently, any quoted diffusion coefficients should be called "effective" diffusion coefficients, which imply that the overall migration process can be approximately described by Fick's laws [\[158\].](#page-175-8)

The fission product speciation in the kernel changes with burnup, especially with UCO kernels as the oxygen potential changes, and these changes in chemistry could affect the mobility of oxide-forming species, including Cs and Sr. The probable exception is silver which appears to remain in elemental form for all kernel compositions and burnups of interest.

Atoms and molecules have the spontaneous tendency to disperse as a consequence of the second law of thermodynamics. The rate of migration of an atom through a medium is 

<!-- page 117 -->

measured by its mass flux *J*, expressed as atoms·m-2· s -1. Atoms migrate down a concentration gradient as described in [\[158\],](#page-175-8) [\[159\]:](#page-175-9)

$$J_x = D \frac{\partial c}{\partial x} \text{ or, more general, } \bar{J} = -D \cdot \bar{\nabla} c \quad (12.5)$$

with c [atoms·m-3] being the concentration as a function of time and space coordinates.

The flux of atoms diffusing through a medium is proportional to the concentration gradient, which give us the balance equation in the absence of source and decay terms:

$$\frac{\partial c}{\partial t} = -\frac{\partial J}{\partial x} \text{ or } \iint_V \frac{\partial c}{\partial t} dV = \oint_S \vec{J} \cdot d\vec{s} , \quad (12.6)$$

where V and S are volume and surface under consideration.

Inserting the diffusion flux J in the balance equation gives us Fick's second law. Fick's second law of diffusion describes the time dependant diffusion process:

$$\frac{\partial c}{\partial t} = \nabla(D\nabla c) \text{ and this is } \frac{\partial c}{\partial t} = \frac{D}{r} \frac{\partial^2(rc)}{\partial r^2} \text{ in spherical coordinates and constant } D, \quad (12.7)$$

where by r (m) is the radial position (in a kernel, in a particle, or in a spherical fuel element). This is known as the diffusion equation, and mathematically, it is a partial differential equation of parabolic type.

In a fuel element there is a source S of atoms (e.g. production from nuclear fission) and a removal term λc (radioactive decay) so that the diffusion equation becomes

$$\frac{\partial c}{\partial t} = D \left( \frac{\partial^2 c}{\partial r^2} + \frac{1}{r} \frac{\partial c}{\partial r} \right) - \lambda c + S. \quad (12.8)$$

With the following boundary conditions:

1. For reasons of symmetry, the concentration gradient is 0 at r = 0.

$$\frac{\partial c}{\partial r} \Big|_{r=0} = 0 \quad (12.9)$$

2. Continuity of concentration and flux at the interface between two adjacent materials with diffusion constants D1, and D2

$$c_L = c_R, \text{ and } -D_1 \frac{\partial c}{\partial r} \Big|_L = -D_2 \frac{\partial c}{\partial r} \Big|_R \quad (12.10)$$

3. Mass transfer at the fuel surface.

$$-D \frac{\partial c}{\partial r} \Big|_{r=r_s} = \beta (\alpha c_s - c_g) \quad (12.11)$$

<!-- page 118 -->

where, *β* is the mass transfer coefficient from the surface to the coolant,  *α* is determined by the sorption isotherm,  *cs* and *cg* are concentrations on the surface and in the coolant.

The third boundary condition defines the release rate from the surface of the fuel sphere (atoms·cm-2·s -1) [\[160\].](#page-175-10) At the coolant boundary, the mass flux from the surface into the flowing coolant is given by the product of a convective mass transfer coefficient and a concentration driving force which is the difference between the desorption pressure (expressed as a volumetric concentration) and the "free stream" or mixed mean concentration in the coolant. In practical terms, the assumption of free evaporation from the surface can be made, i.e.

| $\beta \rightarrow \infty$ , or, equivalently: $c_s \equiv 0$ | (12.12) |
|---------------------------------------------------------------|---------|
|---------------------------------------------------------------|---------|

The matrix material used in fuel compacts for the prismatic core designs is porous and provides little holdup of the fission gases which are released from the fuel particles, and any retention effect is generally neglected. However, this matrix is a composite material which has a high content of amorphous carbon, and this constituent of the matrix is highly sorptive of metallic fission products, especially Sr. While the matrix is highly sorptive of metals, it provides little resistance to diffusion/migration of fission metals because of its high interconnected porosity.

The matrix of a spherical fuel element is more dense and partially graphitized so it does provide more diffusion/migration resistance of fission metals.

Metallic fission product transport in matrix material is also modeled as a transient Fickian diffusion process: the transient diffusion equation is solved with an evaporative boundary condition. It is assumed that at equilibrium, the vapor pressure in the helium-filled gap and solid-phase concentration on the fuel-compact surface are uniquely related to one another by a sorption isotherm which is determined experimentally.

Sorption isotherms for Cs, Sr and Ag have been measured for a variety of nuclear graphites and matrix materials; the data are summarized in IAEA-TECDOC-978 [16]. Experimental data are generally correlated with a simple Henry isotherm (linear dependence) for low sorbate concentrations and with a Freundlich isotherm (exponential dependence) at higher sorbate concentrations [16].

The partial pressure is assumed to be the sum of the pressures calculated with the two isotherms:

|  | $p = p_H + p_F$ | (12.13) |
|--|-----------------|---------|
|--|-----------------|---------|

| Henry: | $p_H = c_s \exp \left[ \left( A + \frac{B}{T} \right) + \left( D - 1 + \frac{E}{T} \right) \ln c_t \right], \quad (12.14)$ |
|--------|----------------------------------------------------------------------------------------------------------------------------|
|--------|----------------------------------------------------------------------------------------------------------------------------|

| Freundlich: | $p_F = \exp \left[ \left( A + \frac{B}{T} \right) + \left( D + \frac{E}{T} \right) \ln c_s \right], \text{ and} \quad (12.15)$ |
|-------------|--------------------------------------------------------------------------------------------------------------------------------|
|-------------|--------------------------------------------------------------------------------------------------------------------------------|

| transition at $c_i : \ln c_i = d_1 - d_2 T$ , | (12.16) |
|-----------------------------------------------|---------|
|-----------------------------------------------|---------|

<!-- page 119 -->

 $c_s$  is the mass concentration of sorbate (mol/kg of carbon or graphite)  
 A, B, D, E,  $c_t$ ,  $d_1$ ,  $d_2$  are empirically derived constants.

In most cases, the concentrations are low and the equilibrium vapor pressure can be expressed by:

$$p_H = c_s \cdot e^{(A+B/T)}. \quad (12.17)$$

### 12.3.3. Fission product release from fuel materials

In the Equivalent Sphere Model [158], the primary fission product retaining object is a  $\text{UO}_2$  or  $(\text{Th}, \text{U})\text{O}_2$  grain that is modeled as a sphere with radius  $a$ . With the initial and boundary conditions

$$c(0 \leq r \leq a, t=0) = 0, \quad \frac{\partial c(r=0, \forall t)}{\partial r} = 0, \quad c(r=a, \forall t) = 0. \quad (12.18)$$

Solving the diffusion equation

$$\frac{\partial c}{\partial t} = D \left( \frac{\partial^2 c}{\partial r^2} + \frac{1}{r} \frac{\partial c}{\partial r} \right) - \lambda c + S \quad (12.8a)$$

for concentration  $c$  as a function of radius  $r$  and time  $t$  reveals

$$c(r, t) = \frac{S}{\lambda} \left[ 1 - \frac{\sinh \rho \sqrt{\lambda/D'}}{\rho \sinh \sqrt{\lambda/D'}} \right] - \left[ \frac{2}{\pi} \frac{S}{D'} \frac{e^{-\lambda t}}{\rho} \sum_{n=1}^{\infty} (-1)^{n+1} \frac{e^{-n^2 \pi^2 D' t}}{n (n^2 \pi^2 + \lambda/D')} \sin n \pi \rho \right], \quad (12.19)$$

with reduced radius  $\rho = \frac{r}{a}$  and

$$\text{reduced diffusion coefficient } D' = \frac{D}{a^2}. \quad (12.19b)$$

For short-lived fission gases,  $\lambda \geq 10^{-6} \text{ s}$ , and

only the steady state first term of equation (12.19) needs to be used. Thus, Eq (12.19b) becomes

$$\frac{R}{B} = 3 \sqrt{\frac{D'}{\lambda}} \left( \coth \sqrt{\frac{\lambda}{D'}} - \sqrt{\frac{D'}{\lambda}} \right) \approx 3 \sqrt{\frac{D'}{\lambda}} \propto \sqrt{\tau}, \quad (12.20)$$

where R/B is the ratio of release-rate (R) over birth-rate (B) is approximately proportional to the square root of the half life,  $\tau^{1/2}$ . Figure 63 shows the good agreement of this model with a calibration experiment for gas release rates. The diffusion coefficient used here is given by

$$D = D'_0 e^{-\frac{Q}{RT}} \text{ with} \quad (12.21)$$

$$D'_0 = 2.1 \times 10^{-5} \text{ s}^{-1}, \quad Q = 126 \text{ kJ/mol} \text{ activation energy,}$$

<!-- page 120 -->

*<sup>R</sup>* = 8.3145 *<sup>J</sup>* /*mol* /*K* universal gas constant, and () *KT* fuel temperature.

![](../_page_119_Figure_1.jpeg)

*Fig. 63. 85mKr release rate from UO2: model predictions and measurements during the calibration experiment FRJ2-P28/2.* 

The accumulated diffusive fractional release, *F,* of long lived or stable fission products, <sup>λ</sup> ≈ 0, is given by the transient solution of the diffusion equation to yield

$$F = 1 - \frac{6}{\tau} \sum_{n=1}^{\infty} \frac{1 - e^{-n^2 \pi^2 \tau}}{n^4 \pi^4} = 4 \sqrt{\frac{\tau}{\pi}} - \frac{3}{2} \tau + 48 \sqrt{\tau} \sum_{n=1}^{\infty} i^3 \operatorname{erfc} \frac{n}{\sqrt{\tau}}. \quad (12.22)$$

The fractional release is shown as the lower curve in Fig. 64 as a function of diffusion time τ; it can be efficiently approximated by

$$F \approx 4\sqrt{\frac{D't}{\pi}} - \frac{3}{2}D't \text{ for } \tau \leq 0.35, \text{ and } (12.22a)$$

| $F \approx 1 - \frac{1}{15D'_t}$ for $\tau > 0.35$ . | (12.2b) |
|------------------------------------------------------|---------|
|------------------------------------------------------|---------|

In these expressions, the diffusion time <sup>τ</sup> = *D t*′ .

#### *12.3.4. Kernel release from post-irradiation heating tests*

Kernel release of long-lived or stable fission products (λ = 0) during accident condition heating tests (no source term, *S* = 0) can be approximated by solving the diffusion equation (13.8)

$$\frac{\partial c}{\partial t} = D \frac{1}{r} \frac{\partial^2(rc)}{\partial r^2} \quad (12.8b)$$

with the boundary conditions 
$$\frac{\partial c}{\partial r} \Big|_{r=0} = 0$$
,  $c(r = a, t) = 0$ . (12.23)

<!-- page 121 -->

The initial condition () *trc* 0, == 0for constant <≤ *ar* approximates the case of a prior coldirradiation.

The out-of-reactor fractional release [\[158\]](#page-175-8) *F* −− *reactorofout* from the fuel kernel is

$$F_{out-of-reactor} = 1 - 6 \sum_{n=1}^{\infty} \frac{e^{-n^2 \pi^2 D't}}{n^2 \pi^2}, \quad (12.24)$$

where ()<sup>1</sup> <sup>2</sup> ′ <sup>=</sup> *aDsD* <sup>−</sup> the reduced diffusion coefficient. The out-of-reactor fractional release is efficiently approximated as

$$F_{iyt-of-reactir} \approx 6\sqrt{\frac{D't}{\pi}} - 3D't \text{ for } D't \leq 0.15, \text{ and } (12.24a)$$

$$F_{out-of-reactor} \approx 1 - \frac{6e^{-\pi^2 D't}}{\pi^2} \text{ for } D't > 0.15. \quad (12.24b)$$

The release curve, applicable to a heating test of a bare kernel or broken particle, is shown as the upper term in Fig. 64. The predicted release curves for the out-of-reactor (top) and inreactor (bottom, without recoil) fractional release versus a dimensionless kernel diffusion time given by the product of the reduced diffusion coefficient with heating or irradiation time.

![](../_page_120_Figure_7.jpeg)

*Fig. 64. Fractional release of long-lived fission productions during heating (top) and during irradiation (below) as a function of diffusion time* τ *=D't according to the equivalent sphere model.*

The cesium release fraction shown in Fig. 65 is the good agreement with experimental data when using the following diffusion coefficient of cesium in UO2:

$$D'_{Cs-in-UO_2}(s^{-1}) = 0.90e^{-209 kJ/mol/RT} + 8320e^{-362 kJ/mol/RT}. \quad (12.25)$$

<!-- page 122 -->

![](../_page_121_Figure_0.jpeg)

*Fig. 65. Predicted and measured cesium release from irradiated kernels in a 300-1000- 1600°C accident condition simulation test. Five UO2 kernels in coupon C6 had been irradiated in FRJ2-P28 to 8.1% FIMA, were reactivated in FRJ1, and subjected to KUEFA heating tests.* 

Figure 65 displays the predicted release curves for the out-of-reactor and in-reactor (without recoil) fractional release versus a dimensionless kernel diffusion time given by the product of the reduced diffusion coefficient with heating or irradiation time.

# *12.3.5. Diffusion coefficients*

Kernel retention is mainly due to fission product slow-down in UO2 grains; further delays in grain boundaries, intergranular bubbles etc. are usually neglected in high burnup (>10% FIMA) HTGR fuel. Because numerical diffusions codes like GETTER and FRESCO treat the whole kernel as one unit, the fuel kernel radius being equated to the equivalent grain radius

$$D' = \frac{D_{grain}}{a^2} = \frac{D_k}{r_k^2}, \quad (12.26)$$

with *a* being the equivalent grain radius and *mrk* = 250μ kernel radius. Usual tables like Table 15 below contain *Dk* [m2 s -1] values.

# *12.3.6. Retention by a single layer*

In a situation typical of a heating test, an estimate of the breakthrough time for the release of long-lived or stable fission products through a thin spherical shell can be made with the expression

Table 15. DIFFUSION COEFFICIENTS, FROM [16]

|        |            | Diffusion Coefficients |          |             |
|--------|------------|------------------------|----------|-------------|
|        | /s] D1 [m2 | Q1 [kJ/mol]            | D2 [m2   |             |
| Cesium |            |                        | /s]      | Q2 [kJ/mol] |
| in UO2 | 5.6*10 -8  | 209                    | 5.2*10-4 | 362         |

<!-- page 123 -->

| in buffer in PyC in SiC in matrix A3-3     | 1*10 5.5*10 | -8 6.3*10 -8 -14 * e Γ /5 3.6*10 -4 | 0 222 125 1.6*10-2 514 189 |
|--------------------------------------------|-------------|-------------------------------------|----------------------------|
| in matrix A3- Strontium                    | 3.6*10      | -3                                  | 189                        |
| in UO2                                     | 2.2*10      | -3                                  | 488                        |
| in buffer                                  | 1*10        | -8                                  | 0                          |
| in PyC                                     | 2.3*10      | -6                                  | 197                        |
| in SiC                                     | 1.2*10      | -9                                  | 205 1.8*106                |
| in matrix Silver                           | 1.0*10      | -2                                  | 303                        |
| in UO2                                     | 6.7*10      | -9                                  | 165                        |
| in buffer                                  | 1*10        | -8                                  | 0                          |
| in PyC                                     | 5.3*10      | -9                                  | 154                        |
| in SiC                                     | 3.6*10      | -9                                  | 215                        |
| in irradiated matrix A3-3 Krypton (Iodine) | 1.6         |                                     | 258                        |
| in UO2                                     | 8.8*10      | -15                                 | 54 6.0*10-1 480            |
| in buffer                                  | 1*10        | -8                                  | 0                          |
| in PyC                                     | 1*10        | -30                                 | 0                          |
| in SiC                                     | 1*10        | -30                                 | 0                          |
| in matrix                                  | 6.0*10      | -6                                  | 0                          |

$$t_0 = \frac{\ln\left(1 + \frac{\gamma}{2}\right)}{3\gamma D^*}, \quad (12.27)$$

which for small γ can be approximated by

$$t_0 \approx \frac{1}{6D^*}, \quad (12.28)$$

whereby γ is the ratio of layer thickness d to the inner radius, r2, of the layer, D is the diffusion coefficient in the retaining layer, and *D*\* = *Dd*<sup>2</sup> . The underlying assumption is that the only delay in release is determined from the slow diffusion through this coating layer.

Assuming that a fixed number of molecules are completely mobile inside r2 and there is an infinitely fast release from the surface at R = r2+d, mathematically expressed by C(r=R)=0. The breakthrough time estimate comes from the long-time, large release approximation for the release fraction F:

$$F \approx 1 - \left(1 + \frac{\gamma}{2}\right) \exp(-3\lambda D^* t), \quad (12.29)$$

and its zero-crossing F=0. This release fraction ranges from a few percent release to 100% release and comes from the solution of the diffusion equation below with its boundary conditions.

<!-- page 124 -->

In the thin, retaining coating layer *r*<sup>2</sup> ≤ *r* ≤ *R*, characterized by diffusion coefficient D, the diffusion equation (13.8b) describing concentration *c* as a function of time t and radius r for given spherical geometry. Within the coating layer, the initial condition is the concentration is zero, *)t,r(C* ≡= 00 . The boundary condition at the outer surface, r = R, is *cr*() = *R*,*t* ≡ 0 for all times, i.e. infinitely fast evaporation from the surface. Initially, inside the spherical shell, there are N freely movable atoms, i.e. an initial concentration*c*<sup>0</sup> () *<sup>r</sup>*,*<sup>t</sup>* = <sup>0</sup> = *<sup>N</sup>* 4 3<sup>π</sup> *r*<sup>2</sup> <sup>3</sup> , that can

be depleted only by diffusion into the spherical shell

$$-\frac{4\pi r_2^3}{3} \frac{\partial c_o}{\partial t} = -4\pi r_2^2 D \frac{\partial c}{\partial r} \bigg|_{r=r_2} \quad (12.30)$$

Also, it is assumed that the partition coefficient between inner volume and the spherical shell is equal to 1, i.e. *co* = *cr* = *<sup>r</sup>*<sup>2</sup> (),*t* for all times.

Of interest is the cumulative fraction release defined by

$$F = \frac{\int_0^\infty -4\pi R^2 D \frac{\partial c}{\partial r} \Big|_{r=R} dt}{N} \quad (12.31)$$

The solution in Laplace space yields the fractional release *F* whereby s is the Laplace transformed time variable:

$$\bar{F} = \frac{1+\gamma}{s} \cdot \frac{1}{\left(\frac{q^2}{3\gamma} + \gamma\right) \frac{\sinh(q)}{q} + \cosh(q)} \quad (12.32)$$

or alternatively

$$\hat{F} = \frac{1+\gamma}{s} \cdot \frac{3\gamma q / \sinh(q)}{q^2 + \gamma^2 + 3\gamma q \cdot \coth(q)}, \quad (12.32a)$$

$$q \equiv \sqrt{\frac{s}{D^*}}.$$
where,

Transformation into real space gives:

$$F = 1 - \sum_{m=0}^{\infty} T_m \cdot \exp(-y_m^2 \tau), \quad (12.32b)$$

where 
$$\tau \equiv D^* t \equiv \frac{Dt}{d^2}$$
 and coefficients

<!-- page 125 -->

$$\tan y_m = \frac{3\gamma y_m}{y_m^2 - 3\gamma^2}, \quad y_m > 0, \quad (12.33a)$$

$$T_m = \frac{1+\gamma}{\cos y_m} \frac{1}{\frac{y_m^2}{6\gamma} + \frac{1}{2} + \gamma + \frac{3\gamma^2 + 4.5\gamma^3}{y_m^2 + 3\gamma^2}} \quad (12.33b)$$

For short diffusion times <sup>τ</sup> < 0.07, the fractional release can be approximated by

$$F \cong \frac{24\gamma(1+\gamma)}{\sqrt{\pi}} \exp\left(-\frac{1}{4\tau}\right) \tau^{1.5} [1 - 6\tau(1+\gamma) + 12\tau^2(5+6\gamma+6\gamma^2) - +\dots]. \quad (12.34)$$

Figure 66 is a comparison of the release fraction calculated using the exact solution and the approximation for short diffusion times. The fractional release values are nearly identical for diffusion times < 0.07.

![](../_page_124_Figure_6.jpeg)

*Fig. 66. Fractional release calculations based upon the exact solution and the solution for short diffusion times* <sup>τ</sup> = *D*\* *<sup>t</sup>* = *Dt <sup>d</sup>*<sup>2</sup> <sup>&</sup>lt; 0.07 *.*

For large diffusion times <sup>τ</sup> > 0.2, the variables s and q in Laplace space are small and can be approximated by

$$\frac{q}{\sinh q} \approx 1 - \frac{q^2}{6} \text{ and}$$

*<sup>q</sup>*coth*<sup>q</sup>* <sup>≈</sup>1<sup>+</sup> *<sup>q</sup>* 2 3 Substituting them into Eq. (13.33a) the approximation in Laplase space is

$$q \coth q \approx 1 + \frac{q^2}{3}$$
 Substituting them into Eq. (13.33a) the approximation in Laplase space is

<!-- page 126 -->

$$\hat{F} \equiv \frac{1}{2} \frac{\gamma(1+\gamma)}{s} \frac{6-q^2}{q^2+3\gamma^2+3\gamma+\gamma q^2} = \frac{1}{2} \frac{\gamma}{s} \frac{q^2-6}{q^2+3\gamma} = \frac{1}{2} \frac{\gamma}{s} \frac{s-6D^*}{s+3\gamma D^*} = \frac{1}{s} \frac{1+\gamma/2}{s+3\gamma D^*} \quad (12.35)$$

For large diffusion times, i.e.  $\tau > 0.2$ , this approximation becomes

$$F \equiv 1 - \left(1 + \frac{\gamma}{2}\right) \exp(-3\gamma\tau) \quad (12.36)$$

A comparison of the release fraction calculated using the exact solution and the approximation for long diffusion times is shown in Fig. 67. The fractional release values are nearly identical for diffusion times  $> 0.2$ .

![](../_page_125_Figure_15.jpeg)

Fig. 67. Fractional release calculations based upon the exact solution and the solution for long diffusion times ( $\tau = D^*t = \frac{Dt}{d^2} > 0.2$ ).

#### 12.4. Verification and validation

The verification and validation status of calculation models and software used in safety calculations for design and licensing purposes are critical to the success of such an application. The terms verification and validation are defined below:

**Verification:** Verification is the assurance that the operations specified in a numerical model are correctly performed.

**Validation:** Validation is the assurance that a computational method is a correct and independent representation of the process or system for which it is intended.

<!-- page 127 -->

#### *12.4.1. Verification*

The first step in any verification effort is to ensure that the theory and principles underlying the software product or model are clearly understood. For legacy calculation models, this usually requires reverse engineering of software and re-evaluation of parameters used. After the theory is understood, it must be ascertained that the theory has been correctly applied, followed by mathematical verification of numerical solutions.

Additionally, alternative calculation models may be used in comparisons and benchmarking exercises, for example comparison between the analytical solutions namely 'Booth equation' [161] and numerical solution for Fick's laws for short lived fission products. A comparison between different codes completes the verification effort.

In general, the computer codes used to predict fission product transport in HTGR cores are judged to have been properly verified.

# *12.4.2. Validation*

Validation usually requires more effort, as real life experiments and benchmarks must be evaluated. A thorough evaluation of independent data available from suitable irradiation and post-irradiation heating tests is required. For spherical fuel, the irradiation tests performed in the High Flux Reactor in Petten, HFR-K5, and -K6, are highly valuable data for validation purposes. The evaluation of the heatup investigations performed in the cold finger apparatus (KÜFA) after HFR-K3 irradiation gives valuable information for metallic fission product transport validation. Measurements done during the HFR-K5 and -K6 irradiations provide good data for gaseous fission product release validation [\[164\].](#page-175-11)

# **12.5. Pebble bed reactor/spherical fuel example: PBMR calculation model**

# *12.5.1. Information required*

Fuel analyses require an understanding of almost all the fields of nuclear engineering. An understanding of the fuel design and the reactor design in which it will be used are vital. The data and parameters required can be summarized as follows:

- **Core data.** The core geometry, expected core power under various operating conditions, fuel residence times and different enrichments used are required.
- **Neutronics and thermal-hydraulics.** Neutron fluxes and their corresponding cross sections for the specific nuclides of interest, along with their fission yields, must be known. In addition, removal due to neutron absorption and decay must be considered. The temperatures, pressures and flow rated of the coolant medium are also required.
- **Material data.** A thorough understanding of the fuel specifications, heat transfer and transport parameters of all fuel materials.
- **Coated particle performance.** Coated particle performance may be estimated by a calculation model or a statistical evaluation may be used. The PBMR example shown in Fig. 68 is based on a statistical evaluation of all German irradiation and heat-up testing results [\[165\].](#page-175-12)

<!-- page 128 -->

![](../_page_127_Figure_0.jpeg)

*Fig. 68. PBMR and HTGR-module failure fraction vs. temperature curves.* 

# *12.5.2. Calculation models - PBMR example*

The diffusion coefficient for gaseous fission product transport through a PyC layer is ~2×10-18 m2 /s. Then for all practical purposes, PyC can be considered impervious to fission gases [\[166\].](#page-175-13) Hence the gaseous fission product source term for intact coated particles can be ignored. Furthermore, the half-lives for most fission gases are relatively short and only steady-state conditions can realistically be assessed. However, this is not the case for longlived metallic fission products. Two separate calculation models are therefore required to predict all the radiological significant fission products released from the fuel.

# *12.5.2.1. Short-lived fission products*

The short-lived fission product calculational model is presented in Fig. 69. Releases are calculated with the NOBLEG software program, a legacy code from the German fuel development program. It is in principal based on Booth's "equivalent sphere" model, and calculates the steady state releases of fission gases from fuel [\[162\]](#page-175-14).

It contains a thermo-hydraulic routine that calculates fuel temperatures based on the power produced and coolant temperatures in each core region. Fission product production is determined by the power produced in each core region. Transport of gaseous fission products are calculated from contamination sources in the matrix material and from defective coated particles source. Defective coated particles are treated as bare kernels. The NOBLEG transport model describing the release of fission gases from defect particles and contamination is shown in Fig. 70.

<!-- page 129 -->

![](../_page_128_Diagram_0.jpeg)

*Fig. 69. PBMR short-lived fission product calculational model.* 

![](../_page_128_Diagram_3.jpeg)

*Fig.70. NOBLEG model for fission gas release calculations, after [\[162\]](#page-175-14).*

For the release of fission gases from uranium and thorium contamination in the matrix material, the graphitic material is treated as a three-component system. Component 1 may be attributed to the graphite grains of the raw material, and component 2 to the amorphous, nongraphitized binder coke between the grains. The open pore system filled with helium constitutes the gaseous component 3. Primary fission products are distributed homogeneously in these components by direct recoil. Gas atoms diffuse from the recoil sites in the grains of the solid components to the open porosity of the fuel sphere.

<!-- page 130 -->

For the release of fission gases from defective coated particles, a four-component system is used. It consists of kernel 'grains', two material components of the buffer layer ('grains' and 'amorphous constituents'), and helium-filled open pores in the kernel and in the porous buffer layer. The birth rates of primary fission products in the four components are calculated with the known relations for the recoil stopping ranges in different materials. In the NOBLEG code these transport processes are solved separately for each model, and combined over all regions of the core. An R/B calculation for all relevant fission gases (Kr + Xe) is shown in Fig. 71 as a function of half-life.

![](../_page_129_Figure_1.jpeg)

*Fig. 71. Total R/B at 1000o C fuel temperature, 9 MPa helium pressure.* 

# *12.5.2.2. Long lived fission products*

The long-lived fission product calculation model is presented in Fig. 72. Releases are calculated with the GETTER code [\[166\].](#page-175-13) It is based on Fick's laws of diffusion, and calculates the dynamic release of fission products from fuel. Differential equations are solved numerically with specific boundary conditions.

The GETTER code includes subroutines that calculate the burnup and the power history of a fuel sphere in the core and the temperature distribution in the spheres on the bases of given neutron cross sections and gas temperatures. Fission product production is determined by the power produced in each core region. Transport of metallic fission products are calculated for contamination sources in the matrix material, intact coated particles and from failed coated particles. Defective coated particles are treated as bare kernels, and intact coated particles according to the specific fuel design.

In case of activation products (134Cs, 110mAg), GETTER is run two times: first for the release of the parent nuclide (133Cs, 109Ag); and a second time for the activation products whereby the time dependent concentration profiles of the parent nuclides define the source term for the 

<!-- page 131 -->

second run. For gas precursors (137Xe -> 137Cs or 90Kr -> 90Sr), a Booth type calculation similar to the NOBLEG model is applied.

![](../_page_130_Diagram_1.jpeg)

*Fig. 72. PBMR long-lived fission product calculational model.* 

The metallic fission product section has been expanded to include non-metallic fission product analyses as well. In order to determine iodine release during accident conditions, GETTER was also equipped to handle branched diffusion coefficients. Special storage condition equations were also derived from AVR fuel element storage tests to perform 85Kr release analyses under similar storage conditions.

Figure 73 describes the release of 110mAg from a fuel element (sphere) for 6 passes through an illustration PBMR core. The release increases for each subsequent pass as the fission product inventory grows and silver is transported through the fuel constituent materials.

<!-- page 132 -->

![](../_page_131_Figure_0.jpeg)

*Fig. 73. Expected 110mAg release from a spherical fuel element.* 

# *12.5.2.3. Full core analyses*

The PBMR core consists of a bed of spherical fuel elements. The fuel elements are introduced at the top of the core, flow downwards and exit from the base of the core. This flow pattern is modeled using a number of vertical flow channels, each flow channel being axially subdivided into core regions. A typical PBMR core is modeled as 4 to 6 flow channels, with each channel consisting of between 10 and 20 axial subdivisions, resulting in 70 to 120 core regions. The axial subdivisions are chosen so that the residence times for the fuel elements in all core regions are equal, typically 8 to 12 days. These core regions, not necessarily of equal volume, are used by the core neutronics, thermo-hydraulic and fission product release codes to model the entire core.

Depending on the fuel-loading scheme, the fuel elements may pass through the pebble bed core up to 16 times before finally being discarded. The core, therefore, consists of a random mixture of fuel elements with different irradiation histories.

The GETTER code calculates the fission product release rate for a single fuel element at each time-step throughout its residence history in the core. In order to accurately represent the entire core (approximately 450 000 fuel elements in the 400 MWth design), individual fuelelement histories are sampled and a GETTER calculation performed for each. The results are then combined using arithmetic averaging and normalization to determine total core release rates.

This implies that GETTER must calculate all the fuel element release histories in the core for all the possible irradiation histories, given that the irradiation and temperature conditions in each flow channel of the core are unique. Performing GETTER calculations for each of the 450 000 elements in the reactor core are not feasible. Furthermore, exact calculation of 

<!-- page 133 -->

DLOFC-type accidents would be virtually impossible because the accident can occur at any time-step in a specific fuel element's irradiation history.

However, it was found that significantly smaller sample sizes give satisfactory statistical convergence. Multiple independent calculations using sample sizes of 10 000 fuel elements, for example, showed a variance in calculated release rates of <1%. The FIPREX-GETTER software was developed to generate GETTER input files for both normal operation and accident conditions [\[166\]](#page-175-13). Accident conditions can be defined and the time of accident specified.

Figure 74 presents the predicted 111Ag release from the illustration PBMR core during four different accident events. A medium pipe break with very short coolant depressurization and small pipe breaks with depressurization times of 24, 48 and 72 hours.

![](../_page_132_Figure_3.jpeg)

*Fig. 74. Predicted 111Ag releases from fuel during small and medium pipe break accident events as a function of accident duration.* 

# *12.5.2.4. Uncertainty analyses*

Input parameters, values and data sets that include uncertainty in their derivation are investigated to determine a design value for fission product release under the specified operating conditions. Uncertain parameters and values can be categorized and described as follows:

- The diffusion coefficients describing metallic fission product transport through the fuel materials were derived from irradiation experiments conducted on TRISO particles, fuel compacts and complete fuel spheres. Due to uncertainties in the measurements taken during irradiation and in irradiation conditions, uncertainty factors of between two and eight were suggested for metallic diffusion constants.
- The fuel specification allows maximum values for the uncontained uranium fraction of 6×10-5 and the thorium contamination of 0.4 mg thorium per spherical fuel element. This defines upper limits for the failed particle fraction, the uranium

<!-- page 134 -->

contamination and the thorium contamination of 5.6×10-5, 4.0×10-6 and 6.0×10-6 (effective), respectively.

- The uncertainty in the sorption isotherm was calculated by assuming a variation in the partial pressures by a factor of four.
- Thermo hydraulic uncertainties in the material properties and correlations used lead to uncertainties in fuel temperatures.
- The statistical evaluation of German irradiation experiments with TRISO UO2 particles showed that due to the restricted sample size (Poisson distribution), growing failure fractions cannot be excluded at burn-ups above 5% FIMA. The uncertainty in the failure fraction under excessive temperature is derived from statistical evaluations of experimentally measured failure fractions. These expected curves and their uncertainty ranges were modeled and are used in design calculations.
- Neutronic uncertainties are cross section and neutron fluxes that lead to uncertainties in power production, temperatures, burn-up and inventories.

Three types of uncertainty analyses have been developed:

- S**tacked uncertainty analyses**. All uncertain parameters are simply set to their design parameters and the calculation is performed. This method is most conservative, relatively simple to perform, and easy to defend.
- **Monte Carlo analyses**. For each parameter, a suitable probability distribution is chosen and values are randomly sampled (example shown in Figure 74. After the Monte Carlo calculations are done, the upper 95% confidence limit is determined from the sampled output. This complicated method calculates the lowest design values, but is very difficult to defend.
- **Least squares analyses.** Each uncertain parameter is evaluated separately. The result is squared and added to the squared results of all the other parameter evaluations. The square of this sum gives the design value. Most information is extracted from this method, but is extremely time consuming.

All three uncertainty analyses methods have their place in core design and analyses. Monte Carlo analyses is quick and can be used to compare different core designs, least square analyses tells us what parameters are most important for different conditions, and stacked analyses provides the upper limit for design calculations for licensing applications.

### **12.6. Prismatic core reactor/graphite block - HTR-GT example**

# *12.6.1. Introduction*

A characteristic feature of HTGRs is the essential role of the coated fuel particle acting as miniature containment and serving as the main barrier against radionuclide release under all operational and accidental conditions. The performance of TRISO fuel particles and other types of coated fuel particles has been extensively investigated and a number of performance models developed. Previously published fuel performance models were largely developed in the US, the UK and Germany [\[167\].](#page-175-15) A detailed compilation of these models has been published as an IAEA-TECDOC-978 [16].

The following present a description and gives some preliminary results of the fission product diffusion model, developed at AREVA NP.

<!-- page 135 -->

#### Objective

The main purpose of this work is to estimate, as an example, the inventory of the fission product 137Cs released into helium coolant of the core of the Japanese 600 MWth HTR-GT concept. These results are then compared with the available calculated values from the JAEA Japanese team [\[168\]](#page-176-0) for their 600 MWth HTR-GT concept.

# *12.6.2. Diffusion model hypothesis in the particle*

Fick's diffusion with an equivalent diffusion coefficient that generalizes all diffusion mechanisms is adopted. The source term in the kernel and radioactive decay must be added to complete the mass balance:

$$\frac{\partial c}{\partial t} = \nabla \cdot D \nabla c - \lambda c + \dot{S} \quad (12.8)$$

c: fission product concentration (m-3) λ: decay constant (7.297.10-10 s-1 for 137Cs)

S: source term (m-3.s-1)

D: equivalent diffusion coefficient of the considered layer, D = D0 exp -

Q RT

 Do: pre exponential term (m2

.s-1)

Q: activation energy (J.mol-1)

R = 8.3145 J/mol/K T: temperature (K)

Equivalent diffusion coefficients :

According to the IAEA publication reference [16], the values for the pre-exponential term (D0) and the activation energy (Q) which defines the 137Cs diffusion in the fuel constituent materials in this study are shown in Table 16.

Table 16. PRE-EXPONENTIAL AND ACTIVATION ENERGY COMPONENTS OF THE EQUIVALENT DIFFUSION COEFFICIENT FOR CESIUM IN FUEL CONSTITUENT MATERIALS FOR THE HTR-GT CONCEPT [\[168\]](#page-176-0) 

|                                    |            |            |             | /s)        |                |                |
|------------------------------------|------------|------------|-------------|------------|----------------|----------------|
| UO2                                | Buffer     | iPyC       | SiC         | oPyC       | Compact Matrix | Graphite Block |
| 6.75x10 -6 Pre-exponential (m2 /s) | 6.69x10 -6 | 6.69x10 -9 | 6.75x10 -12 | 6.69x10 -9 | 3.6x10 -4      | 9 x10 -6       |
| 177 000 Activation Energy J/(mol)  | 197 880    | 197 880    | 177 000     | 197 880    | 189 000        | 157 140        |

# *12.6.3. Fraction of defective fuel particles*

Three types of particle have to be considered:

<!-- page 136 -->

- 1. **Particle with A Failed SiC Layer** (Fig. 75). The diffusion coefficient of the defective layer is replaced by the PyC value. The fraction of coated particles with this defect in the total particle population is equal to 5x10**-**<sup>4</sup> according to reference [\[168\].](#page-176-0)
- 2. **Exposed UO2 Fuel Kernels** (Fig. 76). These particles have all their coatings completely failed allowing fission products to migrate directly and rapidly outside the particle. The fraction of coated particles this type of particle is equal to 2.10**-**<sup>5</sup> according to reference [\[168\]](#page-176-0).
- 3. **Intact Particles** All the coatings of these particles are unbroken.

![](../_page_135_Picture_1.jpeg)

*Fig. 75. Photomicrograph of an irradiated particle with a through-crack in the SiC layer.* 

![](../_page_135_Picture_3.jpeg)

*Fig. 76. Irradiated particle with through cracks in all of its coating layers (iPyC, SiC, oPyC, and an outer protective layer).* 

# *12.6.4. Diffusion from the fuel compact or graphite block to the coolant*

It is necessary to know the fraction of fission products that pass through the graphite block to the helium coolant. At the boundary between a solid and a gas, the transition of diffusing atoms occurs by the processes of sorption and evaporation. In most cases, these two processes are so fast that a local equilibrium between the concentration of atoms adsorbed at the solid surface and the concentration of atoms in the neighboring layer of gas ("vapor pressure") may 

<!-- page 137 -->

be assumed. This means that the phenomenological data of importance is the sorption equation which relates these two equilibrium values.

Generally the equilibrium vapor pressure in the gas phase is expressed as a function of the fractional coverage of the solid surface by adsorbed atoms. In practice, adsorption is mainly of importance in the case of porous solids which have a large internal surface area per unit weight. The vapor pressure is expressed as an exponential function of temperature and adsorbed concentration.

The transition of metallic fission products between fuel element surface and the turbulent coolant is described by sorption isotherms. Figure 77 [16] is an example of the sorption isotherms in the case of cesium on H-451 graphite.

![](../_page_136_Figure_3.jpeg)

*Fig. 77. Sorption isotherms for cesium on H-451 graphite [16].* 

To determine the concentration of fission products in the helium when it is known in the graphite, the relevant equations are the Henry's law, the Freundlich's law and the ideal gas law. The partial pressure is assumed to be the sum of the pressures calculated with the two isotherms (see Fig. 77):

$$p = p_H + p_F$$
, (13.14a)

Henry's law dominates at low concentrations and which supposes an adsorption heat directly proportional to the pressures and the concentrations of the adsorbed species and is given by the expression:

<!-- page 138 -->

$$p_H = c_s \exp \left[ \left( A + \frac{B}{T} \right) + \left( D - 1 + \frac{E}{T} \right) \ln c_t \right], \quad (12.15)$$

Freundlich's law dominates at higher concentrations and assumes a decreasing adsorption heat and an increasing concentration is given by the expression:

$$p_F = \exp \left[ \left( A + \frac{B}{T} \right) + \left( D + \frac{E}{T} \right) \ln c_s \right], \text{ and} \quad (12.16)$$

$$\text{transition at } c_t: \ln c_t = d_1 - d_2 T, \quad (12.17)$$

where  $T$  is the absolute temperature (K)  
 $c_s$  is the mass concentration of sorbate (mol/kg of carbon or graphite)  
A, B, D, E,  $c_t$ ,  $d_1$ ,  $d_2$  are empirically derived constants given in [16].

The ideal gas law is applied to the sum of both Henry and Freundlich pressures.

From the boundary helium gas layer, fission products are transported into the coolant. The governing equation in the helium coolant is given by:

$$\frac{\partial c_{He}(x,t)}{\partial t} = - \frac{\partial v(x) c_{He}(x,t)}{\partial x} - \frac{k_m(x,t) \cdot p_L(x)}{A_f(x)} (c_{He}(x,t) - c_b(x,t)) \quad (12.38)$$

where:

| $c_{He}$ : | concentration of fission product in turbulent helium gas stream; |
|------------|------------------------------------------------------------------|
| $c_b$ :    | concentration of fission product in boundary layer;              |
| $A_f$ :    | sectional flow area ( $m^2$ );                                   |
| $k_m$ :    | mass transfer coefficient ( $m \cdot s^{-1}$ );                  |
| $p_L$ :    | wetted perimeter (m);                                            |
| $v$ :      | helium velocity ( $m \cdot s^{-1}$ ).                            |

In the Japanese model [168], a global parameter " $\alpha$ " is introduced and used as the ratio of an absorbed fission product concentration to a transported fission product concentration.

Figure 78 shows the global parameter " $\alpha$ " as a function of temperature over the range of 100°C to 900°C for the fission product  $^{137}Cs$  and the activation product  $^{110m}Ag$ . Above temperatures of 700°C, the concentration ratio for key fission products between the helium coolant and graphite is given by  $c_{He} = 0.9 c_{Gr}$ . These simplified functions are based on measurements made at Peach Bottom HGR Nuclear Power Plant.

<!-- page 139 -->

![](../_page_138_Figure_0.jpeg)

*Fig. 78. The global parameter "*α*" which represents the concentration ratio of absorbed fission product to a transported fission product as a function of temperature [\[168\]](#page-176-0).* 

# *12.6.5. Fuel loading scheme*

During its lifetime within the prismatic core, a hexagonal fuel assembly occupies three different locations within the core and experiences three different ranges of temperature before being removed from the plant. Modeling this subassembly redistribution within the core is complicated. In order to simplify, and at this step of evaluation, a so called Daruma-Otoshi fuel loading scheme is adopted. This is a simplified scheme which well represents the more complicated real one. It models and shares the whole core in nine equivalent blocks which are grouped by three. This Daruma-Otoshi scheme is employed in the Japanese code FORNAX [\[168\]](#page-176-0) and for the HTR-GT is represented in Fig. 79 below:

*Fig. 79. The HTR-GT Daruma-Otoshi fuel loading scheme employed in the Japanese code FORNAX [\[168\]](#page-176-0).* 

<!-- page 140 -->

#### *12.6.6. Temperature maps*

# *12.6.6.1. In TRISO coated fuel particles*

For the TRISO particles of HTR-GT project, the temperature profile shown in Fig. 75 is representative of steady- state normal operating conditions.

![](../_page_139_Figure_3.jpeg)

*Fig. 80. Temperature profile across the UO2 TRISO coated particle in a typical high temperature reactor operation*.

# *12.6.6.2. In the compact matrix and graphite blocks*

The temperature distributions in the fuel compact matrix and graphite blocks of the HTR-GT, calculated in the AREVA NP studies, have been adopted for steady- state normal operating conditions. These temperature distributions are shown below in Fig. 81. A comparison of the temperatures experienced in the helium coolant, fuel compacts and hexagonal block graphite as a function of core height are shown in Fig. 82. These temperatures are also from the AREVA NP studies.

In order to apply a "Daruma Otoshi" Fuel Loading Scheme [\[168\]](#page-176-0), the hexagonal graphite columns are divided in nine fictitious blocks and for each column an exponential average temperature has been calculated as it is done for the different layers of a TRISO particle. Nine equivalent diffusion coefficients linked to the height in the core are then obtained.

<!-- page 141 -->

![](../_page_140_Figure_0.jpeg)

*Fig. 81. Temperature distributions in the fuel compact and hexagonal block graphite for the NTGR-GT concept based on analyses performed by AREVA-NP.* 

![](../_page_140_Figure_2.jpeg)

*Fig. 82. Temperature comparison as a function of core height for the He coolant, fuel compacts and graphite blocks in the HTR-GT concept.* 

# *12.6.7. Finite difference code description*

The code developed for calculating the release of a single metallic fission product nuclide (e.g., 137Cs) from the core of a HTGR is a one-dimensional, finite difference computer program. It calculates the diffusive transport of fission products through multi-layered coated particles, graphite matrix (compact and hexagonal block or spherical elements), equilibrium evaporation and condensation at the graphite surfaces, and diffusion across the coolant boundary layer. The code is based on the discretization of the selected Fickian Diffusion Law by means of the Forward Time Centered Space scheme.

<!-- page 142 -->

$$\frac{\partial c}{\partial t} = D \cdot \left[ \frac{\partial^2 c}{\partial x^2} + \frac{\partial^2 c}{\partial y^2} + \frac{\partial^2 c}{\partial z^2} \right] - \lambda c + \dot{S} \quad (12.8a)$$

in Cartesian co-ordinates (for graphite block geometry),

$$\frac{\partial c}{\partial t} = D \cdot \frac{1}{r^2} \frac{\partial}{\partial r} (r^2 \frac{\partial c}{\partial r}) - \lambda c + \dot{S} \quad (12.8b)$$

in spherical co-ordinates (for TRISO particles geometry), and

$$\frac{\partial c}{\partial t} = D \cdot \frac{1}{r} \frac{\partial}{\partial r} (r \frac{\partial c}{\partial r}) - \lambda c + \dot{S} \quad (12.8c)$$

in cylindrical co-ordinates (for compact geometry).

The explicit scheme employed can be unstable if the parameters ∂t and ∂r do not verify stability criteria. The Von Neumann Stability Analysis is a stability criterion that is applied to all the calculations. For the three systems of co-ordinates, the Forward Time Centered Space scheme applies to our equation is stable if:

$$\frac{2D \cdot dt}{dr^2} + \lambda \cdot dt \leq 1 \quad (12.39)$$

Thus, the values of ∂t and ∂r chosen in the code are always verified by this criteria.

# *12.6.8. Results*

Table 17 summarizes the 137Cs release results obtained with the AREVA NP evaluation and compares it to the results obtained in by the JAEA [\[168\]](#page-176-0).

In the AREVA NP modeling analysis, nearly all of the main Japanese hypotheses (fuel loading scheme, TRISO particle design and core dimensions, sorption - desorption simplified function, diffusion coefficients, etc.) were used as in the JAEA in-house code FORNAX [\[168\].](#page-176-0) Since the diffusion coefficients are being exponentially dependant on the temperature, a relatively small difference in the selected temperatures can explain the difference between the two evaluations.

Table 17. COMPARISON OF THE 137CS INVENTORY RELEASED TO THE COOLANT FOR THE HTR-GT CONCEPT FROM THE AREVA NP ANALYSIS WITH THE JAEA RESULTS [\[168\]](#page-176-0) 

| HTR-GT Concept                                        | AREVA NP Result            | JAEA Result                |
|-------------------------------------------------------|----------------------------|----------------------------|
| 137Cs Released to Coolant after 450 days of operation | 11.25 x10 <sup>12</sup> Bq | 15.84 x10 <sup>12</sup> Bq |

<!-- page 143 -->

