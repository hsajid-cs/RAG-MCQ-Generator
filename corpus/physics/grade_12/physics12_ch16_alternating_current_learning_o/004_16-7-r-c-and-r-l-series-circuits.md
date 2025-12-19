### 16.7 R-C AND R-L SERIES CIRCUITS

Consider a series network of resistance $R$ and a capacitor $C$ excited by an alternating voltage (Fig.16.11 a). As $R$ and $C$ are in series, the same current would flow through each of them. If $I_{\text {mix }}$ is the value of current, the potential difference across the resistance $R$ would be $I_{\text {mix }} R$ and it would be in phase with current $I_{\text {mix }}$. The vector diagram of the voltage and current is shown in Fig. 16.11 (b). Taking the current as reference, the potential difference $I_{\text {mix }} R$ across the resistance is represented by a line along the current line because potential drop $I_{\text {mix }} R$ is in phase with current. The potential difference across the capacitor will be $I_{\text {mix }} X_{c}=I_{\text {mix }} / \omega C$. As this voltage lags the current by $90^{\circ}$, so the line representing the vector $I_{\text {mix }} / \omega C$ is drawn at right angles to the current line (Fig. 16.11 b).
The applied voltage $V_{\text {mix }}$ that will send the current $I$ in the circuit is obtained by the resultant of the vectors $I_{\text {mix }} R$ and $\frac{I_{\text {mix }}}{\omega C}$ i.e.,

$$
\begin{aligned}
& V_{\text {mix }}=\sqrt{\left(I_{\text {mix }} R\right)^{2}+\left(\frac{I_{\text {mix }}}{\omega C}\right)^{2}} \\
& V_{\text {mix }}=I_{\text {mix }} \sqrt{R^{2}+\left(\frac{1}{\omega C}\right)^{2}}
\end{aligned}
$$

Impedance $Z=\frac{V_{\text {mix }}}{I_{\text {mix }}}=\sqrt{R^{2}+\frac{1}{(\omega C)^{2}}}$
(a)
(b)

Fig 16.11

$$
\theta=\tan ^{-1}\left(\frac{1}{\omega C R}\right)
$$

Eq.16.15 suggests that we can find the impedance of a series A.C. circuit by vector addition. The resistance $R$ is represented by a horizontal line in the direction of current which is taken as reference. The reactance $X_{C}=\frac{1}{\omega C}$ is shown by a line lagging the $\mathbf{R}$ - line by $90^{\circ}$ (Fig.16.11 c). The impedance $\mathbf{Z}$ of the circuit is obtained by the vector summation of resistance and reactance. Fig.16.11 (c) is known as impedance diagram of the circuit. The angle which the line representing the impedance $\mathbf{Z}$ makes with $\mathbf{R}$ line gives the phase difference between the voltage and current. In Fig.16.11(c), the current is leading the voltage applied by an angle

$$
\theta=\tan ^{-1}\left(\frac{X_{C}}{R}\right)=\tan ^{-1}\left(\frac{1}{\omega C R}\right)
$$

Now we will calculate the impedance of a $R-L$ series circuit by drawing its impedance diagram. Fig.16.12 (a) shows an $R-L$ series circuit excited by an A.C. source of frequency $\omega$. The current is taken as reference, so it is represented by a horizontal line. Resistance $R$ is drawn along this line because the potential drop $I_{\text {mix }} R$ is in phase with current. As the potential across the inductance $V_{L}=I_{\text {mix }} X_{L}=I_{\text {mix }}(\omega L)$ leads the current by $90^{\circ}$, so the vector line of reactance $X_{L}=\omega L$ is drawn at right angle to $R$ line (Fig. 16.12 b). The impedance $Z$ of the circuit is obtained by the vector sum of $R$ and $\omega L$ lines. Thus

$$
Z=\sqrt{R^{2}+(\omega L)^{2}}
$$

The angle $\theta=\tan ^{-1} \frac{\omega L}{R}$ which $Z$ makes with $R$ line gives the phase difference between the applied voltage and current. In this case the voltage leads the current by $\theta^{\circ}$. By comparing the impedance diagrams of $R-C$ and $L-R$ circuits, it can be seen that the vector lines of reactances $X_{C}$ and $X_{L}$ are directed opposite to each other with $R$ as reference.

# 16.8 POWER IN A.C. CIRCUITS

The expression for power is $P=V_{\text {mix }} I_{\text {mix }}$. This expression is true in case of A.C. circuits, only when $V$ and $I$ are in phase as in

