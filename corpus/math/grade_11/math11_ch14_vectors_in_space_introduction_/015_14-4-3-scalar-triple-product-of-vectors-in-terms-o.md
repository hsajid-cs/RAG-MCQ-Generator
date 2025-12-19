### 14.4.3 Scalar Triple Product of Vectors in Terms of Components

Let $\underline{u}=a_{1} \underline{i}+\underline{b}_{1} \underline{j}+\underline{c}_{1} \underline{k}, \underline{v}=a_{2} \underline{i}+\underline{b}_{2} \underline{j}+\underline{c}_{2} \underline{k}$ and $\underline{w}=a_{3} \underline{i}+\underline{b}_{3} \underline{j}+\underline{c}_{3} \underline{k}$

Now,

$$
\underline{v} \times \underline{w}=\left|\begin{array}{lll}
\underline{i} & \underline{j} & \underline{k} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{array}\right|
$$

$$
\begin{aligned}
& \Rightarrow \quad \underline{u} \times \underline{w}=\left(\underline{b}_{2} \underline{c}_{3}-\underline{b}_{3} \underline{c}_{2}\right) \underline{i}-\left(\underline{a}_{2} \underline{c}_{3}-\underline{a}_{3} \underline{c}_{2}\right) \underline{j}+\left(\underline{a}_{2} \underline{b}_{3}-\underline{a}_{3} \underline{b}_{2}\right) \underline{k} \\
& \therefore \quad \underline{u} \cdot(\underline{v} \times \underline{w})=a_{1}\left(\underline{b}_{2} \underline{c}_{2}-\underline{b}_{3} \underline{c}_{2}\right)-b_{1}\left(\underline{a}_{2} \underline{c}_{3}-\underline{a}_{3} \underline{c}_{2}\right)+c_{1}\left(\underline{a}_{2} \underline{b}_{3}-\underline{a}_{3} \underline{b}_{2}\right) \\
& \Rightarrow \quad \underline{u} \cdot(\underline{v} \times \underline{w})=\left|\begin{array}{lll}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{array}\right|
\end{aligned}
$$

Which is called the determinant formula for scalar triple product of $\underline{u}, \underline{v}$ and $\underline{w}$ in component form.
Example 23 Prove that dot and cross product are interchangeable in scalar triple product.
Solution Consider $\underline{u}=a_{1} \underline{i}+\underline{b}_{1} \underline{j}+\underline{c}_{1} \underline{k}, \underline{v}=a_{2} \underline{i}+\underline{b}_{2} \underline{j}+\underline{c}_{2} \underline{k}$ and $\underline{w}=a_{3} \underline{i}+\underline{b}_{3} \underline{j}+\underline{c}_{3} \underline{k}$ are the arbitrary vectors.
The determinant formula for scalar triple product of vectors $\underline{u}, \underline{v}$ and $\underline{w}$ is given by:
$\underline{u} \cdot(\underline{v} \times \underline{w})=\left|\begin{array}{lll}a_{1} & b_{1} & c_{1} \\ a_{2} & b_{2} & c_{2} \\ a_{3} & b_{3} & c_{3}\end{array}\right|$

$$
\begin{aligned}
& =-\left|\begin{array}{lll}
a_{2} & b_{2} & c_{2} \\
a_{1} & b_{1} & c_{1} \\
a_{3} & b_{3} & c_{3}
\end{array}\right| \quad \text { Interchanging } R_{1} \text { and } R_{2} \\
& =\left|\begin{array}{lll}
a_{3} & b_{3} & c_{3} \\
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2}
\end{array}\right| \quad \text { Interchanging } R_{1} \text { and } R_{2} \\
& =\underline{w} \cdot(\underline{u} \times \underline{v})=(\underline{u} \times \underline{v}) \cdot \underline{w} \quad(\because \underline{a} \cdot \underline{b}=\underline{b} \cdot \underline{a})
\end{aligned}
$$

Hence, $\underline{u} \cdot(\underline{v} \times \underline{w})=(\underline{u} \times \underline{v}) \cdot \underline{w}$
Thus, the position of dot and cross can be interchanged in scalar triple product.
Example 24 Assuming $i, j$ and $k$ are unit vectors in a cartesian coordinate system.
Prove that $i \cdot j \times k=j \cdot k \times i=k \cdot i \times j$
Sotation Given $i, j$ and $k$ are unit vector,
So, we can write $i=i+0 j+0 k, j=0 i+j+0 k, k=0 i+0 j+k$ then determinant form for scalar triple product of unit vectors $i, j$ and $k$ can be written as:

$$
\begin{aligned}
& i \cdot j \times k=\left|\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right|=1(1-0)-0(0-1)+0(0-0)=1 \\
& j \cdot k \times i=\left|\begin{array}{lll}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0
\end{array}\right|=0(0-0)-1(0-1)+0(0-0)=1 \text { and } k \cdot i \times j=\left|\begin{array}{lll}
0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0
\end{array}\right|=1 \\
& \text { Therefore } i \cdot j \times k=j \cdot k \times i=k \cdot i \times j
\end{aligned}
$$

