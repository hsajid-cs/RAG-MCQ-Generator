### 18.1 BRIEF REVIEW OF p-n JUNCTION AND ITS CHARACTERISTICS

A p-n junction is formed when a crystal of germanium or silicon is grown in such a way that its one half is doped with a trivalent impurity and the other half with a pentavalent impurity. One of the most important building blocks of electronic devices is the p-n junction. Its n-region contains free electrons as majority charge carriers and p-region contains holes as majority charge carriers. Just after the formation of the junction, the free electrons in the n-region, because of their random motion, diffuse into the p-region. As a result of this diffusion, a region is formed around the junction in which charge carriers are not present. This region is known as depletion region (Fig. 18.1 a). In this figure, blue dots represent the free electrons and the small circles show the holes whereas the circles with + and - signs show the positive and negative ions which constitute the depletion region. Due to charge on

these ions a potential difference develops across the depletion region (Fig. 18.1 b). Its value is 0.7 V in case of silicon and 0.3 V in case of germanium. This potential difference, called potential barrier, stops further diffusion of electrons into the p-region.

# Forward Biased p-n Junction

When an external potential difference is applied across a p-n junction such that p -side is positive and n -side is negative, then this external potential difference supplies energy to free electrons in the n-region and to holes in p-region. When this energy is sufficient to overcome the potential barrier, a current of the order of a few miliamperes begins to flow across the p-n junction. In this state the p-n junction is said to be forward biased (Fig. 18.2 a). The variation of current through the junction with the bias voltage can be studied by the circuit shown in Fig. 18.2 (b). The value of current for different values of bias voltage is noted and a current-bias voltage graph is plotted. Fig. 18.3 shows the graph for a typical low power silicon diode.
As shown in Fig.18.3, if forward bias voltage is increased by $\Delta V_{n}$ the current increases by $\Delta I_{r}$. The ratio $\Delta V_{r} / \Delta I_{r}$ is known as forward resistance of the p-n junction, i.e.,

$$
r_{r}=\frac{\Delta V_{L}}{\Delta I_{r}}
$$

It is the resistance offered by the p-n junction when it is conducting. The value of $r_{r}$ is only a few ohms.

## Reverse Biased p-n Junction

When the external source of voltage is applied across a p-n junction such that its positive terminal is connected to nregion and its negative terminal to p-region, the p-n junction is said to be reverse biased (Fig. 18.4). In this situation no current flows due to the majority charge carries. However a very small current, of the order of few microamperes flows across the junction due to flow of minority charge carriers (Fig.18.4). It is known as reverse current or leakage current. The variation of reverse current with the applied bias voltage can be studied by the circuit shown in Fig.18.5. Fig. 18.6 shows the reverse characteristic for the p-n junction. It can be seen that as the reverse voltage is increased from 0 , the reverse current quickly rises to its saturation value $I_{s}$. As the reverse voltage is further increased, the reverse current
Fig. 18.4. Under a reversed biased condition there is almost no current through the diode.
remains almost constant. Here the resistance offered by the diode is very high - of the order of several mega ohms.
As the reverse voltage is increased, the kinetic energy of the minority charge carriers with which they cross the depletion region also increases till it is sufficient to break a covalent bond. As the covalent bond breaks, more electron-hole pairs are created. Thus, minority charge carriers begin to multiply due to which the reverse current begin to increase till a point is reached when the junction breaks down and reverse current rises sharply (Fig.18.6). After breakdown the reverse current will rise to very high value which will damage the junction.
P-n junction is also known as a semi-conductor diode whose symbolic representation is given in Fig. 18.7. The arrow head represents the $p$ - region and is known as anode. The vertical line represents the n-region and is known as cathode. The current flows in the direction of arrow when the diode is forward biased.

# 18.2 RECTIFICATION

Conversion of alternating current into direct current is called rectification. Semi-conductor diodes are extensively used for this purpose. There are two very common types of rectification.
(i) Half-wave rectification and
(ii) Full-wave rectification

## Half-Wave Rectification

A half-wave rectification is shown in Fig. 18.8 where an alternating voltage of period $T$ called input voltage is applied to a diode $D$ which is connected in series with a load resistance $R$. In this method only one half of alternating current cycle is converted into direct current.
During the positive half cycle of the input alternating voltage i.e., during the interval $0 \rightarrow T / 2$, the diode $D$ is forward biased, so it offers a very low resistance and current flows through $R$. The flow of current through $R$ causes a potential drop across it which varies in accordance with the alternating input (Fig. 18.8 c ).
During the negative half cycle i.e., during the period $T / 2 \rightarrow T$, the diode is reverse biased. Now it offers a very high resistance, so practically no current flows through $R$ and potential drop across it is almost zero (Fig. 18.8 c). The same events repeat during the next cycle and so on. The current through $R$ flows in only one direction which means it is a direct current. However, this current flows in pulses (Fig. 18.8 c). The

voltage which appears across load resistance $R$ is known as output voltage.

# Full-Wave Rectification

We have seen that in a half-wave rectification, only one half of the alternating input voltage is used to send a unidirectional current through a resistance. However both halves of the input voltage cycle can be utilized using full-wave rectification. Its circuit consists of four diodes connected in a bridge type arrangement (Fig.18.9). To understand the operation of the circuit, recall that a diode conducts only when it is forward biased. During the positive half cycle, i.e., during the time $0 \rightarrow T / 2$, the terminal $A$ of the bridge is positive with respect to its other terminal $B$. Now the diodes $D_{1}$ and $D_{2}$, become forward biased and conduct. A current flows through the circuit in the direction shown by arrows in Fig. 18.9 (a). During the negative half cycle, i.e., during the time interval $T / 2 \rightarrow T$, terminal $A$ is negative and $B$ is positive. Now the diodes $D_{4}$ and $D_{3}$ conduct and current flows through the circuit in the path shown by arrows in Fig. 18.9 (b). By comparing Figs. 18.9 (a) and 18.9 (b), it can be seen that direction of current flow through the load resistance $R$ is the same in both the halves of the cycle. Thus both halves of the alternating input voltage send a unidirectional current through $R$. The input and output voltages are shown in Fig. 18.10. However the output voltage is not smooth but pulsating. It can be made smooth by using a circuit known as filter.