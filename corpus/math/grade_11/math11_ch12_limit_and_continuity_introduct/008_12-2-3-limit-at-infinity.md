### 12.2.3 Limit at Infinity

We have studied the limits of the functions $f(x), f(x) . g(x)$ and $\frac{f(x)}{g(x)}$, when $x \rightarrow c$ (a number)
Let us see what happens to the limit of the function $f(x)$ if $c$ is $+\infty$ or $-\infty$ (limits at infinity) i.e., when $x \rightarrow+\infty$ or $x \rightarrow-\infty$.
(a) Limit as $x \rightarrow+\infty$

Let $f(x)=\frac{1}{x}$, when $x \neq 0$
This function has the property that the value of $f(x)$ can be made as close as we please to zero when the number $x$ is sufficiently large.
We express this phenomenon by writing $\operatorname{Lim}_{x \rightarrow \infty} \frac{1}{x}=0$

(b) Limit as $x \rightarrow-\infty$

This type of limits are handled in the same way as limits as $x \rightarrow+\infty$.
i.e., $\operatorname{Lim}_{x \rightarrow-\infty} \frac{1}{x}=0$, where $x \neq 0$.

The following theorem is useful for evaluating limit at infinity.
Theorem: Let $p$ be a positive rational number. If $x^{p}$ is defined, then
$\operatorname{Lim}_{x \rightarrow+\infty} \frac{a}{x^{p}}=0$ and $\operatorname{Lim}_{x \rightarrow-\infty} \frac{a}{x^{p}}=0$, where $a$ is any real number.
For example, $\quad \operatorname{Lim}_{x \rightarrow+\infty} \frac{6}{x^{3}}=0$ and $\operatorname{Lim}_{x \rightarrow+\infty} \frac{-5}{\sqrt[3]{x}}=0$

# 12.2.4 Limit of a Sequence

Let $\left\{a_{n}\right\}$ be a sequence, the limit of a sequence $\left\{a_{n}\right\}$ is the value $L$ that the terms of the sequence approach as $n \rightarrow \infty$, that is,

$$
\operatorname{Lim}_{n \rightarrow \infty} a_{n}=L
$$

If such an $L$ exists, the sequence is said to converge to $L$ and $\left\{a_{n}\right\}$ is called convergent sequence. If no such $L$ exists, the sequence is said to diverge.
For example, consider the sequence $\left\{a_{n}=\frac{1}{n}\right\}$ : As $n \rightarrow \infty, \frac{1}{n} \rightarrow 0$
So, we write $\operatorname{Lim}_{n \rightarrow \infty} a_{n}=\operatorname{Lim}_{n \rightarrow \infty} \frac{1}{n}=0$.
Example 2 Find the limit of the sequence $a_{n}=\frac{2 n+3}{n+1}$.
Solution We can simplify the sequence:

$$
a_{n}=\frac{2 n+3}{n+1}=\frac{n\left(2+\frac{3}{n}\right)}{n\left(1+\frac{1}{n}\right)}=\frac{2+\frac{3}{n}}{1+\frac{1}{n}}
$$

As $n \rightarrow \infty, \frac{3}{n} \rightarrow 0$ and $\frac{1}{n} \rightarrow 0$, so we are left with: $\operatorname{Lim}_{n \rightarrow \infty} a_{n}=\frac{2+0}{1+0}=2$

$$
\text { Thus, } \operatorname{Lim}_{n \rightarrow \infty} \frac{2 n+3}{n+1}=2
$$

Divergent Sequences: A sequence is divergent if it is not convergent. Divergence can occur in the following ways:

- The sequence may increase or decrease without bound (e.g., $a_{n}=n^{2}$ diverges to infinity).
- The sequence may oscillate between different values and not settle near any one value (e.g., $a_{n}=(-1)^{n}$ oscillates between -1 and 1 , so it does not converge).

# 12.2.5 Methods for Evaluating the Limits at Infinity

In this case we first divide each term of both the numerator and the denominator by the highest power of $x$ that appears in the denominator and then use the theorems on limit.

