---
source_pdf: spouted-bed-design-considerations.pdf
pages: 10
converter: pdf2md.py (pdfplumber + pdftotext)
note: lossy conversion — verify quantities and equations against the PDF
---


<!-- page 1 -->

INL/CON-15-36799
PREPRINT
SPOUTED BED DESIGN
CONSIDERATIONS FOR
COATED NUCLEAR
FUEL PARTICLES
Fluidization XV
Douglas W. Marshall
July 2017
This is a preprint of a paper intended for publication in a journal or
proceedings. Since changes may be made before publication, this
preprint should not be cited or reproduced without permission of the
author. This document was prepared as an account of work
sponsored by an agency of the United States Government. Neither
the United States Government nor any agency thereof, or any of
their employees, makes any warranty, expressed or implied, or
assumes any legal liability or responsibility for any third party’s use,
or the results of such use, of any information, apparatus, product or
process disclosed in this report, or represents that its use by such
third party would not infringe privately owned rights. The views
expressed in this paper are not necessarily those of the United
States Government or the sponsoring agency.

*[figure(s) on p.1 → figures/spouted-bed-design-considerations-p01.png]*


<!-- page 2 -->

SPOUTED BED DESIGN CONSIDERATIONS FOR COATED
NUCLEAR FUEL PARTICLES
Douglas W. Marshall, Fuel Design and Development Engineer,
Battelle Energy Alliance, LLC, Idaho Nuclear Laboratory
P.O. Box 1625, Idaho Falls, Idaho, USA 83415-3855
Email: douglas.marshall@inl.gov
Phone: +1 (208) 526-3657
Fax: +1 (208) 526-2930
Abstract:
High Temperature Gas Cooled Reactors (HTGRs) are fueled with tristructural
isotropic (TRISO) coated nuclear fuel particles embedded in a carbon-graphite fuel
body. The TRISO coatings consist of four layers of pyrolytic carbon and silicon
carbide that are applied on uranium ceramic fuel kernels by chemical vapor
deposition in a spouted bed reactor. The TRISO coatings are the primary
containment structure for radionuclides in the HTGR reactor and must have very high
integrity and uniformity.
The four TRISO coatings are deposited in a concatenated series of batch operations
at temperatures ranging from 1230°C to 1550°C. As the coatings are deposited, the
mean particle diameter doubles, bed volume increases 8-fold, and particle envelope
density drops from 11 g/cm3 to 3 g/cm3.
All depositions are accomplished without the aid of sight ports or internal
instrumentation that could compromise the integrity of the layers.
The converging section and gas injection nozzle were designed to prevent bed
stagnation zones and premature decomposition of reactive coating gases. The
equipment designs and operating methods have yielded very good equipment
reliability and product reproducibility.
Background Information
Nuclear reactor designs for High Temperature Gas-Cooled Reactors (HTGRs)
employ small kernels of uranium ceramic (425µm - 500µm diameter) that are
hermetically sealed in four shells of pyrolytic carbon and silicon carbide and
dispersed in a matrix of graphite and vitreous carbon. The layers in the tristructural
isotropic (TRISO) particle constitute the primary containment for highly-radioactive
fission products and must be deposited in a manner that ensures chemical purity,
mechanical integrity, and narrowly distributed layer thicknesses, densities, grain
sizes, and orientation of graphene planes (dense pyrocarbon layers only).

<!-- page 3 -->

Each layer has important functions; Keeley (1). The inner most layer (1 in Figure 1)
is a 100 µm buffer layer of low-density pyrolytic carbon (pyrocarbon) that absorbs the
recoil energies from atomic fragments after a fission event and provides a volume for
accumulating gaseous fission products, thus avoiding excessive internal pressures
that could induce fractures in the outer three layers.
The second layer (2) is the dense inner pyrocarbon layer (IPyC, ~40µm), which
provides a gas-tight seal to protect the fuel kernel during coating and the silicon
carbide (SiC) layer from carbon monoxide and metallic fission products during
irradiation.
The penultimate layer (3) is composed of SiC (~35µm) and serves as the structural
member and a barrier to metallic fission product diffusion.
The outer layer (4) is the dense outer pyrocarbon layer (OPyC, ~40 µm) that protects
the silicon carbide from mechanical damage during handling and is the final barrier to
fission product diffusion.
Both dense pyrocarbon layers shrink during
irradiation and take some of the tensile load
from the SiC layer. The outer three layers
constitute the primary containment structure
1
against fission product migration into the
graphitic fuel bodies and the helium cooling 2
system.
3
Each nuclear reactor may contain billions of 4
TRISO particles embedded in the fuel form,
so high integrity TRISO coating layers are
essential to keep fission product releases at
acceptable levels during normal operations
and during postulated accident scenarios
involving the loss of helium coolant flow. By
Figure 1. Sectioned TRISO fuel particle.
design, the peak centerline core
temperatures, during postulated accident
scenarios, safely remain 200 – 300°C below fuel fabrication temperatures, so
minimal damage occurs to the fuel form.
The need for energy from safe, high-temperature, and low-carbon emitting sources
to replace fossil fuels has stimulated a renewed, worldwide interest in HTGR
technology for process heat, high-temperature hydrogen production processes, and
co-generation of electricity.
Design Challenges
Constraints
Multiple and often competing performance objectives and constraints must be
considered during the design of chemical vapor deposition (CVD) reactors for the
production of TRISO coated nuclear fuels; some of which are unique to the nuclear
industry. For instance, to prevent an unplanned, uncontrolled nuclear criticality in the

