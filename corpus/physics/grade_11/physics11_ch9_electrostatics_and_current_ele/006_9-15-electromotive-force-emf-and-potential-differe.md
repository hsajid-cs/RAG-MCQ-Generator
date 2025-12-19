### 9.15 ELECTROMOTIVE FORCE (EMF) AND POTENTIAL DIFFERENCE

We know that a source of electrical energy, say a cell or a battery, when connected across a resistance, maintains a steady current through it Fig. 9.25. The cell

continuously supplies energy which is dissipated in the resistance of the circuit. Suppose when a steady current has been established in the circuit, a charge $Q$ passes through any cross-section of the circuit in time $t$. During the course of motion, this charge enters the cell at its low potential end and leaves at its high potential end. The source must supply energy $W$ to the positive charge to compel it to go to the point of high potential. The emf $E$ of the source is defined as the energy supplied to unit charge by the cell.
i.e.,

$$
E=\frac{W}{Q}
$$

Fig. 9.25: Electromotive force of a cell

It may be noted that electromotive force is not a force and we do not measure it in newtons. The unit of emf is joule/coulomb which is volt (V). The energy supplied by the cell to the charge carriers is derived from the conversion of chemical energy into electrical energy inside the cell.
Like other components in a circuit, a cell also offers some resistance. This resistance is due to the electrolyte present between the two electrodes of the cell and is called the internal resistance of the cell. Thus, a cell of emf $E$ having an internal resistance $r$ is equivalent to a source of pure emf $E$ with a resistance $r$ in series as shown in Fig. 9.26.
Let us consider the performance of a cell of emf $E$ and internal resistance $r$ as shown in Fig.9.27. A voltmeter of infinite resistance measures the potential difference across the external resistance $R$ or the potential difference $V$ across the terminals of the cell. The current $I$ flowing through the circuit is given by

$$
I=\frac{E}{R+r}
$$

$$
\text { or } E=I R+I r \ldots \ldots \ldots(9.45)
$$

Here $I R=V$ is the terminal potential difference of the cell in the presence of current $I$. When the switch $S$ is open, no current passes through the resistance. In this case, the voltmeter reads the emf $E$ as terminal voltage. Thus, terminal voltage in the presence of the current (switch ON) would be less than the emf Eby Ir.
A voltmeter connected across the terminals of a cell measures: (a) the emf of the cell on open circuit,
(b) the tarminal potential difference on a closed circuit.

Let us interpret the Eq. 9.45 on energy considerations. The left side of this equation is the emf $E$ of the cell which is equal to energy gained by unit charge as it passes through the cell from its negative to positive terminal. The right side of the equation gives an account of the utilization of this energy as the current passes the circuit. It states that, as a unit charge passes through the circuit, a part of this energy equal to irle dissipated into the cell and the rest of the energy is dissipated into the external resistance $R$. It is given by potential drop $I R$. Thus, the emf gives the energy supplied to unit charge by the cell and the potential drop across the various elements account for the dissipation of this energy into other forms as the unit charge passes through these elements.
The emf is the "cause" and potential difference is its "effect". The emf is always present even when no current is drawn through the battery or the cell, but the potential difference across the conductor is zero when no current flows through it.
Example 9.10 The potential difference between the terminals of a battery in open circuit is 2.2 V . When it is connected across a resistance of $5.0 \Omega$, the potential falls to 1.8 V . Calculate the current and the internal resistance of the battery.

Solution

$$
E=2.2 \mathrm{~V}, \quad R=5.0 \Omega, \quad V=1.8 \mathrm{~V}
$$

We have to calculate $I$ and $r$
Using

$$
V=I R \quad \text { or } \quad I=\frac{V}{R}=\frac{1.8 \mathrm{~V}}{5.0 \Omega}=0.36 \mathrm{~A}
$$

Internal resistance $r$ can be calculated by using

