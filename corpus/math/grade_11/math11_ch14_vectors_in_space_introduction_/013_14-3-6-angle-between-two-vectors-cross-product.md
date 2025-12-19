### 14.3.6 Angle Between Two Vectors (Cross Product)

The sine of the angle between two vectors $\underline{a}$ and $\underline{b}$ is determined from the definition of cross product.
If $\theta$ is the sine of the angle between $\underline{a}$ and $\underline{b}$, then $|\underline{a} \times \underline{b}|=|\underline{a}||\underline{b}| \sin \theta$

$$
\Rightarrow \quad \sin \theta=\frac{|\underline{a} \times \underline{b}|}{|\underline{a}||\underline{b}|}
$$

Example 16 If $\underline{a}=4 \underline{i}+3 \underline{j}+\underline{k}$ and $\underline{b}=2 \underline{i}-\underline{j}+2 \underline{k}$. Find a unit vector perpendicular to both $\underline{a}$ and $\underline{b}$. Also find the sine of the angle between the vectors $\underline{a}$ and $\underline{b}$.

Solution

$$
\begin{aligned}
& \underline{a} \times \underline{b}=\left|\begin{array}{ccc}
\underline{i} & \underline{j} & \underline{k} \\
4 & 3 & 1 \\
2 & -1 & 2
\end{array}\right|=7 \underline{i}-6 \underline{j}-10 \underline{k} \\
& \text { and } \quad|\underline{a} \times \underline{b}|=\sqrt{(7)^{2}+(-6)^{2}+(-10)^{2}}=\sqrt{185} \\
& \therefore \quad \text { A unit vector perpendicular to } \underline{a} \text { and } \underline{b}=\frac{\underline{a} \times \underline{b}}{|\underline{a} \times \underline{b}|}=\frac{7 \underline{i}-\underline{b} \underline{j}-10 \underline{k}}{\sqrt{185}} \\
& \text { Now } \quad|\underline{a}|=\sqrt{(4)^{2}+(3)^{2}+(1)^{2}}=\sqrt{26} \\
& \left\lvert\, \underline{b}\right|=\sqrt{(2)^{2}+(-1)^{2}+(2)^{2}}=3
\end{aligned}
$$

If $\theta$ is the angle between $\underline{a}$ and $\underline{b}$, then $|\underline{a} \times \underline{b}|=|\underline{a}||\underline{b}| \sin \theta$

$$
\Rightarrow \quad \sin \theta=\frac{|\underline{a} \times \underline{b}|}{|\underline{a}||\underline{b}|}=\frac{\sqrt{185}}{3 \sqrt{26}}
$$

