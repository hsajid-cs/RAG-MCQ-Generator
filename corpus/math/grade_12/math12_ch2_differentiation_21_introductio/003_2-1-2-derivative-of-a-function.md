### 2.1.2 Derivative of a Function

Let $f$ be a real valued function continuous in the interval $\left(x, x_{i}\right) \subseteq D_{f}$ (the domain of $f$ ), then

$$ \text { difference quotient } \frac{f\left(x_{i}\right)-f(x)}{x_{i}-x} $$

represents the average rate of change in the value of $f$ with respect to the change $x_{i}-x$ in the value of independent variable $x$. If $x_{i}$, approaches to $x$, then

$$
\lim _{x_{i} \rightarrow x} \frac{f\left(x_{i}\right)-f(x)}{x_{i}-x}
$$

provided this limit exists, is called the instantaneous rate of change of $f$ with respect to $x$ at $x$ and is written as $f^{\prime}(x)$. If $x_{i}=x+\delta x$ i.e., $x_{i}-x=\delta x$, then the expression (i) can be expressed as

$$
\frac{f(x+\delta x)-f(x)}{\delta x}
$$

and

$$
\lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}
$$

provided the limit exists, is defined to be the derivative of $f$ (or differential coefficient of $f$ ) with respect to $x$ at $x$ and is denoted by $f^{\prime}(x)$ (read as "f-prime of $x$ "). The domain of $f^{\prime}$ consists of all $x$ for which the limit exists. If $x \in D_{f}$ and $f^{\prime}(x)$ exists, then $f$ is said to be differentiable at $x$. The process of finding $f^{\prime}$ is called differentiation.

## Notation for Derivative

Several notations are used for derivatives. We have used the functional symbol $f^{\prime}(x)$, for the derivative of $f$ at $x$. For the function $y=f(x)$.

$$ y+\delta y=f(x+\delta x) $$

where $\delta y$ is the increment of $y$ (change in the value of $y$ ) corresponding to $\delta x$, the change in the value of $x$, then

$$ \delta y=f(x+\delta x)-f(x) $$

Dividing both the sides of (iv) by $\delta x$, we get

$$ \frac{\delta y}{\delta x}=\frac{f(x+\delta x)-f(x)}{\delta x} $$

Taking limit of both the sides of (v) as $\delta x \rightarrow 0$, we have

$$ \begin{aligned} & \lim *{x \rightarrow \infty} \frac{\delta y}{\delta x}=\lim _{x \rightarrow \infty} \frac{f(x+\delta x)-f(x)}{\delta x} \ & \text { (vi) } \ & \frac{\lim }{x \rightarrow \infty} \frac{\delta y}{\delta x} \text { is denoted by } \frac{d y}{d x}, \text { so (vi) is written as } \frac{d y}{d x}=f^{\prime}(x) \end{aligned} $$

Note: The symbol $\frac{d y}{d x}$ is used for the derivative of $y$ with respect to $x$ and here it is not a quotient of $d y$ and $d x . \frac{d y}{d x}$ is also denoted by $y^{\prime}$.

Now we write, in a table the notations for the derivative of $y=f(x)$ used by different mathematicians:

|  Name of
Mathematician | Leibniz | Newton | Lagrange | Cauchy  |
| --- | --- | --- | --- | --- |
|  Notation used for derivative | $\frac{d y}{d x} \quad \frac{d f}{d x}$ | $f(x)$ | $f^{\prime}(x)$ | $D f(x)$  |

If we replace $x+\delta x$ by $x$ and $x$ by a, then the expression $f(x+\delta x)-f(x)$ becomes $f(x)-f(a)$, and the change $\delta x$ in the independent variable, in this case, is $x-a$.

So the expression $\frac{f(x+\delta x)-f(x)}{\delta x}$ is written as $\frac{f(x)-f(a)}{x-a} \quad$ (vii) Taking the limit of the expressiom(vii) when $x \rightarrow a$, gives

$$ \lim _{x \rightarrow a} \frac{f(x)-f(a)}{x-a}=f^{\prime}(a) \text {. Here } f^{\prime}(a) $$

is called the derivative of $f$ at $x=a$.