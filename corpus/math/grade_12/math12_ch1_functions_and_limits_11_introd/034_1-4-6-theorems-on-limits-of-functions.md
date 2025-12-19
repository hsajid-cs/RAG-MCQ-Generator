### 1.4.6 Theorems on Limits of Functions

Let $f$ and $g$ be two functions, for which $\underline{\operatorname{Lim}} f(x)=\mathrm{L}$ and $\underline{\operatorname{Lim}} \mathrm{g}(x)=\mathrm{M}$, then
Theorem 1: The limit of the sum of two functions is equal to the sum of their limits.

$$
\underline{\operatorname{Lim}}_{x \rightarrow 0}[f(x)+\mathrm{g}(x)]=\underline{\operatorname{Lim}}_{x \rightarrow 0} f(x)+\underline{\operatorname{Lim}}_{x \rightarrow 0} \mathrm{~g}(x)=\mathrm{L}+\mathrm{M}
$$

For example, $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0}(x+5)=\underline{\operatorname{Lim}}_{x \rightarrow 0} x+\underline{\operatorname{Lim}}_{x \rightarrow 0} 5=1+5=6$

## Theorem 2: The limit of the difference of two functions is equal to the difference of their limits.

$$
\underline{\operatorname{Lim}}_{x \rightarrow 0}[f(x)-\mathrm{g}(x)]=\underline{\operatorname{Lim}}_{x \rightarrow 0} f(x)-\underline{\operatorname{Lim}}_{x \rightarrow 0} \mathrm{~g}(x)=\mathrm{L}-\mathrm{M}
$$

For example, $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0}(x-5)=\underline{\operatorname{Lim}}_{x \rightarrow 0} x-\underline{\operatorname{Lim}}_{x \rightarrow 0} 5=3-5=-2$
Theorem 3: If $k$ is any real number, then

$$
\underline{\operatorname{Lim}}_{k \rightarrow k}[k f(x)]=k \underline{\operatorname{Lim}}_{k \rightarrow k} f(x)=k L
$$

For example: $\quad \underline{\operatorname{Lim}}_{k \rightarrow 0}(3 x)=3 \underline{\operatorname{Lim}}_{k \rightarrow 0}(x)=3(2)=6$
Theorem 4: The limit of the product of the functions is equal to the product of their limits.

$$
\underline{\operatorname{Lim}}_{x \rightarrow 0}[f(x) \mathrm{g}(x)]=\left[\underline{\operatorname{Lim}}_{x \rightarrow 0} f(x)\right]\left[\underline{\operatorname{Lim}}_{x \rightarrow 0} \mathrm{~g}(x)\right]=\mathrm{LM}
$$

For example: $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0}(2 x)(x+4)=\left[\underline{\operatorname{Lim}}_{x \rightarrow 0}(2 x)\right]\left[\underline{\operatorname{Lim}}_{x \rightarrow 0}(x+4)\right]=(2)(5)=10$
Theorem 5: The limit of the quotient of the functions is equal to the quotient of their limits provided the limit of the denominator is non-zero.

$$
\underline{\operatorname{Lim}}_{x \rightarrow 0}\left(\frac{f(x)}{\mathrm{g}(x)}\right)=\frac{\underline{\operatorname{Lim}}_{x \rightarrow 0} f(x)}{\underline{\operatorname{Lim}}_{x \rightarrow 0} \mathrm{~g}(x)}=\frac{\mathrm{L}}{\mathrm{M}}, \quad \mathrm{~g}(x) \neq 0, \mathrm{M} \neq 0
$$

For example: $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0}\left(\frac{3 x+4}{x+3}\right)=\frac{\underline{\operatorname{Lim}}_{x \rightarrow 0}(3 x+4)}{\underline{\operatorname{Lim}}_{x \rightarrow 0}(x+3)}=\frac{6+4}{2+3}=\frac{10}{5}=2$
Theorem 6: Limit of $[f(x)]^{\prime \prime}$, where $\mathbf{n}$ is an integer

$$
\underline{\operatorname{Lim}}_{x \rightarrow 0}[f(x)]^{\prime \prime}=\left(\underline{\operatorname{Lim}}_{x \rightarrow 0} f(x)\right)^{\prime \prime}=\mathrm{L}
$$

For example: $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0}(2 x-3)^{2}=\left(\underline{\operatorname{Lim}}_{x \rightarrow 0}(2 x-3)\right)^{2}=(5)^{2}=125$
We conclude from the theorems on limits that limits are evaluated by merely substituting the number that $x$ approaches into the function.

Example: If $P(x)=\sigma_{n} x^{n}+\sigma_{n-1} x^{n-1}+\ldots .+\sigma_{1} x+\sigma_{0}$ is a polynomial function of degree $n$, then show that $\quad \underline{\operatorname{Lim}} P(x)=P(c)$

Solution: Using the theorems on limits, we have

$$
\begin{aligned}
= & \underline{\operatorname{Lim}} P(x) \quad \underline{\operatorname{Lim}}\left(a_{n} x^{n} \quad a_{n-1} x^{0,1}+\ldots . \quad a_{1} x+a_{0}\right. \\
& =a_{1} \underline{\operatorname{Lim}} x^{n}+a_{n-1} \underline{\operatorname{Lim}} x^{n-1}+\ldots .+a_{1} \underline{\operatorname{Lim}} x+\underline{\operatorname{Lim}} a_{0} \\
& =a_{n} \mathrm{e}^{n}+a_{n-1} \mathrm{e}^{n-1}+\ldots .+a_{1} c+a_{0} \\
\therefore & \underline{\operatorname{Lim}} P(x)=P(c)
\end{aligned}
$$