# Chapter
# 14

## Vectors in Space

## INTRODUCTION

In this unit, we will look into the rectangular coordinate system in three-dimensional space and explore the fundamental mathematical operations involving vectors in space. We will begin by understanding the dot product (or scalar product) and the cross product (or vector product) of two vectors and learn about their geometric interpretation. Further, we emphasize their practical applications. For example, we will see how these concepts can be used to calculate the area of a triangle and the area of a parallelogram. Finally, we will explore the extensive use of vectors in three-dimensional space, particularly in physics, where they play an important role in determining forces, velocities, and other essential physical quantities. For example, determining the work done by a constant force when moving an object along a specified vector.

### 14.1 Vectors (Recall)

In previous classes, we learned about two fundamental quantities: scalars and vectors. A scalar is a quantity that has only magnitude or size, such as mass, time, density, temperature, length, volume, speed, work etc. On the other hand, a vector is a quantity that has both magnitude and direction, for example displacement, velocity, acceleration, weight, force, momentum, electric and magnetic fields, etc.
Geometrically, a vector is represented as a directed line segment $\overrightarrow{A B}$ with $A$ as its initial point and $B$ as the terminal point.
In two-dimension $\left(R^{2}\right)$ a vector has components that can be represented by an ordered pair $[x, y]$ of real numbers. For the vector $\underline{u}=[x, y], x$ and $y$ represent the components of $\underline{u}$.
Addition of Vectors: For any two vectors $\underline{u}=\left[x_{1}, y_{1}\right]$ and $\underline{y}=\left[x_{2}, y_{2}\right]$, we have

$$
\underline{u}+\underline{y}=\left[x_{1}, y_{1}\right]+\left[x_{2}, y_{2}\right]=\left[x_{1}+x_{2}, y_{1}+y_{2}\right]
$$

Scalar Multiplication of a Vector: For $\underline{u}=[x, y]$ and $a \in R$, we have

$$
a \underline{u}=a[x, y]=[a x, a y]
$$

Equal Vectors: Two vectors $\underline{u}=\left[x_{1}, y_{1}\right]$ and $\underline{y}=\left[x_{2}, y_{2}\right]$ of $R^{2}$ are said to be equal

if and only if they have the same components. That is, $\left[x_{1}, y_{1}\right]=\left[x_{2}, y_{2}\right]$ if and only if $x_{1}=x_{2}$ and $y_{1}=y_{2}$ and we write $\underline{u}=\underline{v}$
In other words, two vectors $\underline{u}$ and $\underline{v}$ are said to be equal, if they have same magnitude and same direction.
Parallel Vectors: Two vectors are parallel if and only if they are non-zero scalar multiple of each other.
For example, vectors $\overrightarrow{A B},-\overrightarrow{A B}$ and $\frac{3}{2} \overrightarrow{A B}$ are parallel.

# Magnitude of a Vector

The magnitude (or norm or length) of a vector in 2D represents the length of the vector from the origin to the point represented by the vector. For any vector $\underline{u}=[x, y]$ in $R^{2}$, we define the magnitude, as the distance of the point $P(x, y)$ from the origin $O$.

Magnitude of $\overrightarrow{O P}=|\overrightarrow{O P}|=|\underline{u}|=\sqrt{x^{2}+y^{2}}$
Now, we will learn some mathematical operations involving vectors in three-dimensional space.

### 14.1.1 Rectangular Coordinate System in Space

In space a rectangular coordinate system is constructed using three mutually orthogonal (perpendicular) axes, which have origin as their common point of intersection. When sketching figures, we follow the convention that the positive $x$-axis points towards the reader, the positive $y$-axis to the right and the positive $z$-axis points upwards.
These axes are also labeled in accordance with the righthand rule. The fingers of the right hand, pointing in the direction of the positive $x$-axis, curled images toward the positive $y$-axis, and the thumb will point in the direction of the positive $z$-axis. A point $P$ in space has three coordinates, one along $x$-axis, the second along $y$-axis and the third along $z$-axis. If the
Right hand rule

# Unit 44 Vectors in Space

directed distances along $x$-axis, $y$-axis and $z$-axis respectively are $a, b$ and $c$, then the point $P$ is written with a unique triple of real numbers as $P(a, b, c)$ (see figure).

### 14.1.2 Concept of a Vector in Space

The set $R^{3}=\{(x, y, z): x, y, z \in R\}$ is called 3-dimensional space. An element $(x, y, z)$ of $R^{3}$ represents a point $P(x, y, z)$, which is uniquely determined by its coordinates $x, y$ and $z$. Given a vector $\underline{u}$ in space, there exists a unique point $P(x, y, z)$ in space such that the vector $\overrightarrow{O P}$ is equal to $\underline{u}$ (see figure). Now each element $(x, y, z) \in R^{3}$ is associated with a unique ordered triple $(x, y, z)$, which represents the vector $\underline{u}=\overrightarrow{O P}=[x, y, z]$.

### 14.1.3 Fundamental Mathematical Operations for Vectors in Space

We define addition and scalar multiplication in $R^{3}$ by:
(i) Addition of Vectors: For any two vectors $\underline{u}=[x, y, z]$ and $\underline{y}=\left[x^{\prime}, y^{\prime}, z^{\prime}\right]$ we have $\underline{u}+\underline{v}=[x, y, z]+\left[x^{\prime}, y^{\prime}, z^{\prime}\right]=\left[x+x^{\prime}, y+y^{\prime}, z+z^{\prime}\right]$
(ii) Scalar Multiplication of a Vector: For $\underline{u}=[x, y, z]$ and $a \in R$, we have $a \underline{u}=a[x, y, z]=[a x, a y, a z]$
The set of all ordered triples $[x, y, z]$ of real numbers, together with the rules of addition and scalar multiplication is called the set of vectors in $R^{3}$. For the vector $\underline{u}=[x, y, z], x, y$ and $z$ are called the components of $\underline{u}$. The definition of vectors in $R^{3}$ states that vector addition and scalar multiplication are to be carried out also for vectors in space just as for vectors in the plane. Similarly, we define in $R^{3}$ :
(a) The negative of the vector $\underline{u}=[x, y, z]$ as $-\underline{u}=(-1) \underline{u}=[-x,-y,-z]$
(b) The difference of two vectors $\underline{y}=\left[x^{\prime}, y^{\prime}, z^{\prime}\right]$ and $\underline{w}=\left[x^{\prime \prime}, y^{\prime \prime}, z^{\prime \prime}\right]$ as

$$
\underline{v}-\underline{w}=\underline{v}+(-\underline{w})=\left[x^{\prime}-x^{\prime \prime}, y^{\prime}-y^{\prime \prime}, z^{\prime}-z^{\prime \prime}\right]
$$

(c) The zero vector as $O=[0,0,0]$
(d) Equality of two vectors: Two vectors $\underline{y}=\left[x^{\prime}, y^{\prime}, z^{\prime}\right]$ and $\underline{w}=\left[x^{\prime \prime}, y^{\prime \prime}, z^{\prime \prime}\right]$ are equal that is $\underline{v}=\underline{w}$ if and only if $x^{\prime}=x^{\prime \prime}, y^{\prime}=y^{\prime \prime}$ and $z^{\prime}=z^{\prime \prime}$.
(e) Position Vector

For any point $P(x, y, z)$ in $R^{3}$, a vector $\underline{u}=[x, y, z]$ is represented by a directed line segment $\overrightarrow{O P}$, whose initial point is at origin. Such vectors are called position vectors in $R^{3}$.

# 14.1.4 Magnitude of a Vector in Space

We define the magnitude, norm, or length of a vector $\underline{u}=[x, y, z]$ in space by the distance of the point $P(x, y, z)$ from the origin $O$.

$$
\therefore \quad \overrightarrow{O P}=|u|=\sqrt{x^{2}+y^{2}+z^{2}}
$$

Example 1 For the vectors, $\underline{u}=[1,-2,3], \underline{y}=[2,1,3]$ and $\underline{w}=[-1,4,0]$, find the following:
(i) $\underline{y}+\underline{w}$
(ii) $2 \underline{w}$
(iii) $|u|$
(iv) $|\underline{v}-2 \underline{w}|$
(v) $|2 \underline{u}-\underline{y}+3 \underline{w}|$

Solution (i) $\underline{y}+\underline{w}=[2-1,1+4,3+0]=[1,5,3]$
(ii) $2 \underline{w}=2[-1,4,0]=[-2,8,0]$
(iii) $|u|=[1,-2,3]=\sqrt{(1)^{2}+(-2)^{2}+(3)^{2}}=\sqrt{1+4+9}=\sqrt{14}$
(iv) $|\underline{v}-2 \underline{w}|=|[2+2,1-8,3-0]|=|[4,-7,3]|$

$$
=\sqrt{(4)^{2}+(-7)^{2}+(3)^{2}}=\sqrt{16+49+9}=\sqrt{74}
$$

(v) $|2 \underline{u}-\underline{y}+3 \underline{w}|=|2[1,-2,3]-[2,1,3]+3[-1,4,0]|=|[2,-4,6]-[2,1,3]+[-3,12,0]|$

$$
=[-3,7,3]=\sqrt{(-3)^{2}+(7)^{2}+(3)^{2}}=\sqrt{9+49+9}=\sqrt{67}
$$

### 14.1.5 Components of a Vector

As in plane, we introduce three special vectors $i=[1,0,0]$, $j=[0,1,0]$ and $k=[0,0,1]$ in $R^{3}$

As magnitude of $i=\sqrt{1^{2}+0^{2}+0^{2}}=1$
magnitude of $j=\sqrt{0^{2}+1^{2}+0^{2}}=1$ and
magnitude of $k=\sqrt{0^{2}+0^{2}+1^{2}}=1$. So, $i, j$
and $k$ are called unit vectors along $x$-axis, $y$-axis and $z$-axis respectively. Using the definition of addition and scalar multiplication, the vector $[x, y, z]$ can be written as:

$$
\begin{aligned}
\underline{u}=[x, y, z] & =[x, 0,0]+[0, y, 0]+[0,0, z] \\
& =x[1,0,0]+y[0,1,0]+z[0,0,1]=x i+y j+z k
\end{aligned}
$$

Thus, each vector $[x, y, z]$ in $R^{3}$ can be uniquely represented by $x i+y i+z k$.

## Unit Vector

A unit vector is defined as a vector whose magnitude is unity. In three-dimensional space the unit vector of the vector $\underline{u}=x i+y j+z k$ is written as $\hat{u}$ (read as $u$ hat) and

is defined by

$$
\hat{u}=\frac{u}{|u|}=\frac{x}{\sqrt{x^{2}+y^{2}+z^{2}}} i+\frac{y}{\sqrt{x^{2}+y^{2}+z^{2}}} j+\frac{z}{\sqrt{x^{2}+y^{2}+z^{2}}} k
$$

In terms of unit vector $i, j$, and $k$, the sum $u+y$ of two vectors.
$\underline{u}=\left[x_{1}, y_{1}, z_{1}\right]$ and $y=\left[x_{2}, y_{2}, z_{2}\right]$ is written as:

$$
\begin{aligned}
\underline{u}+\underline{v} & =\left[x_{1}+x_{2}, y_{1}+y_{2}, z_{1}+z_{2}\right] \\
& =\left(x_{1}+x_{2}\right) i+\left(y_{1}+y_{2}\right) j+\left(z_{1}+z_{2}\right) k
\end{aligned}
$$

Example 2 Find the unit vector of $\underline{u}=2 i+5 j-k$.
Solution Given vector $\underline{u}=2 i+5 \underline{j}-k$, to find the unit vector