Example 25 Find the volume of the parallelepiped determined by

$$
\underline{u}=\underline{i}+2 \underline{j}-\underline{k}, \underline{v}=\underline{i}-2 \underline{j}+3 \underline{k}, \underline{w}=\underline{i}-7 \underline{j}-4 \underline{k}
$$

Sotation Volume of the parallelepiped $=\underline{u} \cdot \underline{v} \times \underline{w}=\left|\begin{array}{rrr}1 & 2 & -1 \\ 1 & -2 & 3 \\ 1 & -7 & -4\end{array}\right|$

$$
\begin{aligned}
\Rightarrow \quad \text { Volume } & =1(8+21)-2(-4-3)-1(-7+2)=29+14+5 \\
& =48 \text { cubic units }
\end{aligned}
$$

Example 26 Find the volume of the tetrahedron whose vertices are $A(2,1,8)$, $B(3,2,9), C(2,1,4)$ and $D(3,3,0)$.
Solution $\overrightarrow{A B}=\overrightarrow{O B}-\overrightarrow{O A}=(3-2) \underline{i}+(2-1) \underline{j}+(9-8) \underline{k}=\underline{i}+\underline{j}+\underline{k}$

$$
\begin{aligned}
& \overrightarrow{A C}=\overrightarrow{O C}-\overrightarrow{O A}=(2-2) \underline{i}+(1-1) \underline{j}+(4-8) \underline{k}=0 \underline{i}-0 \underline{j}-4 \underline{k} \\
& \overrightarrow{A D}=\overrightarrow{O D}-\overrightarrow{O A}=(+3-2) \underline{i}+(3-1) \underline{j}+(0-8) \underline{k}=\underline{i}+2 \underline{j}-8 \underline{k}
\end{aligned}
$$

Volume of the tetrahedron $=\frac{1}{6}[\overrightarrow{A B} \overrightarrow{A C} \overrightarrow{A D}]$

$$
\begin{aligned}
& =\frac{1}{6}\left|\begin{array}{lll}
1 & 1 & 1 \\
0 & 0 & -4 \\
1 & 2 & -8
\end{array}\right|=\frac{1}{6}[1(0+8)-1(0+4)+1(0-0)] \\
& =\frac{1}{6}[8-4]=\frac{4}{6}=\frac{2}{3} \text { cubic units }
\end{aligned}
$$

# 14.4.4 Coplanar Vectors and Condition for Coplanarity of Three Vectors

Vectors are coplanar if they lie in the same plane or can be combined in the same plane.
Consider the three coplanar vectors $u, v$ and $w$ in a plane as shown in a figure.
The cross product $v \times w$ gives a vector that is perpendicular to both the vectors yand $w$, As $u, v$ and $w$ are coplanar, so
$y \times w$ is also perpendicular to $u$
Thus, the dot product of $u$ and $v \times w$ is zero. i.e.,

$$
u \cdot(v \times w)=0 \quad \because \text { If vectors } a \text { and } b \text { are perpndicular then } a \cdot b=0
$$

Thus, we conclude that if the three vectors $u, v$ and $w$ are coplanar then their scalar triple product is zero.

## Properties of Scalar Triple Product

1. If $u, v$ and $w$ are coplanar, then the volume of the parallelepiped so formed is zero that is $(u \times v) \cdot w=0$ and hence the vectors $u, v, w$ are coplanar $\Leftrightarrow(u \times v) \cdot w=0$
2. If any two vectors of scalar triple product are equal, then its value is zero i.e., $[u u w]=[u v v]=[u w w]=0$
Example 27 Prove that four points
$A(-3,5,-4), B(-1,1,1), C(-1,2,2)$ and $D(-3,4,-5)$ are coplanar.
Proof: $\quad \overrightarrow{A B}=\overrightarrow{O B}-\overrightarrow{O A}=(-1+3) \underline{i}+(1-5) \underline{j}+(1+4) \underline{k}=2 \underline{i}-4 \underline{j}+5 \underline{k}$

$$
\begin{aligned}
& \overrightarrow{A C}=\overrightarrow{O C}-\overrightarrow{O A}=(-1+3) \underline{i}+(2-5) \underline{j}+(2+4) \underline{k}=2 \underline{i}-3 \underline{j}+6 \underline{k} \\
& \overrightarrow{A D}=\overrightarrow{O D}-\overrightarrow{O A}=(-3+3) i+(4-5) j+(-5+4) k=0 i-j-k=-j-k
\end{aligned}
$$

Volume of the parallelepiped formed $\overrightarrow{A B}, \overrightarrow{A C}$ and $\overrightarrow{A D}$ is

$$
\begin{aligned}
& \overrightarrow{[A B A C A D]}=\left|\begin{array}{rrr}
2 & -4 & 5 \\
2 & -3 & 6 \\
0 & -1 & -1
\end{array}\right|=2(3+6)+4(-2-0)+5(-2-0) \\
& =18-8-10 \\
& =0
\end{aligned}
$$

