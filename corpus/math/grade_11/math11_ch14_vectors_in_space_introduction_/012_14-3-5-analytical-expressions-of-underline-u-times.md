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