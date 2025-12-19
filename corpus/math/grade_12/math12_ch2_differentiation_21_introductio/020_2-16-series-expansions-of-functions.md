### 2.16 SERIES EXPANSIONS OF FUNCTIONS

A series of the form $a_{n}+a_{1} x+a_{2} x^{2}+a_{3} x^{3}+a_{4} x^{4}+\ldots \ldots+a_{n} x^{n}+\ldots$ is called a power series expansion of a function $f(x)$ where $a_{n}, a_{1}, a_{2}, \ldots, a_{n}, \ldots$ are constants and $x$ is a variable.

We determine the coefficient $a_{n}, a_{1}, a_{2}, \ldots, a_{n}, \ldots$ to specify power series by finding successive derivatives of the power series and evaluating them at $x=0$. That is,
version: 1.1

$$
\begin{aligned}
& f(x)=a_{0}+a_{1} x+a_{2} x^{2}+a_{3} x^{3}+a_{4} x^{4}+a_{5} x^{5}+\ldots \ldots+a_{n} x^{n}+\ldots . f(0)=a_{0} \\
& f^{\prime}(x)=a_{1}+2 a_{2} x+3 a_{3} x^{2}+4 a_{4} x^{3}+5 a_{5} x^{4}+\ldots \ldots+n a x^{n-1}+\ldots . f^{\prime}(0)=a_{1} \\
& f^{\prime \prime}(x)=2 a_{2}+6 a_{3} x+12 a_{4} x^{2}+20 a_{5} x^{3}+\ldots+n(n-1) a_{n} x^{n-2}+\ldots f^{\prime \prime}(0)=2 a_{2} \\
& f^{\prime \prime \prime}(x)=6 a_{3}+24 a_{4} x+60 a_{5} x^{2}+\ldots . \quad f^{\prime \prime}(0)=6 a_{3} \\
& f^{(0)}(x)=24 a_{4}+120 a_{5} x \ldots \ldots . \quad f^{(0)}(0)=24 a_{4}
\end{aligned}
$$

So we have $a_{0}=f(0), a_{1}=f^{\prime}(0), a_{2}=\frac{f^{\prime}(0)}{2!}, a_{3}=\frac{f^{\prime \prime}(0)}{3!}, a_{4}=\frac{f^{(0)}(0)}{4!}$
Following the above pattern, we can write $a_{n}=\frac{f^{\prime \prime}(0)}{n!}$
Thus substituting these values in the power series, we have

$$
f(x)=f(0)+f^{\prime}(0) x+\frac{f^{\prime \prime}(0)}{2!} x^{2}+\frac{f^{\prime \prime}(0)}{3!} x^{3}+\frac{f^{(0)}(0)}{4!} x^{4}+\ldots+\frac{f^{\prime \prime}(0)}{n!} x^{n}+\ldots
$$

This expansion of $f(x)$ is called the Maclaurin series expansion.
The above expansion is also named as Maclaurin's Theorem and can be stated as:
If $f(x)$ is expanded in ascending powers of $x$ as an infinite series, then

$$
f(x)=f(0)+f^{\prime}(0) x+\frac{f^{\prime \prime}(0)}{2!} x^{2}+\frac{f^{\prime \prime}(0)}{3!} x^{3}+\frac{f^{(0)}(0)}{4!} x^{4}+\ldots+\frac{f^{\prime \prime}(0)}{n!} x^{n}+\ldots
$$

Note that a function $f$ can be expanded in the Maclaurin series if the function is defined in the interval containing 0 and its derivatives exist at $x=0$.

The expansion is only valid if it is convergent.

Example 1: $\quad$ Expand $f(x)=\frac{1}{1+x}$ in the Maclaurin series.
Solution: $f$ is defined at $x=0$ that is, $f(0) 1$. Now we find successive derivatives of $f$ and their values at $x=0$.

