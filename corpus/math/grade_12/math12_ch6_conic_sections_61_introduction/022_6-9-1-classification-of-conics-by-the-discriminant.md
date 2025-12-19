### 6.9.1 Classification of Conics by the Discriminant

The most general equation of the second degree

$$
\alpha x^{2}+2 h x y+b y^{2}+2 g x+2 f y+c=0
$$

represents a conic. The quantity $h^{2}-a b$ is called the discriminant of (1). Nature of the conic can be determined by the discriminant as follows. (1) represents:
(i) an ellipse or a circle if $h^{2}-a b<0$
(ii) a parabola if $h^{2}-a b=0$
(iii) a hyperbola if $h^{2}-a b>0$

The equation (1) can be transformed to the form

$$
A X^{2}+B Y^{2}+2 G X+2 F y+C=0
$$

if the axes are rotated about the origin through an angle $\theta,\left(0<\theta<90^{\circ}\right)$ where $\theta$ is given by

$$
\tan 2 \theta=\frac{2 h}{a-b}
$$

If $a=b$ or $a=0=b$, then the axes are to be rotated through an angle of $45^{\circ}$.
Equations of transformation (as already found) are

$$
\left.\begin{array}{l}
x=X \cos \theta-Y \sin \theta \\
y=X \sin \theta+Y \cos \theta
\end{array}\right\}
$$

Substitution of these values of $x, y$ into (1) will result in an equation of the form (2) in which product term $X Y$ will be missing. Nature of the conic (2) has already been discussed in the last article.

Solving equations (3) for $X, Y$ we find

$$
\left.\begin{array}{l}
X=x \cos \theta+y \sin \theta \\
Y=\pi \sin \theta \quad y \cos \theta
\end{array}\right\}
$$

These equations will be useful in numerical problems.
Note: Under certain conditions equation (1) may not represent any conic, in such a case we say (1) represents a degenerate conic.

One such degenerate conic is a pair of straight lines represented by (1) if

$$
\left.\begin{array}{lll}
a & h & g \\
h & b & f \\
g & f & c
\end{array}\right\}=0
$$

The proofs of the above observations are beyond our scope and are omitted.

## Example 1: $\quad$ Discuss the conic $7 x^{2}-6 \sqrt{3} x y+13 y^{2}-16=0$ and find its elements.

Solution. In order to remove the term involving $x y$, the angle through which axes be rotated is given by

$$
\tan 2 \theta=\frac{-6 \sqrt{3}}{7-13}=\sqrt{3} \quad{ }^{\circ} \text { or } \quad \theta \approx 30
$$

Equations of transformation are

$$
\begin{aligned}
& x=X \cos 30^{\circ}-Y \sin 30^{\circ}=\frac{\sqrt{3} X-Y}{2} \\
& y=X \sin 30^{\circ}+Y \cos 30^{\circ}=\frac{X+\sqrt{3} Y}{2}
\end{aligned}
$$

Substituting these expressions in to the equation (1), we get

$$
\sqrt[3]{\left(\frac{\sqrt{3} X-Y}{2}\right)^{2}-6 \sqrt{3}\left(\frac{\sqrt{3} X-Y}{2}\right)\left(\frac{X+\sqrt{3} Y}{2}\right)}+13\left(\frac{X+\sqrt{3} Y}{2}\right)^{2}=16
$$

which simplifies to

$$
4 X^{2}+16 Y^{2}=16+\quad \text { or } \quad \frac{X^{2}}{4} \quad \frac{Y^{2}}{1} \quad 1
$$