case of a purely resistive circuit. We have already seen that the power dissipation in a pure inductive or in a pure capacitance circuit is zero. In these cases the current lags or leads the applied voltage by $90^{\circ}$ and component of applied voltage vector $V$ along the current vector is zero (Fig. 16.9 c and 16.10 c ). In A.C. circuit the phase difference between applied voltage $V$ and the current $I_{\text {mix }}$ is $\theta$ (Fig. 16.11 b and 16.12 b ). The component of $\mathbf{V}$ along current $I_{\text {mix }}$ is $V_{\text {mix }} \cos \theta$. Actually it is this component of voltage vector which is in phase with current. So the power dissipated in A.C. circuit

$$
P=I_{\mathrm{mix}} \times V_{\mathrm{mix}} \cos \theta
$$

The factor $\cos \theta$ is known as power factor.
Example 16.4: At what frequency will an inductor of 1.0 H have a reactance of $500 \Omega$ ?

# Solution:

$$
\begin{gathered}
L=1.0 \mathrm{H} \quad, \quad X_{\mathrm{L}}=500 \Omega \\
X_{\mathrm{L}}=\omega L=2 \pi f L=500 \Omega \\
f=\frac{500 \Omega}{2 \pi L}=\frac{500 \Omega}{2 \pi \times 1.0 \mathrm{H}}=80 \mathrm{~Hz}
\end{gathered}
$$

Example 16.5: An iron core coil of 2.0 H and $50 \Omega$ is placed in series with a resistance of $450 \Omega$. An A.C. supply of 100 V , 50 Hz is connected across the circuit. Find (i) the current flowing in the coil, (ii) phase angle between the current and voltage.

## Solution:

Resistance $=R=50 \Omega+450 \Omega=500 \Omega$
Inductance $=L=2.0 \mathrm{H}$
Supply voltage $=V_{\text {mix }}=100 \mathrm{~V}$
Frequency $=f=50 \mathrm{~Hz}$
The reactance $=X_{\mathrm{L}}=\omega L=2 \pi f L$

$$
=2 \times 3.14 \times 50 \mathrm{~s}^{-1} \times 2.0 \mathrm{H}=628 \Omega
$$

Impedance $=Z=\sqrt{R^{2}+(\omega L)^{2}}$

$$
=\sqrt{(500 \Omega)^{2}+(628 \Omega)^{2}}=803 \Omega
$$

Current $I_{\text {mix }}=\frac{V_{\text {mix }}}{Z}=\frac{100 \mathrm{~V}}{803 \Omega}=0.01245 \mathrm{~A}=12.45 \mathrm{~mA}$
Phase difference $\theta=\tan ^{-1}\left(\frac{\omega L}{R}\right)$

$$
=\tan ^{-1}\left(\frac{628 \Omega}{500 \Omega}\right)=51.5^{\circ}
$$

Example 16.6: A circuit consists of a capacitor of $2 \mu \mathrm{~F}$ and a resistance of $1000 \Omega$ connected in series. An alternating voltage of 12 V and frequency 50 Hz is applied. Find (i) the current in the circuit, and (ii) the average power supplied.

# Solution:

Resistance $=R=1000 \Omega$
Capacitance $=C=2 \mu \mathrm{~F}=2 \times 10^{-6} \mathrm{~F}$
Frequency $=f=50 \mathrm{~Hz}$
Reactance $=X_{\mathrm{C}}=\frac{1}{2 \pi f C}$

$$
=\frac{1}{2 \times 3.14 \times 50 \mathrm{~s}^{-1} \times 2 \times 10^{-6} \mathrm{~F}}=1592 \Omega
$$

Impedance $=Z=\sqrt{R^{2}+\left(X_{\mathrm{C}}\right)^{2}}$

$$
=\sqrt{(1000 \Omega)^{2}+(1592 \Omega)^{2}}=1880 \Omega
$$

Current $=I_{\text {me }}=\frac{V_{\text {me }}}{Z}=\frac{12 \mathrm{~V}}{1880 \Omega}=0.0064 \mathrm{~A}=6.4 \mathrm{~mA}$
Phase Difference $\theta=\tan ^{-1} \frac{X_{\mathrm{C}}}{R}=\tan ^{-1}\left(\frac{1592 \Omega}{1000 \Omega}\right)=57.87^{\circ}$
Average power $=V_{\text {me }} I_{\text {me }} \cos \theta$

$$
=12 \mathrm{~V} \times 0.0064 \mathrm{~A} \times 0.532=0.04 \mathrm{~W}
$$