$$
\begin{aligned}
& \Rightarrow \quad|u|=\sqrt{(2)^{2}+(5)^{2}+(-1)^{2}}=\sqrt{30} \\
& \quad \text { The unit vector is: } \\
& \Rightarrow \quad \hat{u}=\frac{u}{|u|}=\frac{2 i+5 j-k}{\sqrt{30}}=\frac{1}{\sqrt{30}}(2 i+5 j-k)
\end{aligned}
$$

Thus, $\hat{u}=\frac{1}{\sqrt{30}}(2 i+5 j-k)$ is the required unit vector.
Example 3 If $\underline{u}=2 i+3 j+k, \underline{v}=4 i+6 j+2 k$ and $\underline{w}=-6 i-9 j-3 k$, then show that $\underline{u}, \underline{v}$ and $\underline{w}$ are parallel to each other.
Solution $\quad \underline{v}=4 i+6 j+2 k=2(2 i+3 j+k)$

$$
\therefore \quad \underline{v}=2 \underline{u}
$$

$\Rightarrow \underline{u}$ and $\underline{v}$ are parallel vectors.

$$
\begin{aligned}
& \underline{w}=-6 i-9 j-3 k \\
& =-3(2 i+3 j+k) \quad \therefore \quad \underline{w}=-3 \underline{u}
\end{aligned}
$$

$\Rightarrow \underline{u}$ and $\underline{w}$ are parallel vectors.
Hence $\underline{u}, \underline{v}$ and $\underline{w}$ are parallel to each other.

# 14.1.6 Properties of Vectors

Let $\underline{u}, \underline{v}$ and $\underline{w}$ be vectors in the plane or in space and let $a, b \in R$, then they have the following properties:
(i) $\underline{u}+\underline{v}=\underline{v}+\underline{u}$
(Commutative property)
(ii) $(\underline{u}+\underline{v})+\underline{w}=\underline{u}+(\underline{v}+\underline{w})$
(Associative property)
(iii) $\underline{u}+\underline{o}=\underline{u}$
(Additive Identity)
(iv) $\underline{u}+(-1) \underline{u}=\underline{u}-\underline{u}=\underline{o}$
(Inverse for vector addition)
(v) $a(\underline{v}+\underline{w})=a \underline{v}+\alpha \underline{w}$
(Distributive property)
(vi) $a(b \underline{u})=(a b) \underline{u}$
(Scalar multiplication)

Proof: (i) Since for any two real numbers $a, b \in R, a+b=b+a$, it follows that for any two vectors $\underline{u}=[x, y, z]$ and $\underline{y}=\left[x^{\prime}, y^{\prime}, z^{\prime}\right]$ in $R^{3}$, where components of $\underline{u}$ and $\underline{y}$ belong to $R$.
We have

$$
\begin{aligned}
\underline{u}+\underline{y} & =[x, y, z]+\left[x^{\prime}, y^{\prime}, z^{\prime}\right] \\
& =\left[x+x^{\prime}, y+y^{\prime}, z+z^{\prime}\right] \\
& =\left[x^{\prime}+x, y^{\prime}+y, z^{\prime}+z\right] \quad \because \quad a+b=b+a \\
& =\left[x^{\prime}, y^{\prime}, z^{\prime}\right]+[x, y, z] \\
& =\underline{y}+\underline{u}
\end{aligned}
$$

So, addition of vectors in $R^{3}$ is commutative.
(ii) Since for any three real numbers $a, b, c \in R,(a+b)+c=a+(b+c)$, it follows that for any three vectors, $\underline{u}=[x, y, z], \underline{y}=\left[x^{\prime}, y^{\prime}, z^{\prime}\right]$ and $\underline{w}=\left[x^{\prime \prime}, y^{\prime \prime}, z^{\prime \prime}\right]$ in $R^{3}$. Where components of $\underline{u}, \underline{y}$ and $\underline{w}$ belong to $R$.
We have

$$
\begin{aligned}
(\underline{u}+\underline{y})+\underline{w} & =\left[x+x^{\prime}, y+y^{\prime}, z+z^{\prime}\right]+\left[x^{\prime \prime}, y^{\prime \prime}, z^{\prime \prime}\right] \\
& =\left[\left(x+x^{\prime}\right)+x^{\prime \prime},\left(y+y^{\prime}\right)+y^{\prime \prime},\left(z+z^{\prime}\right)+z^{\prime \prime}\right] \\
& =\left[x+\left(x^{\prime}+x^{\prime \prime}\right), y+\left(y^{\prime}+y^{\prime \prime}\right), z+\left(z^{\prime}+z^{\prime \prime}\right)\right] \\
& \because \quad(a+b)+c=a+(b+c) \\
& =[x, y, z]+\left[x^{\prime}+x^{\prime \prime}, y^{\prime}+y^{\prime \prime}, z^{\prime}+z^{\prime \prime}\right] \\
& =\underline{u}+(\underline{y}+\underline{w})
\end{aligned}
$$

So, addition of vectors in $R^{3}$ is associative.
(iii) Since for any real number $a$ and 0

$$
a+0=a, \text { it follows that }
$$

for any vectors, $\underline{u}=[x, y, z]$, and $\underline{o}=[0,0,0]$, where $\underline{o}$ is the zero vector in $R^{3}$.
We have

$$
\begin{aligned}
\underline{u}+\underline{o} & =[x, y, z]+[0,0,0] \\
& =[x+0, y+0, z+0] \\
& =[x, y, z]=\underline{u} \\
\underline{u}+\underline{o} & =\underline{u}
\end{aligned}
$$

Thus, $\underline{o}$ is the additive identity in $\mathrm{R}^{3}$
(iv) Since for any real number $a$, there exist $-a$ such that

$$
a+(-a)=a-a=0 \quad, \quad \text { it follows that }
$$

for any vector, $\underline{u}=[x, y, z]$, there exists $-\underline{u}=[-x,-y,-z]$ in $R^{3}$
Such that

$$
\begin{aligned}
\underline{u}+(-\underline{u}) & =[x, y, z]+[-\infty x,-y,-z]=[x+(-x), y+(-y), z+(-z)] \\
& =[x-x, y-y, z-z] \\
& =[0,0,0]=\underline{o}, \text { where } \underline{o} \text { is the additive identity } \\
\underline{u}+(-\underline{u}) & =\underline{o}
\end{aligned}
$$

Thus $-\underline{u}$ is the additive inverse of $\underline{u}$ in $\mathrm{R}^{3}$
The proofs of the other parts are left as an exercise for the students.

# 14.1.7 Distance Between Two Points in Space

If $\overrightarrow{O P_{1}}$ and $\overrightarrow{O P_{2}}$ are the position vectors of the points $P_{1}\left(x_{1}, y_{1}, z_{1}\right)$ and $P_{2}\left(x_{2}, y_{2}, z_{2}\right)$
The vector $\overrightarrow{P_{1} P_{2}}$ is given by

$$
\overrightarrow{P_{1} P_{2}}=\overrightarrow{O P_{2}}-\overrightarrow{O P_{1}}=\left[x_{2}-x_{1}, y_{2}-y_{1}, z_{2}-z_{1}\right]
$$

Distance between $P_{1}$ and $P_{2}=\left|\overrightarrow{P_{1} P_{2}}\right|$