This is an ellipse.
Solving equations (2) for $X$ and $Y$, (or as already found in (4) of 7.7.1, we have

$$
X=\frac{\sqrt{3} x+y}{2}, \quad Y \quad \frac{-x+\sqrt{3} y}{2}
$$

Centre of the ellipse (3) is $X=0, Y=0$
i.e., $\quad \sqrt{3} x+y=0-\quad+$ and $=\quad x \quad \sqrt{3} y \quad 0$
giving $\quad x=0, y=0$. Thus centre of (1) is $(0,0)$
Length of the major axis $=4$, length of minor axis $=2$
Vertices of (3) are: $\quad X=\pm 2, Y=0$

$$
\text { i.e., } \quad \frac{\sqrt{3} x+y}{2}=2 \quad \text { and } \quad \frac{-x+\sqrt{3} y}{2} \quad 0
$$

Solving these equations for $x, y$, we have

$$
(\sqrt{3}, 1),(-\sqrt{3},-1), \text { as vertices of }(1)
$$

Ends of the minor axis are $X=0$ and $Y=1$ i.e., $\frac{\sqrt{3} x+y}{2} \quad 0$ and $\frac{-x+\sqrt{3} y}{2}= \pm 1$. Solving these equations, we get $\left(\frac{1}{2}, \frac{-\sqrt{3}}{2}\right)$ and $\left(-\frac{1}{2}, \frac{\sqrt{3}}{2}\right)$
as ends of the minor axis of (1).
Equation of the major axis: $Y=0$,
i.e.,

$$
-x+\sqrt{3} y=0
$$

Equation of the minor axis: $X=0$,
i.e., $\sqrt{3} x+y=0$

Example 2: Analyze the conic $x y=4$ and write its elements.
Solution: Equation of the conic is

$$
x y-4=0
$$

Here $a=0=b$, so we rotate the axes through an angle of $45^{\circ}$. Equations of transformation are

$$
\begin{aligned}
& x=X \cos 45^{\circ}-Y \sin 45^{\circ}=\frac{X-Y}{\sqrt{2}} \\
& y=X \sin 45^{\circ}-Y \cos 45^{\circ}=\frac{X+Y}{\sqrt{2}}
\end{aligned}
$$

Substituting into (1), we have

$$
\left(\frac{X-Y}{\sqrt{2}}\right)\left(\frac{X+Y}{\sqrt{2}}\right)-4=0
$$

or $X^{2}-Y^{2}=8$

$$
\frac{X^{2}}{8} \cdot \frac{Y^{2}}{8}=1
$$

which is a hyperbola.
Solving equations (2) for $X, Y$, we have

$$
X=\frac{x+y}{\sqrt{2}}, \quad Y \quad \frac{-x+y}{\sqrt{2}}
$$

Centre of the hyperbola (3) is

$$
X=0, Y=0
$$

i.e., $\frac{x+y}{\sqrt{2}}=0, \quad$ and $\frac{-x+y}{\sqrt{2}} \quad 0$
or $\quad x=0, \quad y=0$ is the centre of (1)
Equation of the focal axis:
$Y=0$ i.e. $y=x$.
Equation of the conjugate axis: $X=0$ i.e. $y=-x$.
Eccentricity $=\sqrt{2}$
Foci of (3): $X=2 \sqrt{2} \cdot \sqrt{2} \quad \pm Y \quad 0$
or $\quad x+y= \pm 4 \sqrt{2}$
and $-x+y=0$
Solving the above equations for $x, y$, we have the foci of (1) as $(2 \sqrt{2}, 2 \sqrt{2})$ and $(-2 \sqrt{2},-2 \sqrt{2})$
Vertices of (3): $X=2 \sqrt{2}, \quad Y \quad 0$
i.e., $\frac{x+y}{\sqrt{2}}= \pm 2 \sqrt{2}$ and $-x+y=0$

Solving these equations, we have the foci of (1) as

$$
(2 \sqrt{2}, 2 \sqrt{2}) \text { and }(-2 \sqrt{2},-2 \sqrt{2})
$$

Vertices of (3): $X=2 \sqrt{2}, \quad Y \quad 0$

$$
\frac{x+y}{\sqrt{2}}= \pm 2 \sqrt{2} \quad \text { and } \quad-x+y=0
$$

Solving these equations, we have
$(2,2),(-2,-2)$ as vertices of (1).
Asymptotes of the hyperbola (3) are given by $X^{2}-Y^{2}=0$
or $\quad X-Y=0 \quad$ and $\quad X+Y=0$
i.e., $\frac{x+y}{\sqrt{2}}-\frac{-x+y}{\sqrt{2}}=0$ and $\frac{x+y}{\sqrt{2}}-\frac{-x+y}{\sqrt{2}}=0$
i.e., $x=0$ and $y=0$ are equations of the asymptotes of (1).

Example 3: By a rotation of axes, eliminate the $x y$-term in the equation

$$
9 x^{2}+12 x y+4 y^{2}+2 x-3 y=0
$$

Identify the conic and find its elements.

Solution: Here $a=9, b=4,2 h=12$. The angle $\theta$ through which axes be rotated to given by

$$
\begin{aligned}
& \tan 2 \theta=\frac{12}{9-4}=\frac{12}{5} \\
& \text { or } \quad \frac{2 \tan \theta}{1-\tan ^{2} \theta}=\frac{12}{5} \\
& \text { or } 5 \tan \theta=6-6 \tan ^{2} \theta \\
& \text { or } 6 \tan ^{2} \theta+5 \tan \theta-6=0 \\
& \tan \theta=\frac{-5 \pm \sqrt{25+144}}{12}=\frac{-5 \pm 13}{12} \quad \frac{2}{3}, \frac{-3}{2}
\end{aligned}
$$

Since $\theta$ lies in the first quadrant, $\tan \theta=-\frac{2}{3}$ is not admissible.

$$
\tan \theta=\frac{2}{3} \Rightarrow \quad \sin \theta \quad \frac{2}{\sqrt{13}}, \quad \cos \theta \quad \frac{3}{\sqrt{13}}
$$

Equations of transformation become

$$
\begin{aligned}
& x=X \cos \theta-Y \sin \theta=\frac{2}{\sqrt{13}} X-\frac{2}{\sqrt{13}} Y \\
& y=X \sin \theta+Y \cos \theta=\frac{2}{\sqrt{13}} X+\frac{3}{\sqrt{13}} Y
\end{aligned}
$$

Substituting these expressions for $x$ and $y$ into (1), we get

$$
\begin{aligned}
& \frac{9}{(\sqrt{13})^{2}}(3 X-2 Y)^{2}+\frac{12}{13}(3 X-2 Y)(3 X+3 Y)+\frac{4}{13}(2 X+3 Y)^{2} \\
& +\frac{2}{\sqrt{13}}(3 X-2 Y)-\frac{3}{\sqrt{13}}(2 X+3 Y)=0 \\
& \text { or } \quad \frac{9}{13}\left(9 X^{2}-12 X Y+9 Y^{2}\right)+\frac{12}{13}\left(6 X^{2}+5 X Y-6 Y^{2}\right) \\
& +\frac{4}{13}\left(4 X^{2}+12 X Y-9 Y^{2}\right)-\sqrt{13} Y=0 \\
& \text { or } \quad\left(\frac{81}{13}+\frac{72}{13}+\frac{16}{13}\right) X^{2}+\left(-\frac{108}{13}+\frac{60}{13}+\frac{48}{13}\right) X Y \\
& +\left(\frac{36}{13}-\frac{72}{13}+\frac{36}{13}\right) Y^{2}-\sqrt{13} Y=0
\end{aligned}
$$

or $13 X^{2}-\sqrt{13} Y=0 \quad$ or $\quad X^{2} \quad \frac{1}{\sqrt{13}} Y$
which is a parabola.
Solving equation (2) for $X, Y$, we have $X=\frac{3 x+2 y}{\sqrt{13}}, Y=\frac{-2 x+3 y}{\sqrt{13}}$
Elements of the parabola are:
Focus: $X=0, \quad Y=\frac{1}{4 \sqrt{13}}$
i.e., $\frac{3 x+2 y}{\sqrt{13}}=\theta \quad$ and $\quad \frac{-2 x+3 y}{\sqrt{13}} \quad \frac{1}{4 \sqrt{13}}$

Solving these equations, we have $x=\frac{1}{26}, y \quad \frac{3}{52}$ i.e., Focus $\left(\frac{1}{26}, \frac{3}{52}\right)$
Vertex: $\quad X=0, \quad Y=0 \quad$ i.e., $\quad 3 x+2 y=0$ and $-2 x+3 y=0$
i.e., $\quad x=0, \quad y=0 \quad$ i.e., $(0,0)$

Axis: $\quad X=0 \quad$ i.e., $\quad 3 x+2 y=0$

$$
x \text {-intercept }=-\frac{2}{9}, \quad y \text {-intercept }=\frac{3}{4}
$$

Example 4: $\quad$ Show that $2 x^{2}-x y+5 x-2 y+2=0$ represents a pair of lines. Also find an equation of each line.

Solution: Here $a=2, b=0, h=\frac{1}{2}, g \quad \frac{5}{2}, f \quad 1, c=2$.

$$
\begin{gathered}
\left|\begin{array}{ccc}
a & h & g \\
h & b & f \\
g & f & c
\end{array}\right|=\left|\begin{array}{ccc}
2 & -\frac{1}{2} & \frac{5}{2} \\
\frac{1}{2} & 0 & 1 \\
\frac{5}{2} & -1 & 2 \\
\end{array}\right| \\
=\frac{1}{2}\left(-1+\frac{5}{2}\right)+1\left(-2+\frac{5}{4}\right)
\end{gathered}
$$

$$
-\frac{3}{4}-\frac{3}{4}=0
$$

The given equation represents a degenerate conic which is a pair of lines. The given equation is

$$
\begin{aligned}
& 2 x^{2}+x(5-y)+(-2 y+2)=0 \\
\text { or } \quad & x=\frac{y-5 \pm \sqrt{(y-5)^{2}-h(-2 y+2)}}{4} \\
& =\frac{y-5 \pm \sqrt{y^{2}-10 y+25+16 y-16}}{4} \\
& =\frac{y-5 \pm(y+3)}{4} \\
& =\frac{2 y-2}{4}, \quad-2
\end{aligned}
$$

Equations of the lines are $2 x-y+1=0$ and $x+2=0$.

## Tangent

Find an equation of the tangent to the conic

$$
a x^{2}+2 h x y+b y^{2}+2 g x+2 f y+c=0
$$

at the point $\left(x_{1}, y_{1}\right)$
Differentiating (1) w.r.t. $\quad x$, we have

$$
2 a x+2 h y+2 h x \frac{d y}{d x}+2 b y \frac{d y}{d x}+2 g+2 f \frac{d y}{d x}=0
$$

or $\quad \frac{d y}{d x}=-\frac{a x+h y+g}{h x+b y+f}$
or $\left.\frac{d y}{d x}\right|_{x_{1}, y_{1}}=-\frac{a x_{1}+h y_{1}+g}{h x_{1}+b y_{1}+f}$
Equation of the tangent at $\left(x_{1}, y_{1}\right)$ is

$$
y-y_{1}=-\frac{a x_{1}+h y_{1}+g}{h x_{1}+b y_{1}+f}\left(x_{1}, y_{1}\right)
$$

or $\quad(x-x_{1})\left(a x_{1}+h y_{1}+g\right)+(y-y_{1})\left(h x_{1}+b y_{1}+f\right)=0$
or $\quad a x x_{1}+h x y_{1}+g x++h x_{1} y+b y_{1} y+f y$

$$
=a x_{1}^{2}+2 h x_{1} y_{1}+g x_{1}+b y_{1}^{2}+f y_{1}
$$

Adding $g x_{1}+f y_{1}+c$ to both sides of the above equation and regrouping the terms, we have

$$
\begin{aligned}
& a x x_{1}+h\left(x y_{1}+y x_{1}\right)+b y y_{1}+g\left(x+x_{1}\right)+f\left(y+y_{1}\right)+c \\
& =a x_{1}^{2}+2 h x_{1} y_{1}+b y_{1}^{2}+2 g x_{1}+2 f y_{1}+c \\
& =0
\end{aligned}
$$

since the point $\left(x_{1}, y_{1}\right)$ lies on (1).
Hence an equation of the tangent to (1) at $\left(x_{1}, y_{1}\right)$ is

$$
a x x_{1}+h\left(x y_{1}+y x_{1}\right)+b y y_{1}+g\left(x+x_{1}\right)+f\left(y+y_{1}\right)+c=0
$$

Note: An equation of the tangent to the general equation of the second degree at the point $\left(x_{1}, y_{1}\right)$ may be obtained by replacing

$$
\begin{aligned}
& x^{2} \text { by } x x_{1} \\
& y^{2} \text { by } y y_{1} \\
& 2 x y \text { by } x y_{1}+y x_{1} \\
& 2 x \text { by } x+x_{1} \\
& 2 y \text { by } y+y_{1}
\end{aligned}
$$

in the equation of the conic
Example 5: Find an equation of the tangent to the conic $x^{2}-x y+y^{2}-2=0$ at the point whose ordinate is $\sqrt{2}$.

Solution: Putting $y=\sqrt{2}$ into the given equation, we have

$$
\begin{aligned}
& x^{2}-\sqrt{2} x=0 \\
& x(x-\sqrt{2})=0 \quad x=0, \sqrt{2}
\end{aligned}
$$

The two points on the conic are $(0, \sqrt{2})$ and $(\sqrt{2}, \sqrt{2})$.
Tangent at $(0, \sqrt{2})$ is

$$
0, x-\frac{1}{2}(x \sqrt{2}+0, y)+\sqrt{2} y-2=0
$$

or $\quad x-2 y+2 \sqrt{2}=0$
Tangent at $(\sqrt{2}, \sqrt{2})$ is

$$
\sqrt{2} x-\frac{1}{2}(\sqrt{2} x+\sqrt{2} y)+\sqrt{2} y-2=0
$$

or $\quad \sqrt{2} x+\sqrt{2} y-4=0$

# EXERCISE 6.9

1. By a rotation of axes, eliminate the $x y$-term in each of the following equations. Identify the conic and find its elements:
(i) $4 x^{2}-4 x y+y^{2}-6=0$
(ii) $x^{2}-2 x y+y^{2}-8 x-8 y=0$
(iii) $x^{2}+2 x y+y^{2}+2 \sqrt{2}-2 \sqrt{2} y+2=0$
(iv) $x^{2}+x y+y^{2}-4=0$
(v) $7 x^{2}-6 \sqrt{3} x y+13 y^{2}-16=0$
(vi) $4 x^{2}-4 x y+7 y^{2}+12 x+6 y-9=0$
(vii) $x y-4 x-2 y=0$
(viii) $x^{2}+4 x y-2 y^{2}-6=0$
(ix) $x^{2}-4 x y-2 y^{2}+10 x+4 y=0$
2. Show that
(i) $10 x y+8 x-15 y-12=0$ and
(ii) $6 x^{2}+x y-y^{2}-21 x-8 y+9=0$
each represents a pair of straight lines and find an equation of each line.
3. Find an equation of the tangent to each of the given conics at the indicated point.
(i) $3 x^{2}-7 y^{2}+2 x-y-48=0$ at $(4,1)$
(ii) $x^{2}+5 x y-4 y^{2}+4=0$ at $y=-1$
(iii) $x^{2}+4 x y-3 y^{2}-5 x-9 y+6=0$ at $x=3$.