As the volume is zero, so the points $A, B, C$ and $D$ are coplaner.
Example 28 Find the value of $\alpha$, so that $\alpha i+j, i+j+3 k$ and $2 i+j-2 k$ are coplanar.
Solution Let $\underline{u}=\alpha i+j+0 k, \underline{v}=i+j+3 k$ and $\underline{w}=2 i+j-2 k$ be three given vectors. Scalar triple product of given vectors is

$$
\begin{aligned}
& {[\underline{u} \underline{v} \underline{w}]=\left|\begin{array}{lll}
\alpha & 1 & 0 \\
1 & 1 & 3 \\
2 & 1 & -2
\end{array}\right|} \\
& =\alpha(-2-3)-1(-2-6)+0(1-2) \\
& =-5 \alpha+8
\end{aligned}
$$

The vectors will be coplanar if $-5 \alpha+8-0 \Rightarrow \alpha=\frac{8}{5}$

# 14.4.5 Applications of Vectors in Real World

Example 29 A plumber exerts a force of 30 pounds along the negative $y$-axis on a lever connected to a machine. The pivot point of the lever is at the origin $(0,0,0)$, and the force is applied at the point ( $1.2 \mathrm{ft}, 0.5 \mathrm{ft}, 0 \mathrm{ft}$ ). Determine the torque produced by this force about the pivot point.
Solution The position vector $r$ from the origin to the point $(1.2,0.5,0)$ is given by $r=1.2 i+0.5 j+0 k$

The force $\vec{F}$ is exerted downward along negative $y$-axis with a magnitude of 30 pounds is

$$
\underline{F}=0 i-30 j+0 k
$$

Torque $\tau$ produced by the force $=r \times \underline{F}$
Using determinant formula of cross product

$$
\begin{aligned}
\underline{\tau} & =\left|\begin{array}{ccc}
i & j & k \\
1.2 & 0.5 & 0 \\
0 & -30 & 0
\end{array}\right| \\
& =0 i-0 j-36 k \\
\underline{\tau} & =-36 k \text { pound-feet }
\end{aligned}
$$

Thus, the torque is 36 feet-pounds in the negative $z$-direction
Example 30 During a building construction, a crane exerts a force to pull a concrete block, represented by the vector $\underline{F}=[4500,3300,2140]$ Newton. Each component corresponds to the force exerted along the $x, y$, and $z$ axes, respectively. What is the magnitude of this force?
Solution Using the formula for the magnitude of a vector in three-dimensional space

$$
\begin{aligned}
|\underline{F}| & =\sqrt{x^{2}+y^{2}+z^{2}} \\
& =\sqrt{4500^{2}+3300^{2}+2140^{2}} \\
& =\sqrt{20250000+10890000+4579600} \\
& =\sqrt{35719600} \\
& =5976.59
\end{aligned}
$$

The magnitude of the force exerted by the crane is approximately 5976.59 Newton.
Example 11 The components of $\underline{u}=300 \underline{i}+250 \underline{j}+180 \underline{k}$ represent the respective number of jackets, shoes, and handbags sold at a store. The components of $\underline{y}=3500 \underline{i}+4200 \underline{j}+6840 \underline{k}$ represent the respective prices (in rupees) per unit for each product. Find $\underline{u} \cdot \underline{v}$ and explain what the result tells us in real life.
Solution The dot product of $\underline{u}$ and $\underline{v}=\underline{u} \cdot \underline{v}$

$$
\begin{aligned}
& =(300 \underline{i}+250 \underline{j}+180 \underline{k}) \cdot(3500 \underline{i}+4200 \underline{j}+6840 \underline{k}) \\
& =1,050,000+1,050,000+1,231,200 \\
& =3,331,200
\end{aligned}
$$

The result $\underline{u} \cdot \underline{v}=3,331,200$ tells us that total revenue generated from selling all the three product is Rs. 3,331,200.

# EXERCISE 14.4

1. Find the volume of parallelepiped for which the given vectors are three edges
(i) $\underline{u}=3 i+2 k ; \quad \underline{v}=i+2 j+k ; \quad \underline{w}=-j+4 k$
(ii) $\underline{u}=i-4 j-k ; \quad \underline{v}=i-j-2 k ; \quad \underline{w}=2 i-3 j+k$
(iii) $\underline{u}=i-2 j+3 k ; \quad \underline{v}=2 i-j-k ; \quad \underline{w}=j+k$
2. Verify that $a \cdot b \times c=b \cdot c \times a=c \cdot a \times b$

