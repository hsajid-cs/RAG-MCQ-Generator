### 7.5.3 The Volume of the Tetrahedron:

Volume of the tetrahedron $A B C D$

$$
=\frac{1}{3}(\Delta A B C)(\text { height of } D \text { above the place } A B C)
$$

version: 1.1

$$
\begin{aligned}
& =\frac{1}{3} \frac{1}{2}|\underline{u} \times \underline{v}|(h) \\
& =\frac{1}{6}(\text { Area of parallelogram with } A B \text { and } A C \text { as adjacent sides })(\mathrm{h}) \\
& =\frac{1}{6}(\text { Volume of the parallelepiped with } \underline{u}, \underline{v}, \underline{w} \text { as edges })
\end{aligned}
$$

Thus Volume $=\frac{1}{6}(\underline{u} \times \underline{v}) \cdot \underline{w}=\frac{1}{6}[\underline{u} \underline{v} \underline{w}]$

## Properties of triple scalar Product:

1. If $\underline{u}, \underline{v}$ and $\underline{w}$ are coplanar, then the volume of the parallelepiped so formed is zero i.e; the vectors $\underline{u}, \underline{v}, \underline{w}$ are coplanar $\Leftrightarrow(\underline{u} \times \underline{v}) \cdot \underline{w}=0$
2. If any two vectors of triple scalar product are equal, then its value is zero i.e;

$$
[\underline{u} \underline{u} \underline{w}]=[\underline{u} \underline{v} \underline{v}]=0
$$

Example 1: Find the volume of the parallelepiped determined by

