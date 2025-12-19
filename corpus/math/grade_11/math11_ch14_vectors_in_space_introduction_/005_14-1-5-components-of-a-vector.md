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