$$
\begin{aligned}
E & =V+i r \\
2.2 V & =1.8 \mathrm{~V}+0.36 \mathrm{Ax} r
\end{aligned}
$$

or
$r=1.1 \Omega$

# 9.16 KIRCHHOFF'S RULES

Kirchhoff's rules are two fundamental principles in circuit analysis that help to determine the current and voltage in electrical circuits. They are particularly useful for analysing complex circuits that cannot be simplified by Ohm's law and series or parallel combinations.

## Kirchhoff's First Rule

It states that the sum of all the currents meeting at a point in the circuit is zero.
i.e., $\quad 27=0$
It is a convention that a current flowing towards a point is taken as positive and that flowing away from a point is taken as negative.

For your information
A node is a point in an electric circuit which joins the two or more branches.

Consider a situation where four wires meet at a point $A$ (Fig.9.28). The currents flowing into the point $A$ sre $I_{1}$ and $I_{2}$ and currents flowing away from the point are $I_{3}$ and $I_{4}$.
According to the convention, currents $I_{1}$ and $I_{2}$ are positive and currents $I_{3}$ and $I_{4}$ are negative. Applying Eq. 9.48 , we have

$$
I_{1}+I_{2}+\left(-I_{3}\right)+\left(-I_{4}\right)=0
$$

or

$$
I_{1}+I_{2}=I_{3}+I_{4}
$$

Using Eq.9.47, Kirchhoff's first rule can be stated in other words as:

The sum of all the currents flowing towards a point is equal to the sum of all the currents flowing away from the point.
Fig. 9.28: According to Kirchhoff's $1^{\text {st }}$ rule $I_{1}+I_{2}=I_{3}+I_{4}$

## Deved know?

The node at which potential is taken as zero is called datum node or reference node.

Kirchhoff's first rule which is also known as Kirchhoff's point rule is a manifestation of law of conservation of charge. If there is no sink or source of charge at a point, the total charge flowing towards the point must be equal to the total charge flowing away from it.

# Kirchhoff's Second Rule

It states that the algebraic sum of voltage changes in a closed circuit or a loop must be equal to zero. Consider a closed circuit shown in Fig. 9.29. The direction of the current / flowing through the circuit depends on the cell having the greater emf. Suppose $E_{1}$ is greater than $E_{2}$, so the current flows in counter clockwise direction. We know that a steady current is equivalent to a continuous flow of positive charges through the circuit. We also know that a voltage change or potential difference is equal to the work done on a unit positive charge or energy gained or lost by it in moving from one point to the other. Thus, when a positive charge $Q$ due to the current $I$ in the closed circuit (Fig.9.29), passes through the cell $E_{1}$ from low (-ve) to high potential ( +ve ), it gains energy because work is done on it. Using Eq. 9.44 the energy gain is $E_{1} Q$. When the current passes through the cell $E_{2}$, it loses energy equal to $-E_{2} Q$ because here the charge passes from high to low potential. In going through the resistor $R_{1}$, the charge $Q$ loses energy equal to $-I R_{1} Q$ where $I R_{1}$ is potential difference across $R_{1}$. The minus sign shows that the charge is passing from high to low potential. Similarly, the loss of energy while passing through the resistor $R_{2}$ is $-I R_{2} Q$. Finally, the charge reaches the negative terminal of the cell $E_{2}$ from where we started. According to the law of conservation of energy, the total change in energy of our system is zero. Therefore, we can write:

$$
E_{1} Q-I R_{1} Q-E_{2} Q-I R_{2} Q=0
$$

or

$$
E_{1}-I R_{1}-E_{2}-I R_{2}=0
$$

Fig. 9.29: According to Kirchhoff's $2^{\text {nd }}$ rule $E_{1}-I R_{1}-E_{2}-I R_{2}=0$

