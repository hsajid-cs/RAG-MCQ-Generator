### 7.4.4 Parallel Vectors

If $\underline{u}$ and $\underline{v}$ are parallel vectors, $(\theta=\mathbf{0} \quad \sin \theta$ ), then
$\underline{u} \times \underline{v}=\|\underline{u}\| \frac{1}{2} \sin \theta \hat{n}$
$\underline{u} \times \underline{v}=\underline{0}$ or $\underline{v} \times \underline{u}=0$
And if $\underline{u} \times \underline{v}=\underline{0}$, then
either $\sin \theta=0$ or $\left|\underline{u}\right|=0$ or $\left|\underline{v}\right|=0$
(i) If $\sin \theta=0 \Rightarrow \theta=0^{\prime}$ or $180^{\prime}$, which shows that the vectors $\underline{u}$ and $\underline{v}$ are parallel.
(ii) If $\underline{u}=0$ or $\underline{v}=0$, then since the zero vector has no specific direction, we adopt the convention that the zero vector is parallel to every vector.

Note: Zero vector is both parallel and perpendicular to every vector. This apparent contradiction will cause no trouble, since the angle between two vectors is never applied when one of them is zero vector.

Example 1: Find a vector perpendicular to each of the vectors

$$
\underline{a}=2 \underline{i}+\underline{j}+\underline{k} \quad \text { and } \quad \underline{b}=4 \underline{i}+2 \underline{j}-\underline{k}
$$

Solution: A vector perpendicular to both the vectors $\underline{a}$ and $\underline{b}$ is $\underline{a} \times \underline{b}$

$$
\therefore \quad \underline{a} \times \underline{b}=\left|\begin{array}{ccc}
\underline{i} & \underline{j} & \underline{k} \\
2 & -1 & 1 \\
4 & 2 & -1
\end{array}\right|=-i+6 \underline{j}+8 \underline{k}
$$

Verification:

$$
\underline{a}, \underline{a} \times \underline{b}=(2 i+\underline{j}+\underline{k}) \cdot(-i+6 \underline{j}+8 \underline{k})=(2)(-1)+(-1)(6)+(1)(8)=0
$$

and $\quad \underline{b}, \underline{a} \times \underline{b}=(4 i+2 \underline{j}-\underline{k}) \cdot(-i+6 \underline{j}+8 \underline{k})=(4)(-1)+(2)(6)+(-1)(8)=0$
Hence $\underline{a} \times \underline{b}$ is perpendicular to both the vectors $\underline{a}$ and $\underline{b}$.

Example 2: If $\underline{a}=4 i+3 \underline{j}+\underline{k}$ and $\underline{b}=2 i-\underline{j}+2 \underline{k}$. Find a unit vector perpendicular to both $\underline{a}$ and $\underline{b}$. Also find the sine of the angle between the vectors $\underline{a}$ and $\underline{b}$.

$$
\begin{aligned}
& \text { Solution: } \quad \underline{a} \times \underline{b}=\left|\begin{array}{ccc}
\underline{i} & \underline{j} & \underline{k} \\
4 & 3 & 1 \\
2 & -1 & 2
\end{array}\right|=7 i-6 \underline{j}-10 \underline{k} \\
& \text { and } \quad|\underline{a} \times \underline{b}|=\sqrt{(7)^{2}+(-6)^{2}+(10)^{2}}=\sqrt{185} \\
& \therefore \quad \text { A unit vector } \underline{\theta} \text { perpendicular to } \underline{a} \text { and } \underline{b}=\left|\begin{array}{l}
\underline{a} \times \underline{b} \\
|\underline{a} \times \underline{b}| \\
=\frac{1}{\sqrt{185}}(7 i-6 \underline{j}-10 \underline{k})
\end{array}\right| \\
& \text { Now }|\underline{a}|=\sqrt{(4)^{2}+(3)^{2}+(1)^{2}}=\sqrt{26} \\
& \quad|\underline{b}|=\sqrt{(2)^{2}+(-1)^{2}+(2)^{2}}=3
\end{aligned}
$$

If $\theta$ is the angle between $\underline{a}$ and $\underline{b}$, then $|\underline{a} \times \underline{b}|=|\underline{a}||\underline{b}| \sin \theta$

$$
\Rightarrow \quad \sin \theta=\frac{\underline{a} \times \underline{b}}{|\underline{a} \times \underline{b}|}=\frac{\sqrt{185}}{3 \sqrt{26}}
$$

Example 3: Prove that $\sin (\alpha+\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta$
Proof: Let $\overrightarrow{O A}$ and $\overrightarrow{O B}$ be unit vectors in the $x y$-plane making angles $\alpha$ and $-\beta$ with the positive $x$-axis respectively

$$
\begin{aligned}
& \text { So that } \angle A O B=\alpha+\beta \\
& \text { Now } \overrightarrow{O A}=\cos \alpha i+\sin \alpha j \\
& \text { and } \quad \overrightarrow{O B}=\cos (-\beta) i+\sin (-\beta) \underline{j} \\
& =\cos \beta i-\sin \beta j \\
& \therefore \overrightarrow{O B} \times \overrightarrow{O A}=(\cos \beta i-\sin \beta j) \times(\cos \alpha i+\sin \alpha j) \\
& \Rightarrow \quad|\overrightarrow{O B}||\overrightarrow{O A}| \sin (\alpha+\beta) \underline{k}=\left|\begin{array}{ccc}
\underline{i} & \underline{j} & \underline{k} \\
\cos \beta & -\sin \beta & 0 \\
\cos \alpha & \sin \alpha & 0
\end{array}\right| \\
& \Rightarrow \quad \sin (\alpha+\beta) \underline{k}=(\sin \alpha \cos \beta+\cos \alpha \sin \beta) \underline{k} \\
& \therefore \quad \sin (\alpha+\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta
\end{aligned}
$$

Example 4: In any triangle $A B C$, prove that

$$
\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C} \quad \text { (Law of Sines) }
$$

Proof: Suppose vectors $\underline{a}, \underline{b}$ and $\underline{c}$ are along the sides $B C, C A$ and $A B$ respectively of the triangle $A B C$.

$$
\begin{aligned}
& \therefore \quad \underline{a}+\underline{b}+\underline{c}=0 \\
& \Rightarrow \quad \underline{b}+\underline{c}=-\underline{a} \\
& \text { Take cross product with } \underline{c} \\
& \underline{b} \times \underline{c}+\underline{c} \times \underline{c}=-\underline{a} \times \underline{c} \\
& \underline{b} \times \underline{c}=\underline{c} \times \underline{a} \quad(\therefore \underline{c} \times \underline{c}=0) \\
& \Rightarrow \quad|\underline{b} \times \underline{c}|=|\underline{c} \times \underline{a}| \\
& |\underline{b}||\underline{c}| \sin (\pi-A)=-|\underline{c}||\underline{a}| \sin (\pi \quad B) \\
& \Rightarrow \quad b c \sin A=a \sin B \Rightarrow b \sin A=a \sin B \\
& \therefore \quad \frac{a}{\sin A}=\frac{b}{\sin B}
\end{aligned}
$$

similarly by taking cross product of (i) with $\underline{b}$, we have

$$
\frac{a}{\sin A}=\frac{c}{\sin C}
$$

From (ii) and (iii), we get

$$
\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}
$$