*[figure(s) on p.3 → figures/spouted-bed-design-considerations-p03.png]*


<!-- page 4 -->

fuel fabrication equipment, fissile material enrichment and mass, equipment
geometry, and neutron moderation are constrained within safe limits to provide
multiple, independent defenses “in depth.” Equipment designed for depositing
TRISO coating layers of low-enriched uranium (LEU) kernels have had retort
diameters up to 24 cm; Noren (2), Kasten (3). The system design discussed in this
paper is housed in a facility licensed for highly-enriched uranium (HEU) and is
constrained to an internal diameter of 15.2 cm to ensure criticality safety should HEU
be used inadvertently.
The relatively small retort diameter, required to ensure the system is critically safe by
geometry, introduces more design caveats. The first caveat relates to matching of
the Glicksman dimensionless scaling relationships; Glicksman (4). Having similar
superficial gas velocities and gas residence times would be preferred, but not
possible. Gas flow rates were established in lab-scale equipment to achieve the
desired linear deposition rate for each layer and to ensure fluidization as particle
dimensions change. The linear rate of deposition is controlled because it influences
the layer isotropy, grain size, and density. Isotropy is essential to promote uniform
pyrocarbon shrinkage to preclude excessive stress accumulation in the layers;
Jellison (5).
At constant linear deposition rates, the volumetric gas flow rates are proportional to
the bed mass, which is proportional to the cube of the retort diameter. The
superficial gas velocity is a function of volumetric flow and the retort cross sectional
area, so it increases proportionally to the retort diameter. Gas residence time
decreases with the increase in gas velocity, which adversely impacts coating
efficiency. Coating efficiency can be improved with a well-designed gas distributor
nozzle that encourages percolation of coating gases through the descending annular
bed.
Secondly, the narrow retort also makes gas distribution important to preclude
accretions forming on the walls. Lifting the bed in the bottom of the retort can
expose the retort wall to condensing species and causing accretions. Equally
important is to avoid direct impingement of reactive coating gases on the retort wall
that would form accretions and impact bed circulation.
A third consideration is the fluidization mode. Bed slugging is avoided and bed
circulation is enhanced by maintaining a relatively shallow bed and intentionally
operating the coater in a spouting bed mode. The uranium ceramic fuel kernels have
narrowly distributed particle diameter of either 425µm or 500µm and particle
envelope densities near 11 g/cm3. The final products, after the TRISO coating layers
are applied, are 860 – 950 µm in diameter with particle densities near 3 g/cm3. The
particles roughly double in both mass and diameter during the coating process and
the bed expands to approximately eight times the original volume. These changes
happen too quickly, during pyrocarbon deposition, to allow the bed to operate in
steady state conditions. An example of the dimensional changes is given in Table 1.

<!-- page 5 -->

