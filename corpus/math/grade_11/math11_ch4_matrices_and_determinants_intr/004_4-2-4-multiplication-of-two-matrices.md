### 4.2.4 Multiplication of two Matrices

## Note

If $n$ is a positive integer, then $A+A+A+\cdots$ to $n$ terms $=n A$.

Two matrices $A$ and $B$ are said to be conformable for the product $A B$ if the number of columns of $A$ is equal to the number of rows of $B$.
Let $A=\left[a_{i j}\right]$ be a $2 \times 3$ matrix and $B=\left[b_{i j}\right]$ be a $3 \times 2$ matrix, then the product $A B$ is defined to be the $2 \times 2$ matrix $C$ whose element $c_{i j}$ is the sum of products of the corresponding elements of the $i$ th row of $A$ with elements of $j$ th column of $B$. For example, the element $c_{21}$ of $C$ is shown in the figure (A), that is
Figure (A)
$c_{21}=a_{21} b_{11}+a_{22} b_{21}+a_{23} b_{31}$. Thus
$A B=\left[\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23}\end{array}\right]\left[\begin{array}{lll}b_{11} & b_{12} \\ b_{21} & b_{22} \\ b_{31} & b_{32}\end{array}\right]=\left[\begin{array}{lll}a_{11} b_{11}+a_{12} b_{21}+a_{13} b_{31} & a_{11} b_{12}+a_{12} b_{22}+a_{13} b_{32} \\ a_{21} b_{11}+a_{22} b_{21}+a_{23} b_{31} & a_{21} b_{12}+a_{22} b_{22}+a_{23} b_{32}\end{array}\right]$

Similarly $B A=\left[\begin{array}{lll}b_{11} & b_{12} \\ b_{21} & b_{22} \\ b_{31} & b_{32}\end{array}\right]\left[\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23}\end{array}\right]$

$$
=\left[\begin{array}{lll}
b_{11} a_{11}+b_{12} a_{21} & b_{11} a_{12}+b_{12} a_{22} & b_{11} a_{13}+b_{12} a_{23} \\
b_{21} a_{11}+b_{22} a_{21} & b_{21} a_{12}+b_{22} a_{22} & b_{21} a_{13}+b_{22} a_{23} \\
b_{31} a_{11}+b_{32} a_{21} & b_{31} a_{12}+b_{32} a_{22} & b_{31} a_{13}+b_{32} a_{23}
\end{array}\right]
$$

From (i) and (ii), $A B$ and $B A$ are calculated their orders are $2 \times 2$ and $3 \times 3$ respectively.
Note1. In general, $A B \neq B A$
Note 2. If the product $A B$ is defined, then the order of the product can be illustrated as given below:

Order of $A$
Order of $B$
Order of $A B$
Example 2 If $A=\left[\begin{array}{rrr}2 & -1 & 0 \\ 1 & 2 & -3 \\ 1 & 2 & -2\end{array}\right]$ and $B=\left[\begin{array}{rrr}2 & -2 & 3 \\ -1 & -4 & 6 \\ 0 & -5 & 5\end{array}\right]$, then compute $A^{2} B$.

Solution

$$
\begin{aligned}
A^{2} & =A \cdot A=\left[\begin{array}{rrr}
2 & -1 & 0 \\
1 & 2 & -3 \\
1 & 2 & -2
\end{array}\right]\left[\begin{array}{rrr}
2 & -1 & 0 \\
1 & 2 & -3 \\
1 & 2 & -2
\end{array}\right] \\
& =\left[\begin{array}{rrr}
4-1+0 & -2-2+0 & 0+3+0 \\
2+2-3 & -1+4-6 & 0-6+6 \\
2+2-2 & -1+4-4 & 0-6+4
\end{array}\right]=\left[\begin{array}{rrr}
3 & -4 & 3 \\
1 & -3 & 0 \\
2 & -1 & -2
\end{array}\right] \\
\therefore \quad A^{2} B & =\left[\begin{array}{rrr}
3 & -4 & 3 \\
1 & -3 & 0 \\
2 & -1 & -2
\end{array}\right]\left[\begin{array}{rrr}
2 & -2 & 3 \\
-1 & -4 & 6 \\
0 & -5 & 5
\end{array}\right] \\
& =\left[\begin{array}{rrr}
6+4+0 & -6+16-15 & 9-24+15 \\
2+3+0 & -2+12+0 & 3-18+0 \\
4+1+0 & -4+4+10 & 6-6-10
\end{array}\right]=\left[\begin{array}{rrr}
10 & -5 & 0 \\
5 & 10 & -15 \\
5 & 10 & -10
\end{array}\right]
\end{aligned}
$$

Note: Powers of square matrices are defined as:

$$
\begin{aligned}
& A^{2}=A \times A, A^{3}=A \times A \times A \\
& A^{n}=A \times A \times A \times \cdots \text { to } n \text { factors. }
\end{aligned}
$$

# 4.3 Properties of Matrix Addition, Scalar Multiplication and Matrix Multiplication

