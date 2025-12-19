### 3.1.2 Distinguishing Between *dy* and $\delta y$

The tangent line is drawn to the graph of *y* = *f*(*x*) at *P*(*x*, *f*(*x*) and *MP* is the ordinate of *P*, that is, *MP* = *f*(*x*). (see Fig. 3.1)

Let $\delta x$ be small number, then the point *N* is located at *x* + $\delta x$ on the *x*-axis. Let the vertical line through *N* cut the tangent line at *T* and the graph of *f* at *Q*. Then the point *Q* is (*x* + $\delta x$, *f*(*x* + $\delta x*)), so

$$
d x = \delta x = PR
$$

and

$$
\delta y = RQ = RT + TQ
$$

$$
= \tan \varphi \delta x + TQ \qquad \left( \because \tan \varphi = \frac{RT}{PR} \right)
$$

where $\varphi$ is the angle which the tangent *PT* makes with the positive direction of the *x*-axis.

or

$$
\delta y = f'(x) dx + TQ \qquad \left( \therefore \tan \varphi \delta x = f'(x) \right)
$$

$$
\Rightarrow \quad \delta y = dy + TQ
$$

We see that $\delta y$ is the rise of *f* for a change $\delta x$ in *x* at *x* where as *dy* is the rise of the tangent line at *P* corresponding to the same change $\delta x$ in *x*.

The importance of the differential is obvious from the figure 3.1. As $\delta x$ approaches 0, the value of *dy* gets closer and closer to that of $\delta y$, so for small values of $\delta x$,

$$
dy = \delta y
$$

or

$$
dy = f'(x) dx \quad [\because dy = f'(x) dx] \qquad \text{(iv)}
$$

We know that

$$
\delta y = f(x + \delta x) - f(x) \qquad \text{ for } f(x + \delta x) = f(x) + \delta y
$$

But

$$
\delta y \approx dy, \text{ so}
$$

$$
f(x + \delta x) \approx f(x) + dy \qquad \text{(v)}
$$

$$
f(x + \delta x) \approx f(x) + f'(x) dx \qquad \text{(vi)}
$$

Example: Find $\delta y$ and $d y$ of the function defined as $f(x)=x^{2}, \quad$ when $x=2$ and $d x=0.01$

Solution: As $f(x)=x^{2}$, so $f^{\prime}(x)=2 x$

$$
\begin{aligned}
& \delta y=f(x+\delta x)-f(x)=(x+\delta x)^{2}-x^{2} \\
& =2 x \delta x+(\delta x)^{2}=2 x d x+(d x)^{2} \quad(\because \delta x=d x) \\
& \text { Thus } f(2+0.01)-f(2)=2(2)(0.01)+(0.01)^{2} \\
& =0.04+0.0001=0.0401 \text {, that is } \\
& \delta y=0.0401 \text { when } x=2 \text { and } \delta x=d x=0.01 \\
& \text { Also } d y=f^{\prime}(x) d x \\
& =2(2) \times(0.01)=0.04 \quad\left(\because f^{\prime}(x)=2 x, x=2 \text { and } d x=0.01\right) \\
& \text { Thus } \delta y-d y=0.0401-0.04=0.0001 \text {. }
\end{aligned}
$$