which is Kirchhoff's second rule and it states that:
The algebraic sum of potential changes in a closed circuit is zero.
We have seen that this rule is simply a particular way of stating the law of conservation of energy in electrical problems.
Before applying this rule for the analysis of complex network, it is worthwhile to thoroughly understand the rules for finding the potential changes.
(i) If a source of emf is traversed from positive to negative terminal, the potential change is positive. It is negative in the opposite direction.
(ii) If a resistor is traversed in the direction of current, the change in potential is positive. It is negative in the opposite direction.
Example 9.11 Calculate the currents in the three resistances of the circuit shown in Fig. 9.30.

# Solution

First we select two loops abcda and ebcfe. The choice of loops is quite arbitrary, but it should be such that each resistance is included at least once in the selected loops.
Fig. 9.30

After selecting the loops, suppose a current $I_{1}$ is flowing in the first loop and $I_{2}$ in the second loop, all flowing in the same sense. These currents are called loop currents. The actual currents will be calculated with their help. It should be noted that the sense of the current flowing in all loops should essentially be the same. It may be clockwise or anticlockwise. Here we have assumed it to be clockwise.
We now apply Kirchhoff's second rule to obtain the equations required to calculate the currents through the resistances. We first consider the loop abcda. Starting at point a we follow the loop clockwise. The voltage change while crossing the battery $E_{1}$ is $-E_{1}$ because the current flows through it from positive to negative. The voltage change across $R_{1}$ is $-I_{1} R_{1}$. The resistance $R_{2}$ is common to both the loops $I_{1}$ and $I_{2}$, therefore, the currents $I_{1}$ and $I_{2}$ simultaneously flow through it. The directions of currents $I_{1}$ and $I_{2}$ as flowing through $R_{2}$ are opposite, so we have to decide that which of these currents is to be assigned a positive sign. The convention regarding the sign of the current is that if we are applying the Kirchhoff's second rule in the first loop, then the current of this loop i.e., $I_{1}$ will be assigned a positive sign and all currents flowing opposite to $I_{1}$ have a negative sign. Similarly, while applying Kirchhoff's second rule in the second loop, the current $I_{2}$ will be considered as positive and $I_{1}$ as negative. Using this convention the current

flowing through $R_{2}$ is $\left(I_{1}-I_{2}\right)$ and the voltage change across is $-\left(I_{1}-I_{2}\right) R_{2}$. The voltage change across the battery $E_{2}$ is $E_{2}$. Thus, the Kirchhoff's second rule as applied to the loop abode gives

$$
-E_{1}-I_{1} R_{1}-\left(I_{1}-I_{2}\right) R_{2}+E_{2}=0
$$

Substituting the values, we have

$$
\begin{gathered}
-40 \mathrm{~V}-I_{1} \times 10 \Omega-\left(I_{1}-I_{2}\right) \times 30 \Omega+60 \mathrm{~V}=0 \\
20 \mathrm{~V}-10 \Omega \times\left[I_{1}+3\left(I_{1}-I_{2}\right)\right]=0 \\
4 I_{1}-3 I_{2}=2 \mathrm{~V} \Omega^{1}=2 \mathrm{~A} \\
4 I_{1}-3 I_{2}=2 \mathrm{~V} \Omega^{1}=2 \mathrm{~A}
\end{gathered}
$$

Similarly, applying Kirchhoff's second rule to the loop ebote, we have

$$
-E_{2}-\left(I_{2}-I_{1}\right) R_{2}-I_{2} R_{2}+E_{2}=0
$$

Substituting the values

$$
\begin{gathered}
-60 \mathrm{~V}-\left(I_{2}-I_{1}\right) \times 30 \Omega-I_{2} \times 15 \Omega+50 \mathrm{~V}=0 \\
-10 \mathrm{~V}-15 \Omega \times\left[I_{2}+2\left(I_{2}-I_{1}\right)\right]=0 \\
6 I_{1}-9 I_{2}=2 \mathrm{~V} \Omega^{1}=2 \mathrm{~A}
\end{gathered}
$$

Solving Eq.(i) and Eq. (ii) for $I_{1}$ and $I_{2}$, we have

