### **4.5. ANGLE BETWEEN TWO LINES**

Let *l<sub>1</sub>* and *l<sub>2</sub>* be two intersecting lines, which meet at a point *P*. At the point *P* two supplementary angles are formed by the lines *l<sub>1</sub>* and *l<sub>2</sub>*.

Unless *l<sub>1</sub>* ⊥ *l<sub>2</sub>* one of the two angles is acute. The angle from *l<sub>1</sub>* to *l<sub>2</sub>* is the angle *θ* through which *l<sub>1</sub>* is rotated anti-clockwise about the point *P* so that it coincides with *l<sub>2</sub>*.

In the figure below *θ* is angle of intersection of the two lines and it is measured from *l<sub>1</sub>* to *l<sub>2</sub>* in counterclockwise direction, *ψ* is also angle of intersection but it is measured from *l<sub>1</sub>* to *l<sub>1</sub>*.

With this convention for angle of intersection, it is clear that the inclination of a line is the angle measured in the counterclockwise direction from the positive *x*-axis to the line, and it tallies with the earlier definition of the inclination of a line.

**Theorem:** Let *l<sub>1</sub>* and *l<sub>2</sub>* be two non-vertical lines such that they are not perpendicular to each other. If *m<sub>1</sub>* and *m<sub>2</sub>* are the slopes of *l<sub>1</sub>* and *l<sub>2</sub>* respectively: the angle *θ* from *l<sub>1</sub>* to *l<sub>2</sub>* is given by:

$$
\tan \theta = \frac{m_1 - m_1}{1 + m_1 m_2}
$$

**Proof:** From the figure, we have

$$
\alpha_2 = \alpha_1 + \theta
$$

or

$$
\theta = \alpha_2 - \alpha_1
$$

$$
\tan \theta = \tan(\alpha_2 - \alpha_1) = \frac{\tan \alpha_2 - \tan \alpha_1}{1 + \tan \alpha_1 \tan \alpha_2} = \frac{m_2 - m_1}{1 + m_1 m_2}
$$

$$
\therefore \quad \tan \theta = \tan(\alpha_2 - \alpha_1) = \frac{\tan \alpha_2 - \tan \alpha_1}{1 + \tan \alpha_1 \tan \alpha_2} = \frac{m_2 - m_1}{1 + m_1 m_2}
$$

**Corollary 1.** *l<sub>1</sub>* || *l<sub>2</sub>* if and only if *m<sub>1</sub>* = *m<sub>2</sub>*

$$
\Rightarrow \quad \tan \theta = 0 \quad \frac{m_1 - m_1}{1 + m_1 m_2}
$$

$$
\Rightarrow \quad m_2 = m_1
$$

**Corollary 2.** *l<sub>1</sub>* ⊥ *l<sub>2</sub>* iff 1 + *m<sub>1</sub>m<sub>2</sub>* = 0

$$
\Rightarrow \quad \tan \theta = \frac{m_2 - m_1}{1 + m_1 m_2} = \tan \frac{\theta}{2} = + \quad = 1 \quad m_1 m_2 \quad 0
$$

These two results have already been stated in 4.3.1.

**Example 1:** Find the angle from the line with slope $$\frac{-7}{3}$$ to the line with slope $$\frac{5}{2}$$.

**Solution:** Here *m<sub>2</sub>* = $$\frac{5}{2}$$, *m<sub>1</sub>* = $$\frac{-7}{3}$$. If *θ* is measure of the required angle, then

$$
\tan \theta=\frac{\frac{5}{2}-\left(\frac{-7}{3}\right)}{1+\frac{5}{2}\left(\frac{-7}{3}\right)}=\frac{29}{-29}=-1
$$

Thus $\theta=135^{\circ}$
Example 2: Find the angles of the triangle whose vertices are

$$
A(-5,4), B(-2,-1), C(7,-5)
$$

Solution: Let the slopes of the sides $A B, B C$ and $C A$ be denoted by $m_{x}, m_{y}, m_{z}$ respectively. Then

