### 2.13 DERIVATIVE OF HYPERBOLIC FUNCTIONS

The functions defined by:

$$
\begin{aligned}
& \sinh x=\frac{e^{x}-e^{-x}}{2}, x \in R ; \cosh x=\frac{e^{x}+e^{-x}}{2} ; x \in R \\
& \tanh x=\frac{\sinh x}{\cosh x}=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}} ; x \in R
\end{aligned}
$$

are called hyperbolic functions.
The reciprocals of these three functions are defined as:

$$
\begin{aligned}
& \operatorname{cosech} x=\frac{1}{\sinh x}=\frac{2}{e^{x}-e^{-x}}, x \in R-\{0\} \\
& \operatorname{sech} x=\frac{1}{\cosh x}=\frac{2}{e^{x}+e^{-x}}, x \in R \\
& \operatorname{coth}=\frac{1}{\tanh x}=\frac{e^{x}+e^{-x}}{e^{x}-e^{-x}}, x \in R-\{0\}
\end{aligned}
$$

Derivatives of $\sin h x, \cos h x$ and $\tan h x$ are found as explained below:

$$
\begin{aligned}
& \frac{d}{d x}(\sinh x)=\frac{d}{d x}\left[\frac{1}{2}\left(e^{x}-e^{-x}\right)\right]=\frac{1}{2}\left[e^{x}-e^{-x} t-1 j\right]=\frac{1}{2}\left(e^{x}+e^{-x}\right)=\cosh x \\
& \frac{d}{d x}(\cosh x)=\frac{d}{d x}\left[\frac{1}{2}\left(e^{x}+e^{-x}\right)\right]=\frac{1}{2}\left[e^{x}+e^{-x} \cdot t-1 j\right]=\frac{1}{2}\left(e^{x}-e^{-x}\right)=\sinh x \\
& \frac{d}{d x}[\tanh x]=\frac{d}{d x} \frac{e^{x}-e^{-x}}{e^{x}+e^{-x}} \cdot \frac{\left(e^{x}+e^{-x}\right)\left(e^{x}+e^{-x}\right)-\left(e^{x}-e^{-x}\right)\left(e^{x}-e^{-x}\right)}{\left(e^{x}+e^{-x}\right)^{2}} \\
& =\frac{e^{2 x}+e^{-2 x}+2-\left(e^{2 x}+e^{-2 x}-2\right)}{\left(e^{x}+e^{-x}\right)^{2}} \quad \frac{4}{\left(e^{x}+e^{-x}\right)^{2}} \\
& =\left(\frac{2}{e^{x}+e^{-x}}\right)^{2}=\operatorname{sech}^{2} x
\end{aligned}
$$

The following results can easily be proved.

$$
\begin{aligned}
& \frac{d}{d x}(\cos e h x)=\operatorname{coth} x \cos \operatorname{ech} x ; \frac{d}{d x}(\operatorname{sech} x) \quad \tanh x \operatorname{sech} x \\
& \frac{d}{d x}(\operatorname{coth} x)=-\cos e c h^{2} x
\end{aligned}
$$

Example 1: $\quad$ Find $\frac{d y}{d x}$ if $y=\sinh 2 x$
Solution: Let $u=2 x$, then

$$
y=\sinh u \quad \Rightarrow \frac{d y}{d u}=\cosh u
$$

and $\frac{d u}{d x}=\frac{d}{d x}(2 x)=2$.
Thus $\frac{d y}{d x}=\frac{d y}{d u} \cdot \frac{d u}{d x}=\cosh u \cdot \frac{d u}{d x}=[\cosh (2 x)]. 2=2 \cosh 2 x$
or $\frac{d}{d x}[\sinh 2 x]=2 \cosh 2 x$.
Example 2: $\quad$ Find $\frac{d y}{d x}$ if $y=\tanh \left(x^{2}\right)$
Solution: Let $u=x^{2}$, then $y=\tanh u \Rightarrow \frac{d y}{d u}=\operatorname{sech}^{2} u$
and $\frac{d u}{d x}=\frac{d}{d x}(x)=2 x$
Thus $\frac{d y}{d x}=\frac{d y}{d u} \cdot \frac{d u}{d x}=\operatorname{sech}^{2} u \cdot \frac{d u}{d x}=\left[\operatorname{sech}^{2}\left(x^{2}\right)\right] \quad 2 x$
or $\frac{d}{d x}\left[\tanh x^{2}\right]=2 x \operatorname{sech}^{2} x^{2}$