Table 1. Nominal TRISO particle layer dimensions with a 425 µm kernel.
Layer Layer Particle Particle Δ
Relative Relative
Material Thickness Density Diameter Density Time
Mass Volume
(µm) (g/cm3) (µm) (g/cm3) (min)
Kernel --- --- 425 11.1 1.00 1.00 ---
Buffer 100 1.00 625 4.18 1.20 3.18 5
IPyC 40 1.90 705 3.49 1.43 4.56 12
Silicon
35 3.20 775 3.42 1.87 6.06 100
carbide
OPyC 40 1.90 855 3.03 2.22 8.14 13
The TRISO coating furnace retorts are fabricated from purified, nuclear grade,
graphite to prevent chemical contamination of the coating layers that would
compromise layer integrity and fission product retention during irradiation. Transition
metal contaminants can form molten carbide phases that can migrate along thermal
gradients to create pathways for carbon monoxide and fission product escape
through the pyrocarbon that can corrode the SiC layer; Minato (6), Tiegs (7).
Instrument penetrations through the graphite retort wall are precluded because they
are problematic to seal, may trap partially coated particles, and refractory instrument
sheaths are susceptible to breakage. The radial position of thermocouples hung
from the top of the coater cannot be controlled or maintained. The radial
temperature profile within the coater, due to the influx of cool carrier gases and the
exothermicity of coating gases, makes futile any attempt to use an internal
thermocouple for process monitoring or control. Another concern is that nascent
coating layers may be cracked or broken when a spouted particle impinges on the an
instrument probe.
An opaque, black smoke is generated during the deposition of the pyrocarbon layers
that prevents the use of optical pyrometers for direct bed temperature monitoring or
any visual observation of bed dynamics. In consideration of the limitations on
instrumentation, the coating depositions are accomplished without internal
instrumentation.

**Table (p.5) — auto-extracted, verify against PDF:**

| Material | Layer Thickness (µm) | Layer Density (g/cm3) | Particle Diameter (µm) | Particle Density (g/cm3) | Relative Mass | Relative Volume | Δ Time (min) |
|---|---|---|---|---|---|---|---|
| Kernel | --- | --- | 425 | 11.1 | 1.00 | 1.00 | --- |
| Buffer | 100 | 1.00 | 625 | 4.18 | 1.20 | 3.18 | 5 |
| IPyC | 40 | 1.90 | 705 | 3.49 | 1.43 | 4.56 | 12 |
| Silicon carbide | 35 | 3.20 | 775 | 3.42 | 1.87 | 6.06 | 100 |
| OPyC | 40 | 1.90 | 855 | 3.03 | 2.22 | 8.14 | 13 |


<!-- page 6 -->

The TRISO coater retorts are externally
heated and the temperature is
controlled by external thermocouples
set off from the retort wall by a few
millimeters. The ratio of retort wall
surface area to the volumetric gas flow
rate decreases with increasing retort
diameter and bed mass. The net result
is that process temperature setpoints
established in a laboratory-scale
coating furnace are inaccurate for larger
diameter furnaces and additional
process development is often needed to
achieve the desired coating layer
material properties.
The particle and fluidizing gas
properties are such that the entire
coating process falls outside of the
region mapped for spouted beds
(Figure 2); Grace (8), Kunii (9). High
process temperatures (approximately
1230°C to 1550°C) and small particle
diameters decrease the dimensionless
particle diameter and dimensionless
gas velocity during coating.
Figure 1. Mapped T∗RISO la ⅓ yer start and
𝑑𝑑𝑝𝑝 =𝑁𝑁𝐴𝐴𝐴𝐴
Stable (coherent) spouting is not end points for each layer.
achieved, but the bed fluidizes in a
pulsatory spouted bed mode; Epstein (10), Pianarosa (11). Pulsatory spouting was
verified by sensing pressure fluctuations transmitted upstream through the gas inlet
and by modelling conditions with CPFD Barracuda VR® software.
Spouting is achieved with a mixture of argon and hydrogen when silicon carbide is
deposited and argon and organic precursors (propene and/or ethyne) for deposition
of the pyrocarbons.
As one might anticipate, published correlations for minimum spouting velocities,
which were developed under less extreme conditions, do not yield reliable estimates
of the minimum spouting velocity for the TRISO coating conditions.
Gas Injector
The gas injector nozzle was designed to resist excessive accretion formation at the
orifice(s) by precluding premature decomposition of precursor gases and shielding
the nozzle surface with inert gases. Furthermore, the nozzle configuration diffuses
the gas jet to prevent bed stagnation zones while precluding direct impingement of
coating gases on the retort wall. Laboratory testing has demonstrated that product
uniformity was improved using a gas distributor nozzle in preference to the single
gas inlet commonly used in spouted beds; Noren (2), Kasten (3), Lackey (12).
Moreover, a single gas orifice in a 5-cm conical-cylindrical coater, formed volcano-
⅓
2
∗
��𝑔𝑔∙�𝑔𝑔𝜌𝜌−
𝑝𝑝𝜌𝜌�∙𝜇𝜇�/𝑔𝑔𝜌𝜌�𝑈𝑈=
𝑈𝑈

*[figure(s) on p.6 → figures/spouted-bed-design-considerations-p06.png]*


<!-- page 7 -->

