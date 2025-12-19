### **6.3 ANALYTIC PROOFS OF IMPORTANT PROPERTIES OF A CIRCLE**

A line segment whose end points lie on a circle is called a **chord** of the circle. A **diameter** of a circle is a chord containing the centre of the circle.

**Theorem:** Length of a diameter of the circle *x*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup> is 2*a*.

**Proof:** Let *AOB* be a diameter of the circle

*a*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup>

(1)

*O*(0,0) is center of (1).

Let the coordinates of *A* be (*x*<sub>*1*</sub>, *y*<sub>*1*</sub>).

Equation of *AOB* is

$$
y = \frac{y_1}{x_1} x
$$

(2)

Substituting the value of *y* from (2) into (1), we have

$$
x^2 + \frac{y_1^2}{x_1^2} x^2 = a^2 \quad \text{or} \quad x^2 (x_1^2 + y_1^2) = a^2 x_1^2
$$

or

$$
a^2 x^2 = a^2 x_1^2 \qquad \qquad \qquad \qquad \text{( }x_1^2 + y_1^2 = x^2 \text{)}
$$

i.e.,

$$
x = \pm x_1
$$

If

$$
x = x_1, \quad \text{then } y = y_1 \qquad \qquad \qquad y = \frac{y_1}{x_1} x_1
$$

Similarly when

$$
x = -x_1, \quad \text{then } y = -y_1
$$

Thus *B* has coordinates (−*x*<sub>*1*</sub>, −*y*<sub>*1*</sub>).

Length of diameter *AB* = $$\sqrt{(x_1 + x_1)^2 + (y_1 + y_1)^2}$$

$$
= \sqrt{4(x_1^2 + y_1^2)} = \sqrt{4a^2} = 2a
$$

**Theorem 2:** Perpendicular dropped from the centre of a circle on a chord bisects the chord.

**Proof:** Let *x*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup> be a circle, in which *AB* is a chord with end points *A*(*x*<sub>*1*</sub>, *y*<sub>*1*</sub>), *B*(*x*<sub>*2*</sub>, *y*<sub>*2*</sub>) on the circle and *OM* is perpendicular from the centre to the chord. We need to show that *OM* bisects the chord *AB*.

$$
\text{Slop of } AB = \frac{y_2 - y_1}{x_2 - x_1}
$$

$$
\text{Slop of perpendicular to } AB = \frac{-(x_2 - x_1)}{y_2 - y_1} = \frac{x_2 - x_1}{y_2 - y_1} = m \text{ (say)}
$$

So equation of *OM* with slope *m* and point *O*(0,0) on it, is given by

$$
y - 0 = \frac{(x_1 - x_1)}{(y_2 - y_1)}(x - 0) \qquad \text{(point - slope form)}
$$

or

$$
y = \left(\frac{x_1 - x_1}{y_2 - y_1}\right)x
$$

(1)

(1) is the equation of the perpendicular $O M$ from centre to the chord. We will show that it bisects the chord i.e., intersection of $O M$ and $A B$ is the midpoint of $A B$.

Equation of $A B$ is

$$
y-y_{1}=\frac{y_{1}-y_{2}}{x_{1}-x_{2}}\left(x-x_{1}\right)
$$

The foot of the perpendicular $O M$ is the point of intersection of (1) and (2). Inserting the value of $y$ from (1) into (2), we have

