### 18.15 APPLICATIONS OF GATES IN CONTROL SYSTEMS

Gates are widely used in control systems. They control the function of the system by monitoring some physical parameter such as temperature, pressure or some other physical quantity of the system. As gates operate with electrical voltages only, so some devices are required which can convert various physical quantities into electric voltage.

These devices are known as sensors. For example, in the example of night switch, Light Dependent Resistance (LDR) is a sensor for light because it can convert changes in the intensity of light into electric voltage. A thermister is a sensor for temperature. A microphone is a sound sensor. Similarly there are level sensors which give an electrical signal when the level of liquid in a vessel attains a certain limit. One such application is described here. For example sensors are used to monitor the pressure and temperature of a chemical solution stored in a vat. The circuitry for each sensor is such that it produces a HIGH, i.e., 1 when either the temperature or pressure exceeds a specified value. A circuit is to be designed which will ring an alarm when either the temperature or pressure or both cross the maximum specified limit. The alarm requires a LOW(0) voltage for its activation.

The block diagram of the problem is shown in Fig. 18.43 in which $C$ is the circuit to be designed. Its inputs $A$ and $B$ are fed by the temperature and pressure sensors $T$ and $P$ fitted into the vat. Whenever output of the circuit $C$ is LOW, the alarm is activated. So the circuit $C$ should be such that its output is 0 as soon as the limit for temperature or pressure is exceeded, i.e., when $A=0, B=1$ or when $A=1, B=0$ or when $A=B=1$. The output of $C$ should be HIGH when temperature and pressure are within the specified limit, i.e., when $A=B=0$. This gives the truth table 18.9 which the circuit $C$ has to implement. It can be seen that it is the truth table of NOR gate. So the circuit $C$ in Fig. 18.43 should be a NOR gate as shown in Fig. 18.44.
Fig. 18.43

| Table 18.9 |  |  |
| :--: | :--: | :--: |
| A | B | C |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

Fig. 18.44

# GUMMARY

When an external potential difference is applied across a p-n junction such that p -side is positive and n -side is negative, it is called forward biased.

- When the external source of voltage is applied across a p-n junction such that its positive terminal is connected to n-region and its negative terminal to p-region, the p-n junction is said to be reverse biased.
- Conversion of alternating current into direct current is called rectification.
- When only one half of alternating current cycle is converted into direct current, it is called half-wave rectification.
- Transistor is a semiconductor device consisting of three electrodes, namely emitter, base and collector. For normal operation, the base-emitter junction is forward biased whereas the collector-base junction is reverse biased.

- Input resistance is the resistance between the positive and negative inputs of the amplifier.
- Output resistance is the resistance between the output terminal and ground.
- Instead of making amplifier circuit by discrete components, the whole amplifier is integrated on a small silicon chip and enclosed in a capsule. Pins connected with working terminals such as inputs, outputs and power supply project outside the capsule. Such an integrated amplifier is known as operational amplifier.
- Open loop gain is the ratio of output voltage and the difference between noninverting and inverting inputs when there is no external connection between the outputs and inputs.
- A digital system deals with quantities or variables which have only two discrete values or states.
- The electronic circuits which implement the various logic operations are known as logic gates.

# QUESTIONS

18.1 How does the motion of an electron in a n-type substance differ from the motion of holes in a p-type substance?
18.2 What is the net charge on a n-type or a p-type substance?
18.3 The anode of a diode is 0.2 V positive with respect to its cathode. Is it forward biased?
18.4 Why charge carriers are not present in the depletion region?
18.5 What is the effect of forward and reverse biasing of a diode on the width of depletion region?
18.6 Why ordinary silicon diodes do not emit light?
18.7 Why a photo diode is operated in reverse biased state?
18.8 Why is the base current in a transistor very small?
18.9 What is the biasing requirement of the junctions of a transistor for its normal operation? Explain how these requirements are met in a common emitter amplifier?
18.10 What is the principle of virtual ground? Apply it to find the gain of an inverting amplifier.
18.11 The inputs of a gate are 1 and 0 . Identify the gate if its output is (a) 0 , (b) 1
18.12 Tick $(\checkmark)$ the correct answer
(i) A diode characteristic curve is a plot between
(a) current and time
(b) voltage and time
(c) voltage and current
(d) forward voltage and reverse voltage

(ii). The colour of light emitted by a LED depends on
(a) its forward bias
(b) its reverse bias
(c) the amount of
(d) the type of semi-conductor forward current material used.
(iii) In a half-wave rectifier the diode conducts during
a. both halves of the input cycle
b. a portion of the positive half of the input cycle
c. a portion of the negative half of the input cycle
d. One half of the input cycle
(iv) In a bridge rectifier of Fig. Q. 18.1 when $V$, is positive at point $B$ with respect to point $A$, which diodes are $O N$.
a. $\quad D_{2}$ and $D_{4}$
b. $\quad D_{1}$ and $D_{3}$
c. $\quad D_{2}$ and $D_{3}$
d. $\quad D_{1}$ and $D_{4}$
(v) The common emitter current amplification factor $\beta$ is given by
a. $\frac{I_{C}}{I_{E}}$
b. $\frac{I_{C}}{I_{B}}$
c. $\frac{I_{E}}{I_{B}}$
d. $\frac{I_{B}}{I_{E}}$

Fig. Q. 18.1
(vi) Truth table of logic function
a. summarizes its output values
b. tabulates all its input conditions only
c. display all its input/output possibilities
d. is not based on logic algebra
(vii) The output of a two inputs OR gate is 0 only when its
a. both inputs are 0
b. either input is 1
c. both inputs are 1
d. either input is 0
(viii) A two inputs NAND gate with inputs $A$ and $B$ has an output 0 if
a. Ais 0
b. Bis 0
c. both $A$ and $B$ are zero
d. both $A$ and $B$ are 1
(ix) The truth table shown below is for
a. XNOR gate
b. OR gate
c. AND gate
d. NAND gate

| A | B | X |
| :--: | :--: | :--: |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

# PROBLEMS

18.1 The current flowing into the base of a transistor is 100 $\mu \mathrm{A}$. Find its collector current $I_{c}$, its emitter current $I_{E}$ and the ratio $I_{c} / I_{E}$, if the value of current gain $\beta$ is 100 .
(Ans: $10 \mathrm{~mA}, 10.1 \mathrm{~mA}, 0.99$ )
18.2 Fig.P.18.2 shows a transistor which operates a relay as the switch $S$ is closed. The relay is energized by a current of 10 mA . Calculate the value $R_{e}$ which will just make the relay operate. The current gain $\beta$ of the transistor is 200 . When the transistor conducts, its $V_{e c}$ can be assumed to be 0.6 V .
(Ans: $168 \mathrm{k} \Omega$ )
18.3 In circuit (Fig.P.18.3), there is negligible potential drop between $B$ and $E$, if, $\beta$ is 100 . Calculate
(i) base current
(ii) collector current
(iii) potential drop across $R_{c}$
(iv) $V_{c e}$,
(Ans: $11.25 \mu \mathrm{~A}, 1.125 \mathrm{~mA}, 1.125 \mathrm{~V}, 7.875 \mathrm{~V}$ )
Fig. P. 18.3
Fig. P. 18.4
18.5 Calculate the gain of non-inverting amplifier shown in Fig.P.18.5.
(Ans: 5)