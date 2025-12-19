### 13.7 ELECTRICAL POWER AND POWER DISSIPATION IN RESISTORS

Consider a circuit consisting of a battery $E$ connected in series with a resistance $R$ (Fig. 13.16). A steady current $I$ flows through the circuit and a steady potential difference $V$ exists between the terminals $A$ and $B$ of the resistor $R$. Terminal A, connected to the positive pole of the battery, is at a higher potential than the terminal B. In this circuit the battery is continuously lifting charge uphill through the potential difference $V$. Using the meaning of potential difference, the work done in moving a charge $\Delta Q$ up through the potential difference $V$ is given by

$$
\text { Work done }=\Delta W=V \times \Delta Q \ldots \ldots(13.12)
$$

This is the energy supplied by the battery. The rate at which the battery is supplying electrical energy is the power output or electrical power of the battery. Using the definition of power we have

$$
\text { Electrical power }=\frac{\text { Energy supplied }}{\text { Time taken }}=V \frac{\Delta Q}{\Delta t}
$$

Since

$$
I=\frac{\Delta Q}{\Delta t}, s o
$$

Electrical power $=V \times I$
Eq. 13.12a is a general relation for power delivered from a source of current $I$ operating on a voltage $V$. In the circuit shown in Fig.13.16 the power supplied by the battery is expended or dissipated in the resistor $R$. The principle of conservation of energy tells us that the power dissipated in the resistor is also given by Eq. 13.12.3

$$
\text { Power dissipated }(P)=V \times I
$$

Alternative equation for calculating power can be found by substituting $V=I R, I=V / R$ in turn in Eq. 13.13

$$
\begin{aligned}
& P=V \times I=I R \times I=I^{2} R \\
& P=V \times I=V \times \frac{V}{R}=\frac{V^{2}}{R}
\end{aligned}
$$

Thus we have three equations for calculating the power dissipated in a resistor.

$$
P=V \times I, \quad P=I^{2} R, \quad P=\frac{V^{2}}{R}
$$

If $V$ is expressed in volts and $I$ in amperes, the power is expressed in watts.

# 13.8 ELECTROMOTIVE FORCE (EMF) AND POTENTIAL DIFFERENCE

We know that a source of electrical energy, say a cell or a battery, when connected across a resistance maintains a steady current through it (Fig. 13.17). The cell continuously supplies energy which is dissipated in the resistance of the circuit. Suppose when a steady current has been established in the circuit, a charge $\Delta Q$ passes through any cross section of the circuit in time $\Delta t$. During the course of motion, this charge enters the cell at its low potential end and leaves at its high potential end. The source must supply energy $\Delta W$ to the positive charge to force it to go to the point of high potential. The emf $E$ of the source is defined as the energy supplied to unit charge by the cell.
i.e

$$
E=\frac{\Delta W}{\Delta Q}
$$

Fig. 13.17 Electromotive force of a cell.

It may be noted that electromotive force is not a force and we do not measure it in newtons. The unit of emf is joule/coulomb which is volt (V).
The energy supplied by the cell to the charge carriers is derived from the conversion of chemical energy into electrical energy inside the cell.
Like other components in a circuit a cell also offers some resistance. This resistance is due to the electrolyte present between the two electrodes of the cell and is called the internal resistance $r$ of the cell. Thus a cell of emf $E$ having an internal resistance $r$ is equivalent to a source of pure emf $E$ with a resistance rin series as shown in Fig. 13.18.
Let us consider the performance of a cell of emf $E$ and internal resistance $r$ as shown in Fig. 13.19. A voltmeter of infinite resistance measures the potential difference across the external resistance $R$ or the potential difference $V$ across the terminals of the cell. The current / flowing through the circuit is given by

$$
I=\frac{E}{R+r}
$$

or

$$
E=I R+I r
$$

Here $I R=V$ is the terminal potential difference of the cell in the presence of current $I$. When the switch $S$ is open, no current passes through the resistance. In this case the voltmeter reads the emf $E$ as terminal voltage. Thus terminal voltage in the presence of the current (switch on) would be less than the emf $E$ by $/ r$.
Let us interpret the Eq. 13.16 on energy considerations. The left side of this equation is the emf $E$ of the cell which is equal to energy gained by unit charge as it passes through the cell from its negative to positive terminal. The right side of the equation gives an account of the utilization of this energy as the current passes the circuit. It states that, as a unit charge passes through the circuit, a part of this energy equal to $I$ is dissipated into the cell and the rest of the energy is dissipated into the external resistance $R$. It is given by potential drop $I R$. Thus the emf gives the energy supplied to unit charge by the cell and the potential drop across the various elements account for the dissipation of this energy into other forms as the unit charge passes through these elements.
The emf is the "cause" and potential difference is its "effect". The emf is always present even when no current is drawn

