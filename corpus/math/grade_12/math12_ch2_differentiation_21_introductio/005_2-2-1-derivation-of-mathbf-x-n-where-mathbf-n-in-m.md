### 2.2.1 Derivation of $\mathbf{x}^{n}$ where $\mathbf{n} \in \mathbf{Z}$.

(a) We find the derivative of $x^{n}$ when $n$ is positive integer.
(a) Let $y=x^{n}$. Then

$$
y+\delta y=(x+\delta x)^{n}
$$

and $\quad \delta y=(x+\delta x)^{n}-x^{n}$
Using the binomial theorem, we have

$$
\delta y=\left[x^{n}+n x^{n-1} \cdot \delta x+\frac{n(n-1)}{\frac{1}{n} \cdot} x^{n-2}\left(\left(\delta x^{2} \cdot\right) \quad \cdot n \quad(\delta x)^{n}\right)\right] \quad x^{n}
$$

i.e., $\quad \delta y=\delta x\left[n x^{n-1}+\frac{n(n-1)}{\frac{1}{n} \cdot} x^{n-2} \cdot \delta x \quad \ldots \quad\left(\delta x\right)^{n-1}\right]$
Dividing both sides of (i) by $\delta x$, gives

$$
\frac{\delta y}{\delta x}=n x^{n-1}+\frac{n(n-1)}{\frac{1}{n} \cdot} x^{n-2} \cdot \delta x+\ldots \quad(\delta x)^{n-1}
$$

Note that each term on the right hand side of (ii) involves $\delta x$ except the first term, so taking the limit as $\delta x \rightarrow 0$, we get $\frac{d y}{d x}=n x^{n-1}$

As $y=\alpha^{n}$, so $\frac{d}{d x}\left(x^{n}\right) \quad n \cdot x^{n-1}$

$$
y=x^{n}
$$

Note: If $n=0$, then the formula $\frac{d}{d x}\left(x^{n}\right)=n x^{n-1}$ reduces to $\frac{d}{d x}\left(x^{0}\right)=0 x^{0-1}=0$ i.e., $\frac{d}{d x}(1)=0$ which is correct by example 1 part (a).
(b) Let $y=x^{n}$ where $n$ is a negative integer.

Let $n=-m$ ( $m$ is a positive integer). Then

$$
y=x^{-m}=\frac{1}{x^{m}}
$$

and $\quad y+\delta y=\frac{1}{(x+\delta x)^{m}}$
Subtracting (i) from (ii). gives

$$
\begin{aligned}
& \delta y=\frac{1}{(x+\delta x)^{m}}-\frac{1}{x^{m}}=\frac{x^{m}-(x+\delta x)^{m}}{x^{m}(x+\delta x)^{m}} \\
= & \frac{x^{m}-\left(x^{m}+m x^{m-1} \delta x+\frac{m(m-1)}{\frac{1}{n} \cdot} x^{m-2}(\delta x)^{2}+\ldots+(\delta x)^{m}\right]}{x^{m}(x+\delta x)^{m}} \\
& \quad \text { (expanding }(x+\delta x)^{m} \text { by binomial theorem) } \\
= & \frac{-\delta x\left(m x^{m-1}+\frac{m(m-1)}{\frac{1}{n} \cdot} x^{m-2} \delta x+\ldots+(\delta x)^{m-1}\right)}{x^{m}(x+\delta x)^{m}} \\
& \text { and } \frac{\delta y}{\delta x}=\frac{-1}{x^{m}(x+\delta x)^{m}}\left(m x^{m-1}+\frac{m(m-1)}{\frac{1}{n} \cdot} x^{m-2} \cdot \delta x \quad \ldots \quad(\delta x)^{m-1}\right)
\end{aligned}
$$

Taking limit when $\delta x \rightarrow 0$, we get

$$
\frac{d y}{d x}=\frac{-1}{x^{m} \cdot x^{n}}\left(m x^{m-1}\right) \quad \text { (all terms containing } \delta x \text {,vanish) }
$$

$$
\begin{aligned}
& =(-m) x^{m-1} \cdot x^{-2 m}=(-m) x^{(-m)+1}=n x^{n-1} \quad[\because m-n] \\
& \text { or } \quad \frac{d}{d x}(x)^{n}=n x^{n-1}
\end{aligned}
$$

So far we have proved that $\frac{d}{d x}[x]^{n}=n x^{n-1}$, if $n \in Z$
The above rule holds if $n \in Q-Z$
For example $\frac{d}{d x}\left(x^{\frac{2}{3}}\right)=\frac{2}{3} x^{\frac{2}{3}-1}=\frac{2}{3 x^{\frac{1}{3}}}$
The proof of $\frac{d}{d x}\left[x^{n}\right]=n x^{n-1}$ when $n \in Q-Z$ is left as an exercise.

Note that $\frac{d}{d x}\left[x^{n}\right]=n x^{n-1}$ is called power rule.

## Exercise 2.1

1. Find by definition, the derivatives w.r.t ' $x$ ' of the following functions defined as:
(i) $2 x^{2}+1$
(ii) $2-\sqrt{x}$
(iii) $\frac{1}{\sqrt{x}}$
(iv) $\frac{1}{x^{2}}$
(v) $\frac{1}{x-a}$
(vi) $x(x-3)$
(vii) $\frac{2}{x^{4}}$
(viii) $(x+4)^{\frac{1}{2}}$
(ix) $x^{\frac{2}{3}}$
(xi) $x^{m}, m \in N$
(xii) $\frac{1}{x^{n}, m \in N}$
(xiii) $x^{4 n}$
(xiv) $x^{-100}$
2. Find $\frac{d y}{d x}$ from first principle if
(i) $\sqrt{x+2}$
(ii) $\frac{1}{\sqrt{x+a}}$
version: 1.1