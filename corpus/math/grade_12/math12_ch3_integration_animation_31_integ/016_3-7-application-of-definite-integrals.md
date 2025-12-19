### 3.7 APPLICATION OF DEFINITE INTEGRALS.

Here we shall give some examples involving area bounded by the curve and the $x$-axis.
Example 1. Find the area bounded by the curve $y=4-x^{2}$ and the $x$-axis.

Solution: We first find the points where the curve cuts the $x$-axis. Putting $y=0$, we have
$4-x^{2}=0 \Rightarrow x= \pm 2$.
So the curve cuts the $x$-axis at $(-2,0)$ and $(2,0)$
The area above the $x$-axis and under the curve $y=4-x^{2}$ is
shown in the figure as shaded region..

Thus the required area $=\int(4-x) d x=[4 x--]$

$$
\begin{aligned}
& =\left(4(2)-\frac{(2)^{2}}{3}\right)-\left(4(-2)-\frac{(-2)^{2}}{3}\right) \\
& =\left(8-\frac{8}{3}\right)-\left(-8+\frac{8}{3}\right) \\
& =\frac{16}{3}\left(\frac{-16}{3}\right) \quad \frac{32}{3}
\end{aligned}
$$

Example 2. Find the area bounded by the curve $y=x^{3}+3 x^{2}$ and the $x$-axis.
Solution: Putting $y=0$, we have

$$
\begin{aligned}
x^{3}+3 x^{2} & =0 \\
\Rightarrow x^{2}(x+3) & =0 \Rightarrow x=0, x=-3
\end{aligned}
$$

The curve cuts the $x$-axis at $(-3,0)$ and $(0,0)$ (see the figure).

Thus the required area $=\int_{-3}^{0}\left(x^{3}+3 x^{2}\right) d x$

$$
\begin{aligned}
& =\left[\frac{x^{4}}{4}+x^{2}\right]_{-3}^{0} \\
& =\left(\frac{0}{4}+0\right)-\left(\frac{(-3)^{4}}{4}+(-3)^{2}\right) \\
& =0-\left(\frac{81}{4}-27\right)=-\left(\frac{81-108}{4}\right)=-\left(-\frac{27}{4}\right)=\frac{27}{4}
\end{aligned}
$$

Example 3. Find the area bounded by $y=x\left(x^{3}-4\right)$ and the $x$-axis.
Solution: Putting $y=0$, we have

$$
x\left(x^{3}-4\right) \Rightarrow x=0, x= \pm 2
$$

The curve cuts the $x$-axis at $(-2,0),(0,0)$ and $(2,0)$. The graph of $f$ is shown in the figure and we have to calculate the area of the shaded region.

$$
f(x)=x\left(x^{2}-4\right)
$$

$f(x) \geq 0$ for $-2 \leq x \leq 0$, that is, the area in the interval $[-2,0]$ is above the $x$-axis and is equal to

$$
\begin{aligned}
& \int_{0}^{x} x\left(x^{2}-4\right) d x \\
& =\int_{-2}^{0}\left(x^{3} \quad 4 x\right) d x=\left|\frac{x^{4}}{4} \quad 4\left(\frac{x^{2}}{2}\right)\right|_{-2}^{0}=-\left[\frac{x^{4}}{4} \quad 2 x^{2}\right]_{-2}^{0} \\
& =0-\left(\frac{(-2)^{4}}{4}-2(-2)^{2}\right)=0-\left(\frac{16}{4}-8\right)=-(4-8)=4
\end{aligned}
$$

$f(x) \leq 0$ for $0 \leq x \leq 2$, that is, the area in the interval $[0,2]$ is below the $x$-axis and is equal to $-\int_{0}^{x}\left(x^{2}-4\right) d x \ll\left[\frac{x^{4}}{4} \quad 2 x^{2}\right]_{0}^{2}$

$$
\begin{aligned}
& =\left[\left(\frac{16}{4} \quad 2(4)\right) \quad 0\right] \\
& =-[-4-8]=-(-4)=4
\end{aligned}
$$

