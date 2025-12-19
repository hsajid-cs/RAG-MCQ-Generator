### 2.17 TAILOR SERIES EXPANSIONS OF FUNCTIONS:

If $f$ is defined in the interval containing ' $\alpha$ ' and its derivatives of all orders exist at $x=\alpha$, then we can expand $f(x)$ as

$$
\begin{aligned}
f(x)= & f(a)+f^{\prime}(a)(x-a)+\frac{f^{\prime}(a)}{\lfloor 2}(x-a)^{2}+\frac{f^{\prime \prime}(a)}{\lfloor 3}(x-a)^{3} \\
& +\frac{f^{(1)}(a)}{\lfloor 4}(x-a)^{4}+\ldots+\frac{f^{(n)}(a)}{\lfloor n}(x-a)^{n}+\ldots
\end{aligned}
$$

Let $\quad f(x)=a_{0}+a_{1}(x-a)+a_{2}(x-a)^{2}+a_{3}(x-a)^{3}+a_{4}(x-a)^{4}+\ldots$ $+a_{n}(x-a)^{n}+\ldots$
Obviously $f(a)=a_{0}(\cdot ;$ putting $x=a$, all other terms vanish $)$

$$
\begin{aligned}
& f^{\prime}(x) \neq a_{1} \quad 2 a_{2}(x+a) \quad 3 a_{3}(x-a)^{2} \quad 4 a_{4}(x-a)^{3}+\ldots \quad n a_{5}(x-a)^{n-1} \quad \ldots \\
& f^{\prime \prime}(x)=2 a_{1}+6 a_{1}(x-a)+12 a_{4}(x-a)^{3}+\ldots+n(n-1) a_{n}(x-a)^{n-2}+\ldots \\
& f^{\prime \prime \prime}(x)=6 a_{1}+24 a_{4}(x-a)+\ldots \ldots
\end{aligned}
$$

Putting $x=a$, we get $f^{\prime \prime}(a)=a_{1} ; f^{\prime \prime \prime}(a)=2 a_{2} \Rightarrow a_{2}=\frac{f^{\prime \prime \prime}(a)}{\lfloor 2} ;=f^{\prime \prime \prime \prime}(a) \quad 6 a_{3}$
$\Rightarrow \quad a_{3}=\frac{f^{\prime \prime \prime \prime}(a)}{\lfloor 3}$

Following the above pattern, we have $\quad \frac{f^{(1)}(a)}{\lfloor}$
Substituting the values of $a_{0}, a_{1}, a_{2}, a_{3}, \ldots$, we get

$$
\begin{aligned}
f(x)=f(a)+f^{\prime}(a)(x-a)+\frac{f^{\prime \prime \prime}(a)}{\lfloor 2}(x-a)^{2}+\frac{f^{\prime \prime \prime \prime}(a)}{\lfloor 3}(x-a)^{3}+\ldots \\
+\frac{f^{(n)}(a)}{\lfloor n}(x-a)^{n}+\ldots
\end{aligned}
$$

This expansion is the Taylor series for $f$ at $x=a$. The expansionisonly valid if it is convergent.

If $\sigma=0$, then the above expansion becomes

$$
f(x)=f(0)+f^{\prime}(0) x+\frac{f^{\prime \prime \prime}(0)}{\lfloor 2} x^{2}+\frac{f^{\prime \prime \prime}(0)}{\lfloor 3} x^{3}+\ldots+\frac{f^{(n)}(0)}{\lfloor n} x^{n}+\ldots
$$

which is the Maclaurin series for $f$ at $x=a$.
Replacing $x$ by $x+h$ and $\alpha$ by $x$, the expansion in (A) can be written as
$f(x+h)=f(x)+f^{\prime}(x) h+\frac{f^{\prime \prime \prime}(x)}{\lfloor 2} h^{2}+\frac{f^{\prime \prime \prime \prime}(x)}{\lfloor 3} h^{3}+\ldots+\frac{f^{(n)}(x)}{\lfloor n} h^{n}+\ldots$ (B)
The expansions in (B) is termed as Taylor's Theorem and can be stated as: If $x$ and $h$ are two independent quantities and $f(x+h)$ can be expanded in ascending power of $h$ as an infinite series, then