Example17 Prove that $\sin (\alpha+\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta$
Proof: Let $\overrightarrow{O A}$ and $\overrightarrow{O B}$ be two unit vectors in the $x y$-plane making angles $\alpha$ and $-\beta$ with the positive $x$-axis respectively.

So that $m \angle A O B=\alpha+\beta$
Now $\quad \overrightarrow{O A}=\cos \alpha i+\sin \alpha j$
and

$$
\begin{aligned}
\overrightarrow{O B} & =\cos (-\beta) i+\sin (-\beta) j \\
& =\cos \beta i-\sin \beta j \\
\therefore \quad \overrightarrow{O B} \times \overrightarrow{O A} & =(\cos \beta i-\sin \beta j) \times(\cos \alpha i+\sin \alpha i) \\
\Rightarrow \quad & \left|\overrightarrow{O B}\right||\overrightarrow{O A}| \sin (\alpha+\beta) k=\left|\begin{array}{ccc}
i & j & k \\
\cos \beta & -\sin \beta & 0 \\
\cos \alpha & \sin \alpha & 0
\end{array}\right| \\
\Rightarrow \quad & \sin (\alpha+\beta) k=(\sin \alpha \cos \beta+\cos \alpha \sin \beta) k
\end{aligned}
$$

$\therefore \quad \sin (\alpha+\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta$
Example18 In any triangle $A B C$, prove that

$$
\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C} \text { (Law of Sines) }
$$

Proof: Suppose vectors $\underline{a}, \underline{b}$ and $\underline{c}$ are along the sides $B C, C A$ and $A B$ respectively of the triangle $A B C$.

$$
\begin{aligned}
& \therefore \quad \underline{a}+\underline{b}+\underline{c}=\underline{0} \\
& \Rightarrow \quad \underline{b}+\underline{c}=-\underline{a}
\end{aligned}
$$

Take cross product with $\underline{c}$

$$
\begin{aligned}
& \underline{b} \times \underline{c}+\underline{c} \times \underline{c}=-a \times \underline{c} \\
& \underline{b} \times \underline{c}=\underline{c} \times \underline{a} \quad(\because \underline{c} \times \underline{c}=\underline{0}) \\
& \Rightarrow \quad|\underline{b} \times \underline{c}|=|\underline{c} \times \underline{a}| \\
& \begin{array}{l}
|\underline{b}||\underline{c}| \sin (\pi-A)=|\underline{c}||\underline{a}| \sin (\pi-B) \\
\Rightarrow \quad b c \sin A=c a \sin B \Rightarrow b \sin A=a \sin B
\end{array} \\
& \therefore \quad \frac{b}{\sin B}=\frac{a}{\sin A}
\end{aligned}
$$

Similarly, by taking cross product of (i) with $\underline{b}$, we have

$$
\frac{a}{\sin A}=\frac{c}{\sin C}
$$

From (ii) and (iii), we get $\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}$
Example 19 If $\underline{u}=2 \underline{i}-\underline{j}+\underline{k}$ and $\underline{v}=4 \underline{i}+2 \underline{j}-\underline{k}$, find by determinant formula
(i) $\underline{u} \times \underline{u}$
(ii) $\underline{u} \times \underline{v}$
(iii) $\underline{v} \times \underline{u}$

Solution $\underline{u}=2 \underline{i}-\underline{j}+\underline{k}$ and $\underline{v}=4 \underline{i}+2 \underline{j}-\underline{k}$
By determinant formula
(i) $\quad \underline{u} \times \underline{u}=\left|\begin{array}{ccc}\underline{i} & \underline{j} & \underline{k} \\ 2 & -1 & 1 \\ 2 & -1 & 1\end{array}\right|=0 \quad$ ( $\therefore$ Two rows are same)
(ii) $\quad \underline{u} \times \underline{v}=\left|\begin{array}{ccc}\underline{i} & \underline{j} & \underline{k} \\ 2 & -1 & 1 \\ 4 & 2 & -1\end{array}\right|=(1-2) \underline{i}-(-2-4) \underline{j}+(4+4) \underline{k}=-\underline{i}+6 \underline{j}+8 \underline{k}$
(iii) $\underline{v} \times \underline{u}=\left|\begin{array}{ccc}\underline{i} & \underline{j} & \underline{k} \\ 4 & 2 & -1 \\ 2 & -1 & -1\end{array}\right|=(2-1) \underline{i}-(4+2) \underline{j}+(-4-4) \underline{k}=\underline{i}-6 \underline{j}-8 \underline{k}$

# 14.3.7 Real World Applications on Cross or Vector Product

(a) Area of Parallelogram

Suppose $\underline{u}$ and $\underline{v}$ are two non-zero vectors and $\theta$ is the angle between them, and suppose that $|\underline{u}|$ and $|\underline{v}|$ represent the length of the adjacent sides of a parallelogram, (see figure). We know that:
Area of parallelogram $=$ Base $\times$ Height

$$
=(\text { Base })(h)=|\underline{u}||\underline{v}| \sin \theta
$$

$\therefore$ Area of parallelogram $=|\underline{u} \times \underline{v}|$

(b) Area of Triangle

