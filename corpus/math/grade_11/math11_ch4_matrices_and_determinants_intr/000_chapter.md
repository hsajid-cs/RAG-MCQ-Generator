# Chapter
# 4

## Matrices and Determinants

## INTRODUCTION

This unit introduces the fundamental concepts and operations of matrices, equipping students with the skills to perform matrix addition, subtraction and multiplication involving both real and complex entries. It explores the essential properties of determinants and provides techniques for evaluating the determinant of a $3 \times 3$ matrix using cofactors and determinant properties. Students will learn to apply row operations to determine the inverse and rank of matrices, as well as distinguish between consistent and inconsistent systems of linear equations through practical examples. The unit further explores into solving systems of linear equations, both homogeneous and non-homogeneous, using advanced methods such as matrix inversion, Cramer's Rule and Gaussian elimination. Emphasis is placed on the realworld applications of matrices in diverse fields such as graphic design, cryptography, data encryption, geometric transformations and highlighting the importance and versatility of matrix algebra in solving complex, practical problems.

### 4.1 Matrix

While solving linear systems of equations, a new notation was introduced to reduce the amount of writing. For this new notation the word matrix was first used by the English mathematician James Sylvester (1814 - 1897). Arthur Cayley (1821 - 1895) developed the theory of matrices and used them in the linear transformations. Now-adays, matrices are used in high speed computers and also in other various disciplines. The concept of determinants was used by Chinese and Japanese mathematicians but the Japanese mathematician Seki Kowa (1642-1708) and the German Mathematician Gottfried Wilhelm Leibniz (1646-1716) are credited for the invention of determinants. G. Cramer (1704-1752) employed the determinants successfully for solving the systems of linear equations.
A rectangular array of numbers enclosed by a pair of bracket is called a matrix such as:

$$
\left[\begin{array}{ccc}
2 & -1 & 3 \\
-5 & 4 & 7
\end{array}\right] \quad \text { (i) } \quad \text { or } \quad\left[\begin{array}{ccc}
2 & 3 & 0 \\
1 & -1 & 4 \\
3 & 2 & 6 \\
4 & 1 & -1
\end{array}\right]
$$

called columns. The numbers used in rows or columns are said to be the entries or elements of the matrix.
The matrix in (i) has two rows and three columns while the matrix in (ii) has four rows and three columns. Note that the number of the elements of the matrix in (ii) is $4 \times 3=12$. Now the general definition of a matrix is:
Generally, a bracketed rectangular array of $m \cdot n$ elements $a_{i j}\left(1,2,3, \ldots, m\right.$; $j=1,2,3, \ldots, n$ ), arranged in $m$ rows and $n$ columns such as:
is called an $m$ by $n$ matrix (written as $m \times n$ matrix), where $m \times n$ is called the order of the matrix in (iii). The matrices are usually represented by the capital letters such as $A, B, C, X, Y$, etc., and small letters such as $a, b, c, l, m, n$, or $a_{11}, a_{12}, a_{13}, \ldots$, etc., are used to indicate the entries of the matrices.
Let the matrix in (iii) be denoted by $A$. The $i$ th row and the $j$ th column of $A$ are indicated in the following tabular representation of $A$.
The elements of the $i$ th row of $A$ are $a_{i 1} a_{i 2} a_{i 3} \ldots a_{i j} \ldots a_{i n}$ while the elements of the $j$ th column of $A$ are $a_{1 j} a_{2 j} a_{3 j} \ldots a_{i j} \ldots a_{m j}$. We note that $a_{i j}$ is the element of the $i$ th row and $j$ th column of $A$. The double subscripts are useful to name the elements of the matrices. For example, the element 7 is at $a_{23}$ position in the matrix $\left[\begin{array}{ccc}2 & -1 & 3 \\ -5 & 4 & 7\end{array}\right]$. For convenience, we shall write the matrix $A$ as:

$A=\left[a_{i j}\right]_{m \times n}$ or $A=\left[a_{i j}\right]$, for $i=1,2,3, \ldots, m ; j=1,2,3, \ldots, n$, where $a_{i j}$ is the element of the $i$ th row and $j$ th column of $A$.
The elements (entries) of matrices need not always be numbers but in the study of matrices, we shall take the elements of the

## Note

The matrix $A$ is called real matrix if all of its elements are real.
matrices from $R$ or $C$.
Row Matrix or Row vector: A matrix, which has only one row, i.e., $1 \times n$ matrix of the form $\left[\begin{array}{llll}a_{i 1} & a_{i 2} & a_{i 3} & \ldots & a_{i n}\end{array}\right]$ is said to be a row matrix or a row vector.
Column Matrix or Column Vector: A matrix which has only one column i.e., an $m \times 1$ matrix of the form $\left[\begin{array}{c}a_{1 j} \\ a_{2 j} \\ a_{3 j} \\ \vdots \\ a_{m j}\end{array}\right]$ is said to be a column matrix or a column vector.

For example [1-1 3 4] is a row matrix having 4 columns and $\left[\begin{array}{l}2 \\ -1 \\ 3\end{array}\right]$ is a column matrix having 3 rows.
Rectangular Matrix: If $m \neq n$, then the matrix is called a rectangular matrix of order $m \times n$, that is, the matrix in which the number of rows is not equal to the number of columns, is said to be a rectangular matrix. For example;
$\left[\begin{array}{lll}2 & 3 & 1 \\ -1 & 0 & 4\end{array}\right]$ and $\left[\begin{array}{rrr}2 & -3 & 0 \\ 1 & 2 & 4 \\ 3 & -1 & 5 \\ 0 & 1 & 2\end{array}\right]$ are rectangular matrices of orders $2 \times 3$ and $4 \times 3$ respectively.
Square Matrix: If $m=n$, then the matrix of order $m \times n$ is said to be a square matrix of order $n$ or $m$. i.e., the matrix which has the same number of rows and columns is called a square matrix. For example: $[0],\left[\begin{array}{rr}2 & 5 \\ -1 & 6\end{array}\right]$ and $\left[\begin{array}{rrr}1 & 1 & 2 \\ 2 & -1 & 8 \\ 3 & 5 & 4\end{array}\right]$ are square matrices of orders 1,2 and 3 respectively.

Let $A=\left[a_{i j}\right]$ be a square matrix of order $n$, then the entries $a_{11}, a_{22}, a_{33}, \ldots, a_{n n}$ form the principal diagonal for the matrix $A$ and the entries $a_{1 n}, a_{2 n-1}, a_{3 n-2}, \ldots, a_{n-12}, a_{n 1}$ form the secondary diagonal for the matrix $A$. For example, in the matrix

$$
\left[\begin{array}{llll}
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
a_{31} & a_{32} & a_{33} & a_{34} \\
a_{41} & a_{42} & a_{43} & a_{44}
\end{array}\right], \text { the entries of the principal diagonal are } a_{11}, a_{22}, a_{33}, a_{44} \text { and the }
$$

entries of the secondary diagonal are $a_{14}, a_{23}, a_{32}, a_{41}$.
The principal diagonal of a square matrix is also called the leading diagonal or main diagonal of the matrix.
Diagonal Matrix: Let $A=\left[a_{i j}\right]$ be a square matrix of order $n$.
If $a_{i j}=0$ for all $i \neq j$ and at least one $a_{i j} \neq 0$ for $i=j$, that is, some elements of the principal diagonal of $A$ may be zero but not all, then the matrix $A$ is called a diagonal matrix. The matrices

$$
[7],\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 5
\end{array}\right] \text { and }\left[\begin{array}{llll}
0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 2 & 0 \\
0 & 0 & 0 & 4
\end{array}\right] \text { are diagonal matrices. }
$$

Scalar Matrix: Let $A=\left[a_{i j}\right]$ be a square matrix of order $n$.
If $a_{i j}=0$ for all $i \neq j$ and $a_{i j}=k$ (some non-zero scalar) for all $i=j$, then the matrix $A$ is called a scalar matrix of order $n$. For example:
$\left[\begin{array}{ll}7 & 0 \\ 0 & 7\end{array}\right],\left[\begin{array}{llll}a & 0 & 0 \\ 0 & a & 0 \\ 0 & 0 & a\end{array}\right](a \neq 0)$ and $\left[\begin{array}{llll}3 & 0 & 0 & 0 \\ 0 & 3 & 0 & 0 \\ 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 3\end{array}\right]$ are scalar matrices of order 2,3 and 4 respectively.
Unit Matrix or Identity Matrix: Let $A=\left[a_{i j}\right]$ be a square matrix of order $n$. If $a_{i j}=0$ for all $i \neq j$ and $a_{i j}=1$ for all $i=j$, then the matrix $A$ is called a unit matrix or identity matrix of order $n$. We denote such a matrix by $I_{n}$ or simply $I$ and it is of the form:

