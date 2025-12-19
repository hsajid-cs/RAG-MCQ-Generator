### 16.3 A.C. THROUGH A RESISTOR

Fig. 16.7 (a) shows a resistor of resistance $R$ connected with an alternating voltage source.
At any time $t$ the potential difference across the terminals of the resistor is given by

$$
V=V_{0} \sin \omega t
$$

where $V_{0}$ is the peak value of the alternating voltage. The current $/$ flowing through the circuit is given by Ohm's law

$$
\begin{aligned}
& i=\frac{V}{R}=\frac{V_{0}}{R} \sin \omega t \\
& i=I_{0} \sin \omega t
\end{aligned}
$$

or
where $i$ is the instantaneous current and $I_{0}=\frac{V_{0}}{R}$ is the
peak value of the current. It follows from Eqs. 16.5 and 16.6 that the instantaneous values of both voltage and current are sine functions which vary with time (Fig.16.7b). This figure shows that when voltage rises, the current also rises. If the voltage falls, the current also does so - both pass their maximum and minimum values at the same instant. Thus in a purely resistive A.C. circuit, instantaneous values of voltage and current are in phase. This behaviour is shown graphically in Fig. 16.7 (b) and vectorially in Fig. 16.7 (c).
Fig. 16.7 (c) shows $V$ and $I$ vectors for resistance. They are drawn parallel because there is no phase difference between them. The opposition to A.C. which the circuit

presents is the resistance

$$
R=\frac{V}{I}
$$

The instantaneous power in the resistance is given by

$$
P=I^{2} R=V I=V^{2} / R
$$

$P$ is in watts, $V$ is in volts, $I$ is in amperes and $R$ is in ohms. It is very important to note that the Eq. 16.8 holds only when the current and voltage are in phase.

# 16.4 A.C. THROUGH A CAPACITOR

Alternating current can flow through a resistor, but it is not obvious that how it can flow through a capacitor. This can be demonstrated by the circuit shown in Fig.16.8. A low power bulb is connected in series with a $1 \mu \mathrm{~F}$ capacitor to supply mains through a switch. When the switch is closed, the bulb lights up showing that the current is flowing through the capacitor. Direct current cannot flow through a capacitor continuously because of the presence of an insulating medium between the plates of the capacitor. Now let us see how does A.C. flows through a capacitor. The current flows because the capacitor plates are continuously charged, discharged and charged the other way round by the alternating voltage (Fig. 16.9 a). The basic relation between the charge $q$ on a capacitor and the voltage $V$ across its plates i.e. $q=C V$ holds at every instant. If $V=V_{0} \sin \omega t$ is the applied alternating voltage, the charge on the capacitor at any instant will be given by

$$
q=C V=C V_{0} \sin \omega t
$$

Fig. 16.8
(a)
(b)

Fig. 16.9

Referring to the Fig. 16.2 (b) it can be seen that the phase at $O$ is zero and the phase at the upper maximum is $\pi / 2$. So in Fig. 16.9 (b) the phase of $V$ at $O$ is zero but the current at this point is maximum so its phase is $\pi / 2$. Thus, the current is leading the applied voltage by $90^{\circ}$ or $\pi / 2$. Now consider the points $A$ and $N$. The phase of alternating voltage at $A$ is $\pi / 2$ but the phase of current at $N$ is $\pi$. Again the current is leading the voltage by $90^{\circ}$ or $\pi / 2$. Similarly by comparing the phase at the pair of points ( $B, R),(C, S)$ and $(D, T)$ it can be seen that at all these points the current leads the voltage by $90^{\circ}$ or $\pi / 2$. This is vectorially represented in Fig. 16.9 (c).
Reactance of a capacitor is a measure of the opposition offered by the capacitor to the flow of A.C. It is usually represented by $X_{\mathrm{C}}$. Its value is given by

$$
X_{\mathrm{C}}=\frac{V_{\mathrm{me}}}{I_{\mathrm{me}}}
$$

where $V_{\text {me }}$ is the rms value of the alternating voltage across the capacitor and $I_{\text {me }}$ is the rms value of current passing through the capacitor. The unit of reactance is ohm. In case of capacitor

$$
X_{\mathrm{C}}=\frac{1}{2 \pi f C}=\frac{1}{\omega C}
$$

According to Eq.16.11, a certain capacitor will have a large reactance at low frequency. So the magnitude of the opposition offered by it will be large and the current in the circuit will be small. On the other hand at high frequency, the reactance will be low and the high frequency current through the same capacitor will be large.
Example 16.2: A $100 \mu \mathrm{~F}$ capacitor is connected to an alternating voltage of 24 V and frequency 50 Hz . Calculate
(a) The reactance of the capacitor, and
(b) The current in the circuit

# Solution:

