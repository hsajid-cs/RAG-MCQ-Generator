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