$$
f(x+h)=f(x)+f^{\prime}(x) h+\frac{f^{\prime \prime}(x)}{\frac{1}{2}} h^{2}+\frac{f^{\prime \prime \prime}(x)}{\frac{1}{2}} h^{2}+\ldots+\frac{f^{(n)}(x)}{\frac{1}{2}} h^{n}+\ldots
$$

Example 1: Find the Taylor series expansion of $\ln (1+x)$ at $x=2$.
Solution: Let $f(x)=\ln (1+x)$, then $f(2)=\ln (1+2)=\ln 3$
Finding he successive derivatives of $\ln (1+x)$ and evaluating them at $x=2$

$$
\begin{aligned}
& f^{\prime}(x)=\frac{1}{1+x} \quad \text { and } f^{\prime}(2)=\frac{1}{1+2}=\frac{1}{3} \\
& f^{\prime \prime}(x)=(-1)(-2)(1+x)^{-\frac{1}{3}} \quad \text { and } f^{\prime \prime}(2)=(-1+2)^{-2}=-\frac{1}{9} \\
& f^{\prime \prime \prime}(x)=(-1)(-2)(1+x)^{-3} \quad \text { and } f^{\prime \prime}(2)=\frac{1}{2} \cdot(1+2)^{-2}=\frac{\frac{1}{2}}{27} \\
& f^{(n)}(x)=(-1)(-2)(-3)(1+x)^{-4}=(-1)^{2} \frac{1}{2}(1+x)^{-4} \text { and } f^{(n)}(2)=\frac{\frac{1}{3}}{81}
\end{aligned}
$$

The Taylor series expansions of $f$ at $x=a$ is

$$
f(x)=f(a)+f^{\prime}(a) \cdot(x-a)+\frac{f^{\prime}(a)}{\frac{1}{2}}(x-a)^{2}+\frac{f^{\prime \prime}(a)}{\frac{1}{2}}(x-a)^{3}+\ldots
$$

Now substituting the relative values, we have

$$
\begin{aligned}
& \ln (1+x)=\ln 3+\frac{1}{3}(x-2)+\frac{-1}{\frac{1}{2}}(x-2)^{2}+\frac{\frac{12}{27}}{\frac{1}{2}}(x-2)^{3}+\frac{-\frac{13}{81}}{\frac{1}{2}}(x-2)^{4}+\ldots \\
& =\ln 3+\frac{x-2}{1.3}-\frac{(x-2)^{2}}{2.3^{2}}+\frac{(x-2)^{2}}{3.3^{2}}-\frac{(x-2)^{3}}{4.3^{3}}+\ldots
\end{aligned}
$$

Example 2: Use the Taylor series expansion to find the value of $\sin 31^{\circ}$.
Solution: We take $a=30^{\circ}=\frac{\pi}{6}$

$$
\text { Let } f(x)=\sin x \text {, then } F\left(\frac{\pi}{6}\right) \quad \min \frac{\pi}{6} \quad \frac{1}{2}
$$

Now taking the successive derivative of $\sin x$ and evaluating them at $\frac{\pi}{6}$, we have

$$
\begin{array}{ll}
f^{\prime}(x)=\cos x & \text { and } f^{\prime}\left(\frac{\pi}{6}\right)=\cos \frac{\pi}{6}=\frac{\sqrt{3}}{2} \\
f^{\prime \prime \prime}(x)=-\sin x & \text { and } f^{\prime}\left(\frac{\pi}{6}\right)=\sin \frac{\pi}{6}-\frac{-1}{2} \\
f^{\prime \prime}(x)=-\cos x & \text { and } f^{\prime}\left(\frac{\pi}{6}\right)=\cos \frac{\pi}{6}-\frac{\sqrt{3}}{2} \\
f^{(n)}(x)=-(- \sin x)=\sin x & \text { and } f^{(n)}\left(\frac{\pi}{6}\right)=\sin \frac{\pi}{6}=\frac{1}{2}
\end{array}
$$