$$
I_{1}=0.86 \AA \text { and } I_{2}=0.22 \mathrm{~A}
$$

Knowing the value of loop currents $I_{1}$ and $I_{2}$ the actual current flowing through each resistance of the circuit can be determined. Fig. 9.29 shows that $I_{1}$ and $I_{2}$ are the actual currents through the resistances $R_{1}$ and $R_{2}$. The actual current through $R_{2}$ is the difference of $I_{1}$ and $I_{2}$ and its direction is along the larger current. Thus,
The current through $R_{1}=I_{1}=2 / 3 A=0.66$ A flowing in the direction of $I_{1}$ i.e., from a to d.
The current through $R_{2}=I_{1}-I_{2}=2 / 3 A-2 / 9 A=0.44$ A flowing in the direction of $I_{1}$ i.e., from cto b.
The current through $R_{2}=I_{2}=2 / 9 A=0.22$ A flowing in the direction of $I_{1}$ i.e., from $f$ to e.

# Procedures of Solution of Circuit Problems

After solving the above problem, we are in a position to apply the same procedure to analyse other direct current complex networks. While using Kirchhoff's rules in other problems, it is worthwhile to follow the approach given below:
(i) Draw the circuit diagram.
(ii) The choice of loops should be such that each resistance is included at least once in the selected loops.
(iii) Assume a loop current in each loop. All the loop currents should be in the same sense. It may be either clockwise or anticlockwise.
(iv) Write the loop equations for all the selected loops. For writing each loop equation, the voltage change across any component is positive if traversed from low to high

potential and it is negative if traversed from high to low potential.
(v) Solve these equations for the unknown quantities.

# 9.17 WHEATSTONE BRIDGE

It is an electric circuit. The Wheatstone bridge circuit shown in Fig. 9.31 consists of four resistances $R_{1}, R_{2}, R_{3}$ and $R_{4}$ connected in such a way so as to form a mesh ABCDA. A battery is connected between points $A$ and $C$. A sensitive galvanometer of resistance $R_{2}$ is connected between points $B$ and $D$. If the switch $S$ is closed, a current will flow through the galvanometer. We have to determine the condition under which no current flows through the galvanometer even after the switch is closed. For this purpose, we analyse this circuit using Kirchhoff's second rule. We consider two loops ABDA and BCDB and assume anticlockwise loop currents $I_{1}$ and $I_{2}$ through the loops respectively. The Kirchhoff's second rule as applied to loop ABDA gives:
Fig. 9.31: Wheatstone bridge circuit

$$
-I_{1} R_{1}-\left(I_{1}-I_{2}\right) R_{2}-I_{1} R_{3}=0
$$

Similarly, by applying the Kirchhoff's second rule to loop BCDB, we have

$$
-I_{2} R_{2}-I_{1} R_{1}-\left(I_{2}-I_{1}\right) R_{2}=0
$$

The current flowing through the galvanometer will be zero if, $I_{1}-I_{2}=0$ or $I_{1}=I_{2}$. With this condition Eq. 9.51 and Eq. 9.52 reduce to:

$$
-I_{2} R_{2}=I_{1} R_{3}
$$

and

$$
-I_{3} R_{2}=I_{1} R_{4}
$$

Dividing Eq. 9.48 by Eq. 9.49, we have

$$
\frac{-I_{1} R_{1}}{-I_{2} R_{2}}=\frac{I_{1} R_{3}}{I_{2} R_{4}}
$$

As $I_{1}=I_{2}$, therefore,

$$
\frac{R_{1}}{R_{2}}=\frac{R_{2}}{R_{4}}
$$

## Point to ponder!

Why is a three pin plug used in some electric appliances?

Thus, whenever the condition of Eq. 9.54 is satisfied, no current flows through the galvanometer and it shows no deflection, or conversely when the galvanometer in the Wheatstone bridge circuit shows no deflection, Eq. 9.54 is satisfied. If we connect three

