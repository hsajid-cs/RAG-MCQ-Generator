### 2.12 LOGARITHMIC DIFFERENTIATION

Algebraic expressions consisting of product, quotient and powers can be often simplified before differentiation by taking logarithm.

Example 1: $\quad$ Differentiate $y=e^{f(y)}$ w.r.t.' $x^{\prime}$.
Solution: Here $y=e^{f(x)}$
Taking logarithm of both sides of (i), we have

$$
\begin{aligned}
\ln y & =f(x) \cdot \ln e \\
& =f(x) \\
& \text { ( } \because \text { In } \mathrm{e}=1)
\end{aligned}
$$

Differentiating w.r.t $x$, we get

$$
\begin{aligned}
& \frac{1}{y} \cdot \frac{d y}{d x}=f^{\prime}(x) \\
& \text { So } \frac{d y}{d x} y \quad f^{\prime}(x) \quad e^{f(x)} \quad f^{\prime}(x) \\
& \text { or } \frac{d}{d x}\left(e^{f(x)}\right)=e^{f(x)} \times f^{\prime}(x)
\end{aligned}
$$

Example 2: $\quad$ Find derivative of $\frac{x \sqrt{x^{2}+3}}{x^{2}+1}$
Solution: Let $y=\frac{x \sqrt{x^{2}+3}}{\left(x^{2}+1\right)}$
Taking logarithm of both sides, we have

$$
\ln y=\ln \left(\frac{x \sqrt{x^{2}+3}}{x^{2}+1}\right)=\ln \left(x \sqrt{x^{2}+3}\right)-\ln \left(x^{2}+1\right)
$$

or $\ln y=\ln x+\frac{1}{2} \ln \left(x^{2}+3\right)-\ln \left(x^{2}+1\right)$
Differentiating both sides of (ii) w.r.t ' $x$ ',

$$
\begin{aligned}
& \frac{d}{d x}[\ln y]=\frac{d}{d x}\left[\ln x+\frac{1}{2} \ln \left(x^{2}+3\right)-\ln \left(x^{2}+1\right)\right] \\
& \frac{1}{y} \frac{d y}{d x}=\frac{1}{x}+\frac{1}{2} \cdot \frac{1}{x^{2}+3}+2 x-\frac{1}{x^{2}+1}+2 x \\
& \quad \frac{1}{x} \cdot \frac{x}{x^{2}+3}-\frac{2 x}{x^{2}+1} \\
& =\frac{\left(x^{2}+3\right)\left(x^{2}+1\right)+x \cdot x\left(x^{2}+1\right)-2 x \cdot x\left(x^{2}+3\right)}{x\left(x^{2}+3\right)\left(x^{2}+1\right)} \\
& =\frac{x^{4}+4 x^{2}+3+x^{4}+x^{2}-2 x^{4}-6 x^{2}}{x\left(x^{2}+3\right)\left(x^{2}+1\right)} \cdot \frac{3-x^{2}}{x\left(x^{2}+3\right)\left(x^{2}+1\right)} \\
& \text { Thus } \frac{d y}{d x}=\frac{y\left(3-x^{2}\right)}{x\left(x^{2}+1\right)\left(x^{2}+1\right)} \cdot \frac{y \sqrt{x^{2}+3}}{x^{2}+1} \cdot \frac{3-x^{2}}{x\left(x^{2}+3\right)\left(x^{2}+1\right)} \\
& =\frac{3-x^{2}}{\sqrt{x^{2}+3} \cdot\left(x^{2}+1\right)^{2}}
\end{aligned}
$$

Example 3: Differentiate $(\ln x)^{t}$ w.r.t. ' $x$ '.

Solution: Let $y=(\ln x)^{t}$
Taking logarithm of both sides of (i), we have

$$
\ln y=\ln \left[(\ln x)^{t}\right] \quad x \ln (\ln x)
$$

Differentiating w.r.t $x$,

$$
\begin{aligned}
\frac{1}{y} \frac{d y}{d x} & =1 \cdot \ln (\ln x)+x \cdot \frac{1}{\ln x} \cdot \frac{d}{d x}(\ln x) \\
& =\ln (\ln x)+x \cdot \frac{1}{\ln x} \cdot \frac{1}{x}=\ln (\ln x)+\frac{1}{\ln x} \\
\frac{d y}{d x} & =y\left[\ln (\ln x)+\frac{1}{\ln x}\right]=(\ln x)^{t}\left[\ln (\ln x)+\frac{1}{\ln x}\right]
\end{aligned}
$$