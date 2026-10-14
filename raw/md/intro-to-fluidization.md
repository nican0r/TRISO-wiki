---
source_pdf: intro-to-fluidization.pdf
pages: 9
converter: pdf2md.py (pdfplumber + pdftotext)
note: lossy conversion — verify quantities and equations against the PDF
---


<!-- page 1 -->

Back to Basics
Introduction to
Fluidization
Ray Cocco Fluidized beds offer excellent heat transfer,
S. B. Reddy Karri
and have the unique ability to move
Ted Knowlton
Particulate Solid a wide range of solid particles in a fluid-like fashion.
Research, Inc. (PSRI)
This article explains the basics of fluidization theory
and outlines how to design a typical fluidized bed.
Fluidized-bed processes have operated commercially ten times greater than that in a packed-bed reactor. Moving
since the 1920s, beginning with the advent of the particles, especially small particles, can transport heat much
Winkler coal gasifier in Germany. Fluidized catalytic more efficiently than gas alone. Even for the most extreme
cracking units (FCCUs) for the production of high-octane exothermic reactions, a fluidized bed can maintain an iso-
gasoline and fluidized-bed reactors for making phthalic thermal profile within a few degrees.
anhydride debuted in the 1940s. Today, about three-quarters The acrylonitrile process, for example, capitalizes on
of all polyolefins are made by a fluidized-bed process. this benefit. The reaction of propylene with ammonia and
The development of a specialized zeolite catalyst for oxygen has an exothermic heat of reaction on the order of
cracking heavy oil into various fractions enabled the com- 515 kJ/mol and the product is prone to thermal degradation.
mercialization of the FCC circulating fluidized bed. In this Yet, acrylonitrile can be made in a fluidized bed with less
process, oil is injected into a riser, and the feedstock and than 5°C of variability in the reactor temperature.
catalyst flow upward. As the oil is cracked, a layer of coke Another benefit of fluidized beds is the ability to move
(a high-molecular-weight carbonaceous material) builds solids in a fluid-like fashion. Catalyst can be added or
up on the catalyst, deactivating the catalyst in a matter of removed from the reactor without requiring a shutdown.
seconds. The coke is removed and the catalyst reactivated in Furthermore, in many cases, the entire inventory of catalyst
a fluidized-bed regenerator. can be removed and replaced in less than a day — whereas it
Fluidized beds typically are more complex to design, would take many days or weeks to uniformly fill a packed-
build, and operate than other types of reactors, such as bed reactor with fresh catalyst. In addition, reactors can be
packed-bed and stirred-tank reactors. Scaleup of fluidized coupled such that the catalyst can be cycled and regenerated;
beds can be difficult (1). Fluidized beds are prone to erosion the FCC circulating fluidized-bed reactor is based on this
and particle attrition caused by the moving particles. Solids advantage.
losses can result in significant operating costs, especially Thus, the benefits of using fluidized-bed technology can
when the solid particles are an expensive catalyst. Bubbles easily outweigh the disadvantages, especially for processes
also need to be managed, as large bubbles can travel faster requiring catalyst circulation or superior heat transfer or
than smaller bubbles in a fluidized bed, which reduces the both. Reaping these benefits, however, requires a good
mass transfer between phases. understanding of fluidization.
Despite these challenges, fluidized beds offer three
distinct advantages over other process technologies: superior Fluidization theory
heat transfer, the ability to easily move solids like a fluid, Particles become fluidized when an upward-flowing gas
and the ability to process materials with a wide particle size imposes a high enough drag force to overcome the down-
distribution. ward force of gravity. The drag force is the frictional force
The heat-transfer rate in a fluidized bed can be five to imposed by the gas on the particle; the particle imposes an
Copyright © 2014 American Institute of Chemical Engineers (AIChE) CEP November 2014 www.aiche.org/cep 21

<!-- page 2 -->

