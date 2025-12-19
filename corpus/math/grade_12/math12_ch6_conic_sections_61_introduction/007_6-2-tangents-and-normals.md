### 6.2 TANGENTS AND NORMALS

A tangent to a curve is a line that touches the curve without cutting through it. We know that for any curve whose equation is given by $y=f(x)$ or $f(x, y)=0$, the derivative is slope of the tangent at any point $P(x, y)$ to the curve. The equation of the tangent to the curve can easily be written by the pointslope formula. The normal to the curve at $P$ is the line through $P$ perpendicular to the tangent to the curve at $P$. This method can be very

conveniently employed to find equations of tangent and normal to the circle $x^{2}+y^{2}+2 g x+2 f y+c=0$ at the point $P\left(x_{1}, y_{1}\right)$.
Here $\quad f\left(x_{1} y\right)=x^{2}+y^{2}+2 g x+2 f y+c=0$
Differentiating (1) w.r.t. $x$, we get

$$
\begin{aligned}
& 2 x+2 y \frac{d y}{d x}+2 g+2 f \frac{d y}{d x}=0 \text { or } \quad \frac{d y}{d x}=\frac{x+g}{y+f} \\
& \left.\frac{d y}{d x}\right]_{x_{1}, y_{1}}=-\frac{x_{1}+g}{y_{1}+f}=\text { Slope of the tangent at }\left(x_{1}, y_{1}\right)
\end{aligned}
$$

Equation of the Tangent at $P$ is given by

$$
\begin{aligned}
& y-y_{1}=-\frac{x_{1}+g}{y_{1}+f}\left(x-x_{1}\right) \quad \text { (Point-slope form) } \\
& \text { or } \quad y\left(y_{1}+f\right)-y_{1}^{2}-y_{1} f=-x\left(x_{1}+g\right)+x_{1}^{2}+x_{1} g \\
& \text { or } \quad x x_{1}+y y_{1}+g x+f y=x_{1}^{2}+y_{1}^{2}+g x_{1}+f y_{1} \\
& \text { or } \quad x x_{1}+y y_{1}+g x+f y+g x_{1}+f y_{1}+c=x_{1}^{2}+y_{1}^{2}+g x_{1}+f y_{1}+g x_{1}+f y_{1}+c \\
& \text { (adding } g x_{1}+f y_{1}+c \text { to both sides) } \\
& x x_{1}+y y_{1}+g\left(x+x_{1}\right)+f\left(y+y_{1}\right)+c=0 \\
& \text { since } \quad\left(x_{1}, y_{1}\right) \text { lies on (1) and so } \\
& x_{1}^{2}+y_{1}^{2}+2 g x_{1}+2 f y_{1}+c=0
\end{aligned}
$$

Thus $\frac{\left(x_{1}+y y_{1}+g\left(x+x_{1}\right)+f\left(y+y_{1}\right)+c=0\right)}{x_{1}+g}$ is the required equation of the tangent.
To find an equation of the normal at $P$, we note that slope of the normal is

$$
\frac{y_{1}+f}{x_{1}+g} \quad \text { (negative reciprocal of slope of the tangent) }
$$

Equation of the normal at $P\left(x_{1}, y_{1}\right)$ is

$$
y-y_{1}=\frac{y_{1}+f}{x_{1}+g}\left(x-x_{1}\right)
$$

or $\quad \frac{\left(y-y_{1}\right)\left(x_{1}+g\right)=\left(x-x_{1}\right)\left(y_{1}+f\right)}{x_{1}+g}$ is an equation of the normal at $\left(x_{1}, y_{1}\right)$.

## Theorem:

The point $P\left(x_{1}, y_{1}\right)$ lies outside, on or inside the circle $x^{2}+y^{2}+2 g x+2 f y+c=0$ according as

$$
x_{1}^{2}+y_{1}^{2}+2 g x_{1}+2 f y_{1}+c \stackrel{\infty}{\times} \mid 0
$$

Proof. Radius $r$ of the given circle is

$$
r=\sqrt{g^{2}+f^{2}-c}
$$

The point $P\left(x_{1}, y_{1}\right)$ lies outside, on or inside the circle, according as:

$$
m[C P] \stackrel{\infty}{\times} \mid r
$$

i.e., according as: $\quad \sqrt{\left(x_{1}+g\right)^{2}+\left(y_{1}+f\right)^{2}} \stackrel{\infty}{\times} \sqrt{g^{2}+f^{2}-c}$
or according as : $\quad x_{1}^{2}+2 g x_{1}+g^{2}+y_{1}^{2}+f^{2}+2 f y_{1} \stackrel{\infty}{\times} \sqrt[2]{g^{2}+f^{2}-c}$
or according as : $\quad x_{1}^{2}+y_{1}^{2}+2 g x_{1}+2 f y_{1}+c \stackrel{\infty}{\times} \mid 0$.
Example 1: Determine whether the point $P(-5,6)$ lies outside, on or inside the circle: $x^{2}+y^{2}+4 x-6 y-12=0$