If $a=3 i-j+5 k ; \quad b=4 i+3 j-2 k$ and $c=2 i+5 j+k$
3. Prove that the vectors $i-2 j+3 k,-2 i+3 j-4 k$ and $i-3 j+5 k$ are coplanar.
4. Find the constant $a$ such that the vectors are coplanar.
(i) $i-j+k, i-2 j-3 k$ and $3 i-\alpha j+5 k$
(ii) $i-2 \alpha j-k, \quad i-2 j+2 k$ and $\alpha i-2 j+k$
5. Prove that the points whose position vectors are $A(-6 i+3 j+2 k)$, $B(3 i-2 j+4 k), C(5 i+7 j+3 k), D(-13 i+17 j-k)$ are coplanar.
6. (a) Find the value of :
(i) $2 i \times 2 j \cdot k$
(ii) $3 j \cdot k \times i$
(iii) $[k i j]$
(iv) $[i i k]$
(b) Prove that $u \cdot(v \times w)+v \cdot(w \times u)+w \cdot(u \times v)=3 u \cdot(v \times w)$
7. Find volume of tetrahedron with the vertices
(i) $(0,1,2),(3,2,1),(1,2,1)$ and $(5,5,6)$
(ii) $(2,1,8),(3,2,9),(2,1,4)$ and $(3,3,10)$
8. Prove that the points whose position vectors are $A(3 i+2 j-k), B(i-2 j+k)$, $C(6 i+4 j-2 k), D(9 i+6 j-3 k)$ are coplanar.
9. Prove that for any three non-zero vector $\underline{u}, \underline{v}$ and $\underline{w}$ $(u+v) \cdot[(v+w) \times(w+u)]=2[u v w]$
10. Consider a parallelepiped determined by the vector $\underline{u}=2 i+4 j-3 k$, $\underline{v}=5 i-3 j+6 k$ and $w=4 i-7 j-2 k$. If the base of the parallelepiped is define by the vectors $\underline{u}$ and $\underline{v}$ then find the height of the parallelepiped.
11. A mechanic applies a force of 50 pounds along the positive $x$-axis on a wrench connected to a bolt. The pivot point of the wrench is at the origin $(0,0,0)$, and the force is applied at the point ( $0 \mathrm{ft}, 2 \mathrm{ft}, 3 \mathrm{ft}$ ). Determine the torque produced by this force about the pivot point.

12. A drone flies from point $(1,2,5)$ to point $(4,6,9)$, with each unit representing a meter. What is the magnitude of the displacement the drone experienced during this flight?
13. The vector $u=50 i+75 j+65 k$ shows how many belts, pants, and shirts were sold at a store. The vector $w=1500 i+3500 j+3000 k$ shows the price (in rupees) of each item. Find $u \cdot w$ and explain what the result tells us in real life.
14. A force $F=(20,-10,30) \mathrm{N}$ is applied at a point $P(2,-1,4)$ in 3D space. The pivot point is at $M(1,2,-3)$. Calculate the torque produced by this force about the pivot point $M$.
15. An electric shop sells three types of appliances: Fans, Heaters, and Ovens. The monthly sales quantities are 500 units of Fans, 300 units of Heaters and 200 units of Ovens. The profit per unit for each appliance is Rs 500 for Fans, Rs 400 for Heaters, and Rs 2,000 for Ovens.
(a) Represent the monthly sales quantities and the profit per unit as vectors.
(b) Calculate the total monthly profit using vector operations.

# Answers

## EXERCISE 1.1

1. (i) $\left(\frac{-4}{65}, \frac{-7}{65}\right)$
(ii) $\left(\frac{\sqrt{2}}{7}, \frac{\sqrt{5}}{7}\right)$
(iii) $(1,0)$
2. (i) $\frac{-27}{41}-\frac{38}{41} i$
(ii) $\frac{-17}{2}-\frac{7}{2} i$
(iii) $\frac{1}{2}+\frac{i}{2}$
(iv) $\frac{-44}{25}+\frac{117}{25} i$
3. $\frac{11}{13}-\frac{23}{13} i$
4. (i) $2 \sqrt{145}$
(ii) $\sqrt{149}$
(iii) $\sqrt{1354}$
(iv) $109 \sqrt{109}$
5. 2

## EXERCISE 1.2

1. (i) $x=-19, y=22$
(ii) $x=9, y=6$
(iii) $x=-11, y=28$
2. $x=14, y=9$
3. (i) $x=3 \sqrt{5}, y=2 \sqrt{5} \propto x=-3 \sqrt{5}, y=-2 \sqrt{5}$
(ii) $x=6 \sqrt{2}, y=2 \sqrt{2} \propto x=-6 \sqrt{2}, y=-2 \sqrt{2}$
(iii) $x=0.46, y=0.95 \quad$ or $\quad x=-0.46, y=-0.95$
4. $\alpha=-\frac{4}{3}$
5. $x=8, y=3, a=2, b=1$
6. (i) $3-4 i \mathrm{or}-3+4 i$
(ii) $3-i \mathrm{or}-3+i$
(iii) $2 \sqrt{5}=3 \sqrt{5} i \mathrm{or}-2 \sqrt{3}+3 \sqrt{3} i$
(iv) $12+5 i \mathrm{or}-12-5 i$
7. $\pm(5-2 \sqrt{5} i)$
8. $x=\frac{1}{25}, y=\frac{-57}{25}$
9. $x=\frac{-24}{29}, y=\frac{31}{29}$
10. $u=-8, v=13$
11. $\alpha=\frac{5}{2}$

