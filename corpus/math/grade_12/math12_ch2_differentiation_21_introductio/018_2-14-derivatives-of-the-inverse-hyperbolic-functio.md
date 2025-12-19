### 2.14 DERIVATIVES OF THE INVERSE HYPERBOLIC FUNCTIONS:

The inverse hyperbolic functions are defined by:

1. $y=\sinh ^{-1} \infty$ if and if $x \quad \sinh y ; x, y \quad R$
2. $y=\cosh ^{-1} x$ if and only if $x \cosh y \infty ; x[\mathrm{~V}), y[0,]]$
3. $y=\tanh ^{-1} x$ if andonly if $x \in \tanh y ; x(1,1), y \quad R$
4. $y=\operatorname{coth}^{-1} x$ if andonly if $x \in \operatorname{coth} y ; x[1,1], y \quad R\{0\}$
5. $y=\operatorname{sech}^{-1} x$ if and only if $x=\operatorname{sech} y ; x(0,1], y[0$, )
6. $y=\cos e c h^{-1} x$ if andonly if $x \operatorname{osec} h y ; x \not R \quad\{0\}, y \quad R\{0\}$

The following two equations can easily be derived:
(i) $\sinh ^{-1} x=\ln \left(x+\sqrt{x^{2}+1}\right)$
(ii) $\cosh ^{-1} x=\ln \left(x \cdot \sqrt{x^{2}-1}\right)$

## Proof of (i).

Let $y=\min ^{-1} x$ for $x, y \quad R$, then

$$
\begin{aligned}
& x=\sinh y \Rightarrow x=\frac{e^{y}-e^{-y}}{2} \\
& \Rightarrow 2 x e^{y}=e^{2 y}-1
\end{aligned}
$$

or $e^{2 y}-2 x e^{y}-1=0$
Solving the above equation for $e^{y}$, we have

$$
\begin{aligned}
e^{y} & =\frac{2 x \pm \sqrt{4 x^{2}+4}}{2} \\
& =\frac{2 x \pm 2 \sqrt{x^{2}+1}}{2}=x \pm \sqrt{x^{2}+1}
\end{aligned}
$$

As $e^{y}$ is positive for $y \in R$, so we discard

$$
x-\sqrt{x^{2}+1}
$$

Thus $e^{y}=x+\sqrt{x^{2}+1} \Rightarrow y=\ln \left(x+\sqrt{x^{2}+1}\right)$

$$
\Rightarrow \sinh ^{-1} x=\operatorname{In}\left(x+\sqrt{x^{2}+1}\right)
$$

Proof of (ii)
Let $y=\cosh ^{-1} x$ for $x \in[1, \infty), y \in[0, \in)$, then

$$
x=\cosh y \Rightarrow x=\frac{e^{y}+e^{-y}}{2} \Rightarrow e^{2 y}-2 e^{y}+1=0
$$

Solivng (1) gives, $e^{y}=\frac{2 x \pm \sqrt{4 x^{2}-4}}{2}=\frac{2 x \pm 2 \sqrt{x^{2}-1}}{2}=x \pm \sqrt{x^{2}-1}$.
$e^{y}=x-\sqrt{x^{2}-1}$ can be written as $y=\ln \left(x \quad \sqrt{x^{2}-1}\right)$
If $x=1$, then $y=\ln (1-\sqrt{1-1})=\ln (1)=0$ but
$\ln \left(x-\sqrt{x^{2}-1}\right)$ is negative for all $x>1$, that is
for each $x \in(1, \infty), y \notin(0, \infty)$, so we discard this value of $e^{y}$
Thus $e^{y}=x+\sqrt{x^{2}+1}$ which give $y=\ln \left(x+\sqrt{x^{2}-1}\right)$, that is

$$
\cosh ^{-1} x=\operatorname{In}\left(x+\sqrt{x^{2}-1}\right)
$$

Derivative of $\sinh ^{-1} x$ :
Let $y=\mathfrak{a} \operatorname{inh}^{-1} x ; x, y \quad R$
Then $x=\sinh y$