From figure it is clear that
Area of triangle $=\frac{1}{2}$ (Area of parallelogram)
Area of triangle $=\frac{1}{2}|u \times v|$
where $\underline{u}$ and $\underline{v}$ are vectors along two adjacent sides of the triangle.
Example 20 Find area of the parallelogram whose vertices are $P(0,0,0), Q(-1,2,4), R(2,-1,4)$ and $S(1,1,8)$.
Solution Area of parallelogram $=|P \vec{Q} \times \overrightarrow{P R}|$
Where $|P \vec{Q}|$ and $|P \vec{R}|$ are two adjacent sides of the parallelogram

$$
\begin{aligned}
& \overrightarrow{P Q}=\overrightarrow{O Q}-\overrightarrow{O P}=(-1-0) \underline{i}+(2-0) \underline{j}+(4-0) \underline{k}=-\underline{i}+2 \underline{j}+4 \underline{k} \\
& \overrightarrow{P R}=\overrightarrow{O R}-\overrightarrow{O P}=(2-0) \underline{i}+(-1-0) \underline{j}+(4-0) \underline{k}=2 \underline{i}-\underline{j}+4 \underline{k} \\
& \text { Now } \quad \overrightarrow{P Q} \times \overrightarrow{P R}=\left|\begin{array}{ccc}
i & j & k \\
-1 & 2 & 4 \\
2 & -1 & 4
\end{array}\right|=(8+4) i-(-4-8) j+(1-4) k \\
& =12 i+12 j-3 k
\end{aligned}
$$

$\therefore$ Area of parallelogram $=|P \vec{Q} \times \overrightarrow{P R}|=12 i+12 j-3 k$

$$
=\sqrt{144+144+9}=\sqrt{297} \text { square units }
$$

Example 21 Find the area of the triangle with vertices $A(1,-1,1), B(2,1,-1)$ and $C(-1,1,2)$. Also find a unit vector perpendicular to the plane of triangle $A B C$.
Solution $\overrightarrow{A B}=\overrightarrow{O B}-\overrightarrow{O A}=(2-1) \underline{i}+(1+1) \underline{j}+(-1-1) \underline{k}=\underline{i}+2 \underline{j}-2 \underline{k}$

$$
\begin{aligned}
\overrightarrow{A C} & =\overrightarrow{O C}-\overrightarrow{O A}=(-1-1) \underline{i}+(1+1) \underline{j}+(2-1) \underline{k}=-2 \underline{i}+2 \underline{j}+\underline{k} \\
\overrightarrow{A B} \times \overrightarrow{A C} & =\left|\begin{array}{ccc}
i & j & k \\
1 & 2 & -2 \\
-2 & 2 & 1
\end{array}\right|=(2+4) i-(1-4) j+(2+4) k=6 i+3 j+6 k
\end{aligned}
$$

The area of the parallelogram with adjacent sides $|\overrightarrow{A B}|$ and $|\overrightarrow{A C}|$ and is given by

$$
|\overrightarrow{A B} \times \overrightarrow{A C}|=|6 i+3 j+6 k|=\sqrt{36+9+36}=\sqrt{81}=9
$$

$\therefore \quad$ Area of triangle $=\frac{1}{2}|\overrightarrow{A B} \times \overrightarrow{A C}|=\frac{1}{2}|6 i+3 j+6 k|=\frac{9}{2}$ square units
A unit vector $\perp$ to the plane $A B C=\frac{\overrightarrow{A B} \times \overrightarrow{A C}}{|\overrightarrow{A B} \times \overrightarrow{A C}|}=\frac{1}{9}(6 i+3 j+6 k)=\frac{1}{3}(2 i+j+2 k)$

# Unit 44 Vectors in Space <281

## (c) Moment of Force

Let a force $\underline{F}(\overrightarrow{P Q})$ act at a point $P$, as shown in the figure. The moment of $\underline{F}$ about $O$
$=$ Product of force $\underline{F}$ and the perpendicular distance $\overrightarrow{O N}$ in the direction of $s$.