Example 3 Evaluate $\operatorname{Lim}_{x \rightarrow+\infty} \frac{5 x^{4}-10 x^{2}+1}{-3 x^{3}+10 x^{2}+50}$
Solution Dividing numerator and denominator by $x^{3}$, we get
$\operatorname{Lim}_{x \rightarrow+\infty} \frac{5 x^{4}-10 x^{2}+1}{-3 x^{3}+10 x^{2}+50}=\operatorname{Lim}_{x \rightarrow+\infty} \frac{5 x-\frac{10}{x}+\frac{1}{x^{3}}}{-3+\frac{10}{x}+\frac{50}{x^{3}}}=\frac{\infty-0+0}{-3+0+0}=-\infty: \lim _{x \rightarrow \infty} \frac{a}{x^{a}}=0$
Example 4 Evaluate $\operatorname{Lim}_{x \rightarrow-\infty} \frac{4 x^{4}-5 x^{3}}{-3 x^{3}+2 x^{2}+1}$
Solution Dividing numerator and denominator by $x^{2}$, we get

$$
\operatorname{Lim}_{x \rightarrow-\infty} \frac{4 x^{4}-5 x^{3}}{-3 x^{3}+2 x^{2}+1}=\operatorname{Lim}_{x \rightarrow-\infty} \frac{\frac{4}{x}-\frac{5}{x^{2}}}{-3+\frac{2}{x^{3}}+\frac{1}{x^{3}}}=\frac{0-0}{-3+0+0}=0
$$

Example 5 Evaluate:
(i) $\quad \operatorname{Lim}_{x \rightarrow-\infty} \frac{2-3 x}{\sqrt{3}+4 x^{3}}$
(ii) $\quad \operatorname{Lim}_{x \rightarrow+\infty} \frac{2-3 x}{\sqrt{3}+4 x^{2}}$

Solution
(i) Here $\sqrt{x^{2}}=|x|=-x$ as $x<0$
$\therefore \quad$ Dividing numerator and denominator by $-x$, we get

$$
\operatorname{Lim}_{x \rightarrow-\infty} \frac{2-3 x}{\sqrt{3}+4 x^{2}}=\operatorname{Lim}_{x \rightarrow-\infty} \frac{-\frac{2}{x}+3}{\sqrt{\frac{3}{x^{2}}+4}}=\frac{0+3}{\sqrt{0+4}}=\frac{3}{2}
$$

(ii) Here $\sqrt{x^{2}}=|x|=x$ as $x>0$
$\therefore \quad$ Dividing numerator and denominator by $x$, we get

$$
\lim _{x \rightarrow+\infty} \frac{2-3 x}{\sqrt{3+4 x^{2}}}=\operatorname{Lim}_{x \rightarrow+\infty} \frac{\frac{2}{x}-3}{\sqrt{\frac{3}{x^{2}}+4}}=\frac{0-3}{\sqrt{0+4}}=\frac{-3}{2}
$$