through the battery or the cell, but the potential difference across the conductor is zero when no current flows through it.
Example 13.4: The potential difference between the terminals of a battery in open circuit is 2.2 V . When it is connected across a resistance of $5.0 \Omega$, the potential falls to 1.8 V . Calculate the current and the internal resistance of the battery.

# Solution:

Given $E=2.2 \mathrm{~V}, \quad R=5.0 \Omega, \quad V=1.8 \mathrm{~V}$
We are to calculate $/$ and $r$.
We have

$$
V=1 R
$$

or

$$
I=\frac{V}{R}=\frac{1.8 \mathrm{~V}}{5.0 \Omega}=0.36 \mathrm{~A}
$$

Internal resistance $r$ can be calculated by using

$$
\begin{aligned}
& E=V+1 r \\
& 2.2 \mathrm{~V}=1.8 \mathrm{~V}+0.36 \mathrm{Ax} r \\
& \text { or } \\
& r=1.11 \mathrm{VA}=1.11 \Omega
\end{aligned}
$$

## Maximum Power Output

In the circuit of Fig. 13.19, as the current / flows through the resistance $R$, the charges flow from a point of higher potential to a point of lower potential and as such, they loose potential energy. If $V$ is the potential difference across $R$, the loss of potential energy per second is $V I$. This loss of energy per second appears in other forms of energy and is known as power delivered to $R$ by current $I$.
$\therefore \quad$ Power delivered to $R=P_{\text {out }}=V I$

$$
=I^{2} R \quad(\because \quad V=I R)
$$

As

$$
I=\frac{E}{R+r}
$$

$$
P_{\text {out }}=\frac{E^{2} R}{(R+r)^{2}}=\frac{E^{2} R}{(R-r)^{2}+4 R r}
$$

when $R=r$, the denominator of the expression of $P_{\text {out }}$ is least and so $P_{\text {out }}$ is then a maximum. Thus we see that maximum power is delivered to a resistance (load), when the internal resistance of the source equals the load resistance. The

## A voltmeter connected across the terminals of a cell measures (a) the emf of the cell on open circuit, (b) the terminal potential difference on a closed circuit.

value of this maximum output power as given by Eq. 13.17 is $\frac{E^{2}}{4 R}$

# 13.9 KIRCHHOFF'S RULES

Ohm's law and rules of series and parallel combination of resistance are quite useful to analyze simple electrical circuits consisting of more than one resistance. However such a method fails in the case of complex networks consisting of a number of resistors, and a number of voltage sources. Problems of such networks can be solved by a system of analysis, which is based upon two rules, known as Kirchhoff's rules.

## Kirchhoff's First Rule

It states that the sum of all the currents meeting at a point in the circuit is zero i.e.,

$$
\Sigma I=0
$$

It is a convention that a current flowing towards a point is taken as positive and that flowing away from a point is taken as negative.
Consider a situation where four wires meet at a point $A$ (Fig. 13.20). The currents flowing into the point $A$ are $I_{1}$ and $I_{2}$ and currents flowing away from the point are $I_{3}$ and $I_{4}$. According to the convention currents $I_{1}$ and $I_{2}$ are positive and currents $I_{3}$ and $I_{4}$ are negative. Applying Eq. 13.18 we have

$$
I_{1}+I_{2}+\left(-I_{3}\right)+\left(-I_{4}\right)=0
$$

or

$$
I_{1}+I_{2}=I_{3}+I_{4}
$$

Using Eq. 13.19 Kirchhoff's first rule can be stated in other words as

The sum of all the currents flowing towards a point is equal to the sum of all the currents flowing away from the point.

Kirchhoff's first rule which is also known as Kirchhoff's point rule is a manifestation of law of conservation of charge. If there is no sink or source of charge at a point, the total charge flowing towards the point must be equal to the total charge flowing away from it.

# Kirchhoff's Second Rule