$$
=\sqrt{\left(x_{2}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(z_{2}-z_{1}\right)^{2}}
$$

This is called distance formula between two points $P_{1}$ and $P_{2}$ in $R^{3}$.
Example 4 Suppose a butterfly's flight path passed through points $(2,4,7)$ and $(6,1,3)$, where each unit represents a metre. What is the magnitude of the displacement the butterfly experienced in traveling between these two points?
Solution Distance between two points in three-dimensional space is given by the formula

$$
d=\sqrt{\left(x_{2}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(z_{2}-z_{1}\right)^{2}}
$$

Substitute the coordinates of the given points into the formula:

$$
\begin{aligned}
& d=\sqrt{(6-2)^{2}+(1-4)^{2}+(3-7)^{2}} \\
& d=\sqrt{16+9+16}=\sqrt{41}=6.40
\end{aligned}
$$

The magnitude of the displacement the butterfly experienced in traveling between these two points is approximately 6.40 metres.

### 14.1.8 Direction Angles and Direction Cosines of a Vector

Let $r=\overrightarrow{O P}=x i+y j+z k$ be a non-zero vector, let $\alpha, \beta$ and $\gamma$ denote the angles formed between $r$ and the unit coordinate vectors $i, j$ and $k$ respectively,
where $0 \leq \alpha \leq \pi, 0 \leq \beta \leq \pi$ and $0 \leq \gamma \leq \pi$
(i) The angles $\alpha, \beta$ and $\gamma$ are called the direction angles of the vector $r$.
(ii) The numbers $\cos \alpha, \cos \beta$ and $\cos \gamma$ are called direction cosines of the vector $r$.

# Important Result:

Prove that $\cos ^{2} \alpha+\cos ^{2} \beta+\cos ^{2} \gamma=1$
Proof: Let

$$
\begin{aligned}
& r=[x, y, z]=x i+y j+z k \\
& \therefore \quad|r|=\sqrt{x^{2}+y^{2}+z^{2}}=r
\end{aligned}
$$

then $\frac{r}{|r|}=\left[\frac{x}{r}, \frac{y}{r}, \frac{z}{r}\right]$ is the unit vector in the direction of the vector $\underline{r}=\overrightarrow{O P}$
It can be visualized that the triangle $O A P$ is a right triangle with $m \angle A=90^{\circ}$.
Therefore, in right triangle $O A P$,

$$
\begin{aligned}
& \cos \alpha=\frac{\overrightarrow{O A}}{O P}=\frac{x}{r}, \text { similarly } \\
& \cos \beta=\frac{y}{r}, \cos \gamma=\frac{z}{r}
\end{aligned}
$$

The numbers $\cos \alpha=\frac{x}{r}, \cos \beta=\frac{y}{r}$ and $\cos \gamma=\frac{z}{r}$ are called the direction cosines of $\overrightarrow{O P}$

$$
\cos ^{2} \alpha+\cos ^{2} \beta+\cos ^{2} \gamma=\frac{x^{2}}{r^{2}}+\frac{y^{2}}{r^{2}}+\frac{z^{2}}{r^{2}}=\frac{x^{2}+y^{2}+z^{2}}{r^{2}}=\frac{r^{2}}{r^{2}}=1
$$

## EXERCISE 14.1

1. Let $\underline{u}=3 \underline{i}+2 \underline{j}-5 \underline{k} \underline{y}=\underline{i}-5 \underline{j}-\underline{k}$ and $w=-4 \underline{i}-\underline{j}+7 \underline{k}$. Find the following:
(i) $\underline{u}+2 \underline{v}+\underline{w}$
(ii) $\underline{v}-3 \underline{w}$
(iii) $|3 \underline{v}+\underline{w}|$.
2. Find the magnitude of the vector $\underline{v}$ and write the direction cosines of $\underline{v}$.
(i) $\underline{v}=3 \underline{i}-2 \underline{j}+6 \underline{k}$
(ii) $\underline{v}=-4 \underline{i}+4 \underline{j}+2 \underline{k}$
(iii) $\underline{v}=-6 \underline{i}+8 \underline{j}$
3. Find $t$, so that $|2 i+(t-1) j+t k|=\sqrt{13}$
4. Find a unit vector in the direction of $\underline{v}=-i+4 \underline{j}-8 \underline{k}$
5. If $\underline{u}=2 \underline{i}+\underline{j}-3 \underline{k}, \underline{v}=-\underline{i}+4 \underline{j}+2 \underline{k}$ and $\underline{w}=3 \underline{i}-2 \underline{j}+\underline{k}$, Find a unit vector parallel to $4 \underline{u}-3 \underline{v}+2 \underline{w}$.
6. Find a vector whose
(i) magnitude is 5 and is parallel to $3 \underline{i}+4 \underline{j}-\underline{k}$
(ii) magnitude is 7 and is parallel to $-\underline{i}+\underline{j}+\underline{k}$.

7. If $u=x i+2 j+3 k, v=i+y j-3 k$ and $w=-2 i-3 j$ represent the sides of a triangle. Find the values of $x$ and $y$.
8. The position vectors of the points $A, B, C$ and $D$ are $u=i+2 j+k, v=7 i+8 j+4 k$, $w=-i+k$ and $z=i+2 j+2 k$ respectively. Show that $\overrightarrow{A B}$ is parallel to $\overrightarrow{C D}$.
9. We say that two vectors $v$ and $w$ in space are parallel if there is a scalar $c$ such that $v=c w$. The vectors point in the same direction if $c>0$ and the vectors point in the opposite direction if $c<0$
(a) Find two vectors of length 2 parallel to the vector $v=2 i-4 j+4 k$.
(b) Find the constant $a$ so that the vectors $v=i-3 j+4 k$ and $w=a i+9 j-12 k$ are parallel.
(c) Find a vector of length 5 in the direction opposite that of $v=i-2 j+3 k$.
(d) Find $a$ and $b$ so that the vectors $3 i-j+4 k$ and $a i+b j-2 k$ are parallel.
10. A spacecraft moves from point $(120,240, \rightarrow 50)$ to point $(130,210,80)$ in kilometres. What is the magnitude of the displacement vector in kilometres?
11. Find the direction cosines for the given vector:
(i) $u=-6 i+3 j+2 k$
(ii) $v=4 i+2 j-5 k$
(iii) $P Q$, where $P(9,3,13)$ and $Q(11,6,19)$.
12. Which of the following triple can be the direction angles of a single vector?
(i) $45^{\circ}, 45^{\circ}, 60^{\circ}$
(ii) $30^{\circ}, 45^{\circ}, 60^{\circ}$
(iii) $45^{\circ}, 60^{\circ}, 60^{\circ}$

Product of Two Vectors: Multiplication of two vectors is an important algebraic operation in vector algebra. This algebraic operation plays a fundamental role for understanding various physical and mathematical real-life situation. Unlike the multiplication of numbers, product of vector can be performed in two distinct ways. The two primary types of vector multiplication are the dot product and the cross product. The dot product is a scalar number while cross product is a vector quantity.

# 14.2 Dot or Scalar Product

14.2.1 Dot or Scalax Product of Two Vectors and Its Geometrical Interpretation We shall now consider products of two vectors that originated in the study of physics and engineering. The concept of angle between two vectors is expressed in terms of a scalar product of two vectors.

Definition 1: Let two non-zero vectors $\underline{u}$ and $\underline{v}$, in the plane or in space, have same initial point. The dot product of $\underline{u}$ and $\underline{v}$, written as $\underline{u} \cdot \underline{v}$, is defined by

$$
\underline{u} \cdot \underline{v}=|\underline{u}||\underline{v}| \cos 0
$$

Where $\theta$ in the angle between $\underline{u}$ and $\underline{v}$ and $0 \leq \theta \leq \pi$

# Definition 2:

(a) If $\underline{u}=a_{1} \underline{i}+\underline{b}_{1} \underline{j}$ and $\underline{v}=a_{2} \underline{i}+\underline{b}_{2} \underline{j}$ are two non-zero vectors in the plane. The dot product $\underline{u} \cdot \underline{v}$ is defined by:

$$
\underline{u} \cdot \underline{v}=a_{1} a_{2}+b_{1} b_{2}
$$

(b) If $\underline{u}=a_{1} \underline{i}+\underline{b}_{1} \underline{j}+\underline{c}_{1} \underline{k}$ and $\underline{v}=a_{2} \underline{i}+\underline{b}_{2} \underline{j}+\underline{c}_{2} \underline{k}$ are two non-zero vectors in space. The dot product $\underline{u} \cdot \underline{v}$ is defined by

$$
\underline{u} \cdot \underline{v}=a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2}
$$

Note The dot product is also referred as the scalar product or the inner product.
Example 5 Prove the equivalence of above two definitions of dot product of two vectors:
(i) If $\underline{v}=\left[x_{1}, y_{1}\right]$ and $\underline{w}=\left[x_{2}, y_{2}\right]$ are two vectors in the plane, then $\underline{v} \underline{w}=x_{1} x_{2}+y_{1} y_{2}$
(ii) If $\underline{v}$ and $\underline{w}$ are two non-zero vectors in the plane, then $\underline{v} \cdot \underline{w}=|\underline{v}||\underline{w}| \cos \theta$, where $\theta$ is the angle between $\underline{v}$ and $\underline{w}$ and $0 \leq \theta \leq \pi$.
Proof: Let $\underline{v}$ and $\underline{w}$ be the sides of a triangle then the third side opposite to the angle $\theta$, has length $|\underline{v}-\underline{w}|$ By law of cosines,

$$
\begin{aligned}
|\underline{v}-\underline{w}|^{2} & =|\underline{v}|^{2}+|\underline{w}|^{2}-2|\underline{v}||\underline{w}| \cos \theta \\
\text { if } \quad \underline{v} & =\left[x_{1}, y_{1}\right] \text { and } \underline{w}=\left[x_{2}, y_{2}\right] \text {, then } \\
\underline{v}-\underline{w} & =\left[x_{1}-x_{2}, y_{1}-y_{2}\right]
\end{aligned}
$$

The law of cosine: $a^{2}=b^{2}+c^{2}-2 b c \cos a$

So, equation (1) becomes:

$$
\begin{aligned}
& \left(x_{1}-x_{2}\right)^{2}+\left(y_{1}-y_{2}\right)^{2}=x_{1}^{2}+y_{1}^{2}+x_{2}^{2}+y_{2}^{2}-2|\underline{v}||\underline{w}| \cos \theta \\
& -2 x_{1} x_{2}-2 y_{1} y_{2}=-2|\underline{v}||\underline{w}| \cos \theta \\
& x_{1} x_{2}+y_{1} y_{2}=|\underline{v}||\underline{w}| \cos \theta=\underline{v} \cdot \underline{w}
\end{aligned}
$$

# 14.2.2 Deduction of the Important Results

By applying the definition of dot product to unit vectors $i, j$ and $k$, we have
(a) $i . i=|i| i \mid \cos 0^{\circ}=1$
$j . j=|j||j \cos 0^{\circ}=1$
$k . k=|k||k \cos 0^{\circ}=1$
(b) $i . j=|i||j \cos 90^{\circ}=0$
$j . k=|j||k \cos 90^{\circ}=0$
$k . i=|k||i \cos 90^{\circ}=0$

### 14.2.3 Projection of a Vector along Another Vector

In many physical applications, it is required to know "how much" of a vector is applied along a given direction. For this purpose, we find the projection of one vector along the other vector.
Let $\overrightarrow{O A}=\underline{u}$ and $\overrightarrow{O B}=\underline{v}$
Let $\theta$ be the angle between them, such that $0 \leq \theta \leq \pi$.
Draw $\overrightarrow{B M} \perp \overrightarrow{O A}$. Then $\overrightarrow{O M}$ is called the projection of $\underline{v}$ along $\underline{u}$.
From the figure: $\frac{\overrightarrow{O M}}{\overrightarrow{O B}}=\cos \theta$, that is,

$$
\overrightarrow{O M}=|\overrightarrow{O B}| \cos \theta=|\underline{v}| \cos \theta
$$

Now, $u \cdot \underline{v}=|\underline{u}||\underline{v}| \cos \theta=|\underline{u}|(|\underline{v}| \cos \theta)=|\underline{u}|(\overrightarrow{O M})$
$=$ (magnitude of $\underline{u}$ ). (projection of $\underline{v}$ along $\underline{u}$ )
Thus, geometrically, the dot product of two vectors represents the product of the magnitude of one vector and the projection of the other vector onto it. In other words, the dot product of two vectors shows how much one vector extends in the direction of another.

Now, by definition, $\quad \cos \theta=\frac{u \cdot v}{|\underline{u}||\underline{v}|}$
From (1) and (2),

$$
\overrightarrow{O M}=|\underline{v}| \cdot \frac{u \cdot \underline{v}}{|\underline{u}||\underline{v}|}=\frac{u \cdot \underline{v}}{|\underline{u}|}
$$

$\therefore \quad$ Projection of $\underline{v}$ along $\underline{u}=\frac{\underline{u} \cdot \underline{v}}{|\underline{u}|}$
Similarly, projection of $\underline{u}$ along $\underline{v}=\frac{\underline{u} \cdot \underline{v}}{|\underline{v}|}$

# 14.2.4 Properties of Dot Product

Let $\underline{u}, \underline{v}$ and $\underline{w}$ be vectors and let $c$ be any real number, then
(i) $\underline{u} \cdot \underline{v}=0 \Rightarrow \underline{u}=0$ or $\underline{v}=0$ or $\underline{u} \perp \underline{v}$
(ii) $\underline{u} \cdot \underline{v}=\underline{v} \cdot \underline{u} \quad$ (Commutative property)
(iii) $\underline{u} \cdot(\underline{v}+\underline{w})=\underline{u} \cdot \underline{v}+\underline{u} \cdot \underline{w} \quad$ (Distributive property)
(iv) $(c \underline{u}) \cdot \underline{v}=c(\underline{u} \cdot \underline{v}) \quad$ (c is scalar)
(v) $\underline{u} \cdot \underline{u}=|\underline{u}|^{2}$

### 14.2.5 Dot Product of Vectors in terms of their components

Let $\underline{u}=a_{1} \underline{i}+b_{1} \underline{j}+c_{1} \underline{k}$ and $\underline{v}=a_{2} \underline{i}+b_{2} \underline{j}+c_{2} \underline{k}$ be two non-zero vectors.
From distributive law we can write:

$$
\begin{aligned}
\therefore \quad \underline{u} \cdot \underline{v}= & \left(a_{1} i+b_{1} \underline{j}+c_{1} \underline{k}\right) \cdot\left(a_{2} i+b_{2} \underline{j}+c_{2} \underline{k}\right) \\
= & a_{1} a_{2}(i \cdot i)+a_{1} b_{2}(i \cdot j)+a_{1} c_{2}(i \cdot k)+b_{1} a_{2}(j \cdot i)+b_{1} b_{2}(j \cdot j)+b_{1} c_{2}(j \cdot k) \\
& +c_{1} a_{2}(k \cdot i)+c_{1} b_{2}(k \cdot j)+c_{1} c_{2}(k \cdot k) \\
\Rightarrow \underline{u} \cdot \underline{v}= & a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2} \quad \because i \cdot i=\underline{j} \cdot \underline{j}=\underline{k} \cdot \underline{k}=1 \\
& i \cdot j=\underline{j} \cdot \underline{k}=\underline{k} \cdot \underline{i}=0
\end{aligned}
$$

Hence the dot product of two vectors is the sum of the product of their corresponding components.
Example 6 Show that the components of a vector are the projections of that vector along $i, j$ and $k$ respectively.
Proof: Let $\underline{v}=a \underline{i}+b \underline{j}+c \underline{k}$, then
Projection of $\underline{v}$ along $\underline{i}=\frac{\underline{v} \cdot \underline{i}}{|\underline{i}|}=(a \underline{i}+b \underline{j}+c \underline{k}) \cdot \underline{i}=a$
Projection of $\underline{v}$ along $\underline{j}=\frac{\underline{v} \cdot \underline{j}}{|\underline{j}|}=(a \underline{i}+b \underline{j}+c \underline{k}) \cdot \underline{j}=b$
Projection of $\underline{v}$ along $\underline{k}=\frac{\underline{v} \cdot \underline{k}}{|\underline{k}|}=(a \underline{i}+b \underline{j}+c \underline{k}) \cdot \underline{k}=c$
Hence components $a, b$ and $c$ of vector $\underline{v}=a \underline{i}+b \underline{j}+c \underline{k}$ are projections of vector $\underline{v}$ along $i, j$ and $k$ respectively.

