### 18.9 OP-AMP AS NON-INVERTING AMPLIFIER

The circuit diagram of op-amp as non-inverting amplified is shown in Fig. 18.29. In this case the input signal $V_{n}$ is applied at the non-inverting terminal ( + ). As explained earlier, due to high open loop gain of amplifier, the inverting (-) and non

inverting ( + ) inputs are virtually at the same potential. That is,

$$
V_{+}=V_{+}=V_{\text {in }}
$$

Also, from Fig.18.29,

$$
\begin{aligned}
& \text { Current through } R_{1}=I_{1}=\frac{0-V_{-}}{R_{1}}=\frac{0-V_{0}}{R_{1}}=\frac{-V_{\text {in }}}{R_{1}} \\
& \text { Current through } R_{2}=I_{2}=\frac{V_{-}-V_{0}}{R_{2}}=\frac{V_{0}-V_{0}}{R_{2}}
\end{aligned}
$$

As practically no current flows between (-) and (+) terminals, so by Kirchhoff's current rule

$$
I_{1}=I_{2}
$$

Hence

$$
\frac{-V_{0}}{R_{1}}=\frac{V_{0}-V_{0}}{R_{2}}
$$

or

$$
V_{n}\left(\frac{1}{R_{1}}+\frac{1}{R_{2}}\right)=\frac{V_{0}}{R_{2}}
$$

or

$$
\text { Gain }=\frac{V_{0}}{V_{\text {in }}}=1+\frac{R_{2}}{R_{1}}
$$

Again the gain of the amplifier is independent of the internal structure of the op-amp. It just depends upon the two externally connected resistances $R_{1}$ and $R_{2}$. The positive sign of gain indicates that the input and out put signals are in phase.
Example 18.2: Find the gain of the circuit as shown in Fig.18.30.

## Solution:

As the input signal $V_{\text {in }}$ is connected to non-inverting input $(+)$, so the op-amp acts as a non-inverting amplifier. Comparing it with the circuit of non-inverting amplifier as shown in Fig. 18.29, we have

$$
\begin{aligned}
R_{1} & =\text { infinity } \\
\therefore \quad \text { Gain } & =1+\frac{R_{2}}{R_{1}}=1
\end{aligned}
$$

and

## 18.10 OP-AMP AS A COMPARATOR

Op-amp usually requires two power supplies of equal voltage but of opposite polarity. Most op-amp operate with $V_{\mathrm{CC}}= \pm 12 \mathrm{~V}$ supply (Fig. 18.31).

## An op amplifier - The circuits in the black box.
Fig. 18.30
Fig. 18.31

Integrated circuit (IC) chips are manufactured on wafers of semiconductor material.
Fig. 18.33

As the open loop gain of the op-amp is very high ( $10^{7}$ ), even a very small potential difference between the inverting and noninverting inputs is amplified to such a large extent that the amplifier gets saturated, i.e., its output either becomes equal to $+V_{\mathrm{cc}}$ or $-V_{\mathrm{cc}}$. This feature of op-amp is used to compare two voltages. Fig. 18.32 shows the circuit of an op-amp used as
Fig. 18.32
comparator. $V_{R}$ is reference voltage which is connected with $(+)$ terminal and $V$ is the voltage which is to be compared with the reference $V_{R}$. It is connected with (-) terminal.
When
$V_{1}>V_{1}$ or $V>V_{R}$, then $V_{1}=-V_{c c}$
and if
$V_{1}<V_{1}$ or $V<V_{R}$, then $V_{1}=+V_{c c}$