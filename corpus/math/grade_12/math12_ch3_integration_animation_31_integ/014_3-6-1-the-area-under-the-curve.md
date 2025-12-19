### 3.6.1 The Area Under The Curve

About 300 B.C. and around this, mathematicians succeeded to find area of plane region like triangle, rectangle, trapezium and regular polygons etc. but the area of the complicated region bounded by the curves and the $x$-axis from $x=a$ to $x=b$ was a challenge for mathematicians before the invention of integral calculus.

Now we give attention to the use of integration for evaluating areas. Suppose that a function $f$ is continuous on interval $a \leq x \leq b$ and $f(x)>0$. To determine the area under the graph of $f$ and above the $x$-axis from $x=a$ to $x=b$, we follow the idea of Archimedes (287-212 B.C.) for approximating the function by horizontal functions and the area under $f$ by the sum of small rectangles.

To explain the idea mentioned above, we first draw the graph of $f$ defined as: $f(x)=\frac{1}{2} x^{2}$

The graph of $f$ is shown in the figure. We divide the interval $[1,3]$ into four sub-intervals of equal length $=\frac{3-1}{4}=\frac{1}{2}$.

As the subintervals are
$\left[x_{0}, x_{1}\right],\left[x_{1}, x_{2}\right],\left[x_{2}, x_{3}\right],\left[x_{3}, x_{4}\right]$, so
$x_{0}=1, x_{1}=1.5, x_{2}=2, x_{3}=2.5, x_{4}=3$
In the figure $M A=f\left(x_{0}\right), N B=f\left(x_{1}\right)$ and $M N=\delta x$, so it
is obvious that the area of the rectangle $A M N C<$ the area of the shaded region $A M N B<$ area of the rectangle $D M N B$, that is,
$f\left(x_{0}\right) \delta x<$ area of the shaded region $A M N B<f\left(x_{1}\right) \delta x$
Let $\stackrel{\circ}{x}_{1}, \stackrel{\circ}{x}_{2}, \stackrel{\circ}{x}_{3}, \stackrel{\circ}{x}_{4}$ be the mid point of four subintervals mentioned above.

Then the value of $f$ at $\stackrel{\circ}{x}_{1}$, is $f\left(\stackrel{\circ}{x}_{1}\right)$, so the area of the rectangle $F M N E=f\left(\stackrel{\circ}{x}_{1}\right) \delta x$
(See the rectangle $F M N E$ shown in the figure)
We observe that the area of the rectangle $F M N E$ is approximately equal to the area of the region $A M N B$ under the graph of $f$ from $x_{0}$ to $x_{1}$.
Now we calculate the sum of areas of the rectangles shown in the figure, that is, $f\left(\stackrel{\circ}{x}_{1}\right) \delta x+f\left(\stackrel{\circ}{x}_{2}\right) \delta x+f\left(\stackrel{\circ}{x}_{3}\right) \delta x+f\left(\stackrel{\circ}{x}_{4}\right) \delta x$

$$
=\left[f\left(\stackrel{\circ}{x}_{1}\right)+f\left(\stackrel{\circ}{x}_{2}\right)+f\left(\stackrel{\circ}{x}_{3}\right)+f\left(\stackrel{\circ}{x}_{4}\right)\right] \delta x
$$

$$
\begin{aligned}
& =\left[\frac{1}{2}\left(\frac{x_{0}+x_{1}}{2}\right)^{2}+\frac{1}{2}\left(\frac{x_{1}+x_{2}}{2}\right)^{2}+\frac{1}{2}\left(\frac{x_{2}+x_{3}}{2}\right)^{2}+\frac{1}{2}\left(\frac{x_{3}+x_{4}}{2}\right)^{2}\right] \frac{1}{2} \\
& =\frac{1}{4}\left[\left(\frac{1+1.5}{2}\right)^{2}+\left(\frac{1.5+2}{2}\right)^{2}+\left(\frac{2+2.5}{2}\right)^{2}+\left(\frac{2.5+3}{2}\right)^{2}\right] \\
& =\frac{1}{4}\left[\left(1.25\right)^{2}+\left(1.75\right)^{2}+\left(2.25\right)^{2}+\left(2.75\right)^{2}\right] \\
& =\frac{1}{4}\left(1.5625+3.0625+5.0625+7.5625\right) \\
& =\frac{1}{4}(17.25)=4.3125
\end{aligned}
$$

But $\int \frac{1}{2} x^{2} d x=\left[\frac{1}{2} \cdot \frac{x^{2}}{3}\right]_{1}^{3}=\frac{1}{6}(27-1)=\frac{26}{6}=4.3$
If we go on increasing the number of intervals, then the sum of areas of small rectangles approaches closer to the number 4.3.

If we divide the interval $[1,3]$ into $n$ intervals and take $x_{i}$ the coordinate of any point of the $i$ th interval and $\delta x_{i}=x_{i}-x_{i-1}, i=1,2,3, \ldots, n$, then the sum of areas of $n$ rectangles is $\sum_{i=1}^{n} f\left(x_{i}\right) \delta x$ which tends to the number 4.3 when $n \rightarrow \infty$ and each $\delta x_{i} \rightarrow 0$.