$$
I_{n}=\left[\begin{array}{ccccc}
1 & 0 & 0 & \cdots & 0 \\
0 & 1 & 0 & \cdots & 0 \\
0 & 0 & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & & \vdots \\
0 & 0 & 0 & \cdots & 1
\end{array}\right]
$$

The identity matrix of order 3 is denoted by $I_{3}$, that is, $I_{3}=\left[\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right]$
Null Matrix or Zero Matrix: A square or rectangular matrix whose each element is zero, is called a null or zero matrix. An $m \times n$ matrix with all its elements equal to zero, is denoted by $O_{m \times n}$. Null matrices may be of any order. Here are some examples:
$[0],\left[\begin{array}{llll}0 & 0 & 0 & 0\end{array}\right],\left[\begin{array}{llll}0 & 0 & 0 \\ 0 & 0 & 0\end{array}\right],\left[\begin{array}{lll}0 & 0 \\ 0 & 0\end{array}\right],\left[\begin{array}{l}0 \\ 0 \\ 0\end{array}\right],\left[\begin{array}{llll}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{array}\right]$
Note
$O$ may be used to denote null matrix of any order if there is no confusion.
are null matrices of order $1,1 \times 3,2 \times 3,2 \times 2,3 \times 1,3 \times 4$ respectively.
Equal Matrices: Two matrices of the same order are said to be equal if their corresponding entries are equal. For example, $A=\left[a_{i j}\right]_{m \times n}$ and $B=\left[b_{i j}\right]_{m \times n}$ are equal, i.e., $A=B$ iff $a_{i j}=b_{i j}$ for $i=1,2,3, \ldots, m, j=1,2,3, \ldots, n$. In other words, $A$ and $B$ represent the same matrix.
Transpose of a Matrix: If $A$ is a matrix of order $m \times n$ then an $n \times m$ matrix obtained by interchanging the rows and columns of $A$, is called the transpose of $A$. It is denoted by $A^{t}$. Let $A=\left[a_{i j}\right]_{m \times n}$, then the transpose of $A$ is defined as:

$$
A^{t}=\left[a_{i j}^{t}\right]_{m \times n} \text { where } a_{i j}^{t}=a_{j i} \text { for } i=1,2,3, \ldots, n \text { and } j=1,2,3, \ldots, m
$$

For example, if $B=\left[b_{i j}\right]_{3 \times 4}=\left[\begin{array}{llll}b_{11} & b_{12} & b_{13} & b_{14} \\ b_{21} & b_{22} & b_{23} & b_{24} \\ b_{31} & b_{32} & b_{33} & b_{34}\end{array}\right]$, then
$B^{t}=\left[b_{i j}^{t}\right]_{4 \times 3}$ where $b_{i j}^{t}=b_{j i}$ for $i=1,2,3,4$ and $j=1,2,3$ i.e.,

$$
B^{t}=\left[\begin{array}{lll}
b_{11}^{t} & b_{12}^{t} & b_{13}^{t} \\
b_{21}^{t} & b_{22}^{t} & b_{23}^{t} \\
b_{31}^{t} & b_{32}^{t} & b_{33}^{t} \\
b_{41}^{t} & b_{42}^{t} & b_{43}^{t}
\end{array}\right]=\left[\begin{array}{lll}
b_{11} & b_{21} & b_{31} \\
b_{12} & b_{22} & b_{32} \\
b_{13} & b_{23} & b_{33} \\
b_{14} & b_{24} & b_{34}
\end{array}\right]
$$

Note that the $2^{\text {nd }}$ row of $B$ has the same entries respectively as the $2^{\text {nd }}$ column of $B^{t}$ and the $3^{\text {rd }}$ row of $B^{t}$ has the same entries respectively as the $3^{\text {rd }}$ column of $B$ etc.

# 4.2 Matrix Operations

Matrix operations involve various techniques and procedures applied to matrices. These operations are foundational in linear algebra and have applications in numerous fields such as computer graphics, physics, statistics, etc. Here are some key matrix operations:

### 4.2.1 Addition of Matrices

Two matrices are conformable for addition if they are of the same order.
The sum $A+B$ of two $m \times n$, matrices $A=\left[a_{i j}\right]$ and $B=\left[b_{i j}\right]$ is the $m \times n$ matrix $C=\left[c_{i j}\right]$ formed by adding the corresponding entries of $A$ and $B$ together. In symbols, we write as $C=A+B$, that is:

$$
\left[c_{i j}\right]=\left[a_{i j}+b_{i j}\right] \text { where } c_{i j}=a_{i j}+b_{i j} \text { for } i=1,2,3, \ldots, m ; j=1,2,3, \ldots, n
$$

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

### 4.4 Determinants

The determinants of square matrices of order $n \geq 3$, can be written by the following pattern. For example, if $n=3$

$A=\left[\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right]$, then the determinant of $A=|A|=\left|\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right|$
Now our aim is to compute the determinants of matrices of various orders.

# 4.4.1 Minor and Cofactor of an Element of a Matrix or its Determinant Minor of an Element: Let us consider a square matrix $A$ of order $n$, then the minor of an element $a_{i j}$, denoted by $M_{i j}$ is the determinant formed by deleting the $i$ th row and the $j$ th column of $A($ or $|A|)$.

For example, consider a square matrix $A$ of order $3, A=\left[\begin{array}{llll}a_{11} & a_{13} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right]$
To find the minor of the element $a_{12}$, delete the first row and second column of $A$

$$
\left[\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right], \text { that is } M_{12}=\left|\begin{array}{ll}
a_{21} & a_{23} \\
a_{31} & a_{33}
\end{array}\right|
$$

Cofactor of an Element: The cofactor of an element $a_{i j}$ of a square matrix $A$ denoted by $A_{i j}$ is defined by $A_{i j}=(-1)^{i+j} M_{i j}$
For example, $A_{12}=(-1)^{1 / 2} M_{13}=(-1)^{3}\left|\begin{array}{ll}a_{21} & a_{23} \\ a_{31} & a_{33}\end{array}\right|=-\left|\begin{array}{ll}a_{21} & a_{23} \\ a_{31} & a_{33}\end{array}\right|$

### 4.4.2 Determinant of a Square Matrix of Order $n=3$