$$
m_{x}=\frac{4+1}{-5+2}-\frac{-5}{3}, m_{y}=\frac{-5+1}{7+2}=\frac{-4}{9}, m_{z}=\frac{-5-4}{7+5}=\frac{-3}{4}
$$

Now angle $A$ is measured from $A B$ to $A C$.

$$
\tan A=\frac{m_{x}-m_{y}}{1+m_{x} m_{y}}=\frac{\frac{-3}{4}+\frac{5}{3}}{1+\left(\frac{-3}{4}\right)\left(\frac{-5}{3}\right)} \quad \frac{11}{27} \quad \text { or } \quad m \angle \underline{A} \quad 22.2^{\circ}
$$

The angle $B$ is measured from $B C$ to $B A$

$$
\therefore \quad \tan B=\frac{m_{x}-m_{y}}{1+m_{x} m_{y}}=\frac{\frac{-5}{3}+\frac{4}{9}}{1+\left(\frac{-5}{3}\right)\left(\frac{-4}{9}\right)}=\frac{-33}{47} \quad \text { or } \quad m \angle \underline{B}=144.9^{\circ}
$$

The angle $C$ is measured from $C A$ to $C B$.

$$
\therefore \quad \tan A=\frac{m_{x}-m_{y}}{1+m_{x} m_{y}}=\frac{\frac{-4}{9}+\frac{3}{4}}{1+\left(\frac{-4}{9}\right)\left(\frac{-3}{4}\right)}=\frac{11}{48} \quad \text { or } \quad m \angle \underline{C}=12.9^{\circ}
$$

# 4.5.1 Equation of a Straight Line in Matrix form

It is easy to solve two or three simultaneous linear equations by elementary methods. If the number of equations and variables become large, the solution of the equations by ordinary method becomes very difficult. In such a case, given equations are written in matrix form and solved.

## One Linear Equation:

A linear equation

$$
l: a x+b y+c=0
$$

in two variables $x$ and $y$ has its matrix form as:

$$
\begin{aligned}
& {[a x+b y]=[-c]} \\
& \text { or } \quad\left[\begin{array}{ll}
a & b
\end{array}\right]\left[\begin{array}{l}
x \\
y
\end{array}\right]=[-c] \\
& \text { or } \quad A X \times C
\end{aligned}
$$

where $\quad A=[a \quad b], \quad X=\left[\begin{array}{l}x \\ y\end{array}\right]$ and $C=[-c]$

## A System of Two Linear Equations:

A system of two linear equations

$$
\begin{aligned}
& l_{1}: a_{1} x+b_{1} y+c=0 \\
& l: a_{2} x+b_{2} y+c=0
\end{aligned}
$$

in two variables $x$ and $y$ can be written in matrix form as:

$$
\begin{aligned}
& {\left[\begin{array}{l}
a_{1} x+b_{1} y \\
a_{2} x+b_{2} y
\end{array}\right] \times\left[\begin{array}{l}
-c_{1} \\
-c_{2}
\end{array}\right]} \\
& \text { or } \\
& \left[\begin{array}{ll}
a_{1} & b_{1} \\
a_{2} & b_{2}
\end{array}\right]\left[\begin{array}{l}
x \\
y
\end{array}\right] \times\left[\begin{array}{l}
-c_{1} \\
-c_{2}
\end{array}\right] \\
& \text { or } \\
& A X \times C
\end{aligned}
$$

version: 1.1

where $\quad A=\left[\begin{array}{ll}a_{1} & b_{1} \\ a_{2} & b_{2}\end{array}\right], \quad X\left[\begin{array}{l}x \\ y\end{array}\right]$ and $C=\left[\begin{array}{l}-c_{1} \\ -c_{2}\end{array}\right]$
Equations (2) have a solution iff $\operatorname{det} A \neq 0$.

## A System of Three Linear Equations:

A system of three linear equations

$$
\begin{aligned}
& l_{1}: a_{1} x+b_{1} y+c_{1}=0 \\
& l_{2}: a_{2} x+b_{2} y+c_{2}=0 \\
& l_{3}: a_{3} x+b_{3} y+c_{3}=0
\end{aligned}
$$

in two variables $y$ and $y$ takes the matrix form as