Thus the Taylor series expansion at $a=\frac{\pi}{6}$ is

$$
\begin{aligned}
\sin x= & \frac{1}{2}+\frac{\sqrt{3}}{2}\left(x-\frac{\pi}{6}\right)+\frac{-\frac{1}{2}}{\frac{1}{2}}\left(x-\frac{\pi}{6}\right)^{2}+\frac{-\frac{\sqrt{3}}{2}}{\frac{1}{2}}\left(x-\frac{\pi}{6}\right)^{3}+\ldots \\
& =\frac{1}{2}+\frac{\sqrt{3}}{2}\left(x-\frac{\pi}{6}\right)-\frac{1}{2 \frac{1}{2}}\left(x-\frac{\pi}{6}\right)^{2}-\frac{\sqrt{3}}{2 \frac{1}{2}}\left(x-\frac{\pi}{6}\right)^{3}+\ldots \\
\text { For } x= & 31^{\circ} \cdot x \quad \frac{\pi}{6}=\left(34^{\circ} \quad 30^{\circ}\right) \sim 4^{\circ} \quad .017455 \\
\sin 31^{\circ} & =\frac{1}{2}+\frac{\sqrt{3}}{2}(.017455)-\frac{1}{4}(.017455)^{2}-\frac{\sqrt{3}}{12}(.017455)^{3} \\
& \approx .5+.015116-0.000076 \approx .5150
\end{aligned}
$$

Example 3: $\quad$ Prove that $e^{a+b}=e^{a}\left(1+h+\frac{h^{2}}{12}+\frac{h^{3}}{12}+\ldots\right)$

Solution: Let $f(x+h)=e^{a+b_{0}}$ then $f(x) \quad e^{x} \quad$...(i)
By successive derivatives of (i) w.r.t ' $x$ ' we have

$$
f^{\prime}(x)=e^{x}, f^{\prime \prime}(x)=e^{x}, f^{\prime \prime}(x)=e^{x} \quad \text { etc. }
$$

By Taylor's Theorem we have

$$
f(x+h)=f(x)+h f^{\prime}(x)+\frac{h^{2}}{12} f^{\prime \prime \prime}(x)+\frac{h^{3}}{12}+f^{\prime \prime \prime \prime}(x)+\ldots
$$

Putting the relative values, we get

$$
\begin{aligned}
e^{x+h} & =e^{x}+h e^{x}+\frac{h^{2}}{12} e^{x}+\frac{h^{3}}{12} e^{x}+\ldots \\
& =e^{x}\left[1+h+\frac{h^{2}}{12}+\frac{h^{3}}{12}+\ldots\right]
\end{aligned}
$$

## EXERCISE 2.8

1. Apply the Maclaurin series expansion to prove that:
(i) $\ln (1+x)=x-\frac{x^{2}}{2}+\frac{x^{3}}{2}-\frac{x^{4}}{2}+\ldots \ldots$
(ii) $\cos x=1-\frac{x^{2}}{12}+\frac{x^{4}}{14}-\frac{x^{6}}{16}+\ldots \ldots$
(iii) $\sqrt{1+x}=1+\frac{x}{2}-\frac{x^{2}}{8}+\frac{x^{3}}{16}+\ldots \ldots$
(iv) $e^{x} \quad=1+x+\frac{x^{2}}{12}+\frac{x^{3}}{13}+\ldots \ldots$
(v) $e^{2 x}=1+2 x+\frac{4 x^{2}}{12}-\frac{8 x^{3}}{13}+\ldots \ldots$
2. Show that:
$\cos (x+h)=\cos x-h \sin x-\frac{h^{2}}{12} \cos x+\frac{h^{3}}{12} \sin x+\ldots \ldots$
and evaluate $\cos 61^{\circ}$.
3. Show that $2^{x+h}=2^{x}\{1+(\ln 2) h+\frac{(\ln 2)^{2} h^{2}}{12}+\frac{(\ln 2)^{3} h^{3}}{12}+\ldots\}$

