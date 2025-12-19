### 1.4.1 The Polar Form of a Complex Nurnber

Consider the adjoining diagram representing the complex number $z=x+i y$. From the diagram, we see that $x=r \cos \theta$ and $y=r \sin \theta$, where $r=|z|$ is modulus and $\theta$ is called an argument of $z$.
Hence $\quad x+i y=r \cos \theta+i r \sin \theta$
where $r=|z|=\sqrt{x^{2}+y^{2}}$ and $\theta=\tan ^{-1} \frac{y}{x}$
Equation (i) is called the polar form of the complex number $z$.
Example 12 Express the complex number $1+i \sqrt{3}$ in polar form.
Solution Step - I: Put $r \cos \theta=1$ and $r \sin \theta=\sqrt{3}$
Step - II: $r^{2}=(1)^{2}+(\sqrt{3})^{2}$

$$
\begin{aligned}
& \Rightarrow r^{2}=1+3=4 \\
& \Rightarrow r=2
\end{aligned}
$$

Step - III: $\quad \theta=\tan ^{-1} \frac{\sqrt{3}}{1}=\tan ^{-1} \sqrt{3}=60^{\circ}$

## Note

- If $x=0, y>0$ then $\theta=90^{\circ}$
- If $x=0, y<0$ then $\theta=-90^{\circ}$
- If $x=0, y=0$ then $\theta$ is undefined.
- If $y=0, x>0$ then $\theta=0^{\circ}$.
- If $y=0, x<0$ then $\theta=180^{\circ}$.

Thus $1+i \sqrt{3}=2 \cos 60^{\circ}+i 2 \sin 60^{\circ}$
Principal Argument: The principal argument $\theta$ of a complex number $z=a+b i$ is the angle between the positive real axis and the line joining $(a, b)$ to the origin in the Argand plane.

$$
\operatorname{Arg} z=\theta=\tan ^{-1}\left(\frac{b}{a}\right) \quad(a \neq 0)
$$

It is denoted by Arg. It is a single, specific value of the argument, typically chosen within a standard range: $\operatorname{Arg} z \in(-\pi, \pi]$.

# 1.3.3 Operations on Complex Numbers in Polar Form

## Addition and Subtraction of Complex number in Polar form

Let $z_{1}=r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)$ and $z_{2}=r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right)$ be two complex numbers in polar form. The addition and subtraction of these numbers can be computed simply as

$$
z_{1}+z_{2}=r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)+r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right)
$$

and $z_{1}-z_{2}=r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)-r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right)$

## Multiplication of Complex number in Polar form

Let $z_{1}=r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)$ and $z_{2}=r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right)$ be two complex number in polar form. The product of these numbers can be derived by multiplying them directly and simplifying

$$
\begin{aligned}
& z_{1} \cdot z_{2}=r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right) \cdot r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right) \\
& z_{1} \cdot z_{2}=r_{1} \cdot r_{2}\left(\cos \theta_{1} \cos \theta_{2}+i \cos \theta_{1} \sin \theta_{2}+i \sin \theta_{1} \cos \theta_{2}+i^{2} \sin \theta_{1} \sin \theta_{2}\right) \\
& z_{1} \cdot z_{2}=r_{1} \cdot r_{2}\left[\left(\cos \theta_{1} \cos \theta_{2}-\sin \theta_{1} \sin \theta_{2}\right)+i\left(\cos \theta_{1} \sin \theta_{2}+\sin \theta_{1} \cos \theta_{2}\right)\right] \quad \because i^{2}=-1 \\
& z_{1} \cdot z_{2}=r_{1} \cdot r_{2}\left[\cos \left(\theta_{1}+\theta_{2}\right)+i \sin \left(\theta_{1}+\theta_{2}\right)\right] \quad \text { (Using trigonometric identities) }
\end{aligned}
$$

Thus, multiplying two complex numbers in polar form involves multiplying their moduli and summing their arguments i.e., $\arg \left(z_{1} \cdot z_{2}\right)=\arg \left(z_{1}\right)+\arg \left(z_{2}\right)$
Example13 Find the product of $5\left(\cos \frac{\pi}{6}+i \sin \frac{\pi}{6}\right)$ and $4\left(\cos \frac{3 \pi}{2}+i \sin \frac{3 \pi}{2}\right)$.
Solution Let $z_{1}=5\left(\cos \frac{\pi}{6}+i \sin \frac{\pi}{6}\right)$ and $z_{2}=4\left(\cos \frac{3 \pi}{2}+i \sin \frac{3 \pi}{2}\right)$
Here, $r_{1}=5$ and $\theta_{1}=\frac{\pi}{6}$, while $r_{2}=4$ and $\theta_{2}=\frac{3 \pi}{2}$
Substitute this value in the product formula

