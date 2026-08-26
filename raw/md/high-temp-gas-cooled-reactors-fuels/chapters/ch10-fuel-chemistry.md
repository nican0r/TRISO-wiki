---
type: source-chapter
chapter: 10
title: Fuel Chemistry
pages: 93-106
source_md: high-temp-gas-cooled-reactors-fuels.md
---

# **10. FUEL CHEMISTRY**

#### **10.1. Introduction**

The wide-ranging phenomena occurring during irradiation of oxide fuels has been more or less understood for a long time [\[89\].](#page-172-1) This knowledge can be applied qualitatively to the oxide fuel kernels of the HTGR LEU TRISO coated particles. Fission process in uranium atoms produces a great variety of fission products, radiation, as well as neutrons. The fission products can themselves be radioactively unstable leading to additional nuclides. Another important consequence of UO2 fission is the creation of free oxygen since only a part of the O2 recombines with the fission products. In the TRISO particle, an important parameter is that portion of this free oxygen which combines with carbon from the PyC coatings to form CO and CO2 gases. Identification of those compounds (solid and gaseous) that can form in fuel during normal and off-normal conditions and which elements remain in elemental form, is known as fuel chemistry. This chemistry may lead to many important mechanisms affecting fuel performance, e.g., kernel size (swelling), kernel migration (amoeba effect), stresses in the 

<!-- page 94 -->

coatings (particle pressurization due to fission products and carbon oxide gases), thermal conductivity, creep properties modification, etc.

The oxygen potential, the pressure of oxygen in the gas phase within the fuel, is the critical parameter determining which elements in their competition for oxygen form oxides. Calculation of the oxygen potential is complex since it generally varies with distance from the particle center and with temperature, fuel burnup, fission product yields, chemical state of fission products including solid and gas phases and the effectiveness of the coating layers (notably the buffer) to absorb fission products and oxygen. Furthermore, in comparison with Light-Water Reactor (LWR) fuels, four parameters influencing the oxygen potential and fuel physical-chemistry are significantly different: the higher temperature prevailing in the kernel under normal conditions (between 1273 and 1473 K compared to around 773-1273 K for LWRs), higher enrichment, higher fission rate and higher final burnup (10 to 15 at% compared to about 5 at%). In addition, the fuel temperature in HTGRs is, for the vast majority of particles, fairly uniform, whereas in LWR fuel pellets a significant radial temperature gradient exist. Furthermore, the TRISO particle induces specific thermo-mechanical kernel behavior which in turn can modify fission product behavior (e.g., the local stresses may play a determining role).

In this Chapter, the relevant phenomenology focusing on the different aspects that affect the oxygen potential are summarized along with illustration of existing models used for evaluation. The complexity of the chemical system leads to a need to first consider unirradiated oxide fuel and then to highlight modifications due to formation and inclusion of fission products in the fuel-coating system.

# **10.2. Unirradiated fuel**

The unirradiated fuel particle comprises a UO2 fuel kernel, the porous-carbon coating, the IPyC layer, the silicon carbide coating and the OPyC layer. A detailed description of this chemical system was given in [\[90\]](#page-172-2) and is summarized therein. At the nominal temperature of an HTGR, one can assume (in an initial approach) that the fuel within the coated particle reaches thermodynamic equilibrium with its surrounding coatings. The main product of the reaction between UO2+x (x>0) and carbon is gaseous carbon monoxide, CO, by the following reactions:

| $\text{UO}_{2+\text{x}} \rightarrow \text{UO}_{2+\text{y}} + \frac{1}{2} (\text{x-y}) \text{O}_2$ | (10-1) |
|---------------------------------------------------------------------------------------------------|--------|
|---------------------------------------------------------------------------------------------------|--------|

| $¼(x-y) O_2^+(x-y) C \rightarrow (x-y) CO$ | (10-2) |
|--------------------------------------------|--------|
|--------------------------------------------|--------|

i.e., by the equation:

| $\text{UO}_{2+\text{x}} + (\text{x-y}) \text{C} \rightarrow \text{UO}_{2+\text{y}} + (\text{x-y}) \text{CO}$ | (10-3) |
|--------------------------------------------------------------------------------------------------------------|--------|
|--------------------------------------------------------------------------------------------------------------|--------|

If reaction (2) has equilibrium constant Kp, one may write:

| $\text{Log P(CO)} = \text{Log } K_p + \frac{1}{2} \text{Log P(O}_2\text{)}$ | (10-4) |
|-----------------------------------------------------------------------------|--------|
|-----------------------------------------------------------------------------|--------|

where, Kp, is the oxidation constant of carbon up to carbon monoxide (which can be found, e.g., in [\[91\]](#page-172-3)) and PCO the pressure of CO gas (in atm.) and P(O2) the oxygen partial pressure (in atm.) linked with the oxygen potential, μ(O2) (in J/mol). The oxygen potential is represented by the following relationship:

<!-- page 95 -->

| $\mu(\text{O}_2) = \text{RT Log P}(\text{O}_2)$ | (10-5) |
|-------------------------------------------------|--------|
|-------------------------------------------------|--------|

where, R is the Universal Gas Constant and T the absolute temperature (K). Stoichiometric UO2 has an oxygen potential of roughly -400 kJ/mol at nominal HTGR operating temperatures.

Figure 50 shows U-O-C phase diagram at 1573K from [\[92\].](#page-172-4)

![](../_page_94_Picture_4.jpeg)

*Fig.50. U-O-C phase diagram at 1573K.* 

According to the U-O-C phase diagram at 1573 K (Fig. 50) [\[92\]](#page-172-4), if O/U>2 with an excess of carbon (which typically corresponds to the chemical system with the fuel kernel surrounding by the carbon buffer), there are only two condensed phases (UO2+xand C). In this biphasic domain, the pressure of CO gas not only depends on temperature but also on the O/U ratio in UO2+x, in other words on the oxygen potential variations in the UO2±x phase (a review of the µ(O2) variations is available in [\[93\]](#page-172-5), [\[94\]](#page-172-6)).

Thermodynamic calculations (Fig. 51) shows that, at 1573 K, CO pressure dominates over the entire interval of oxygen potentials between –700 and –300 kJ/mol. At lower temperature CO2 may dominate.

<!-- page 96 -->

![](../_page_95_Figure_0.jpeg)

*Fig. 51. Calculated thermodynamic pressures of CO, CO2 as a function of oxygen potential for UO2 kernel and a buffer volume fixed at 3.10-11 m 3 at 1573 K using the MEPHISTA thermodynamic database [\[95\].](#page-172-7)* 

The result of CO (and CO2) formation is internal pressurization of the particle coatings which may lead, in extreme conditions, to particle failure. To limit this pressurization other fuelkernel concepts have been and are being studied. Of particular interest is the oxycarbide fuel (or UCO) comprising a mixture of UC2 and UO2 [\[116\]](#page-173-0). Gas formation is effectively reduced within the UCO particle as compared to a UO2 particle due primarily to their lower oxygen inventory as well as to the gettering effect the UC2 has on the oxygen released during UO2 fission to form condensed oxide rather than CO gas. The presence of both oxide and carbide phases in the kernel allows chemical "buffering" of the oxygen potential and hence the CO pressure. The calculated oxygen potential along the composition line UC2-O at 1573 K in the U-O-C phase diagram is represented in Fig. 52. It shows that the oxygen potential [μ(O2)] is effectively reduced to –700 kJ/mol in the triphasic domain UC2-UO2+C in comparison to the biphasic domain UO2+x+C.

<!-- page 97 -->

![](../_page_96_Figure_0.jpeg)

*Fig. 52. Calculated oxygen potential as a function of O/U (along the composition line UC2-O in the U-O-C phase diagram) at 1 573 K using the thermodynamic MEPHISTA database [\[95\].](#page-172-7)* 

#### **10.3. Irradiated fuel**

#### *10.3.1. Particle composition and fission product behavior*

Element and isotope inventories for irradiated high burnup HTGR fuel are as well-known as they are for low burnup LWR fuel. The rate of change of each nuclide is a function of three processes:

 depletion of heavy nuclei by fission and corresponding production of lighter nuclei (fission products); production by radioactive decay (actinides and fission products) and/or by neutron capture (actinides); and loss by radioactive decay (actinides and fission products) and/or by neutron capture (actinides).

Nuclide production and inventory variations during irradiation are described by the Bateman equation which is, in fact, a coupled set of rate equations (one for each nuclide) as a function of neutron flux. To calculate HTGR core isotope inventories it is usual to apply general computer codes developed for depletion/decay in nuclear fuels such as ORIGEN2 [\[101\]](#page-172-8) with an appropriate library of cross-sections for HTGR conditions; indeed, this depletion/decay code may be used, e.g., in a core analysis via the MONTEBURNS coupled neutronic/isotopic Monte Carlo code system [\[102\].](#page-172-9) For fuel chemistry, the isotopic details are of no interest since it is the relative quantities of each element that are really important. An element inventory for an irradiated HTGR particle is illustrated in Table 13 below.

# **Location of fission products in UO2 fuel**

Fission products exist in the fuel lattice as atoms and ions. Their location depends mainly on the fuel stoichiometry. Atomic-scale calculations performed for LWR fuel show Xe incorporated in uranium vacancies in UO2+x (or divacancy in stoichiometric UO2) [\[117\]](#page-173-1). The same is foreseen for Cs, Ba, Sr, Zr and the rare earths (Sm, La, Nd, Pr, Ce, Y). Molybdenum 

<!-- page 98 -->

might also be incorporated in uranium vacancies [\[118\]](#page-173-2), [\[119\]](#page-173-3) with Mo ionization varying with O/M ratio. Iodine, Br and Te are also found most stable in uranium vacancies in possibly different charge states including cationic ones.

Table 13. ELEMENTAL INVENTORY IN AN HTGR FUEL PARTICLE AT 5.5% FIMA (FROM [\[103\]](#page-172-10))

| Element | Amount (10-8 moles) | Element | Amount (10-8 moles) |
|---------|---------------------|---------|---------------------|
| UO2     | 411                 | Zr      | 6.49                |
| C       | 755                 | Ru      | 3.63                |
| Kr      | 0.74                | Ba      | 1.57                |
| Xe      | 5.32                | La      | 1.46                |
| Sr      | 1.78                | Ag      | 0.13                |
| Se      | 0.12                | Br      | 0.04                |
| Rb      | 0.70                | Y       | 0.91                |
| Mo      | 5.74                | Tc      | 1.47                |
| Rh      | 1.03                | Pd      | 1.08                |
| Cd      | 0.06                | Sn      | 0.06                |
| Sb      | 0.03                | Te      | 0.57                |
| I       | 0.29                | Cs      | 4.79                |
| Ce      | 2.75                | Pr      | 1.35                |
| Nd      | 4.62                | Sm      | 0.52                |
| Eu      | 0.07                | Gd      | 0.02                |

# **Solubility of fission products in UO2 fuel**

From atomic-scale calculations, it is also possible to derive estimates of fission product solubilities in irradiated UO2 to be compared to the values obtained from experiments [\[120\]](#page-173-4). It is well acknowledged that noble gases exhibit almost total insolubility. Iodine, Br and Te are also highly insoluble whereas Cs and Ba exhibit only low solubility in the case of hyperstoichiometric fuel. Then the solubility increases from Zr (depending on temperature) to Sr, reaching very high solubilities for the rare earth elements, namely Ce, which is extremely soluble.

# **Behavior of gaseous fission products (Xe and Kr) in UO2 fuel**

Fission products in the fuel lattice can diffuse out of the UO2+x to grain boundaries. The diffusion mechanism depends on the nature of the fission product trap sites and on the fission product intrinsic characteristics (size and charge, see [\[121\]\)](#page-173-5). Irradiation effects can greatly enhance or reduce this diffusion by trapping mechanisms on extended defects (dislocations, for example).

The behavior of fission-gases is unique because of their very low solubility and high volatility. The gases precipitate primarily as intragranular bubbles. These bubbles can grow by gas-atom and vacancy absorption [\[122\]](#page-173-6). Generally speaking, bubble mobility is limited (defects and impurities created by irradiation limit bubble diffusivity) [\[123\];](#page-173-7) nevertheless, because of high fuel temperatures, some bubble coalescence can not be excluded. Additional mechanisms for bubble growth are associated with interactions with dislocations, essentially at high burnup, that can induce high local stresses increasing bubble diffusivity, bubble trapping [\[124\]](#page-173-8) and the possibility of bubble growth by dislocation-loop punching (mainly during transients) [\[125\]](#page-173-9). The thermodynamic state in the bubbles depends greatly on the 

<!-- page 99 -->

interaction with defects, mainly vacancies. Bubble relaxation is a function of the local vacancy concentration, and in the case of limited vacancy concentration, highly-overpressurized bubbles can be observed [\[124\]](#page-173-8). For the UO2 kernel in TRISO fuel particles, both fission-rate and temperature help to strongly limit bubble size and maintain a substantial fission-gas atom population in the fuel lattice by re-solution of gas from bubbles. Fission gases can migrate to grain boundaries by atomic or bubble diffusion to form intergranular bubbles (porosities) where they can grow by addition of gas and vacancies (thermally produced at grain boundaries) [\[126\].](#page-173-10) Like intragranular bubbles, high levels of irradiationinduced re-solution significantly limits this growth (and bubble-induced swelling of the kernel) while stresses in the particle may also limit the equilibrium bubble size. Once intergranular-bubble growth becomes significant causing interconnection of porosity, a path from within the kernel to the buffer is created leading to fission-gas release by a percolation mechanism. This release mechanism can be significant and can reach values from ~20% at 4% FIMA to ~35% at 10% FIMA at 1450 K [\[115\].](#page-173-11)

# **Behavior of chemically active fission products in fuel**

For the behavior of solid fission products one must consider solubility, possible oxidation (as expressed by the Ellingham diagram in Fig. 53 [\[127\]](#page-174-0)) and diffusion. For oxygen potentials expected in HTGR fuel particles, the Rare Earths (RE) are highly soluble being incorporated in the fuel lattice as oxides (REO2 or RE2O3) where they remain stable with the possible exception of Ce (seen to be significantly released at around 1743 K for 4% FIMA fuel [\[103\]](#page-172-10)). With respect to UCO fuel, we note that as the UC2/UO2 ratio increases then so do the mobilities of the REs since their "trapping" in the kernel in oxide form is lessened. Zirconium, Nb and Sr have significant solubility in UO2 (more at high temperature for Zr) and are easy to oxidize (ZrO2, Nb2O3 and SrO). Barium is in the form of low-solubility BaO and can migrate to grain boundaries forming separate complex ternary compounds with Sr, Zr, REs (and small amounts of Cs and Mo, see below) of perovskite structure. This complex phase can only be observed at high temperature and high burnup (it was not observed at 4% FIMA by Minato et al. [\[103\]](#page-172-10) even at high temperature; furthermore, significant Ba release out of the kernel was measured). Tellurium is also of low solubility and is difficult to oxidize; at grain boundaries it forms inter-metallic compounds (e.g., with Pd) and Cs2Te (rarely observed) and is significantly released from the kernel [\[103\]](#page-172-10). Many of the other metallic elements also have rather low solubility and are difficult to oxidize except at high oxygen potentials and, after segregation at grain boundaries, form metallic inclusions. Noble metals (Mo, Ru, Rh, Tc and Pd) constitute the main type of inclusion. Other inclusions of Te, Sn or Pd, Ag, Cd are also observed. The size of inclusions is very temperature dependent [\[103\]](#page-172-10). Pd and Ag have high volatility and are significantly released out of the fuel kernel [\[103\].](#page-172-10) Molybdenum has a complex behavior because its oxidation potential is close to the value corresponding to stoichiometric fuel and a significant amount can be oxidized to MoO2 (limiting increase of fuel stoichiometry), a low solubility oxide. At high temperature Mo can form molybdate compounds with Cs or Ba but even at high temperature (>1673K) these were not observed in [\[103\]](#page-172-10) (but only for 4% FIMA fuel). Cesium also has low solubility and might be oxidized to Cs2O depending on the fuel temperature and oxygen potential. This oxide also has low solubility. Once again, formation of complex ternary phases could be foreseen at high temperature and high burnup [\[151\]](#page-175-0) but were not observed in [\[103\]](#page-172-10) where significant release of Cs from the kernel was observed.

<!-- page 100 -->

![](../_page_99_Figure_0.jpeg)

*Fig. 53. Ellingham diagram for different oxides of fission products (from [\[107\]\)](#page-173-12).*

In the UCO-type fuel kernel, oxygen liberated during the fission process of UO2, first oxidizes the carbide UC2 phase and then the RE fission products because of their high affinity for oxygen (Fig. 54). When the UC2 phase is present in the kernel, the oxygen potential is maintained at a fixed value which is about –700 kJ/mol at 1573 K (Fig. 52). Under these conditions, the results shown in Fig. 54 indicate that those fission product elements with lower affinity for oxygen (Sr, Eu, Zr, Ba) exist as carbide compounds. As the burnup increases, the UC2 phase in the kernel decreases. When UC2 has fully disappeared, the oxygen potential then increases and oxygen is available to form oxide compounds with these fission products. A rather complete investigation of these chemical modifications in the UCO kernel as a function of burn up can be found in [\[109\]](#page-173-13).

<!-- page 101 -->

![](../_page_100_Figure_0.jpeg)

*Fig. 54. Oxidation diagram for carbides of interest (from [\[96\]\)](#page-172-11).* 

#### *10.3.2. Urania (UO2) kernel oxygen potential*

Uranium-atom fissions (i.e., burnup) deplete the uranium content replacing each uranium atom with two fission products that, overall, have a slightly lower affinity for the oxygen of the urania (in particular, a large fraction of the noble gas xenon (~28%) is produced – see Table 13 – which has no affinity for oxygen). Thus, the fuel oxygen potential increases during irradiation and the fuel becomes slightly hyperstoichiometric (excess oxygen), a trend tempered by some of this oxygen reacting with the carbon buffer layer. Different approaches can be used to determine the oxygen potential in TRISO particles:

 tables of fission yields can be used to determine the amount of each fission product element and then calculate the oxygen requirements as metal monoxide (BaO, etc.), sesquioxide (La2O3, etc.) and dioxide (ZrO2, etc.); this approach was used by Minato et al. [\[103\]](#page-172-10) (or in [\[108\]](#page-173-14)) who estimated an oxygen potential in an HTGR particle of 5.5% FIMA burnup at around –400 kJ/mol at 1573 K and –370 kJ/mol at 2000 K (Fig. 55); measure the CO trapped in the buffer layer by crushing a particle at elevated temperature in a mass spectrometer, as performed by Bildstein and Strigl [\[104\]](#page-172-12) for 6% FIMA HTGR, irradiated in the temperature range of 1200-2100 K; Lindemer and de Nordwall [\[90\]](#page-172-2) reviewed these data and derived an interval for the oxygen potential between –500 and –375 kJ/mol in the temperature range of 1200 and 2100 K (Fig. 56). The same values were later deduced by Homan et al. [\[109\];](#page-173-13) analyze microprobe investigations conducted during post-irradiation examination if irradiated HTGR fuel particles to determine chemical speciation that are usually indicators of the oxygen potential range.

<!-- page 102 -->

![](../_page_101_Figure_0.jpeg)

*Fig. 55. Calculated oxygen potentials in HTGR UO2 fuel as a function of burnup and temperature (from [\[103\]\)](#page-172-10).* 

![](../_page_101_Figure_2.jpeg)

*Fig. 56. Calculated oxygen potentials from UO2 pressure measurements for HTGR UO2 fuel (from [\[90\]\)](#page-172-2).* 

These results are fairly consistent with observations for LWR UO2: Matzke showed [\[105\]](#page-172-13) that, for 6% FIMA (equivalent to ~58 GWd/tHM) fuel, between 900 and 1400 K, the oxygen potential was evaluated in the interval between –400 and –500 kJ/mol. At higher burnup (HTGR conditions), recent studies on LWR UO2 [\[106\]](#page-172-14), [\[107\]](#page-173-12) indicate for a burnup of 16% FIMA (equivalent to ~161 GWd/tHM), at 1273 K, the fuel oxygen potential is greater than – 300 kJ/mol. This oxygen potential value is above the threshold for the oxidation of molybdenum (Fig. 57).

<!-- page 103 -->

For such low-enriched LWR fuel, the burnup accumulated after the third irradiation cycle mainly results from the fission of 239Pu which is known to be a more oxidizing process than the fission of 235U. For the HTGR fuel kernel, the uranium fission is assumed to be preponderant during a longer time considering the higher initial enrichment. Consequently it is expected that HTGR UO2 fuel kernels reach these oxygen potential values at higher burnup.

![](../_page_102_Diagram_1.jpeg)

*Fig. 57. Measured oxygen potentials for irradiated LWR and BWR UO2 fuels (Figure from [\[107\]](#page-173-12) and from experimental data in Matzke [\[105\]](#page-172-13) and Walker et al. [\[106\]\)](#page-172-14).* 

# *10.3.3. CO/CO2 formation and particle pressurization*

The result of CO and CO2 formation is internal pressurizing of the particle that increases with burnup and adds to the pressurization from fission gases.

For a burnup of 9% FIMA, at 1450 K, the pressure resulting from fission gases can represent one half of the contribution of CO and CO2 in an HTGR TRISO coated particle (see Fig. 58). At lower burnup (≤ 6 % FIMA), it must be stressed that pressurization of the particle arises principally from fission-gas release from the fuel kernel [\[114\]](#page-173-15), [\[115\]](#page-173-11). The significant role played by the fission gases on the pressurization of the particle has to be tempered by the fact that the total pressure may be lower because some fraction of these noble fission gases may remain trapped within the fuel kernel.

<!-- page 104 -->

![](../_page_103_Figure_0.jpeg)

*Fig. 58. Thermodynamic calculations of the Xe+Kr pressure as a function of burn up at 1450 K and 1873 K [115].* 

Thermodynamic calculations provide an upper bound for oxygen release as given by.

| $O/f < 0.40 \ f_U + 0.85 \ f_{p_U}$ | (10-6) |
|-------------------------------------|--------|
|-------------------------------------|--------|

| $O/f < 0.40 \ f_U + 0.85 \ f_{\text{pu}}$ | (10-6) |
|-------------------------------------------|--------|
|-------------------------------------------|--------|

where, O/f is the atomic oxygen release per fission, fU and fPu are the fractions for uranium and plutonium fissions, respectively.

The observed values are usually lower and can be described by the Proksch correlations [\[113\]](#page-173-16)

| $\text{Log}_{10} [(\text{O}/\text{f})/t^2] = -0.21-8500/\text{T}$ | (10-7) |
|-------------------------------------------------------------------|--------|
|-------------------------------------------------------------------|--------|

| $\text{Log}_{10} [(\text{O}/\text{f})t^2]=-0.21-8500/\text{T}$ | (10-7) |
|----------------------------------------------------------------|--------|
|----------------------------------------------------------------|--------|

where, O/f is the atomic oxygen release per fission, t, the irradiation time (in days) and T, the particle surface temperature (K). This equation is valid for 66< t < 550, 1223 K< T < 1808 K.

The suppression of excessive CO formation during oxidation of a UO2 based particle remains an important design objective at moderate and high burnup. The failure of the SiC layer may happen because of over-pressurization due to CO formation. However, the SiC layer may fail by other mechanisms where CO formation is implied. Corrosion of the SiC layer by CO [\[97\]](#page-172-15), can occur as a result from failure of the IPyC coating caused by irradiation-induced shrinkage [\[98\].](#page-172-16) Carbon monoxide and CO2 pressures are suspected of being partly responsible for the mechanical weakening of the IPyC coating by acting as the vehicle for mass transfer of carbon in presence of a thermal gradient [\[99\],](#page-172-17) [\[100\].](#page-172-18) Uranium oxi-carbide fuel allows a significant reduction of CO and CO2 pressurization, especially at high burnup, in comparison with UO2 particles [\[116\]](#page-173-0).

#### *10.3.4. Silicon carbide corrosion by fission products*

In the typical HTGR TRISO coating design, the silicon carbide layer serves as a critical fission product barrier. Nevertheless, it has been shown experimentally that the silicon carbide layer can be corroded by metallic fission products, in particular, palladium [\[128\].](#page-174-1) It was additionally found that silver [\[129\],](#page-174-2) [\[130\]](#page-174-3) could be transported through intact SiC layers. 

<!-- page 105 -->

These processes tend to limit the fuel life time, especially at high temperature. For this reason, considerable literature exists on the experimental study of interface reactions between metallic fission products and SiC [\[131\],](#page-174-4) [\[132\].](#page-174-5)

For Pd, the reaction with SiC can be qualitatively explained by phase-diagram arguments [\[133\]](#page-174-6) (the Si-C-Pd system was experimentally investigated [\[134\]](#page-174-7) and recently modeled by [\[135\]\)](#page-174-8). To prevent corrosion by Pd, new combinations of coating layers were proposed with success in [\[136\]](#page-174-9). The idea was to introduce a sacrificial layer inside the SiC coating able to retain the offending fission products. An alternative approach consists of replacing the SiC coating by a ZrC layer. Review and evaluation of the ZrC coating for HTGR fuel particles has been performed [\[137\]](#page-174-10), [\[138\]](#page-174-11). In particular, experimental observations [\[139\],](#page-174-12) [\[140\]](#page-174-13) showed neither Pd attack nor thermal degradation of ZrC up to 1600°C. Zirconium carbide was also shown to have a high capacity to retain cesium [\[141\]](#page-174-14); however, Ru retention was not as good as for SiC. At higher temperatures, the deterioration of the ZrC particle is caused by failure of the IPyC [\[142\].](#page-174-15) The development of TRISO-coated particles with a ZrC-coating must be viewed as at an early stage compared to the development of the SiC-coated design for which many experiments have been performed.

Silver release has been observed [\[129\]](#page-174-2), [\[130\]](#page-174-3) from undamaged particles suggesting that Ag migrates through intact SiC layers at temperatures >1100°C. Today, the Ag migration mechanism remains not fully understood. A review of the possible explanations for this process is available [\[143\]](#page-174-16). In many situations of the past, Ag release was modeled as a diffusive mechanism since measurements of silver release exhibited temperature dependence. It seems that recent experimental results do not support this mechanism. McLean et al. [\[143\]](#page-174-16) showed that, if grain-boundary diffusion is assumed, the expected value of the diffusion coefficient in SiC is inconsistent with the value derived from Ag release measurements. Nabielek et al. [\[129\]](#page-174-2) speculate that Ag migration is due to the presence of free silicon at the grain boundaries. Recent experimental studies [\[143\],](#page-174-16) [\[144\]](#page-174-17) indicate that Ag migration by diffusion (intergranular or intragranular) does not occur up to 1300°C and alternative explanations are proposed.

Once cesium has migrated into the buffer, it can react with carbon [145]. The question of the stability of the CnCs compounds at temperatures higher than 1100 K is an important concern. At nominal temperatures, cesium may be released and associated with carbon of the buffer layer to form compounds. These compounds, if they are not stable with increasing temperatures, may become a potential source of cesium release. The thermodynamic properties of these compounds, CnCs (n=8,10,24,36,48,60), can be derived from vapor pressures measured in the temperature range between 670 and 1070 K [\[147\],](#page-174-18) [\[148\]](#page-175-1). There are no data at higher temperatures as mentioned in different reviews [\[149\]](#page-175-2), [\[150\].](#page-175-3) It was only shown that cesium-graphite compounds are not stable at 923 K under vacuum and decompose to give cesium vapor and graphite [\[151\]](#page-175-0). A method was developed [\[152\]](#page-175-4) for estimating the conditions under which graphite reacts with cesium in HTGR conditions (high temperatures and low cesium pressures) to form compounds.

# **10.4. Some trends in accident conditions**

Accident scenarios and conditions are presented in [16] along with some experimental results on oxidation of coatings (inducing particle failure) and fission product release. Severe accident scenarios involving air or water ingress, after sufficient erosion of the graphite fuel compact, could have a dramatic effect on failed particles (already-failed or oxidized during the accident) by allowing contact between the kernel and an air-helium, steam-helium or air

<!-- page 106 -->

steam-helium mixture. This situation is not unique to HTGR accidents as similar situations are possible in LWRs where extensive knowledge exists. Such situations are considered beyond the scope of the present book and the reader is referred to [16], [\[146\]](#page-174-19). For a loss-offorced-circulation accident scenario (also called a "core conduction heatup" accident), a rapid depressurization occurs along with a flow coast down and reactor scram. The depressurization coolant is helium with no air ingress. The primary consequence of this accident is heating-up of the fuel beyond nominal conditions (about 1250°C) where modern core designs aim to limit the peak fuel temperatures to 1600°C. The principal result as far as the fuel is concerned is an enhanced release of fission products from the UO2 kernel into (and through) the coating layers. For example, half or more of the inventories of the fission gases, I, Cs, Te and Pd could be released from the kernel. This is important in two aspects: one, increased release from the small number of defective and failed particles and, secondly, possible corrosion with SiC layer. Most fission products will still be retained by intact coatings.

