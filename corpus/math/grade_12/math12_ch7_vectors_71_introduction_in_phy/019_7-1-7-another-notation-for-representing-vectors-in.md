### 7.1.7 Another notation for representing vectors in plane

We introduce two special vectors,

$$
i = [1, 0], \quad j = [0, 1] \text{ in } R^2
$$

As magnitude of **i** = √(1^2 + 0^2) = 1

$$
\text{magnitude of } j = \sqrt{0^2 + 1^2} = 1
$$

So **i** and **j** are called unit vectors along **x**-axis, and along **y**-axis respectively. Using the definition of addition and scalar multiplication, the vector [**x, y**] can be written as

$$
\begin{aligned}
\mathbf{u} &= [x, y] = [x, 0] + [0, y] \\
&= x[1, 0] + y[0, 1] \\
&= xi + y
\end{aligned}
$$

Thus each vector [**x, y**] in **R²** can be uniquely represented by **xi + y**.

In terms of unit vector **i** and **j**, the sum **u + v** of two vectors

$$
\begin{aligned}
\mathbf{u} &= [x, y] \text{ and } \mathbf{v} \quad [x', y'] \text{ is written as} \\
\mathbf{u} + \mathbf{v} &= [x + x', y + y'] \\
&= (x + x')i + (y + y')j
\end{aligned}
$$

**version: 1.1**

7.1.8 A unit vector in the direction of another given vector.

A vector $\underline{u}$ is called a unit vector, if $|\underline{u}|=1$
Now we find a unit vector $u$ in the direction of any other given vector $\underline{v}$.
We can do by the use of property (ii) of magnitude of vector, as follows:
$\therefore \quad\left|\frac{1}{|\underline{v}|}\right|=\frac{1}{|\underline{v}||\underline{v}|}=1$
$\therefore \quad$ the vector $\underline{v}=\frac{1}{|\underline{v}|} \underline{v}$ is the required unit vector
It points in the same direction as $v$, because it is a positive scalar multiple of $\underline{v}$.

## Example 1:

For $\underline{v}=[1,-3]$ and $\underline{w}=[2,5]$
(i) $\underline{v}+\underline{w}=[1,-3]+[2,5]=[1+2,-3+5]=[3,2]$
(ii) $4 \underline{v}+2 \underline{w}=[4,-12]+[4,10]=[8,-2]$
(iii) $\underline{v}-\underline{w}=[1,-3]-[2,5]=[1-2,-3-5]=[-1,-8]$
(iv) $\underline{v}-\underline{v}=[1-1,-3+3]=[0,0]=0$
(v) $|\underline{v}|=\sqrt{(1)^{2}+(-3)^{2}}=\sqrt{1+9}=\sqrt{10}$

Example 2: Find the unit vector in the same direction as the vector $\underline{v}=[3,-4]$.
Solution: $\quad \underline{v}=[3,-4]=3(-4 \underline{j})$

$$
|\underline{v}|=\sqrt{3^{2}+(-4)^{2}}=\sqrt{25}=5
$$

Now $\quad \underline{u}=\frac{1}{|\underline{v}|} \underline{v}=\frac{1}{3}[3,-4] \quad$ ( $\underline{u}$ is unit vector in the direction of $v$ )

$$
=\left[\frac{3}{5}, \frac{-4}{5}\right]
$$

Verification: $|\underline{u}|=\sqrt{\left(\frac{3}{5}\right)^{2}+\left(\frac{-4}{5}\right)^{2}}=\sqrt{\frac{9}{25}+\frac{16}{25}}=1$

$$
\underline{v}=[3,-4]=3(-4 \underline{j})
$$

Example 3: Find a unit vector in the direction of the vector
(i) $\underline{v}=2 i+6 \underline{j}$
(ii) $\underline{v}=[-2,4]$

Solution: (i) $\underline{v}=2 i+6 \underline{j}$

$$
|\underline{v}|=\sqrt{(2)^{2}+(6)^{2}}=\sqrt{4+36}=\sqrt{40}
$$

$\therefore \quad$ A unit vector in the direction of $\underline{v}=\frac{\underline{v}}{|\underline{v}|} \quad \frac{2}{\sqrt{40}} i \quad \frac{6}{\sqrt{40}} \underline{j} \quad \frac{1}{\sqrt{10}} i \quad \frac{3}{\sqrt{10}} \underline{j}$
(ii) $\underline{v}=[-2,4]=-2 i+4 \underline{j}$

$$
|\underline{v}|=\sqrt{(-2)^{2}+(4)^{2}}=\sqrt{4+16}=\sqrt{20}
$$

$\therefore \quad$ A unit vector in the direction of $\underline{v}=\frac{\underline{v}}{|\underline{v}|} \quad \frac{-2}{\sqrt{20}} i \quad \frac{4}{\sqrt{20}} \underline{j} \quad \frac{-1}{\sqrt{5}} i \quad \frac{2}{\sqrt{5}} \underline{j}$

Example 4: If $A B C D$ is a parallelogram such that the points $A, B$ and $C$ are respectively $(-2,-3),(1,4)$ and $(0,-5)$. Find the coordinates of $D$.

Solution: Suppose the coordinates of $D$ are $(x, y)$
As $A B C D$ is a parallelogram

$$
\begin{aligned}
& \therefore \quad \overline{A B}=\overline{D C} \text { and } \overline{A B} \| \overline{D C} \\
& \Rightarrow \quad \overline{A B}=\overline{D C} \\
& \therefore \quad(1+2) i+(4+3) \underline{j}=(0-x) i+(-5-y) \underline{j} \\
& \Rightarrow \quad 3 i+7 \underline{j}=-x i+(-5-y) \underline{j}
\end{aligned}
$$

Equating horizontal and vertical components, we have

$$
-x=3 \Rightarrow x=-3
$$

and $\quad-5-y=7 \Rightarrow y=-12$
Hence coordinates of $D$ are $(-3,12)$.