Example 7 Prove that in any triangle $A B C$
(i) $\quad a^{2}=b^{2}+c^{2}-2 b c \cos A$
(ii) $\quad a=b \cos C+c \cos B$
(Cosine Law)
(Projection Law)
Proof: Let the vectors $\underline{a}, \underline{b}$ and $\underline{c}$ be along the sides $B C, C A$ and $A B$ of the triangle $A B C$ as shown in the figure.
(i) $\underline{a}+\underline{b}+\underline{c}=\underline{0}$
$\Rightarrow \quad \underline{a}=-(\underline{b}+\underline{c})$
Now $\quad \underline{a} \cdot \underline{a}=(\underline{b}+\underline{c}) \cdot(\underline{b}+\underline{c})$
$\Rightarrow \quad=\underline{b} \cdot \underline{b}+\underline{b} \cdot \underline{c}+\underline{c} \cdot \underline{b}+\underline{c} \cdot \underline{c}$
$\Rightarrow \quad a^{2}=b^{2}+2 \underline{b} \cdot \underline{c}+c^{2} \quad(\because \underline{b} \cdot \underline{c}=\underline{c} \cdot \underline{b})$
$\Rightarrow \quad a^{2}=b^{2}+c^{2}+2 b c \cos (\pi-A)$
$\therefore \quad a^{2}=b^{2}+c^{2}-2 b c \cos A$
(ii) $\underline{a}+\underline{b}+\underline{c}=\underline{0}$
$\Rightarrow \quad \underline{a}=-\underline{b}-\underline{c}$
Take dot product with $\underline{a}$

$$
\begin{aligned}
\underline{a} \cdot \underline{a} & =-\underline{a} \cdot \underline{b}-\underline{a} \cdot \underline{c} \\
& =-a b \cos (\pi-C)-a c \cos (\pi-B) \\
& =-a b(-\cos C)-a c(-\cos B) \\
a^{2} & =a b \cos C+a c \cos B \\
\Rightarrow \quad a & =b \cos C+c \cos B
\end{aligned}
$$

Example 8 Prove that: $\cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta$
Proof: Let $\overrightarrow{O A}$ and $\overrightarrow{O B}$ be the unit vectors in the $x y$-plane making angles $\alpha$ and $\beta$ with the positive $x$-axis.
So that $m \angle A O B=\alpha-\beta$
Now $\overrightarrow{O A}=\cos \alpha \underline{i}+\sin \alpha \underline{j}$
and $\overrightarrow{O B}=\cos \beta \underline{i}+\sin \beta \underline{j}$
$\therefore \quad \overrightarrow{O A} \cdot \overrightarrow{O B}=(\cos \alpha \underline{i}+\sin \alpha \underline{j}) \cdot(\cos \beta \underline{i}+\sin \beta \underline{j})$
$\Rightarrow|\overrightarrow{O A}||\overrightarrow{O B}| \cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta$
$\therefore \quad \cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta$
$(\because|\overrightarrow{O A}|=|\overrightarrow{O B}|=1)$

# 14.2.6 Orthogonality of Two Vectors

Definition: Two non-zero vectors $\underline{u}$ and $\underline{v}$ are orthogonal (perpendicular) if and only if $\underline{u} \cdot \underline{v}=0$.
The dot product of two vectors $\underline{u}$ and $\underline{v}$ becomes zero when $\underline{u} \perp \underline{v}, \theta=90^{\circ}$ or $\frac{\pi}{2}$ radius.

$$
\underline{u} \cdot \underline{v}=|\underline{u}| \perp|\underline{v}| \cos 90^{\circ}=0
$$

Note:
The zero vector $\underline{o}$ is orthogonal to every vector because:

$$
\underline{o} \cdot \underline{b}=0 \forall \underline{b}
$$

Thus, $\underline{u} \cdot \underline{v}=0 \Leftrightarrow \underline{u} \perp \underline{v}$
Example 9 If $\underline{u}=3 \underline{i}-j-2 \underline{k}$ and $\underline{v}=i+2 j-\underline{k}$, then find $\underline{u} \cdot \underline{v}$.
Solution $\underline{u} \cdot \underline{v}=(3)(1)+(-1)(2)+(-2)(-1)=3$
Example 10 If $\underline{u}=2 \underline{i}-4 \underline{j}+5 \underline{k}$ and $\underline{v}=4 \underline{i}-3 \underline{j}-4 \underline{k}$, then prove that $\underline{u}$ and $\underline{v}$ are orthogonal.
Solution $\underline{u} \cdot \underline{v}=(2)(4)+(-4)(-3)+(5)(-4)=0$
$\Rightarrow \quad \underline{u}$ and $\underline{v}$ are perpendicular
Example 11 Find a scalar $a$ so that the vectors $2 \underline{i}+\alpha \underline{j}+5 \underline{k}$ and $3 \underline{i}+\underline{j}+\alpha \underline{k}$ are orthogonal.
Solution Let $\underline{u}=2 \underline{i}+\alpha \underline{j}+5 \underline{k}$ and $\underline{v}=3 \underline{i}+\underline{j}+\alpha \underline{k}$
It is given that $\underline{u}$ and $\underline{v}$ are orthogonal

$$
\begin{aligned}
& \therefore \quad \underline{u} \cdot \underline{v} \\
& \Rightarrow \quad(2 \underline{i}+\alpha \underline{j}+5 \underline{k}) \cdot(3 \underline{i}+\underline{j}+\alpha \underline{k})=0 \\
& \Rightarrow \quad 6+\alpha+5 \alpha=0 \\
& \quad \therefore \quad \alpha=-1
\end{aligned}
$$

### 14.2.7 Angle Between Two Vectors

The angle between two vectors $\underline{u}$ and $\underline{v}$ is determined from the definition of dot product, that is
(a) $\underline{u} \cdot \underline{v}=|\underline{u}||\underline{v}| \cos 0, \quad$ where $0 \leq \theta \leq \pi$

$$
\Rightarrow \quad \cos \theta=\frac{\underline{u} \cdot \underline{v}}{|\underline{u}||\underline{v}|}
$$

(b) If $\underline{u}=a_{1} \underline{i}+\underline{b}_{1} \underline{j}+\underline{c}_{1} \underline{k} \quad$ and $\quad \underline{v}=\underline{a}_{2} \underline{i}+\underline{b}_{2} \underline{j}+\underline{c}_{2} \underline{k}$, then

$$
\begin{aligned}
\underline{u} \cdot \underline{v} & =a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2} \\
|\underline{u}| & =\sqrt{a_{1}^{2}+b_{1}^{2}+c_{1}^{2}} \quad \text { and } \quad|\underline{v}|=\sqrt{a_{2}^{2}+b_{2}^{2}+c_{2}^{2}}
\end{aligned}
$$

$$
\begin{aligned}
& \therefore \quad \cos \theta=\frac{u \cdot \psi}{|u||v|} \\
& \therefore \quad \cos \theta=\frac{a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2}}{\sqrt{a_{1}^{2}+b_{1}^{2}+c_{1}^{2}} \sqrt{a_{2}^{2}+b_{2}^{2}+c_{2}^{2}}}
\end{aligned}
$$

Example 12 Find the angle between the vectors.

$$
u=2 i-j+k \quad \text { and } \quad v=-i+j
$$

Solution $u \cdot v=(2 i-j+k) \cdot(-i+j+0 k)$

$$
=(2)(-1)+(-1)(1)+(1)(0)=-3
$$

and

$$
\begin{aligned}
& |u|=|2 i-j+k|=\sqrt{(2)^{2}+(-1)^{2}+(1)^{2}}=\sqrt{6} \\
& |v|=|-i+j+0 k|=\sqrt{(-1)^{2}+(1)^{2}+(0)^{2}}=\sqrt{2}
\end{aligned}
$$

Now $\cos \theta=\frac{u \cdot v}{|u| \cdot|v|}$
$\Rightarrow \quad \cos \theta=\frac{-3}{\sqrt{6} \cdot \sqrt{2}}$

$$
=-\frac{\sqrt{3}}{2}
$$

$$
\therefore \quad 0=\frac{5 \pi}{6}
$$

Example 13 Show that the vectors $\overrightarrow{A B}=2 i-j+k, \overrightarrow{B C}=i-3 j-5 k$ and $\overrightarrow{A C}=3 i-4 j-4 k$ are the sides of a right triangle.
Solution Given $\overrightarrow{A B}=2 i-j+k, \overrightarrow{B C}=i-3 j-5 k$ and

$$
\overrightarrow{A C}=3 i-4 j-4 k
$$

Now

$$
\begin{aligned}
\overrightarrow{A B}+\overrightarrow{B C} & =(2 i-j+k)+(i-3 j-5 k) \\
& =3 i-4 j-4 k=\overrightarrow{A C} \text { (third side) }
\end{aligned}
$$

$\therefore \quad \overrightarrow{A B}, \overrightarrow{B C}$ and $\overrightarrow{A C}$ form a triangle $A B C$.
Further we prove that $\triangle A B C$ is a right triangle

$$
\begin{aligned}
\overrightarrow{A B} \cdot \overrightarrow{B C} & =(2 i-j+k) \cdot(i-3 j-5 k) \\
& =(2)(1)+(-1)(-3)+(1)(-5)=2+3-5=0 \\
\therefore \quad \overrightarrow{A B} \perp \overrightarrow{B C} & \\
& \text { Hence, } \triangle A B C \text { is a right triangle. }
\end{aligned}
$$

# 14.2.8 Work Done By a Constant Force

If a constant force $F$, applied to a body, acts at an angle $\theta$ to the direction of motion, then the work done by $\underline{F}$ is defined to be the product of the component of $\underline{F}$ in the direction of the displacement and the distance that the body moves.
In figure, a constant force $\underline{F}$ acting on a body, displaces it from $A$ to $B$.
$\therefore \quad$ Work done $=($ component of $\underline{F}$ along $A B)$ (displacement)

$$
=(F \cos \theta)(A B)=\underline{F} \cdot \underline{A B}=\underline{F} \cdot \underline{d}
$$

Example 14 The constant forces $2 i+5 j+6 k$ and $-i-2 j-k$ act on a body displaced from position $P(4,-3,-2)$ to $Q(6,1,-3)$. Find the total work done.
Solution
Total force $=(2 i+5 j+6 k)+(-i-2 j-k)$

$$
\Rightarrow \quad \underline{F}=i+3 j+5 k
$$

The displacement of the body $=P \vec{Q}=(6-4) i+(1+3) j+(-3+2) k$

$$
\Rightarrow \quad \underline{d}=2 i+4 j-k
$$

$\therefore \quad$ Work done $=\underline{F} \cdot \underline{d}$

$$
=(i+3 j+5 k) \cdot(2 i+4 j-k)=2+12-5=9 \text { units }
$$

## EXERCISE 14.2

1. Find the coahues of the angle $\theta$ between $\underline{u}$ and $\underline{v}$ :
(i) $\underline{u}=2 i+3 j+k, \underline{v}=-i+2 j+2 k$
(ii) $\underline{u}=[-3,2,5], \underline{v}=[1,6,-2]$
2. If $a+b+c=0$ and $|a|=3,|b|=5$ and $|c|=7$. Find the angle between $a$ and $b$.
3. If $|a|=3,|b|=4$ and $|a+b|=5$. Find the angle between $a$ and $b$.
4. Calculate the projection of $a$ along $b$ and projection of $b$ along $a$ when:
(i) $a=2 i+3 j-k, b=i-2 j+4 k$ (ii) $a=4 i-2 j+3 k, b=i+j+k$
5. Find a real number $a$ so that the vectors $u$ and $v$ are perpendicular:
(i) $\underline{u}=\alpha i+3 j+k, \underline{v}=i-2 j+\alpha k$ (ii) $\underline{u}=\alpha i+2 \alpha j-k, \underline{v}=i+\alpha j+3 k$
6. Find the number $z$ so that the triangle with vertices $A(3,0,-2), B(0,3,1)$ and $C(1,1, z)$ is a right triangle with right angle at $C$.