$$
\begin{aligned}
& -\frac{x_{1}-x_{2}}{y_{1}-y_{2}} x-y_{1}=\frac{y_{1}-y_{2}}{x_{1}-x_{2}}\left(x-x_{1}\right) \\
\text { or } & x\left(\frac{y_{1}-y_{2}}{x_{1}-x_{2}}+\frac{x_{1}-x_{2}}{y_{1}-y_{2}}\right)=\frac{x_{1}\left(y_{1}-y_{2}\right)}{x_{1}-x_{2}}-y_{1} \\
\text { or } & \frac{x\left[y_{1}^{2}+y_{2}^{2}-2 y_{1} y_{2}+x_{1}^{2}+x_{2}^{2}-2 x_{1} x_{2}\right]}{\left(x_{1}-x_{2}\right)\left(y_{1}-y_{2}\right)}=\frac{x_{2} y_{1}-x_{1} y_{2}}{x_{1}-x_{2}} \\
\text { or } & x\left(2 a^{2}-2 x_{1} x_{2}-2 y_{1} y_{2}\right)=x_{2} y_{1}^{2}-x_{1} y_{1} y_{2}-x_{2} y_{1} y_{2}+x_{2} y_{2}^{2} \\
\text { or } & 2 x\left(a^{2}-x_{1} x_{2}-y_{1} y_{2}\right)=x_{2}\left(a^{2}-x_{1}^{2}\right)-y_{1} y_{2}\left(x_{1}+x_{2}\right)+x_{1}\left(a^{2}-x_{2}^{2}\right) \\
& \quad=a^{2}\left(x_{1}+x_{2}\right)-x_{1} x_{2}\left(x_{1}+x_{2}\right)-y_{1} y_{2}\left(x_{1}+x_{2}\right) \\
& \quad=\left(x_{1}+x_{2}\right)\left(a^{2}-x_{1} x_{2}-y_{1} y_{2}\right)
\end{aligned}
$$

(The points $\left(x_{1}, y_{1}\right)$ and $\left(x_{2}, y_{2}\right)$ lie on the circle)
or $\quad x=\frac{x_{1}+x_{2}}{2}$
Putting $\quad x=\frac{x_{1}+x_{2}}{2} \quad$ into (1), we get

$$
y=\frac{\left(x_{1}-x_{2}\right)}{y_{2}-y_{1}} \frac{\left(x_{1}+x_{2}\right)}{2} \quad \frac{x_{1}^{2}-x_{2}^{2}}{2\left(y_{2}-y_{1}\right)}
$$

or $\quad y=\frac{y_{2}^{2}-y_{1}^{2}}{2\left(y_{2}-y_{1}\right)}=\frac{\left(y_{2}-y_{1}\right)\left(y_{2}+y_{1}\right)}{2\left(y_{2}-y_{1}\right)} \quad\left[\begin{array}{l}x_{1}^{2}+y_{1}^{2}=a^{2} \\ x_{2}^{2}+y_{2}^{2}=a^{2} \\ \Rightarrow x_{1}^{2}-x_{2}^{2}=y_{1}^{2}-y_{2}^{2}\end{array}\right]$
So, $\quad\left(\frac{x_{1}+x_{2}}{2}, \frac{y_{1}+y_{2}}{2}\right)$ is the point of intersection of $O M$ and $A B$ which is the midpoint of $A B$.
version: 1.1

## Theorem 3:

The perpendicular bisector of any chord of a circle passes through the centre of the circle.

Proof: $\quad$ Let $x^{2}+y^{2}=a^{2}$ be a circle and $A\left(x_{1}, y_{1}\right)$,
$B\left(x_{2}, y_{2}\right)$ be the end points of a chord of this circle. Let $M$ be the mid point of $A B$, i.e.
$M\left(\frac{x_{1}+x_{2}}{2}, \frac{y_{1}+y_{2}}{2}\right)$
The slop of $A B=\frac{y_{2}-y_{1}}{x_{2}-x_{1}}$
The slope of perpendicular bisector of $A B$ is
$$
-\left(\frac{x_{2}-x_{1}}{y_{2}-y_{1}}\right)
$$

So, equation of perpendicular bisector in point-slope form, is

$$
y-\frac{y_{1}+y_{2}}{2}=\left(\frac{x_{2}-x_{1}}{y_{2}-y_{1}}\right)\left(x-\frac{x_{1}+x_{2}}{2}\right)
$$

We check whether the centre $(0,0)$ of the circle lies on (1) or not

$$
\begin{aligned}
& 0-\frac{y_{1}+y_{2}}{2}=\frac{-\left(x_{2}-x_{1}\right)}{\left(y_{2}-y_{1}\right)}\left(0-\frac{x_{1}+x_{2}}{2}\right) \\
\text { or } & -\left(\frac{y_{1}+y_{2}}{2}\right)\left(y_{2}-y_{1}\right)=\left(x_{2}-x_{1}\right) \frac{\left(x_{1}+x_{2}\right)}{2} \\
\text { or } & -\left(y_{2}^{2}-y_{1}^{2}\right)=x_{2}^{2}-x_{1}^{2} \text { or } x_{1}^{2}+y_{1}^{2}=x_{2}^{2}+y_{2}^{2} \\
\text { or } & a^{2}=a^{2} \quad \text { which is true }
\end{aligned}
$$

