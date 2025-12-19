### 6.8 TRANSLATION AND ROTATION OF AXES

## Translation of Axes

In order to facilitate the investigation of properties of a curve with a given equation, it is sometimes necessary to shift the origin $O(0,0)$ to some other point $O^{\prime}(h, k)$. The axes $O^{\prime} X, O^{\prime} Y$ drawn through $O^{\prime}$ remain parallel to the original axes $O x$ and $O y$. The process is called translation of axes.

We have already obtained in Chapter 4 formulas showing relationships between the two sets of coordinates of a point referred to the two sets of coordinate axes.

Recall that if a point $P$ has coordinates $(x$, $y)$ referred to the $x y$-system and has coordinates $(X, Y)$ referred to the translated axes $O^{\prime} X, O^{\prime} Y$ through $O^{\prime}(h, k)$, then
$$
\left.\begin{array}{l}
x=X+h \\
y=T+k
\end{array}\right\}
$$

These are called equations of transformation.
From (1), we have

$$
\left.\begin{array}{l}
X=x-h \\
Y=y-k
\end{array}\right\}
$$

(1) and (2) will be used to transform an equation in one system into the other system. The axes $O x$ and $O y$ are referred to as the original (or old) axes and $O^{\prime} X, O^{\prime} Y$ are called the translated axes (or new axes).

Example 1: Transform the equation $x^{2}+6 x-8 y+17=0$
referred to $O^{\prime}(-3,1)$ as origin, axes remaining parallel to the old axes.

Solution. Equations of transformation are

$$
\begin{aligned}
& x=X-3 \\
& y=Y+1
\end{aligned}
$$

Substituting these values of $x, y$ into (1), we have

$$
(X-3)^{2}+6(X-3)-8(Y+1)+17=0
$$

or $\quad X^{2}-6 X+9+6 X-18-8 Y-8+17=0$
or $\quad X^{2}-8 Y=0$ is the required transformed equation.

Example 2: By transforming the equation

$$
x^{2}+4 y^{2}-4 x+8 y+4=0
$$

referred to a new origin and axes remaining parallel to the original axes, the first degree terms are removed. Find the coordinates of the new origin and the transformed equation.

Solution. Let the coordinates of the new origin be $(h, k)$. Equations of transformation are

$$
\begin{aligned}
& x=X+h \quad, \quad y=Y+k \\
& \text { Substituting these values of } x, y \text { into (1), we get } \\
& (X+h)^{2}+4(Y+k)^{2}-4(X+h)+8(Y+k)+4=0 \\
& \text { or } \quad X^{2}+4 Y^{2}+X(2 h-4)+Y(8 k+8)+h^{2}+4 k^{2}-4 h+8 k+4=0
\end{aligned}
$$

$(h, k)$ is to be so chosen that first degree terms are removed from the transformed equation.

Therefore, $2 h-4=0$ and $8 k+8=0$ giving $h=2$ and $k=-1$. New origin is $O^{\prime}(2,-1)$. Putting $h=2, k=-1$ into (2), the transformed equation is $X^{2}+4 Y^{2}-4=0$.

## Rotation of Axes

To find equations for a rotation of axes about the origin through an angle $\theta(0<\theta<90^{\circ})$. (origin remaining unaltered).

Let the axes be rotated about the origin through an angle $\theta$. The new axes $O X, O Y$ are as shown in the figure.

Let $P$ be any point in the plane with coordinates $P(x, y)$ referred to the $x y$-system and $P(X, Y)$ referred to the $X Y$-system. In either system the distance $r$ between $P$ and $O$ is the same. Draw $P M \perp O x$ and $P Q \perp O X$. Let $\alpha$ be the inclination of $O P$ with $O X$. From the figure, we have
$$
\begin{aligned}
& X=O Q=r \cos \alpha, Y=Q P=r \sin \alpha \\
& \text { and } \quad x=r \cos (\theta+\alpha), y=r \sin (\theta+\alpha) \\
& \text { or } \quad\left.\begin{array}{l}
x=r \cos \theta \cos \alpha \quad r \sin \theta \sin \alpha \\
y=r \sin \theta \cos \alpha+r \cos \theta \sin \alpha
\end{array}\right\}
\end{aligned}
$$

Substituting the values of $r \cos \alpha, r \sin \alpha$ from (1) into (2), we get

$$
\left.\begin{array}{l}
x=X \cos \theta-Y \sin \theta \\
y=X \sin \theta+y \cos \theta
\end{array}\right]
$$

as the required equations of transformation for a rotation of axes through an angle $\theta$.
Example 3: Find an equation of $5 x^{2}-6 x y+5 y^{2}-8=0$ with respect to new axes obtained by rotation of axes about the origin through an angle of $135^{\circ}$.

Solution. Here $\theta=135$. Equations of transformation are