Solution: Putting $x=-5$ and $y=6$ in the left hand member of the equation of the circle, we get

$$
25+36-20-36-12=-7<0
$$

Thus the point $P(-5,6)$ lies inside the circle.
Theorem: The line $y=m x+c$ intersects the circle $x^{2}+y^{2}=a^{2}$ in at the most two points.
Proof: It is known from plane geometry that a line can meet a circle in at the most two points.

To prove it analytically, we note that the coordinates of the points where the line

$$
\begin{aligned}
& y=m x+c \\
& \text { intersects the circle } \\
& x^{2}+y^{2}=a^{2}
\end{aligned}
$$

are the simultaneous solutions of the equations (1) and (2).
Substituting the value of $y$ from equation (1) into equation (2), we get

$$
x^{2}+(m x+c)^{2}=a^{2}
$$

or $\quad x^{2}\left(1+m^{2}\right)+2 m c x+c^{2}-a^{2}=0$
This being quadratic in $x$, gives two values of $x$ say $x_{1}$ and $x_{2}$. Thus the line intersects the circle in at the most two points. For nature of the points we examine the discriminant of (3).

The discriminant of (3) is $\left(2 m c\right)^{2}-4\left(1+m^{2}\right)\left(c^{2}-a^{2}\right)$

$$
\begin{aligned}
& =4 m^{2} c^{2}-4\left(1+m^{2}\right)\left(c^{2}-a^{2}\right) \\
& =4 m^{2} c^{2}-4 m^{2} c^{2}-4\left(c^{2}-a^{2}-a^{2} m^{2}\right) \\
& =4\left[-c^{2}+a^{2}\left(1+m^{2}\right)\right]
\end{aligned}
$$

These points are
(i) Real and distinct, if $a^{2}\left(1+m^{2}\right)-c^{2}>0$
(ii) Real and coincident if $a^{2}\left(1+m^{2}\right)-c^{2}=0$
(iii) Imaginary if $a^{2}\left(1+m^{2}\right)-c^{2}<0$

## Condition that the line may be a tangent to the circle.

The line (1) is tangent to the circle (2) if it meets the circle in one point.
i.e., if $c^{2}=a^{2}\left(1+m^{2}\right)$ or $\varepsilon=\alpha \sqrt{1-m^{2}}$
is the condition for (1) to be a tangent to (2).
Example 2: Find the co-ordinates of the points of intersection of the line $2 x+y=5$ and the circle $x^{2}+y^{2}+2 x-9=0$. Also find the length of the intercepted chord.

Solution: From $2 x+y=5$, we have

$$
y=(5-2 x)
$$

Inserting this value of $y$ into the equation of the circle, we get

$$
\begin{aligned}
& x^{2}+(5-2 x)^{2}+2 x-9=0 \\
& \text { or } \quad 5 x^{2}-18 x+16=0 \\
& \Rightarrow \quad x=\frac{18 \pm \sqrt{324-320}}{10} \quad \frac{18 \pm 2}{10} \quad 2, \frac{8}{5}
\end{aligned}
$$

When $x=2, y=5-4=1$
When $x=\frac{8}{5}, y=5-\frac{16}{5}-\frac{9}{5}$

Thus the points of intersection are $P(2,1)$ and $Q\left(\frac{8}{5}, \frac{9}{5}\right)$
Length of the chord intercepted

$$
=\sqrt[3]{P Q}=\sqrt{\left(\frac{8}{5}-2\right)^{2}+\left(\frac{9}{5}-1\right)^{2}}=\sqrt{\frac{4}{25}-\frac{16}{25}}=\frac{2}{\sqrt{5}}
$$

Theorem: Two tangents can be drawn to a circle from any point $P\left(x_{1}, y_{1}\right)$. The tangents are real and distinct, coincident or imaginary according as the point lies outside, on or inside the circle.

Proof: Let an equation of the circle be $x^{2}+y^{2}=a^{2}$
We have already seen that the line

$$
y=m x+a \sqrt{1+m^{2}}
$$

is a tangent to the given circle for all values of $m$. If it passes through the point $P\left(x_{1}, y_{1}\right)$, then