If $A$ is a matrix of order 3 , that is, $A=\left[\begin{array}{llll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right]$, then:

$$
|A|=a_{i 1} A_{i 1}+a_{i 2} A_{i 2}+a_{i 3} A_{i 3} \quad \text { for } i=1,2,3
$$

or $|A|=a_{1 j} A_{1 j}+a_{2 j} A_{2 j}+a_{3 j} A_{3 j}$ for $j=1,2,3$
For example, for $i=1, j=1$ and $j=2$, we have

$$
\begin{aligned}
& |A|=a_{11} A_{11}+a_{12} A_{12}+a_{13} A_{13} \\
& \text { or }|A|=a_{11} A_{11}+a_{21} A_{21}+a_{31} A_{31} \\
& \text { or }|A|=a_{12} A_{12}+a_{22} A_{22}+a_{32} A_{32}
\end{aligned}
$$

(iii) can be written as: $|A|=a_{12}(-1)^{1 / 2} M_{12}+a_{22}(-1)^{2 / 2} M_{22}+a_{32}(-1)^{3 / 2} M_{32}$

i.e., $|A|=-a_{12} M_{12}+a_{23} M_{23}-a_{32} M_{32}$
Similarly (i) can be written as $|A|=a_{11} M_{11}-a_{12} M_{12}+a_{13} M_{13}$
Putting the values of $M_{11}, M_{12}$ and $M_{13}$ in (v), we obtain

$$
\begin{aligned}
& |A|=\left.a_{11}\right|_{a_{32}} ^{a_{23}}\left.a_{33}\right|_{-a_{12}}\left|\begin{array}{ll}
a_{21} & a_{33} \\
a_{31} & a_{33}
\end{array}\right|+a_{13}\left|\begin{array}{ll}
a_{21} & a_{32} \\
a_{31} & a_{32}
\end{array}\right| \\
& \text { or }|A|=a_{11}\left(a_{22} a_{33}-a_{23} a_{32}\right)-a_{12}\left(a_{21} a_{33}-a_{22} a_{31}\right)+a_{13}\left(a_{21} a_{32}-a_{22} a_{31}\right) \\
& \text { or }|A|=a_{11} a_{22} a_{33}+a_{12} a_{23} a_{31}+a_{13} a_{21} a_{32}-a_{11} a_{23} a_{32}-a_{12} a_{21} a_{33}-a_{13} a_{22} a_{31}
\end{aligned}
$$

Equation (vii) is the required expansion of determinant of square matrix of order 3.
Example 4 Evaluate the determinant if $A=\left[\begin{array}{rrr}1 & -2 & 3 \\ -2 & 3 & 1 \\ 4 & -3 & 2\end{array}\right]$.

Solution $|A|=\left|\begin{array}{rrr}1 & -2 & 3 \\ -2 & 3 & 1 \\ 4 & -3 & 2\end{array}\right|$
using

$$
\begin{aligned}
|A| & =a_{11} M_{11}-a_{12} M_{12}+a_{13} M_{13}, \text { we get } \\
|A| & =1\left|\begin{array}{rr}
3 & 1 \\
-3 & 2
\end{array}\right|-(-2)\left|\begin{array}{rr}
-2 & 3 \\
4 & 2
\end{array}\right|+3\left|\begin{array}{rr}
-2 & 3 \\
4 & -3
\end{array}\right| \\
& =1(6-1(-3)]+2[(-2)(2)-(1)(4)]+3[(-2)(-3)-12] \\
& =(6+3)+2(-4-4)+3(6-12)=9-16-18=-25
\end{aligned}
$$

Example 5 Find the cofactors $A_{12}, A_{22}$ and $A_{32}$ of $A=\left[\begin{array}{rrr}1 & -2 & 3 \\ -2 & 3 & 1 \\ 4 & -3 & 2\end{array}\right]$ and find $|A|$.
Solution We first find $M_{12}, M_{22}$ and $M_{32}$,

$$
\begin{aligned}
& M_{12}=\left|\begin{array}{rr}
-2 & 1 \\
4 & 2
\end{array}\right|=-4-4=-8 ; M_{22}=\left|\begin{array}{ll}
1 & 3 \\
4 & 2
\end{array}\right|=2-12=-10 \\
& \text { and } \quad M_{32}=\left|\begin{array}{rr}
1 & 3 \\
-2 & 1
\end{array}\right|=1-(-6)=7 \\
& \text { Thus } \quad A_{12}=(-1)^{1+2} M_{12}=(-1)(-8)=8 ; \quad A_{22}=(-1)^{2+2} M_{22}=1(-10)=-10 \\
& A_{32}=(-1)^{3+2} M_{32}=(-1)(7)=-7 \\
& \text { and } \quad|A|=a_{12} A_{12}+a_{22} A_{22}+a_{33} A_{33}=(-2) 8+3(-10)+(-3)(-7) \\
& \quad=-16-30+21=-25
\end{aligned}
$$

# 4.4.3 Properties of Determinants

i. For a square matrix $A,|A|=|A|$
ii. If in a square matrix $A$, two rows or two columns are interchanged, the determinant of the resulting matrix is $-|A|$.
iii. If a square matrix $A$ has two identical rows or two identical columns, then $|A|=0$.
iv. If all the entries of a row (or a column) of a square matrix $A$ are zero, then $|A|=0$.
v. If the entries of a row (or a column) in a square matrix $A$ are multiplied by a number $k \in R$, then the determinant of the resulting matrix is $k|A|$.
vi. If each entry of a row (or a column) of a square matrix consists of two terms, then its determinant can be written as the sum of two determinants, i.e., if

$$
\begin{aligned}
& B=\left[\begin{array}{lll}
a_{11}+b_{11} & a_{12} & a_{13} \\
a_{21}+b_{21} & a_{22} & a_{23} \\
a_{31}+b_{31} & a_{32} & a_{33}
\end{array}\right], \text { then } \\
& |B|=\left|\begin{array}{lll}
a_{11}+b_{11} & a_{12} & a_{13} \\
a_{21}+b_{21} & a_{22} & a_{23}
\end{array}\right|=\left|\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23}
\end{array}\right|+\left|\begin{array}{lll}
b_{11} & a_{12} & a_{13} \\
b_{21} & a_{22} & a_{23}
\end{array}\right| \\
& a_{31}+b_{31} \quad a_{32} \quad a_{33}
\end{aligned}
$$

vii. If any row (column) of a determinant is multiplied by a non-zero number $k$ and the result is added to the corresponding entries of another row (column), the value of the determinant does not change.
viii. If a matrix is in triangular form, then the value of its determinant is the product of the entries on its main diagonal.

## Note We shall define triangular matrices on page 61.

Example 6 Without expansion, show that $\left|\begin{array}{lll}x & a+x & b+c \\ x & b+x & c+a \\ x & c+x & a+b\end{array}\right|$
Solution Adding the entries of $C_{3}$ to the corresponding entries of $C_{2}$.
L.H.S $=\left|\begin{array}{lll}x & a+b+c+x & b+c \\ x & a+b+c+x & c+a \\ x & a+b+c+x & a+b\end{array}\right|$

$$
\begin{aligned}
& =x(a+b+c+x)\left|\begin{array}{lll}
1 & 1 & b+c \\
1 & 1 & c+a \\
1 & 1 & a+b
\end{array}\right| \quad\left(\begin{array}{lll}
\text { by taking } x \text { common from } C_{1} \text { and } \\
(a+b+c+x) \text { common from } C_{2}
\end{array}\right) \\
& =x(a+b+c+x) \cdot 0 \quad\left(\because C_{1} \text { and } C_{2} \text { are identical }\right) \\
& =0=\text { R.H.S }
\end{aligned}
$$

# 4.5 Adjoint and Inverse of a Square Matrix

Let $A=\left[\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right]$, then the matrix of co-factors of $A=\left[\begin{array}{lll}A_{11} & A_{12} & A_{13} \\ A_{21} & A_{22} & A_{23} \\ A_{31} & A_{32} & A_{33}\end{array}\right]$,
and adj $A=\left[\begin{array}{lll}A_{11} & A_{21} & A_{31} \\ A_{12} & A_{22} & A_{32} \\ A_{13} & A_{23} & A_{33}\end{array}\right]$
Inverse of a Square Matrix of Order $n \geq 3$ : Let $A$ be a non singular $(|A| \neq 0)$ square matrix of order $n$. If there exists a matrix $B$ such that $A B=B A=I_{n}$, then $B$ is called the multiplicative inverse of $A$ and is denoted by $A^{-1}$. It is obvious that the order of $A^{-1}$ is $n \times n$.
Thus, $A A^{-1}=I_{n}$ and $A^{-1} A=I_{n}$.
If $A$ is non singular matrix then

$$
A^{-1}=\frac{1}{|A|} \operatorname{adj} A
$$

Example 7 Find $A^{-1}$ if $A=\left[\begin{array}{ccc}1 & 0 & 2 \\ 0 & 2 & 1 \\ 1 & -1 & 1\end{array}\right]$.
Solution We first find the cofactors of the elements of $A$.
$A_{11}=(-1)^{1+1}\left|\begin{array}{cc}2 & 1 \\ -1 & 1\end{array}\right|=1 \cdot(2+1)=3, \quad A_{12}=(-1)^{1+2}\left|\begin{array}{ll}0 & 1 \\ 1 & 1\end{array}\right|=(-1)(-1)=1$
$A_{13}=(-1)^{1+3}\left|\begin{array}{ll}0 & 2 \\ 1 & -1\end{array}\right|=1 \cdot(0-2)=-2, \quad A_{21}=(-1)^{2+1}\left|\begin{array}{cc}0 & 2 \\ -1 & 1\end{array}\right|=(-1)(0+2)=-2$
$A_{22}=(-1)^{2+2}\left|\begin{array}{ll}1 & 2 \\ 1 & 1\end{array}\right|=1 \cdot(1-2)=-1, \quad A_{23}=(-1)^{2+3}\left|\begin{array}{cc}1 & 0 \\ 1 & -1\end{array}\right|=(-1)(-1-0)=1$
$A_{31}=(-1)^{3+1}\left|\begin{array}{ll}0 & 2 \\ 2 & 1\end{array}\right|=1 \cdot(0-4)=-4, \quad A_{32}=(-1)^{3+2}\left|\begin{array}{ll}1 & 2 \\ 0 & 1\end{array}\right|=(-1)(1-0)=-1$
$A_{33}=(-1)^{3+3}\left|\begin{array}{ll}1 & 0 \\ 0 & 2\end{array}\right|=1 \cdot(2-0)=2$

