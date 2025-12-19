### 4.2.2 Subtraction of Matrices

If $A=\left[a_{i j}\right]$ and $B=\left[b_{i j}\right]$ are matrices of order $m \times n$, then we define subtraction of $B$ from $A$ as:

$$
\begin{aligned}
A-B & =A+(-B) \\
& =\left[a_{i j}\right]+\left[-b_{i j}\right]=\left[a_{i j}+\left(-b_{i j}\right)\right]=\left[a_{i j}-b_{i j}\right] \text { for } i=1,2,3, \ldots, m ; j=1,2,3, \ldots, n
\end{aligned}
$$

Thus, the matrix $A-B$ is formed by subtracting each entry of $B$ from the corresponding entry of $A$.

Example 1 If $A=\left[\begin{array}{cccc}1 & 0 & -1 & 2 \\ 3 & 1 & 2 & 5 \\ 0 & -2 & 1 & 6\end{array}\right]$ and $B=\left[\begin{array}{cccc}2 & -1 & 3 & 1 \\ 1 & 3 & -1 & 4 \\ 3 & 1 & 2 & -1\end{array}\right]$, then show that

$$
(A+B)^{t}=A^{t}+B^{t}
$$

Solution

$$
\begin{aligned}
& A+B=\left[\begin{array}{cccc}
1 & 0 & -1 & 2 \\
3 & 1 & 2 & 5 \\
0 & -2 & 1 & 6
\end{array}\right]+\left[\begin{array}{cccc}
2 & -1 & 3 & 1 \\
1 & 3 & -1 & 4 \\
3 & 1 & 2 & -1
\end{array}\right]=\left[\begin{array}{cccc}
1+2 & 0+(-1) & -1+3 & 2+1 \\
3+1 & 1+3 & 2+(-1) & 5+4 \\
0+3 & -2+1 & 1+2 & 6+(-1)
\end{array}\right] \\
& =\left[\begin{array}{cccc}
3 & -1 & 2 & 3 \\
4 & 4 & 1 & 9 \\
3 & -1 & 3 & 5
\end{array}\right] \\
& \text { and }(A+B)^{t}=\left[\begin{array}{ccc}
3 & 4 & 3 \\
-1 & 4 & -1 \\
2 & 1 & 3 \\
3 & 9 & 5
\end{array}\right]
\end{aligned}
$$

Taking transpose of $A$ and $B$, we have

$$
\begin{gathered}
A^{t}=\left[\begin{array}{ccc}
1 & 3 & 0 \\
0 & 1 & -2 \\
-1 & 2 & 1 \\
2 & 5 & 6
\end{array}\right] \text { and } B^{t}=\left[\begin{array}{ccc}
2 & 1 & 3 \\
-1 & 3 & 1 \\
3 & -1 & 2 \\
1 & 4 & -1
\end{array}\right] \\
\Rightarrow \quad A^{t}+B^{t}=\left[\begin{array}{ccc}
1 & 3 & 0 \\
0 & 1 & -2 \\
-1 & 2 & 1 \\
2 & 5 & 6
\end{array}\right]+\left[\begin{array}{ccc}
2 & 1 & 3 \\
-1 & 3 & 1 \\
3 & -1 & 2 \\
1 & 4 & -1
\end{array}\right]=\left[\begin{array}{ccc}
3 & 4 & 3 \\
-1 & 4 & -1 \\
2 & 1 & 3 \\
3 & 9 & 5
\end{array}\right]
\end{gathered}
$$

From (i) and (ii), we have $(A+B)^{t}=A^{t}+B^{t}$

# 4.2.3 Scalar Multiplication

If $A=\left[a_{i j}\right]$ is $m \times n$ matrix and $k$ is a real or complex number, then the product of $k$ and $A$, denoted by $k A$, is the matrix formed by multiplying each entry of $A$ by $k$, that is
$k A=\left[k a_{i j}\right]$
Obviously, order of $k A$ is $m \times n$.