$$
\begin{aligned}
& {\left[\begin{array}{lll}
a_{1} x+b_{1} y+c_{1} \\
a_{2} x+b_{2} y+c_{2}
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]} \\
& \text { or } \quad\left[\begin{array}{llll}
a_{1} & b_{1} & c_{1}
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
a_{2}
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]
\end{aligned}
$$

or

$$
\left[\begin{array}{lll}
a_{1} & b_{1} & c_{1}
\end{array}\right]
$$

If the matrix

$$
\left[\begin{array}{lll}
a_{1} & b_{1} & c_{1}
\end{array}\right] \text { is singular, then the lines (5) are concurrent }
$$

is singular, then the lines (5) are concurrent
a $_{1} \quad b_{1} \quad c_{1}$ and so the system (5) has a unique solution.
Example 1: Express the system

$$
\begin{aligned}
& 3 x+4 y-7=0 \\
& 2 x-5 y+8=0 \\
& x+y-3=0
\end{aligned}
$$

in matrix form and check whether the three lines are concurrent
Solution. The matrix form of the system is

$$
\left[\begin{array}{rrrr}
3 & 4 & -7 \\
2 & -5 & 8 \\
1 & 1 & -3
\end{array}\right]\left[\begin{array}{l}
x \\
y \\

\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]
$$

Coefficient matrix of the system is

$$
A=\left[\begin{array}{rrrr}
3 & 4 & -7 \\
2 & 5 & 8 \\
1 & 1 & -3
\end{array}\right] \text { and } \operatorname{det} A\left[\begin{array}{lll}
0 & 1 & 2 \\
0 & & 7 & 14 \\
1 & & 1 & -3
\end{array}\right] \begin{aligned}
& \text { by } R_{1}-3 R_{2} \\
& \text { and } R_{2}-2 R_{3}
\end{aligned}
$$

and $\operatorname{det} A=1(14+14)=28 \neq 0$
As $A$ is non-singular, so the lines are not concurrent.
Example 2: Find a system of linear equations corresponding to the matrix form

$$
\left[\begin{array}{llll}
1 & 2 & 5 \\
3 & 5 & 1 \\
4 & 7 & 6
\end{array}\right]\left[\begin{array}{l}
x \\
y \\

\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]
$$

Are the lines represented by the system concurrent?
Solution: Multiplying the matrices on the L.H.S. of (1), we have

$$
\left[\begin{array}{l}
x+2 y+5 \\
3 x+5 y+1 \\
4 x+7 y+6
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]
$$

By using the definition of equality of two matrices, we have from (2),

$$
\begin{aligned}
& x+2 y+5=0 \\
& 3 x+5 y+1=0 \\
& 4 x+7 y+6=0
\end{aligned}
$$

as the required system of equations. The coefficient matrix $A$ of the system is such that

$$
\operatorname{det} A=\left[\begin{array}{llll}
1 & 2 & 5 \\
3 & 5 & 1 \\
4 & 7 & 6
\end{array}\right]=\left[\begin{array}{lll}
1 & 2 & 5 \\
0 & -1 & -14 \\
0 & -1 & -14
\end{array}\right]=0
$$

Thus the lines of the system are concurrent.

## EXERCISE 4.4