Thus

$$
\left[A_{i j}\right]_{3 \times 3}=\left[\begin{array}{lll}
A_{11} & A_{12} & A_{13} \\
A_{21} & A_{22} & A_{23} \\
A_{31} & A_{32} & A_{33}
\end{array}\right]=\left[\begin{array}{rrr}
3 & 1 & -2 \\
-2 & -1 & 1 \\
-4 & -1 & 2
\end{array}\right]
$$

and adj $A=\left[A_{i j}\right]_{3 \times 3}=\left[\begin{array}{rrr}3 & -2 & -4 \\ 1 & -1 & -1 \\ -2 & 1 & 2\end{array}\right] \quad\left(\because A_{i j}^{\prime}=A_{j i}\right.$ for $\left.i, j=1,2,3\right)$
Since

$$
\begin{aligned}
|A| & =a_{11} A_{11}+a_{12} A_{12}+a_{13} A_{13} \\
& =1(3)+0(1)+2(-2) \\
& =3+0-4=-1
\end{aligned}
$$

So

$$
A^{-1}=\frac{1}{|A|} \operatorname{adj} A=\frac{1}{-1}\left[\begin{array}{rrr}
3 & -2 & -4 \\
1 & -1 & -1 \\
-2 & 1 & 2
\end{array}\right]=\left[\begin{array}{rrr}
-3 & 2 & 4 \\
-1 & 1 & 1 \\
2 & -1 & -2
\end{array}\right]
$$

# EXERCISE 4.2

1. Evaluate the following determinants
(i) $\left|\begin{array}{rrr}1 & -2 & -4 \\ 3 & -1 & -3 \\ -2 & 3 & 2\end{array}\right|$
(ii) $\left|\begin{array}{llll}a+b & a-b & a \\ a & a+b & a-b \\ a-b & a & a+b\end{array}\right|$
(iii) $\left|\begin{array}{llll}2 x & x & x \\ y & 2 y & y \\ z & z & 2 z\end{array}\right|$
2. Without expansion, alow that:
(i) $\left|\begin{array}{llll}7 & 8 & 9 \\ 5 & 6 & 7 \\ 2 & 3 & 4\end{array}\right|=0$
(ii) $\left|\begin{array}{llll}5 & 6 & -1 \\ 2 & 2 & 0 \\ 2 & -8 & 10\end{array}\right|=0$
(iii) $\left|\begin{array}{ccc}-a & 0 & b \\ 0 & a & -c \\ c & -b & 0\end{array}\right|=0$
(iv) $\left|\begin{array}{lllllll}l & m+n & 1 & =0 & (v) & \left|\begin{array}{lllll}2 & 1 & 3 x \\ 2 & 3 & 9 x \\ 3 & 5 & 15 x\end{array}\right|=0 & (v) & \left|\begin{array}{lllll}b c & a & a^{2} \\ c a & b & b^{2} \\ a b & c & c^{2}\end{array}\right|=\left|\begin{array}{lllll}1 & a^{2} & a^{3} \\ 1 & b^{2} & b^{3} \\ 1 & c^{2} & c^{3}\end{array}\right|$
3. Using properties of determinants, show that:
(i) $\left|\begin{array}{lllll}3 & 5 & 0 \\ 5 & 25 & 10\end{array}\right|=25\left|\begin{array}{lllll}3 & 1 & 0 \\ 1 & 1 & 2 \\ 7 & 25 & 1\end{array}\right|$
(ii) $\left|\begin{array}{ccc}a+x & a & a \\ a & a+x & a \\ a & a & a+x\end{array}\right|=x^{3}(3 a+x)$

(iii) $\left|\begin{array}{lll}1 & x & y z \\ 1 & y & z x \\ 1 & z & x y\end{array}\right|=\left|\begin{array}{ccc}1 & x & x^{2} \\ 1 & y & y^{2} \\ 1 & z & z^{2}\end{array}\right|$
(iv) $\left|\begin{array}{ccc}1 & x & x^{2} \\ 1 & y & y^{2} \\ 1 & z & z^{2}\end{array}\right|=(x-y)(y-z)(z-x)$
(v) $\left|\begin{array}{ccc}1 & 1 & 1 \\ a+1 & b+1 & c+1 \\ (a+1)^{2} & (b+1)^{2} & (c+1)^{2}\end{array}\right|=(a-b)(b-c)(c-a)$
(vi) $\left|\begin{array}{ccc}a^{2}+b^{2} & c^{2} & c^{2} \\ a^{2} & b^{2}+c^{2} & a^{2} \\ b^{2} & b^{2} & c^{2}+a^{2}\end{array}\right|=4 a^{2} b^{2} c^{2}$
(vii) $\left|\begin{array}{ccc}a & b & c \\ b+c & c+a & a+b \\ a+b & b+c & c+a\end{array}\right|=a^{3}+b^{3}+c^{3}-3 a b c$
(viii) $\left|\begin{array}{ccc}a+t & a & a \\ b & b+t & b \\ c & c & c+t\end{array}\right|=t^{2}(a+b+c+t)$
(ix) $\left|\begin{array}{ccc}a-b-c & 2 a & 2 a \\ 2 b & b-c-a & 2 b \\ 2 c & 2 c & c-a-b\end{array}\right|=(a+b+c)^{3}$
(x) $\left|\begin{array}{ccc}y+z & z+x & x+y \\ x & y & z \\ x^{2} & y^{2} & z^{2}\end{array}\right|=(x+y+z)(x-y)(y-z)(z-x)$
(xi) $\left|\begin{array}{ccc}1 & 1 & 1 \\ a^{2}+1 & b^{2}+1 & c^{2}+1 \\ a^{2}+a & b^{2}+b & c^{3}+c\end{array}\right|=(a-b)(b-c)(c-a)(a b+b c+c a-1)$
(xii) $\left|\begin{array}{ccc}1+a & 1 & 1 \\ 1 & 1+b & 1 \\ 1 & 1 & 1+c\end{array}\right|=a b c+a b+b c+c a \quad$ (xiii) $\left|\begin{array}{ccc}1 & a & a^{2}-b c \\ 1 & b & b^{2}-c a \\ 1 & c & c^{2}-a b\end{array}\right|=0$

(a) Matrices and Determinants
(2) Mathemathes (1)
$(x i v)$ | $2 x+3$ | $x+2$ | $x+a$ |
| :-- | :-- | :-- |
| $2 x+5$ | $x+3$ | $x+b=0$, where $2 b=a+c$ |
| $2 x+7$ | $x+4$ | $x+c \mid$ |

(xv) | $a$ | $b$ | $c$ |
| :-- | :-- | :-- |
| $c$ | $a$ | $b \mid=(a+b+c)\left(a+b \omega+c \omega^{2}\right)\left(a+b \omega^{2}+c \omega\right)$, where $\omega$ is an |
| $b$ | $c$ | $a \mid$ |

imaginary cube root of unity.
4. If $A=\left[\begin{array}{ccc}1 & 2 & -3 \\ 0 & -5 & 0 \\ -2 & -2 & 7\end{array}\right]$ and $B=\left[\begin{array}{ccc}-5 & -2 & 5 \\ -3 & -1 & 4 \\ -2 & -1 & 2\end{array}\right]$, then find:
(i) $A_{13}, A_{23}, A_{33}$ and $|A|$
(ii) $B_{31}, B_{32}, B_{33}$ and $|B|$
5. Find the values of $x$ if:
(i) $\left|\begin{array}{ccc}2 & 1 & x \\ -1 & -4 & -3 \\ x & 1 & 0\end{array}\right|=5$
(ii) $\left|\begin{array}{ccc}1 & x-1 & 3 \\ -1 & x+1 & 2 \\ 2 & -3 & x\end{array}\right|=9$
(iii) $\left|\begin{array}{ccc}1 & 1 & 1 \\ 2 & x & 2 \\ 3 & 6 & x\end{array}\right|=0$
6. Find $\left|A A^{\prime}\right|$ and $|A A|$ if:
(i) $A=\left[\begin{array}{lll}-3 & 2 & -1 \\ 2 & 1 & 3\end{array}\right]$
(ii) $A=\left[\begin{array}{ll}3 & 1 \\ 2 & 2 \\ 1 & 3\end{array}\right]$
7. If $A$ is a square matrix of order 3 , then show that $|k A|=k^{3}|A|$.
8. Find the values of $A$ if $A$ and $B$ are singular.