$$
\begin{aligned}
& \frac{d x}{d y}=\cosh y \quad \Rightarrow \frac{d y}{d x}=\frac{1}{\cosh y} \quad\left(\because \frac{d y}{d x} \frac{1}{d x}\right) \\
& \text { or } \quad \frac{d y}{d x}=\frac{1}{\cosh y}=\frac{1}{\sqrt{1+\sinh ^{2} y}}> \quad(\because \cosh y \quad 0) \\
& \frac{d y}{d x}=\frac{d}{d x}\left(\operatorname{asinh}^{-1} x\right) \quad \frac{1}{\sqrt{1+x^{2}}} \quad(x \quad R)
\end{aligned}
$$

## Derivative of $\cosh ^{-1} x$ :

Let $y=\cosh ^{-1} \alpha ; \quad \in x \ni[1), y[0$, )
Then $x=\cosh y$

$$
\begin{aligned}
& \text { and } \frac{d x}{d y}=\sinh y \quad \Rightarrow \frac{d y}{d x}=\frac{1}{\sinh y}=\quad\left(\because \frac{d y}{d x} \frac{1}{d x}\right) \\
& \text { or } \frac{d y}{d x}=\frac{1}{\sinh y}=\frac{1}{\sqrt{\cosh ^{2} y-1}} \quad(\because \sinh y>0, \text { as } y>0) \\
& \text { Thus } \frac{d y}{d x}=\frac{d}{d x}\left(\operatorname{asinh}^{-1} x\right) \quad \frac{1}{\sqrt{x^{2}-1}} \quad(x \quad 1) \\
& \text { As } \cosh ^{-1} x=\ln \left(x+\sqrt{x^{2}-1}\right), \text { so } \\
& \frac{d}{d x}\left[\cosh ^{-1} x\right]=\frac{1}{x+\sqrt{x^{2}-1}}\left(1+\frac{2 x}{2 \sqrt{x^{2}-1}}\right)=\frac{1}{x+\sqrt{x^{2}-1}} \cdot \frac{\sqrt{x^{2}-1}+x}{\sqrt{x^{2}-1}} \cdot \frac{1}{\sqrt{x^{2}-1}}
\end{aligned}
$$

## Derivative of $\tanh ^{-1} x$ :

Let $y=\tanh ^{-1} x ; \quad x \in(-1,1), y \in R$

$$
\begin{aligned}
& \text { Then } x=\tanh y \text { and } \frac{d x}{d y}=\operatorname{sech}^{2} \Rightarrow \frac{d y}{d x}=\frac{1}{\operatorname{sech}^{2} y} \quad \frac{d y}{d x} \frac{1}{d x} \\
& \frac{d y}{d x}=\frac{1}{1-\tanh ^{2} y}-\frac{1}{1-x^{2}} \quad\left(\because \operatorname{sech}^{2} y-1 \quad \tanh ^{2} y\right) \\
& \text { Thus } \frac{d}{d x}\left(\tanh ^{-1} x\right)=\frac{1}{1-x^{2}} \quad ; \quad-1<x<1 \text { or }|x| \quad 1
\end{aligned}
$$

The following differentiation formulae can be easily proved.

$$
\frac{d}{d x}\left(\cosh ^{-1} x\right)=\frac{1}{1-x^{2}} \quad \text { or }-\frac{1}{x^{2}-1} \quad|x|>1
$$

$$
\begin{aligned}
& \frac{d}{d x}\left(\operatorname{sech}^{-1} x\right)=-\frac{1}{x \sqrt{1-x^{2}}} ; \quad 0 \Rightarrow 4 \\
& \frac{d}{d x}\left(\operatorname{conech}^{-1} x\right)=\frac{1}{x \sqrt{1+x^{2}}} ; x \quad 0 \\
& \text { or } \frac{d}{d x}\left(\operatorname{conech}^{-1} x\right)=-\frac{1}{|x| \sqrt{1+x^{2}}} ; \quad x \quad \text { of }-|0|
\end{aligned}
$$

