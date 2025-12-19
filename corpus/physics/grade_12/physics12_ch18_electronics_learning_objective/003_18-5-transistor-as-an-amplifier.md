### 18.5 TRANSISTOR AS AN AMPLIFIER

In majority of electronic circuits, transistors are basically used as amplifiers. An amplifier is thus the building block of every complex electronic circuit. It is for this reason that study of transistor amplifier is important.

The circuit in Fig. 18.21 is a transistor voltage amplifier. The battery $\mathrm{V}_{\mathrm{BE}}$ forward biases the base-emitter junction and $\mathrm{V}_{\mathrm{CC}}$ reverse biases the collector-base junction. $\mathrm{V}_{\mathrm{BE}}$ and $\mathrm{V}_{\mathrm{CE}}$ are the input and output voltages respectively. The base current is $I_{B}=V_{B E} / r_{i e}$ where $r_{i e}$ is base emitter resistance of the transistor. The transistor amplifies it $\beta$ times. So

$$
I_{0}=\beta I_{B}=\beta V_{B E} / r_{i e}
$$

The output voltage $V_{O}=V_{C E}$ is determined by applying KVL equation in the output loop which gives

$$
V_{C C}=I_{C} R_{C}+V_{C E} \quad \text { or } \quad V_{C E}=V_{C C}-I_{C} R_{C}
$$

Substituting the value of $I_{0}$ and replacing by $V_{C E}$ by $V_{0}$

$$
V_{0}=V_{C C}-\beta V_{B E} R_{C} / r_{i e}
$$

When small signal voltage $\Delta V_{\text {in }}$ is applied at the input terminal B, the input voltage changes from $\mathrm{V}_{\mathrm{BE}}$ to $\mathrm{V}_{\mathrm{BE}}+\Delta \mathrm{V}_{\mathrm{in}}$. This causes a little change in base current from $I_{B}$ to $\left(I_{B}+\Delta I_{B}\right)$ due to which the collector current changes from $I_{C}$ to $\left(I_{C}+\Delta I_{C}\right)$. As the collector current changes, the voltage drop across $R_{C}$ i.e., $\left(I_{C} R_{C}\right)$ also changes due to which the output voltage $V_{0}$ changes by $\Delta V_{0}$. Substituting the changed values in Eq. 18.4(a)

$$
V_{0}+\Delta V_{0}=V_{C C}-\beta\left(V_{B E}+\Delta V_{B}\right) R_{C} / r_{i e}
$$

Subtracting Eq. 18.4(a) from Eq. 18.4(b)

$$
\Delta V_{0}=-\beta \Delta V_{b} R_{C} / r_{i e}
$$

Fig. 18.21

Therefore the gain of the amplifier $A=\Delta V_{0} / V_{m}=\beta R_{C} / r_{i e}$ The value of the factor $\beta R_{C} / r_{i e}$ is of the order of hundreds, so the input voltage is amplified. The negative sign shows that there is a phase shift of $180^{\circ}$ between the input and the output signals.

# 18.6 TRANSISTORASASWITCH

Fig. 18.22 (a) shows the circuit in which a transistor is used as a switch. The collectors $C$ and emitter $E$ behave as the terminals of the switch. The circuit in which the current is to be turned OFF and ON, is connected across these terminals. The base $B$ and emitter $E$ act as control terminals which decide the state of the switch.
In order to turn on the switch, a potential $V_{B}$ is applied between control terminals B-E (Fig. 1822 a). This injects a large current $I_{B}$ into the base circuit due to which a very heavy current $I_{C}$ begins to flow in the CE circuit. This large value of collector current is possible only when the resistance between $C$ and $E$ drops down to such a small value that the potential drop across CE is nearly 0.1 volt. In Fig. 18.22 (a) emitter is at ground, so we can assume that collector is also at ground and collector emitter circuit of Fig. 18.22 (a) can be drawn as shown in Fig. 18.22 (b). CE switch is closed and the bulb glows due to flow of large collector current. To turn the switch OFF the base current $I_{B}$ is set zero by opening the base circuit (Fig. 18.22 c). As $I_{C}=\beta I_{B}$, so $I_{C}$ becomes zero and C-E circuit becomes open (Fig. 18.22 d) Now the resistance between $C$ and $E$ becomes nearly infinity which opens the CE switch.
An electronic computer is basically a vast arrangement of electronic switches which are made from transistors.