Back to Basics
equal and opposite drag force on the gas. Thus, as a particle
becomes more fluidized, it affects the local gas velocity
around it due to these drag forces. This effect is minimal
for spherical particles, but the influence of the drag force is
more significant for irregularly shaped particles.
Figure 1 shows the increase in pressure drop with
increasing superficial gas velocity through a bed of par-
ticles that is initially packed. As the superficial gas veloc-
ity increases, the pressure drop across the bed increases in
accordance with the Ergun equation (2). When the gas veloc-
ity is high enough that the drag force on the particles equals
the weight of the particles (i.e., m×g), the bed becomes flu-
idized. This point is commonly referred to as the minimum
fluidization velocity, u . Higher gas velocities do not create
mf
higher pressure drop, because at this point the pressure drop
is due solely to the weight of the suspended bed. Thus, the
inventory of any fluidized bed can be determined by measur-
ing the pressure drop across the bed and calculating the bed
height (3):
Δ
where ΔP is the pressure drop across the bed, H is the
bed bed
height of the bed when fluidized, g is the acceleration due
to gravity, g is the force-weight conversion factor, ρ is the
c p
particle density, ε is the bed voidage (i.e., gas volume frac-
tion), ρ is the gas density, and ρ is the bulk density. The
g bulk
gas density is minimal compared to the bulk density and can
be disregarded in Eq. 1.
The minimum fluidization velocity, u , can be estimated
mf
for spherical particles by first calculating the Archimedes
number, Ar:
where d is the Sauter mean particle size and μ is the fluid
p
viscosity. The Wen and Yu equation (4) is a second-order
Superficial Gas Velocity (u)
o
p Figure 1. This typical minimum fluidization curve shows that the
pressure drop (red line) increases with superficial gas velocity until the
point at which the gas velocity is high enough that the drag force is equal
to the weight of the particle. At this point, the minimum fluidization velocity,
the bed becomes fluidized, and the bed height (blue line) increases.
22 www.aiche.org/cep November 2014 CEP
)L/P∆(
porD
erusserP
)
H(
thgieH
deB
deb
u
mf

polynomial with respect to the particle Reynolds number
calculated at the minimum fluidization velocity, Re :
p,mf
After calculating the Archimedes number, the Reynolds
number can be determined using the quadratic equation or
an equation solver.
Finally, the minimum fluidization velocity, u , can be
mf
determined after solving for Re :
p,mf
Other minimum fluidization correlations exist, but
Eq. 3, based on the work of Wen and Yu (4), is the most
popular.
When the gas velocities increase beyond the minimum
fluidization velocity, bubbles can form. The point at which
this occurs depends on the particle size and density. Smaller
or lighter particles tend to experience smooth fluidization
before bubbles appear. Larger or denser particles tend to start
bubbling at the point of minimum fluidization.
The movement of a gas through a fluidized bed can best
be described using the two-phase theory (5). According to
this theory, gas moves through the bed in two ways — as
bubbles, and as part of an emulsion (or dense) phase — as
illustrated in Figure 2. The two-phase theory is represented
by the equation:
where Q is the total gas volumetric flowrate through the
bed
bed, Q is the gas volumetric flowrate through the
emulsion
dense phase, Q is the gas volumetric flowrate through
bubbles
the bubbles, A is the cross-sectional area of the bed, and
bed
u is the superficial gas velocity.
o
Up to the minimum fluidization point, all the gas
moves through the bed via the emulsion phase. Beyond the
minimum fluidization point, any additional gas introduced
should travel through the bed as bubbles. Thus, bubbles can
be considered as the gas bypassing the process, which is det-
rimental for mass-transfer-limited processes, such as some
heterogeneous reactions. Larger bubbles travel faster than
smaller bubbles, so managing bubble size is an important
design criterion.
In reality, Eq. 5 is not completely correct. First, small
t Figure 2. According to the theory
of two-phase fluidization, gas moves
Q Q through the particle bed as bubbles
emulsion bubbles
and as an emulsion (or dense phase).
Copyright © 2014 American Institute of Chemical Engineers (AIChE)

*[figure(s) on p.2 → figures/intro-to-fluidization-p02.png]*


<!-- page 3 -->

particles can experience smooth fluidization before bubbles
form (i.e., the region between the minimum fluidization and
minimum bubbling velocities). Second, a small amount of
gas leaks into and out of the bubbles. Thus, a more accurate
version of Eq. 5 is:
where u is the minimum bubbling velocity for the onset
mb
of bubbles in the bed and Y is the fraction of the gas in the
bubbles (which ranges from 0 to 1).
As the gas velocity through the bed continues to
increase, the type of fluidization changes, as shown in
Figure 3. The bed transitions from a bubbling fluidized bed
to a turbulent fluidized bed in which the gas voids are no
longer regularly shaped bubbles, but rather have elongated
shapes. The top of the bed becomes less well defined due
to the increase in entrained particles. At even higher gas
velocities, all of the particles are entrained out of the bed.
This type of fluidization is called fast fluidization. Further
increases in the superficial gas velocity result in complete
conveying of all of the particles.
With such variations in bed hydrodynamics based on
particle properties, it would seem tedious to predict particle
behavior in a fluidized bed. However, Geldart (6) provides
convenient criteria for predicting the fluidization behavior
based on the Sauter mean particle size, d , and the particle
p
density. Based on these parameters, particles are classified
into four groups: Geldart Groups A, B, C, and D, as depicted
in Figure 4. (Note that Figure 4 applies only at ambient
temperatures and pressures.)
Geldart Group A. Particles in the Geldart Group A tend
to be aeratable and fluidize well. Indeed, most particles used
in fluidized beds are Group A powders, mainly because they
can be easily made by spray drying.
Group A particle sizes range from 30 μm to 125 μm, and
particle densities are on the order of 1,500 kg/m3. Typically,
Group A powders do not promote maximum bubble sizes
larger than 20 cm (7). At low gas velocities, Group A pow-
ders exhibit significant bed expansion without the forma-
Packed Smooth Turbulent
Bed Fluidization Fluidization Conveying
Increasing Gas Velocity
Minimum Bubbling Fast
Fluidization Fluidization Fluidization
p Figure 3. As the gas velocity through the bed increases, the type of
fluidization shifts.
Copyright © 2014 American Institute of Chemical Engineers (AIChE)

tion of bubbles (i.e., smooth fluidization). At high pressure,
Group A powders can experience bed expansions of 100%
or more. If a fluidized bed is not designed for this type of
expansion, it could lose most of its mass to downstream
equipment.
The zeolite-based catalysts used in FCC units fall into
the Geldart Group A classification. Other fluidized beds,
such as catalytic oxidation, oxychlorination, and acrylo-
nitrile processes, also employ catalysts that have a Group A
behavior. Most particles used in fluidized beds are Geldart
Group A powders.
Geldart Group B. These particles have a particle size
range of 150 μm to 1,000 μm. Group B particles tend not to
undergo smooth fluidization, and bubbles form at the onset
of fluidization. Thus, the minimum fluidization velocity
and the minimum bubbling velocity are similar. Group B
powders fluidize easily and are used in a wide range of fluid-
ized unit operations with few difficulties. Most fluidized-
bed combustors and fluidized-bed pyrolysis units use coal
powders with Group B characteristics.
Slugging occurs when the walls of the fluidized bed
stabilize the bubbles such that the bubbles push the solids
upward in the unit. Group B powders tend to allow the
formation of very large bubbles (on the order of meters in
tall beds), so slugging can occur in even some large units.
Bubble sizes larger than two-thirds the diameter of the bed
can cause slugging.
Geldart Group C. Geldart Group C powders are typi-
cally less than 30 μm and are the most difficult to fluidize.
These particles are considered cohesive, and almost always
experience significant channeling (i.e., the formation of
a channel of fast moving bubbles that bypass most of the
bed) during fluidization. In fact, particles this small tend to
10.0
5.0
2.0
1.0
0.5
0.2
10 20 50 100 200 500 1000 2000
d, μm
p
CEP November 2014 www.aiche.org/cep 23
3mc/g
,ytisneD
diulF
–
ytisneD
elcitraP
Group D
Group B
Spoutable Sand-like
Group A
Aeratable
Group C
Cohesive
p Figure 4. The fluidization behavior of particles can be predicted by the
Sauter mean particle size and the particle density. Particles are classified
into four Geldart groups. Group A particles are typically the easiest to fluid-
ize, while Group C are the most difficult due to their cohesive properties.

*[figure(s) on p.3 → figures/intro-to-fluidization-p03.png]*


<!-- page 4 -->

Back to Basics
behave more as particle clusters than single, independent
particles (8). Nanoparticles fall into this classifi cation.
To limit this effect, Group C powders are usually fluid-
ized with the aid of baffles, microjets, pulsing, and/or
mechanical vibration. Sometimes larger particles, such
as Group B powders, are added to the bed to promote
smoother fluidization.
Geldart Group D. The largest particles fall into the
Geldart Group D classification. The gas requirements for
fluidizing Group D powders are large. During fluidization
of Group D powders, the bubbles formed are enormous, and
slugging can be observed even in large fluidized beds. Thus,
these powders are sometimes processed in spouting beds,
which have lower gas requirements than standard fluidized
beds (9). A spouting bed is a type of fluidized bed in which
the gas moves primarily through the center of the bed.
Gas pressure can cause a particle’s classification to
change, which is not captured in the Geldart chart in
Figure 4. Under high pressure, powders of small Group B
particles may behave as Group A powders. Furthermore, the
transition from one group to another is not well defined. In
some cases, the behavior of a powder may fit into more than
one classification. For example, some powders fluidize as
well as a Group A powder, but become permanently defluid-
ized as a Group C powder once at rest (i.e., consolidation).
These powders are sometimes referred to as Group A/C
powders.
Fluidized-bed design
A typical fluidized-bed reactor contains a plenum, a gas
distributor (such as a grid plate or sparger), the particle bed
region, a freeboard region above the particle bed, heating
and cooling coils if needed, and cyclones (Figure 5). Some
Cyclones
Freeboard
Diplegs
Heating/Cooling Coils
Bed
Sparger
Grid Plate with Bubble Caps
Plenum
p Figure 5. A typical fluidized bed has a plenum, a gas distributor,
cyclones and diplegs, and heating/cooling coils. This fluidized bed has a
dual feed system consisting of both a grid plate and a sparger.
24 www.aiche.org/cep November 2014 CEP

fluidized beds may have a dual feed system consisting of a
grid plate with a sparger above it. The acrylonitrile process
uses this configuration, in which air is fed through a plenum
and distributed by a grid plate while ammonia and propylene
are fed through spargers (10). Propylene ammoxidation is
highly exothermic (–515 kJ/mol), so heat is removed from
the reactor by an array of cooling coils located above the
spargers.
Fluidized beds are also used as dryers and heat treaters.
Their design is somewhat different from that of a typi-
cal reactor. The bed heights in fluidized-bed dryers and
heat treaters tend to range from 0.3 m to 0.5 m, whereas
fluidized- bed reactors usually have bed heights on the order
of 1–10 m.
Several constraints need to be considered in the design
of a fluidized bed to ensure reliable operation. The grid plate
and sparger are subject to pressure drop and spacing limits.
Entrainment rates need to be measured or estimated. Also,
cyclones need to be designed for high collection efficiency
and low pressure drop.
Distributors
The primary purpose of a grid plate or a sparger is
to provide good gas distribution. In addition to pressure
drop and spacing considerations, their design also needs
to take into account particle attrition, erosion of the vessel
and internal components, and mechanical constraints (i.e.,
thermal expansion, bed slumping during emergency shut-
downs, etc.).
Many distributor designs are available (Figure 6). Grid
plates can range from simple perforated plates to bubble-
Grids Spargers
Treed
Bubble-Cap Plate
Ringed
Slit-Nozzle or Tent-Grid Plate
Orthogonal
Perforated Plate
p Figure 6. Fluidized beds employ a variety of grid plate and sparger
designs. Grid plates with bubble caps help reduce particle weeping into
the plenum. The most common sparger designs have a treed, ringed, or
orthogonal pattern.
Copyright © 2014 American Institute of Chemical Engineers (AIChE)

*[figure(s) on p.4 → figures/intro-to-fluidization-p04.png]*


<!-- page 5 -->

cap plates. Bubble cap grid plates are designed to minimize                a pressure drop across each orifice above the minimum
particle weeping into the plenum.                                          helps limit particle weeping into the plenum and sparger
      Spargers can be designed with jets that point downward,              manifolds.
upward, or laterally. Spargers have the advantage of being                      For shorter fluidized beds such as dryers and heat treat-
easily engineered to accommodate thermal expansion. Com-                   ers, the recommended pressure drop across the distributor
mon sparger designs have ring, orthogonal, or treed layouts.               is the overall bed pressure drop. These units tend to have
     Grids and spargers can be equipped with shrouds to                    shallow beds, so Eq. 7 should be expressed as:
minimize particle attrition and to better direct the gas                   Δ
(Figure 7).
     Gas (fluid) distribution. The number of orifices and the                   Ideally, the pressure drop across a distributor or grid
diameter of the orifices need to be balanced for good gas                  plate should never be less than 2,500 Pa.
distribution and pressure drop. If the grid pressure drop is                    Particle attrition and erosion. High particle attrition in a
too low, the hydrodynamics of the bed will determine gas                   fluidized bed that is not designed correctly can cause losses
flow and the gas will be poorly distributed. This is because               of tens of millions of dollars per year. To minimize particle
the motion of solids and gas in a fluidized bed is comprised               attrition:
of chaotic swirls and eddies, and such motion could create a                    • use a particle that is designed for such applications
path of least resistance for the incoming gas or fluid. Thus,                   • ensure that high-energy particle collisions in the bed
it is recommended that a fluidized bed with a relatively tall              are kept to a minimum.
bed height (greater than 0.3 m) have a pressure drop across                     Particles in a fluidized bed will experience varying levels
each orifice in the distributor or sparger (ΔPorifice) that is at
least one-third the pressure drop across the bed (11). Thus,
from Eq. 1:                                                                                             Nomenclature
                                                                               Abed         = cross-sectional area of the bed
Δ                                                                              Ar           = Archimedes number
                                                                               dp           = Sauter mean particle size
    The placement and size of the orifices determine where                     Dp,50        = median particle size within each particle size
the gas enters the fluidized bed. If Eq. 7 is not satisfied, then                              distribution
the hydrodynamics of the bed could determine the amount                        g            = acceleration due to gravity
                                                                               gc           = force-weight conversion factor
of gas coming from each orifice. In addition, maintaining                      Hbed         = height of the bed when fluidized
                                                                               mcollected   = total collection rate
                   Grids                         Spargers                      mi           = rate of collection for a particle of diameter i
                                                                               minlet       = rate of collection at the inlet of the cyclone
                                                                               ΔPbed        = pressure drop across the bed
                              Bubble Cap                      Manifold
                                                                               ΔPorifice    = pressure drop across each orifice in the distribu-
     With
                                                  Orifices
                                                                                               tor or sparger
    Shrouds
                                                                               Qbed         = total gas volumetric flowrate through the bed
                                                                               Qemulsion    = gas volumetric flowrate through the dense phase
                                                                               Qbubbles     = gas volumetric flowrate through the bubbles
                              Shrouds or                        Weeped
                                                                Catalyst       Rep,mf       = particle Reynolds number calculated at the mini-
                               Diffusers
                                                                                               mum fluidization velocity
                  Orifice                                                      umb          = minimum bubbling velocity for the onset of
                                                                                               bubbles in the bed
                                                                               umf          = minimum fluidization velocity
                                                                               uo           = superficial gas velocity
                              Bubble Cap                      Manifold         xi           = collection efficiency for a particle of size i
                                                                                               obtained from the grade efficiency curve
    Without                                                                    Y            = fraction of the gas in the bubbles (which ranges
    Shrouds                                                                                    from 0 to 1)
                                                                               Greek Letters
                                                                               ε            = bed voidage (i.e., gas volume fraction)
                                                                               μ            = fluid viscosity
                   Orifice                         Orifices                    ρbulk        = bulk density
                                                                               ρg           = gas density
p Figure 7. The addition of shrouds on bubble caps and spargers can help       ρp           = particle density
minimize particle attrition and particle entrainment.


Copyright © 2014 American Institute of Chemical Engineers (AIChE)                                  CEP    November 2014   www.aiche.org/cep   25

<!-- page 6 -->

Back to Basics
of trauma. The dynamic nature of the bed and the high
velocities in the cyclones can cause particles to fragment
or abrade. Particle fragmentation is a catastrophic breakup
of a parent particle into daughter particles. Abrasion is the
removal of small edges and protrusions from the particle
surfaces; although the size of the parent particle does not
change much, an excess of fines (i.e., particles smaller than
40 μm) may develop.
It should be noted that the crush strength of a particle
is not an indication of particle attrition properties. Crush
strength testing is relatively static and used mostly for
packed-bed applications. Attrition is caused by transient,
dynamic forces. Hence, attrition is typically evaluated by
ball mill testing (12), jet impact testing, immersed jet test-
ing (13), or jet cup testing (14). The jet cup method, which
involves using a tangential gas jet to promote swirling flow
in a cylindrical or conical cup (14), is usually used, as it
resembles the abrasion caused by a cyclone wall.
Particle attrition occurs when the high-velocity gas jets
from the distributor cause particles to collide with each
other and with the walls of the vessel. Attrition also occurs
when particles carried by the swirling gas flow collide at the
cyclone inlet and throughout the cyclone cone region.
It is imperative that gas jets exiting the distributor do
not intersect with each other or impact the vessel wall
or internals. The velocities of these gas jets can exceed
100 ft/sec (30 m/sec), and particles carried in them can reach
velocities of more than 50 ft/sec (15 m/sec). A particle in a
gas jet impinging on a wall might experience a 30 mph or
higher collision; two particles in impinging jets could collide
at more than 60 mph. Furthermore, jets that are too close
together can coalesce, which increases particle attrition.
Therefore, the distributor needs to be designed so that the
gas jet’s penetration length is less than the distance between
TDH
Bed Height
0 0.2 0.4
Solids Volume Fraction
26 www.aiche.org/cep November 2014 CEP
thgieH
60
40
20
0
p Figure 8. The transport disengagement height (TDH) is the point at
which larger entrained particles return to the bed, while smaller particles
remain entrained.

the orifice and the vessel wall or other internals. This will
reduce erosion of the vessel walls and internals as well. The
design also needs to ensure that the trajectory of each jet
does not intersect with any other jet trajectory.
In order to design a distributor correctly, the appropri-
ate jet penetration length needs to be determined. Published
correlations (15–17) work well for typical systems with
Geldart Group A and B particles. However, there can be
a wide variation in results for atypical systems, such as
high- pressure fluidized beds and fluidized beds containing
nonspherical particles or large particles.
High attrition could still be an issue even if a distribu-
tor is designed to minimize jet-wall internal collisions or jet
intersections, especially if the particles are fragile. In such
cases, shrouds (sometimes called diffusers) can be installed
to limit particle entrainment in the jet. Shrouds are sec-
tions of piping that extend from each orifice in a grid plate
(Figure 7) to shield part of the jet, making it less likely for
particles to become entrained. It is important that the shrouds
extend far enough to prevent particles from being sucked
into the base of the jet.
Structural integrity. Mechanical stress in a fluidized bed
can be significant. A power outage can cause the entire bed
of material to fall onto the distributor. Thus, the distributor
needs to be designed to withstand such forces.
Furthermore, thermal expansion can cause even the
thickest distributor to buckle. Thus, the design needs to
allow for such expansion. Conical and convex plates have
been used successfully for such applications.
In addition, a bubbling fluidized bed has an inherent
frequency ranging from 1 Hz to 5 Hz. The harmonics of the
distributor plate or sparger need to account for this.
Entrainment
For a particle to be carried out of a bed, the local gas
velocity needs to exceed the particle’s terminal velocity.
Terminal velocity is the speed at which an object in free
fall is no longer accelerating. A skydiver’s terminal veloc-
ity is about 120 mph (155 km/sec). A particle in a bed has a
different field of reference. Instead of a body falling through
a stagnant fluid, in a fluidized bed, the fluid is moving the
body. A particle’s terminal velocity is the lowest gas velocity
that causes particles to start moving with the gas. This is the
point at which entrainment begins.
However, particle entrainment appears to occur well
before the superficial gas velocity exceeds the single-particle
terminal velocity. While the single-particle terminal veloc-
ity is a factor, other factors contribute to entrainment as
well. For instance, local gas velocities may be higher than
the superficial gas velocity, and small particles may have
terminal velocities lower than the local gas velocity. There
is often a wide distribution of particle sizes in the bed, and
Copyright © 2014 American Institute of Chemical Engineers (AIChE)

*[figure(s) on p.6 → figures/intro-to-fluidization-p06.png]*


<!-- page 7 -->

particle separation based on size (elutriation) may occur.
This is common with bubbles that have rise velocities higher
than the superficial gas velocity. The momentum of a bubble
breaking at the top of a fluidized bed also plays a role in
entrainment: As a bubble bursts, particles at the bottom of
the bubble can be ejected upward into the freeboard region
above the bed (18).
As the gas containing entrained particles flows upward,
the larger and/or heavier particles may fall back into the bed.
At some distance above the bed, only the smaller particles
remain entrained. This point is referred to as the transport
disengagement height (TDH). Figure 8 illustrates a typical
solids concentration profile for a bubbling fluidized bed and
the location of the TDH.
The TDH, entrainment rate, and the size of the particles
being entrained are important design parameters for a fluid-
ized bed. The TDH is required because the cyclone or vessel
exits are commonly installed at or above the TDH to reduce
the solids loading to the cyclones and minimize exit losses.
The entrained particle size distribution is needed to size the
cyclones and determine the resulting collection efficiency.
The entrained particle size distribution is also used, with the
entrainment rate, to estimate the solids loss rate, which is
required to specify the size of the cyclone dipleg. Diplegs
designed based on an entrainment rate that is too high or too
low are prone to plugging.
Empirical entrainment rate correlations are available
(19–24), but their accuracy is tied to the systems from which
the data were collected. As a result, entrainment rate cor-
relations can vary by two orders of magnitude, especially
for particles smaller than 50 μm. The variability among
Cyclone with Dust Hopper Cyclone with Vortex Stabilizer
Outlet Tube
Inlet
Barrel
Cone
Dust Hopper
Vortex Stabilizer
Dipleg
p Figure 9. In a reverse-flow cyclone separator, entrained particles enter
from the top of the cyclone. Centrifugal forces separate the solids from the
gases. The particles spiral down the barrel and cone region and exit via the
dipleg. The gas exits through the outlet tube.
Copyright © 2014 American Institute of Chemical Engineers (AIChE)

entrainment rate correlations occurs, in part, because the
correlations were derived based on the assumption that
particles in a fluidized bed behave independently of each
other. This may not be the case for small particles, which
can form weakly bound clusters that have a larger aero-
dynamic diameter and are less likely to be entrained than the
lone particles (8). Therefore, it is recommended that when
designing a system with a new or untested type of particle,
the entrainment rate should first be measured experimentally
before using a correlation that has not been validated or
completing computational fluid dynamics modeling.
Cyclones
The gases from a fluidized bed usually need to be cleaned
of entrained particles. In commercial-sized units, particle
entrainment can be significant, and the particles often need
to be collected and returned to the bed. Cyclone separators
(Figure 9) are typically employed for such applications.
Ray CoCCo is the President and CEO of Particulate Solid Research, Inc.
(PSRI), a consortium-based company with 32 member companies
in Canada, France, Brazil, Finland, Germany, India, South Africa,
Saudi Arabia, and the U.S. Before joining PSRI, he was with the Dow
Chemical Co. for 17 years as a technical research leader. He was Chair
of the AIChE Particle Technology Forum (Group 3), is a board member
of ASTM’s D18.24 Committee on Characterization and Handling of
Powders and Bulk Solids, and is on the Editorial Advisory Board for
Powder and Bulk Engineering and Powder Technology. He is a member
of AIChE’s Chemical Engineering Technology Operating Council (CTOC),
and the Advisory Boards for the Univ. of Florida’s Chemical Engineering
Dept., Auburn Univ.’s Chemical Engineering Dept., and Centre of Nature
Inspired Engineering at Univ. College London. Cocco is also a member
of the International Fluidization Conference Advisory Committee and
the meeting chair for the next World Congress in Particle Technology
(WCPT8). He has 40 publications, three book chapters, three patents
and patent applications, and numerous invited presentations. He
consults for industry, national labs, and universities on a regular basis.
Cocco received his BS in chemical engineering from the Univ. of Florida
and his PhD from Auburn Univ.
S. B. REDDy KaRRi is an engineering director at PSRI. He is an expert in the
area of fluid-particle systems, such as fluid beds, cyclones, diplegs,
standpipes, and risers. He extensively consults and troubleshoots
industrial problems in the energy field. He is currently Chair of the
Fluidization and Fluid Particle Systems Sub committee of the Particle
Technology Forum. He has written over 100 papers in the area of
fluid-particle systems, and has been teaching PSRI technical seminars
to industrial engineers from all over the world for the last 20 years.
Karri received his BS in chemical engineering from the Univ. of New
Hampshire.
TED KnowlTon is a research fellow at PSRI. Previously, he was the head
of the Fluidization Research and Consulting Group of the Institute of
Gas Technology (IGT). He is recognized worldwide as an authority in
the field of fluidization, fluid-solid contacting, and solids transport. He
developed the L-valve, a nonmechanical device that controls solids flow
in high-pressure, high-temperature systems. He received the Distin-
guished Service Award from the Fluidization and Fluid-Particle Systems
Committee of AIChE in 1990, the Fluor Daniel Lectureship Award for his
contributions to the area of fluidization in 1996, and the Thiele Award
for outstanding lifelong contributions to the field of chemical engineer-
ing in 2004. He has authored over 120 technical articles and three
book chapters, has edited several books on fluidization, and holds four
patents. Knowlton received his BS and PhD in chemical engineering
from Iowa State Univ.
Article continues on next page
CEP November 2014 www.aiche.org/cep 27

*[figure(s) on p.7 → figures/intro-to-fluidization-p07.png]*


<!-- page 8 -->

Back to Basics


                                                                                 a. Primary Inlet                                  b. Primary                                 c. Primary Outlet
                                                                            Particle Size Distribution                          Grade Efficiency                          Particle Size Distribution
                                                          0.2                                                   1                                        0.2




                                                                                                             Grade Eff.
                                                                                      Dp,50=41 µm                               96.8% Efficiency                                     Dp,50=28 µm




                                                                                                                                                         wt%
                                                          wt%
                                                                                      10.2 kg/s                                                                                      0.32 kg/s


                                                              0                                         0.75                                                0
                                                                        0            dp, µm          120     0                      dp, µm         120                0            dp, µm          120

                                                                                  f. Tertiary                               e. Secondary Outlet                                d. Secondary
                                                                               Grade Efficiency                           Particle Size Distribution                          Grade Efficiency
                                                              1                                            0.4                                               1




                                                                                                                                                         Grade Eff.
                                                           Grade Eff.
                                                                                  89.4% Efficiency                                Dp,50=6.6 µm                                93.5% Efficiency




                                                                                                           wt%
                                                                                                                                  0.02 kg/s


                                                         0.85                                                0                                           0.8
                                                                    0                dp, µm          120           0                dp, µm         120            0                dp, µm          120
                                                                                    g. Tertiary Outlet
                                                                                Particle Size Distribution
                                      Tertiary Cyclone    0.7


                     Secondary Cyclone
                                                                                        Dp,50<1 µm
                                                           wt%




                                                                                        0.002 kg/s
      Primary Cyclone

                                                              0
                                                                   0                      dp, µm                          120

p Figure 10. Solids losses can be reduced by using a train of cyclones. In this example, adding secondary and tertiary cyclones after the primary cyclone
reduces the solids losses from 10.2 kg/sec to 0.002 kg/sec. The Dp,50 is the median particle size within each particle size distribution (PSD).


    The most common type of cyclone separator used in                                          size distribution has a median size, or a Dp,50, of 41 μm
fluidized beds is the reverse-flow cyclone (Figure 9), which                                   (Figure 10a). This corresponds to a solids loss rate of more
consists of an inlet connected tangentially to a barrel section                                than 850 m.t./day. Even for a low-cost solid, such a loss rate
with a conical exit at the bottom. An outlet tube (or vortex                                   translates to hundreds of millions of dollars a year. Further-
finder) extends from the top of the barrel section. Momen-                                     more, the downstream equipment would need to be cleaned
tum pushes the incoming particles toward the wall, where                                       to remove particle buildup, adding another cost. The addi-
centrifugal forces cause gas-solid separation. The particles,                                  tion of cyclone separators can reduce these losses 100-fold
which experience forces as high as hundreds of times the                                       or more.
force of gravity, spiral down the barrel and cone region and                                       The grade efficiency curve for the primary cyclone
exit through the dipleg. Most of the gas reverses its flow,                                    (Figure 10b) allows the particle collection efficiency to be
typically in the cone region, and exits through the outlet                                     determined from:
tube. This reverse flow of gas has a tighter spiral, which pro-
vides a second stage of separation with even higher forces
that move the particles back to the wall. Thus, the name —
reverse flow cyclones.
    The collection efficiency of a cyclone can be estimated
from a grade efficiency curve — a plot of the probability                                      where mi is the rate of collection for a particle of diameter i,
that a particle of a particular size can be collected. Smaller                                 minlet is the rate of collection at the inlet of the cyclone,
particles are less likely to be collected than larger particles                                xi is the collection efficiency for a particle of size i obtained
unless they cluster or agglomerate. Correlations are avail-                                    from the grade efficiency curve, and mcollected is the total
able (25, 26) to construct the cyclone grade efficiency curve                                  collection rate. The primary cyclone reduces the loss rate to
based on design parameters, operating conditions, and physi-                                   0.32 kg/sec, and the particle size distribution shifts and now
cal properties.                                                                                has a median of 28 μm (Figure 10c). This corresponds to an
    For most fluidized-bed applications, one cyclone is                                        overall cyclone collection efficiency of 96.8%.
not enough. Suppose the entrainment rate from the exit of                                           Even with a 96.8% collection efficiency for the primary
a fluidized bed is measured at 10 kg/sec and the particle                                      cyclone, losses will amount to millions of dollars per year.


28       www.aiche.org/cep    November 2014 CEP                                                          Copyright © 2014 American Institute of Chemical Engineers (AIChE)

<!-- page 9 -->

A secondary cyclone installed downstream of the is that they are difficult to access for servicing. Because
primary cyclone’s outlet tube reduces the loss rate to cyclones are a common source of reliability problems, ser-
0.02 kg/sec (Figure 10e). If that rate is still too high, a ter- vicing capabilities need to be considered.
tiary cyclone can be added to reduce the loss rate further, to
0.002 kg/sec (Figure 10g). A train of cyclones such as this Closing thoughts
can reduce the costs due to particle losses from the fluidized Many new fluidizing processes are emerging, including
bed from tens of millions of dollars per year to hundreds of biomass gasification and pyrolysis, coal gasification, poly-
thousands of dollars. crystalline silicone synthesis (for solar panel manufactur-
Adding more cyclones beyond three is usually not cost- ing), chemical looping (for carbon dioxide sequestration),
effective. As the median size of the particles exiting succes- methane coupling, gas-to-liquid (GTL) conversion, and
sive cyclones decreases, the probability of collection by a propane dehydrogenation, to name a few. Fluidized beds
subsequent cyclone decreases (Figures 10b, 10d, and 10f) can be an effective unit operation if designed correctly.
and the collection efficiency decreases. In addition to the factors discussed here, other impor-
Cyclones are often located within the fluidized bed, as tant considerations include the management of fines, bed
this reduces capital costs, especially for beds operating at expansion, pressure effects, and potential gas bypassing.
high pressures. Some pilot units, dryers, and heat treaters With proper engineering, fluidized beds can provide years
have external cyclones. A disadvantage of internal cyclones of reliable, economical service. CEP
Literature Cited
1. Merrow, E., “Linking R&D to Problems Experienced in Solids D5757-00, ASTM, West Conshohocken, PA (Dec. 2004).
Processing,” Rand Report No. P-7034, Rand Corp., Santa Monica,
14. Cocco, R., et al., “Jet Cup Attrition Testing,” Powder Technology,
CA, pp. 1–23 (Nov. 1984).
200, pp. 224–233 (2010).
2. Ergun, S., “Fluid Flow through Packed Columns,” Chem. Eng.
15. Shakhova, N. A., “Discharge of Turbulent Jets into a Bed,”
Progress, 48, pp. 89–94 (1952).
Inzhenerno-Fizicheskii Zhurnal, 14 (1), pp. 61–69 (1968).
3. ASTM International, “Standard Test Method for Measuring the
16. Zenz, F., “Bubble Formation and Grid Design,” Institute of Chemi-
Minimum Fluidization Velocity of Free Flow Powders,” ASTM
cal Engineering Symposium Series, Ser. 30, p. 136 (1968).
D7743-12, ASTM, West Conshohocken, PA (2012).
17. Merry, J. M. D., “Penetration of Vertical Jets into Fluidized Beds,”
4. Wen, C. Y., and Y. H. Yu, “A Generalized Method for Predicting
AIChE Journal, 21 (3), pp. 507–510 (1975).
the Minimum Fluidization Velocity,” AIChE Journal, 12,
pp. 610–612 (1966). 18. Davidson, J. F., and D. Harrison, “Fluidized Particles,”
Cambridge University Press, Cambridge, U.K. (1963).
5. Toomey, R. D., and H. F. Johnstone, “Gaseous Fluidization of
Solid Particles,” Chem. Eng. Progress, 48 (5), pp. 220–226 19. Zenz, F., and N. A. Weil, “A Theoretical-Empirical Approach to the
(May 1952). Mechanism of Particle Entrainment from Fluidized Beds,” AIChE
Journal, 4 (4), pp. 472–479 (1958).
6. Geldart, D., “Types of Gas Fluidization,” Powder Technology, 7,
pp. 285–292 (1972). 20. Geldart, D., et al., “The Effect of Fines on Entrainment from Gas
Fluidized Beds,” Transactions of the Institute of Chemical Engi-
7. Kunni, D., and O. Levenspiel, “Fluidization Engineering,” 2nd ed.,
neering, 57, pp. 269–277 (1979).
Butterworth-Heinemann, Boston, MA (1991).
21. Lin, L., et al., “Elutriation and Attrition of Char from a Large Fluid-
8. Cocco, R. F., et al., “Particle Clusters in and above Fluidized Beds,”
ized Bed,” Powder Technology, 27 (1), pp. 105–115 (1980).
Powder Technology, 203, pp. 3–11 (2010).
22. Colakyan, M., et al., “Elutriation from a Large Particle Fluidized
9. Epstein, N., and J. R. Grace, “Spouting of Particulate Solids” in
Bed with and without Immersed Heat Transfer Tubes,” Chem. Eng.
“Handbook of Powder Science and Technology,” Fayed, M. E., and
Progress Symposium Series, 77 (205), pp. 66–75 (1981).
L. Otten, eds., Springer, NY, pp. 532–567 (1997).
23. Colakyan, M., and O. Levenspiel, “Elutriation from Fluidized
10. Grasselli, R. K., “Handbook of Heterogeneous Catalysis: Vol. 1,” Beds,” Powder Technology, 38, pp. 223–232 (1984).
Ertl, G., et al., eds., 2nd ed., Wiley-VCH, p. 2302 (1997).
24. Stojkovski, V., and Z. Kostic, “Empirical Correlation for Predic-
11. Karri, S. B. R., and T. Knowlton, “Gas Distributor and Plenum
tion of the Elutriation Rate Constant,” Thermal Science, 7,
Design in Fluidized Beds,” in “Fluidization Solids Handling and
pp. 43–58 (2003).
Processing,” Yang, W.-C., ed., Noyes Publications, Westwood, NJ,
pp. 209–235 (1999). 25. Leith, D., and W. Licht, “The Collection Efficiency of Cyclone
Type Particle Collectors — A New Theoretical Approach,” Chem.
12. ASTM International, “Standard Test Method for Attrition and
Eng. Progress Symposium Series, 68 (126), pp. 196–206 (1972).
Abrasion of Catalysts and Catalyst Carriers,” ASTM D4058-96,
ASTM, West Conshohocken, PA (Mar. 2006). 26. Hoffmann, A. C., and L. E. Stein, “Gas Cyclones and Swirl Tubes:
Principles, Design and Operations,” 2nd ed., Springer, Heidelberg,
13. ASTM International, “Standard Test Method for Determination of
Germany (2008).
Attrition and Abrasion of Powdered Catalysts by Air Jets,” ASTM
Copyright © 2014 American Institute of Chemical Engineers (AIChE) CEP November 2014 www.aiche.org/cep 29

**Table (p.9) — auto-extracted, verify against PDF:**

| Literature Cited |
|---|
| 1. Merrow, E., “Linking R&D to Problems Experienced in Solids D5757-00, ASTM, West Conshohocken, PA (Dec. 2004). |
| Processing,” Rand Report No. P-7034, Rand Corp., Santa Monica, 14. Cocco, R., et al., “Jet Cup Attrition Testing,” Powder Technology, CA, pp. 1–23 (Nov. 1984). 200, pp. 224–233 (2010). 2. Ergun, S., “Fluid Flow through Packed Columns,” Chem. Eng. 15. Shakhova, N. A., “Discharge of Turbulent Jets into a Bed,” Progress, 48, pp. 89–94 (1952). Inzhenerno-Fizicheskii Zhurnal, 14 (1), pp. 61–69 (1968). 3. ASTM International, “Standard Test Method for Measuring the 16. Zenz, F., “Bubble Formation and Grid Design,” Institute of Chemi- Minimum Fluidization Velocity of Free Flow Powders,” ASTM cal Engineering Symposium Series, Ser. 30, p. 136 (1968). D7743-12, ASTM, West Conshohocken, PA (2012). 17. Merry, J. M. D., “Penetration of Vertical Jets into Fluidized Beds,” 4. Wen, C. Y., and Y. H. Yu, “A Generalized Method for Predicting AIChE Journal, 21 (3), pp. 507–510 (1975). the Minimum Fluidization Velocity,” AIChE Journal, 12, pp. 610–612 (1966). 18. Davidson, J. F., and D. Harrison, “Fluidized Particles,” Cambridge University Press, Cambridge, U.K. (1963). 5. Toomey, R. D., and H. F. Johnstone, “Gaseous Fluidization of Solid Particles,” Chem. Eng. Progress, 48 (5), pp. 220–226 19. Zenz, F., and N. A. Weil, “A Theoretical-Empirical Approach to the (May 1952). Mechanism of Particle Entrainment from Fluidized Beds,” AIChE Journal, 4 (4), pp. 472–479 (1958). 6. Geldart, D., “Types of Gas Fluidization,” Powder Technology, 7, pp. 285–292 (1972). 20. Geldart, D., et al., “The Effect of Fines on Entrainment from Gas Fluidized Beds,” Transactions of the Institute of Chemical Engi- 7. Kunni, D., and O. Levenspiel, “Fluidization Engineering,” 2nd ed., neering, 57, pp. 269–277 (1979). Butterworth-Heinemann, Boston, MA (1991). 21. Lin, L., et al., “Elutriation and Attrition of Char from a Large Fluid- 8. Cocco, R. F., et al., “Particle Clusters in and above Fluidized Beds,” ized Bed,” Powder Technology, 27 (1), pp. 105–115 (1980). Powder Technology, 203, pp. 3–11 (2010). 22. Colakyan, M., et al., “Elutriation from a Large Particle Fluidized 9. Epstein, N., and J. R. Grace, “Spouting of Particulate Solids” in Bed with and without Immersed Heat Transfer Tubes,” Chem. Eng. “Handbook of Powder Science and Technology,” Fayed, M. E., and Progress Symposium Series, 77 (205), pp. 66–75 (1981). L. Otten, eds., Springer, NY, pp. 532–567 (1997). 23. Colakyan, M., and O. Levenspiel, “Elutriation from Fluidized 10. Grasselli, R. K., “Handbook of Heterogeneous Catalysis: Vol. 1,” Beds,” Powder Technology, 38, pp. 223–232 (1984). Ertl, G., et al., eds., 2nd ed., Wiley-VCH, p. 2302 (1997). 24. Stojkovski, V., and Z. Kostic, “Empirical Correlation for Predic- 11. Karri, S. B. R., and T. Knowlton, “Gas Distributor and Plenum tion of the Elutriation Rate Constant,” Thermal Science, 7, Design in Fluidized Beds,” in “Fluidization Solids Handling and pp. 43–58 (2003). Processing,” Yang, W.-C., ed., Noyes Publications, Westwood, NJ, pp. 209–235 (1999). 25. Leith, D., and W. Licht, “The Collection Efficiency of Cyclone Type Particle Collectors — A New Theoretical Approach,” Chem. 12. ASTM International, “Standard Test Method for Attrition and Eng. Progress Symposium Series, 68 (126), pp. 196–206 (1972). Abrasion of Catalysts and Catalyst Carriers,” ASTM D4058-96, ASTM, West Conshohocken, PA (Mar. 2006). 26. Hoffmann, A. C., and L. E. Stein, “Gas Cyclones and Swirl Tubes: Principles, Design and Operations,” 2nd ed., Springer, Heidelberg, 13. ASTM International, “Standard Test Method for Determination of Germany (2008). Attrition and Abrasion of Powdered Catalysts by Air Jets,” ASTM |