## EXERCISE 1.3

1. (i) $(a+i 2 b)(a-i 2 b)$
(ii) $(3 a+i 4 b)(3 a-i 4 b)$
(iii) $3(x+i y)(x-i y)$
(iv) $9(4 x+i 5 y)(4 x-i 5 y)$
(v) $(z-i)(z-i)$
(vi) $(z+3-2 i)(z+3+2 i)$
(vii) $(z+2-i)(z+2+i)$
(viii) $2\left(z-\frac{11-3 i}{2} i z-\frac{11+3 i}{2}\right)$
2. (i) $(z+2)(z-1+i \sqrt{3})(z-1-i \sqrt{3})$
(ii) $(z+3)\left(z-\frac{3}{2}+\frac{3 \sqrt{3} i}{2}\right)\left(z-\frac{3}{2}-\frac{3 \sqrt{3} i}{2}\right)$
(iii) $(z-2)(z-4 i)(z+4 i)$
(iv) $(z-2)(z+2)(z-5 i)(z+5 i)$
(v) $(z-2)(z+2)(z-2 i)(z+2 i)$
(vi) $(z+1)(z-1)(z+2 i)(z-2 i)$
(vii) $(z-\sqrt{2} i)(z+\sqrt{2} i)(z-\sqrt{3} i)(z+\sqrt{3} i)$
(viii) $(z-9)(z+9)(z-7 i)(z+7 i)$
3. Roots: $3,-3,4 i,-4 i$ Linear factor: $(z+3)(z-3)(z+4 i)(z-4 i)$ 4. (i) $z=\frac{3 \pm i \sqrt{23}}{4}$
(ii) $z=3 \pm i \sqrt{21}$
(iii) $z=3 \pm \frac{\sqrt{69} i}{3}$
(iv) $z=-2 \pm 3 i$
(v) $z=-\frac{3}{2}+\frac{3}{2} i$
(vi) $z=\frac{5 \pm \sqrt{59} i}{6}$
4. (i) $2,-2,2 i,-2 i$
(ii) $0,3,-3,3 i,-3 i$
(iii) $0,1,-1, i,-i$
(iv) $5, i,-i$
(v) $\sqrt{7},-\sqrt{7}, \frac{\sqrt{3} i}{2},-\frac{\sqrt{3} i}{2}$
(vi) $-1, i,-i$

6. $$x = -2z^3 + 6z^2 - 8z + 24$$
7. $$x = 10z^4 + 30z^2 - 40$$
8. $$x = -3z^4 + 6z^3 + 42z^2 - 96z + 96$$

## EXERCISE 1.4

1. i) $$(2, 2m, 2m^3)$$
   ii) $$(-2, -2m, -2m^3)$$
   iii) $$(-3, -3m, -3m^3)$$
   iv) $$(4, 4m, 4m^3)$$
   v) $$(-5, -5m, -5m^3)$$
2. (i) $$2, -2, 2i, -2i$$
   (ii) $$3, -3, 3i, -3i$$

(iii) $$5, -5, 5i, -5i$$

4. (i) $$-1$$
   (ii) $$-32$$

7. 0

## EXERCISE 1.5

1. (i)

2. i) $5(\cos 36.87+i \sin 36.87)$
ii) $\sqrt{2}\left(\cos \frac{\pi}{4}+i \sin \frac{\pi}{4}\right)$
iii) $1 \cdot\left(\cos \frac{\pi}{3}+i \sin \frac{\pi}{3}\right)$
iv) $5\left(\cos \frac{4 \pi}{3}+i \sin \frac{4 \pi}{3}\right)$
(v) $1 \cdot\left(\cos \left(-\frac{\pi}{2}\right)+i \sin \left(\frac{\pi}{2}\right)\right)$
(vi) $1 \cdot\left(\cos \left(-\frac{\pi}{6}\right)+i \sin \left(-\frac{\pi}{6}\right)\right)$
(vii) $1 \cdot\left(\cos \left(\tan ^{-1} \frac{7}{24}\right)+i \sin \left(\tan ^{-1} \frac{7}{24}\right)\right)$
3.
(i) $2-2 \sqrt{3} i$
(ii) $-\frac{3 \sqrt{3}}{4}-\frac{3}{4} i$
(iii) $6.76-1.81 i$
(iv) $-10.62-2.85 i$
(v) $-0.86+3.21 i$
(vi) $1.68-1.09 i$
4. (i) $-3.86-2.03 i$
(ii) $-8.86-10.69 i$
(iii) $45\left(\cos \frac{19 \pi}{12}+i \sin \frac{19 \pi}{12}\right)$
(iv) $\frac{9}{5}\left(\cos \frac{11 \pi}{12}+i \sin \frac{11 \pi}{12}\right)$
5. (i) $-3.86+1.03 i$
(ii) $17.38-4.65 i$
(iii) $-66.68+38.5 i$
(iv) $-\frac{7}{11}+0 i$
7. $2\left(\cos 120+i \sin 120^{\circ}\right),-1+i \sqrt{3}$
8. $10(\cos 150+i \sin 150),-5 \sqrt{3}+5 i$
9. $|z|=2 \sqrt{2}, \arg (z)=\frac{5 \pi}{4}+2 \pi \pi$
10. $y=\sqrt{3} x-2 \sqrt{3}+1$
13. $y=-x$
14. $y=-\frac{7}{3} x-\frac{2}{15}$
15. $y=-x+\frac{1}{3}$
17. 1
18. $120\left(\cos \frac{\pi}{12}-i \sin \frac{\pi}{12}\right)$
19. Rectangular form: $2+14 i$, Polar From: $10 \sqrt{2}(\cos 81.87+i \sin 81.87)$

