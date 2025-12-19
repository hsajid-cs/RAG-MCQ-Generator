### 3.1.3 Finding $\frac{d y}{d x}$ by using differentials

We explain the process in the following example.
Example: Using differentials find $\frac{d y}{d x}$ when $\frac{y}{x}-\ln x=\ln c$
Solution: Finding differentials of both sides of the given equation, we get

$$
d\left[\frac{y}{x}-\ln x\right]=d[\ln c]=0
$$

using $d(f \pm g)=d f \pm d g$, we have

$$
d\left[\frac{y}{x}\right]-d(\ln x) \gg 0 \quad \frac{d}{d x}\left[y \frac{1}{x}\right] \quad \frac{1}{x} d x \quad 0
$$

Using $d(f g)=f d g+g d f$, we get

$$
\begin{aligned}
& y d\left(\frac{1}{x}\right)+\frac{1}{x} d y-\frac{1}{x} d x=0 \\
& y \times\left(\frac{1}{x^{2}} d x\right)+\frac{1}{x} d y-\frac{1}{x} d x=0 \Rightarrow \frac{1}{x} d y=\frac{1}{x} d x+\frac{y}{x^{2}} d x
\end{aligned}
$$

$$
\begin{aligned}
& \text { or } \quad \frac{1}{x} d y=\left(\frac{1}{x} \quad \frac{y}{x^{2}}\right) d x \quad\left(\frac{x+y}{x^{2}}\right) d x \quad \frac{1}{x}\left(\frac{x+y}{x}\right) d x \\
& \Rightarrow d y=\left(\frac{x+y}{x}\right) d x \\
& \text { Thus } \quad \frac{d y}{d x}=\frac{x+y}{x} \quad\left[\because d y=f^{\prime}(x) d x\right]
\end{aligned}
$$