$$
\begin{aligned}
& f^{\prime}(x)=(-1)(1+x)^{-2} \text { and } f^{\prime}(0)=1 \\
& f^{\prime \prime}(x)=(-1)(-2)(1+x)^{-3} \text { and } f^{\prime \prime}(0) \leftarrow 1 \longdiv { 1 } \\
& f^{\prime \prime}(x)=(-1)(-2)(-3)(1+x)^{-4} \text { and } f^{\prime \prime}(0) \leftarrow 1 \longdiv { 1 } \\
& \text { version: } 1.1
\end{aligned}
$$

$$
f^{(0)}(x)=(-1)(-2)(-3)(-4)(1+x)^{-3} \text { and } f^{(0)}(0) \quad(-1)^{3} \mid 4
$$

Following the pattern, we can write $f^{(x)}(0)=(-1)^{3} \mid \underline{n}$
Now substituting $f(0)=1, f^{\prime}(0)=1, f^{\prime \prime}(0)(1)^{3} \mid \underline{2}$,
$f^{\prime \prime}(0)=(-1)^{3} \mid 3, f^{(0)}(0)(1)^{3} \mid 4, \ldots, f^{(x)}(0)(1)^{3} \mid \underline{n}$ in the formula.
$f(x)=f(0)+f^{\prime}(0) x+\frac{f^{\prime}(0)}{12} x^{2}+\frac{f^{\prime \prime}(0)}{13} x^{3}+\frac{f^{(0)}(0)}{14} x^{4}=\ldots+\frac{f^{(x)}(0)}{1 \underline{n}} x^{2} \ldots$

$$
+\frac{f^{(x)}(0)}{1 \underline{n}} x^{2}+\ldots \text {, we have }
$$

$$
\frac{1}{1+x}=1+(-1) x+(-1)^{3} \frac{13}{12} x^{2}+(-1)^{3} \frac{13}{13} x^{3}+(-1)^{4} \frac{14}{14} x^{4}+\ldots+\frac{(-1)^{3} \mid \underline{n}}{1 \underline{n}} x^{4}+\ldots
$$

Thus, the Maclaurin series for $\frac{1}{1+x}$ is the geometric series with the first term 1 and common ratio -x .

Note: Applying the formula $x=\frac{n_{1}}{1-x}$, we have

$$
1-x+x_{1}-x_{1}+\ldots=\frac{1}{1-(-x)}=\frac{1}{1+x}
$$

Example 2: Find the Maclaurin series for $\sin x$
Solution: Let $f(x)=\sin x$. Then $f(0)=\sin 00$.

$$
\begin{aligned}
& f^{\prime}(x)=\cos x \text { and } f^{\prime}(0)=\cos 0=1 ; f^{\prime}(x)=\sin x \text { and } f^{\prime}(0) \quad \sin 0 \quad 0 \\
& f^{\prime \prime}(x)=-\cos x \text { and } f^{\prime \prime}(0)=-\cos 0=-1 ; f^{(0)}(x)=-\{-\sin x\}=-\sin x \\
& \text { and } f^{(0)}(0)=\sin (0)=0 \\
& f^{(3)}=(x)=\cos x \text { and } f^{(3)}(0)=\cos 0-1, f^{(0)}(x)=-\sin x \\
& \text { and } f^{(0)}(0)=0 ; f^{(3)} \quad \cos x \text { and } f^{(3)}(0) \quad 1
\end{aligned}
$$

Putting these values in the formula

$$
\begin{aligned}
& f(x)=f(0)+f^{\prime}(0) x+\frac{f^{\prime}(0)}{12} x^{2}+\frac{f^{\prime \prime}(0)}{13} x^{3}+\frac{f^{(0)}(0)}{14} x^{4}+\frac{f^{(3)}(0)}{15}+\ldots \text {, we have } \\
& \sin x=0 \quad 1 . x \quad \frac{0}{12} x^{2} \quad \frac{-1}{13} x^{3} \quad \frac{0}{14} x^{4} \quad \frac{1}{15} x^{5} \quad \frac{0}{16} x^{6} \quad \frac{-1}{15} x^{7} \quad \ldots \\
& \quad=x-\frac{x^{3}}{13}+\frac{x^{5}}{15}-\frac{x^{7}}{17}+\ldots \ldots
\end{aligned}
$$