$$
A=\left[\begin{array}{ccc}
4 & 2 & 3 \\
7 & 1 & 6 \\
2 & 3 & 1
\end{array}\right], \quad B=\left[\begin{array}{ccc}
-2 & 4 & 5 \\
1 & -2 & 1 \\
2 & 1 & 0
\end{array}\right]
$$

9. Find the inverse of $A=\left[\begin{array}{ccc}1 & 2 & 1 \\ -5 & 0 & 4 \\ 5 & 4 & 0\end{array}\right]$ and show that $A^{-1} A=I$,
10. Verify that $(A B)^{\prime}=B^{\prime} A^{\prime}$ if:
(i) $A=\left[\begin{array}{ccc}1 & -1 & 2 \\ 0 & -3 & 1\end{array}\right]$ and $B=\left[\begin{array}{cc}1 & 1 \\ -3 & -2 \\ 0 & 1\end{array}\right]$
(ii) $A=\left[\begin{array}{ll}1 & 2 \\ 1 & 4 \\ 2 & 1\end{array}\right]$ and $B=\left[\begin{array}{cc}1 & -3 \\ -2 & 1\end{array}\right]$

# 4.6 Elementary Row Operations on a Matrix

Usually, a given system of linear equations is reduced to a simple equivalent system by applying elementary operations which are stated as below:
(i) Interchanging two equations.
(ii) Multiplying an equation by a non-zero number.
(iii) Adding a multiple of one equation to another equation.

Corresponding to these three elementary operations, the following elementary row operations are applied to matrices to obtain equivalent matrices:
(i) Interchanging two rows
(ii) Multiplying a row by a non-zero number
(iii) Adding a multiple of one row to another row

Note Matrices $A$ and $B$ are equivalent if $B$ can
Notations that are used to represent row operations for (i) to (iii) are given below:
in turn a finite number of row operations on $A$.

- Interchanging $R_{i}$ and $R_{j}$ is expressed as $R_{i} \leftrightarrow R_{j}$.
- $k$ times $R_{i}$ is denoted by $k R_{i} \rightarrow R_{i}^{\prime}$.
- Adding $k$ times $R_{j}$ to $R_{i}$ is expressed as $R_{i}+k R_{j} \rightarrow R_{i}^{\prime}$
( $R_{i}^{\prime}$ is the new row obtained after applying the row operation).
For equivalent matrices $A$ and $B$, we write $A \underline{B} B$.
If $A \underline{B} B$ then $B \underline{B} A$
Upper Triangular Matrix: A square matrix $A=\left[a_{i j}\right]$ is called an upper triangular matrix if all elements below the principal diagonal are zero, that is,

$$
a_{i j}=0 \text { for all } i>j
$$

Lower Triangulur Matrix: A square matrix $A=\left[a_{i j}\right]$ is said to be lower triangular matrix if all elements above the principal diagonal are zero, that is,

$$
a_{i j} \geqslant 0 \text { for all } i<j
$$

Triangular Matrix: A square matrix $A$ is named as triangular matrix whether it is upper triangular or lower triangular. For example, the matrices

$$
\left[\begin{array}{lll}
1 & 2 & 3 \\
0 & 1 & 4 \\
0 & 0 & 6
\end{array}\right] \text { and }\left[\begin{array}{llll}
1 & 0 & 0 & 0 \\
3 & 2 & 0 & 0 \\
4 & 1 & 5 & 0 \\
-1 & 2 & 3 & 1
\end{array}\right] \text { are triangular matrices of order } 3 \text { and } 4 \text { respectively. }
$$

The first matrix is upper triangular while the second is lower triangular.

## Remember!

Diagonal matrices are both upper triangular and lower triangular.

# 4.7 Echelon and Reduced Echelon Forms of Matrices

In any non-zero row of a matrix, the first non-zero entry is called the leading entry of that row.

## Echelon Form of a Matrix

An $m \times n$ matrix $A$ is called in echelon form if:
(i) The number of zeros before the leading entry is greater than the number zeros in the preceding row.
(ii) Every non-zero row in $A$ precedes every zero row (if any).
(iii) The first non-zero entry (or leading entry) in each row is 1 .

The matrices $\left[\begin{array}{llll}0 & 1 & -2 & 4 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0\end{array}\right]$ and $\left[\begin{array}{llll}1 & 2 & -3 & 4 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 1\end{array}\right]$ are in echelon form

Reduced Echelon Form of a Matrix: An $m \times n$ matrix $A$ is said to be in reduced (row) echelon form if the first non-zero entry (or leading entry) in $R_{i}$ lies in $C_{j}$, then all other entries of $C_{j}$ are zero.

The matrices $\left[\begin{array}{llll}0 & 1 & 0 & 4 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0\end{array}\right]$ and $\left[\begin{array}{llll}1 & 2 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{array}\right]$ are in (row) reduced echelon form.

Example 3 Reduce $\left[\begin{array}{llll}2 & 3 & -1 & 9 \\ 1 & -1 & 2 & -3 \\ 3 & 1 & 3 & 2\end{array}\right]$ to (row) echelon and reduced (row) echelon form.

Solution $\left[\begin{array}{llll}2 & 3 & -1 & 9 \\ 1 & -1 & 2 & -3 \\ 3 & 1 & 3 & 2\end{array}\right], \notin\left[\begin{array}{llll}1 & -1 & 2 & -3 \\ 2 & 3 & -1 & 9 \\ 3 & 1 & 3 & 2\end{array}\right]$ By $R_{1} \leftrightarrow R_{2}$

$$
\begin{aligned}
& \text { B }\left[\begin{array}{llll}
1 & -1 & 2 & -3 \\
0 & 5 & -5 & 15 \\
0 & 4 & -3 & 11
\end{array}\right] \begin{array}{l}
\text { By } R_{2}+(-2) R_{1} \rightarrow R_{2}^{\prime} \\
\text { and } R_{3}+(-3) R_{1} \rightarrow R_{1}^{\prime}
\end{array} \notin\left[\begin{array}{llll}
1 & -1 & 2 & -3 \\
0 & 1 & -1 & 3 \\
0 & 4 & -3 & 11
\end{array}\right] \frac{1}{2} R_{2} \rightarrow R_{2}^{\prime}
\end{aligned}
$$

$$
\begin{aligned}
& \text { 定 }\left[\begin{array}{llll}
1 & -1 & 2 & -3 \\
0 & 1 & -1 & 3 \\
0 & 0 & 1 & -1
\end{array}\right] R_{2}+(-4) R_{2} \rightarrow R_{2}^{\prime} \quad \notin\left[\begin{array}{llll}
1 & 0 & 1 & 0 \\
0 & 1 & -1 & 3 \\
0 & 0 & 1 & -1
\end{array}\right] R_{1}+1 . R_{2} \rightarrow R_{1}^{\prime}
\end{aligned}
$$

$R\left[\begin{array}{llll}1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & -1\end{array}\right]$
Thus $\left[\begin{array}{llll}1 & -1 & 2 & -3 \\ 0 & 1 & -1 & 3 \\ 0 & 0 & 1 & -1\end{array}\right]$ and $\left[\begin{array}{llll}1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & -1\end{array}\right]$ are (row) echelon and reduced (row)
echelon forms of the given matrix respectively.
Inverse of a Matriz: Let $A$ be a non-singular matrix. If the application of elementary row operations on $A: I$ in succession reduces $A$ to $I$, then the resulting matrix is $I: A^{-1}$.

Example 9 Find the inverse of the matrix $A=\left[\begin{array}{llll}2 & 5 & -1 \\ 3 & 4 & 2 \\ 1 & 2 & -2\end{array}\right]$
Solution $|A|=\left|\begin{array}{lll}2 & 5 & -1 \\ 3 & 4 & 2 \\ 1 & 2 & -2\end{array}\right|=2(-8-4)-5(-6-2)-1(6-4)=-24+40-2=40-26=14$
As $|A| \neq 0$, so $A$ is non-singular.
Appending $I_{3}$ on the right of the matrix $A$, we have $\left[\begin{array}{llllll}2 & 5 & -1 & \vdots & 1 & 0 & 0 \\ 3 & 4 & 2 & \vdots & 0 & 1 & 0 \\ 1 & 2 & -2 & \vdots & 0 & 0 & 1\end{array}\right]$
Interchanging $R_{1}$ and $R_{2}$ we get,