It states that the algebraic sum of voltage changes in a closed circuit or a loop must be equal to zero. Consider a closed circuit shown in Fig. 13.21. The direction of the current / flowing through the circuit depends on the cell having the greater emf. Suppose $E_{1}$ is greater than $E_{2}$, so the current flows in counter clockwise direction (Fig. 13.21). We know that a steady current is equivalent to a continuous flow of positive charges through the circuit. We also know that a voltage change or potential difference is equal to the work done on a unit positive charge or energy gained or lost by it in moving from one point to the other. Thus when a positive charge $\Delta Q$ due to the current $I$ in the closed circuit (Fig. 13.21), passes through the cell $E_{1}$ from low (-ve) to high potential ( +ve), it gains energy because work is done on it. Using Eq. 13.12 the energy gain is $E_{1} \Delta Q$. When the current passes through the cell $E_{2}$ it loses energy equal to $-E_{2} \Delta Q$ because here the charge passes from high to low potential. In going through the resistor $R_{1}$, the charge $\Delta Q$ loses energy equal to $-I R_{1} \Delta Q$ where $I R_{1}$ is potential difference across $R_{1}$. The minus sign shows that the charge is passing from high to low potential. Similarly the loss of energy while passing through the resistor $R_{2}$ is $-I R_{2} \Delta Q$. Finally the charge reaches the negative terminal of the cell $E_{1}$ from where we started. According to the law of conservation of energy the total change in energy of our system is zero. Therefore, we can write

$$
E_{1} \Delta Q-I R_{1} \Delta Q-E_{2} \Delta Q-I R_{2} \Delta Q=0
$$

$$
\text { or } \quad E_{1}-I R_{1}-E_{2}-I R_{2}=0
$$

which is Kirchhoff's second rule and it states that

## The algebraic sum of potential changes in a closed circuit is zero.

We have seen that this rule is simply a particular way of stating the law of conservation of energy in electrical problems.

Before applying this rule for the analysis of complex network it is worthwhile to thoroughly understand the rules for finding the potential changes.

(i) If a source of emf is traversed from negative to positive terminal, the potential change is positive, it is negative in the opposite direction.
(ii) If a resistor is traversed in the direction of current, the change in potential is negative, it is positive in the opposite direction.
Example 13.6: Calculate the currents in the three resistances of the circuit shown in Fig. 13.22.

# Solution:

First we select two loops abcda and ebcfe. The choice of loops is quite arbitrary, but it should be such that each resistance is included at least once in the selected loops.
After selecting the loops, suppose a current $I_{1}$ is flowing in the first loop and $I_{2}$ in the second loop, all flowing in the same sense. These currents are called loop currents. The actual currents will be calculated with their help. It should be noted that the sense of the current flowing in all loops should essentially be the same. It may be clockwise or anticlockwise. Here we have assumed it to be clockwise (Fig. 13.22).
We now apply Kirchhoff's second rule to obtain the equations required to calculate the currents through the resistances. We first consider the loop abcda. Starting at a point 'a' we follow the loop clockwise. The voltage change while crossing the battery $E_{1}$ is $-E_{1}$ because the current flows through it from positive to negative. The voltage change across $R_{1}$ is $-I_{1} R_{1}$. The resistance $R_{2}$ is common to both the loops $I_{1}$ and $I_{2}$ therefore, the currents $I_{1}$ and $I_{2}$ simultaneously flow through it. The directions of currents $I_{1}$ and $I_{2}$ as flowing through $R_{2}$ are opposite, so we have to decide that which of these currents is to be assigned a positive sign. The convention regarding the sign of the current is that if we are applying the Kirchhoffs second rule in the first loop, then the current of this loop i.e, $I_{1}$ will be assigned a positive sign and all currents, flowing opposite to $I_{1}$ have a negative sign. Similarly, while applying Kirchhoffs second rule in the second loop, the current $I_{2}$ will be considered as positive and $I_{1}$ as negative. Using this convention the current flowing through $R_{2}$ is $\left(I_{1}-I_{2}\right)$ and the voltage change across is - $\left(I_{1}-I_{2}\right) R_{2}$. The voltage change across the battery $E_{2}$ is $E_{2}$. Thus the Kirchhoffs second rule as applied to the loop abcda gives

$$
-E_{1}-I_{1} R_{1}-\left(I_{1}-I_{2}\right) R_{2}+E_{2}=0
$$

Substituting the values, we have