$$
\begin{aligned}
& =\overrightarrow{(P Q)}(\overrightarrow{O N})(s)=(P Q)(O P) \sin \theta(s) \\
& =\overrightarrow{O P} \times \overrightarrow{P Q}=\underline{r} \times \underline{F}
\end{aligned}
$$

Example 22 Find the moment about the point $M(-2,4,-6)$ of the force represented by $\overrightarrow{A B}$, where coordinates of points $A$ and $B$ are $(1,2,-3)$ and $(3,-4,2)$ respectively.
Solution $\overrightarrow{A B}=\overrightarrow{O B}-\overrightarrow{O A}=(3-1) i+(-4-2) j+(2+3) \underline{k}=2 i-6 j+5 \underline{k}$

$$
\overrightarrow{M A}=(1+2) i+(2-4) j+(-3+6) k=3 i-2 j+3 k
$$

Moment of $A B$ about $M(-2,4,-6)=\underline{r} \times \underline{F}=\overrightarrow{M A} \times \overrightarrow{A B}$

$$
\begin{aligned}
& =i \quad j \quad k \\
& =3 \quad-2 \quad 3 \\
& =2 \quad-6 \quad 5 \\
& =(-10+18) i-(15-6) j+(-18+4) k \\
& =8 i-9 j-14 k
\end{aligned}
$$

Magnitude of the moment $=\sqrt{(8)^{2}+(-9)^{2}+(-14)^{2}}=\sqrt{341}$

## EXERCISE 14.3

1. Compute the cross product $a \times b$ and $b \times a$. Check your answer by showing that each $a$ and $b$ are perpendicular to $a \times b$ and $b \times a$.
(i) $\underline{a}=2 i+\underline{j}-\underline{k}, \underline{b}=\underline{i}-\underline{j}+\underline{k}$
(ii) $a=i+3 j+2 k, \underline{b}=2 i-\underline{j}+\underline{k}$
(iii) $\underline{a}=2 i-2 \underline{j}+\underline{k}, \underline{b}=-\underline{i}+\underline{j}+3 \underline{k}$
(iv) $\underline{a}=-4 i+\underline{j}-2 \underline{k}, \underline{b}=2 i+\underline{j}+\underline{k}$
2. Find a unit vector perpendicular to the plane containing $a$ and $b$. Also find sine of the angle between them:
(i) $\underline{a}=i+6 \underline{j}-3 \underline{k}, \underline{b}=2 i+\underline{j}+3 \underline{k}$
(ii) $\underline{a}=-\underline{i}-\underline{j}-\underline{k}, \underline{b}=2 i-3 \underline{j}+4 \underline{k}$
(iii) $\underline{a}=\underline{i}+\underline{j}+\underline{k}, \underline{b}=\underline{i}-\underline{j}-\underline{k}$
(iv) $\underline{a}=5 i+\underline{j}-3 \underline{k}, \underline{b}=-2 i+4 \underline{j}+\underline{k}$

