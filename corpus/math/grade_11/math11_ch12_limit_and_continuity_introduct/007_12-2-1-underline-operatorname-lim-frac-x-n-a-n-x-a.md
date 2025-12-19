### 12.2.1 $\underline{\operatorname{Lim}} \frac{x^{n}-a^{n}}{x-a}=n a^{n-1}$ where $n$ is a non-zero integer and $a>0$

Case I: Suppose $n$ is a positive integer.
By substituting $x=a$, we get $\binom{0}{0}$ form, so we make factors as follows:

$$
\begin{aligned}
x^{n}-a^{n} & =(x-a)\left(x^{n-1}+a x^{n-2}+a^{2} x^{n-3}+\ldots+a^{n-1}\right) \\
\lim _{x \rightarrow a} \frac{x^{n}-a^{n}}{x-a} & =\lim _{x \rightarrow a} \frac{(x-a)\left(x^{n-1}+a x^{n-2}+a^{2} x^{n-3}+\ldots+a^{n-1}\right)}{x-a} \\
& =\operatorname{Lim}_{x \rightarrow a}\left(x^{n-1}+a x^{n-2}+a^{2} x^{n-3}+\ldots+a^{n-1}\right) \\
& =a^{n-1}+a \quad a^{n-2}+a^{2} a^{n-3}+a^{3} a^{n-4}+\ldots+a^{n-1} \\
& =a^{n-1}+a^{n-1}+a^{n-1}+a^{n-1} \ldots+a^{n-1}=n a^{n-1}
\end{aligned}
$$

Case II: Suppose $n$ is a negative integer (Say $n=-m$ ) where $m$ is a positive integer.

$$
\begin{aligned}
& \text { Now, } \quad \frac{x^{n}-a^{n}}{x-a}=\frac{x^{-n}-a^{-n}}{x-a}=\frac{\frac{1}{x^{m}}-\frac{1}{a^{m}}}{x-a}=\frac{\frac{a^{m}-x^{m}}{x^{n} a^{m}}}{x-a} \\
& \therefore \quad \operatorname{Lim}_{x \rightarrow a} \frac{x^{n}-a^{n}}{x-a}=\operatorname{Lim}_{x \rightarrow a}\left(\frac{-1}{x^{m} a^{m}}\right)\left(\frac{x^{n}-a^{m}}{x-a}\right) \\
& =\frac{-1}{a^{m} a^{m}}\left(m a^{m-1}\right) \quad \text { (by Case }-1 \text { ) } \\
& =-m a^{-m-1} \\
& \therefore \quad \operatorname{Lim}_{x \rightarrow a}\left(\frac{x^{n}-a^{n}}{x-a}\right)=n a^{n-1} \quad \because n=-m
\end{aligned}
$$

# 12.2.2 $\underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{\sqrt{x+a}-\sqrt{a}}{x}=\frac{1}{2 \sqrt{a}}$, where $n$ is an integer and $a>0$.

By substituting $x=0$, we have $\left(\frac{0}{0}\right)$ form, so rationalizing the numerator.

$$
\begin{aligned}
\lim _{x \rightarrow 0} \frac{\sqrt{x+a}-\sqrt{a}}{x} & =\lim _{x \rightarrow 0}\left(\frac{\sqrt{x+a}-\sqrt{a}}{x}\right)\left(\frac{\sqrt{x+a}+\sqrt{a}}{\sqrt{x+a}+\sqrt{a}}\right)=\lim _{x \rightarrow 0} \frac{x+a-a}{x(\sqrt{x+a}+\sqrt{a})} \\
& =\lim _{x \rightarrow 0}\left(\frac{1}{\sqrt{x+a}+\sqrt{a}}\right) \\
& =\lim _{x \rightarrow 0} \frac{1}{\sqrt{x+a}+\sqrt{a}}=\frac{1}{\sqrt{a}+\sqrt{a}}=\frac{1}{2 \sqrt{a}}
\end{aligned}
$$

Example 1 Evaluate: (i) $\quad \lim _{x \rightarrow 1} \frac{x^{2}-1}{x^{2}-x}$
(ii) $\quad \lim _{x \rightarrow 3} \frac{x-3}{\sqrt{x}-\sqrt{3}}$

Solution (i) $\quad \lim _{x \rightarrow 1} \frac{x^{2}-1}{x^{2}-x} \quad\left(\frac{0}{0}\right)$ form.

$$
\begin{aligned}
\lim _{x \rightarrow 1} \frac{x^{2}-1}{x^{2}-x} & =\lim _{x \rightarrow 1} \frac{(x-1)(x+1)}{x(x-1)}=\lim _{x \rightarrow 1} \frac{x+1}{x} \\
& =\frac{1+1}{1}=\frac{2}{1}=2
\end{aligned}
$$

(ii) $\quad \lim _{x \rightarrow 3} \frac{x-3}{\sqrt{x}-\sqrt{3}}=\underline{\operatorname{Lim}}_{x \rightarrow 3} \frac{(\sqrt{x}+\sqrt{3})(\sqrt{x}=\sqrt{3})}{(\sqrt{x}=\sqrt{3})}=\operatorname{Lim}_{x \rightarrow 3}(\sqrt{x}+\sqrt{3})=\sqrt{3}+\sqrt{3}=2 \sqrt{3}$