Hence the perpendicular bisector of any chord passes through the centre of the circle.

## Theorem 4:

The line joining the centre of a circle to the midpoint of a chord is perpendicular to the chord.

Proof: $\quad$ Let $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$ be the end points of any chord the circle $x^{2}+y^{2}=a^{2} . O(0,0)$

is centre of the circle and *M* [ *x*<sup>1</sup> + *x*<sup>2</sup> + *y*<sup>1</sup> + *y*<sup>2</sup> ] is the midpoint of *AB*. Join the centre *O* with the mid point *M*. We need to show that *OM* is perpendicular to *AB* i.e., product of slopes of *AB* and *OM* is –1.

Slope of *AB* = *m*<sup>1</sup> = *x*<sup>1</sup> − *y*<sup>1</sup> *x*<sup>2</sup> − *x*<sup>1</sup> Slope of *OM* *m*<sup>2</sup> = *x*<sup>2</sup> − *y*<sup>2</sup> *x*<sup>2</sup> − *x*<sup>1</sup> *x*<sup>2</sup> − *x*<sup>1</sup> *2*

∴ *m*<sup>1</sup>*m*<sup>2</sup> = *x*<sup>2</sup> − *y*<sup>2</sup> *x*<sup>2</sup> + *y*<sup>1</sup> *x*<sup>2</sup> = *y*<sup>2</sup> − *x*<sup>1</sup> *x*<sup>2</sup> − *x*<sup>1</sup> *2*

As *A* and *B* lie on the circle, so

*x*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup> and *x*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup>

Their subtraction gives *x*<sup>2</sup> − *x*<sup>2</sup> + *y*<sup>2</sup> − *y*<sup>2</sup> = θ

or *y*<sup>2</sup> − *y*<sup>2</sup> = *x*<sup>2</sup> − *x*<sup>2</sup> = −(*x*<sup>2</sup> − *x*<sup>1</sup>)

Putting this value in (1), we get

*m*<sup>1</sup>*m*<sup>1</sup> = *x*<sup>2</sup> − *x*<sup>1</sup> *x*<sup>2</sup> = 1

So *OM* is perpendicular to *AB*.

**Theorem 5:** Congruent chords of a circle are equidistant from the centre.