$$
\begin{aligned}
& x=X \cos 135^{\circ}-Y \sin 135^{\circ}=\frac{-X}{\sqrt{2}}-\frac{Y}{\sqrt{2}}=\frac{-1}{\sqrt{2}}(X+Y) \\
& x=X \sin 135^{\circ}+Y \cos 135^{\circ}=\frac{X}{\sqrt{2}}-\frac{Y}{\sqrt{2}}=\frac{1}{\sqrt{2}}(X-Y)
\end{aligned}
$$

Substituting these expressions for $x, y$ into the given equation, we have

$$
\begin{aligned}
& 5\left(-\frac{X+Y}{\sqrt{2}}\right)^{2}-6\left(-\frac{X+Y}{\sqrt{2}}-\frac{X-Y}{\sqrt{2}}\right)+5\left(\frac{X-Y}{\sqrt{2}}\right)^{2}-8=0 \\
\text { or } \quad & \frac{5}{2}\left(X^{2}+2 X Y+Y^{2}\right)+3\left(X^{2}-Y^{2}\right)+\frac{5}{2}\left(X^{2}-2 X Y+Y^{2}\right)-8=0 \\
\text { or } & 8 X^{2}+2 Y^{2}-8=0 \quad \text { or } \quad 4 X^{2}+Y^{2}=4
\end{aligned}
$$

is the required transformed equation.

Example 4: Find the angle through which the axes be rotated about the origin so that the product term $X Y$ is removed from the transformed equation of $5 x^{2}+2 \sqrt{3} x y+7 x^{2}-16=0$. Also find the transformed equation.

Solution. Let the axes be rotated through an angle $\theta$. Equations of transformation are

$$
x=X \cos \theta-Y \sin \theta \quad ; \quad y=X \sin \theta+Y \cos \theta
$$

Substituting into the given equation, we get

$$
\begin{aligned}
& 5(X \cos \theta-Y \sin \theta)^{2}+2 \sqrt{3}(X \cos \theta-Y \sin \theta)(X \sin \theta+Y \cos \theta) \\
& +7(X \sin \theta+y \cos \theta)^{2}-16=0
\end{aligned}
$$

Since this equation is to be free from the product term $X Y$, the coefficient of $X Y$ is zero, i.e. $-10 \sin \theta \cos \theta+2 \sqrt{3}\left(\cos ^{2} \theta-\sin ^{2} \theta\right)+14 \sin \theta \cos \theta=0$

$$
\text { or } \quad 2 \sin 2 \theta+2 \sqrt{3} \cos 2 \theta=0
$$

$$
\text { or } \quad \tan 2 \theta=\frac{-2 \sqrt{3}}{2}=\tan 120^{\circ} \quad \text { or } \quad \theta=60^{\circ}
$$

Thus axes be rotated through an angle of $60^{\circ}$ so that $X Y$ term is removed from the transformed equation.

Setting $\theta=60^{\circ}$ into (1), the transformed equation is (after simplification)

$$
8 X^{2}+4 Y^{2}-16=0 \quad \text { or } \quad 2 X^{2}+Y^{2}-4=0
$$

## EXERCISE 6.8

1. Find an equation of each of the following with respect to new parallel axes obtained by shifting the origin to the indicated point:
(i) $x^{2}+16 y-16 \quad=0, \quad O^{\prime}(0,1)$
(ii) $4 x^{2}+y^{2}+16 x-10 y+37 \quad=0, \quad O^{\prime}(2,5)$
(iii) $9 x^{2}+4 x^{2}+18 x-16 y-11 \quad=0, \quad O^{\prime}(-1,2)$
(iv) $x^{2}-y^{2}+4 x+8 y-11 \quad=0, \quad O^{\prime}(-2,4)$
(v) $9 x^{2}-4 y^{2}+36 x+8 y-4 \quad=0, \quad O^{\prime}(2,1)$
2. Find coordinates of the new origin (axes remaining parallel) so that first degree terms are removed from the transformed equation of each of the following. Also find the transformed equation:
(i) $3 x^{2}-2 y^{2}+24 x+12 y+24=0$
(ii) $25 x^{2}+9 y^{2}+50 x-36 y-164=0$
(iii) $x^{2}-y^{2}-6 x+2 y+7=0$
3. In each of the following, find an equation referred to the new axes obtained by rotation of axes about the origin through the given angle:
(i) $x y=1, \quad \theta=45^{\circ}$
(ii) $7 x^{2}-8 x y+y^{2}-9=0, \quad \theta=\arctan 2$
(iii) $9 x^{2}+12 x y+4 y^{2}-x-y=0, \quad \theta=\arctan \frac{2}{3}$
(iv) $x^{2}-2 x y+y^{2}-2 \sqrt{2} x-2 \sqrt{2} y+2=0, \quad \theta=45^{\circ}$

4. Find measure of the angle through which the axes be rotated so that the product term $X Y$ is removed from the transformed equation. Also find the transformed equation:
(i) $2 x^{2}+6 x y+10 y^{2}-11=0$
(ii) $x y+4 x-3 y-10=0$
(iii) $5 x^{2}-6 x y+5 y^{2}-8=0$