Thus the area of the shaded region $=4+4=8$
Example 4: Find the area bounded by the curve $f(x)=x^{3}-2 x^{2}+1$ and the $x$-axis in the 1st quadrant.

Solution: As $f(1)=1-2+1=0$, so $x-1$ is factor of $x^{3}-2 x^{2}+1$. By long division, we find that $x^{2}-x-1$ is also a factor of $x^{3}-2 x^{2}+1$.

Solving $x^{2}-x-1=0$, we get

$$
x=\frac{1 \pm \sqrt{1+4}}{2}=\frac{1 \pm \sqrt{5}}{2}
$$

Thus the curve cuts the $x$-axis at $x=1, \frac{1+\sqrt{5}}{2}$ and $\frac{1-\sqrt{5}}{2}$

The graph of the curve is shown in the adjoining figure and the required area is shaded.
The required area $A$ will be

$$
\begin{aligned}
A & =\int_{0}^{A}\left(x^{2}-2 x^{2}+1\right) d x \\
& =\left|\frac{x^{4}}{4}-2 \frac{x^{2}}{3}+x\right|_{0} \\
& =\left(\frac{1}{4}-\frac{2}{3}+1\right)-0=\frac{3-8+12}{12}=\frac{7}{12}
\end{aligned}
$$

Example 5: Find the area between the $x$-axis and the curve $y^{2}=4-x$ in the first quadrant from $x=0$ to $x=3$.

Solution: The branch of the curve above the $x$-axis is

$$
y=\sqrt{4-x}
$$

The area to be determined is shaded in the adjoining figure.
Thus the required area $=\int_{0}^{1} \sqrt{4-x} d x$
Let $4-x=t$ (i), then $-d x=d t \Rightarrow d x=-d t$
Putting $x=0$ and $x=3$ (i), we get $t=4$ and $t=1$
Now the required area $=\int_{t}^{1} t^{\frac{1}{2}} \times(-d t)=-\int_{t}^{1} t^{\frac{1}{2}} d t$

$$
\begin{aligned}
& =\int_{t}^{4} t^{\frac{1}{2}} d t=\left|\frac{t^{0.5}}{3 / 2}\right|_{0}^{4} \\
& =\frac{2}{3}\left|t^{0.5}\right|_{0}^{4}=\frac{2}{3}\left[(4)^{\frac{3}{2}} \quad(1)^{\frac{1}{2}}\right] \quad \frac{2}{3}[8 \quad 4] \quad \frac{14}{3} \text { (square units) }
\end{aligned}
$$

## EXERCISE 3.7

1. Find the area between the $x$-axis and the curve $y=x^{2}+1$ from $x=1$ to $x=2$.
2. Find the area, above the $x$-axis and under the curve $y=5-x^{2}$ from $x=-1$ to $x=2$.
3. Find the area below the curve $y=3 \sqrt{x}$ and above the $x$-axis between $x=1$ and $x=4$.
4. Find the area bounded by $\cos$ function from $x=-\frac{\pi}{4}$ to $x=\frac{\pi}{2}$
5. Find the area between the $x$-axis and the curve $y=4 x-x^{2}$.
6. Determine the area bounded by the parabola $y=x^{2}+2 x-3$ and the $x$-axis.
7. Find the area bounded by the curve $y=x^{3}+1$, the $x$-axis and line $x=2$.
8. Find the area bounded by the curve $y=x^{2}-4 x$ and the $x$-axis.
9. Find the area between the curve $y=x(x-1)(x+1)$ and the $x$-axis.
10. Find the area above the $x$-axis, bounded by the curve $y^{2}=3-x$ from $x=-1$ to $x=2$
11. Find the area between the $x$-axis and the curve $y=-\cos \frac{1}{2} x$ from $x=\pi$ to $\pi$
12. Find the area between the $x$-axis and the curve $y=\sin 2 x$ from $x=0$ to $x=\frac{\pi}{3}$
13. Find the area between the $x$-axis and the curve $y=\sqrt{2 a x-x^{2}}$ when $a>0$.