resistances $R_{1}, R_{2}$ and $R_{3}$ of known adjustable values and a fourth resistance $R_{4}$ of unknown value and the resistances $R_{1}, R_{2}$ and $R_{3}$ are so adjusted that the galvanometer shows no deflection, then from the known resistances $R_{1}, R_{2}$ and $R_{3}$, the unknown resistance $R_{4}$ can be determined by using Eq. 9.54.

# 9.18 POTENTIOMETER

A potentiometer is mainly used to compare potential differences and to find the value of an unknown resistance. It works on the principle of Wheatslone Bridge.

## Working of Potentiometer

Potential difference is usually measured by an instrument called a voltmeter. The voltmeter is connected across the two points in a circuit between which potential difference is to be measured. It is necessary that the resistance of the voltmeter be large compared to the circuit resistance across which the voltmeter is connected. Otherwise, an appreciable current will flow through the voltmeter which will alter the circuit current and the potential difference to be measured. Thus, the voltmeter can read the correct potential difference only when it does not draw any current from the circuit across which it is connected. An ideal voltmeter would have an infinite resistance.
However, there are some potential measuring instruments such as digital voltmeter and cathode-ray oscilloscope which practically do not draw any current from the circuit because of their large resistance and are thus very accurate potential measuring instruments. But these instruments are very expensive. A very simple instrument which can measure and compare potential differences accurately is a potentiometer.
A potentiometer consists of a resistor $R$ in the form of a wire on which a terminal $C$ can slide (Fig. 9.32-a). The resistance between $A$ and $C$ can be varied from 0 to $R$ as the sliding contact $C$ is moved from $A$ to $B$. If a battery of emf $E$ is connected across $R$ (Fig. 9.32-b) the current flowing through it is $I=E / R$. If we represent the resistance between $A$ and $C$ by $r$, the potential drop between these points will be $r I=r E / R$. Thus, as $C$ is moved from $A$ to $B, r$ varies from 0 to $R$ and the potential drop between $A$ and $C$ changes from 0 to $E$.
Such an arrangement also known as potential divider can be used to measure the unknown emf of a source by using the circuit shown in Fig. 9.33. Here $R$ is in the form of a straight wire of uniform area of cross-section. A source of potential, say a cell whose emf $E_{x}$ is to be
Fig. 9.32

measured, is connected between $A$ and the sliding contact $C$ through a galvanometer $G$. It should be noted that the positive terminal of $E_{x}$ and that of the potential divider are connected to the same point $A$. If, in the loop AGCA, the point $C$ and the negative terminal of $E_{x}$ are at the same potential, then the two terminals of the galvanometer will be at the same potential and no current will flow through the galvanometer. Therefore, to measure the potential $E_{x}$, the position of $C$ is so adjusted that the galvanometer shows no deflection. Under this
Fig. 9.33
condition, the emf $E_{x}$, of the cell is equal to the potential difference between $A$ and $C$ whose value $E_{x} / R$ is known. In case of a wire of uniform cross-section, the resistance is proportional to the length of the wire. Therefore, the unknown emf is also given by

$$
E_{x}=E \frac{\ell}{R}=E \frac{\ell}{L}
$$

where $L$ is the total length of the wire $A B$ and $\ell$ is its length from $A$ to $C$, after $C$ has been adjusted for no deflection. As the maximum potential that can be obtained between $A$ and $C$ is $E$, so the unknown emf $E_{x}$ should not exceed this value, otherwise the null condition will not be obtained. It can be seen that the unknown emf $E_{x}$ is determined when no current is drawn from it and therefore, potentiometer is one of the most accurate methods for measuring potential.
The method for measuring the emf of a cell as described above can be used to compare the emfs $E_{1}$ and $E_{2}$ of two cells. The balancing lengths $\ell$, and $\ell_{2}$ are found separately for the two cells. Then,