(a) Reactance of the capacitor $X_{\mathrm{C}}=\frac{1}{2 \pi f C}$

$$
=\frac{1}{2 \times 3.14 \times 50 \mathrm{~s}^{-1} \times 100 \times 10^{-6} \mathrm{~F}}
$$

$$
X_{\mathrm{C}}=31.8 \frac{\mathrm{~V}}{\mathrm{Cs}}=31.8 \Omega
$$

(b) From the equation $X_{C}=\frac{V_{\text {ma }}}{I_{\text {ma }}}$
or

$$
I_{\mathrm{ma}}=\frac{V_{\mathrm{ma}}}{X_{\mathrm{C}}} \frac{24 \mathrm{~V}}{31.8 \Omega}=0.75 \mathrm{~A}
$$

# 16.5 A.C. THROUGH AN INDUCTOR

An inductor is usually in the form of a coil or a solenoid wound from a thick wire so that it has a large value of self inductance and has a negligible resistance. We have already seen how self inductance opposes changes of current. So when an alternating source of voltage is applied across an inductor, it must oppose the flow of A.C. which is continuously changing (Fig. 16.10). Let us assume that the resistance of the coil is negligible. We can simplify the theory by considering first, the current and then finding the potential difference across the inductor which will cause this current. Suppose the current is . $I=I_{0} \sin 2 \pi f t$. If $L$ is the inductance of the coil, the changing current sets up a back emf in the coil of magnitude

$$
\varepsilon_{L}=L \frac{\Delta I}{\Delta t}
$$

To maintain the current, the applied voltage must be equal to the back e.m.f. The applied voltage across the coil must, therefore, be equal to

$$
V=L \frac{\Delta I}{\Delta t}
$$

Since $L$ is a constant, $V$ is proportional to $\frac{\Delta I}{\Delta t}$. Fig. 16.10 (b) shows how the current $I$ varies with time. The value of $\Delta / / \Delta t$ is given by the slope of the $I-t$ curve at the various instants of time. At $O$, the value of the slope is maximum, so the maximum value of $V$ equal to $V_{0}$ occurs at $O$ and is represented by OP (Fig. 16.10 b). From $O$ to $A$ the slope of $I-t$ graph decreases to zero so the voltage decreases form $V_{0}$ to zero at Q. From A to B, the slope of the $I-t$ graph is negative, so the voltage curve goes from $Q$ to $R$. In this way the voltage is represented by the curve PQRST corresponding to current curve OABCD. By comparing the phases of the pair of points $(\mathrm{O}, \mathrm{P}),(\mathrm{A}, \mathrm{Q}),(\mathrm{B}, \mathrm{R}),(\mathrm{C}, \mathrm{S})$ and $(\mathrm{D}, \mathrm{T})$, it can be seen that the phase of the current is always less than the phase of voltage by $90^{\circ}$ or $\pi / 2$ i.e., current lags behind the applied voltage by $90^{\circ}$ or $\pi / 2$ or the applied voltage leads the current by $90^{\circ}$ or $\pi / 2$.
Inductors are made in many sizes to perform a wide variety of functions in business and industry.

This is vectorially shown in Fig. 16.10(c) Inductive reactance is a measure of the opposition offered by the inductance coil to the flow ofA.C. It is usually denoted by $X_{L}$.

$$
X_{L}=\frac{V_{\mathrm{rms}}}{I_{\mathrm{rms}}}
$$

If $V_{\text {rms }}$ is rms value of the alternating voltage across an inductance and $I_{\mathrm{rms}}$, the rms value of the current passing through it, the value of $X_{L}$ is given by

$$
X_{L}=\frac{V_{\mathrm{rms}}}{I_{\mathrm{rms}}}=2 \pi f L=\omega L
$$

The reactance of a coil, therefore, depends upon the frequency of the A.C. and the inductance $L$. It is directly proportional to both $f$ and $L . L$ is expressed in henry, $f$ in hertz, and $X_{L}$ in ohms. It is to be noted that inductance and capacitance behave oppositely as a function of frequency. If $f$ is low $X_{L}$ is small but $X_{C}$ is large. For high $f, X_{L}$ is large but $X_{C}$ is small. The behaviour of resistance is independent of frequency.
Referring to Fig.16.10 (b), it can be seen that no power is dissipated in a pure inductor. In the first quarter of cycle both $V$ and $I$ are positive so the power is positive, which means energy is supplied to inductor. In the second quarter, $V$ is positive but $I$ is negative. Now power is negative which implies that energy is returned by the inductor. Again in third quarter, it receives energy but returns the same amount in the fourth quarter. Thus, there is no net change of energy in a complete cycle. Since an inductor coil does not consume energy, the coil is often employed for controlling A.C. without consumption of energy. Such an inductance coil is known as choke.