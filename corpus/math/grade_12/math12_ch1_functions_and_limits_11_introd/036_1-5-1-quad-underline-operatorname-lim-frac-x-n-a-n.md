### 1.5.1 $\quad \underline{\operatorname{Lim}} \frac{x^{n}-a^{n}}{x-a}=n a^{n-1}$ where $n$ is an integer and $a>0$

Case 1: Suppose $n$ is a positive integer.
By substituting $x=a$, we get $\binom{0}{0}$ form. So we make factors as follows:

$$
x^{n}-a^{n}=(x-a)\left(x^{n-1}+a x^{n-2}+a^{2} x^{n-2}+\ldots .+a^{n-1}\right)
$$

$\therefore \quad \underline{\operatorname{Lim}} \frac{x^{n}-a^{n}}{x-a}=\underline{\operatorname{Lim}} \frac{(x-a)\left(a x^{n-1}+a x^{n-2} a^{2} x^{n-2}+\ldots .+a^{n-1}\right)}{x-a}$
$=\underline{\operatorname{Lim}}\left(x^{n-1}+a x^{n-2}+a^{2} x^{n-2}+\ldots .+a^{n-1}\right)$ (polynomial function)
$=a^{n-1}+a \cdot a^{n-2}+a^{2} \cdot a^{n-2}+\ldots .+a^{n-1}$
$=a^{n-1}+a^{n-1}+a^{n-1}+\ldots .+a^{n-1} \quad(n$ terms)
$=n a^{n-1}$

Case II: Suppose $n$ is a negative integer (say $n=-m$ ), where $m$ is a positive integer.

$$
\begin{aligned}
& \text { Now } \frac{x^{n}-\mathrm{a}^{n}}{x-\mathrm{a}}=\frac{x^{-n}-\mathrm{a}^{-n}}{x-\mathrm{a}} \\
& =\frac{-1}{x^{m} \mathrm{a}^{m}}\left(\frac{x^{m}-\mathrm{a}^{m}}{x-\mathrm{a}}\right) \quad(\mathrm{a} \neq 0) \\
& \therefore \quad \underline{\operatorname{Lim}} \frac{x^{n}-\mathrm{a}^{n}}{x-\mathrm{a}}=\underline{\operatorname{Lim}}\left(\frac{-1}{x^{m} \mathrm{a}^{m}}\right)\left(\frac{x^{m}-\mathrm{a}^{m}}{x-\mathrm{a}}\right) \\
& =\frac{-1}{a^{m} \mathrm{a}^{m}} \cdot\left(m a^{m-1}\right), \quad \quad \text { (By case 1) } \\
& =-m a^{-m-1} \\
& \therefore \quad \underline{\operatorname{Lim}} \frac{x^{n}-\mathrm{a}^{n}}{x-\mathrm{a}}=\mathrm{na}^{n-1} \quad(\mathrm{n}=-\mathrm{m})
\end{aligned}
$$

1.5.2 $\quad \underline{\operatorname{Lim}} \sqrt{\overline{+a}} \sqrt{a}=\frac{\sqrt{a}}{}$

By substituting $x=0$, we have $\binom{0}{0}$ form, so rationalizing the numerator.

$$
\begin{aligned}
\therefore \quad \underline{\operatorname{Lim}} \frac{\sqrt{x+a} \cdot \sqrt{a}}{x} & =\underline{\operatorname{Lim}} \cdot\left(\frac{\sqrt{x+a} \cdot \sqrt{a}}{x}\right)\left(\frac{\sqrt{x+a}+\sqrt{a}}{\sqrt{x+a}+\sqrt{a}}\right) \\
& =\underline{\operatorname{Lim}} \frac{x+a-a}{x(\sqrt{x+a}+\sqrt{a})} \\
& =\underline{\operatorname{Lim}} \frac{x}{x(\sqrt{x+a}+\sqrt{a})} \\
& =\underline{\operatorname{Lim}} \frac{1}{\sqrt{x+a}+\sqrt{a}} \\
& =\frac{1}{\sqrt{a}+\sqrt{a}}=\frac{1}{2 \sqrt{a}}
\end{aligned}
$$

Example 1: Evaluate
(i) $\quad \underline{L i m}_{\varepsilon \rightarrow 0} \frac{x^{2}-1}{x^{2}-x}$
(ii) $\quad \underline{L i m}_{\varepsilon \rightarrow 0} \frac{x-3}{\sqrt{x}-\sqrt{3}}$

Solution: (i) $\quad \underline{L i m}_{\varepsilon \rightarrow 0} \frac{x^{2}-1}{x^{2}-x} \quad\left(\frac{0}{0}\right)$ form (By making factors)
$\therefore \quad \underline{L i m}_{\varepsilon \rightarrow 0} \frac{x^{2}-1}{x^{2}-x}=\underline{L i m}_{\varepsilon \rightarrow 0} \frac{(x-1)(x+1)}{x(x-1)}=\underline{L i m}_{\varepsilon \rightarrow 0} \frac{x+1}{x}=\frac{1+1}{1}=2$
(ii) $\quad \underline{L i m}_{\varepsilon \rightarrow 0} \frac{x-3}{\sqrt{x}-\sqrt{3}}\left(\frac{0}{0}\right)$ form (By making factors of $x-3$ )
$\therefore \quad \underline{L i m}_{\varepsilon \rightarrow 0} \frac{x-3}{\sqrt{x}-\sqrt{3}}=\underline{L i m}_{\varepsilon \rightarrow 0} \frac{(\sqrt{x}+\sqrt{3}) /(\sqrt{x}-\sqrt{3})}{\sqrt{x}-\sqrt{3}}$

$$
\begin{aligned}
& =\underline{L i m}_{\varepsilon \rightarrow 0}(\sqrt{x}+\sqrt{3}) \\
& =(\sqrt{3}+\sqrt{3}) \\
& =2 \sqrt{3}
\end{aligned}
$$