shaped accretions around the inlet that trapped fuel particles between the accretion
vent and the retort wall.
Design objectives were met using a domed
gas distributor nozzle with multiple gas inlet
orifices and a serrated flange (Figure 3).
The orifice sizes were selected to ensure
sufficient gas velocity to prevent particle
weeping and sufficient back pressure to
ensure balanced gas distribution and prevent
instantaneous gas flow reversals in individual
orifices.
The serrated flange engages a conical port in
the bottom of the retort converging section.
The serrations reduce heat conduction from
the retort by limiting the contact area and
ensure sufficient off set to form an annular
orifice between the base of the dome and the
Figure 2. Graphite gas distributor
converging section through which an inert gas
nozzle.
is passed. The inert gas fluidizes particles in
the bottom of the bed, convects heat away from the nozzle, displaces reactive gases
away from the nozzle face, and dilutes the precursor gases to the desired
concentration within the bed.
Although orifice accretions were not entirely eliminated, all orifices remain open for
the duration of the coating depositions and none of the accretions trap fuel particles.
Each distributor nozzle is a single use component that is replaced after each fuel
coating run.
Converging Section
The converging section of a spouted bed encourages bed circulation by eliminating
regions that would be stagnant in a cylindrical configuration. Common spouted bed
designs have conical converging sections with included cone angles ranging from
45° to 60°. While many factors may be considered in the choice of the cone angle,
the driving factors for nuclear fuel coating are maintaining particle sphericity and
achieving a narrow distribution in coating properties.
When a narrow cone angle (~45°) is employed, the injected gases may lift the entire
bed away from the vessel bottom; causing localized slugging and possibly exposing
the walls to the reactive coating gases. A narrow converging section, however, does
promote more bulk-flow behavior in an annular bed of spherical particles and less
drag on bed movement along the walls. When the cone angle is wide (~60°), the
spout is more easily stabilized and bed depth is more shallow, but bed circulation
along the walls is impaired and some localized bed stagnation may occur, especially
with spherical particles, which readily exhibit funnel-flow behavior in a spouted bed.
Any bed stagnation or impairment of circulation leads is undesirable.

*[figure(s) on p.7 → figures/spouted-bed-design-considerations-p07.png]*


<!-- page 8 -->

Designs of some bubbling and spouted beds incorporate narrow included cone
angles at the top of the converging section and transition step-wise to broader angles
at the bottom; Epstein (10), Flamm (13), Uhlemann (14). Stepped changes in the
cone angles can adversely impact bed circulation where the conical frusta meet. A
gradual transition in the slope is deemed preferable. Whereas TRISO coating
furnace retorts have diameters generally less than 24cm and are lathed from
graphite billet, the converging section profile is not constrained by economics to
conical geometries, as might a larger metal vessel.
The objectives of encouraging spout
stability with a broad cone-angle base and
facilitating good bed circulation without
exposing the converging section walls to
reactive coating gases or risking bed
stagnation zones were met by designing a
curvilinear converging section with a
continuously variable slope, (Figure 4);
Marshall (15). The local slope at the
intersection with the cylindrical section
equates to an included angle of 22° and
approximately 116° at the base.
Inspections of the converging section and
gas injection nozzle after each coating run
show no evidence of bed stagnation zones
or significant accretions. Metallographic
mounts of the TRISO coated particles
reveal that the variability in coating
Figure 3. Rendered cross-section of a
thickness is low and that particle sphericity
curvilinear converging section.
is acceptable.
Carbonaceous “soot” accumulates above the fountain and on the wall of the
cylindrical section during the deposition of the carbon buffer layer. Ejecta from the
particle bed will, occasionally, impact the soot and take a loosely adherent soot layer
back into the bed where it becomes
encapsulated within the layer being
deposited. These soot inclusions
(Figure 5) are undesirable as they
interfere with physical properties and
function of the layers. Although
frequently observed in mounted TRISO
particles coated in a laboratory-scale
(5-cm) conical-cylindrical spouted bed
with a single gas inlet port at the cone
apex, soot inclusions are infrequently
observed in product from the 15-cm
coater with the curvilinear converging
section and multiport gas distributor Figure 4. Soot inclusion within the SiC layer.
nozzle.

*[figure(s) on p.8 → figures/spouted-bed-design-considerations-p08.png]*


<!-- page 9 -->

