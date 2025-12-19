### 2.10 DERIVATIVE OF EXPONENTIAL FUNCTIONS:

A function $f$ defined by
$f(x)=a^{x}$
$a>0, a \neq 1$ and $x$ is any real number.
is called an exponential function
If $a=e$, then $y=a^{x}$ becomes $y=e^{x} \cdot e^{x}$ is called the natural exponential function.
Now we find derivatives of $e^{x}$ and $a^{x}$ from the first principle:

1. Let $y=e^{x}$ then
$y+\delta y=e^{x+\delta x}$ and $\delta y=y+\delta y-y=e^{x+\delta x}-e^{x}=e^{x} \cdot e^{\delta x}-e^{x}$
That is, $\delta y=e^{x}\left(e^{\delta x}-1\right)$ and $\frac{\delta y}{\delta x} \quad e^{x} \cdot\left(\frac{e^{\delta x}-1}{\delta x}\right)$
Thus $\lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0} e^{x}\left(\frac{e^{\delta x}-1}{\delta x}\right) e^{x} \cdot \lim _{\delta x \rightarrow 0}\left(\frac{e^{\delta x}-1}{\delta x}\right)$
$\left(\because \lim _{\delta x \rightarrow 0} e^{x}=e^{x} \cdot\right)$

$$
\frac{d y}{d x}=e^{x} \cdot 1\left(\text { Using } \lim _{h \rightarrow 0} \frac{e^{h}-1}{h} 1\right)
$$

or $\frac{d}{d x}\left(e^{x}\right)=e^{x}$
2. Let $\quad y=a^{x}$, then

$$
y+\delta y=a^{x+\delta x} \text { and } \delta y=a^{x+\delta x}-a^{x}=a^{x} \cdot a^{\delta x}-a^{x}=a^{x}\left(a^{\delta x}-1\right)
$$

Dividing both sides by $\delta x$, we have

$$
\frac{\delta y}{\delta x}=a^{x}\left(\frac{a^{\delta x}-1}{\delta x}\right)
$$

Thus $\frac{d y}{d x}=\lim _{\delta x \rightarrow 0} a^{x}\left(\frac{a^{\delta x}-1}{\delta x}\right) a^{x} \cdot \lim _{\delta x \rightarrow 0}\left(\frac{a^{\delta x}-1}{\delta x}\right)\left(\because \lim _{\delta x \rightarrow 0} a^{x} a^{x}\right)$

$$
=a^{x} \cdot(\ln a)\left(\text { Using } \lim _{h \rightarrow 0} \frac{a^{h}-1}{h} \quad \log ^{a}{ }_{h} \ln a\right)
$$

or $\frac{d}{d x}\left(a^{x}\right)=a^{x} \cdot(\ln a)$

Example 1: $\quad$ Find $\frac{d y}{d x}$ if : (i) $y=e^{x^{2}+1}$
(ii) $y=a^{x / 2}$

Solution: (i) Let $\quad u=x^{2}+1$, then

$$
y=\mathrm{e}^{u} \quad \ldots .(\mathrm{A}) \text { and } \frac{d u}{d x}=\frac{d}{d x}\left(x^{2}+1\right)=2 x
$$

Differentiating both sides of (A) w.r.t. ' $x$ ', we have

$$
\begin{aligned}
& \frac{d}{d x}(y)=\frac{d}{d x}\left(e^{u}\right)=\frac{d}{d u}\left(e^{u}\right) \cdot \frac{d u}{d x} \quad \text { (Using the chain rule) } \\
& =e^{u} \frac{d u}{d x} \quad\left(\text { Using } \frac{d}{d x}\left(e^{u}\right) \quad e^{x}\right) \\
& \text { Thus } \frac{d y}{d x}=e^{x^{2}+1} \cdot(2 x) \quad\left(\forall u \quad x^{2} \quad 1 \Rightarrow \text { and } \frac{d u}{d x} \quad 2 x\right)
\end{aligned}
$$

(ii) Let $u=\sqrt{x} \quad$ Then $\quad y \quad a^{u}$
and $\frac{d u}{d x}=\frac{d}{d x}\left(x^{1 / 2}\right)=\frac{1}{2} x^{-1 / 2}=\frac{1}{2 \sqrt{x}}$
Differentiating both sides of (A) w.r.t. ' $x$ ', gives

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left(a^{u}\right)=\frac{d}{d u}\left(a^{u}\right) \cdot \frac{d u}{d x} \quad\left(\because \frac{d y}{d x} \quad \frac{d y}{d u} \frac{d u}{d x}\right) \\
& =\left(a^{u} \ln a\right) \cdot \frac{d u}{d x} \quad\left(\text { Using } \frac{d}{d x}\left(a^{x}\right) \quad a^{x} \ln a\right) \\
& \text { Thus } \frac{d}{d x}\left(a^{x / 2}\right)=\left(a^{x / 2} \ln a\right) \cdot \frac{1}{2 \sqrt{x}}=\left(\because u \quad \sqrt{x} \text { and } \frac{d u}{d x} \quad \frac{1}{2 \sqrt{x}}\right)
\end{aligned}
$$

$$
=\frac{\ln a}{2} \cdot a^{\sqrt{x}} \frac{1}{\sqrt{x}}
$$

Example 2: Differentiate $y=a^{x}$ w.r.t. $x$.
Solution: Here $y=a^{x}$

$$
=e^{x \ln a}
$$

Differentiating w.r.t. ' $x$ ', we have

$$
\begin{aligned}
\frac{d y}{d x} & =e^{x \ln a} \cdot \frac{d}{d x}(x \ln a) \\
& =w^{\prime} \cdot(\ln a) \quad\left(\because e^{x \ln a} \quad a^{x}\right) \\
& =w^{\prime} \cdot(\ln a) \quad\left(\because e^{x \ln a} \quad a^{x}\right)
\end{aligned}
$$