$$
\begin{aligned}
& -40 \mathrm{~V}-I_{1} \times 10 \Omega-\left(I_{1}-I_{2}\right) \times 30 \Omega+60 \mathrm{~V}=0 \\
& 20 \mathrm{~V}-10 \Omega \times\left[I_{1}+3\left(I_{1}-I_{2}\right)\right]=0 \\
& 4 I_{1}-3 I_{2}=2 \mathrm{~V} \Omega^{-1}=2 \mathrm{~A}
\end{aligned}
$$

Similarly applying Kirchhoff's second rule to the loop ebcfe, we get

$$
-E_{2}-\left(I_{2}-I_{1}\right) R_{2}-I_{2} R_{1}+E_{2}=0
$$

Substituting the values, we have

$$
\begin{aligned}
& -60 \mathrm{~V}-\left(I_{2}-I_{1}\right) \times 30 \Omega-I_{2} \times 15 \Omega+50 \mathrm{~V}=0 \\
& -10 \mathrm{~V}-15 \Omega \times\left[I_{2}+2\left(I_{2}-I_{1}\right)\right]=0 \\
& 6 I_{1}-9 I_{2}=2 \mathrm{~V} \Omega^{-1}=2 \mathrm{~A}
\end{aligned}
$$

Solving Eq. 13.21 and Eq. 13.22 for $I_{1}$ and $I_{2}$, we get

$$
I_{1}=\frac{2}{3} \mathrm{~A} \text { and } \quad I_{2}=\frac{2}{9} \mathrm{~A}
$$

Knowing the values of loop currents $I_{1}$ and $I_{2}$ the actual current flowing through each resistance of the circuit can be determined. Fig. 13.22 shows that $I_{1}$ and $I_{2}$ are the actual currents through the resistances $R_{1}$ and $R_{2}$. The actual current through $R_{2}$ is the difference of $I_{1}$ and $I_{2}$ and its direction is along the larger current. Thus

The current through $R_{1}=I_{1}=\frac{2}{3} \mathrm{~A}=0.66 \mathrm{~A}$ flowing in the direction of $I_{1}$ i.e., from a to d.

The current through $R_{2}=I_{1}-I_{2}=\frac{2}{3} \mathrm{~A}-\frac{2}{9} \mathrm{~A}=0.44 \mathrm{~A}$ flowing in the direction of $I_{1}$ i.e., from c to b.

The current through $R_{3}=I_{2}=\frac{2}{9} \mathrm{~A}=0.22 \mathrm{~A}$ flowing in the direction of $I_{1}$ i.e., from $f$ to e.

# Procedure of Solution of Circuit Problems

After solving the above problem we are in a position to apply the same procedure to analyse other direct current complex networks. While using Kirchhoff's rules in other problems, it is worthwhile to follow the approach given below:
(i) Draw the circuit diagram.
(ii) The choice of loops should be such that each resistance is included at least once in the selected loops.

Fig. 13.23 Wheatstone bridge circuit
(iii) Assume a loop current in each loop, all the loop currents should be in the same sense. It may be either clockwise or anticlockwise.
(iv) Write the loop equations for all the selected loops. For writing each loop equation the voltage change across any component is positive if traversed from low to high potential and it is negative if traversed from high to low potential.
(v) Solve these equations for the unknown quantities.

# 13.9 WHEATSTONE BRIDGE

The Wheatstone bridge circuit shown in Fig. 13.23 consists of four resistances $R_{1}, R_{2}, R_{3}$ and $R_{4}$ connected in such a way so as to form a mesh ABCDA. A battery is connected between points $A$ and $C$. A sensitive galvanometer of resistance $R_{5}$ is connected between points $B$ and $D$. If the switch $S$ is closed, a current will flow through the galvanometer. We are to determine the condition under which no current flows through the galvanometer even after the switch is closed. For this purpose we analyse this circuit using Kirchhoff's second rule. We consider the loops ABDA, BCDB and ADCA and assume anticlockwise loop currents $I_{1}, I_{2}$ and $I_{3}$ through the loops respectively. The Kirchhoff's second rule as applied to loopABDAgives

$$
-I_{1} R_{1}-\left(I_{1}-I_{2}\right) R_{2}-\left(I_{1}-I_{3}\right) R_{3}=0
$$

Similarly by applying the Kirchhoff's second rule to loop -BCDB we have

$$
-I_{2} R_{2}-\left(I_{2}-I_{3}\right) R_{4}-\left(I_{2}-I_{1}\right) R_{5}=0
$$

The current flowing through the galvanometer will be zero if, $I_{1}-I_{2}=0$ or $I_{1}=I_{2}$. With this condition Eq. 13.23 and Eq. 13.24 reduce to

