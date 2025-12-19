### 7.2 INTRODUCTION OF VECTOR IN SPACE

In space, a rectangular coordinate system is constructed using three mutually orthogonal (perpendicular) axes, which have orgin as their common point of intersection. When sketching figures, we follow the convention that the positive $y$ $x$-axis points towards the reader, the positive $y$-axis to the right and the positive $z$-axis points upwards.

These axis are also labeled in accordance with the right hand rule. If fingers of the right hand, pointing in the direction of positive $x$-axis, are curled toward the positive $y$-axis, then the thumb will point in the direction of positive $z$-axis, perpendicular to the $x y$-plane. The broken lines in the figure represent the negative axes.

A point $P$ in space has three coordinates, one along $x$-axis, the second along $y$-axis and the third along $z$-axis. If the distances along $x$-axis, $y$-axis and $z$-axis respectively are $a, b$, and $c$, then the point $P$ is written with a unique triple of real numbers as $P=(a, b, c)$ (see figure).
right hand rule
version: 1.1

# 7.2.1 Concept of a vector in space

The set *R*^3 = ((*x*, *y*, *z*) : *x*, *y*, *z* ∈ *R*) is called the 3-dimensional space. An element (*x*, *y*, *z*) of *R*^3 represents a point *P*(*x*, *y*, *z*), which is uniquely determined by its coordinates *x*, *y* and *z*. Given a vector *u* in space, there exists a unique point *P*(*x*, *y*, *z*) in space such that the vector *∂P* is equal to *u* (see figure).

Now each element (*x*, *y*, *z*) ∈ *P*^3 is associated to a unique ordered triple [*x*, *y*, *z*], which represents the vector *u* = *∂P* = [*x*, *y*, *z*].

We define addition and scalar multiplication in *R*^3.

by:

- (i) **Addition:** For any two vectors *u* = [*x*, *y*, *z*] and *v* = [*x'*, *y'*, *z'*], we have

  *u* + *v* = [*x*, *y*, *z*] + [*x'*, *y'*, *z'*] = [*x* + *x'*, *y* + *y'*, *z* + *z'*]

- (ii) **Scalar Multiplication:** For *u* = [*x*, *y*, *z*] and *α* ∈ *R*, we have

  *αu* = *α*[*x*, *y*, *z*] = [*αx*, *αy*, *αz*]

**Definition:** The set of all ordered triples [*x*, *y*, *z*] of real numbers, together with the rules of addition and scalar multiplication, is called the set of **vectors** in *R*^3.

For the vector *u* = [*x*, *y*, *z*], *x*, *y* and *z* are called the components of *u*.

The definition of vectors in *R*^3 states that vector addition and scalar multiplication are to be carried out for vectors in space just as for vectors in the plane. So we define in *R*^3:

- a) The **negative** of the vector *u* = [*x*, *y*, *z*] as - *u* = (-1)*u* = [-*x*, -*y*, -*z*]
- b) The **difference** of two vectors *v* = [*x'*, *y'*, *z'*] and *v* = [*x'*, *y'*, *z'*] as *v* = *v* = *v* + (-*v*) = [*x'* - *x'*, *y'* - *y'*, *z'* - *z'*]
- c) The **zero vector** as 0 = [0,0,0]
- d) **Equality** of two vectors *v* = [*x'*, *y'*, *z'*] and *v* = [*x'*, *y'*, *z'*] by *v* if and only *x'* = *x'*, *y'* = *y'* and *z'* = *z'*.
- e) **Position Vector**

For any point *P*(*x*, *y*, *z*) in *R*^3, a vector *u* = [*x*, *y*, *z*] is represented by a directed line segment *∂P*, whose initial point is at origin. Such vectors are called position vectors in *R*^3.

- f) **Magnitude** of a vector: We define the **magnitude** or **norm** or **length** of a vector *u* in space by the distance of the point *P*(*x*, *y*, *z*) from the origin *O*.

  *∴* |*∂P*|=|*u*| = √*x*+*y*+*z*+

  **Example 1:** For the vectors *v* = [2,1,3] and *w* = [−1,4,0], we have the following

  - (i) *v* + *w* = [2 − 1, 1 + 4, 3 + 0] = [1,5,3]
  - (ii) *v* − *w* = [2 + 1,1 − 4, 3 − 0] = [3, −3, 3]
  - (iii) 2*w* = 2[−1, 4, 0] = [−2, 8, 0]
  - (iv) |*v* − 2*u*| = [2 + 2,1 − 8,3 − 0]| = [4, −7, 3]| = √(4)+(-7)+(3)+

# 7.2.2 Properties of Vectors

Vectors, both in the plane and in space, have the following properties:

Let *u*, *v* and *w* be vectors in the plane or in space and let *a*, *b* ∈ *R*, then they have the following properties

- (i) *u* + *v* = *v* + *u* (Commutative Property)
- (ii) (*u* + *v*) + *w* = *u* + (*v* + *w*) (Associative Property)
- (iii) *u* + (−1)*u* = *u* − *u* = 0 (Inverse for vector addition)
- (iv) *a*(*v* + *w*) = *a**v* + *a**w* (Distributive Property)
- (v) *a*(*bu*) = (*ab*)*u* (Scalar Multiplication)

**Proof:** Each statement is proved by writing the vector/vectors in component form in *R*^3 / *R*^3 and using the properties of real numbers. We give the proofs of properties (i) and (ii) as follows.

- (i) Since for any two real numbers *a* and *b*

  *a* + *b* = *b* + *a*, it follows, that

  for any two vectors *u* = [*x*, *y*] and *v* = [*x'*, *y'*] in *R*^3, we have

  *u* + *v* = [*x*, *y*] + [*x'* + *y'*]

  = [*x* + *x'*, *y* + *y'*]

  = [*x'* + *x*, *y'* + *y*]

  = [*x'*, *y'*] + [*x*, *y*]

  = *v* + *u*

  So addition of vectors in *R*^3 is commutative

(ii) Since for any three real numbers $a, b, c$,

$$
(a+b)+c=a+(b+c) \quad \text { it follows that }
$$

for any three vectors, $\underline{u}=[x, y], \underline{v}=\left(x^{\prime}, y^{\prime}\right]$ and $w\left[x^{\prime \prime}, y^{\prime \prime}\right]$ in $R^{2}$, we have

$$
\begin{aligned}
(\underline{u}+\underline{v})+\underline{w} & =\left[x+x^{\prime}, y+y^{\prime}\right]+\left[x^{\prime \prime}, y^{\prime \prime}\right] \\
& =\left[\left(x+x^{\prime}\right)+x^{\prime \prime},\left(y+y^{\prime}\right)+y^{\prime \prime}\right] \\
& =\left[x+\left(x^{\prime}+x^{\prime \prime}\right), y+\left(y^{\prime}+y^{\prime \prime}\right)\right] \\
& =\left[x, y\right]+\left[x^{\prime}+x^{\prime \prime}, y^{\prime}+y^{\prime \prime}\right] \\
& =\underline{u}+(\underline{v}+\underline{w})
\end{aligned}
$$

So addition of vectors in $R^{2}$ is associative
The proofs of the other parts are left as an exercise for the students.