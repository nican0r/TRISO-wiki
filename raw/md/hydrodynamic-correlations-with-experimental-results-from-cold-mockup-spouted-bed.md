---
source_pdf: Hydrodynamic Correlations with Experimental Results from Cold Mockup Spouted Beds for Nuclear Fuel Particle Coating .pdf
pages: 19
converter: pdf2md.py (pdfplumber + pdftotext)
note: lossy conversion — verify quantities and equations against the PDF
---


<!-- page 1 -->

Hydrodynamic Correlations with Experimental
Results from Cold Mockup Spouted Beds for
Nuclear Fuel Particle Coating
Jiandong Zhou1, Duane D. Bruns1, Charles E. A. Finney2, C. Stuart Daw2 and
Sreekanth Pannala3, David L. McCollum4
(1) Chemical Engineering Department, University of Tennessee, Knoxville, 419
Dougherty Hall, Knoxville, TN 37996.
(2) Engineering Science and Technology Division, Oak Ridge National Laboratory,
Oak Ridge, TN 37831,
(3) Computational Science and Mathematics Division, Oak Ridge National
Laboratory, Oak Ridge, TN 37831,
(4) Institute of Transportation Studies, University of California, Davis, CA 95616.
Abstract
A cold mockup of a nuclear particle spouted bed coater is systematically studied over an
experimental matrix of four particle radii, three cone angles, several gas (humidified air)
flow rates, and four particle inventories. Spherical ZrO particles of 300, 400, 500 and
2
650μm with a tight distributed size are selected as surrogates for nuclear fuel particles
due to their similar physical properties. Three spouted beds with 45, 60, and 75-degree
cone angles are used. The gas flow rate spans the fully spouted condition to minimum
spouted condition. The bed inventories are H/D of 0.50, 0.55, 0.60 and 0.65. The column
c
diameter is 5 cm with an inlet throat diameter of 0.04 cm. The U measurements closely
mf
follow the Wen and Yue correlation. Due to the high density of our particles a new U
ms
correlation is needed. Our dimensionless U correlation for ZrO2 particles is presented
ms
as a function of Re number at U , particle size (D cone angle of the spouted bed (γ)
ms p),
and static particle height (H /D ). A new quantitative method for U evaluation is
0 c ms
presented. Another dimensionless correlation for average pressure drop across the
spouted bed covering the experimental matrix is given in terms of U/U , γ, H /D and
ms 0 c,
D /D . The first four moments and the power spectral density of the pressure time series
p c
are calculated with trends described. The main frequency peak of the pressure drop signal
shifts from a high to a low value as the air velocity drops from fully spouted velocity to
near minimum spouting velocity. As the air flow rate is lowered to 1.1~1.2 U , the main
ms
frequency peak increases sharply. Main frequency peak of the pressure signal increases
as particle size, static particle height or cone angle increase. The 0.5mm particles have
the sharpest main frequency peak plot while the other plots become wider as D increases
p
or decreases. The standard deviation of the pressure signal for the 0.3mm, 0.4mm and
0.65mm particles tend to increase as gas flow rate is lowered to U while that of the
ms
0.5mm particles tends to decreases. The skewness also increases as gas flow rate is
lowered to U except for 0.65mm particles. In general, the kurtosis also increases as gas
ms
flow rate approaches U .
ms

<!-- page 2 -->

