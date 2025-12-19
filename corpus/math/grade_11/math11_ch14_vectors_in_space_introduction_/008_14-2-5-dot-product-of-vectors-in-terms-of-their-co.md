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