$$
\begin{aligned}
& -I_{1} R_{1}=\left(I_{1}-I_{3}\right) R_{4} \\
& -I_{1} R_{2}=\left(I_{2}-I_{3}\right) R_{4}
\end{aligned}
$$

Dividing Eq. 13.25 by Eq. 13.26

$$
\frac{R_{1}}{R_{2}}=\frac{R_{3}}{R_{4}}
$$

Thus whenever the condition of Eq. 13.27 is satisfied, no current flows through the galvanometer and it shows no deflection, or conversely when the galvanometer in the Wheatstone bridge circuit shows no deflection, Eq. 13.27 is satisfied.

If we connect three resistances $R_{1}, R_{2}$ and $R_{3}$ of known adjustable values and a fourth resistance $R_{4}$ of unknown value and the resistances $R_{1}, R_{2}$ and $R_{3}$ are so adjusted that the galvanometer shows no deflection then, from the known resistances $R_{1}, R_{2}$ and $R_{3}$ the unknown resistance $R_{4}$ can be determined by using Eq. 13.27.

# 13.10 POTENTIOMETER

Potential difference is usually measured by an instrument called a voltmeter. The voltmeter is connected across the two points in a circuit between which potential difference is to be measured. It is necessary that the resistance of the voltmeter be large compared to the circuit resistance across which the voltmeter is connected. Otherwise an appreciable current will flow through the voltmeter which will alter the circuit current and the potential difference to be measured. Thus the voltmeter can read the correct potential difference only when it does not draw any current from the circuit across which it is connected. An ideal voltmeter would have an infinite resistance.
However, there are some potential measuring instruments such as digital voltmeter and cathode ray oscilloscope which practically do not draw any current from the circuit because of their large resistance and are thus very accurate potential measuring instruments. But these instruments are very expensive and are difficult to use. A very simple instrument which can measure and compare potential differences accurately is a potentiometer.
A potentiometer consists of a resistor $R$ in the form of a wire on which a terminal $C$ can slide (Fig. 13.24 a). The resistance between $A$ and $C$ can be varied from 0 to $R$ as the sliding contact $C$ is moved from $A$ to $B$. If a battery of emf $E$ is connected across $R$ (Fig. 13.24 b), the current flowing through it is $I=E / R$. If we represent the resistance between $A$ and $C$ by $r$, the potential drop between these points will be $r I=r E / R$. Thus as $C$ is moved from $A$ to $B, r$ varies from 0 to $R$ and the potential drop between $A$ and $C$ changes from 0 to $E$. Such an arrangement also known as potential divider can be used to measure the unknown emf of a source by using the circuit shown in Fig. 13.25. Here $R$ is in the form of a straight wire of uniform area of cross section. A source of potential, say a cell whose emf $E$, is to be measured, is connected between $A$ and the sliding contact $C$ through a galvanometer G. It should be noted that the positive terminal of $E$, and that of
Fig. 13.24
Fig. 13.25
the potential divider are connected to the same point $A$. If, in

the loop AGCA, the point $C$ and the negative terminal of $E_{1}$ are at the same potential then the two terminals of the galvanometer will be at the same potential and no current will flow through the galvanometer. Therefore, to measure the potential $E_{1}$, the position of $C$ is so adjusted that the galvanometer shows no deflection. Under this condition, the emf $E_{1}$ of the cell is equal to the potential difference between $A$ and $C$ whose value $E r / R$ is known. In case of a wire of uniform cross section, the resistance is proportional to the length of the wire. Therefore, the unknown emf is also given by

$$
E_{1}=E \frac{r}{R}=E \frac{l}{L}
$$

where $L$ is the total length of the wire $A B$ and $l$ is its length from $A$ to $C$, after $C$ has been adjusted for no deflection. As the maximum potential that can be obtained between $A$ and $C$ is $E$, so the unknown emf $E_{1}$ should not exceed this value, otherwise the null condition will not be obtained. It can be seen that the unknown emf $E_{1}$ is determined when no current is drawn from it and therefore, potentiometer is one of the most accurate methods for measuring potential.
The method for measuring the emf of a cell as described above can be used to compare the emfs $E_{1}$ and $E_{2}$ of two cells. The balancing lengths $t_{1}$ and $t_{2}$ are found separately for the two cells. Then,

$$
E_{1}=E \frac{t_{1}}{L} \text { and } E_{2}=E \frac{t_{2}}{L}
$$