7. If $\hat{a}$ and $\hat{b}$ are unit vectors and $2 \theta$ is the angle between them, show that $\sin \theta=\frac{1}{2}|\hat{a}-\hat{b}|$.
8. If $|a+b|=|a-b|$, then show that $a$ and $b$ are perpendicular.
9. (i) Show that the vectors $3 i-2 j+k, i-3 j+5 k$ and $2 i+j-4 k$ form a right triangle.
(ii) Show that the set of points $P(4,-1,2), Q(1,3,-1)$ and $R(-2,4,6)$ form a right triangle.
10. Prove that the $\cos (\alpha+\beta)=\cos \alpha \cos \beta-\sin \alpha \sin \beta$
11. Prove that in any triangle $A B C$.
(i) $b=c \cos A+a \cos C$
(ii) $c=a \cos B+b \cos A$
(iii) $b^{2}=c^{2}+a^{2}-2 c a \cos B$
(iv) $c^{2}=a^{2}+b^{2}-2 a b \cos C$
12. Show that for any vectors $a$ and $b,| | a|-|b| \leq|a+b| \leq|a|+|b|$
13. Find the work done, if the point at which the constant force $F=2 i+5 j+3 k$ is applied to an object, moves it from $P_{1}(2,-3,1)$ to $P_{2}(7,5,3)$.
14. A particle, acted by constant forces $F_{1}=3 i+4 j-3 k$ and $F_{2}=i+4 j-k$, is displaced from $A(2,1,3)$ to $B(5,4,4)$. Find the work done.
15. A particle is displaced from the point $A(5,-5,-7)$ to the point $B(6,2,-2)$ under the action of constant forces defined by $10 i-j+11 k, 4 i+5 j+9 k$ and $-2 i+j-9 k$. Show that the total work done by the force is 102 units.
16. A force of magnitude 6 units acting parallel to $4 i+3 j-k$ displace the point of application from $A(2,-1,3)$ to $B(7,3,2)$. Find the work done.

# 14.3 Cross Product or Vector Product

### 14.3.1 The Cross Product or Vector Product of Two Vectors and its Geometrical Interpretation

One of the key multiplication operations involving vectors in space is the cross product. Unlike the dot product, which results is a scalar, the cross product of two vectors yields a vector quantity. The vector product of two vectors is widely used in Physics, particularly in fields of mechanics and electricity. It is only defined for vectors in space. Let $\underline{u}$ and $\underline{v}$ be two non-zero vectors. The cross or vector product of $\underline{u}$ and $\underline{v}$ gives a

vector that is perpendicular to both the vectors $\underline{u}$ and $\underline{v}$, written as $\underline{u} \times \underline{v}$, is defined by

$$
\underline{u} \times \underline{v}=(\|\underline{u}\| \mid \underline{v} \mid \sin \theta) \underline{n}
$$

where $\theta$ is the angle between the vectors, such that $0 \leq \theta \leq \pi$ and $\underline{n}$ is a unit vector perpendicular to the plane of $\underline{u}$ and $\underline{v}$ with direction given by the right-hand rule.
Figure (a)
Right hand
Right hand rule
Figure (b)
(i) If the fingers of the right hand point along the vector $\underline{u}$ and then curl towards the vector $\underline{v}$, then the thumb will give the direction of $\underline{n}$ which is $\underline{u} \times \underline{v}$. It is shown in the figure (a).
(ii) In figure (b), the right hand rule shows the direction of $\underline{v} \times \underline{u}$.

# 14.3.2 Parallel Vectors

If $\underline{u}$ and $\underline{v}$ are parallel vectors, then $(\theta=0 \Rightarrow \sin 0=0)$.

$$
\begin{aligned}
& \underline{u} \times \underline{v}=\|\underline{u}\| \mid \underline{v}\| \sin \theta \underline{n} \\
& \underline{u} \times \underline{v}=0 \quad \text { or } \quad \mid \underline{u} \times \underline{v}=0
\end{aligned}
$$

And if $\underline{u} \times \underline{v}=0$, then either $\sin \theta=0 \quad$ or $\quad\|\underline{u}\|=0 \quad$ or $\quad\|\underline{v}\|=0$
(i) If $\sin \theta=0 \Rightarrow \theta=0^{\circ}$ or $180^{\circ}$. Which shows that the vectors $\underline{u}$ and $\underline{v}$ are parallel.
(ii) If $\underline{u}=\underline{0}$ or $\underline{v}=\underline{0}$, then since the zero vector has no specific direction, we adopt the convention that the zero vector is parallel to every vector.

## Note: Zero vector is both parallel and perpendicular to every vector. This apparent contradiction will cause no trouble, since the angle between two vectors is never applied when one of them is zero vector.

### 14.3.3 Derivation of Useful Results of Cross Products

By applying the definition of cross product to unit vectors $i, j$ and $k$, we have:
(a) $\underline{i} \times \underline{i}=\|\underline{i}\| \mid i\left\|\sin 0^{\circ} \underline{n}=\underline{0}\right.$
$\underline{j} \times \underline{j}=\|\underline{j}\| \mid \underline{j}\| \sin 0^{\circ} \underline{n}=\underline{0}$
$\underline{k} \times \underline{k}=\|\underline{k}\| \mid \underline{k}\left\|\sin 0^{\circ} \underline{n}=\underline{0}\right.$
(b) $\quad \underline{i} \times \underline{j}=|\underline{i}||\underline{j}| \sin 90^{\circ} \underline{k}=\underline{k}$

$$
\begin{aligned}
& \underline{j} \times \underline{k}=|\underline{j}||\underline{k}| \sin 90^{\circ} \underline{i}=\underline{i} \\
& \underline{k} \times \underline{i}=|\underline{k}||\underline{i}| \sin 90^{\circ} \underline{j}=\underline{j}
\end{aligned}
$$

(c) $\quad \underline{u} \times \underline{u}=|\underline{u}||\underline{u}| \sin 0 \underline{n}=\underline{0}$

# 14.3.4 Properties of Cross Product

The cross product possesses the following properties:
(i) $\underline{u} \times \underline{v}=\underline{0}$ if $\underline{u}=\underline{0}$ or $\underline{v}=\underline{0}$
(ii) $\underline{u} \times \underline{v}=-\underline{v} \times \underline{u}$
(iii) $\underline{u} \times(\underline{v}+\underline{w})=\underline{u} \times \underline{v}+\underline{u} \times \underline{w}$
(iv) $\underline{u} \times(\underline{k} \underline{v})=(\underline{k} \underline{u}) \times \underline{v}=\underline{k}(\underline{u} \times \underline{v})$
(v) $\underline{u} \times \underline{u}=\underline{0}$

The proofs of these properties are left as an exercise for the students.

### 14.3.5 Analytical Expressions of $\underline{u} \times \underline{v}$ (Determinant formula for $\underline{u} \times \underline{v}$ )

Let $\underline{u}=a_{1} \underline{i}+\underline{b}_{1} \underline{j}+\underline{c}_{1} \underline{k}$ and $\underline{v}=a_{2} \underline{i}+\underline{b}_{2} \underline{j}+\underline{c}_{2} \underline{k}$, then

$$
\begin{aligned}
\underline{u} \times \underline{v}= & \left(a_{1} \underline{i}+\underline{b}_{1} \underline{j}+\underline{c}_{1} \underline{k}\right) \times\left(a_{2} \underline{i}+\underline{b}_{2} \underline{j}+\underline{c}_{2} \underline{k}\right) \\
= & a_{1} a_{2}(\underline{i} \times \underline{i})+a_{1} \underline{b}_{2}(\underline{i} \times \underline{j})+a_{1} \underline{c}_{2}(\underline{i} \times \underline{k}) \\
& +\underline{b}_{1} a_{2}(\underline{j} \times \underline{i})+\underline{b}_{1} \underline{b}_{2}(\underline{j} \times \underline{j})+\underline{b}_{1} \underline{c}_{2}(\underline{j} \times \underline{k}) \\
& +\underline{c}_{1} \underline{a}_{2}(\underline{k} \times \underline{i})+\underline{c}_{1} \underline{b}_{2}(\underline{k} \times \underline{j})+\underline{c}_{1} \underline{c}_{2}(\underline{k} \times \underline{k}) \\
& =a_{1} \underline{b}_{2} \underline{k}-a_{1} \underline{c}_{2} \underline{j}-\underline{b}_{1} \underline{a}_{2} \underline{k}+\underline{b}_{1} \underline{c}_{2} \underline{i}+\underline{c}_{1} \underline{a}_{2} \underline{j}-\underline{c}_{1} \underline{b}_{2} \underline{i} \\
\Rightarrow \quad & \underline{u} \times \underline{v}=\left(\underline{b}_{1} \underline{c}_{2}-\underline{c}_{1} \underline{b}_{2}\right) \underline{i}-\left(\underline{a}_{1} \underline{c}_{2}-\underline{c}_{1} \underline{a}_{2}\right) \underline{j}+\left(\underline{a}_{1} \underline{b}_{2}-\underline{b}_{1} \underline{a}_{2}\right) \underline{k}
\end{aligned}
$$

The expression of $3 \times 3$ determinant

$$
=\left|\begin{array}{ccc}
\underline{i} & \underline{i} & \underline{k} \\
a_{1} & \underline{b}_{1} & \underline{c}_{1} \\
a_{2} & \underline{b}_{2} & \underline{c}_{2}
\end{array}\right|=\left(\underline{b}_{1} \underline{c}_{2}-\underline{c}_{1} \underline{b}_{2}\right) \underline{i}-\left(\underline{a}_{1} \underline{c}_{2}-\underline{c}_{1} \underline{a}_{2}\right) \underline{j}+\left(\underline{a}_{1} \underline{b}_{2}-\underline{b}_{1} \underline{a}_{2}\right) \underline{k}
$$

The terms on R.H.S of equation (i) are the same as the terms in the expansion of the above determinant.

$$
\text { Hence } \underline{u} \times \underline{v}=\left|\begin{array}{ccc}
\underline{i} & \underline{j} & \underline{k} \\
a_{1} & \underline{b}_{1} & \underline{c}_{1} \\
a_{2} & \underline{b}_{2} & \underline{c}_{2}
\end{array}\right|
$$

which is known as determinant formula for $\underline{u} \times \underline{v}$.

# Unit 44 Vectors in Space

Note The expression on R.H.S. of equation (ii) is not an actual determinant, since its entries are not all scalars. It is simply a way of remembering the complicated expression on R.H.S of equation (i).

Example 15 Find a vector perpendicular to each of the vectors. Also verify that $\underline{a}$ and $\underline{b}$ are $\perp$ to $\underline{a} \times \underline{b}$

$$
\underline{a}=2 \underline{i}-\underline{j}+\underline{k} \quad \text { and } \quad \underline{b}=4 \underline{i}+2 \underline{j}-\underline{k}
$$

Solution A vector perpendicular to both the vectors $\underline{a}$ and $\underline{b}$ is $\underline{a} \times \underline{b}$.

$$
\therefore \quad \underline{a} \times \underline{b}=\left|\begin{array}{ccc}
\underline{i} & \underline{j} & \underline{k} \\
2 & -1 & 1 \\
4 & 2 & -1
\end{array}\right|=-i+6 j+8 k
$$