$$
\begin{aligned}
& y_{1}=m x_{1}+a \sqrt{1+m^{2}} \\
& \text { or } \quad\left(y_{1}-m x_{1}\right)^{2}=a^{2}\left(1+m^{2}\right) \\
& \text { or } \quad m^{2}\left(x_{1}^{2}-a^{2}\right)-2 m x_{1} y_{1}+y_{1}^{2}-a^{2}=0
\end{aligned}
$$

This being quadratic in $m$, gives two values of $m$ and so there are two tangents from $P\left(x_{1}, y_{1}\right)$ to the circle. These tangents are real and distinct, coincident or imaginary according as the roots of (2) are real and distinct, coincident or imaginary
i.e., according as $x_{1}^{2} y_{1}^{2}-\left(x_{1}^{2}-a^{2}\right)\left(y_{1}^{2}-a^{2}\right) \stackrel{\text { o }}{=} 0$
or $\quad x_{1}^{2} a^{2}+y_{1}^{2} a^{2}+a^{2} \stackrel{\text { o }}{=} 0 \quad$ or $\quad x_{1}^{2}+y_{1}^{2}-a^{2} \stackrel{\text { o }}{=} 0$
i.e., according as the point $P\left(x_{1}, y_{1}\right)$ lies outside, on or inside the circle $x^{2}+y^{2}-a^{2}=0$

Example 3: Write equations of two tangents from $(2,3)$ to the circle $x^{2}+y^{2}=9$.
Solution. Any tangent to the circle is

$$
y=m x+3 \sqrt{1+m^{2}}
$$

If it passes through $(2,3)$, then

$$
\begin{aligned}
& 3=2 m+3 \sqrt{1+m^{2}} \\
\text { or } & (3-2 m)^{2} \equiv 9\left(1+m^{2}\right) \\
\text { or } & 9-12 m+4 m^{2} \equiv 9+9 m^{2} \\
& \text { or } \quad 5 m^{2}+12 m=0 \quad \text { i.e., } m=0, \frac{-12}{5}
\end{aligned}
$$

Inserting these values of $m$ into (1), we have equations of the tangents from $(2,3)$ to the circle as :

$$
\begin{aligned}
& \text { For } m=0: y=0 . x+3 \sqrt{1+0} \\
& \text { or } y=3 \\
& \text { For } m=\frac{-12}{5}: y=\frac{-12}{5} x+3 \sqrt{1+\frac{144}{25}}=\frac{-12}{5} x+\frac{39}{5} \\
& \text { or } \quad 5 y+12 x-39=0
\end{aligned}
$$

Example 4: Write equations of the tangents to the circle

$$
x^{2}+y^{2}-4 x+6 y+9 \equiv 0
$$

at the points on the circle whose ordinate is -2 .

Solution: Substituting $y=-2$ into (1), we get

$$
\begin{aligned}
& x^{2}-4 x+1 \equiv 0 \\
& \text { or } \quad x=\frac{4 \pm \sqrt{16-4}}{2} \quad \pm 2 \quad \sqrt{3}
\end{aligned}
$$

The points on the circle with ordinate -2 are

$$
(2+\sqrt{3},-2),(2-\sqrt{3},-2)
$$

Equations of the tangents to (1) at these points are

$$
\begin{aligned}
& (2+\sqrt{3}) x-2 y-2(x+2+\sqrt{3})+3(y-2)+9=0 \\
& \text { and } \quad(2-\sqrt{3}) x-2 y-2(x+2-\sqrt{3})+3(y-2)+9=0 \\
& \text { i.e., } \quad \sqrt{3} x+y-2 \sqrt{3}-1=0 \\
& \text { and } \quad-\sqrt{3} x+y+2 \sqrt{3}-1=0
\end{aligned}
$$

## Example 5: $\quad$ Find a joint equation to the pair of tangents drawn from $(5,0)$ to the circle: $x^{2}+y^{2}=9$

Solution: Let $P(h, k)$ be any point on either of the two tangents drawn from $A(5,0)$ to the given circle (1). Equation of $P A$ is

$$
y-0=\frac{k-0}{h-5}(x-5) \quad \text { or } k x-(h-5) y-5 k=0
$$

Since (2) is tangent to the circle (1), the perpendicular distance of (2) from the centre of the circle equals the radius of the circle.
i.e., $\quad \frac{|-5 k|}{\sqrt{k^{2}+(h-5)^{2}}}=3$
or $\quad 25 k^{2}=9\left[k^{2}+(h-5)^{2}\right]$ or $16 k^{2}-9(h-5)^{2}=0$
Thus $(h, k)$ lies on

$$
9(x-5)^{2}-16 y^{2} \equiv 0
$$

But $(h, k)$ is any point of either of the two tangents.
Hence (3) is the joint equations of the two tangents.