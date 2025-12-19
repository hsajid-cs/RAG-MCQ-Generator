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