$$
\begin{aligned}
z_{1} \cdot z_{2} & =r_{1} \cdot r_{2}\left[\cos \left(\theta_{1}+\theta_{2}\right)+i \sin \left(\theta_{1}+\theta_{2}\right)\right] \\
& =5 \times 4\left[\cos \left(\frac{\pi}{6}+\frac{3 \pi}{2}\right)+i \sin \left(\frac{\pi}{6}+\frac{3 \pi}{2}\right)\right]=20\left(\cos \frac{5 \pi}{3}+i \sin \frac{5 \pi}{3}\right)
\end{aligned}
$$

Thus, the required product is $20\left(\cos \frac{5 \pi}{3}+i \sin \frac{5 \pi}{3}\right)$

# Division of Complex Number in Polar Form

Let $z_{1}=r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)$ and $z_{2}=r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right)$ be two complex numbers in polar form. The formula for division of these numbers in polar form can be derived as below:
$\frac{z_{1}}{z_{2}}=\frac{r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)}{r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right)}$
$\frac{z_{1}}{z_{2}}=\frac{r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)}{r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right) \cdot\left(\cos \theta_{2}-i \sin \theta_{2}\right) \quad$ (Multiply and divide the R.H.S by conjugate of $\cos \theta_{2}+i \sin \theta_{2}$ )
$\frac{z_{1}}{z_{2}}=\frac{r_{1}}{r_{2}} \frac{\left(\cos \theta_{1} \cos \theta_{2}+\sin \theta_{1} \sin \theta_{2}\right)+i\left(\sin \theta_{1} \cos \theta_{2}-\cos \theta_{1} \sin \theta_{2}\right)}{\cos ^{2} \theta_{2}+\sin ^{2} \theta_{2}}$
$\frac{z_{1}}{z_{2}}=\frac{r_{1}}{r_{2}}\left[\cos \left(\theta_{1}-\theta_{2}\right)+i \sin \left(\theta_{1}-\theta_{2}\right)\right] \quad$ (Using trigonometric identities)
Thus, the modulus of the division of two complex numbers equals the quotient of their moduli, while the arguments of the quotient is the difference between their arguments.
Thus, when dividing two complex numbers, the modulus of the result is the ratio of their moduli, and the argument of the result is the difference between their arguments i.e., $\arg \left(\frac{z_{1}}{z_{2}}\right)=\arg \left(z_{1}\right)-\arg \left(z_{2}\right)$

Example 14 Divide $\frac{2}{7}\left(\cos \frac{7 \pi}{6}+i \sin \frac{7 \pi}{6}\right)$ by $\frac{3}{5}\left(\cos \left(-\frac{\pi}{2}\right)+i \sin \left(-\frac{\pi}{2}\right)\right)$.
Solution Let $z_{1}=\frac{2}{7}\left(\cos \frac{7 \pi}{6}+i \sin \frac{7 \pi}{6}\right)$ and $z_{2}=\frac{3}{5}\left(\cos \left(-\frac{\pi}{2}\right)+i \sin \left(-\frac{\pi}{2}\right)\right)$
Here, $\quad r_{1}=\frac{2}{7}, \theta_{1}=\frac{7 \pi}{6}, r_{1}=\frac{3}{5}$ and $\theta_{2}=-\frac{\pi}{2}$.
Substitute value in the quotient formula

$$
\begin{aligned}
\frac{z_{1}}{z_{2}} & =\frac{r_{1}}{r_{2}}\left[\cos \left(\theta_{1}-\theta_{2}\right)+i \sin \left(\theta_{1}-\theta_{2}\right)\right] \\
& =\frac{2}{7} \times \frac{5}{3}\left[\cos \left(\frac{7 \pi}{6}-\left(-\frac{\pi}{2}\right)\right)+i \sin \left(\frac{7 \pi}{6}-\left(-\frac{\pi}{2}\right)\right)\right] \\
\frac{z_{1}}{z_{2}} & =\frac{10}{21}\left(\cos \frac{5 \pi}{3}+i \sin \frac{5 \pi}{3}\right)
\end{aligned}
$$

