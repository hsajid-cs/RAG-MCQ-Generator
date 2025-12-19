### 4.9.1 Solution of System of Homogeneous Linear Equations by Gaussian Elimination Method

Gaussian Elimination is a systematic method for solving systems of linear equations, named after the German mathematician Carl Friedrich Gauss. It involves performing a series of row operations on the system's augmented matrix to transform it into rowechelon form. Once the matrix is in this simplified form, the solution to the system can be determined through back substitution. This method is widely used due to its efficiency and clarity in solving linear systems.

Example 14 Solve the following system of equations by Gaussian Elimination method:

$$
\begin{aligned}
x+2 y+z & =0 \\
2 x+3 y+4 z & =0 \\
4 x+3 y+2 z & =0
\end{aligned}
$$

Solution The augmented matrix is

$$
\begin{aligned}
& A_{0}=\left[\begin{array}{lll|l}
1 & 2 & 1 & 0 \\
2 & 3 & 4 & 0 \\
4 & 3 & 2 & 0
\end{array}\right] \\
& \underset{=}{E}\left[\begin{array}{rrr|r}
1 & 2 & 1 & 0 \\
0 & -1 & 2 & 0 \\
0 & -5 & -2 & 0
\end{array}\right] B y R_{2}+(-2) R_{1} \rightarrow R_{2}^{\prime} \text { and } R_{3}+(-4) R_{1} \rightarrow R_{3}^{\prime} \\
& \Rightarrow \quad \underset{=}{E}\left[\begin{array}{llll|r}
1 & 2 & 1 & 0 \\
0 & 1 & -2 & 0 \\
0 & -5 & -2 & 0
\end{array}\right] B y(-1) R_{2} \rightarrow R_{2}^{\prime} \\
& \Rightarrow \quad \underset{=}{E}\left[\begin{array}{llll|r}
1 & 2 & 1 & 0 \\
0 & 1 & -2 & 0 \\
0 & 0 & -12 & 0
\end{array}\right] B y R_{3}+5 R_{2} \rightarrow R_{3}^{\prime} \\
& \Rightarrow \quad \underset{=}{E}\left[\begin{array}{llll|r}
1 & 2 & 1 & 0 \\
0 & 1 & -2 & 0 \\
0 & 0 & 1 & 0
\end{array}\right] B y\left(\frac{-1}{12}\right) R_{3} \rightarrow R_{3}^{\prime} \quad \text { (Rank of } A=3=\text { number of variables) }
\end{aligned}
$$

The matrix is in row-echelon form.
By back-substitution, from the third row, $z=0$.
From the second row: $y-2 z=0$

$$
\begin{aligned}
y-2(0) & =0 \\
y & =0
\end{aligned}
$$

From the first row, $x+2 y+z=0$, substituting $y=0$ and $x=0$, we have

$$
\begin{aligned}
x+2(0)+0 & =0 \\
x & =0
\end{aligned}
$$

Thus, the system has only trivial solution, i.e., $(x, y, z)=(0,0,0)$.

Example 15 Solve the following system of equations using Gaussian Elimination Method.

$$
\begin{aligned}
& x_{1}+x_{2}+x_{3}=0 \\
& x_{1}-x_{2}+3 x_{3}=0 \\
& x_{1}+3 x_{2}-x_{3}=0
\end{aligned}
$$

Solution The argumented matrix is

$$
\begin{aligned}
& A_{b}=\left[\begin{array}{rrr}
1 & 1 & 1 & 0 \\
1 & -1 & 3 & 0 \\
1 & 3 & -1 & 0
\end{array}\right] \\
& \underline{\underline{R}}\left[\begin{array}{rrr}
1 & 1 & 1 & 0 \\
0 & -2 & 2 & 0 \\
0 & 2 & -2 & 0
\end{array}\right] \text { By } R_{2}+(-1) R_{1} \rightarrow R_{2}^{\prime} \text { and } R_{3}+(-1) R_{1} \rightarrow R_{2}^{\prime} \\
& \Rightarrow \quad \underline{\underline{R}}\left[\begin{array}{lll}
1 & 1 & 1 & 0 \\
0 & 1 & -1 & 0 \\
0 & 2 & -2 & 0
\end{array}\right] \text { By }\left(-\frac{1}{2}\right) R_{2} \rightarrow R_{2}^{\prime} \\
& \Rightarrow \quad \underline{\underline{R}}\left[\begin{array}{lll}
1 & 1 & 1 & 0 \\
0 & 1 & -1 & 0 \\
0 & 0 & 0 & 0
\end{array}\right] \text { By } R_{3}+(-2) R_{2} \rightarrow R_{3}^{\prime} \quad \text { (Rank of } A<\text { number of variables) }
\end{aligned}
$$