1. Introduction
Coating nuclear fuel particles can improve safety and flexibility during their storage,
movement, and usage [1]. The spouted bed is a good candidate for coating nuclear fuel
particles due to good mixing affects and uniform exposure time of the particles to the
CVD (Chemical Vapor Deposition) gases so that the different layers coat the fuel
particles uniformly.
The TRISCO coated uranium fuel particle has been developed. It is coated by 4 layers: an
amorphous (soft) carbon layer, then a pyrolytic (hard) carbon layer, then Silicon Carbide
(SiC), and finally another pyrolytic carbon layer. This coating process uses a CVD
spouted bed running at temperatures typically from 1200 to 1800 degree C. In order to
produce large quantities of fuel to support the option to use AGRs, the spouted bed coater
process must be scaled-up from the present experimental 5-cm diameter coaters. There is
no universal way to scale-up fluidized beds even for hydrodynamics [2]. Spouted
fluidized beds are more considered more complex than fluidized beds. In addition, in the
high temperature coaters, it is nearly impossible to optically observe and monitor the
particles due to the opaque carbon wall of the bed and dense carbon soot inside the bed.
In general, it is also very expensive to set up and run a high-temperature surrogate coater.
Given the above constraints and in consideration of the fact that the state-of-the-art in
fluidized bed design and scale-up is to establish the hydrodynamics from cold bed studies
without reaction, the ambient room-temperature spouted bed coater will be studied first
utilizing both experiment and simulation. Only experimental results are reported in this
paper. Other members of the research team are using the experimental results to calibrate
and evaluate simulation code. Initial interaction between experimental and simulation
campaigns is published elsewhere [16].
The experiments that are necessary for validating the simulations [3] are focused on
exploring the hydrodynamics of surrogate particles (ZrO ) in cold mockup spouted beds.
2
For this purpose the bed pressure drop signal is studied first including its variation
characteristics. Beyond the average pressure, the dynamic pressure characteristics dictate
the behavior of fluidized and spouted fluidized beds. Thus, it is critical that simulations
capture this dynamic behavior. It is also one of the most easily obtained process signals
from mockup coaters and hot coaters. By comparing the hot pressure signal with
preliminary experimental results from the cold mockup we are getting insight into the
running status of the hot spouted bed coaters. Although there are many papers analyzing
the pressure signals in fluidized beds [4-6], most of them deal with the particles with
densities lower than or around 3 grams/cc. These included glass, polymer materials,
wheat, beans etc. The density of the surrogate nuclear fuel particle, ZrO , is 6 grams/cc,
2
which is much higher than the normally studied and reported materials. We need to
investigate the behavior of higher density particles in order to provide solid data for
validating the computer models being developed for uranium particle coaters.
In this paper the gas pressure drop across the spouted bed at stable spouting conditions
(1≤U/U ≤1.9) is studied extensively. The Ums and average pressure drop prediction
ms

<!-- page 3 -->

equations are developed, which is a function of particle size, cone angle, gas flow rate,
and static solid particle height inside the spouted bed. The high frequency variations in
the pressure signals are analyzed with statistical methods and in the frequency domain.
2. Experiments
Figure 1. Photo of experimental spouted bed, γ=60 degree.
Three spouted beds with 45, 60, and 75-degree cone angles are used in this research.
Figure 1 shows the 60 degree spouted bed. The diameter of the columns are all equal to
0.05m. The inlet throat diameter is 0.004m. The conical base is made of Aluminum for
regularity while the cylindrical column is made out of quartz to provide optical access.
The pressure drop across the spouted bed is measured with MKS pressure sensors whose
ranges are 0~ 1,333Pa and 0-13,332Pa.
The data is collected by means of a National Instrument data acquisition system.
Typically the pressure time series is collected at 1,000Hz for one minute. Then the mean
pressure drop is calculated. The gas flow rate is controlled with a MKS mass flow
controller (MFC) with a range of 0~0.2m3/min. The MFC is periodically calibrated to
guarantee its reliability and accuracy. As a result, the gas flow rate is controlled very
accurately and precisely.
Spherical ZrO particles of 300, 400, 500, and 650μm with tight distributed size are
2
selected as surrogates for nuclear fuel particles due to their similar physical properties to
uranium particles. The ZrO particles have a density of 6,050 kg/m3. Compressed air is
2
humidified and used as the fluidizing gas. The air temperature is between 70-79 ˚F and
ambient pressure is around 740mmHg.

*[figure(s) on p.3 → figures/hydrodynamic-correlations-with-experimental-results-from-cold-mockup-spouted-bed-p03.png]*


<!-- page 4 -->