Thus $\lim _{\substack{x \rightarrow \infty \\ x_{i} \rightarrow 0}} \sum_{i=1}^{n} f\left(x_{i}\right) \delta x_{i}=4.3$ and we conclude that

$$
\lim _{\substack{x \rightarrow \infty \\ x_{i} \rightarrow 0}} \sum_{i=1}^{n} f\left(x_{i}\right) \delta_{i} x=\int_{1}^{3} \frac{1}{2} x^{2} d x
$$

Thus the area above the $x$-axis and under the curve $y=f(x)$ from $a$ to $b$ is the definite integral $\int f(x) d x$.

Consider a function $f$ which is continuous on the interval $a \leq x \leq b$ and $f(x)>0$. The graph of $f$ is shown in the figure.
We define the function $A(x)$ as the area above the $x$-axis and under the curve $y=f(x)$ from $a$ to $x$. Let $\delta x$ be a small positive number and $x+\delta x$ be any number in the interval $[a, b]$ such that $a<x<x+\delta x$.

Let $P\left(x, f(x)\right)$ and $Q(x+\delta x, f(x+b x))$ be two points on the graph of $f$. The ordinates $P M$ and $Q N$ are drawn and two rectangles $P M N R, S M N Q$ are completed.

According to above definition, the area above the $x$-axis and under the curve $y=f(x)$ from $a$ to $x+\delta x$
is $A(x+\delta x)$, so the change in area is
$A(x+\delta x)-A(x)$ which is shaded in the figure
Note that the function $f$ is increasing in the interval $\left[x, x+\delta x\right]$.
From the figure, it is obvious that area of the rectangle $P M N R<A(x+\delta x)-A(x)<$ area of the rectangle $S M N Q$, i.e.,

$$
f(x) \delta x<A(x+\delta x)-A(x)<f(x+\delta x) \delta x
$$

Dividing the inequality by $\delta x$, we have

$$
\begin{aligned}
& f(x)<\frac{A(x+\delta x)-A(x)}{d x}<f(x+\delta x) \\
& \lim _{x \rightarrow \infty} f(x)=f(x) \quad \text { and } \quad \lim _{x \rightarrow \infty} f(x+\delta x)=f(x)
\end{aligned}
$$

Since the limits of the extremes in (I) are equal, so

$$
\frac{A(x+\delta x)-A(x)}{\delta x} \longrightarrow f(x) \quad \text { when } \delta x \rightarrow 0
$$

Thus $\quad \lim _{x \rightarrow \infty} \frac{A(x+\delta x)-A(x)}{\delta x}=f(x)$.
or

$$
A^{+}(x)=f(x)
$$

that is, $A(x)$ is an antiderivative of $f$, so $\int f(x) d x=A(x)+c$
and $\int f(x) d x=[A(x)]_{a}^{c}=A(x)-A(a)$

Since $A(x)$ is defined as the area under the curve $y=f(x)$ from $a$ to $x$, so $A(a)=0$
Thus

$$
A(x)=\int f(x) d x
$$

Putting $x=b$ in the equation (I), gives

$$
A(b)=\int f(x) d x
$$

which shows that the area $A$ of the region, above the $x$-axis and under the curve $y=f(x)$ from $a$ to $b$ is given by
$\int_{a}^{b} f(x) d x$, that is, $A=\int_{a}^{b} f(x) d x$
If the graph of $f$ is entirely below the $x$-axis, then the value of each $f\left(x_{i}\right)$ is negative and each product $f\left(x_{i}\right) d x_{i}$, is also negative, so in such a case, the definite integral is negative.

Thus the area, bounded in this case by the curve $y=f(x)$, the $x$-axis and the lines $x=a, x=b$ is $-\int f(x) d x$.

For example, $\sin x$ is negative for $-\pi<x<0$ and is positive for $0<x<\pi$.

Therefore the area bounded by the $x$-axis and graph of $\sin$ function from $-\pi$ to $\pi$ is given by

$$
\begin{aligned}
-\int_{-\pi}^{\pi} \sin x & d x+\int_{0}^{\pi} \sin x d x=\int_{0}^{\pi} \sin x d x+\int_{0}^{\pi} \sin x d x\left[\cup \int_{\pi}^{\pi} f(x) d x=\int_{0}^{\pi} f(x) d x\right] \\
& =[-\cos x]_{0}^{-\pi}+[-\cos x]_{0}^{\pi}=-\left[\cos (-\pi)-\cos 0\right]+[-(\cos \pi-\cos 0)] \\
& =-[(-1)-1]-[(-1)-1]=2+2=4
\end{aligned}
$$

## Note:

$\int \sin x d x=\int \cos x]_{0}^{-\pi}-\int \cos \pi-\cos (\pi)-\int(-1) \geq 0$