Verification:

$$
\begin{gathered}
\underline{a} \cdot \underline{a} \times \underline{b}=(2 \underline{i}-\underline{j}+\underline{k}) \cdot(-i+6 \underline{j}+8 \underline{k})=(2)(-1)+(-1)(6)+(1)(8)=0 \\
\text { and } \quad \underline{b} \cdot \underline{a} \times \underline{b}=(4 \underline{i}+2 \underline{j}-\underline{k}) \cdot(-i+6 \underline{j}+8 \underline{k})=(4)(-1)+(2)(6)+(-1)(8)=0
\end{gathered}
$$

Hence $\underline{a} \times \underline{b}$ is perpendicular to both the vectors $\underline{a}$ and $\underline{b}$.

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

### 14.4.1 The Volume of the Parallelepiped

The triple scalar product $(\underline{u} \times \underline{v}) \cdot \underline{w}$ represents the volume of the parallelepiped having $\underline{u}, \underline{v}$ and $\underline{w}$ as its conterminous edges.
As it is seen from the formula that:

Hence, (i) $\backslash[\underline{u} \times \underline{v}]:=\operatorname{area}$ of the parallelogram with two adjacent sides $\underline{u}$ and $\underline{v}$.
(ii) $|\underline{w}| \cos \theta=$ height of the parallelepiped
$(\underline{u} \times \underline{v}) \cdot \underline{w}=|\underline{u} \times \underline{v}||\underline{w}| \cos \theta=$ (Area of Parallelogram) (height)
$=$ Volume of the parallelepiped
Similarly, be taking the base plane formed by $\underline{v}$ and $\underline{w}$, we have
The volume of the parallelepiped $=(\underline{v} \times \underline{w}) \cdot \underline{u}$
And by taking the base plane formed by $\underline{w}$ and $\underline{u}$, we have
The volume of the parallelepiped $=(\underline{w} \times \underline{u}) \cdot \underline{v}$
So, we have: $(\underline{u} \times \underline{v}) \cdot \underline{w}=(\underline{v} \times \underline{w}) \cdot \underline{u}=(\underline{w} \times \underline{u}) \cdot \underline{v}$

# 14.4.2 The Volume of the Tetrahedron

Volume of the tetrahedron $A B C D=\frac{1}{3}$ (area of $A A B C$ )(height of $D$ above the place $A B C$ )

$$
=\frac{1}{3} \times \frac{1}{2}|\underline{u} \times \underline{v}|(h)
$$

$=\frac{1}{6}$ (Area of parallelogram with $A B$ and $A C$ as adjacent sides) ( $h$ )
$=\frac{1}{3}$ (Volume of the parallelepiped with $\underline{u}, \underline{v}, \underline{w}$ as edges)
## Nota

As volume is always positive so ignore negative sign if $(u \times v) \cdot w$ is negative.

Thus, volume of tetrahedron $=\frac{1}{6}(\underline{u} \times \underline{v}) \cdot \underline{w}=\frac{1}{6}[\underline{u} \underline{v} \underline{w}]$

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

### (vi) 1, 25, 5929

### (vii) 4, 16, 36

### (viii) -7, 28, -63

### (vii) -7, 28, -63

### (viii) 3, 120

### (vii) $a_1 r^{n-1}$

### (viii) $\frac{n a_2}{b_1 + c_2}$

### (viii) $\frac{1}{a_1 + (n-1) d}$

## EXERCISE 6.2

1. (i) $d = 7; 30,37$
   (ii) $d = \sqrt{2}; 5 + 3\sqrt{2}, 5 + 4\sqrt{2}$
   2. (i) 2, 15, 28
   (ii) 12, -1, -14

2. $3n + 7, 4 + 6n$

4. (i) 94
   (ii) -47

5. 75

6. No

7. 5

8. 25

9. 62

10. 7, 12, 17, ... ; 502

12. 128

13. 164

14. $\left(\frac{7n-4}{7}\right)^{10}$; No

15. 13

16. 3 : 4 : 5

## EXERCISE 6.3

1. (i) 2
   (ii) $a^2 + b^2$
2. 1, 21
3. $\frac{25}{6\sqrt{2}}, \frac{19}{3\sqrt{2}}, \frac{17}{2\sqrt{2}}, \frac{32}{3\sqrt{2}}, \frac{77}{6\sqrt{2}}$
4. 5, 9 or 9,5

7. 0

## EXERCISE 6.4

1. (i) 630
   (ii) $\frac{n(n+7)}{2\sqrt{5}}$
2. (i) 1300
   (ii) 230
   (iii) 1932

3. 22

4. 14, 51

5. $9cm, 12cm, 15cm$

6. (i) $n(3n-2)$
   (ii) $\frac{n}{2}(9n-13)$

7. 650

8. 385

9. 200000

10. $3 + 7 + 11+$

11. 73

12. 5, 8, 11 or 11, 8, 5

13. 32

14. 5, 7, 9, 11 or 11, 9, 7, 5

15. 3, 4, 5, 6, 7 or 7, 6, 5, 4, 3

17. 11

## EXERCISE 6.5

1. $\frac{-3}{16}$
2. 6561
3. 5
4. (i) 243, 81, 27, 9, 3
   (ii) $579, \frac{-579}{2}, \frac{579}{4}, \frac{-579}{8}, \frac{579}{16}$
5. -64
6. 2, 6, 18, ...; $2 \cdot 3^{n-1}$
7. $\sqrt{mn}$
8. 2, 6, 18 or 18,6, 2
9. 81 · $\sqrt[4]{9}$
10. 2, 7, 12 or 10, 7, 4
11. 1, 2, 3 or 17, 2, -13
12. $\frac{-81}{4}$

## EXERCISE 6.6

1. (i) $4l$ or $-4l$
   (ii) 4 or -4
   (iii) $3\sqrt{6}$ or $-3\sqrt{6}$
2. 6, 12, 24, 48
3. $\frac{1}{2}$
4. 4, 16 or 16,4
5. 2,8 or 8, 2

## EXERCISE 6.7

1. $\frac{7174453}{4782969}$
2. 4, 172
3. (i) $\frac{2}{9} \left[ n-\frac{1}{9} \left( 1-\frac{1}{10^n} \right) \right]$
   (ii) $\frac{1}{3} \left[ \frac{10}{9} \left( 10^n-1 \right)-n \right]$
4. (i) $\frac{a(1-b)(1-a^*)-b(1-a)(1-b^*)}{(a-b)(1-a)(1-b)}$
   (ii) $\frac{r}{1-k} \left( \frac{1-r^2}{1-r} - \frac{k(1-k^*_{r} )}{1-kr} \right)$
5. $\frac{15(1-t)}{8}$

# EXERCISE 6.8

1. 14080
2. $2(4 n-1) 3^{n-1}$
3. $(2 n+3)(-3)^{n} ;-195$
4. (i) $6+(4 n-6) 2^{n}$
(ii) $\frac{3}{2}\left[1-(n+1) 3^{n}+n \cdot 3^{n+1}\right]$
(iii) $4-\frac{4 / 1}{3 \backslash 4} \cdot \frac{4}{3}(3 n-1) \cdot \frac{1}{4}$
(iv) $\frac{15}{8}-\frac{5}{4}(2 n-1) \cdot\left(\frac{1}{5}\right)^{n}-\frac{5 / 1}{8 \backslash 5} \cdot \frac{1}{5}$
(v) $\frac{15}{4}-\frac{3}{2}(3 n-2) \cdot\left(\frac{1}{3}\right)^{n}-\frac{9 / 1}{4 \backslash 3} \cdot \frac{1}{4}$
5. (i) 6
(ii) $\frac{21}{4}$
6. $\frac{2-(n+1) x^{n}+2 n x^{n+1}}{(1-x)^{2}}$
7. $n(2 n+1)$
8. $\frac{2}{1-x}+\frac{3 x\left(1-x^{n-1}\right)}{(1-x)^{2}}-\frac{(3 n-1) x^{n}}{1-x} \cdot \frac{2+x}{(1-x)^{2}}$

## EXERCISE 6.9

1. (i) $\frac{1}{19}$
(ii) $\frac{1}{11}$
2. (i) $-1,2, \frac{1}{2}, \frac{2}{7}, \frac{1}{5}$
(ii) $\frac{3}{22}, \frac{3}{32}, \frac{1}{14}, \frac{3}{52}, \frac{3}{62}$
3. $\frac{1}{13}$
4. -10
5. 67
6. -1
7. 3,6 or 6,3
8. 2,8 or 8,2
9. 19

## EXERCISE 6.10

1. (i) $\frac{n(n+1)(4 n+5)}{6}$
(ii) $\frac{n(n+1)(2 n+3)}{2}$
(iii) $n^{2}(n+1)$
(iv) $\frac{n(n+1)(n+4)(n+5)}{4}$
(v) $\frac{n(n+1)(n+2)(9 n+7)}{12}$
(vi) $\frac{2 n(n+1)(2 n+1)}{3}$
(vii) $\frac{n(n+1)\left(9 n^{2}+13 n+2\right)}{12}$
(ix) $\frac{n(n+1)(4 n+5)}{6}$
(x) $\frac{n(n+1)^{2}(n+2)}{12}$
2. (i) $-n(2 n+1)$
(ii) $\frac{n\left(4 n^{2}+15 n+17\right)}{36}$
3. (i) $n\left(n^{2}+4 n+5\right)$
(ii) $\frac{n\left(2 n^{2}+9 n-11\right)}{6}$
4. (i) $2 n\left(4 n^{2}+8 n+5\right)$
(ii) $\frac{4 n\left(2 n^{2}+3 n-2\right)}{3}$

## EXERCISE 6.11

1. Rs. 65 2. Rs. 239077.50 3. $5 \%$ 4. Rs. 173596 5. (a) 900 litres, (b) 200 weeks,
(c) 400 weeks 6. (a) 23.8 million
(b) $7+1.4 n$
(c) 21
7. (a) $100,80,64,51.2, \ldots$
(b) 482.4.(c) 500 8. Yes, Rs. 8000
9. Rs. 9468.22
10. 17 hours
11. 25 days
12. 1088
13. 7.2 seconds
14. 410.4 mA

## EXERCISE 7.1

1. (i) 90
(ii) 220
(iii) 20
(iv) $n+2$
2. (i) $\frac{(n+1)!}{(n-2)!}$
(ii) $\frac{n!}{(n-r)!}$
3. 5
4. 81
5. $\frac{(n+1)!(n+r+4)}{(r+2)!}$
6. 9

## EXERCISE 7.2

1. (i) 30240
(ii) 20
(iii) 5040
(iv) 720
2. (i) 9
(ii) 5 (iii) 10
3. (i) 720
(ii) 5040
(iii) 40320
4. 30
5. 325
6. 120
7. 100,36
8. 408
9. (i) 48
(ii) 72
10. 600,120
11. 24
12. 30240
13. 1440
14. 2880

# EXERCISE 7.3

1. (i) 20160
(ii) 151200
(iii) 9979200
2. 10
3. 907200
4. 1260
5. (a) 5040
(b) 720
(c) 120
6. 2880
7. 90
8. 12612600
9. 725760
10. 131
11. 967680
12. 2880
13. 60
14. 60

## EXERCISE 7.4

1. (i) 1
(ii) 1
(iii) 120
(iv) 1140
2. (i) 2
(ii) 3
3. (i) 8,3
(ii) 6,2
6. 56
7. 120
8. 560
9. 171028000
10. (i) 1176
(ii) 280 (iii) 490 (iv) 56
11. 90,455
12. 16
13. 435
14. 11760
15. 56
16. 12376,8008
17. (i) 840
(ii) 1016
(iii) 1016
18. 108
19. (a) 94058496
(b) 4838400
20. (i) 518400
(ii) 14400