$$
\left[\begin{array}{llllll}
1 & 2 & -2 & \vdots & 0 & 0 & 1 \\
3 & 4 & 2 & \vdots & 0 & 1 & 0 \\
2 & 5 & -1 & \vdots & 1 & 0 & 0
\end{array}\right] R\left[\begin{array}{llllll}
1 & 2 & -2 & \vdots & 0 & 0 & 1 \\
0 & -2 & 8 & \vdots & 0 & 1 & -3 \\
0 & 1 & 3 & \vdots & 1 & 0 & -2
\end{array}\right] \begin{gathered}
\text { By } R_{3}+(-3) R_{1} \rightarrow R_{2}^{\prime} \\
\text { and } R_{3}+(-2) R_{1} \rightarrow R_{2}^{\prime}
\end{gathered}
$$

By $-\frac{1}{2} R_{2} \rightarrow R_{2}^{\prime}$, we get

$$
\left[\begin{array}{cccccc}
1 & 2 & -2 & \vdots & 0 & 0 & 1 \\
0 & 1 & -4 & \vdots & 0 & -\frac{1}{2} & \frac{3}{2} \\
0 & 1 & 3 & \vdots & 1 & 0 & -2
\end{array}\right] R\left[\begin{array}{cccccc}
1 & 0 & 6 & \vdots & 0 & 1 & -2 \\
0 & 1 & -4 & \vdots & 0 & -\frac{1}{2} & \frac{3}{2} \\
0 & 0 & 7 & \vdots & 1 & \frac{1}{2} & -\frac{7}{2}
\end{array}\right] \begin{gathered}
\text { By } R_{1}+(-1) R_{2} \rightarrow R_{2}^{\prime} \\
\text { and } R_{1}+(-2) R_{2} \rightarrow R_{1}^{\prime}
\end{gathered}
$$

By $\frac{1}{7} R_{3} \rightarrow R_{3}^{\prime}$, we have

$$
\left[\begin{array}{ccccc}
1 & 0 & 6 & \vdots & 0 & 1 & -2 \\
0 & 1 & -4 & \vdots & 0 & -\frac{1}{2} & \frac{3}{2} \\
0 & 0 & 1 & \vdots & \frac{1}{7} & \frac{1}{14} & -\frac{1}{2}
\end{array}\right] \begin{aligned}
& \text { I } \\
& \text { By } R_{1}+(-6) R_{3} \rightarrow R_{1}^{\prime} \\
& \text { and } R_{3}+4 R_{3} \rightarrow R_{2}^{\prime}
\end{aligned}
$$

Thus, the inverse of $A$ is $\left[\begin{array}{rrr}-\frac{6}{7} & \frac{4}{7} & 1 \\ \frac{4}{7} & -\frac{3}{14} & -\frac{1}{2} \\ \frac{1}{7} & \frac{1}{14} & -\frac{1}{2}\end{array}\right]$

Rank of a Matrix: Let $A$ be a non-zero matrix. If $r$ is the number of non-zero rows when it is reduced to the echelon form, then $r$ is called the rank of the matrix $A$.

Example 10 Find the rank of the matrix

$$
\left[\begin{array}{cccc}
1 & -1 & 2 & -3 \\
2 & 0 & 7 & -7 \\
3 & 1 & 12 & -11
\end{array}\right]
$$

Solution $\left[\begin{array}{cccc}1 & -1 & 2 & -3 \\ 2 & 0 & 7 & -7 \\ 3 & 1 & 12 & -11\end{array}\right] \quad\left[\begin{array}{cccc}1 & -1 & 2 & -3 \\ 0 & 2 & 3 & -1 \\ 0 & 4 & 6 & -2\end{array}\right] \quad$ By $R_{2}+(-2) R_{1} \rightarrow R_{2}^{\prime}$ and $R_{3}+(-3) R_{1} \rightarrow R_{3}^{\prime}$

$$
\left[\begin{array}{cccc}
1 & -1 & 2 & -3 \\
0 & 1 & \frac{3}{2} & \frac{1}{2} \\
0 & 4 & \frac{6}{6} & -2
\end{array}\right] \text { By } \frac{1}{2} R_{2} \rightarrow R_{2}^{\prime} \quad\left[\begin{array}{cccc}
1 & -1 & 2 & -3 \\
0 & 1 & \frac{3}{2} & -\frac{1}{2} \\
0 & 0 & 0 & 0
\end{array}\right] \text { By } R_{3}+(-4) R_{2} \rightarrow R_{3}^{\prime}
$$

As the number of non-zero rows is 2 when the given matrix is reduced to echelon form, therefore, the rank of the given matrix is 2 .

# 4.8 System of Non-Homogeneous Linear Equations

Three linear equations in three variables such as:

$$
\left.\begin{array}{rl}
a_{1} x+b_{1} y+c_{1} z & =d_{1} \\
a_{2} x+b_{2} y+c_{2} z & =d_{2} \\
a_{3} x+b_{3} y+c_{3} z & =d_{3}
\end{array}\right\}
$$

is called a system of non-homogeneous linear equations in the three variables $x, y$ and $z$, if constant terms $d_{1}, d_{2}$ and $d_{3}$ are not all zero.

Consistent: A system of linear equations is said to be consistent if the system has a unique solution or it has infinitely many solutions.
Inconsistent: A system of linear equations is said to be inconsistent if the system has no solution.
Now we will solve the system of non-homogeneous linear equations with the help of the following methods:
(i) Using reduced echelon form
(ii) Using matrix inversion method
(iii) Using Cramer's rule

# 4.8.1 Reduced Echelon Form

There are following steps to solve a system of non-homogeneous linear equations (i):
(i) Convert to augmented matrix
i.e.

$$
\left[\begin{array}{lll}
a_{1} & b_{1} & c_{1} & d_{1} \\
a_{2} & b_{2} & c_{2} & d_{2} \\
a_{3} & b_{3} & c_{3} & d_{3}
\end{array}\right]
$$

(ii) Convert to reduced echelon form
(iii) Solve by back substitution

Example 11 Solve the following and explain a consistent and inconsistent system:
(i) $2 x+5 y-z=5$
(ii) $x+y+2 z=1$
(iii) $x-y+2 z=1$
$3 x+4 y+2 z=11$
$2 x-y+7 z=11$
$2 x-6 y+5 z=7$
$x+2 y-2 z=-3$
$3 x+5 y+4 z=-3$
$3 x+5 y+4 z=-3$

Solution (i) The augmented matrix of the given system is $\left[\begin{array}{lllll}2 & 5 & -1 & \vdots & 5 \\ 3 & 4 & 2 & \vdots & 11 \\ 1 & 2 & -2 & \vdots & -3\end{array}\right]$
We apply the elementary row operations to the above matrix to reduce it to the equivalent reduced (row) echelon form, that is,

$$
\left[\begin{array}{lllll}
2 & 5 & -1 & \vdots & 5 \\
3 & 4 & 2 & \vdots & 11 \\
1 & 2 & -2 & \vdots & -3
\end{array}\right] \quad\left[\begin{array}{lllll}
1 & 2 & -2 & \vdots & -3 \\
3 & 4 & 2 & \vdots & 11 \\
2 & 5 & -1 & \vdots & 5
\end{array}\right] \quad \text { By } R_{1} \leftrightarrow R_{3}
$$

$\left[\begin{array}{cccccc}1 & 2 & -2 & \vdots & -3 \\ 0 & -2 & 8 & \vdots & 20 \\ 2 & 5 & -1 & \vdots & 5\end{array}\right]$ By $R_{2}+(-3) R_{1} \rightarrow R_{2}^{\prime} \underline{R}\left[\begin{array}{cccccc}1 & 2 & -2 & \vdots & -3 \\ 0 & -2 & 8 & \vdots & 20 \\ 0 & 1 & 3 & \vdots & 11\end{array}\right]$ By $R_{3}+(-2) R_{1} \rightarrow R_{3}^{\prime}$