Example 15 If $z=x+i y$, then write the equation $|3 z-i|=|3 z+7|$ in terms of $x$ and $y$.
Solution Given $|3 z-i|=|3 \bar{z}+7|$
$|3 z-i|=|3(x+i y)-i|=|3 x+i(3 y-1)|=\sqrt{(3 x)^{2}+(3 y-1)^{2}}$
$|3 \bar{z}+7|=|3 x+3 i y+7|=|3 x-3 i y+7|=|3 x+7+i(-3 y)|=\sqrt{(3 x+7)^{2}+(-3 y)^{2}}$
Substitutes these values in (i)

$$
\sqrt{(3 x)^{2}+(3 y-1)^{2}}=\sqrt{(3 x+7)^{2}+(-3 y)^{2}}
$$

Taking square on both sides

$$
\begin{aligned}
(3 x)^{2}+(3 y-1)^{2} & =(3 x+7)^{2}+(-3 y)^{2} \\
9 x^{2}+9 y^{2}-6 y+1 & =9 x^{2}+42 x+49+9 y^{2} \\
\Rightarrow \quad-6 y+1 & =42 x+49 \\
\Rightarrow \quad-6 y & =42 x+48 \\
\text { or } \quad y & =-7 x-8
\end{aligned}
$$

The equation $y=-7 x-8$ represents a straight line in the complex plane.
Example 16 Show that $(x+2)^{2}+y^{2}=8$ if $\arg \left(\frac{z+2 i}{z-2 i}\right)=\frac{3 \pi}{4}$ for $z=x+i y$.
Solution $\frac{z+2 i}{z-2 i}=\frac{x+i y+2 i}{x+i y-2 i}=\frac{x+i(y+2)}{x+i(y-2)}=\frac{x+i(y+2)}{x+i(y-2)} x \frac{x-i(y-2)}{x-i(y-2)}$
$\Rightarrow \quad \frac{z+2 i}{z-2 i}=\frac{\left(x^{2}+y^{2}-4\right)+4 i x}{x^{2}+(y-2)^{2}}=\frac{x^{2}+y^{2}-4}{x^{2}+(y-2)^{2}}+i \frac{4 x}{x^{2}+(y-2)^{2}}$
As

$$
\arg \left(\frac{z+2 i}{z-2 i}\right)=\frac{3 \pi}{4}
$$

$\Rightarrow \quad \tan ^{-1}\left(\frac{4 x}{\frac{x^{2}+(y-2)^{2}}{x^{2}+y^{2}-4}}\right)=\frac{3 \pi}{4} \quad \Rightarrow \quad \frac{4 x}{x^{2}+y^{2}-4}=\tan \frac{3 \pi}{4}=-1$
$\Rightarrow \quad 4 x=-1\left(x^{2}+y^{2}-4\right) \quad \Rightarrow \quad x^{2}+4 x+y^{2}=4$
Completing the square for $x^{2}$, we have

$$
(x+2)^{2}+y^{2}=8
$$

# 1.5 Complex Numbers in the Real World (Voltage, Current and Resistance)

Ohm's Law is a fundamental principle in physics that describes the relationship between voltage $V$, current $I$ and resistance $R$ in an electrical circuit. Mathematically Ohm's Law can be expressed by the formula $V=I R$.
When dealing with alternating current (AC) circuits, resistance generalizes to impedance ( $Z$ ). Resistance in a circuit is due to inductor $\left(X_{L}\right)$ and capacitor $\left(X_{C}\right)$. Their difference is reactance $X=\left(X_{L}\right)-\left(X_{C}\right)$. Geometrically it is shown in the adjacent figure. Here $Z=R+i X$.
Then for AC circuits, Ohm's Law in Terms of Impedance is expressed by the formula $V=I \cdot Z$.
Example 17 If the impedance of circuit is $11\left(\cos 55.35^{\circ}+i \sin 55.35^{\circ}\right)$ ohms at a voltage of $25\left(\cos 30^{\circ}+i \sin 30^{\circ}\right) V$, find the value of current in the circuit.
Solution Substitute the voltage $25\left(\cos 30^{\circ}+i \sin 30^{\circ}\right)$ and impedance $11\left(\cos 55.35^{\circ}+i \sin 55.35^{\circ}\right)$ into the equation $V=I Z$, where $V$ is voltage, $I$ denote the current and $Z$ is impedance.