Example 3: Expand $a^{x}$ in the Maclaurin series.

Solution: Let $f(x)=a^{x}$, then

$$
\begin{aligned}
& f^{\prime}(x)=a^{x} \ln a, f^{\prime \prime}(x) \quad a^{x}(\ln a)^{3}, f^{\prime \prime}(x) \quad a^{x}(\ln a)^{3} \\
& f^{(0)}(x)=a^{x}(\ln a)^{3}, \ldots, f^{(x)}(x) \quad a^{x}(\ln a)^{(x)}
\end{aligned}
$$

Putting $x=0$ in $f(x), f^{\prime}(x), f^{\prime \prime}(x), f^{(0)}(x), \ldots f^{(x)}(x)$, we get

$$
\begin{aligned}
& f(0)=a^{0}=1, f^{\prime}(0)=a^{0} \ln a=\ln a, f^{\prime}(0)=(\ln a)^{3}, f^{\prime \prime}(0) \quad(\ln a)^{3} \\
& f^{(0)}(0)=(\ln a)^{3}, \ldots, f^{(x)}(0) \quad(\ln a)^{x}
\end{aligned}
$$

Substituting these values in the formula

$$
\begin{aligned}
& f(x)=f(0)+f^{\prime}(0) x+\frac{f^{\prime}(0)}{12} x^{2}+\frac{f^{\prime \prime}(0)}{13} x^{3}+\ldots+\frac{f^{(x)}(0)}{1 \underline{n}} x^{4}+\ldots \text {, we have } \\
& a^{x}=1+(\ln a) . x+\frac{(\ln a)^{3}}{12} x^{2}+\frac{(\ln a)^{3}}{13} x^{3}+\ldots+\frac{(\ln a)^{7}}{1 \underline{n}} x^{4}+\ldots
\end{aligned}
$$

Note: If we put $0=\infty$ in the above expansion, we get

$$
\begin{aligned}
& e^{x}=1+x+\frac{x^{3}}{12}+\frac{x^{5}}{13}+\ldots+\frac{x^{7}}{1 \underline{n}}+\ldots \\
& \text { Replacing } x \text { by } 1 \text {, we have } \\
& e=1+1+\frac{1}{12}+\frac{1}{13}+\ldots+\frac{1}{1 \underline{n}}
\end{aligned}
$$

Example 4: $\quad$ Expand $(1+x)^{n}$ in the Maclaurin series.

Solution: Let $f(x)=(1+x)^{n}$, then

$$
\begin{aligned}
& f^{\prime}(x)=n(1+x)^{n-1}, \quad f^{\prime \prime}(x)=n(n-1)(1+x)^{n-2} \\
& f^{\prime \prime}(x)=n(n-1)(n-2)(1+x)^{n-3}, f^{(1)}(x)=n(n-1)(n-2)(n-3)(1+x)^{n-4}
\end{aligned}
$$

Putting $x=0$, we get

$$
\begin{aligned}
& f(0)=(1+0)^{2}=1, f^{\prime}(0)=n(1+0)^{n-1}=n \\
& f^{\prime}(0)=n(n-1)(1+0)^{n-2}=n(n-1) \\
& f^{\prime \prime}(0)=n(n-1)(n-2)(1+0)^{n-3}=n(n-1)(n-2) \\
& f^{(1)}(0)=n(n-1)(n-2)(n-3)(1+0)^{n-4}=n(n-1)(n-3)
\end{aligned}
$$

Substituting these values in the formula

$$
\begin{aligned}
& f(x)=f(0) \quad f^{\prime}(0) \mathrm{s} x \quad \frac{f^{\prime \prime}(0)}{\lfloor 2 \alpha^{2}} \quad \frac{f^{\prime \prime}(0)}{\lfloor 3 \alpha^{2}} \quad \ldots, \text { we have } \\
& (1+x)^{n} \neq 1 \quad n+x \quad \frac{n(n-1)}{\lfloor 2 \alpha^{2}} \quad \frac{n(n-1)(n-2)}{\lfloor 3 \alpha^{2}+\ldots}
\end{aligned}
$$