$$
E_{1}=E \frac{\ell_{1}}{L} \text { and } E_{2}=E \frac{\ell_{2}}{L}
$$

Dividing these two equations, we have

$$
\frac{E_{1}}{E_{2}}=\frac{\ell}{\ell_{2}}
$$

So, the ratio of the emfs is equal to ratio of the balancing lengths.

# 9.19 USE OF A GALVANOMETER

A galvanometer is an instrument for detecting a current. We are not going to discuss its internal structure and how does it work. We focus only on its use. It is often used in null methods to achieve precise measurements in electrical circuits. The null method involves adjusting the circuit until the galvanometer shows no deflection i.e., a zero reading. This indicates that certain required conditions are met in the circuit. In this state, the electric potentials at both ends of the galvanometer are the same. Although a galvanometer has its own resistance, but at the null reading, its resistance does not

come into play. The reason is that, in this condition no current is passing through it. The null method is widely used in bridge circuits such as Wheatstone and potentiometer setups.
As we have studied in the previous section, the null method is used to measure an unknown resistance in the Wheatstone bridge circuits. The galvanometer is connected between the mid-points of opposite sides. The variable resistance is adjusted until the galvanometer shows no deflection. At this point, the bridge is balanced and the unknown resistance can be calculated using the ratio of the known resistances.
In a potentiometer, null method is used to measure an unknown voltage by comparison with a known reference voltage applied across the resistance wire of the potentiometer. A galvanometer and a jockey are used to make contact along the wire. At null point, the potential difference between the jockey and the end of the wire equals the unknown voltage. The position of the jockey gives the measure of the unknown voltage.
There are some advantages of using a galvanometer in null method.

1. Null method, eliminates the effect of the galvanometer's internal resistance on the measurement resulting in more accurate readings.
2. Galvanometers are highly sensitive and can detect very small currents of the order of $10^{4}$ ampere.
3. "No deflection" indicates a direct and clear condition of balance making it easier to identify the null point.

# 9.20 THERMISTORS

A thermistor is a heat sensitive resistor. Most thermistors have negative temperature coefficient of resistance, i.e., the resistance of such thermistors decreases when their temperature is increased. Thermistors with positive temperature coefficient are also available.
In the thermistors, resistance decreases as temperature increases. This is because increasing temperature provides more energy to the charge carriers (electrons or holes), enabling them to move more freely and thus reducing resistance.
Thermistors are made by heating under high pressure semiconductor ceramic made from mixtures of metallic oxides of manganese, nickel, cobalt, copper, iron, etc. These are pressed into desired shapes and
Fig. 9.34: Thermistors syambols
Fig. 9.35: Types of thermistors

then baked at high temperature. Different types of thermistors are shown in Fig. 9.34. They may be in the form of beads, rods or washers.

# Applications of Thermistors

## Temperature Measurement

Thermistors are used in thermometers, and electric devices such as air conditioners, refrigerators, heaters, microwave ovens, incubators, etc.to monitor temperature.
Thermistors with high negative temperature coefficient are very accurate for measuring low temperatures especially near 10 K . The higher resistance at low temperature enables more accurate measurement possible.
Thermistors have wide applications as temperature sensors, i.e. they convert changes of temperature into electrical voltage which is duly processed. For example, these are used in coolant temperature sensors in automobile engines to prevent the engine overheating and in digital thermometers.

## Temperature Compensation

Thermistors are used in circuits where temperature changes could affect performance. Such as in oscillators, battery charging circuits and power systems.

## Inrush Current Limiting

Thermistors are used to limit the initial flow of current when a device is first turned on.

## Voltage Divider

Thermistors are widely used as voltage divider. As shown in Fig. 9.36 when temperature of a thermistor increases, its resistance decreases. This decreases the voltage drop across the thermistor. As a result, the potential at point B increases that can be used to trigger a circuit connected to it. In case of a fire alarm, the use of a thermistor turns the NOT gate low when it
gets heated. The output of NOT gate goes high and
turns the siren ON