**Proof:** Let *x*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup> be the circle in which *AB* and *CD* are two congruent chords i.e., |*AB*| = |*CD*| and the coordinates of *A*, *B*, *C* and *D* be as in the figure. Also let *OM* and *ON* be the perpendicular distances of the chords from the centre (0, 0)(*x*<sub>1</sub>, *y*<sub>1</sub> of the circle.

We know from Theorem 2 that *M* and *N* are the midpoints of *AB* and *CD* respectively.

*version: 1.1*

$$
\begin{aligned}
\therefore \left| OM \right|^2 &= \left( \frac{y_1 + y_2}{2} - \theta \right)^2 + \left( \frac{x_1 + x_2}{2} - \theta \right)^2 = \frac{y_1^2 + y_2^2 + x_1^2 + x_2^2 + 2x_1x_2 + 2y_1y_2}{4} \\
&= \frac{(x_1^2 + y_2^2) + (x_2^2 + y_2^2) + 2x_1x_2 + 2y_1y_2}{4} \\
&= \frac{a^2 + a^2 + 2x_1x_2 + 2y_1y_2}{4} \quad (\because A \text{ and } B \text{ lie on the circle.}) \\
&\left| OM \right|^2 &= \frac{2a^2 + 2x_1x_2 + 2y_1y_2}{4} \\
&= \frac{a^2 + x_1x_2 + y_1y_2}{2} \\
&\text{Similarly }\left| ON \right|^2 &= \frac{a^2 + x_2x_2 + y_2y_2}{2} \\
&\text{We know that }\left| AB \right|^2 = \left| CD \right|^2 \quad (\because \text{ chords are congruent}) \\
&\text{or } (x_2 - x_1)^2 + (y_2 - y_1)^2 = (x_4 - x_1)^2 + (y_4 - y_2)^2 \\
&\text{or } x_2^2 + x_1^2 + y_2^2 + y_1^2 - 2x_1x_2 - 2y_1y_2 = x_4^2 + x_2^2 - 2x_1x_4 + y_2^2 + y_2^2 - 2y_1y_4 \\
&\text{or } a^2 + a^2 - 2x_1x_2 - 2y_1y_2 = a^2 + a^2 - 2x_1x_4 - 2y_1y_4 \quad (\because x_1^2 + y_1^2 = a^2 \text{ etc}) \\
&\text{or } 2a^2 - 2x_1x_2 - 2y_1y_2 = 2a^2 - 2x_2x_4 - 2y_1y_4 \\
&\text{or } x_1x_2 + y_1y_2 = x_2x_4 + y_1y_4 \quad \text{(3)} \\
&\text{or }\left| OM \right|^2 = \left| ON \right|^2
\end{aligned}
$$

**Challenges**

State and prove the converse of this Theorem.

**Theorem 6:** Show that measure of the central angle of a minor arc is double the measure of the angle subtended in the corresponding major arc.

**Proof:** Let the circle be *x*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup>. *A*(*a* cosθ<sub>1</sub>, *a* sinθ<sub>1</sub>) and *B*(*a* cosθ<sub>2</sub>, *a* sinθ<sub>2</sub>) be end points of a minor arc *AB*. Let *P* (*a* cosθ, *a* sinθ) be a point on the major arc. Central angle subtended by the minor arc *AB* is ∠ *AOB* = θ<sub>2</sub> − θ<sub>1</sub>.

We need to show *m*∠*APB* = $$\frac{1}{2} \left( \theta_1 - \theta_1 \right)$$

$$
\begin{aligned}
m_{1}= & \text { slope of } A P \quad \frac{a(\sin \theta-\sin \theta_{1})}{a(\cos \theta-\cos \theta_{1})} \quad \frac{2 \cos \theta+\theta_{1}}{2} \sin \frac{\theta-\theta_{1}}{2} \\
& =\cot \left(\frac{\theta+\theta_{1}}{2}\right)-\tan \left(\frac{\pi}{2}-\frac{\theta+\theta_{1}}{2}\right)
\end{aligned}
$$

Similarly, (by symmetry)

$$
\begin{aligned}
& m_{2}=\text { slope-of } B P \quad+\tan \left(\frac{\pi}{2}-\frac{\theta+\theta_{2}}{2}\right) \\
& \tan \angle A P B=\frac{m_{2}-m_{1}}{1+m_{1} m_{2}}=\frac{\tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{2}}{2}\right)-\tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{1}}{2}\right)}{1+\tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{1}}{2}\right) \tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{2}}{2}\right)} \\
& =\tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{2}}{2}-\frac{\pi}{2}-\frac{\theta+\theta_{1}}{2}\right)=\tan \left(\frac{\theta_{2}-\theta_{1}}{2}\right) \\
& \text { Hence } m \angle A P B=\frac{1}{2}\left(\theta_{2}-\theta_{1}\right)
\end{aligned}
$$

Theorem 7: An angle in a semi-circle is a right angle.
Proof: Let $x^{2}+y^{2}=a^{2}$ be a circle, with centre $O$. Let $A O B$ be any diameter of the circle and $P\left(x_{1}, y_{1}\right)$ be any point on the circle.