## 2.18 GEOMETRICAL INTERPRETATION OF A DERIVATIVE

Let $A B$ be the arc of the graph of $f$ defined by the equation $y=f(x)$.
Let $P(x, f(x))$ and $Q(x+\delta x, f(x+\delta x))$ be two neighbouring points on the arc $A B$ where $x$, $x+\delta x \in D_{f}$.

The line $P Q$ is secant of the curve and it makes $\angle X S Q$ with the positive direction of the $x$-axis. (See the figure 2.21.1)

Drawing the ordinates $P M, Q N$ and perpendicular $P R$ to $N Q$, we have
$R Q=N Q-N R=N Q-M P=f(x+\delta x)-f(x)$
FIGURE 2.21.1
and $P R=M N=O N-O M=x+\delta x-x=\delta x$
Thus $\tan m \angle X S Q=\tan m \angle R P Q$
$-\frac{R Q}{P R}=\frac{f(x+\delta x)-f(x)}{\delta x}$
Revolving the secant line $P Q$ about $P$ towards $P$, some of its successive positions $P Q_{i}, P Q_{j}, P Q_{k}, \ldots$ are shown in the figure 2.21.2. Points $Q_{i}(i=1,2,3, \ldots)$ are getting closer and closer to the point $P$ and $P R$, i.e; $\delta x_{i}(i=1,2,3, \ldots)$ are approaching to zero.

In other words we can say that the revolving secant line approaches the tangent line $P T$ as its limiting position at $P$ while $\delta x$ approaches zero, that is,
$\tan m \angle X S Q \rightarrow \tan m \angle X T P$ when $\delta \mathrm{x} \rightarrow 0$
or $\frac{f(x+\delta x)-f(x)}{\delta x} \rightarrow \tan m \angle X T P$ as $\delta x \rightarrow 0$
so $\lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}=\tan m \angle X T P$
$$
\text { or } \quad f^{\prime}(x)=\tan m \angle X T P
$$

Thus the slope of the tangent line to the graph of $f$ at $(x, f(x))$ is $f^{\prime}(x)$.
Example 1: $\quad$ Discuss the tangent line to the graph of the function $|x|$ at $x=0$.

Solution: Let $\quad f(x)=|x|$

$$
\begin{aligned}
& f(0)=|0|=0 \quad \text { and } \\
& f(0+\delta x)=|0+\delta x|=|\delta x| \\
& \text { so } \quad f(0+\delta x)-f(0)=|\delta x|-0 \\
& \text { and } \quad \frac{f(0+\delta x)-f(0)}{\delta x}=\frac{|\delta x|}{\delta x} \\
& \text { Thus } f^{\prime}(0)=\lim _{\delta x \rightarrow 0} \frac{|\delta x|}{\delta x} \\
& \text { Because }|\delta x|=\delta x \quad \text { when } \delta x>0 \\
& \text { and } \quad|\delta x|=-\delta x \quad \text { when } \delta x<0
\end{aligned}
$$

so we consider one-sided limits

$$
\begin{aligned}
& \lim _{\delta x \rightarrow 0^{+}} \frac{|\delta x|}{\delta x}=\lim _{\delta x \rightarrow 0^{-}} \frac{\delta x}{\delta x}=1 \\
& \text { and } \lim _{\delta x \rightarrow 0^{-}} \frac{|\delta x|}{\delta x}=\lim _{\delta x \rightarrow 0^{-}} \frac{-\delta x}{\delta x}-1
\end{aligned}
$$

The right hand and left hand limits are not equal, therefore, the $\lim _{\delta x \rightarrow 0^{-}} \frac{|\delta x|}{\delta x}$ does not exist.

This means that $f^{\prime}(0)$, the derivative of $f$ at $x=0$ does not exist and there is no tangent line to the graph of $f$ and $x=0$
(see the figure 2.21.3).

Example 2: Find the equations of the tangents to the curve $x^{2}-y^{2}-6 y=0$ at the point whose abscissa is 4 .

