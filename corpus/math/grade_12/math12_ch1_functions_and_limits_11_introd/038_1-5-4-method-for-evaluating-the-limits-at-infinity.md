### 1.5.4 Method for Evaluating the Limits at Infinity

In this case we first divide each term of both the numerator and the denominator by the highest power of $x$ that appears in the denominator and then use the above theorem.

Example 2: Evaluate $\underline{L i m}_{\varepsilon \rightarrow+\infty} \frac{5 x^{4}-10 x^{2}+1}{-3 x^{3}+10 x^{2}+50}$
Solution: $\quad$ Dividing up and down by $x^{3}$, we get

$$
\underline{L i m}_{\varepsilon \rightarrow+\infty} \frac{5 x^{4}-10 x^{2}+1}{-3^{3}+10 x^{2}+50}=\underline{L i}_{\varepsilon \rightarrow+\infty} \frac{5 x-10 / x+1 / x^{2}}{-3+10 / x+50 / 2}=\frac{\infty-0+0}{-3+0+0}=\infty
$$

Example 3: Evaluate $\underline{L i m}_{\varepsilon \rightarrow-\infty} \frac{4 x^{4}-5 x^{3}}{3 x^{2}+2 x^{2}+1}$
Solution: Since $x<0$, so dividing up and down by $(-x)^{3}=-x^{3}$, we get

$$
\underline{L i m}_{\varepsilon \rightarrow-\infty} \frac{4 x^{4}-5 x^{3}}{3 x^{2}+2 x^{2}+1}=\underline{L i m}_{\varepsilon \rightarrow-\infty} \frac{-4 / x+5 / x^{2}}{-3-2 / x^{2}-1 / x^{2}}=\frac{0+0}{-3-0-0}=0
$$

Example 4: Evaluate
(i) $\lim _{x \rightarrow \infty} \frac{2-3 x}{\sqrt{3+4 x^{2}}}$
(ii) $\quad \lim _{x \rightarrow \infty} \frac{2-3 x}{\sqrt{3+4 x^{2}}}$