12.2.6 $\quad \operatorname{Lim}_{n \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{n}=e$

By the binomial theorem, we have

$$
\begin{aligned}
\left(1+\frac{1}{n}\right)^{n} & =1+n\left(\frac{1}{n}\right)+\frac{n(n-1)}{2!}\left(\frac{1}{n}\right)^{2}+\frac{n(n-1)(n-2)}{3!}\left(\frac{1}{n}\right)^{3}+\ldots \\
& =1+1+\frac{1}{2!}\left(1-\frac{1}{n}\right)+\frac{1}{3!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right)+\ldots
\end{aligned}
$$

When $n \rightarrow+\infty, \frac{1}{n}, \frac{2}{n}, \frac{3}{n}, \ldots$ all tends to zero, therefore

$$
\begin{aligned}
\therefore \quad \operatorname{Lim}_{x \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{n} & =1+1+\frac{1}{2!}+\frac{1}{3!}+\frac{1}{4!}+\ldots \\
& =1+1+0.5+0.166667+0.0416667+\ldots=2.718281 \ldots
\end{aligned}
$$

As approximate value of $e$ is 2.718281 .

$$
\therefore \quad \operatorname{Lim}_{n \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{n}=e
$$

Deduction: $\quad \operatorname{Lim}_{x \rightarrow 0}(1+x)^{x}=e$

We know that $\operatorname{Lim}_{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=e$
(i)

Put $n=\frac{1}{x}$ in (i) then $x=\frac{1}{n}$
When $n \rightarrow \infty, x \rightarrow 0 \quad$ so, $\quad \operatorname{Lim}_{n \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{n}=\operatorname{Lim}_{x \rightarrow 0}(1+x)^{\frac{1}{x}}$

$$
e=\operatorname{Lim}_{x \rightarrow 0}(1+x)^{\frac{1}{x}} \quad \because \quad \operatorname{Lim}_{x \rightarrow 1}\left(1+\frac{1}{n}\right)^{n}=e
$$

Hence $\operatorname{Lim}_{x \rightarrow 0}(1+x)^{\frac{1}{x}}=e$

# 12.2.7 $\lim _{x \rightarrow 0} \frac{a^{x}-1}{x}=\log _{a} a$

Put $a^{x}-1=y$
then $\quad a^{x}=1+y$
So, $\quad x=\log _{a}(1+y)$
From (i) when $x \rightarrow 0, y \rightarrow 0$

$$
\begin{aligned}
\therefore \quad \lim _{x \rightarrow 0} \frac{a^{x}-1}{x} & =\lim _{y \rightarrow 0} \frac{y}{\log _{a}(1+y)}=\underline{\lim _{y \rightarrow 0}} \frac{1}{\frac{1}{y} \log _{a}(1+y)} \\
& =\underline{\lim _{y \rightarrow 0}} \frac{1}{\log _{a}(1+y)^{y}}=\frac{1}{\log _{a} e}=\log _{a} a \quad\left(\underline{\lim _{y \rightarrow 0}(1+y)^{y}}=e\right)
\end{aligned}
$$

Deduction: $\quad \underline{\lim _{x \rightarrow 0}}\left(\frac{e^{x}-1}{x}\right)=\log _{e} e=1$
We know that $\underline{\lim _{x \rightarrow 0}}\left(\frac{a^{x}-1}{x}\right)=\log _{a} a$
Put $a=e$ in (i) we know $\operatorname{Lim}_{x \rightarrow 0}\left(\frac{e^{x}-1}{x}\right)=\log _{e} e=1$
Important Results to Remember
(i) $\quad \operatorname{Lim}_{x \rightarrow \infty} e^{x}=\infty$
(ii) $\quad \operatorname{Lim}_{x \rightarrow-\infty} e^{x}=\operatorname{Lim}_{x \rightarrow \infty}\left(\frac{1}{e^{x}}\right)=0$

## Example 6 Express each limit in terms of $e$.

(i) $\quad \lim _{n \rightarrow \infty}\left(1+\frac{3}{n}\right)^{3 n}$
(ii) $\quad \operatorname{Lim}_{n \rightarrow 0}(1+2 n)^{\frac{1}{n}}$

Solution (i) Observe the resemblance of the limit with $\operatorname{Lim}_{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=e$

$$
\begin{aligned}
& \left(1+\frac{3}{n}\right)^{2 n}=\left[\left(1+\frac{3}{n}\right)^{\frac{n}{3}}\right]^{6}=\left[\left(1+\frac{1}{\frac{n}{3}}\right)^{\frac{n}{3}}\right]^{6} \\
& \because \quad \operatorname{Lim}_{n \rightarrow+\infty}\left(1+\frac{3}{n}\right)^{3 n}=\operatorname{Lim}_{m \rightarrow+\infty}\left[\left(1+\frac{1}{m}\right)^{m}\right]^{6}=e^{6} \text { where, } m=\frac{n}{3}
\end{aligned}
$$

(ii) Observe the resemblance of the limit with $\operatorname{Lim}_{x \rightarrow 0}(1+x)^{\frac{1}{x}}=e$

$$
\begin{aligned}
& \operatorname{Lim}_{n \rightarrow 0}(1+2 n)^{\frac{1}{n}}=\operatorname{Lim}_{n \rightarrow 0}\left[(1+2 n)^{\frac{1}{2 n}}\right]^{2} \\
& \text { put } m=2 n \text {, when } n \rightarrow 0, m \rightarrow 0 \\
& \operatorname{Lim}_{n \rightarrow 0}(1+2 n)^{\frac{1}{n}}=\lim _{m \rightarrow 0}\left[(1+m)^{\frac{1}{m}}\right]^{2}=e^{2}
\end{aligned}
$$

# 12.2.8 The Sandwich Theorem

Let $f, g$ and $h$ be functions such that $f(x) \leq g(x) \leq h(x)$ for all numbers $x$ in some open interval containing " $c$ ", except possibly at $c$ itself.
If $\operatorname{Lim}_{x \rightarrow c} f(x)=L$ and $\operatorname{Lim}_{x \rightarrow c} h(x)=L$, then $\operatorname{Lim}_{x \rightarrow c} g(x)=L$
Many limit problems arise that cannot be directly evaluated by algebraic techniques. They require geometric arguments, so we evaluate an important theorem.