Solution. Given that $x^{2}-y^{2}-6 y=0$
We first find the $y$-coordinates of the points at which the equations of the tangents are to be found. Putting $x=4$ is (i) gives

$$
\begin{aligned}
& 16-y^{2}-6 y=0 \quad \Rightarrow y^{2}+6 y-16=0 \\
& \text { or } y=\frac{-6 \pm \sqrt{36+64}}{2}=\frac{-6 \pm \sqrt{100}}{2}=\frac{-6 \pm 10}{2}, \text { that is, } \\
& y=\frac{-6+10}{2}=\frac{4}{2}=2 \quad \text { or } \quad y=\frac{-6-10}{2}=\frac{-16}{2}=-8
\end{aligned}
$$

Thus the points are $(4,2)$ and $(4,-8)$.
Differentiating (i) w.r.t. ' $x$ ' we have

$$
2 x-2 y \frac{d y}{d x}-6 \frac{d y}{d x}=0 \quad \Rightarrow 2 \frac{d y}{d x}(y+3)=2 x \quad \Rightarrow \frac{d y}{d x}=\frac{x}{y+3}
$$

The slope of the tangent to (i) at $(4,2)==\frac{4}{2+3}=\frac{4}{5}$.
Therefore, the equation of the tangent to (i) at $(4,2)$ is

$$
\begin{aligned}
& y-2=\frac{4}{5}(x-4) \quad \Rightarrow 5 y-10=4 x-16 \\
& \text { or } \quad 5 y=4 x-6
\end{aligned}
$$

The slope of the tangent to (i) at $(4,-8)=\frac{4}{-8+3}=\frac{4}{5}$.
Therefore the equation of the tangent to (i) at $(4,-8)$ is

$$
\begin{aligned}
& y-(-8)=-\frac{4}{5}(x-4) \\
& 5 y+40=-4 x+16 \quad \Rightarrow 4 x+5 y+24=0
\end{aligned}
$$

## 2.19 INCREASING AND DECREASING FUNCTIONS

Let $f$ be defined on an interval $(a, b)$ and let $x_{1}, x_{2} \in(a, b)$. Then
(i) $f$ is increasing on the interval $(a, b)$ if $f\left(x_{2}\right)>f\left(x_{1}\right)$ whenever $x_{2}>x_{1}$
(ii) $f$ is decreasing on the interval $(a, b)$ if $f\left(x_{2}\right)<f\left(x_{1}\right)$ whenever $x_{2}>x_{1}$
We see that a differentiable function $f$ is increasing on $(a, b)$ if tangent lines to its graph at all points $(x, f(x))$ where $x \in(a, b)$ have positive slopes, that is,
$f^{\prime}(x)>0$ for all $x$ such that $a<x<b$
and $f$ is decreasing on $(a, b)$ if tangent lines to its graph at all points $(x, f(x))$ where $x \in(a, b)$, have negative slopes, that is, $f^{\prime}(x)<0$ for all $x$ such that $a<x<b$

Now we state the above observation in the following theorem.

## Theorem:

Let $f$ be a differentiable function on the open interval (a,b). Then
(i) $f$ is increasing on $(a, b)$ if $f^{\prime}(x)>0$ for each $x \in(a, b)$
(ii) $f$ is decreasing on $(a, b)$ if $f^{\prime}(x)<0$ for each $x \in(a, b)$

Let $f(x)=x^{2}$, then

$$
f\left(x_{2}\right)-f\left(x_{1}\right)=x_{2}^{2}-x_{1}^{2}=\left(x_{2}-x_{1}\right)\left(x_{2}+x_{1}\right)
$$

If $\quad x_{1}, x_{2} \in(-\infty, 0)$ and $x_{2}>x_{1}$, then
version: 1.1