Example 1: $\quad$ Find $\frac{d y}{d x}$ if $y=\sinh ^{-1}(a x+b)$
Solution: Let $u=a x+b$, then

$$
\begin{aligned}
& y=\sinh ^{-1} u \Rightarrow \frac{d y}{d x}=\frac{1}{\sqrt{1+u^{2}}} \\
& \frac{d y}{d x}=\frac{d y}{d u} \frac{d u}{d x}=\frac{1}{\sqrt{1+u^{2}}} \frac{d u}{d x}
\end{aligned}
$$

Thus $\frac{d}{d x}\left[\sinh ^{-1}(a x+b)=\frac{1}{\sqrt{1+(a x+b)^{2}}} . a\right.$ $\left(>\frac{d u}{d x} \quad \frac{d}{d x}(a x-b) \quad a\right)$
Example 2: $\quad$ Find $\frac{d y}{d x}$ if $y=\cosh \frac{u}{2}(\sec x) \quad 0 \quad x \quad \pi / 2$
Solution: Let $u=\sec x$, then

$$
\begin{aligned}
& y=\cosh ^{-1} u \Rightarrow \frac{d y}{d x}=\frac{1}{\sqrt{u^{2}-1}} \\
& \text { and } \frac{d u}{d x}=\frac{d}{d x}(\sec x)=\sec x \tan x \\
& \text { Thus } \frac{d y}{d x}=\frac{d y}{d u} \frac{d u}{d x}=\frac{1}{\sqrt{u^{2}-1}} \frac{d u}{d x} \\
& =\frac{1}{\sqrt{\sec x}}(\sec x \tan x) \frac{1}{\tan x}(\sec x \tan x) \sec x \\
& \text { or } \frac{d}{d x}\left[\cosh ^{-1}(\sec x)\right]=\sec x
\end{aligned}
$$

## EXERCISE 2.6

1. Find $f^{x}(x)$ if
(i) $f(x)=e^{i \frac{x}{x-1}}$
(ii) $f(x)=x^{3} e^{\frac{x}{x-1}}(x \neq 0)$
(iii) $f(x)=e^{x}(1+\ln x)$
(iv) $f(x)=\frac{e^{x}}{e^{-x}+1}$
(v) $\ln \left(e^{x}+e^{-x}\right)$
(vi) $f x=\frac{e^{x u}-e^{-x u}}{e^{x u}+e^{-x u}}$
(vii) $f(x)=\sqrt{\ln \left(e^{2 x}+e^{-2 x}\right)}$
(viii) $f(x)=\ln \left(\sqrt{e^{2 x}+e^{-2 x}}\right)$
2. Find $\frac{d y}{d x}$ if
(i) $y=x^{3} \ln \sqrt{x}$
(ii) $y=x \sqrt{\ln x}$
(iii) $y=\frac{x}{\ln x}$
(iv) $y=x^{2} \ln \frac{1}{x}$
(v) $y=\ln \sqrt{\frac{x^{2}-1}{x^{2}+1}}$
(vi) $y=\ln \left(x+\sqrt{x^{2}+1}\right)$
(vii) $y=\ln \left(9-x^{2}\right)$
(viii) $y=e^{-2 x} \sin 2 x$
(ix) $y=e^{-x}\left(x^{2}+2 x^{2}+1\right)$
(x) $y=x e^{x u x}$
(xi) $y=\frac{5 e^{3 x-6}}{x}$
(xii) $y=(l n x)^{n x}$
(xiv) $y=\frac{\sqrt{x^{2}-1}(x+1)}{\left(x^{2}+1\right)^{3 / 2}}$
3. Find $\frac{d y}{d x}$ if
(i) $y=\cosh 2 x$
(ii) $y=\sinh 3 x$
(iii) $y=\tanh ^{-1}(x i n x) \quad \frac{\pi}{2} \quad x \quad \frac{\pi}{2}$
(iv) $y=\sinh ^{-1}\left(x^{2}\right)$
(v) $y=\ln (\tanh x)$
(vi) $y=\sinh ^{-1}\left(\frac{x}{2}\right)$