Figure 2. Spouting bed with 54.5 grams of 0.5mm ZrO particles in 60 degree spouted
2
bed with gas flow rates U/Ums being 1.8, 2.1, 2.4 from left to right.
The experimental matrix includes particle diameter, gas flow rate, cone angle, and
particle inventories (H/Dc). Gas flow rate varies from 1.0 U/U to 1.9 U/U where the
ms ms
spouted bed is running at stable spouting conditions. Below 1 U/U , the particles inside
ms
will stop spouting. Above 2 U/U , the particles are spouted unstably and tend to be
ms
carried out of the spouted bed. The particles are classified as group B by Geldart
classification [7, 8].
3. Results and Discussions
3.1 Measurement of U
mf .
Umf is one key parameter for computer simulation and fluidized bed design. The
classical method [9] is used to measure the U , minimum fluidizing velocity.
mf
4000
3500
3000
2500
2000
1500
1000
500
0
0 0.2 0.4 0.6 0.8 1 1.2
gas velocity(m/s)
)aP(pord
erusserP
Figure 3. Measurement of U of 0.65mm ZrO .
mf 2

*[figure(s) on p.4 → figures/hydrodynamic-correlations-with-experimental-results-from-cold-mockup-spouted-bed-p04.png]*


<!-- page 5 -->

0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
0 0.2 0.4 0.6 0.8
Particle Size(mm)
)s/m(fmU
Test
Wen_Yu correlation
Figure 4. Comparison of measured U with Wen-Yu [8] correlation predicted U for
mf mf
different D .
p
Figure 3 shows that Umf is measured with little scatter in the data. Figure 4 indicates that
the U of ZrO particles used in this research closely follows the Wen and Yue
mf 2
correlation.
3.2 Measurement of U
ms
The minimum spouting velocity, U , which corresponds to the minimum gas velocity
ms
maintaining the spouting condition of the spouted bed, plays an important role in
dimensionless analysis of the hydrodynamic of the spouted bed and design and operation
of gas-solid spouted beds [10]. Although there are quite a few correlations predicting U
ms
[11, 12], most of them are based on Ums of particles with density lower than or around
3,000 kg/m3. It is necessary to measure Ums for the experimental matrix used to
investigate gas pressure drop (ΔP) and study the hydrodynamics further as well as design
and sale-up spouted beds in future. Ums is a function of particle size (D ), cone angle
p
(γ), and static particle height (H). It is measured in a way similar to measure the
minimum fluidized velocity, Umf. The gas velocity is raised up first to get full spouting
condition. Then lower the gas velocity step by step and the corresponding ΔP keeps
decreasing at first. At U=U , it reaches the minimum value and increases sharply as gas
ms
velocity is just lower than Ums, as shown in Figure 5.
Quantitative evaluation of Ums using the ΔP vs gas flow rate plot is new. The HMI
(Human-Machine-Interface) allows the gas flow rate to be decreased in small increments
accurately without any overshoot in the flow rate. This may be one aspect of identifying
the new technique. Previously minimum spouting velocity was determined by carefully
watching for particle movement on the bed surface visually. Using the minimum in the
plots as, Figure 5, corresponds closely to our visual observations, generally, the particles
appear to have stopped moving at a slightly higher gas velocity than the minimum in the
figure. This method is more quantitative and reproducible than visual observations.

<!-- page 6 -->

1160
1140
1120
1100
1080
1060
1040
1020
1000
980
9 11 13 15 17 19
gas flwo rate(SLPM)
)aP(pord
erusserp
Figure 5. Measurement of U for 53.9 grams 0.5mm ZrO in 60 degree spouted bed. U
ms 2 ms
= 12 liter/min.
The Ums correlation is developed as below with the regression coefficient being 0.98.
H γ
Re = 0.0015Ar0.86( 0)1.59 tan( )0.87 (1)
ms D 2
c
Table 1 Comparison of measured U with predicted U values. Dp=0.5mm, γ=45
ms ms
degree.
H /Dc Measured Equation Method Method Method Method Method
0
Value(m/s) (1)(m/s) 1(m/s) 2(m/s) 3(m/s) 4(m/s) 5(m/s)
0.5
0.0450 0.0393 7.43 14.99 3.78 10.61 0.072
0.6
0.0586 0.0525 9.6 18.8 3.9 12.7 0.0869
0.8
0.0874 0.0829 14.7 26.8 4.2 17 0.1159
1
0.1290 0.1182 20.7 35.4 4.4 21.2 0.1448
Among methods 1 to 5, method 5 is the best and its predicted error is between 12%~60%.
The prediction error of correlation (1) is 8~13%. Method 1, 2, 3, 4, and 5 are from [12],
[13], [14], [15] and [10] respectively. Other correlations have higher errors and are not
listed here. Some correlations do not take into account the cone angle and are not
compared here either. Most of the correlations are based on particles with a density lower
than or around 3,000 kg/m3 while the density of ZrO is 6,050kg/m3. In addition, some of
2
them are more suitable for predicting Ums at H /D greater than 1 while equation (1)
0 c
works at H /D equal to or less than 1.
0 c

**Table (p.6) — auto-extracted, verify against PDF:**

| H /Dc 0 | Measured Value(m/s) | Equation (1)(m/s) | Method 1(m/s) | Method 2(m/s) | Method 3(m/s) | Method 4(m/s) | Method 5(m/s) |
|---|---|---|---|---|---|---|---|
| 0.5 | 0.0450 | 0.0393 | 7.43 | 14.99 | 3.78 | 10.61 | 0.072 |
| 0.6 | 0.0586 | 0.0525 | 9.6 | 18.8 | 3.9 | 12.7 | 0.0869 |
| 0.8 | 0.0874 | 0.0829 | 14.7 | 26.8 | 4.2 | 17 | 0.1159 |
| 1 | 0.1290 | 0.1182 | 20.7 | 35.4 | 4.4 | 21.2 | 0.1448 |


<!-- page 7 -->

The obtained U values are used to specify the gas flow rate for measuring the gas
ms
pressure drop at stable spouting conditions at which U/U is between 1 and 1.9 for this
ms
case.
3.3 Average gas pressure drop correlation
At stable spouting conditions, the total gas pressure drop across the spouted bed is
fluctuated around its mean value, as shown in Figure 6. The average ΔP for different
combinations of U/U , D /D , γ, and H /D is based on the data collected at 1,000Hz for
ms p c o c
one minute and then averaged.
1800
1600
1400
1200
1000
800
600
400
200
0
0 2 4 6 8
Time(second)
)aP(porD
erusserP
saG
Figure 6. Total gas pressure drops in time domain for 53.9 grams 0.5mm ZrO in 60
2
degree spouted bed.

<!-- page 8 -->

3.3.1 ΔP versus U/Ums

                                                         2500


                                                         2000
                                Gas pressure drop (Pa)




                                                                                                                                H/Dc=0.5
                                                         1500
                                                                                                                                H/Dc=0.55
                                                                                                                                H/Dc=0.6
                                                         1000
                                                                                                                                H/Dc=0.65


                                                          500


                                                            0
                                                                0        0.5          1           1.5           2    2.5
                                                                                          U/Ums


Figure 7. ΔP versus U/Ums for 53.9 grams 0.5mm ZrO2 in 60 degree spouted bed.

    At constant Dp, H/Dc, and γ, ΔP is 2nd or 3rd order of polynomial function of U/Ums
as shown in Figure 7. (1≤U/Ums≤1.9).

3.3.2 ΔP versus tan(γ/2)

                                                                                                    3.2
  log(Gas pressure drop)(Pa)




                                                                                                    3.1
                                                                                                                    U/Ums=1.3
                                                                                                                    U/Ums=1.5
                                                                                                        3
                                                                                                                    U/Ums=1.7
                                                                                                                    U/Ums=1.9
                                                                                                    2.9



                                                                                                    2.8
                               -0.5                        -0.4       -0.3     -0.2        -0.1             0
                                                                  log(tan(cone angle/2)


Figure 8. Log(ΔP) vs. log(tan(γ/2)) at Dp=0.5mm, H/Dc=0.6, and different U/Ums.

In order to make angle dimensionless, a tangent transformation of angle is used.
Log(ΔP) linearly increases as log(tan(γ/2)) increases at constant Dp, H/Dc and U/Ums.
Ums increase as cone angle increases. As a result, the absolute gas flow rate increases. So
pressure drop increases.

<!-- page 9 -->

3.3.3 ΔP versus H/Dc


                                                            3.25
                                                             3.2
                                                            3.15
   log(Pressure Drop)




                                                             3.1           U/Ums=1.1
                                                            3.05           U/Ums=1.3
                                                               3           U/Ums=1.5
                                                            2.95           U/Ums=1.7
                                                             2.9
                                                            2.85
                                                             2.8
                        -0.4   -0.3      -0.2        -0.1           0
                                      log(H0/Dc)

Figure 9. Log(ΔP) vs. log(H0/Dc) at Dp=0.5mm, γ=60 degree and different U/Ums.

As static particle height increases, the pressure drop increases exponentially.

3.3.4 ΔP versus Dp
                                                                   3.2

                                                               3.15
   log(Pressure Drop)




                                                                   3.1

                                                               3.05           U/Ums=1.1
                                                                              U/Ums=1.3
                                                                    3         U/Ums=1.5
                                                                              U/Ums=1.7
                                                               2.95

                                                                   2.9

                                                                2.85
                        -2.3   -2.2    -2.1     -2          -1.9    -1.8
                                       log(Dp/Dc)

Figure 10. Log(ΔP) vs. log(Dp/Dc) at H0/Dc=0.7, γ=75 degree and different U/Ums.

<!-- page 10 -->

Pressure drop increases as Dp increases while other factors are kept constant. Linear
relationship approximation between log (ΔP) and log (Dp/Dc) is taken to fit the data.
The effect of Dp/Dc on ΔP is much smaller than the effect of H /D , as shown in figure 5
0 c
and figure 6. It is safe to do this approximation.
3.3.5 Average ΔP prediction equation
ΔP ⎡ U U U ⎤ γ−0.235+0.454 U H −0.081+0.378 U D −0.304+0.516 U
= ⎢56.38( )3−179.6( )2+110.01 −74.35⎥ ×[(tan ) Ums( 0) Ums( p) Ums]
ρH g ⎣ U U U ⎦ 2 D D
b 0 ms ms ms c c
(2)
Equation (2) is based on 273 data points and r2 is 0.93. The prediction error is less
than 15%. For lower value of U/U , the error is even less than 5%.
ms
No correlation equation has been found in literature, which use U/U , γ, H /D and
ms 0 c,
D /D as predictors to estimate the stable gas pressure drop across the spouted bed.
p c
3.4 Analyze pressure drop in time and frequency domain
The gas pressure drop fluctuations are analyzed in the time domain by calculating the
first four moments of the time series: average or mean, standard deviation, skewness and
Kurtosis. Fourier transformation is used to calculate the PSD (power spectral density) for
the time series. The characterization of experimental results in these two domains has
been effective in validating the computer model [16].

<!-- page 11 -->

3.4.1 Main frequency peak vs. gas flow rate
Figure 11. Main frequency peak at different gas flow rate U/U for 53.9 grams 0.5mm
ms
ZrO in 60 degree spouted bed with Dc 0.05m and Di 0.004m.
2
Figure 12. Main frequency peak vs. gas flow rate for 53.9 grams 0.5mm ZrO in 60
2
degree spouted bed.

*[figure(s) on p.11 → figures/hydrodynamic-correlations-with-experimental-results-from-cold-mockup-spouted-bed-p11.png]*


<!-- page 12 -->

The main frequency peak of the pressure drop represents for the formation rate of the
bubble inside the spouted bed. It shifts from 21.4Hz to 17.4Hz as air velocity drops
slowly from fully spouted velocity 2.3Ums to low 1.3Ums, which means the bubble
formation rate is lowering as gas flow rate decreases. The gas passing through the spout
region dominates the particle behavior. At U/Ums = 1.2, the main frequency peak splits
into two peaks. The smaller frequency peak corresponds to the bubble formation
frequency. The higher frequency peak reflects the vibration of the annulus. The void
fraction of the solid particles is lowered so much that the vibration of the annulus tends to
dominate. The variation frequency peak is as high as 25.3 Hz and then shifts down slowly
as air velocity keep lowering until the particles fall out of the spouted bed. As U/Ums is
equal to or less than 1, the spout is diminishing. And the whole gas passes slowly through
whole particles inside the spouted bed. And the vibration of the whole particles
dominates. It can be eyeballed for lower static particle height (H /Dc) for 0.5mm ZrO . It
0 2
can also be observed even for high H /Dc for 0.3mm ZrO .
0 2
Figure 13. Main frequency peak vs. gas flow rate for 53.9 grams 0.3mm ZrO in 60
2
degree spouted bed.

*[figure(s) on p.12 → figures/hydrodynamic-correlations-with-experimental-results-from-cold-mockup-spouted-bed-p12.png]*


<!-- page 13 -->

Figure 14. Main frequency peak vs. gas flow rate for 53.9 grams 0.4mm ZrO in 60
2
degree spouted bed.
Figure 15. Main frequency peak vs. gas flow rate for 53.9 grams 0.65mm ZrO in 60
2
degree spouted bed.
The main frequencies of 0.4mm and 0.65mm particles show the same tendency as gas
flow rate changes from high to low. The tendency of 0.3 mm particle is not obvious.

*[figure(s) on p.13 → figures/hydrodynamic-correlations-with-experimental-results-from-cold-mockup-spouted-bed-p13.png]*


<!-- page 14 -->

3.4.2 Main frequency peak vs. particle size
Figure 16. Main frequency peak vs. particle size for 53.9 grams ZrO in 60 degree
2
spouted bed.
As particle size increases, the main frequency peak increases slowly. 0.5mm particle has
sharpest main frequency peak while others become wider as Dp increases or decreases.
3.4.3 Main frequency peak vs. cone angle
Figure 17. Main frequency peak vs. cone angle at U/Ums=1.5, H /Dc=0.6 and
0
Dp=0.65mm.

*[figure(s) on p.14 → figures/hydrodynamic-correlations-with-experimental-results-from-cold-mockup-spouted-bed-p14.png]*


<!-- page 15 -->

As cone angle increases, the main frequency peak increases and its width increases.
3.4.4 Main frequency peak vs. H /Dc
0
Figure 18. Main frequency peak vs. H /Dc at U/Ums=1.5, cone angle=45 and
0
Dp=0.65mm.
As H /Dc increases, main frequency peak increases.
0
3.4.5 Analyze pressure drop statistically

*[figure(s) on p.15 → figures/hydrodynamic-correlations-with-experimental-results-from-cold-mockup-spouted-bed-p15.png]*


<!-- page 16 -->

Figure 19. Standard deviation, skewness and Kurtosis vs. U/Ums for 53.9 grams 0.3mm
ZrO at 60 degree spouted bed.
2
Figure 20. Standard deviation, skewness and Kurtosis vs. U/Ums for 53.9 grams 0.4mm
ZrO at 60 degree spouted bed.
2
Figure 21. Standard deviation, skewness and Kurtosis vs. U/Ums for 53.9 grams 0.5mm
ZrO at 60 degree spouted bed.
2

*[figure(s) on p.16 → figures/hydrodynamic-correlations-with-experimental-results-from-cold-mockup-spouted-bed-p16.png]*


<!-- page 17 -->

Figure 22. STD, skewness and Kurtosis vs. U/Ums for 53.9 grams 0.65mm ZrO at 60
2
degree spouted bed.
The changes of standard deviation, skewness and kurtosis vs. U/Ums are shown above.
All STD increases as gas flow rate is lowered to Ums. The skewness also increases
except 0.65mm particles. In general, kurtosis also increases as gas flow rate is lowered to
Ums.
4. Conclusions
A quantitative method is used to measure Ums of ZrO2 particles. And an effective
correlation to predict Ums of ZrO2 particles is developed.
An effective dimensionless equation to predict the gas pressure drop across the spouted
bed, ∆P, at stable spouting conditions 1≤U/U ≤ 1.9 is developed. The relationship
ms
between log(∆P) and log(tan(γ/2)) or log(H /D ) is linear while other factors are constant.
0 c
∆P is a third order polynomial function of U/Ums. And the effect of tan(γ/2) and H /D
0 c
as well as Dp/Dc is depended on the U/Ums. The larger the U/Ums is, the larger the
effects they exert.
The main frequency peak of the pressure drop signal shifts from high to lower value as
gas flow rate is lowered from higher value corresponding to full spouting condition to
lower value. As gas flow rate is lowered to 1.1~1.2Ums, the main frequency peak
increases sharply. Main frequency peak of the pressure signal increases as particle size or
static particle height inside the spouted bed or cone angle increase. 0.5mm particle has
sharpest main frequency peak while others become wider as Dp increases or decreases.
The standard deviation of the pressure signal of 0.3mm, 0.4mm and 0.65mm particles
tend to increase as gas flow rate is lowered to Ums while the one of 0.5mm particles
tends to decreases. The skewness also increases except 0.65mm particles as gas flow rate
is lowered to Ums. In general, kurtosis also increases as gas flow rate is close to Ums.

*[figure(s) on p.17 → figures/hydrodynamic-correlations-with-experimental-results-from-cold-mockup-spouted-bed-p17.png]*


<!-- page 18 -->

5. Acknowledgements
Financial support from UT-Battelle and the DOE Nuclear Energy Research Initiative for
Universities DOE is gratefully acknowledged.
6. References
[1] R. L. Beatty, F. A. Carlsen Jr., J. L. Cook, Pyrolytic-carbon coating on ceramic fuel
particles. Nucl. Appl. 1, 560, 1965.
[2] T. M. Knowlton, S. B. R. Karri, A. Issangya, Scale-up of fluidized-bed
hydrodynamics, Powder Technology, 150(2005), 72-77
[3] Joseph A. Sholtis, Jr. Ronald J. Lipinski, and Mohamed S. El-Genk, Coated Particles
for Radioisotope Power Systems and Radioisotope Units, Space Technology and
Applications International Forum-1999, 1378-1384.
[4]Jian Xu, Xiaojun Bao, Weisheng Wei, etc., Statistical and frequency analysis of
pressure fluctuations in spouted beds, Powder Technology, 140, 141-154, 2004.
[5] Lii-Ping Leu, Chih-Nan Wu, Prediction of pressure fluctuations and minimum
fluidization velocity of binary mixtures of Geldart Group B particles in bubbling
fluidized beds, The Canadian Journal of Chemical Engineering, Vol. 78, 578-585, 2000.
[6] M. Olazar, M. J. San Jose, T. Aguayo, J. M. Arandes and J. Bilbao, Pressure drop in
conical spouted beds, The Chemical Engineering Journal, 51, 53-60, 1993.
[7] D. Geldart, Gas Fluidization Technology, Wiley, New York, 1986.
[8] Daizo Kunii, Octave Levenspiel, Fluidization Engineering, Butterworth-Heinemann,
1991.
[9] J. F. Dadiason, R. Clift, D. Harrison, Fluidization, Academic Press, 1985.
[10] S. Aravinth, T. Murugesan, Bioprocess Engineering, 16, 289-293, 1997.
[11] H. T. Bi, A. Macchi, J. Chaouki, and R. Legros, The Canadian J. of Chemical
Engineering, 460-465, Vol 75, 1997.
[12] San Jose, M. J. Olazar, M. Aguayo, A. T. Arandes, J. M. Bilbao, Fluidization VII,
Engineering Foundation, 1992.
[13] M. Z. Tsvik, M. N. Nabiev, N. U. Rizaev et al., Uzb. Khim, Zh. 11(2), 50-59, 1967.
[14] A. E. Gorshtein, I .P. Muknlenov, Zh. Prikl. Khim., 37, 1887-1893, 1964

<!-- page 19 -->

[15] I. P. Mukhlenov, A. E. Gorshtein, Khim. Prom. 41(6), 443-446, 1965.
[16] S. Pannala, C. S. Daw, C. E. A. Finney, D. Boyalakuntla, D. Bruns and J. Zhou,
“ORNL FY04 Process Modeling Summary Report for the Advanced Gas Reactor Fuel
Development and Qualification Program,” Oak Ridge National Laboratory Technical
Report ORNL/CF-04/11, September 2004.
Nomenclature
Ar: Archimedes number = gd 3(ρ -ρ )/ μ 2
p p g g
D : diameter of the column of the spouted bed, m
c
Dp: particle size, mm,
Di: gas inlet diameter, m,
g: gravitational acceleration, m/s2
H : static particle height, m,
0
ΔP: gas pressure drop across the spouted bed, Pa,
Re : Reynolds number at U = ρ U d /μ
ms ms g ms p g
U: gas flow rate, m3/s
U : minimum spouting velocity, m3/s
ms
ρ : bulk density of the particle, kg/m3
b
γ: cone angle of the spouted bed, degree