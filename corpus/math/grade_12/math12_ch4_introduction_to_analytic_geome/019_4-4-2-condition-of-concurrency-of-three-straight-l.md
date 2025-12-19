### 4.4.2 Condition of Concurrency of Three Straight Lines

Three non-parallel lines

$$
\begin{aligned}
& l_{1}: a_{1} x+b_{1} y+c_{1}=0 \\
& l_{2}: a_{1} x+b_{2} y+c_{2}=0 \\
& l_{3}: a_{1} x+b_{2} y+c_{3}=0
\end{aligned}
$$

are concurrent iff $\left|\begin{array}{ll}a_{1} & b_{1} \\ a_{2} & b_{2} \\ a_{3} & b_{3} & c_{3}\end{array}\right|=0$

Proof: If the lines are concurrent then they have a common point of intersection $P\left(x_{1}, y_{1}\right)$ say. As $l_{1} \not l_{2}$, so their point of intersection $(x, y)$ is

$$
x=\frac{b_{1} c_{1}-b_{2} c_{2}}{a_{1} b_{2}-a_{2} b_{1}} \text { and } y \quad \frac{a_{1} c_{1}-a_{2} c_{2}}{a_{1} b_{2}-a_{2} b_{1}}
$$

This point also lies on (3), so

$$
\begin{aligned}
& a_{1}\left(\frac{b_{1} c_{1}-b_{2} c_{2}}{a_{1} b_{2}-a_{2} b_{1}}\right)+b_{2}\left(\frac{a_{1} c_{1}-a_{2} c_{2}}{a_{1} b_{2}-a_{2} b_{1}}\right)+c_{3}=0 \\
& a_{1}\left(b_{1} c_{2}-b_{2} c_{1}\right)+b_{2}\left(a_{1} c_{1}-a_{2} c_{2}\right)+c_{3}\left(a_{1} b_{2}-a_{2} b_{1}\right)=0
\end{aligned}
$$

or

An easier way to write the above equation is in the following determinant form:

$$
\left|\begin{array}{lll}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2}
\end{array}\right|=0
$$

This is a necessary and sufficient condition of concurrency of the given three lines.
Example 1: Check whether the following lines are concurrent or not. If concurrent, find the point of concurrency.

$$
\begin{aligned}
& 3 x-4 y-3=0 \\
& 5 x+12 y+1=0 \\
& 32 x+4 y-17=0
\end{aligned}
$$

Solution. The determinant of the coefficients of the given equations is

$$
\begin{aligned}
& \left|\begin{array}{lll}
3 & -4 & -3 \\
5 & 12 & 1 \\
32 & 4 & -17
\end{array}\right|=\left|\begin{array}{lll}
18 & 32 & 0 \\
5 & 12 & 1 \\
117 & 208 & 0
\end{array}\right| \cdot \text { by } \quad R_{1}+3 R_{2} \\
& =-1\left|\begin{array}{ll}
18 & 32 \\
117 & 208
\end{array}\right|=-\left(208 \times 18-117 \times 32\right)=0
\end{aligned}
$$

Thus the lines are concurrent.
The point of intersection of any two lines is the required point of concurrency. From (1) and (2), we have

$$
\begin{aligned}
& \frac{x}{-4+36}=\frac{y}{-15-3}=\frac{1}{36+20} \\
& x=\frac{32}{56}=\frac{4}{7} \text { and } y=\frac{-18}{56}=\frac{-9}{28} \text { i.e. }\left(\frac{4}{7}, \frac{-9}{28}\right)
\end{aligned}
$$

is the point of intersection.