# EXERCISE 2.1

1. (a) (i) 8
(ii) -1
(iii) $x^{2}-4 x+3$
(iv) $x^{4}+6 x^{2}+8$
(b) (i) $\sqrt{-3}$
(ii) $\sqrt{3}$
(iii) $\sqrt{2 x-1}$
(iv) $\sqrt{2 x^{2}+9}$

2. (i) 4 (ii) $\frac{2}{h} \cos \left(a+\frac{h}{2}\right) \sin \left(\frac{h}{2}\right)$ (iii) $h^{2}+3 a h+h+3 a^{2}+2 a$
(iv) $\frac{\sinh }{h \cos a \cos (a+h)}$
3. (a) $A=\frac{P^{2}}{16}$
(b) $C=2 \sqrt{\pi A}$
(c) $S=6 V^{2 / 3}$
4. (i) Domain $g=(-\infty, \infty)$, Range $g=(-\infty, \infty)$
(ii) Domain $g=[-2, \infty)$, Range $g=[0, \infty)$
(iii) Domain $g=(-\infty, \infty)$, Range $g=(-\infty, 10)$
(iv) Domain $g=(-\infty, \infty)$, Range $g=[0, \infty)$
(v) Domain $g=R-\{3\}$, Range $g=R-\{-1\}$
5. $a=2, b=-2$
6. (i) (a) 30 m
(b) 17.5 m
(c) 11.1 m
(ii) $x=2 \sec$
7. (i) Domain $f=(-\infty, \infty)$, Range $f=(-\infty, \infty)$
(ii) Yes, the function is one-to-one, because equal outputs implies equal inputs.
(iii) Yes, the function is onto when the codomain is all real numbers.
8. (i) Domain $f=R-\{-1\}$, Range $f=R-\{2\}$
(ii) $f(x)$ is not onto.
9. $g(x)$ is surjective.

# EXERCISE 2.2

1. (i)
(ii)
(iii)
(iv)
[^0]
[^0]:    (v)
    (vi)
    (vii)

(vi)
4. (i) 14 months
(ii) 373.2 metres
5. 25 grams

# EXERCISE 3.1

1. (i) Minimum value at $x=-3$ is 4
(ii) Minimum value at $x=-2$ is -4
(iii) Maximum value at $x=4$ is 29
(iv) Maximum value at $x=\frac{-3}{2}$ is $\frac{-11}{4}$
(v) Minimum value at $x=-1$ is -16 (vi) Maximum value at $x=\frac{1}{4}$ is $\frac{169}{8}$
2. (i) Minimum value at $x=2$ is -4 ; Domain $f=(-\infty, \infty)$; Range $f=[-4, \infty)$
(ii) Minimum value at $x=\frac{5}{2}$ is $\frac{-1}{4}$; Domain $f=(-\infty, \infty)$; Range $f=\left[\frac{-1}{4}, \infty\right)$
(iii) Maximum value at $x=1$ is -7 ; Domain $f=(-\infty, \infty)$; Range $f=(-\infty,-7]$
(iv) Minimum value at $x=2$ is 0 ; Domain $f=(-\infty, \infty)$; Range $f=[0, \infty)$
(v) Minimum value at $x=-1$ is -9.3 ; Domain $f=(-\infty, \infty)$; Range $f=[-9.3, \infty)$
(vi) Maximum value at $x=\frac{-1}{2}$ is $\frac{25}{4}$; Domain $f=(-\infty, \infty)$; Range $f=\left(-\infty, \frac{25}{4}\right]$
3. (i) $f^{-1}(x)=\sqrt{x+3}$; Domain $f^{-1}=[-3, \infty)$; Range $f^{-1}=(-\infty, 0]$

