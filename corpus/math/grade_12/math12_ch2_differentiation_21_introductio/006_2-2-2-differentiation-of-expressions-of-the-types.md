### 2.2.2 DIFFERENTIATION OF EXPRESSIONS OF THE TYPES:

$$
(a x+b)^{n} \text { and } \frac{1}{(a x+b)^{n}}, \quad n=1,2,3 \ldots
$$

We find the derivatives of $(a x+b)^{n}$ and $\frac{1}{(a x+b)^{n}}$ from the first principle when $n \in N$
Example 1: Find from definition the differential coefficient of $(a x+b)^{n}$ w.r.t. ' $x$ ' when n is a positive integer.

Solution: Let $y=(a x+b)^{n},(n$ is a positive integer)
Then $y+\delta y=[a(x+\delta x)+b]^{n}=[(a x+b)+a \delta x]^{n}$
Using the binomial theorem we have

$$
\begin{aligned}
& y+\delta y=(a x \quad b)^{n} \quad\binom{n}{1}(a x \quad b)^{n-1}(a \delta x) \quad\binom{n}{2}(a x \quad b)^{n-1}(a \delta x)^{2}+\ldots \quad(a \delta x)^{n} \\
& \delta y=(y+\delta y)-y=\binom{n}{1}(a x+b)^{n-1}(a \delta x)+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2}(\delta x)^{2}+\ldots+a^{n}(\delta x)^{n} \\
& \quad=\delta x\left[\binom{n}{1}(a x+b)^{n-1} \cdot a+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2} \delta x+\ldots+a^{n}(\delta x)^{n-1}\right]
\end{aligned}
$$

So $\frac{\delta y}{\delta x}=\binom{n}{1}(a x+b)^{n-1} a+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2} \delta x+\ldots+a^{n}(\delta x)^{n-1}$
Taking limit when $\delta x \rightarrow 0$, we have

$$
\lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0}\left[\binom{n}{1}(a x+b)^{n-1} \cdot a+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2} \delta x+\ldots+a^{n}(\delta x)^{n-1}\right]
$$

Or $\frac{d y}{d x}=\binom{n}{1}(a x+b)^{n-1} \cdot a$ [All other terms tends to zero when $\delta x \rightarrow 0$ ]
Thus $\frac{d}{d x}(a x+b)^{n}=n(a x+b)^{n-1} \cdot a$

Example 2: Find from first principle, the derivative of $\frac{1}{(a x+b)^{2}}$ w.r.t. ' $x$ ',

Solution: Let $y=\frac{1}{(a x+b)^{2}}$ (when $n$ is a positive integer). Then

$$
\begin{aligned}
& y+\delta y=\frac{1}{\left[a(x+\delta x)+b\right]^{n}} \quad \text { and } \\
& \delta y=y+\delta y-y=\frac{1}{\left[(a x+b)+a \delta x\right]^{n}}-\frac{1}{(a x+b)^{n}} \\
& \text { or } \quad \delta y=\frac{(a x+b)^{n}-(a x+b+a \delta x)^{n}}{\left[(a x+b)+a \delta x\right]^{n}(a x+b)^{n}} \\
& \text { or } \quad \delta y=\frac{-1}{\left[(a x+b)+a \delta x\right]^{n}(a x+b)^{n}} \mathrm{x}\left[\left(\begin{array}{ll}
(a x & b)
\end{array}\right) a \delta x\right]^{n}\left(\begin{array}{ll}
(a x & b)
\end{array}\right)^{n} \text { (I) }
\end{aligned}
$$

Using the binomial theorem, we simplify the expression
$\left[(a x+b)+a \delta x\right]^{n}-(a x+b)^{n}$, That is,
$\left[(a x+b)+a \delta x\right]^{n}-(a x+b)^{n}=[(a x+b)^{n}+\binom{n}{1}(a x+b)^{n-1}(a \delta x)$

$$
\begin{gathered}
+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2}(\delta x)^{2}+\ldots+(a \delta x)^{n}] \\
=\binom{n}{1}(a x+b)^{n-1} \cdot a \delta x+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2}(\delta x)^{2}+\ldots+a^{n}(\delta x)^{n} \\
=\delta x\left[\binom{n}{1}(a x+b)^{n-1} \cdot a+\binom{n}{2}(a x+b)^{n-2} a^{2} \delta x+\ldots+a^{n}(\delta x)^{n-1}\right]
\end{gathered}
$$

## Now (I) becomes

$$
\delta y=\frac{\delta x}{[(a x+b)+a \delta x]^{n}(a x+b)^{n-1}}\binom{n}{1}(a \pi b)^{n-1} . a
$$

$$
+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2} \delta x+\ldots+\mathrm{a}^{n}(\delta x)^{n-1}]
$$

and $\frac{\delta y}{\delta x}=\frac{1}{[(a x+b)+a \delta x]^{n}(a x+b)^{n-1}}\binom{n}{1}(a \pi b)^{n-1} . a$

$$
+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2} \delta x+\ldots+\mathrm{a}^{n}(\delta x)^{n-1}]
$$

Using the product and sum rules of limits when $\delta x \rightarrow 0$, we have

$$
\frac{d y}{d x}=\frac{1}{(a x+b)^{n}(a x+b)^{n}}\binom{n}{1}(a \pi b)^{n-1} . a \quad\left(\frac{\square \lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\frac{d y}{d x} \text { and }}{\text { all other terms containing }}\right)
$$

or $\frac{d}{d x}=\left[\frac{1}{(a x+b)^{n}}\right]=\frac{-n a}{(a x+b)^{n-1}}=n(a x b)^{-(n+1)} . a$

## Exercise 2.2

1. Find from first principles, the derivatives of the following expressions w.r.t. their respective independent variables:
(i) $(a x+b)^{2}$
(ii) $(2 x+3)^{3}$
(iii) $(3 t+2)^{-2}$
(iv) $\frac{1}{(a x+b)^{2}}$
(v) $\frac{1}{(a z-b)^{2}}$