By $-\frac{1}{2} R_{2} \rightarrow R_{2}^{\prime}$, we get
$\underline{R}\left[\begin{array}{ccccc:c:}1 & 2 & -2 & \vdots & -3 \\ 0 & 1 & -4 & \vdots & -10 \\ 0 & 1 & 3 & \vdots & 11\end{array}\right] \underline{R}\left[\begin{array}{ccccc:c:}1 & 0 & 6 & \vdots & 17 \\ 0 & 1 & -4 & \vdots & -10 \\ 0 & 0 & 7 & \vdots & 21\end{array}\right]$ and $R_{1}+(-2) R_{2} \rightarrow R_{1}^{\prime}$ and $R_{3}+(-1) R_{2} \rightarrow R_{3}^{\prime}$
$\underline{R}\left[\begin{array}{ccccc:c:}1 & 0 & 6 & \vdots & 17 \\ 0 & 1 & -4 & \vdots & -10 \\ 0 & 0 & 1 & \vdots & 3\end{array}\right]$ By $\frac{1}{7} R_{3} \rightarrow R_{3}^{\prime} \quad \underline{R}\left[\begin{array}{ccccc:c:}1 & 0 & 0 & \vdots & -1 \\ 0 & 1 & 0 & \vdots & 2 \\ 0 & 0 & 1 & \vdots & 3\end{array}\right]$ and $R_{2}+4 R_{3} \rightarrow R_{2}^{\prime}$ Thus, the solution is $x=-1, y=2$ and $z=3$, therefore the given system of linear equations has unique solution and it is consistent.
(ii) The augmented matrix of the given system is $\left[\begin{array}{ccccc:c:}1 & 1 & 2 & \vdots & 1 \\ 2 & -1 & 7 & \vdots & 11 \\ 3 & 5 & 4 & \vdots & -3\end{array}\right]$
$\left[\begin{array}{ccccc:c:}1 & 1 & 2 & \vdots & 1 \\ 2 & -1 & 7 & \vdots & 11 \\ 3 & 5 & 4 & \vdots & -3\end{array}\right] \quad \underline{R}\left[\begin{array}{ccccc:c:}1 & 1 & 2 & \vdots & 1 \\ 0 & -3 & 3 & \vdots & 9 \\ 0 & 2 & -2 & \vdots & -6\end{array}\right]$ Adding $(-2) R_{1}$ to $R_{2}$ and $(-3) R_{1}$ to $R_{3}$.
We get, $\underline{R}\left[\begin{array}{ccccc:c:}1 & 1 & 2 & \vdots & 1 \\ 0 & 1 & -1 & \vdots & -3 \\ 0 & 2 & -2 & \vdots & -6\end{array}\right]$ By $-\frac{1}{3} R_{2} \rightarrow R_{2}^{\prime} \quad \underline{R}\left[\begin{array}{ccccc:c:}1 & 0 & 3 & \vdots & 4 \\ 0 & 1 & -1 & \vdots & -3 \\ 0 & 0 & 0 & \vdots & 0\end{array}\right] \quad \begin{aligned} & \text { By } R_{1}+(-1) R_{2} \rightarrow R_{1}^{\prime} \\ & \text { and } R_{3}+(-2) R_{2} \rightarrow R_{3}^{\prime}\end{aligned}$
The given system is reduced to equivalent system

$$
\begin{aligned}
x+3 z & =4 \\
y-z & =-3 \\
0 z & =0
\end{aligned}
$$

The equation $0 z=0$ is satisfied by any value of $z$.
From the first and second equations, we get

$$
\begin{aligned}
& x=-3 z+4 \\
& \text { and } \quad y=z-3
\end{aligned}
$$

As $z$ is arbitrary, so we can find infinitely many values of $x$ and $y$ from equations (a) and (b) or the given system, is satisfied by $x=4-3 t, y=t-3$ and $z=t$ for any real value of $t$.
Thus, the given system has infinitely many solutions and it is consistent.
(iii) The augmented matrix of the system is $\left[\begin{array}{ccccc:c:}1 & -1 & 2 & \vdots & 1 \\ 2 & -6 & 5 & \vdots & 7 \\ 3 & 5 & 4 & \vdots & -3\end{array}\right]$

$\left[\begin{array}{ccccc}1 & -1 & 2 & \vdots & 1 \\ 2 & -6 & 5 & \vdots & 7 \\ 3 & 5 & 4 & \vdots & -3\end{array}\right] R\left[\begin{array}{ccccc}1 & -1 & 2 & \vdots & 1 \\ 0 & -4 & 1 & \vdots & 5 \\ 0 & 8 & -2 & \vdots & -6\end{array}\right]$ Adding $(-2) R_{1}$ to $R_{2}$ and $\left(-3 R_{1}\right)$ to $R_{2}$.

We have,
$R\left[\begin{array}{ccccc}1 & -1 & 2 & \vdots & 1 \\ 0 & 1 & -\frac{1}{4} & \vdots & -\frac{5}{4} \\ 0 & 8 & -2 & \vdots & -6\end{array}\right] B y-\frac{1}{4} R_{2} \rightarrow R_{2}^{\prime} \quad R\left[\begin{array}{ccccc}1 & 0 & \frac{7}{4} & \vdots & -\frac{1}{4} \\ 0 & 1 & -\frac{1}{4} & \vdots & -\frac{5}{4} \\ 0 & 0 & 0 & \vdots & 4\end{array}\right] \begin{aligned} & \text { By } R_{1}+1 . R_{2} \rightarrow R_{1}^{\prime} \\ & \text { and } R_{2}+(-8) R_{2} \rightarrow R_{2}^{\prime}\end{aligned}$
Thus, the given system is reduced to the equivalent system

$$
\begin{aligned}
x+\frac{7}{4} z & =-\frac{1}{4} \\
y-\frac{1}{4} z & =-\frac{5}{4} \\
0 z & =4
\end{aligned}
$$

The third equation $0 z=4$ has no solution, so the system as a whole has no solution. Thus, the system is inconsistent.
Note We see that in the case of the system (i), the (row) rank of the augmented matrix and the coefficient matrix of the system is the same, that is, 3 which is equal to the number of the variables in the system (i).
Thus, we observe that a linear system is consistent and has a unique solution if the rank of the coefficient matrix is the same as that of the augmented matrix of the system and equal to number of variables.
In the case of the system (ii), the rank of the coefficient matrix is the same as that of the augmented matrix of the system but it is 2 which is less than the number of variables in the system (ii).
Thus, we observe that a system is consistent and has infinitely many solutions if the ranks of the coefficient matrix and the augmented matrix of the system are equal but the rank is less than the number of variables in the system.
In the case of the system (iii), we see that the rank of the coefficient matrix is not equal to the rank of the augmented matrix of the system.
Thus, we observe that a system is inconsistent if the ranks of the coefficient matrix and the augmented matrix of the system are different.

# 4.8.2 Matrix Inversion Method

The matrix inversion method is a way to solve a system of linear equations using the inverse of a matrix.

$$
x_{1}-2 x_{2}+x_{3}=-4
$$

Example 12 Use matrix inversion method to solve the system $2 x_{1}-3 x_{2}+2 x_{3}=-6$

$$
2 x_{1}+2 x_{2}+x_{3}=5
$$

Solution The matrix form of the given system is

$$
\left[\begin{array}{ccc}
1 & -2 & 1 \\
2 & -3 & 2 \\
2 & 2 & 1
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3}
\end{array}\right]=\left[\begin{array}{c}
-4 \\
-6 \\

\end{array}\right]
$$

or $\quad A X=B$
Where

$$
A=\left[\begin{array}{ccc}
1 & -2 & 1 \\
2 & -3 & 2 \\
2 & 2 & 1
\end{array}\right], X=\left[\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3}
\end{array}\right] \text { and } B=\left[\begin{array}{c}
-4 \\
-6 \\

\end{array}\right]
$$

As

$$
|A|=\left|\begin{array}{ccc}
1 & -2 & 1 \\
2 & -3 & 2 \\
2 & 2 & 1
\end{array}\right|=\left|\begin{array}{ccc}
1 & -2 & 1 \\
0 & 1 & 0 \\
2 & 2 & 1
\end{array}\right| \quad \text { By } R_{2}+(-2) R_{1} \rightarrow R_{2}
$$

Expanding by $\mathrm{R}_{2}$ we have

$$
=(-1)^{2+2}\left|\begin{array}{ll}
1 & 1 \\
2 & 1
\end{array}\right|=1-2=-1, \text { that is }
$$

$|A| \neq 0$, so the inverse of A exists and (i) can be written as

$$
X=A^{-1} B
$$

Now we find adj $A$.