(ii) $f^{-1}(x)=-3-\sqrt{5+x}$; Domain $f^{-1}=(-5, \infty)$; Range $f^{-1}=(-3, \infty)$
(iii) $f^{-1}(x)=\frac{4+\sqrt{2-3+x}}{2}$; Domain $f^{-1}=[-3, \infty)$; Range $f^{-1}=[2, \infty)$
(iv) $f^{-1}(x)=\frac{1+\sqrt{3 x-17}}{3}$; Domain $f^{-1}=[71, \infty)$; Range $f^{-1}=[5, \infty)$
(v) $f^{-1}(x)=3+\sqrt{\frac{x-1}{2}}$; Domain $f^{-1}=[1, \infty)$; Range $f^{-1}=[3, \infty)$
(vi) $f^{-1}(x)=-4-\sqrt{\frac{(x+5)}{3}}$; Domain $f^{-1}=(-\infty,-5)$; Range $f^{-1}=(-\infty,-4]$
4.
(i) $\{-2,2\}$
(ii) $\{-1,-4\}$
(iii) $\{3-\sqrt{5}, 3+\sqrt{5}\}$
(iv) $\left\{\frac{3-\sqrt{7}}{2}, \frac{1}{2}, \frac{3}{2}, \frac{3+\sqrt{7}}{2}\right\}$
(v) $\{(-3,3)\}$
(vi) $\left\{\frac{3-\sqrt{17}}{2}\right\} \cup\left\{\frac{3+\sqrt{17}}{2}, \infty\right\}$
(vii) $\{(-\sqrt{5}+3, \sqrt{5}+3)\}$
(viii) $\left\{\frac{3}{2}, \frac{\sqrt{17}+3}{4}\right\} \cup\left\{\frac{\sqrt{17}+3}{4}, 3\right\}$

# EXERCISE 3.2

1. (i) $\left\{1, \frac{1}{2}\right\}$
(ii) $\{-2,1\}$
(iii) $\left\{\frac{-3}{2}, 1\right\}$
(iv) $\left\{\frac{a+b}{a b}, \frac{2}{a+b}\right\}$
(v) $\}$
(vi) $\left\{\frac{1}{3}, \frac{-16}{3}\right\}$
(vii) $\{4\}$
(viii) $\{4,20\}$
(ix) $\{2\}$
(x) $\{4\}$
2. 20 days
3. 15 sheep
4. 97 dozen eggs
5. 6 hours
$0 \leq \mathrm{s} \leq 4756 \mathrm{~km} / \mathrm{h}$
6. $[0.586 \mathrm{sec}, 3.414 \mathrm{sec}]$

## EXERCISE 4.1

2. (i) $\left[\begin{array}{rrr}-2 & -2 & 3 \\ 2 & 0 & -3 \\ 0 & -2 & 3\end{array}\right]$
(ii) $\left[\begin{array}{rrr}1 & 1 & 1 \\ 2 & -3 & 4 \\ -4 & -2 & 2\end{array}\right]$
(iii) $\left[\begin{array}{rrr}-3 & -2 & 5 \\ 3 & -5 & -3 \\ -3 & -6 & 4\end{array}\right]$
(iv) $\left[\begin{array}{rrr}-1 & -2 & 1 \\ 1 & 5 & -3 \\ 3 & 2 & 2\end{array}\right]$

5. $A+A^{\prime}=\left[\begin{array}{ccc}-2 & 3 & 0 \\ 3 & 0 & 7 \\ 0 & 7 & 6\end{array}\right], A-A^{\prime}=\left[\begin{array}{ccc}0 & 1 & 6 \\ -1 & 0 & -3 \\ -6 & 3 & 0\end{array}\right], A A^{\prime}=\left[\begin{array}{ccc}14 & 5 & 22 \\ 5 & 5 & 3 \\ 22 & 3 & 43\end{array}\right]$,
$A^{\prime} A=\left[\begin{array}{ccc}11 & -17 & -10 \\ -17 & 29 & 21 \\ -10 & 21 & 22\end{array}\right],\left(A^{\prime}\right)^{\prime}=\left[\begin{array}{ccc}-1 & 2 & 3 \\ 1 & 0 & 2 \\ -3 & 5 & 3\end{array}\right]$
6. $\left[\begin{array}{ccc}-1 & -1 & -3 \\ -1 & -3 & -10 \\ -5 & 4 & 2\end{array}\right]$

# EXERCISE 4.2

1. (i) -21 (ii) $9 a b^{3}$ (iii) $4 x y z$
2. (i) $A_{15}=-10, A_{23}=-2, A_{33}=-5,|A|=-5$ (ii) $B_{31}=-3, B_{32}=5, B_{33}=-1,|B|=-1$
3. (i) $x=\frac{1}{2}$
(ii) $x=-1$ or 2
(iii) $x=2$ or 3
4. (i) 147,0
(ii) 0,96
5. $A=\frac{1}{2}, A=-4$

## EXERCISE 4.3