$$
\begin{aligned}
25\left(\cos 30^{\circ}+i \sin 30^{\circ}\right) & =I .11\left(\cos 55.35^{\circ}+i \sin 55.35^{\circ}\right) \\
\text { or } \quad I & =\frac{25\left(\cos 30^{\circ}+i \sin 30^{\circ}\right)}{11\left(\cos 55.35^{\circ}+i \sin 55.35^{\circ}\right)} \\
I & =\frac{25}{11}\left[\cos \left(30^{\circ}-55.35^{\circ}\right)+i \sin \left(30^{\circ}-55.35^{\circ}\right)\right. \\
I & =2.27\left[\cos \left(-25.35^{\circ}\right)+i \sin \left(-25.35^{\circ}\right)\right.
\end{aligned}
$$

Express into rectangular form

$$
I=2.27[0.90+i(-0.42)]=2.04-0.95 i
$$

Thus, current is $2.04-0.95 i A$.
Cryptography: It is the science of securing information by transforming readable messages called plaintext into secret code called ciphertext using mathematical algorithms and encryption keys. It consists of two main processes i.e., encryption to lock message with complex math, and decryption to unlock it with the right key.
Example 18 Encrypt the word "MATH" by multiplying it with a complex number $k=2+3 i$ and then decrypted back to its original form using the concept of multiplicative inverse in complex numbers.
Each letter of the alphabet is assigned a numerical value as follows:

$$
A=1, B=2, C=3, \ldots, Z=26
$$

# Unit 4 Complex Numbers

Solution First, we assign each letter in the word "MATH" a complex number with zero imaginary part. The encryption and decryption are shown in the table below

| Letter | Complex Number (x) | $z$ encrypted $-z \times k$ | $z$ decrypled $-z$ encrypted $/ k$ | Letter |
| :--: | :--: | :--: | :--: | :--: |
| M | $13+0 i$ | $(13+0 i)(2+3 i)=26+39 i$ | $(26+39 i) /(2+3 i)=13+0 i$ | M |
| A | $1+0 i$ | $(1+0 i)(2+3 i)=2+3 i$ | $(2+3 i) /(2+3 i)=1+0 i$ | A |
| T | $20+0 i$ | $(20+0 i)(2+3 i)=40+60 i$ | $(40+60 i) / 2+3 i=20+0 i$ | T |
| H | $8+0 i$ | $(8+0 i)(2+3 i)=16+24 i$ | $16+24 i / 2+3 i=8+0 i$ | H |

## EXERCISE 1.5

1. Plot the following points:
(i) $(2,75)$
(ii) $(-3,120)$
(iii) $\left(2, \frac{\pi}{6}\right)$
(iv) $\left(5, \frac{5 \pi}{6}\right)$
(v) $\left(-\frac{5}{2}, \frac{\pi}{3}\right)$
(vi) $\left(-3,-\frac{2 \pi}{3}\right)$
(vii) $\left(-\frac{9}{2},-\frac{19 \pi}{12}\right)$
(viii) $\left(-\frac{5}{2}, \frac{5 \pi}{12}\right)$
2. Express the following complex numbers in polar form:
(i) $4+3 i$
(ii) $1+i$
(iii) $\frac{1}{2}+\frac{\sqrt{3}}{2} i$
(iv) $-\frac{5}{2}-\frac{5 \sqrt{3}}{2} i$
(v) $\frac{1-i}{1+i}$
(vi) $\frac{\sqrt{3}+i}{1+\sqrt{3} i}$
(vii) $\frac{3+4 i}{4+3 i}$
3. Convert each of the complex number $z$ in the rectangular form $x+i y$ :
(i) $4\left(\cos \frac{5 \pi}{3}+i \sin \frac{5 \pi}{3}\right)$
(ii) $\frac{3}{2}\left(\cos \frac{7 \pi}{6}+i \sin \frac{7 \pi}{6}\right)$
(iii) $|z|=7, \arg (z)=\frac{23 \pi}{12}$
(iv) $|z|=11, \arg (z)=-\frac{11 \pi}{12}$
(v) $|z|=\frac{10}{3}, \arg (z)=-\frac{17 \pi}{12}$
(vi) $2 \cos (-33)+i 2 \sin (-33)$
4. If $z_{1}=9\left(\cos \frac{5 \pi}{4}+i \sin \frac{5 \pi}{4}\right)$ and $z_{2}=5\left(\cos \frac{\pi}{3}+i \sin \frac{\pi}{3}\right)$ then find
(i) $z_{1}+z_{2}$
(ii) $z_{1}-z_{2}$
(iii) $z_{1} \cdot z_{2}$
(iv) $\frac{z_{1}}{z_{2}}$
5. If $z_{1}=7\left(\cos \frac{23 \pi}{12}+i \sin \frac{23 \pi}{12}\right)$ and $z_{2}=11\left(\cos \frac{11 \pi}{12}+i \sin \frac{11 \pi}{12}\right)$ then find the following and express the result into $x+i y$ form
(i) $z_{1}+z_{2}$
(ii) $z_{1}-z_{2}$
(iii) $z_{1} \cdot z_{2}$
(iv) $\frac{z_{1}}{z_{2}}$

6. If $z_{1}$ and $z_{2}$ are two complex numbers, show that
(i) $\operatorname{Arg}\left(z_{1} z_{2}\right)=\operatorname{Arg} z_{1}+\operatorname{Arg} z_{2}$
(ii) $\operatorname{Arg}\left(\frac{z_{1}}{z_{2}}\right)=\operatorname{Arg} z_{1}-\operatorname{Arg} z_{2}$
7. Divide $z_{1}=6\left(\cos 150^{\circ}+i \sin 150^{\circ}\right)$ by $z_{2}=3\left(\cos 30^{\circ}+i \sin 30^{\circ}\right)$ and express in $x+i y$ form.
8. Multiply $z_{1}=2\left(\cos 60^{\circ}+i \sin 60^{\circ}\right)$ and $z_{2}=5\left(\cos 90^{\circ}+i \sin 90^{\circ}\right)$ and express in $x+i y$ form.
9. Find the modulus and argument of $z=-2-2 i$.
10. Write the equation $\arg (\bar{z}-2+i)=\frac{2 \pi}{3}$ in cartesian form, if $z=x+i y$.
11. If $z=x+i y$ and $\arg \left(\frac{\bar{z}-1+2 i}{\bar{z}+1-2 i}\right)=\frac{9 \pi}{4}$, show that $x^{2}+y^{2}+4 x+2 y-5=0$.
12. If $z=x+i y$ and $\arg (z-2-3 i)-\arg (z+2+3 i)=2 \pi$, show that $2 y=3 x$.
13. Solve the equation $|z-2 i|=|\bar{z}+2|$ for $z=x+i y$.
14. For $z=x+i y$, solve the equation $\left|5 z+4+i\right|=5 \bar{z}-3+2 i$.
15. Determine the set of points $z=x+i y$ that satisfy the equation $3 \bar{z}-2+i|=3 z+i|$.
16. If $z=x+i y$ and $w=\frac{1-i z}{z-z}$ show that $|w|=1 \Rightarrow z$ is real.
17. If $z_{1}$ and $z_{2}$ are different complex numbers with $\left|z_{2}\right|=1$, find $\left|\frac{z_{2}-z_{1}}{1-z_{1} z_{2}}\right|$.
18. An AC source supplies a voltage of $V=120\left(\cos \frac{\pi}{4}+i \sin \frac{\pi}{4}\right)$ volts to a circuit with impedance $Z=\frac{1+i \sqrt{3}}{2}$ ohms. Calculate the current in polar form.
19. An AC circuit has an impedance of $Z=3-6 i$ ohms and is connected to a voltage source of $V=90+30 i$ volts. Find the current in both rectangular and polar form.
20. Encrypt the word "CODE" by multiplying the complex encryption key $k=2-i$. Then decrypt it back to the original word.
21. Consider the complex encryption key $k=3-3 i$. Encrypt the word "QUIZ", and then recover the original word using the inverse of the key.
22. Encrypt the word "CLASS" by adding the complex encryption key $k=-3+4 i$. Then decrypt it back to the original word.