Dividing these two equations, we get

$$
\frac{E_{1}}{E_{2}}=\frac{t_{1}}{t_{2}}
$$

So the ratio of the emfs is equal to ratio of the balancing lengths.

# SUMMARY

- The electric current is said to be caused by the motion of electric charge.
- The heat energy $H$ produced by a current $I$ in the wire of resistance $R$ during a time interval $t$ is given by $H=I^{2} R t$
- The passage of current is always accompanied by a magnetic field in the surrounding space.

- Certain liquids conduct electricity due to some chemical reaction that takes place within them. The study of this process is known as electrolysis.
- The potential difference $V$ across the ends of a conductor is directly proportional to the current / flowing through it provided the physical state such as temperature etc. of the conductor remains constant.
- The fractional change in resistance per kelvin is known as temperature coefficient of resistance.
- A thermistor is a heat sensitive resistor. Most thermistors have negative temperature coefficient of resistance.
- Electrical power $P=V I=I^{2} R=\frac{V^{2}}{R}$
- The emf $E$ of the source is the energy supplied to unit charge by the cell.
- The sum of all the currents meeting at a point in a circuit is zero is the Kirchhoff's first rule.
- The algebraic sum of potential changes in a closed circuit is zero is known as Kirchhoff's second rule.

# QUESTIONS

13.1 A potential difference is applied across the ends of a copper wire. What is the effect on the drift velocity of free electrons by
(i) increasing the potential difference
(ii) decreasing the length and the temperature of the wire
13.2 Do bends in a wire affect its electrical resistance? Explain.
13.3 What are the resistances of the resistors given in the figures $A$ and $B$ ? What is the tolerance of each? Explain what is meant by the tolerance?
13.4 Why does the resistance of a conductor rise with temperature?
13.5 What are the difficulties in testing whether the filament of a lighted bulb obeys Ohm's law?

13.6 Is the filament resistance lower or higher in a $500 \mathrm{~W}, 220 \mathrm{~V}$ light bulb than in a 100 W , 220 V bulb?
13.7 Describe a circuit which will give a continuously var. ing potential.
13.8 Explain why the terminal potential difference of a battery decreases when the current drawn from it is increased?
13.9 What is Wheatstone bridge? How can it be used to determine an unknown resistance?

# PROBLEMS

13.1 How many electrons pass through an electric buic in one minute if the 300 mA current is passing through it?
(Ans: $1.12 \times 10^{30}$ )
13.2 A charge of 90 C passes through a wire in 1 hour and 15 minutes. What is the current in the wire?
(Ans: 20 mA )
13.3 Find the equivalent resistance of the circuit (Fig.P.13.3), total current drawn from the source and the current through each resistor.
Fig. P. 13.3
(Ans: $6.0 \Omega, 1.0 \mathrm{~A}, 0.5 \mathrm{~A}, 0.5 \mathrm{~A}, 1.0 \mathrm{~A}$ )
13.4 A rectangular bar of iron is 2.0 cm by 2.0 cm in cross section and 40 cm long. Calculate its resistance if the resistivity of iron is $11 \times 10^{-4} \Omega \mathrm{~m}$.
(Ans: $1.1 \times 10^{-4} \Omega$ )
13.5 The resistance of an iron wire at $0^{\circ} \mathrm{C}$ is $1 \times 10^{4} \Omega$. What is the resistance at $500^{\circ} \mathrm{C}$ if the temperature coefficient of resistance of iron is $5.2 \times 10^{-3} \mathrm{~K}^{-1}$ ?
(Ans: $3.6 \times 10^{4} \Omega$ )
13.6 Calculate terminal potential difference of each of cells in circuit of Fig. P.13.6.
Fig.P. 13.6
(Ans: $23.8 \mathrm{~V}, 7.8 \mathrm{~V}$ )

13.7 Find the current which flows in all the resistances of the circuit of Fig. P.13.7.
Fig. P. 13.7
(Ans: 1.25 A, 0.5 A)
13.8 Find the current and power dissipated in each resistance of the circuit, shown in Fig. P.13.8.
Fig.P. 13.8
(Ans: $0.8 \mathrm{~A}, 1.4 \mathrm{~A}, 2.2 \mathrm{~A}, 0.64 \mathrm{~W}, 1.96 \mathrm{~W}, 3.92 \mathrm{~W}, \& 9.68 \mathrm{~W}$ )