$$
\underline{u}=(+2 \underline{j}-\underline{k}, \underline{v}=\underline{j}-\underline{j}+3 \underline{k}, \underline{w}=\underline{j}-7 \underline{j}-4 \underline{k}
$$

Solution: Volume of the parallelepiped $=\underline{u} \cdot \underline{v} \times \underline{w}=\left|\begin{array}{ccc}1 & 2 & -1 \\ 1 & -2 & 3 \\ 1 & -7 & -4\end{array}\right|$

$$
\begin{aligned}
\Rightarrow \quad \text { Volume } & =1(8+21)-2(-4-3)-1(-7+2) \\
& =29+14+5=48
\end{aligned}
$$

Example 2: Prove that four points $A(-3,5,-4), B(-1,1,1), C(-1,2,2)$ and $D(-3,4,-5)$ are coplaner.

Solution: $\overline{A B}=(-1+3)(\underline{+}(1-5) \underline{j}+(\underline{1}+4) \underline{k}=2 \underline{j}-4 \underline{j}+5 \underline{k}$

$$
\begin{aligned}
& \overline{A C}=(-1+3)(\underline{+}(2-5) \underline{j}+(\underline{2}+4) \underline{k}=2 \underline{j}-3 \underline{j}+6 \underline{k} \\
& \overline{A D}=(3-3)(\underline{+}(4-5) \underline{j}+(-5+4) \underline{k}=0 \underline{j}-\underline{k}=-\underline{j}-\underline{k}
\end{aligned}
$$

Volume of the parallelepiped formed by $\overline{A B}, \overline{A C}$ and $\overline{A D}$ is

$$
\begin{aligned}
& {[\overline{A B} \overline{A C} \overline{A D}]=\left|\begin{array}{ccc}
2 & -4 & 5 \\
2 & -3 & 6 \\
0 & -1 & -1
\end{array}\right|=2(3+6)+4(-2-0)+5(-2-0)} \\
& =18-8-10=0
\end{aligned}
$$

As the volume is zero, so the points $A, B, C$ and $D$ are coplaner.
Example 3: Find the volume of the tetrahedron whose vertices are $A(2,1,8), B(3,2,9), C(2,1,4)$ and $D(3,3,0)$
Solution: $\overline{A B}=(3-2)(\underline{+}(2-1) \underline{j}+(\underline{9}-8) \underline{k}=\underline{j}+\underline{k}$

$$
\begin{aligned}
& \overline{A C}=(2-2)(\underline{+}(1-1) \underline{j}+(\underline{4}-8) \underline{k}=0 \underline{j}-0 \underline{j}-4 \underline{k} \\
& \overline{A D}=(3-2)(\underline{+}(3-1) \underline{j}+(\underline{0}-8) \underline{k}=\underline{j}+2 \underline{j}-8 \underline{k} \\
& \therefore \quad \text { Volume of the tetrahedron }=\frac{1}{6}\left[\overline{A B} \overline{A C} \overline{A D}\right] \\
& =\frac{1}{6}\left|\begin{array}{ccc}
1 & 1 & 1 \\
0 & 0 & -4 \\
1 & 2 & -8
\end{array}\right|=\frac{1}{6}[4(2-1)]-\frac{4}{6}-\frac{2}{3}
\end{aligned}
$$

Example 4: Find the value of $\alpha$, so that $\alpha \underline{i}+\underline{j}, \underline{i}+\underline{j}+3 \underline{k}$ and $2 \underline{i}+\underline{j}-2 \underline{k}$ are coplaner.
Solution: Let $\underline{u}=\alpha \underline{i}+\underline{j}, \underline{v}=\underline{i}+\underline{j}+3 \underline{k}$ and $\underline{w}=2 \underline{i}+\underline{j}-2 \underline{k}$
Triple scalar product

$$
\begin{aligned}
& {[\underline{u} \underline{v} \underline{w}]=\left|\begin{array}{ll}
\alpha & 1 & 0 \\
1 & 1 & 3 \\
2 & 1 & -2
\end{array}\right|=\alpha(-2-3)-1(-2-6)+0(1-2)} \\
& =-5 \alpha+8
\end{aligned}
$$

The vectors will be coplaner if $-5 \alpha+8=0 \Rightarrow \alpha=\frac{8}{5}$

Example 5: Prove that the points whose position vectors are $A(-6 i+3 j+2 k)$, $B(3 i-2 j+4 k), C(5 i+7 j+3 k), D(-13 i+17 j-k)$ are coplaner.
Solution: Let $O$ be the origin.

$$
\begin{aligned}
& \therefore \quad \overrightarrow{O A}=-6 i+3 j+2 k ; \overrightarrow{O B}=3 i-2 j+4 k \\
& \therefore \quad \overrightarrow{O C}=5 i+7 j+3 k ; \overrightarrow{O D} \Rightarrow 13 i-17 j \quad k \\
& \therefore \quad \overrightarrow{A B}=\overrightarrow{O B}-\overrightarrow{O A}=(3 i-2 j+4 k)-(-6 i+3 j+2 k) \\
& \therefore \quad=9 i-5 j+2 k \\
& \begin{aligned}
\overrightarrow{A C} & =\overrightarrow{O C}-\overrightarrow{O A}=(5 i+7 j+3 k)-(-6 i+3 j+2 k) \\
& =11 i+4 j+k
\end{aligned} \\
& \begin{aligned}
\overrightarrow{A D} & =\overrightarrow{O D}-\overrightarrow{O A}=(-13 i+17 j-k)-(-6 i+3 j+2 k) \\
& \therefore \quad=-7 i+14 j-3 k
\end{aligned}
\end{aligned}
$$

Now $\quad \overrightarrow{A B} .(\overrightarrow{A C} \times \overrightarrow{A D})=\left|\begin{array}{lll}9 & -5 & 2 \\ 11 & 4 & 1 \\ -7 & 14 & -3\end{array}\right|$

$$
\begin{aligned}
& =9(-12-14)+5(-33+7)+2(154+28) \\
& =234130364 \quad 0
\end{aligned}
$$

$\therefore \overrightarrow{A B}, \overrightarrow{A C}, \overrightarrow{A D}$ are coplaner
$\Rightarrow$ The points $A, B, C$ and $D$ are coplaner.