$$
\begin{aligned}
& \rightarrow \quad[A_{i j}]_{i=3}=\left[\begin{array}{ccc}
-7 & 2 & 10 \\
-1 & -6 & -1 \\
-1 & 0 & 1
\end{array}\right] \\
& \text { Cofactors are } A_{11}=-7, A_{12}=2, A_{13}=10, A_{21}=4 \\
& A_{22}=-1, A_{23}=-6, A_{31}=-1, A_{32}=0, A_{33}=1 \\
& \text { So } \quad \text { adj } A=\left[\begin{array}{ccc}
-7 & 4 & -1 \\
2 & -1 & 0 \\
10 & -6 & 1
\end{array}\right] \\
& \text { and } A^{-1}=\frac{1}{|A|} \operatorname{adj} A=\frac{1}{-1}\left[\begin{array}{ccc}
-7 & 4 & -1 \\
2 & -1 & 0 \\
10 & -6 & 1
\end{array}\right]=\left[\begin{array}{ccc}
7 & -4 & 1 \\
-2 & 1 & 0 \\
-10 & 6 & -1
\end{array}\right]
\end{aligned}
$$

Thus $\left[\begin{array}{l}x_{1} \\ x_{2} \\ x_{3}\end{array}\right]=A^{-1}\left[\begin{array}{c}-4 \\ -6 \\ 5\end{array}\right]=\left[\begin{array}{rrr}7 & -4 & 1 \\ -2 & 1 & 0 \\ -10 & 6 & -1\end{array}\right]\left[\begin{array}{c}-4 \\ -6 \\ 5\end{array}\right]=\left[\begin{array}{c}-28+24+5 \\ 8-6+0 \\ 40-36-5\end{array}\right]$, i.e.,

$$
\left[\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3}
\end{array}\right]=\left[\begin{array}{c}
1 \\
2 \\
-1
\end{array}\right]
$$

Thus, the solution set is $\left\{\left(x_{1}, x_{2}, x_{3}\right)\right\}=\{(1,2,-1)\}$

# 4.8.3 Cramer's Rule

Consider the system of equations,

$$
\left.\begin{array}{l}
a_{11} x_{1}+a_{12} x_{2}+a_{13} x_{3}=b_{1} \\
a_{21} x_{1}+a_{22} x_{2}+a_{23} x_{3}=b_{2} \\
a_{31} x_{1}+a_{32} x_{2}+a_{33} x_{3}=b_{3}
\end{array}\right\}
$$

These are three linear equations in three variables $x_{1}, x_{2}, x_{3}$ with coefficients and constant terms in the real field R. We write the above system of equations in matrix form as:

$$
A X=B
$$

where

$$
A=\left[a_{i j}\right]_{3 \times 31} X=\left[\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3}
\end{array}\right] \text { and } \quad B=\left[\begin{array}{l}
b_{1} \\
b_{2} \\
b_{3}
\end{array}\right]
$$

We know that the matrix equation (ii) can be written as: $X=A^{-1} B$ (if $A^{-1}$ exists)
We have already proved that $A^{-1}=\frac{1}{|A|} \operatorname{adj} A$

$$
\text { and } \quad \operatorname{adj} A=\left[A_{i j}^{\prime}\right]_{3 \times 3}=\left[\begin{array}{llll}
A_{11} & A_{21} & A_{31} \\
A_{12} & A_{22} & A_{32} \\
A_{13} & A_{23} & A_{33}
\end{array}\right] \quad\left(\because A_{i j}^{\prime}=A_{j i}\right)
$$

Thus $\left[\begin{array}{l}x_{1} \\ x_{2} \\ x_{3}\end{array}\right]=\frac{1}{|A|}\left[\begin{array}{llll}A_{11} & A_{21} & A_{31} \\ A_{12} & A_{22} & A_{32} \\ A_{13} & A_{23} & A_{33}\end{array}\right]\left[\begin{array}{l}b_{1} \\ b_{2} \\ b_{3}\end{array}\right]=\frac{1}{|A|}\left[\begin{array}{llll}A_{1} b_{1}+A_{21} b_{2}+A_{31} b_{3} \\ A_{12} b_{1}+A_{22} b_{2}+A_{32} b_{3} \\ A_{13} b_{1}+A_{23} b_{2}+A_{33} b_{3}\end{array}\right]$

i.e., $\left[\begin{array}{l}x_{1} \\ x_{2} \\ x_{3}\end{array}\right]=\left[\begin{array}{l}\frac{A_{11} b_{1}+A_{21} b_{2}+A_{21} b_{3}}{|A|} \\ \frac{A_{12} b_{1}+A_{22} b_{2}+A_{22} b_{3}}{|A|} \\ \frac{A_{13} b_{1}+A_{23} b_{2}+A_{23} b_{3}}{|A|}\end{array}\right]$
Hence

$$
\begin{aligned}
& x_{1}=\frac{b_{1} A_{11}+b_{2} A_{21}+b_{3} A_{31}}{|A|}=\frac{\left|\begin{array}{lll}
b_{1} & a_{12} & a_{13} \\
b_{2} & a_{22} & a_{23}
\end{array}\right|}{\left|A\right|} \\
& x_{2}=\frac{b_{1} A_{12}+b_{2} A_{22}+b_{3} A_{32}}{|A|}=\frac{\left|\begin{array}{lll}
a_{11} & b_{1} & a_{13} \\
a_{21} & b_{2} & a_{23}
\end{array}\right|}{\left|A\right|} \\
& x_{3}=\frac{b_{1} A_{13}+b_{2} A_{23}+b_{3} A_{32}}{|A|}=\frac{\left|\begin{array}{lll}
a_{11} & a_{12} & b_{1} \\
a_{21} & a_{22} & b_{2}
\end{array}\right|}{\left|A\right|}
\end{aligned}
$$

The method of solving the system with the help of results (iii), (iv) and (v) is often referred to as Cramer's Rule.

Example 15 Use Cramer's rule to solve the system. $\left.\begin{array}{l}3 x_{1}+x_{2}-x_{3}=-4 \\ x_{1}+x_{2}-2 x_{3}=-4 \\ -x_{1}+2 x_{2}-x_{3}=1\end{array}\right\}$

$$
\begin{aligned}
& \text { Here }|A|=\left|\begin{array}{ccc}
3 & 1 & -1 \\
1 & 1 & -2 \\
-1 & 2 & -1
\end{array}\right|=3(-1+4)-1 \cdot(-1-2)-1 \cdot(2+1) \\
& =9+3-3=9 \\
& \text { So, } \quad x_{1}=\frac{\left|\begin{array}{ccc}
-4 & 1 & -1 \\
-4 & 1 & -2 \\
1 & 2 & -1
\end{array}\right|}{9}=\frac{-4(-1+4)-1(4+2)-1(-8-1)}{9}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{-12-6+9}{9}=\frac{-9}{9}=-1 \\
& \begin{array}{r}
x_{2}=\frac{\left|\begin{array}{ccc}
3 & -4 & -1 \\
1 & -4 & -2
\end{array}\right|}{9}=\frac{3(4+2)+4(-1-2)-1(1-4)}{9} \\
=\frac{18-12+3}{9}=\frac{9}{9}=1
\end{array} \\
& x_{3}=\frac{\left|\begin{array}{ccc}
3 & 1 & -4 \\
1 & 1 & -4 \\
-1 & 2 & 1
\end{array}\right|}{\begin{array}{ll}
9}

\end{array}}=\frac{3(1+8)-1(1-4)-4(2+1)}{9}=\frac{27+3-12}{9}=\frac{18}{9}=2
\end{aligned}
$$

Hence $\quad x_{1}=-1, x_{2}=1, x_{3}=2$
Thus, the solution set is $\left\{\left(x_{1}, x_{2}, x_{3}\right)\right\}=\{(-1,1,2)\}$

# 4.9 System of Homogeneous Linear Equations

The system of following homogeneous linear equations:

$$
\left.\begin{array}{l}
a_{11} x_{1}+a_{12} x_{2}+a_{13} x_{3}=0 \\
a_{21} x_{1}+a_{22} x_{2}+a_{23} x_{3}=0 \\
a_{31} x_{1}+a_{32} x_{2}+a_{33} x_{3}=0
\end{array}\right\}
$$

is always satisfied by $x_{1}=0, x_{2}=0$ and $x_{3}=0$, so such a system is always consistent.
Trivial Solution: The solution $(0,0,0)$ of the above homogeneous system is called the trivial solution.
Non-Trivial Solution: Any other solution of system (i) other than the trivial solution is called a non-trivial solution.

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