## EXERCISE 8.2

1. (i) $\frac{x^{4}}{64} \frac{3}{8} x^{3} \quad \frac{15}{4} \quad \frac{20}{x^{2}} \left\lvert\, \frac{60}{x^{6}} \frac{96}{x^{5}} \right.$
(ii) $128 a^{7} \quad 448 a^{5} x \quad 672 a^{3} x^{2} \quad 560 a x^{3} \quad 280 \frac{x^{4}}{a} \quad 84 \frac{x^{2}}{a^{2}} \quad 14 \frac{x^{6}}{a^{3}} \frac{x^{7}}{a^{7}}$
(iii) $\frac{a^{3}}{x^{3}} \quad \frac{6 a^{3}}{x^{2}} \left\lvert\, \frac{15 a}{x} \quad 20 \left\lvert\, \frac{15 x}{a} \frac{6 x^{2}}{a^{2}} \right.$
(ii) 0.91267
(iii) 16.64966416
(iii) 9920.23968016
(iv) 40.84101
2. (i) $2 a^{4}+24 a^{2} x^{2}+8 x^{4}$
(ii) 724
3. (i) $16+32 x-8 x^{2}-40 x^{3}+x^{4}+20 x^{2}+2 x^{6}-4 x^{7}+x^{8}$
(ii) $1-4 x+10 x^{2}-16 x^{3}+19 x^{4}-16 x^{3}+10 x^{6}-4 x^{7}+x^{8}$
(iii) $4032 \frac{a^{4}}{x^{2}}$
(iv) $462 x^{2} y^{3}$
4. (i) $\frac{15309}{8}$
(ii) $\frac{(-1)^{n}(2 n)!}{(n!)^{2}}$
5. $\frac{15309}{8} x^{3}$
6. (i) -8064
(ii) $\frac{45}{4}$
(iii) 35
(iv) $\frac{221}{16} x^{6}$
(iii) $\frac{-692}{32} x$ and $\frac{77}{16 x}$
(iii) $2(-1)^{m} \frac{(2 m+1)!}{m!(m+1)!} x$ and $\frac{2}{3}(-1)^{m+1} \frac{(2 m+1)!}{m!(m+1)!} \frac{1}{x}$

## EXERCISE 8.3

1. (i) $1-\frac{1}{3} x+\frac{2}{9} x^{4}-\frac{14}{81} x^{2}+\cdots$ is valid if $|x|<1$
(ii) $2-\frac{3 x}{4} \frac{9 x^{3}}{64} \frac{27 x^{7}}{512}-\cdots$ is valid if $|x|<\frac{4}{3}$
(iii) $1-x+2 x^{2}-2 x^{3}+\ldots$ is valid if $|x|<1$
(iii) $1-x+2 x^{2}-2 x^{3}+\cdots$ is valid if $|x|<1$
(iv) $1+2 x+\frac{3}{2} x^{2}+2 x^{3}+\cdots$ is valid if $|x|<\frac{1}{2}$
2. (i) $(-1)^{n} \times 2 n$
(ii) $4 n$
3. $\frac{2}{\sqrt{5}}$

## EXERCISE 8.4

1. (i) 9.950
(ii) 1.010
(iii) 0.331
(iv) 0.935
2. Remainder $=1$
3. Remainder $=1$
4. (i) $21^{10}>19^{10}+20^{10}$
(ii) $31^{15}>29^{15}+30^{15}$
5. Remainder $=3$
6. 6
7. Rs. $12,616,000$
8. Rs. $2,928,200$
9. 28 matches

## EXERCISE 9.1

1. (i) Quotient $=3 x+2$, Remainder $=4$ (ii) Quotient $=x^{2}+14 x+25$, Remainder $=54$

(iii) Quotient $=x^{3}+x^{2}-2 x+1$, Remainder $=18$ (iv) Quotient $=5 x^{2}-3 x-18$, Remainder $=12 x+71$ (v) Quotient $=3 x^{2}+4 x-3$, Remainder $=-25 x+9$
(ii) 10 (iii) 5 (iv) 91 (v) 10
(ii) $x-2$ is a factor of $x^{2}-5 x+6$
(iv) $x-2$ is a factor of $x^{3}+x^{2}-7 x+2$
(iv) $x-2$ is a factor of $x^{3}+x^{2}-7 x+2$
(v) $x-3$ is not a factor of $x^{4}-3 x^{2}+x^{2}-x+1$
4. (i) $(x-2)(x-1)(x+3)$
(ii) $(x+4)(x-6)(x+2)$
(iii) $(x-2)(x+3)(x+1)(2 x+3)$
5. Quotient $=x^{2}-3 x^{2}-x+1$, Remainder $=1$ 6. $p=2, q=-1$
6. $p \frac{-5}{2}, q \quad \frac{-1}{2}$ 10. $a=-8, b=-16$

# EXERCISE 9.2

1. $26.25 \%$
2. 20 units, 2 units
3. $x=2,-1$
4. $x=-2,-1$
5. $x=-0.5,1$
6. $x=-0.5,0.8$, the system is stable.
7. $x=-0.5,-0.7$, the system is stable.

## EXERCISE 10.1

1. (i) $-\frac{\sqrt{3}}{2}$
(ii) 1
(iii) 2
(iv) 2
(v) $\frac{1}{\sqrt{3}}$
(vi) $\frac{-1}{2}$
2. (i) $-\cos 12^{\circ}$
(ii) $-\sin 12^{\circ}$
(iii) $\cos 27^{\circ}$ (iv) $\tan 33^{\circ}$ (v) $\sin 15^{\circ}$ (vi) $-\sin 39^{\circ}$ (vii) $-\cot 33^{\circ}$
(viii) $-\sin 21^{\circ}(\mathrm{ix})-\sin 30^{\circ}$

## EXERCISE 10.2

1. (i) $\frac{\sqrt{3}-1}{2 \sqrt{2}}$
(ii) $\frac{\sqrt{3}+1}{2 \sqrt{2}}$
(iii) $2-\sqrt{3}$
(iv) $\frac{\sqrt{3}+1}{2 \sqrt{2}}$
(v) $\frac{1-\sqrt{3}}{2 \sqrt{2}}$
(vi) $-2-\sqrt{3}$
2. (i) $-\frac{13}{85}$
(ii) $-\frac{84}{85}$
(iii) $\frac{13}{84}$
(iv) $\frac{77}{85}$
(v) $-\frac{36}{85}$
(vi) $-\frac{77}{36}$

The terminal arms of angles of measure and $\alpha+\beta$ and $\alpha-\beta$ are in III and II quadrants respectively.
10. (i) $\frac{33}{65},-\frac{56}{65}$
(ii) $-\frac{304}{425}, \frac{297}{425}$
15. (i) $25 \sin (\theta+\phi), \tan \phi=\frac{7}{24}$
(ii) $13 \sin (\theta-\varphi)$,
$\tan \varphi=\frac{5}{12}$
(iii) $\sqrt{2} \sin (\theta-\phi), \tan \phi=1$
(iv) $10 \sin (\theta-\varphi), \tan \varphi=\frac{3}{4}$
(v) $1 \sin (\theta+\varphi), \tan \varphi=\sqrt{3}$
(vi) $85 \sin (0-\phi), \tan \phi=\frac{84}{13}$

## EXERCISE 10.3

1. (i) $\sin 2 \alpha=\frac{24}{25}, \cos 2 \alpha=\frac{7}{25}, \tan 2 \alpha=\frac{24}{7}$
(ii) $\sin 2 \alpha=\frac{24}{25}, \cos 2 \alpha=\frac{7}{25}, \tan 2 \alpha=\frac{24}{7}$
2. $\sin ^{4} \theta=\frac{3-4 \cos 2 \theta+\cos 4 \theta}{8}$
3. (i) $\sin 18^{\circ}=\frac{\sqrt{5}-1}{4}, \cos 18^{\circ}=\frac{\sqrt{10+2 \sqrt{5}}}{4}$
(ii) $\sin 36^{\circ}=\frac{\sqrt{10-2 \sqrt{5}}}{4}, \cos 36^{\circ}=\frac{\sqrt{5}+1}{4}$
(iii) $\sin 54^{\circ}=\frac{\sqrt{5}+1}{4}, \cos 54^{\circ}=\frac{\sqrt{10-2 \sqrt{5}}}{4}$

# Answers <br> (iv) $\sin 72^{\circ}=\frac{\sqrt{10+2 \sqrt{5}}}{4}, \cos 72^{\circ}=\frac{\sqrt{5}-1}{4}$

## EXERCISE 10.4

1. (i) $\sin 4 \theta+\sin 2 \theta$
(ii) $\sin 8 \theta-\sin 2 \theta$
(iii) $\frac{1}{2}(\sin 7 \theta+\sin 3 \theta)$
(iv) $\cos 5 \theta-\cos 9 \theta$
(v) $\frac{1}{2}(\sin 2 x-\sin 2 y)$
(vi) $\frac{1}{2}\left(\cos 4 x+\cos 60^{\circ}\right)$
(vii) $\frac{1}{2}\left(\cos 34^{\circ}-\cos 58^{\circ}\right)$
(viii) $\frac{1}{2}\left(\cos 90^{\circ}-\cos 2 x\right)$
2. (i) $2 \sin 4 \theta \cos \theta$
(ii) $2 \cos 6 \theta \sin 2 \theta$
(iii) $2 \cos \frac{9 \theta}{2} \cos \frac{3 \theta}{2}$
(iv) $-2 \sin 4 \theta \sin 3 \theta$
(v) $2 \cos 30^{\circ} \cos 18^{\circ}$ (vi) $2 \sin x \cos 30^{\circ}$

## EXERCISE 11.1

1. (i) even
(ii) neither even nor odd
(iii) even
(iv) neither even nor odd
(v) odd
(vi) odd
(vii) even
(viii) even
2. (i) $\frac{2 \pi}{5}$
(ii) $\frac{2 \pi}{7}$
(iii) $\frac{\pi}{3}$
(iv) $2 \pi$
(v) 40
(vi) $5 \pi$
(vii) $\frac{4 \pi}{3}$ (viii) $\frac{2}{7}$
(ix) 30
(x) $\frac{4 \pi}{7}$ (xi) $30 \pi$

## EXERCISE 11.2

1. (i)
$$
y=\sin \frac{x}{2} x
$$

# EXERCISE 11.3

1. (i) $\mathrm{Max}=4, \mathrm{Min}=2$
(ii) $\mathrm{Max}=4, \mathrm{Min}=2$
(iii) $\mathrm{Max}=\frac{3}{2}, \mathrm{Min}=\frac{-1}{2}$
(iv) $\mathrm{Max}=\frac{5}{2}, \mathrm{Min}=\frac{1}{2}$
(v) $\mathrm{Max}=4, \mathrm{Min}=-2$ (vi) $\mathrm{Max}=3, \mathrm{Min}=-1$ (vii) $\mathrm{Max}=\frac{1}{8}, \mathrm{Min}=\frac{1}{12}$ (viii) $\mathrm{Max}=\frac{1}{4}, \mathrm{Min}=\frac{1}{10}$
(ix) $\mathrm{Max}=\frac{1}{2}, \mathrm{Min}=\frac{1}{8}$
2. (a) Max. temperature $=21.5^{\circ} \mathrm{C}, \mathrm{Min}$ : temperature $=8.5^{\circ} \mathrm{C}$
(b) Temperature at $9 \mathrm{a} . \mathrm{m} .=8.89^{\circ} \mathrm{C} \quad$ 3. distance $=36.78 \mathrm{~m}$ 4. height $=30.92 \mathrm{~m}$
3. (a) $h(t)=-30 \cos \left(\frac{\pi}{40} t\right)-36$ (b) 66 feet (c) 63.72 feet
4. (a) 2.7 m (b) 0.3 m
(c) $\frac{2}{3}$ second
(d) 0.05 second
5. (a) $h(t)=28-20 \cos \left(\frac{\pi}{60} t\right)$
(b) 28 feet
(c) 37.87 s and 82.13 s
6. (a) $66.07^{\circ} \mathrm{F}$
(b) 14 hr or 2 p.m.
(c) $72^{\circ} \mathrm{F}$
7. (a) 65000
(b) 80000