Solution: (i) Here $\sqrt{x^{2}}=|x|=\infty$ as $x<0$
$\therefore \quad$ Dividing up and down by $-x$, we get
$\lim _{x \rightarrow \infty} \frac{2-3 x}{\sqrt{3+4 x^{2}}}=\lim _{x \rightarrow \infty} \frac{-2 / x+3}{\sqrt{3 / x^{2}+4}}=\frac{0+3}{\sqrt{0+4}}=\frac{3}{2}$
(ii) Here $\sqrt{x}=| |=x$ as $x>0$
$\therefore \quad$ Dividing up and down by $x$, we get
$\lim _{x \rightarrow \infty} \frac{2-3 x}{\sqrt{3+4 x^{2}}}=\lim _{x \rightarrow \infty} \frac{2 / x+3}{\sqrt{3 / x^{2}+4}}=\frac{0-3}{\sqrt{0+4}}=\frac{-3}{2}$
$1.5 .5 \quad \lim _{n \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{n}=\mathrm{e}$.

By the Binomial theorem, we have

$$
\begin{aligned}
& \left(1+\frac{1}{n}\right)^{n}=1+n\left(\frac{1}{n}\right)+\frac{n(n-1)}{2!}\left(\frac{1}{n}\right)^{2}+\frac{n(n-1)(n-2)}{3!}\left(\frac{1}{n}\right)^{3}+\ldots \\
& =1+1+\frac{1}{2!}\left(1-\frac{1}{n}\right)+\frac{1}{3!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right)+\ldots \\
& \text { when } \mathrm{n} \longrightarrow \infty, \frac{1}{n} \cdot \frac{2}{n} \cdot \frac{3}{n} \cdot \ldots \text { all tend to zero. } \\
& \therefore \lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=1+1+\frac{1}{2!}+\frac{1}{3!}+\frac{1}{4!}+\frac{1}{5!}+\ldots \\
& =1+1+0.5+0.166667+0.0416667+\ldots=2.718281 \ldots
\end{aligned}
$$

As approximate value of $e$ is $=2.718281$.
$\therefore \lim _{x \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{n}=\mathrm{e}$.
version: 1.1

Deduction $\lim _{x \rightarrow 0}(1+x)^{1 / x}=e$
We know that $\lim _{x \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=\mathrm{e}$
put $\mathrm{n}=\frac{1}{x}$, then $\frac{1}{\mathrm{n}}=x \quad$ in (i)

When $x \rightarrow 0, \mathrm{n} \rightarrow \infty$
$A x \quad \lim _{x \rightarrow \infty}\left(1+\frac{1}{n}\right)^{x}=\mathrm{e}$
$\therefore \quad \lim _{x \rightarrow 0}(1+x)^{1 / x}=\mathrm{e}$
1.5.6 $\quad \lim _{x \rightarrow 0} \frac{a^{x}-1}{x}=\log _{e} a$

$$
\begin{aligned}
& \text { Put } a^{x}-1=y \\
& \text { then } a^{x}=1+y \\
& \text { So } \quad x=\log _{a}(1+y) \\
& \text { From (i) when } x \rightarrow 0, y \rightarrow 0
\end{aligned}
$$

$$
\begin{aligned}
\therefore \lim _{x \rightarrow 0} \frac{a^{x}-1}{x} & =\lim _{y \rightarrow 0} \frac{y}{\log _{a}(1+y)}=\lim _{y \rightarrow 0} \frac{1}{\frac{1}{\log _{a}(1+y)}} \\
& =\lim _{y \rightarrow 0} \frac{1}{\log _{a}(1+y)^{1 / y}}=\frac{1}{\log _{a} e}=\log _{e} a \quad\left(\sqrt{\frac{\lim }{y \rightarrow 0}}(1+y)^{1 / y}=\mathrm{e}\right)
\end{aligned}
$$

Deduction $\lim _{x \rightarrow 0}\left(\frac{e^{x}-1}{x}\right)=\log _{e} e=1$.
We know that $\lim _{x \rightarrow 0} \frac{a^{x}-1}{x}=\log _{e} a$

Put $a \equiv e$ in (1), we have
$\underline{\operatorname{Lim}} \frac{e^{x}-1}{x}=\log _{e} e=1$.

## Important Results to Remember

(i) $\operatorname{Lim}_{x \rightarrow \infty}\left(e^{x}\right)=\infty$
(ii) $\operatorname{Lim}_{x \rightarrow-\infty}\left(e^{x}\right)=\operatorname{Lim}_{x \rightarrow-\infty}\left(\frac{1}{e^{-x}}\right)=0$,
(iii) $\operatorname{Lim}_{x \rightarrow \infty}\left(\frac{a}{x}\right)=0$, where $a$ is any real number.

Example 5: Express each limit in terms of the number ' $e$ '
(a) $\operatorname{Lim}_{x \rightarrow \infty}\left(1+\frac{3}{n}\right)^{2 n}$
(b) $\operatorname{Lim}_{x \rightarrow \infty}(1+2 h)^{\frac{3}{n}}$

Solution: (a) Observe the resemblance of the limit with

$$
\begin{aligned}
& \operatorname{Lim}_{x \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=\mathrm{e} \\
& \left(1+\frac{3}{n}\right)^{2 n}=\left[\left(1+\frac{3}{n}\right)^{\frac{n}{2}}\right]^{n}=\left[\left(1+\frac{1}{n / 3}\right)^{\frac{n}{2}}\right]^{n} \\
& \therefore \quad \operatorname{Lim}_{n \rightarrow \infty}\left(1+\frac{3}{n}\right)^{2 n}=\operatorname{Lim}_{n \rightarrow \infty}\left[\left(1+\frac{1}{m}\right)^{m}\right]^{n}=e^{n} \quad\left(\begin{array}{c}
\text { put } m=n / 3 \\
\text { when } n \rightarrow \infty, \\
m \rightarrow \infty
\end{array}\right)
\end{aligned}
$$

(b) Observe the resemblance of the limit with $\operatorname{Lim}_{x \rightarrow 0}(1+x)^{\frac{1}{n}}=\mathrm{e}$,

$$
\begin{aligned}
\therefore \operatorname{Lim}_{n \rightarrow 0}(1+2 h)^{\frac{3}{n}} & =\operatorname{Lim}_{x \rightarrow 0}\left[(1+2 h)^{\frac{3}{2 n}}\right]^{\frac{n}{2}} \quad(\text { put } m=2 h, \text { when } h \rightarrow 0, m \rightarrow 0 \\
& =\operatorname{Lim}_{m \rightarrow 0}\left[(1+m)^{\frac{1}{m}}\right]^{\frac{1}{n}}=e^{2}
\end{aligned}
$$

version: 1.1