The matrix is in row-echelon form
Thus, the above system is reduced to the equivalent system of equations

$$
\begin{aligned}
x_{1}+x_{2}+x_{3} & =0 \\
x_{2}-x_{3} & =0 \\
0 x_{3} & =0
\end{aligned}
$$

From (i) and (ii), we get

$$
\begin{aligned}
& x_{1}=-x_{2}-x_{3} \\
& x_{2}=x_{3}
\end{aligned}
$$

Substituting $x_{2}=x_{3}$ in (iii), we get

$$
\begin{aligned}
& x_{1}=-x_{3}-x_{3}=2 x_{3} \\
& \Rightarrow \quad x_{1}=-2 x_{3}
\end{aligned}
$$

As $x_{3}$ is arbitrary, so we can find infinitely many values of $x_{1}$ and $x_{2}$ from (iii) and (iv) or the system is satisfied by $x_{1}=-2 t, x_{2}=t$ and $x_{3}=t$ for any value of $t$.

From above examples we observe that:
Rule - I: Homogeneous system of linear equation has only trivial solution if rank of $A=$ number of variables.
Rule - II: Homogeneous system of linear equation has non-trivial solution if rank of $A<$ number of variables.

# 4.10 Applications of Matrices in Real World

Matrices play a crucial role in solving real-world problems across various fields. In graphic design, they help manipulate images through transformations like scaling, rotation, and reflection. Data encryption and cryptography use matrices for secure communication by encoding and decoding messages. In seismic analysis, engineers use matrices to model and predict earthquake wave behavior. Geometric transformations, such as translation and dilation, rely on matrices to modify shapes in computer graphics. Additionally, social network analysis leverages matrices to represent and analyze relationships between individuals, identifying key influencers and connections in a network.
Transformation or Reflection Matrix is a mathematical tool that represents the reflection of a point or object across a mirror line in a coordinate plane. It's a matrix representation of a reflection transformation. In two dimensions, this typically means reflecting across the $x$-axis, $y$-axis or a line such as $y=x$.

To reflect a matrix over the $x$-axis, we have to multiply it by $\left[\begin{array}{ll}1 & 0 \\ 0 & -1\end{array}\right]$
To reflect a matrix over the $y$-axis, we have to multiply it by $\left[\begin{array}{ll}-1 & 0 \\ 0 & 1\end{array}\right]$
To reflect a matrix over the line $y=x$, we have to multiply it by $\left[\begin{array}{ll}0 & 1 \\ 1 & 0\end{array}\right]$
Example 16 A triangle has the vertices $A(2,3), B(-1,4)$ and $C(3,-2)$. Find the vertices of the reflected triangle over the $x$-axis by using transformation matrix.
Solution To reflect a point across a certain axis or line, we have multiply the point as a column vector by the corresponding transformation matrix.
Here, to reflect the given points over the $x$-axis, we use the transformation matrix $\left[\begin{array}{ll}1 & 0 \\ 0 & -1\end{array}\right]$.

Write the points as column matrices

$$
A=\left[\begin{array}{l}
2 \\

\end{array}\right], B=\left[\begin{array}{r}
-1 \\

\end{array}\right], C=\left[\begin{array}{r}
3 \\
-2
\end{array}\right]
$$