Dual Gas Paths
The coater is designed with an annular orifice between the base of the converging
section and the outer margin of the gas distributor nozzle. A portion of the inert
diluent gas is routed through the annular orifice to fluidize fuel particles below the
elevation of the orifice ports on the distributor nozzle, to cool the nozzle, and to limit
accretion formation by displacing reactive coating gases near the nozzle face.
Laboratory tests were conducted in a 2-D physical model of the 15-cm coater using
similar geometries. The tests showed that diverting a portion of the inert diluent gas
to the annular orifice widens the spout diameter and decreases the height of the
spouted bed fountain. Diversion of some inert gas to the annular orifice in concert
with the converging section and multiport nozzle configurations and the larger retort
diameter are thought to be the contributing factors in reducing the incidence of soot
inclusions in the product.
Conclusions
Design and scale up of a TRISO coating retort requires careful consideration of
several competing design parameters and a measure of creativity in order to achieve
high quality coatings on nuclear fuel kernels. Fully developed bed circulation must
be assured without excessive fluidization that could result in soot inclusions or
abrade the layers.
The design objectives were met by incorporating a multi-orifice distributor nozzle,
diverting a portion of the inert gases through an annular orifice at the base of the
coater, and using a curvilinear converging section. High quality TRISO coated fuel
particles with narrowly distributed layer properties, infrequent indication of soot
inclusions, and no observed evidence that bed stagnation has occurred suggest a
successful design has been achieved.
This coating furnace design is in use by the Advanced Gas Reactor Fuel
Development and Qualification program funded by the United States Department of
Energy.
Nomenclature
d particle diameter
p
d * dimensionless particle diameter
p
g gravitational constant
N Archimedes number
Ar
U superficial gas velocity
U* dimensionless superficial gas velocity
µ gas viscosity
ρ gas density
g
ρ particle envelope density
p

<!-- page 10 -->

References
1. Keeley, J. T., et al., “Development of a Continuous CVD Process for TRISO
Coating of AGR Fuel,” Proceedings of the 4th International Meeting on High
Temperature Reactor Technology (2008), Washington D. C., HTR2008-58008.
2. Noren, R. C., and R. Develasco, “Evolution of Coating Gas Distributors,” PC-
000345, General Atomics, August 1992.
3. Kasten, P. R., J. H. Coobs, and A. L. Lotts, “Gas-Cooled Reactor Programs
Annual Progress Report for Period Ending December 31, 1973,” ORNL-4975,
Oak Ridge National Laboratory, April 1976.
4. Glicksman, L. R., M. Hyre, and K. Woloshun, “Simplified Scaling Relationships
for Fluidized Beds,” Powder Technology, 77, 177 – 199.
5. Jellison, G. E., Jr., J. D. Hunn, “Optical Anisotropy Measurement of TRISO
Nuclear Fuel Partice Cross-Sections: The Method,” J. of Nuclear Materials, 392,
January 2008, 36-44.
6. Minato, K. et al., “Carbon Monoxide – Silicon Carbide Interaction in HTGR Fuel
Particles,” J. of Material Science, 26, Issue 9 (May 1972), 2379-2388.
7. Tiegs, T. N., “Fission Product Pd-SiC Interaction in Irradiated Coated-Particle
Fuels,” Nuclear Technology, 57, No. 3 (June, 1982), 389-398.
8. Grace, J. D., “Contacting modes and behaviour classification of gas—solid and
other two-phase suspensions,” CJChE 64 (1986), 3, 353 – 363.
9. Kunii, D. and O. Levenspiel, Fluidization Engineering, Second Edition,
Butterworth – Heinemann, 1991.
10. Epstein, N. and J. Grace (editors), Spouted and Spout-Fluid Beds –
Fundamentals and Applications, Cambridge University Press, 2011.
11. Pianarosa, D. L., L. A. P. Freitas, C. J. Lim, et al., “Voidage and Particle Velocity
Profiles in a Spout-Fluid Bed,” The Canadian Journal of Chemical Engineering,
Vol. 78, Feb. 2000. pp 132-142.
12. Lackey, W. J., D. P. Stinton, and J. D. Sease, “Improved Gas Distrubitor for
Coating High-Temperature Gas-Cooled Reactor Fuel Particles,” Nuclear Tech.,
35 (1997), 227-237.
13. Flamm, H. J., “Fluidized bed apparatus,” US Patent 3,566,830, 2 March 1971.
14. Uhlemann, H., J. Schmoll, M. Bucheler, “Apparatus for Continuous fluidized bed
agglomeration,” US Patent 5,480,617, 2 January 1996.
15. Marshall, D. W., “Methods of forming a fluidized bed of circulating particles,” US
Patent 7,947,326, May 24, 2011