$$
\begin{aligned}
& f\left(x_{2}\right)-f\left(x_{1}\right)<0 \quad\left(\because x_{2}-x_{1}>0 \text { and } x_{2}+x_{1}<0\right) \\
& \Rightarrow f\left(x_{2}\right)<f\left(x_{1}\right) \\
& \Rightarrow f \text { is decreasing on the interval }(-\infty, 0) \\
& \text { If } x_{1}, x_{2} \in(0, \infty) \text { and } x_{2}>x_{1} \text {, then } \\
& f\left(x_{2}\right)-f\left(x_{1}\right)>0 \quad\left(\because x_{2}-x_{1}>0 \text { and } x_{2}+x_{1}>0\right) \\
& \Rightarrow f\left(x_{2}\right)>f\left(x_{1}\right) \\
& \Rightarrow f \text { is increasing on the interval }(0, \infty)
\end{aligned}
$$

Here $f^{\prime}(x)=2 x$ and $f^{\prime}(\mathbf{x})-\mathbf{0}$ for all $x \quad(\quad, 0)$, therefore,
$f$ is decreasing on the interval $(-\infty, 0)$
Also $f^{\prime}(x)>0$ for all $x \in(0, \infty)$, so $f$ is increasing on the interval $(0, \infty)$.
From the above theorem we can conclude that

1. $f^{\prime}\left(x_{1}\right)<0 \Rightarrow f$ is decreasing at $x_{1}$
2. $f^{\prime}\left(x_{1}\right)=0 \Rightarrow f$ is neither increasing nor decreasing at $x_{1}$
3. $f^{\prime}\left(x_{1}\right)>0 \Rightarrow f$ is increasing at $x_{1}$

Now we illustrate the ideas discussed so far considering the function $f$ defined as
$f(x)=4 x-x^{2}$
To draw the graph of $f$, we form a table of some ordered pairs which belongs to $f$

| $x$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $y=f(x)$ | -5 | 0 | 3 | 4 | 3 | 0 | -5 |

From the graph of *f*, it is obvious that *y* rises from 0 to 4 as *x* increases from 0 to 2 and *y* falls from 4 to 0 as *x* increases from 2 to 4.

In other words, we can say that the function *f* defined as in (I) is increasing in the interval 0 < *x* < 2 and is decreasing in the interval 2 < *x* < 4.

The slope of the tangent to the graph of *f* at any point in the interval 0 < *x* < 2, in which the function *f* is increasing is positive because it makes an acute angle with the positive direction of *x*-axis. (See the tangent line to the graph of *f* at (1, 3)).

But the slope of the tangent line to the graph of *f* at any point in the interval 2 < *x* < 4 in which the function *f* is decreasing is negative as it makes an obtuse angle with the positive direction of *x*-axis. (See the tangent line to the graph of *f* at (3, 3)).

As we know that the slope of the tangent line to the graph of *f* at (*x*, *f*(*x*)) is *f* (*x*), so the derivative of the function *f* i.e., *f* (*x*), is positive in the interval in which *f* is increasing and *f* (*x*), is negative in the interval in which *f* is decreasing.

The function *f* under consideration is actually increasing at each *x* for which *f* (*x*) > 0.

$$
\text{i.e. } 4 - 2x > 0 \qquad \Rightarrow -2x > -4 \qquad \Rightarrow x < 2
$$

Thus it is increasing in the interval (-∞, 2). Similarly we can show that it is decreasing, in the interval (2, ∞).

Now we give an analytical approach to the above discussion.

Let *f* be an increasing function in some interval in which it is differentiable. Let *x* and *x* + *δx* be two, points in that interval such that *x* + *δx* > *x*.

As the function *f* is increasing in the interval, it conveys the fact that *f*(*x* + *δx*) > *f*(*x*).

Consequently we have, *f*(*x* + *δx*) - *f*(*x*) > 0 and (*x* + *δx*) - *x* > 0, that is,

$$
f(x + \deltax) - f(x) > 0 \text{ and } \deltax > 0
$$

or

$$
\frac{f(x + \deltax) - f(x)}{\delta x} > 0
$$

The above difference quotient becomes one-sided limit

$$
\lim_{\deltax \to 0} \frac{f(x + \deltax) - f(x)}{\delta x}
$$

As *f* is differentiable, so *f* (*x*) exists and one sided limit must equal to *f* (*x*). Thus *f* (*x*) > 0.