## EXERCISE 12.1

1. (i) 2
(ii) 0
(iii) divergent
(iv) $\frac{1}{2}$
2. (i) 10
(ii) 5
(iii) 4
(iv) 0
(v) 0
(vi) $\frac{13}{4}$
3. (i) 2
(ii) $\frac{1}{4}$
(iii) -12 (iv) 0
(v) 0
(vi) -4
(vii) 2
(viii) $\frac{1}{2 \sqrt{x}}$
(ix) $\frac{\pi}{m} a^{n \rightarrow 4}$
4. (i) 5
(ii) $\frac{\pi}{180}$
(iii) 0
(iv) $\sqrt{2}$ (v) $\frac{b^{2}-a^{2}}{2}$
(vi) 2
(vii) 2
(viii) $\frac{a^{2}-b^{2}}{c^{2}-d^{2}}$
(ix) $\frac{3}{2}$
(x) $6-\log 3$
(xi) $2 \log 2$
5. (i) $e^{2}$
(ii) $\sqrt{e}$
(iii) $\frac{1}{e}$
(iv) $e^{\frac{1}{2}}$
(v) $e^{4}$
(vi) $e^{8}$
(vii) $e^{5}$
(viii) $\frac{a-b}{a b}$
(ix) $\frac{1}{e}$
(x) -1
(xi) 1
(xii) $e^{2}$

## EXERCISE 12.2

1. (i) -2 (ii) 0 (iii) 0
2. (i) $f$ is continuous at $x=2$ (ii) $f$ is discontinuous at $x=1$

3. (i) $f$ is continuous at $x=2$ (ii) $f$ is discontinuous at $x=-2$ 4. $c=-1$
4. (i) $m=1, n=3$ (ii) $m=4$
5. $k=\frac{1}{6}$
6. $f(x)$ is discontinuous at $x=1$.

# EXERCISE 12.3

1. 0
2. 100,000
3. 500
4. (i) 10
(ii) 0
5. (i) $\infty$
(ii) 82.44
5. yes
6. (i) $16.18 \%$
(ii) 134.99
7. yes

## EXERCISE 13.1

1. (i) $4 x$ (ii) $\frac{-1}{2 \sqrt{x}}$ (iii) $-\frac{1}{2} x^{-3 / 2}$ (iv) $2 x-3$
2. (i) $\frac{1}{4 \sqrt{2}}$ (ii) $-\frac{1}{4 \sqrt{2} a^{3 / 2}}$
3. (i) $\frac{1}{3}$ (ii) $2 x+2$
4. (i) $\frac{-6}{(3 x-2)^{3}}$ (ii) $10(2 t+3)^{4}$ (iii) $7 a(a w+b)^{4}$
5. $8, y=8 x+13$
6. $y=7 x+4$
7. $(1,0), y=x-1$
8. 8
9. $\frac{1}{6}, 6 y=x+9$
10. (i) $28 \mathrm{~km} / \mathrm{h}$
(ii) $13 \mathrm{~km} / \mathrm{h}$
11. 0
12. $8^{x} \mathrm{c} / \mathrm{hr}$
13. (i) not differentiable
(ii) not differentiable

## EXERCISE 13.2

1. (i) $4 x^{3}+6 x^{2}+2 x$
(ii) $-3\left(\frac{1}{x^{2}}+\frac{1}{x^{3 / 2}}\right)$
(iii) $\frac{8}{(2 x+1)^{2}}$
(iv) $\frac{1-3 x}{2 \sqrt{x}}$
(v) $1-2 x^{-3}+x^{-6 / 2}$
(vi) $8-2 x$
(vii) $\frac{2 x\left(x^{2}+1\right)\left(x^{2}-3\right)}{\left(x^{2}-1\right)^{2}}$
(vii) $\frac{-8 x}{\left(x^{2}-3\right)^{2}}$
(ix) $\frac{x+2}{\left(x^{2}+1\right)^{3 / 2}}$
(x) $\frac{-a}{\sqrt{a-x(a+x)^{3 / 2}}}$
(xi) $\frac{-2 x}{\sqrt{x^{2}+1}\left(x^{2}-1\right)^{3 / 2}}$
2. $\frac{3 x^{2}-2 x^{3 / 2}-3 x+2}{2 \sqrt{x}(\sqrt{x}-1)^{2}}$
3. $\frac{x^{3}-3 x^{2}+3 x-1}{2 \sqrt{x}\left(x^{3 / 2}-x^{1 / 2}\right)^{2}}$

## EXERCISE 13.3

1. $v=15 t^{2}-6 t+1$
2. Maximum Stress $=100$, Rate of change $=0$
3. (i) $P(x)=-10 x^{2}+700 x-2000$
(ii) Rs. 400
4. (i) 2940
(ii) 27440
5. (i) $152 \mathrm{~m} / \mathrm{s}$
(ii) $96 \mathrm{~m} / \mathrm{s}^{2}$
6. (i) $72 \mathrm{~km} / \mathrm{h}$
(ii) $-12 \mathrm{~km} / \mathrm{h}^{2}$
7. $292 \mathrm{~Pa} / \mathrm{m}$
8. 191686.6 units $/ \mathrm{m}$

## EXERCISE 14.1

1. (i) $1-91$
(ii) $131-21-22 k$
(iii) $\sqrt{273}$
2. (i) $7 ; \frac{3}{7}, \frac{-2}{7}, \frac{6}{7}$
(ii) $6 ; \frac{-2}{3}, \frac{2}{3}, \frac{1}{3}$
(iii) $10 ; \frac{-3}{5}, \frac{4}{5}, 0$
3. $t=\frac{1 \pm \sqrt{17}}{2}$
4. $-\frac{1}{9} 1+\frac{4}{9} 1-\frac{8}{9} k$
5. $\frac{171-121-16 k}{\sqrt{689}}$
6. (i) $\frac{15}{\sqrt{26}} 1+\frac{20}{\sqrt{26}} 1-\frac{5}{\sqrt{26}} k$ (ii) $-\frac{7}{\sqrt{3}} 1+\frac{7}{\sqrt{3}} 1+\frac{7}{\sqrt{3}} k \quad 7 . x=-3, y=-5$ 9. (a) $\frac{2}{3} 1-\frac{4}{3} 1+\frac{4}{3}$ $k$ and $\frac{2}{3} 1+\frac{4}{3} 1-\frac{4}{3} k$ (b) $a=-3$ (c) $-\frac{5 i}{\sqrt{14}}+\frac{10 j}{\sqrt{14}} \frac{15 k}{\sqrt{14}}$ (d) $a=-\frac{3}{2}, b=\frac{1}{2}$

10. $10 \sqrt{179}$ kilometers
11. (i) $-\frac{6}{7}, \frac{3}{7}, \frac{2}{7}$
(ii) $\frac{4}{3 \sqrt{5}}, \frac{2}{3 \sqrt{5}},-\frac{\sqrt{5}}{3}$
(iii) $\frac{2}{7}, \frac{3}{7}, \frac{6}{7}$
11. Only the triple (iii) $45^{\circ}, 60^{\circ}, 60^{\circ}$ satisfies the condition for direction angles of a single vector.

# EXERCISE 14.2

1. (i) $\frac{2}{\sqrt{14}}$ (ii) $\frac{-1}{\sqrt{1558}}$
2. $\theta=60$
3. $\theta=90$
4. (i) Projection of $\underline{a}$ along $\underline{b}:-\frac{4}{7} \underline{a}$; Projection of $\underline{b}$ along $\underline{a}:-\frac{8}{21} \underline{b}$
(ii) Projection of $\underline{a}$ along $\underline{b}: \frac{5}{29} \underline{a}$; Projection of $\underline{b}$ along $\underline{a}: \frac{5}{3} \underline{b}$
5. (i) 3 (ii) 1 or $-\frac{3}{2}$
6. 2 or -3 13. 56 units 14. 32 units 15. 102 units 16. $\frac{198}{\sqrt{26}}$ units

## EXERCISE 14.3

1. (i) $a \times \underline{b}=-3 \underline{j}-3 k ; \underline{b} \times \underline{a}=3 \underline{j}+3 \underline{k}$
(ii) $a \times \underline{b}=5 \underline{j}+3 \underline{j}-7 \underline{k} ; \underline{b} \times \underline{a}=-5 \underline{j}-3 \underline{j}+7 \underline{k}$
(iii) $\underline{a} \times \underline{b}=-7 \underline{j}-7 \underline{j} ; \underline{b} \times \underline{a}=7 \underline{j}+7 \underline{j}$ (iv) $\quad \underline{a} \times \underline{b}=3 \underline{j}-6 \underline{k} ; \underline{b} \times \underline{a}=-3 \underline{j}+6 \underline{k}$
2. (i) $\frac{21 \underline{j}-9 \underline{j}-11 \underline{k}}{\sqrt{643}} ; \sin \theta=\frac{\sqrt{643}}{\sqrt{644}}$
(ii) $\frac{-7 \underline{j}+2 \underline{j}+5 \underline{k}}{\sqrt{78}} ; \sin \theta=\frac{\sqrt{78}}{\sqrt{87}}$
(iii) $\frac{\underline{j}-\underline{k}}{\sqrt{2}} ; \sin \theta=\frac{2 \sqrt{2}}{3}$
(iv) $\frac{13 \underline{j}+\underline{j}+22 \underline{k}}{\sqrt{654}} ; \sin \theta=\frac{\sqrt{654}}{\sqrt{735}}$
3. (i) $\frac{3 \sqrt{26}}{2}$ square units
(ii) $\frac{5 \sqrt{2}}{2}$ square units

4 (i) $\sqrt{237}$ square units
(ii) $\sqrt{190}$ square units
5. $a=\frac{21}{5}, b=\frac{12}{5}$
6. (i) Parallel vectors: $\underline{u}$ and $\underline{w}$; Perpendicular vectors: No
(ii) Parallel vectors: $\underline{u}$ and $\underline{w}$; Perpendicular vectors: $\underline{u}$ and $\underline{v} ; \underline{v}$ and $\underline{w}$
13. $48 \underline{j}-4 \underline{j}+30 \underline{k}$
14. $-14 \underline{j}-14 \underline{k}$
15. $3 \underline{j}+3 \underline{j}+3 \underline{k}$
16. $15 \underline{j}-15 \underline{j}-15 \underline{k}$

## EXERCISE 14.4

1. (i) 25 cubic units (ii) 14 cubic units (iii) 10 cubic units 4. (i) $\frac{5}{2}$ (ii) $\pm 1$
2. (a) (i) 4
(ii) 3
(iii) 1
(iv) 0
3. (i) $\frac{\underline{u}}{3}$ cubic units
(ii) $\frac{2}{3}$ cubic units
4. $\frac{301}{\sqrt{1630}}$
5. $150 \underline{j}-100 \underline{k}$ (in pound feet)
6. $\sqrt{41}$ meters
7. Rs. 532500 , which is the total revenue from the sales of all items.
8. $-20 \underline{j}+110 \underline{j}+50 \underline{k} \mathrm{Nm}$
9. (a) $[500,300,200],[500,400,2000]$
(b) Rs. 770000