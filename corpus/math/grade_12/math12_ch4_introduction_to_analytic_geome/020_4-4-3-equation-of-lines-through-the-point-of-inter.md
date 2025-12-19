### 4.4.3 Equation of Lines through the point of intersection of two lines

We can find a family of lines through the point of intersection of two non parallel lines $l_{1}$ and $l_{2}$.

Let $l_{1}: a_{1} x+b_{1} y+c_{1}=0$
and $l_{2}: a_{2} x+b_{2} y+c_{2}=0$
For a non-zero real $h$, consider the equation

$$
a_{1} x+b_{1} y+c_{1}+h\left(a_{1} x+b_{1} y+c_{2}\right)=0
$$

This, being a linear equation, represents a straight line. For different values of $h$, (3) represents different lines. Thus (3) is a family of lines.

If $\left(x_{1}, y_{1}\right)$ is any point lying on both (1) and (2), then it is their point of intersection. Since $\left(x_{1}, y_{1}\right)$ lies on both (1) and (2), we have

$$
a_{1} x+b_{1} y+c_{1}=0+\text { and }+a_{2} x \quad b_{2} y \quad c_{2} \quad 0
$$

From the above two equations, we note that $\left(x_{1}, y_{1}\right)$ also lies on (3).
Thus (3) is the required family of lines through the point of intersection of (1) and (2). Since $h$ can assume an infinite number of values, (3) represents an infinite number of lines.

A particular line of the family (3) can be determined if one more condition is given.
Example 2: Find the family of lines through the point of intersection of the lines

$$
\begin{aligned}
& 3 x-4 y-10=0 \\
& x+2 y-10=0
\end{aligned}
$$

Find the member of the family which is
(i) parallel to a line with slope $\frac{-2}{3}$
(ii) perpendicular to the line $l: 3 x-4 y+1=0$.

Solution: (i) A family of lines through the point of intersection of equations (1) and (2) is

$$
\begin{aligned}
& 3 x-4 y-10+k(x+2 y-10)=0 \\
& \text { or } \quad(3+k) x+(-4+2 k) y+(-10-10 k)=0
\end{aligned}
$$

Slope $m$ of (3) is given by: $m=-\frac{3+k}{-4+2 k}$
This is slope of any member of the family (3).
If (3) is parallel to the line with slope $-\frac{2}{3}$ then
$-\frac{3+k}{-4+2 k}=\frac{-2}{3}$ or $9+3 k=-8+4 k$ i.e., $k=17$
Substituting $k=17$ into (3), equation of the member of the family is
$20 x+30 y-180=0$ i.e., $2 x+3 y-18=0$
(ii) Slope of $3 x-4 y+1=0$
is $\frac{3}{4}$. Since (3) is to be perpendicular to (4), we have $-\frac{3+k}{-4+2 k} \times \frac{3}{4}=-1$
or $9+3 k=-16+8 k \quad$ or $\quad k=5$
Inserting this value of $k$ into (3), we get $4 x+3 y-30=0$ which is required equation of the line.

Theorem: Altitudes of a triangle are concurrent.
Proof. Let the coordinates of the vertices of $\triangle A B C$ be as shown in the figure.

Then slope of $B C=\frac{y_{2}-y_{1}}{x_{2}-x_{1}}$
Therefore slope of the altitude $A D=-\frac{x_{2}-x_{1}}{y_{2}-y_{1}}$

## Equation of the altitude $A D$ is

$$
y-y_{1}=-\frac{x_{2}-x_{1}}{y_{2}-y_{1}}\left(x-x_{1}\right) \quad \text { (Point-slope form) }
$$

or $\quad x\left(x_{1}-x_{2}\right)+y\left(y_{2}-y_{1}\right)-x_{1}\left(x_{2}-x_{1}\right)-y_{1}\left(y_{2}-y_{2}\right)=0$
Equations of the altitudes $B E$ and $C F$ are respectively (by symmetry)

$$
x\left(x_{1}-x_{1}\right)+y\left(y_{2}-y_{1}\right)-x_{2}\left(x_{2}-x_{1}\right)-y_{2}\left(y_{2}-y_{1}\right)=0
$$

and $x\left(x_{1}-x_{2}\right)+y\left(y_{1}-y_{2}\right)-x_{1}\left(x_{1}-x_{2}\right)-y_{1}\left(y_{2}-y_{1}\right)=0$
The three lines (1), (2) and (3) are concurrent if and only if

$$
\mathrm{D}=\left|\begin{array}{ccc}
x_{2}-x_{1} & y_{2}-y_{1} & -x_{1}\left(x_{2}-x_{1}\right)-y_{1}\left(y_{2}-y_{1}\right) \\
x_{2}-x_{1} & y_{2}-y_{1} & -x_{2}\left(x_{2}-x_{1}\right)-y_{2}\left(y_{2}-y_{1}\right) \\
x_{1}-x_{2} & y_{1}-y_{2} & -x_{1}\left(x_{1}-x_{2}\right)-y_{1}\left(y_{1}-y_{2}\right)
\end{array}\right| \text { is zero }
$$

Adding 2nd and 3rd rows to the 1st row of the determihant, we have

$$
\left|\begin{array}{ccc}
0 & 0 & 0 \\
x_{1}-x_{1} & y_{1}-y_{1} & -x_{2}\left(x_{1}-x_{1}\right)-y_{2}\left(y_{1}-y_{1}\right) \\
x_{1}-x_{2} & y_{1}-y_{2} & -x_{3}\left(x_{1}-x_{2}\right)-y_{3}\left(y_{1}-y_{2}\right)
\end{array}\right| = 0
$$

Thus the altitudes of a triangle are concurrent.

**Theorem:** Right bisectors of a triangle are concurrent.

**Proof.** Let \( A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right) \) and \( C\left(x_{3}, y_{3}\right) \) be the vertices of \( \Delta ABC \).

The midpoint \( D \) of \( BC \) has coordinates

$$
\left(\frac{x_2 + x_1}{2}, \frac{y_2 + y_3}{2}\right)
$$

Since the slope of \( BC \) is \( \frac{y_2 - y_3}{x_2 - x_3} \), the slope of the right bisector \( DO \) of \( BC \) is \( -\frac{x_2 - x_3}{y_2 - y_3} \).