We have to show that $m \angle A P B=90^{\circ}$.
Suppose the coordinates of $A$ are $\left(x_{1}, y_{1}\right)$.
Then $B$ has coordinates
$\left\{-x_{1},-y_{1}\right\}$.
(Slope of $A P=\frac{y_{1}-y_{2}}{x_{1}-x_{2}}=m_{1}$, say
Slope of $B P=\frac{y_{1}+y_{2}}{x_{1}+x_{2}}=m_{2}$, say
Challenged
State and prove the converse of this Theorem.

$$
m_{1} m_{2}=\frac{y_{1}^{2}-y_{2}^{2}}{x_{1}^{2}-x_{2}^{2}}
$$

Since $A\left(x_{1}, y_{1}\right)$ and $P\left(x_{2}, y_{2}\right)$ lie on the circle, we have

$$
\begin{aligned}
& x_{1}^{2}+y_{1}^{2}=a^{2} \Rightarrow x_{1}^{2}=a^{2}-y_{1}^{2} \\
& x_{2}^{2}+y_{2}^{2}=a^{2} \Rightarrow x_{2}^{2}=a^{2}-y_{2}^{2}
\end{aligned}
$$

Substituting the values of $x_{1}^{2}$ and $x_{2}^{2}$ from (2) into (1), we get

$$
m_{1} m_{2}=\frac{y_{1}^{2}-y_{2}^{2}}{\left(a^{2}-y_{1}^{2}\right)-\left(a^{2}-y_{2}^{2}\right)}=\frac{y_{1}^{2}-y_{2}^{2}}{-\left(y_{1}^{2}-y_{2}^{2}\right)}=-1
$$

Thus $A P \perp B P$ and so $m \angle A P B=90^{\circ}$

Theorem 8: The tangent to a circle at any point of the circle is perpendicular to the radial segment at that point.

Proof: Let $P T$ be the tangent to the circle $x^{2}+y^{2}=a^{2}$ at any point $P\left(x_{1}, y_{1}\right)$ lying on it. We have to show that the radial segment $O P \perp P T$.

Differentiating $x^{2}+y^{2}=a^{2}$, we have

$$
2 x+2 y \frac{d y}{d x}=0 \Rightarrow \frac{d y}{d x}=\frac{x}{y}
$$

Slope of the tangent at $P=\frac{d y}{d x} \frac{1}{2}=\frac{-x_{1}}{y_{1}}$
Slope of $O P=\frac{y_{1}-0}{x_{1}-0}-\frac{y_{1}}{x_{1}}$
Product of slopes of $O P$ and $P T=\frac{-x_{1}}{y_{1}} \frac{y_{1}}{x_{1}}=-1$
Thus $O P \perp P T$.

Theorem 9: The perpendicular at the outer end of a radial segment is tangent to the circle.

Proof: Let $P T$ be the perpendicular to the outer end of the radial segment $O P$ of the circle $x^{2}+y^{2} \equiv a^{2}$. We have to show that $P T$ is tangent to the circle at $P$. Suppose the coordinates of $P$ are $\left(x_{1}, y_{1}\right)$.

Since $P T$ is perpendicular to $O P$ so
Slope of $P T=\frac{-1}{\text { slope of } O P} \cdot \frac{-1}{y_{1}} \cdot \frac{-x_{1}}{y_{1}}$
Equation of $P T$ is $y-y_{1}=\frac{-x_{1}}{y_{1}}\left(x-x_{1}\right)$
or $y y_{1}-y^{2}=-x x_{1}+x_{1}^{2}$
or $y y_{1}+x x_{1}=y_{1}^{2}+x_{1}^{2}=a^{2} \quad(\because P$ lies on the circle $)$
or $y y_{1}+x x_{1}-a^{2}=0$
Distance of $P T$ from $O$ (centre of the circle)

$$
=\frac{\left[y_{1}(0)+x_{1}(0)-a^{2}\right]}{\sqrt{x^{2}+y^{2}}} \cdot \frac{\left|a^{2}\right|}{\sqrt{a^{2}}} \cdot \frac{a^{2}}{a} \quad a \quad \text { (radius of the circle) }
$$

Thus $P T$ is tangent to the circle at $P\left(x_{1}, y_{1}\right)$.

## EXERCISE 6.3

1. Prove that normal lines of a circle pass through the centre of the circle.
2. Prove that the straight line drawn from the centre of a circle perpendicular to a tangent passes through the point of tangency.
3. Prove that the mid point of the hypotenuse of a right triangle is the circumcentre of the triangle.
4. Prove that the perpendicular dropped from a point of a circle on a diameter is a mean proportional between the segments into which it divides the diameter.

In the following pages we shall study the remaining three conics.
Let $L$ be a fixed line in a plane and $F$ be a fixed point not on the line $L$.

Suppose $|P M|$ denotes the distance of a point $P(x, y)$ from the line $L$. The set of all points $P$ in the plane such that

$$
\frac{|P F|}{|P M|}=e . \quad(\text { a positive constant })
$$

is called a conic section.
(i) If $e \equiv 1$, then the conic is a parabola.
(ii) If $0<e<1$, then the conic is an ellipse.
(iii) If $e>1$, then the conic is a hyperbola.

The fixed line $L$ is called a directrix and the fixed point $F$ is called a focus of the conic. The number e is called the eccentricity of the conic.