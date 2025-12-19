### 18.3 SPECIALLY DESIGNED p-n JUNCTIONS

In addition to the use of semi-conductor diode as rectifier, many types of p-n junctions have been developed for special purposes. Three most commonly used such diodes are
(i) Light emitting diode
(ii) Photo diode
(iii) Photo voltaic cell

## Light Emitting Diode

Light emitting diodes (LED) are made from special semi-conductors such as gallium arsenide and gallium arsenide phosphide in which the potential barrier between $p$ and $n$ sides is such that when an electron combines with a hole during forward bias conduction, a photon of visible light is emitted. These diodes are commonly used as small light
Fig. 18.9
Fig. 18.10

A seven segment display 0123456789

Fig. 18.11
sources. A specially formed array of seven LED's is used for displaying digits etc., in electronic appliances (Fig. 18.11).

## Photo Diode

Photo diode is used for the detection of light. It is operated in the reverse biased condition (Fig. 18.12 a). A photo diode symbol is shown in Fig. 18.12 (b). When no light is incident
(a)
(b)
on the junction, the reverse current / is almost negligible but when its p-n junction is exposed to light, the reverse current increases with the intensity of light (Fig.18.12 c).
A photo diode can turn its current ON and OFF in nano-seconds. Hence it is one of the fastest photo detection devices. Applications of photo diode include
i. Detection of both visible and invisible radiations
ii. Automatic switching
iii. Logic circuits
iv. Optical communication equipment etc.

## Photo-Voltaic Cell

It consists of a thick n-type region covered by a thin p-type layer. When such a p-n junction having no external bias (Fig.18.13), is exposed to light, absorbed photons generate electron-hole pairs. It results into an increase percentage of minority charge carriers in both the $p$ and $n$-regions and when they diffuse close to the junction, the electric field due to junction potential barrier sweeps them across the junction. It causes a current flow through the external circuit $R$. The current is proportional to intensity of light.

# 18.4 TRANSISTORS

A transistor consists of a single crystal of germanium or silicon which is grown in such a way that it has three regions (Figs. 18.14 \& 18.15).
In Fig. 18.14 the central region is $p$ type which is sandwiched between two $n$ type regions. It is known as $n-p-n$ transistor. In Fig.18.15, the $n$ type central region is sandwiched between two $p$ type regions. It forms a p-n-p transistor. The central region is known as base and the other two regions are called emitter and collector. Usually the base is very thin, of the order of $10^{-5} \mathrm{~m}$. The emitter and collector have greater concentration of impurity. The collector is comparatively larger than the emitter. The emitter has greater concentration of impurity as compared to the collector.

It can be seen in Figs. 18.14 and 18.15 that a transistor is a combination of two back to back p-n junctions: emitter-base junction and collector-base junction.
For normal operation of the transistor, batteries $V_{B B}$ and $V_{c c}$ are connected in such a way that its emitter-base junction is forward biased and its collector base junction is reverse biased. $V_{c c}$ is of much higher value than $V_{B B}$. Fig. 18.16 shows the biasing arrangement for $n-p-n$ transistor when the transistor has been represented by its symbolic form. Fig. 18.17 shows the same for a p-n-p transistor.
Fig. 18.14
Fig. 18.15
Fig. 18.15

Fig. 18.17
It may be noted that polarities of the biasing batteries $V_{B B}$ and $V_{c c}$ are opposite in the two types of the transistors. In actual practice, it is the n-p-n transistor that is generally used. So we will discuss n-p-n transistors only.

# Current Flow in a n-p-n Transistor

Fig. 18.18 (a) shows a n-p-n transistor at the instant when the biasing voltage is applied. Electrons in the emitter, shown by black dots, have not yet entered the base region. After the application of the biasing voltage, emitter base junction is forward biased, so emitter injects a large number of electrons in base region (Fig. 18.18 b). These free electrons in the base can flow in either of two directions. They can either flow out of the base to the positive terminal of $\mathrm{V}_{\mathrm{pp}}$ or they can be attracted towards the collector because of battery $\mathrm{V}_{\mathrm{cc}}$. Since the base is extremely thin, very few electrons manage to recombine with holes and escape out of the base. Almost all of the free electrons injected from the emitter into the base are attracted by the collector due to the large positive potential $\mathrm{V}_{\mathrm{cc}}$ (Fig. 18.18 c ). Thus, in a normally biased transistor due to above mentioned flow of electrons, we can say, that an electronic current $I_{e}$, flows from the emitter into the base. A very small part of it, current $I_{b}$, flows out of the base, the rest of it $I_{c}$ flows out of the collector (Fig. 18.19).
Fig. 18.19

The flow of conventional current is shown in Fig. 18.20. In future we will use conventional current only. From the figure, it can be seen that

$$
I_{c}=I_{c}+I_{a}
$$

As very few electrons flow out of base, so $I_{B}$ is very small as compared to $I_{c}$.
It is also found that for a given transistor the ratio of collector current $I_{c}$ to base current $I_{b}$ is nearly constant i.e.,

$$
\beta=\frac{I_{c}}{I_{B}}
$$

The ratio $\beta$ is called current gain of transistor. Its value is quite large - of the order of hundreds. Eqs. 18.2 and 18.3 are

fundamental equations of all transistors.
Example 18.1: In a certain circuit, the transistor has a collector current of 10 mA and a base current of $40 \mu \mathrm{~A}$. What is the current gain of the transistor?

# Solution:

$$
\beta=\frac{I_{0}}{I_{B}}=\frac{10 \times 10^{-3} \mathrm{~A}}{40 \times 10^{-3} \mathrm{~A}}=250
$$