### 4. Two-point Form of Equation of a Straight Line:

**Theorem:** Equation of a non-vertical straight line passing through two points \( Q(x_1, y_1) \) and \( R(x_2, y_2) \) is

$$
y - y_1 = \frac{y_2 - y_1}{x_2 - x_1} (x - x_1) \text{ or } y - y_2 = \frac{y_2 - y_1}{x_2 - x_1} (x - x_2)
$$

**Proof:** Let \( P(x, y) \) be an arbitrary point of the line passing through \( Q(x_1, y_1) \) and \( R(x_2, y_2) \). So

$$
\frac{y - y_1}{x - x_1} = \frac{y - y_2}{x - x_2} = \frac{y_2 - y_1}{x_2 - x_1} \qquad (P, Q \text{ and } R \text{ are collinear points})
$$

We take

$$
\frac{y - y_1}{x - x_1} = \frac{y_2 - y_1}{x_2 - x_1}
$$

or

$$
y - y_1 = \frac{y_2 - y_1}{x_2 - x_1} (x - x_1) \text{ the required equation of the line } PQ.
$$

or

$$
(y_2 - y_1) x - (x_2 - x_1) y + (x_2 y_2 - x_2 y_1) = 0
$$

We may write this equation in determinant form as:

$$
\left| \begin{array}{ccc}
x & y & 1 \\
x_1 & y_1 & 1 \\
x_2 & y_2 & 1
\end{array} \right|
$$

**Note:** (i) If \( x_1 - x_2 \) then the slope becomes undefined. So, the line is vertical.

(ii) \( y - y_2 = \frac{y_2 - y_1}{x_2 - x_1} (x - x_1) \) can be derived similarly.

Example 3: Find an equation of line through the points $(-2,1)$ and $(6,-4)$.

Solution: Using two-points form of the equation of straight line, the required equation is

$$
\begin{aligned}
& y-1=\frac{-4-1}{6-(-2)}[x-(-2)] \\
\text { or } \quad & y-1=\frac{-5}{9}(x+2) \text { or } 5 x+8 y+2=0
\end{aligned}
$$

## 5. Intercept Form of Equation of a Straight Line:

Theorem: Equation of a line whose non-zero $x$ and $y$-intercepts are $a$ and $b$ respectively is

$$
\frac{x}{a} \cdot \frac{y}{b}=1
$$

Proof: Let $P(x, y)$ be an arbitrary point of the line whose non-zero $x$ and $y$-intercepts are $a$ and $b$ respectively. Obviously, the points $A(a, 0)$ and $B(0, b)$ lie on the required line. So, by the two-point form of the equation of line, we have

$$
\begin{aligned}
& y-0=\frac{b-0}{0-a}(x-a) \quad(P, A \text { and } B \text { are collinear }) \\
& \text { or } \quad-a y=b(x-a) \\
& \text { or } \quad b x+a y=a b \\
& \text { or } \quad \frac{x}{a}+\frac{y}{b}=1 \quad \text { (dividing by } a b \text { ) } \\
& \text { Hence the result. }
\end{aligned}
$$

Example 4: Write down an equation of the line which cuts the $x$-axis at $(2,0)$ and $y$-axis at $(0,-4)$.

Solution: As 2 and -4 are respectively $x$ and $y$-intercepts of the required line, so by two-intercepts form of equation of a straight line, we have

$$
\frac{x}{2}+\frac{y}{-4}=1-\quad \text { or }=2 x \quad y \quad 4 \quad 0
$$

which is the required equation.

Example 5: Find an equation of the line through the point $P(2,3)$ which forms an isosceles triangle with the coordinate axes in the first quadrant.

Solution: Let $O A B$ be an isosceles triangle so that the line $A B$ passes through $A=(a, 0)$ and $B(0, a)$, where $a$ is some positive real number.
Slope of $A B=\frac{a-0}{0-a}=-1$. But $A B$ passes through $P(2,3)$.
$\because \quad$ Equation of the line through $P(2,3)$ with slope -1 is

$$
y-3=-1(x-2) \text { or } \quad x+y-5=0
$$

## 6. Normal Form of Equation of a Straight Line:

Theorem: An equation of a non-vertical straight line $I$, such that length of the perpendicular from the origin to $I$ is $p$ and $\alpha$ is the inclination of this perpendicular, is

$$
x \cos \alpha+y \sin \alpha=p
$$

Proof: Let the line $I$ meet the $x$-axis and $y$-axis at the points $A$ and $B$ respectively. Let $P(x, y)$ be an arbitrary point of $A B$ and let $O R$ be perpendicular to the line $I$. Then $|O R|=p$.

From the right triangles $O R A$ and $O R B$, we have,

$$
\cos \alpha=\frac{p}{O A} \quad \text { or } \quad O A=\frac{p}{\cos \alpha}
$$

and

$$
\cos \left(90^{\circ}-\alpha\right)=\frac{p}{O B} \quad \text { or } \quad O B=\frac{p}{\sin \alpha}
$$

$$
\left[:: \cos \left(90^{\circ}-\alpha\right)=\sin \alpha\right)\right]
$$

As $O A$ and $O B$ are the $x$ and $y$-intercepts of the line $A B$, so equation of $A B$ is

$$
\frac{x}{p / \cos \alpha}+\frac{y}{p / \sin \alpha}=1 \quad \text { (Two-intercept form) }
$$

That is $x \cos \alpha+y \sin \alpha=p$ is the required equation.

Example 6: The length of perpendicular from the origin to a line is 5 units and the inclination of this perpendicular is $120^{\circ}$. Find the slope and $y$-intercept of the line.

Solution. Here $p=5, \alpha=120^{\circ}$.
Equation of the line in normal form is

$$
\begin{aligned}
& x \cos 120^{\circ}+y \sin 120^{\circ}=5 \\
& \Rightarrow \quad-\frac{1}{2} x+\frac{\sqrt{3}}{2} y=5 \\
& \Rightarrow \quad x-\sqrt{3} y+10=0
\end{aligned}
$$

To find the slope of the line, we re-write (1) as: $y=\frac{x}{\sqrt{3}}+\frac{10}{\sqrt{3}}$
which is slope-intercept form of the equation.
Here $\quad m=\frac{1}{\sqrt{3}}$ and $c=\frac{10}{\sqrt{3}}$