The vertex $A^{\prime}$ of the reflected image $=\left[\begin{array}{ll}1 & 0 \\ 0 & -1\end{array}\right]\left[\begin{array}{l}2 \\ 3\end{array}\right]=\left[\begin{array}{l}2+0 \\ 0-3\end{array}\right]=\left[\begin{array}{r}2 \\ -3\end{array}\right]=(2,-3)$
The vertex $B^{\prime}$ of the reflected image $=\left[\begin{array}{ll}1 & 0 \\ 0 & -1\end{array}\right]\left[\begin{array}{l}-1 \\ 4\end{array}\right]=\left[\begin{array}{l}-1+0 \\ 0-4\end{array}\right]=\left[\begin{array}{l}-1 \\ -4\end{array}\right]=(-1,-4)$
The vertex $C^{\prime}$ of the reflected image $=\left[\begin{array}{ll}1 & 0 \\ 0 & -1\end{array}\right]\left[\begin{array}{r}3 \\ -2\end{array}\right]=\left[\begin{array}{l}3-0 \\ 0+2\end{array}\right]=\left[\begin{array}{l}3 \\ 2\end{array}\right]=(3,2)$
Thus, the vertices of the reflected triangle are $A^{\prime}(2,-3), B^{\prime}(-1,-4)$ and $C^{\prime}(3,2)$.
Coding is the process of converting a message into a specific format using a code. A code is a system of symbols, words or signals used to represent other words or meanings. It's often used to hide the actual meaning of a message.
To decode a message, we multiply coded matrix by the inverse of the given matrix.
Example17 Use matrix $A=\left[\begin{array}{ll}1 & 2 \\ 3 & 1\end{array}\right]$ to encode the message: ATTACK, where letters $A$ to $Z$ are corresponding to the numbers 1 to 26 .
Solution Here

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
| N | 0 | P | Q | R | S | T | U | V | W | X | Y | Z |
| 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

Divide the letters of the message into groups of two.

# AT TA CK

Assign the numbers to these letters and convert each pair of numbers into $2 \times 1$ matrices.

$$
\left[\begin{array}{l}
A \\
T
\end{array}\right]=\left[\begin{array}{l}
1 \\

\end{array}\right], \quad\left[\begin{array}{l}
T \\
A
\end{array}\right]=\left[\begin{array}{l}
20 \\

\end{array}\right], \quad\left[\begin{array}{l}
C \\
K
\end{array}\right]=\left[\begin{array}{l}
3 \\

\end{array}\right]
$$

So, the message in $2 \times 1$ matrices is $\left[\begin{array}{l}1 \\ 20\end{array}\right]\left[\begin{array}{l}20 \\ 1\end{array}\right]\left[\begin{array}{l}3 \\ 11\end{array}\right]$
Now to encode, we multiply, on the left, each matrix of our message by the matrix $A$. i.e., $\left[\begin{array}{ll}1 & 2 \\ 3 & 1\end{array}\right]\left[\begin{array}{l}1 \\ 20\end{array}\right]=\left[\begin{array}{ll}1+40 \\ 3+20\end{array}\right]=\left[\begin{array}{l}41 \\ 23\end{array}\right]$

$$
\begin{aligned}
& {\left[\begin{array}{ll}
1 & 2 \\
3 & 1
\end{array}\right]\left[\begin{array}{l}
20 \\

\end{array}\right]=\left[\begin{array}{ll}
20 & +2 \\
60 & +1
\end{array}\right]=\left[\begin{array}{l}
22 \\

\end{array}\right]} \\
& {\left[\begin{array}{ll}
1 & 2 \\
3 & 1
\end{array}\right]\left[\begin{array}{l}
3 \\

\end{array}\right]=\left[\begin{array}{ll}
3 & +22 \\
9 & +11
\end{array}\right]=\left[\begin{array}{l}
25 \\

\end{array}\right]}
\end{aligned}
$$

So, the desired coded message is $\left[\begin{array}{l}41 \\ 23\end{array}\right]\left[\begin{array}{l}22 \\ 61\end{array}\right]\left[\begin{array}{l}25 \\ 20\end{array}\right]$

# EXERCISE 4.3

1. Find the inverses of the following matrices by using row operations:
(i) $\left[\begin{array}{ccc}2 & 6 & -3 \\ 0 & -2 & 0 \\ -2 & 5 & 6\end{array}\right]$
(ii) $\left[\begin{array}{ccc}1 & 2 & -1 \\ 0 & -2 & 8 \\ 1 & 0 & 2\end{array}\right]$
(iii) $\left[\begin{array}{ccc}1 & 6 & 2 \\ 2 & 13 & 0 \\ 0 & -1 & 1\end{array}\right]$
2. Find the rank of the following matrices:
(i) $\left[\begin{array}{cccc}1 & -1 & 3 & 1 \\ -2 & -6 & 1 & -1 \\ 3 & 1 & 4 & -2\end{array}\right]$
(ii) $\left[\begin{array}{cccc}1 & -2 & 3 \\ 2 & -4 & 6 \\ -1 & 0 & 2 \\ 0 & 1 & -1\end{array}\right]$
(iii) $\left[\begin{array}{cccc}3 & -1 & 3 & 0 & 1 \\ 1 & 2 & -1 & -3 & -2 \\ 2 & 3 & 4 & 2 & 1 \\ 2 & 5 & -2 & -3 & 3\end{array}\right]$
3. Solve the following systems of linear equations by Cramer's rule:

$$
\begin{aligned}
& 2 x+y-z=1 \\
& \text { (i) } \begin{array}{c}
x_{1}+2 x_{2}-3 x_{3}=0 \\
4 x_{1}-x_{2}+x_{3}=5 \\
-2 x_{1}+3 x_{2}+2 x_{3}=3
\end{array} \\
& 2 x_{1}-x_{2}+x_{3}=1 \\
& \text { (iii) } x_{1}+2 x_{2}+2 x_{3}=2 \\
& x_{1}-2 x_{2}-x_{3}=1
\end{aligned}
$$

4. Solve the following systems of linear equations by matrix inversion method:

$$
\begin{aligned}
& x-2 y+z=-1 \\
& \left.\begin{array}{c}
2 x_{1}+x_{2}+3 x_{3}=3 \\
\text { (ii) } x_{1}+3 x_{2}-2 x_{3}=0 \\
-3 x_{1}-x_{2}+2 x_{3}=4
\end{array} \right\} \\
& x+y=2 \\
& \text { (iii) } 2 x-z=1 \\
& 2 y-3 z=-1
\end{aligned}
$$

5. Solve the following systems by reducing their augmented matrices to the echelon form and the reduced echelon forms:

$$
\left.\begin{array}{c}
x_{1}+2 x_{2}-2 x_{3}=-1 \\
2 x_{1}+3 x_{2}+x_{3}=1 \\
5 x_{1}+4 x_{2}-3 x_{3}=1
\end{array}\right\} \quad \begin{gathered}
x+2 y+z=2 \\
\text { (ii) } 2 x+y+2 z=3 \\
2 x+3 y-z=7
\end{gathered} \quad \begin{gathered}
x_{1}+4 x_{2}+x_{3}=2 \\
\text { (iii) } 2 x_{1}+x_{2}-2 x_{3}=9 \\
3 x_{1}+x_{2}-x_{3}=12
\end{gathered}
$$

6. Solve the following systems of homogeneous linear equations by using Gaussian elimination method:

$$
\left.\begin{array}{c}
\left.x+4 y-2 z=0\right] \\
\text { (i) } \left.\begin{array}{c}
2 x+y+5 z=0 \\
5 x+2 y+8 z=0
\end{array}\right\} \\
\left.\begin{array}{c}
\left.x_{1}+4 x_{2}+2 x_{3}=0\right] \\
\text { (ii) } \left.\begin{array}{c}
2 x_{1}+x_{2}-3 x_{3}=0 \\
3 x_{1}+2 x_{2}-4 x_{3}=0
\end{array}\right\} \\
\text { (iii) } \begin{array}{c}
x_{1}+2 x_{2}-x_{3}=0 \\
x_{1}-x_{2}+5 x_{3}=0 \\
2 x_{1}+x_{2}+4 x_{3}=0
\end{array}\right\}
$$

7. A triangle has vertices at $A(4,1), B(-2,5)$ and $C(0,-3)$. Find the vertices of the reflected triangle over the $y$-axis using a transformation matrix.
8. The point $A$ is mapped to $(30,20,-5)$ by the scaling matrix $P_{0} \quad 0 \quad-5 \quad 0$

Find the coordinates of $A$.
[Hint: If $A$ is mapped to $A^{\prime}$ by scaling matrix $P$, then $P A=A^{\prime}$ ]
9. Find the equation of the image of the curve with equation $y=x^{2}$ under the transformation with associated matrix $A^{2}$
10. Use the matrix $A=\left[\begin{array}{llll}1 & 0 & 1 \\ 2 & -1 & 1 \\ 0 & 1 & 2\end{array}\right]$ to encode the message: KEEP IT UP, where letters $A$ to $Z$ are corresponding to the numbers 1 to 26.
11. Decode the message $\left[\begin{array}{l}11 \\ 20 \\ 43\end{array}\right]\left[\begin{array}{l}25 \\ 10 \\ 41\end{array}\right]\left[\begin{array}{l}22 \\ 14 \\ 41\end{array}\right]$ that was encoded using matrix
$A=\left[\begin{array}{llll}1 & 1 & -1 \\ 1 & 0 & 1 \\ 2 & 1 & 1\end{array}\right]$, where the numbers 1 to 26 are corresponding to the letters
$A$ to $Z$, and 27 is representing space or $\sim$.