1. Find the point of intersection of the lines
(i) $x-2 y+1=0-\quad$ and $2 x \quad y \quad 2 \quad 0$
(ii) $3 x+y+12=0+\quad$ and $=\quad x \quad 2 y \quad 1 \quad 0$
(iii) $x+4 y-12=0-\quad$ and $=\quad x \quad 3 y \quad 3 \quad 0$
2. Find an equation of the line through
(i) the point $(2,-9)$ and the intersection of the lines $2 x+5 y-8=0-\quad$ and $=3 x \quad 4 y \quad 6 \quad 0$
(ii) the intersection of the lines $x-y-4=0+\quad+$ and $7 x \quad y \quad 20 \quad 0 \quad$ and
(a) parallel
(b) perpendicular to the line $6 x+y-14=0$
(iii) through the intersection of the lines $x+2 y+3=0,3 x+4 y+7=0$ and making equal intercepts on the axes.
3. Find an equation of the line through the intersection of $16 x-10 y-33=0 ; 12 x-14 y-29=0 \quad$ and the intersection of $x-y+4=0 \quad ; \quad x-7 y+2=0$
4. Find the condition that the lines $y=m_{1} x+c_{1} ; y=m_{2} x+c_{2}$ and $y=m_{3} x+c_{3}$ are concurrent.
5. Determine the value of $p$ such that the lines $2 x-3 y-1=0$, $3 x-y-5=0$ and $3 x+4 y+8=0$ meet at a point.
6. Show that the lines $4 x-3 y-8=0,3 x-4 y-6=0$ and $x-y-2=0$ are concurrent and the third-line bisects the angle formed by the first two lines.
7. The vertices of a triangle are $A(-2,3), B(-4,1)$ and $C(3,5)$. Find coordinates of the
(i) centroid
(ii) orthocentre
(iii) circumcentre of the triangle

Are these three points collinear?
8. Check whether the lines
$4 x-3 y-8=0 ; \quad 3 x-4 y-6=0 ; \quad x-y-2=0$
are concurrent. If so, find the point where they meet
9. Find the coordinates of the vertices of the triangle formed by the lines $x-2 y-6=0 ; \quad 3 x-y+3=0 ; \quad 2 x+y-4=0$
Also find measures of the angles of the triangle.
10. Find the angle measured from the line $l_{1}$ to the line $l_{2}$ where
(a) $l_{1}:$ Joining $(2,7)$ and $(7,10)$
$l_{2}:$ Joining $(1,1)$ and $(-5,3)$
(b) $l_{1}:$ Joining $(3,-1)$ and $(5,7)$
$l_{2}:$ Joining $(2,4)$ and $(-8,2)$
Also find the acute angle in each case.
(c) $l_{1}:$ Joining $(1,-7)$ and $(6,-4)$
$l_{2}:$ Joining $(-1,2)$ and $(-6,-1)$
(d) $l_{1}:$ Joining $(-9,-1)$ and $(3,-5)$
$l_{2}:$ Joining $(2,7)$ and $(-6,-7)$
11. Find the interior angles of the triangle whose vertices are
(a) $A(-2,11), B(-6,-3),(4,-9)$
(b) $A(6,1), \quad B(2,7), C(-6,-7)$
(c) $A(2,-5), \quad B(-4,-3),(-1,5)$
(d) $A(2,8), \quad B(-5,4), C(4,-9)$
12. Find the interior angles of the quadrilateral whose vertices are $A(5,2), B(-2,3)$, $C(-3,-4)$ and $D(4,-5)$
13. Show that the points
$A(0,0), B(2,1), C(3,3), D(1,2)$ are the vertices of a rhombus.
Find its interior angles.
14. Find the area of the region bounded by the triangle whose sides are $7 x-y-10=0 ; \quad 10 x+y-14=0 ; \quad 3 x+2 y+3=0$
15. The vertices of a triangle are $A(-2,3), B(-4,1)$ and $C(3,5)$. Find the centre of the circumcircle of the triangle.

16. Express the given system of equations in matrix form. Find in each case whether the lines are concurrent.
(a) $x+3 y-2=0 ; \quad 2 x-y+4=0 ; \quad x-11 y+14=0$
(b) $2 x+3 y+4=0 ; \quad x-2 y-3=0 ; \quad 3 x+y-8=0$
(c) $3 x-4 y-2=0 ; \quad x+2 y-4=0 ; \quad 3 x-2 y+5=0$.
17. Find a system of linear equations corresponding to the given matrix form. Check whether the lines represented by the system are concurrent.
(a) $\left[\begin{array}{cccc|c}1 & 0 & -1 & x \\ 2 & 0 & 1 & y & 0 \\ 0 & -1 & 6 & 1 & 0\end{array}\right]$
(b) $\left[\begin{array}{cccc|c}1 & 1 & 2 & x \\ 2 & 4 & -3 & y & 0 \\ 3 & 6 & -5 & 1\end{array}\right]$
$=\left[\begin{array}{c}0 \\ 0 \\ 0\end{array}\right]$