If $A, B$ and $C$ are conformable for the indicated sum or product of matrices and $c$ and $d$ are scalars, then following properties are true:
(i) Commutative property w.r.t. addition: $A+B=B+A$
(ii) Associative property w.r.t. addition: $(A+B)+C=A+(B+C)$
(iii) Associative property of scalar multiplication: $(c d) A=c(d A)$
(iv) Existence of additive identity: $A+O=O+A=A \quad \begin{cases}O \text { is null matrix and } \\ A \text { is a square matrix }\end{cases}$
(v) Existence of multiplicative identity: $I A=A I=A \quad$ (I is unit/identity matrix)
(vi) Distributive property w.r.t scalar multiplication:
(a) $c(A+B)=c A+c B$
(b) $(c+d) A=c A+d A$
(vii) Associative property w.r.t. multiplication: $A(B C)=(A B) C$
(viii) Left distributive property: $A(B+C)=A B+A C$
(ix) Right distributive property: $(A+B) C=A C+B C$
(x) $c(A B)=(c A) B=A(c B)$

Example 3 Find $A B$ and $B A$ if $A=\left[\begin{array}{lll}2 & 0 & 1 \\ 1 & 4 & 2 \\ 3 & 0 & 6\end{array}\right]$ and $B=\left[\begin{array}{rrr}1 & -1 & 0 \\ 2 & 3 & -1 \\ 1 & -2 & 3\end{array}\right]$
Solution $A B=\left[\begin{array}{lll}2 & 0 & 1 \\ 1 & 4 & 2 \\ 3 & 0 & 6\end{array}\right]\left[\begin{array}{rrr}1 & -1 & 0 \\ 2 & 3 & -1 \\ 1 & -2 & 3\end{array}\right]$

$$
\begin{aligned}
& =\left[\begin{array}{rrr}
2 \times 1+0 \times 2+1 \times 1 & 2 \times(-1)+0 \times 3+1 \times(-2) & 2 \times 0+0 \times(-1)+1 \times 3 \\
1 \times 1+4 \times 2+2 \times 1 & 1 \times(-1)+4 \times 3+2 \times(-2) & 1 \times 0+4 \times(-1)+2 \times 3 \\
3 \times 1+0 \times 2+6 \times 1 & 3 \times(-1)+0 \times 3+6 \times(-2) & 3 \times 0+0 \times(-1)+6 \times 3
\end{array}\right] \\
& =\left[\begin{array}{rrr}
3 & -4 & 3 \\
11 & 7 & 2 \\
9 & -15 & 18
\end{array}\right] \\
& B A=\left[\begin{array}{rrr}
1 & -1 & 0 \\
2 & 3 & -1 \\
1 & -2 & 3
\end{array}\right]\left[\begin{array}{lll}
2 & 0 & 1 \\
1 & 4 & 2 \\
3 & 0 & 6
\end{array}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\left[\begin{array}{l}
1 \times 2+(-1) \times 1+0 \times 3 \quad 1 \times 0+(-1) \times 4+0 \times 0 \quad 1 \times 1+(-1) \times 2+0 \times 6 \\
2 \times 2+3 \times 1+(-1) \times 3 \quad 2 \times 0+3 \times 4+(-1) \times 0 \quad 2 \times 1+3 \times 2+(-1) \times 6 \\
1 \times 2+(-2) \times 1+3 \times 3 \quad 1 \times 0+(-2) \times 4+3 \times 0 \quad 1 \times 1+(-2) \times 2+3 \times 6
\end{array}\right] \\
& =\left[\begin{array}{rrr}
1 & -4 & -1 \\
4 & 12 & 2 \\
9 & -8 & 15
\end{array}\right]
\end{aligned}
$$

Note
Matrix multiplication is not commutative in general.

Thus, from (i) and (ii), $A B \neq B A$

# EXERCISE 4.1

1. If $A=\left[a_{i j}\right]_{i=1}$, then show that
(i) $I_{2} A=A$
(ii) $A I_{4}=A$
2. If $A=\left[\begin{array}{lll}0 & -1 & 2 \\ 3 & 2 & 1 \\ -1 & 0 & 4\end{array}\right], B=\left[\begin{array}{llll}2 & 1 & -1 \\ 1 & 2 & 4 \\ -1 & 2 & 1\end{array}\right]$ and $C=\left[\begin{array}{llll}1 & 0 & -2 \\ -1 & 5 & 0 \\ 3 & 4 & -1\end{array}\right]$, then find
(i) $A-B$
(ii) B-C
(iii) $(A-B)-C$
(iv) $A-(B-C)$
3. If $A=\left[\begin{array}{lll}i & 2 i \\ 1 & -i\end{array}\right], B=\left[\begin{array}{cc}-i & 1 \\ 2 i & 1\end{array}\right]$ and $C=\left[\begin{array}{cc}2 i & 1 \\ -i & i\end{array}\right]$, then show that
(i) $(A B) C=A(B C)$
(ii) $A(B+C)=A B+A C$
4. If $A$ and $B$ are square matrices of the same order, then explain why in general;
(i) $(A+B)^{2} \neq A^{2}+2 A B+B^{2}$
(ii) $(A-B)^{2} \neq A^{2}-2 A B+B^{2}$
(iii) $(A+B)(A-B) \neq A^{2}-B^{2}$
5. If $A=\left[\begin{array}{ccc}-1 & 2 & 3 \\ 1 & 0 & 2 \\ -3 & 5 & 3\end{array}\right]$, then find $A+A^{t}, A-A^{t}, A A^{t}, A^{t} A$ and $\left(A^{t}\right)^{t}$.
6. Solve the matrix equation $A^{2}-5 A+4 I-X=0$ if $A=\left[\begin{array}{lll}2 & 0 & 1 \\ 2 & 1 & 3 \\ 1 & -1 & 0\end{array}\right]$
7. If $A$ and $B$ are two matrices such that $A B=B$ and $B A=A$, show that $A^{2}+B^{2}=A+B$.