3. Find the area of the triangle, formed by the points $P, Q$ and $R$.
(i) $P(2,3,5) ; Q(1,2,0) ; R(4,1,2)$
(ii) $P(0,0,1) ; Q(2,-1,2) ; R(-1,3,2)$
4. Find the area of a parallelogram, whose vertices are:
(i) $A(1,1,1) ; B(4,2,3) ; C(5,6,7) ; D(2,5,5)$
(ii) $A(4,5,6) ; B(1,3,2) ; C(-2,0,1) ; D(1,2,5)$
5. If the cross product of the vectors $\underline{u}=7 \underline{i}-4 \underline{j}+5 \underline{k}$ and $\underline{v}=a \underline{i}-b \underline{j}+3 \underline{k}$ is zero, then find the values of $a$ and $b$.
6. Which vectors, if any, are perpendicular or parallel
(i) $\underline{u}=5 \underline{i}-\underline{j}+\underline{k} ; \underline{v}=\underline{j}-5 \underline{k} ; \underline{w}=-15 \underline{i}+3 \underline{j}-3 \underline{k}$
(ii) $\underline{u}=\underline{i}+2 \underline{j}-\underline{k} ; \underline{v}=-\underline{i}+\underline{j}+\underline{k} ; \underline{w}=-\frac{\pi}{2} \underline{i}-\pi \underline{j}+\frac{\pi}{2} \underline{k}$
7. Use the definition of cross product, for any vectors $\underline{u}, \underline{v}, \underline{w}$ and scalar $\underline{k}$, prove that
(i) $\underline{u} \times(-u)=0$
(ii) $\underline{u} \times \underline{v}=-v \times \underline{u}$
(iii) $\underline{u} \times(\underline{k} \underline{v})=(\underline{k} \underline{u}) \times \underline{v}=\underline{k}(\underline{u} \times \underline{v})$
(iv) $\underline{u} \times(\underline{v}+\underline{w})=(\underline{u} \times \underline{v})+(\underline{u} \times \underline{w})$
8. Prove that: $\underline{a} \times(\underline{b}+\underline{c})+\underline{b} \times(\underline{c}+\underline{a})+\underline{c} \times(\underline{a}+\underline{b})=0$.
9. If $\underline{a}+\underline{b}+\underline{c}=\underline{0}$, then prove that $\underline{a} \times \underline{b}=\underline{b} \times \underline{c}=\underline{c} \times \underline{a}$
10. Prove that: $\sin (\alpha-\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta$
11. Show that $|\underline{a} \times \underline{b}|^{2}=|\underline{a}|^{2}|\underline{b}|^{2}-(\underline{a} \cdot \underline{b})^{2}$
12. Use the definition of cross product, prove that for any vectors $\underline{u}$ and $\underline{v}$ $(\underline{u}+\underline{v}) \times(\underline{u}-\underline{v})=-2(\underline{u} \times \underline{v})$.
13. Find the moment about the point $M(1,-3,3)$ of the force represented by $\overrightarrow{A B}$, where the coordinates of points $A(4,3,-1)$ and $B(-1,3,7)$ are given.
14. A force $\vec{F}=6 \underline{i}+4 \underline{j}-4 \underline{k}$ is applied at the point $A(1,-1,2)$. Find the moment of the force about the point $B(3,-2,3)$.
15. Give a force $\underline{F}=2 \underline{i}+\underline{j}-3 \underline{k}$ acting at a point $A(1,-2,1)$. Find the moment of $\vec{F}$ about the point $B(2,0,-2)$.
16. A force $\underline{F}=-2 \underline{i}+\underline{j}-3 \underline{k}$ is applied at $P(-1,-3,2)$. Find its moment about the point $Q(4,2,2)$.

# 14.4 Scalar Triple Product

The scalar triple product is a key concept in vector calculus with wide-ranging applications covering various fields. In three-dimensional space, it provides a significant role in calculating the volume of geometric shapes such as parallelepipeds and tetrahedrons, defined by three vectors, which we will learn later in this chapter. Additionally, it plays as a vital tool for determining the coplanarity of vectors, providing a condition to verify whether three vectors lie within the same plane.
There are two types of triple product of vectors:
(a) Scalar Triple Product: $\underline{u} \cdot(\underline{v} \times \underline{w})$
(b) Vector Triple Product: $\underline{u} \times(\underline{v} \times \underline{w})$

In this section we shall study the scalar triple product only.
Let $\underline{u}, \underline{v}$ and $\underline{w}$ be three non-zero vectors
The scalar triple product of vector $\underline{u}, \underline{v}$ and $\underline{w}$ is defined by

$$
\underline{u} \cdot(\underline{v} \times \underline{w}) \quad \text { or } \quad \underline{v} \cdot(\underline{w} \times \underline{u}) \text { or } \quad \underline{w} \cdot(\underline{u} \times \underline{v})
$$

The scalar triple product $\underline{u} \cdot(\underline{v} \times \underline{w})$ is written as

$$
\underline{u} \cdot(\underline{v} \times \underline{w}) \in[\underline{u} \times \underline{w}]
$$