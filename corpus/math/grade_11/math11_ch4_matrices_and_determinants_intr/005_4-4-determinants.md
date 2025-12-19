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