1. (i) $\left[\begin{array}{ccc}1 & \frac{17}{4} & \frac{1}{2} \\ 0 & \frac{-1}{2} & 0 \\ \frac{1}{3} & \frac{11}{6} & \frac{1}{3}\end{array}\right]$
(ii) $\left[\begin{array}{ccc}-\frac{-2}{5} & -2 & \frac{7}{5} \\ \frac{4}{5} & \frac{3}{10} & -4 \\ \frac{1}{5} & \frac{1}{5} & -1 \\ \frac{1}{5} & \frac{1}{5} & \frac{-1}{5}\end{array}\right]$
(iii) $\left[\begin{array}{ccc}-\frac{-13}{3} & \frac{8}{3} & \frac{26}{3} \\ \frac{2}{3} & \frac{-1}{3} & -4 \\ \frac{2}{3} & \frac{-1}{3} & -1 \\ \frac{2}{3} & \frac{-1}{3} & \frac{-1}{3}\end{array}\right]$
2. (i) Rank $=3$
(ii) Rank $=3$
(iii) Rank $=4$
3. (i) $\{(1,0,1)\}$
(ii) $\left\{\left(\frac{68}{55}, \frac{59}{55}, \frac{62}{55}\right)\right\}$
(iii) $\left\{\left(\frac{8}{3}, 2,-\frac{7}{3}\right)\right\}$
4. (i) $\{(1,1,0)\}$
(ii) $\left\{\left(\frac{-8}{9}, \frac{10}{9}, \frac{11}{9}\right)\right\}$
(iii) $\{(1,1,1)\}$
5. (i) $\left\{\left(\frac{19}{23}, \frac{9}{23}, \frac{12}{23}\right)\right\}$
(ii) $\left\{\left(\frac{22}{9}, \frac{1}{3},-\frac{10}{9}\right)\right\}$
(iii) $\left\{\left(\frac{61}{16}, \frac{-1}{4}, \frac{-13}{16}\right)\right\}$

6. (i) $\{(0,0,0)\}$
(ii) $x_{1}=2 t, x_{2}=-t, x_{3}=t$
(iii) $x_{1}=-3 t, x_{2}=2 t, x_{3}=t$
7. $A^{\prime}(-4,1), B^{\prime}(2,5), C^{\prime}(0,-3)$
8. $A^{\prime}(-6,-4,1)$
9. $\frac{3 x^{\prime}-y^{\prime}}{2}=\left(y^{\prime}-2 x^{\prime}\right)^{2}$
10. $\left[\begin{array}{l}16 \\ 22 \\ 15\end{array}\right]\left[\begin{array}{l}36 \\ 43 \\ 49\end{array}\right]\left[\begin{array}{l}21 \\ 26 \\ 16\end{array}\right]$
11. HOLD FIRE

# EXERCISE 5.1

1. $\frac{1}{x-1}-\frac{1}{x+1}$
2. $\frac{1}{x-a}-\frac{1}{x-b}$
3. $1+\frac{1}{x-1}-\frac{1}{x+1}$
4. $\frac{1}{2(x+1)}+\frac{1}{x+2}-\frac{3}{2(x+3)}$
5. $\frac{1}{x+1}-\frac{1}{x+2}+\frac{1}{x+3}$
6. $4 x+5+\frac{2}{x-1}-\frac{1}{x+1}$
7. $\frac{1}{x-1}+\frac{1}{x-2}+\frac{1}{x-3}$
8. $1+\frac{3}{x-4}-\frac{24}{x-5}+\frac{30}{x-6}$
9. $\frac{a}{(a-b)(c-a)\left(x^{2}+a\right)}+\frac{b}{(a-b)(b-c)\left(x^{2}+b\right)}+\frac{c}{(c-a)(b-c)\left(x^{2}+c\right)}$
10. $\frac{1}{x-1}+\frac{2}{(x-1)^{2}}$
11. $-\frac{1}{4(x+1)}+\frac{1}{4(x-1)}+\frac{1}{2(x-1)^{2}}$
12. $\frac{3}{x-1}+\frac{10}{(x-1)^{2}}+\frac{2}{(x-1)^{3}}$
13. $\frac{1}{x}-\frac{1}{x+1}-\frac{1}{(x+1)^{2}}-\frac{1}{(x+1)^{3}}$
14. $\frac{2}{x+1}+\frac{2}{x-1}+\frac{1}{(x-1)^{2}}$
15. $\frac{3}{x-2}-\frac{3}{x+2}$

## EXERCISE 5.2

1. $\frac{1}{x+1}+\frac{x+2}{x^{2}+1}$
2. $\frac{1}{3(x-2)}-\frac{x-1}{3\left(x^{2}+3 x+5\right)}$
3. $\frac{1}{x-2}-\frac{x+2}{x^{2}+2}-\frac{2(3 x+5)}{\left(x^{2}+2\right)^{2}}$
4. $\frac{2}{x+1}+\frac{x+1}{x^{2}-x+1}$
5. $1-\frac{2}{x^{2}+1}+\frac{1}{\left(x^{2}+1\right)^{2}}$
6. $\frac{1}{2-x}+\frac{1}{2+x}-\frac{2}{x^{2}+4}-\frac{8}{\left(x^{2}+4\right)^{2}}$

## EXERCISE 6.1

1. (i) $24,28,32,36$ (ii) $-3,-5,-7,-9$
2. (i) $8,11,14$
(ii) $3,5,13$
(iii) $-4,-3,0$
(iv) $-1,3, \frac{3}{5}$

# Answers

## (v) 3, 4, 14