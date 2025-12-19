### 18.7 OPERATIONALAMPLIFIER

As stated earlier, amplifier is an important electronic circuit that is used in almost every electronic instrument. So instead of making amplifier circuit by discrete components, the whole amplifier is integrated on a small silicon chip and enclosed in a capsule. Pins connected with working terminals such as input, output and power supply project outside the capsule (Fig. 18.23 a). The enclosed circuit of the amplifier is used by making requisite connections with these pins. Such as

integrated amplifier is known as operational amplifier (op-amp), as it is some times used to perform mathematical operations electronically.
The op-amp is usually represented by its symbol shown in Fig. 18.23 (b). It has two input terminals. One is known as inverting input (-) and the other non-inventing input (+). A signal that is applied at the inverting (-) input, appears after amplification, at the output terminal with a phase shift of $180^{\circ}$ (Fig. 18.24 a). It can be seen that the signal is inverted as it appears at the output. This is why this terminal is known as inverting. If the signal is applied at non-inverting input ( + ), it is amplified at the output without any change of phase (Fig. 18.24 b).
Fig. 18.24
Fig. 18.24
Fig. 18.25
Fig. 18.26

# (ii) Output

It is the resistance between the output terminal and ground (Fig. 18.26). Its value is only a few ohms.

## (iii) Open Loop Gain

It is the ratio of output voltage $V_{0}$ to the voltage difference between non-inverting and inverting inputs when there is no external connection between the output and the inputs (Fig. 18.27) i.e.,

$$
A_{\mathrm{OL}}=\frac{V_{0}}{V_{0}-V_{-}}=\frac{V_{0}}{V_{1}}
$$

Fig. 18.28

The open loop gain of the amplifier is very high. It is of the order of $10^{5}$.

# 18.8 OP-AMP AS INVERTING AMPLIFIER

Fig. 18.28 shows the circuit of an op-amp when used as an inverting amplifier. The input signal $V_{i n}$ which is to be amplified, is applied at inverting terminal (-) through a resistance $R_{1}, V_{n}$ is its output. The non-inverting terminal ( + ) is grounded, i.e., its potential is zero. We know that $A_{0 k}$ is $V_{n}$ very high, of the order of $10^{5}$. As $V_{n}$ may have any value between $+V_{c c}(+12 \mathrm{~V})$ and $-V_{c c}(-12 \mathrm{~V})$ so according to Eq.18.5, for finite ( $\pm 12 \mathrm{~V}$ ) value of $V_{n}, V_{n}-V_{n}=0$ or $V_{n}=V_{n}$. Since $V_{n}$ is at ground so $V_{1}$ is virtually at ground potential i.e., $V_{1}=0$. Referring to Fig. 18.28,

Current through $\quad R_{1}=I_{1}=\frac{V_{m}-V_{1}}{R_{1}}=\frac{V_{m}-0}{R_{1}}=\frac{V_{m}}{R_{1}}$
Current through $\quad R_{2}=I_{2}=\frac{V_{-}-V_{n}}{R_{2}}=\frac{0-V_{n}}{R_{2}}=-\frac{V_{n}}{R_{2}}$
As practically no current flows between $(-)$ and $(+)$ terminals, so according to Kirchhoff's current rule $\quad I_{1}=I_{2}$ or

$$
\frac{V_{m}}{R_{1}}=-\frac{V_{n}}{R_{2}} \quad \text { or } \quad \frac{V_{n}}{V_{m}}=-\frac{R_{2}}{R_{1}}
$$

As $V_{0} / V_{m}$ is defined as gain $G$ of the inverting amplifier, so

$$
G=-\frac{R_{2}}{R_{1}}
$$

The negative sign indicates that the output signal is $180^{\circ}$ out of phase with respect to input signal. It is interesting to note that the closed loop gain depends upon the two externally connected resistances $R_{1}$ and $R_{2}$. The gain is independent of what is happening inside the amplifier.
If $R_{1}=10 \mathrm{k} \Omega$ and $R_{2}=100 \mathrm{k} \Omega$, the gain of the amplifier is

$$
G=\frac{V_{m}}{V_{m}}=\frac{-R_{2}}{R_{1}}=\frac{-100 \Omega}{10 \mathrm{k} \Omega}=-10
$$