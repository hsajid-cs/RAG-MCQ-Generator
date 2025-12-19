### 2.7 Differentiation of Implicit Relations

Sometimes the functional relation is not explicitly expressed in the form $y=f(x)$ but an equation involving $x$ and $y$ is given. To find $\frac{d y}{d x}$ from such an equation, we differentiate each term of the equation and use the chain rule where it is required. The process of finding $\frac{d y}{d x}$ in this way, is called implicit differentiation. We explain the implicit differentiation in the following examples.

Example 1: $\quad$ Find $\frac{d y}{d x}$ if $x^{2}+y^{2}=4$
Solution: Here $x^{2}+y^{2}=4$
Differentiating both sides of (i) w.r.t. ' $x$ ', we get

$$
\begin{aligned}
& 2 x+2 y \frac{d y}{d x}=0 \\
& \text { or } x+y \frac{d y}{d x}=0 \Rightarrow \frac{d y}{d x}=\frac{x}{y}
\end{aligned}
$$

Solving (i) for $y$ in terms of $x$, we have
$y \equiv \sqrt{4 x^{2}}$
$\Rightarrow y=\sqrt{4-x^{2}}$
(ii)
or $y \equiv \sqrt{4 x^{2}}$
(iii)
$\frac{d y}{d x}$ found above represents the derivative of each of functions defined as in $d x$ (ii) and (iii)

From (ii) $\frac{d y}{d x}=\frac{1}{2 \sqrt{4-x^{2}}} \times(-2 x)=\frac{x}{\sqrt{4-x^{2}}}$

$$
=-\frac{x}{y}\left(\because \sqrt{4-x^{2}=y}\right)
$$

From (iii) $\frac{d y}{d x}=-\frac{1}{2 \sqrt{4-x^{2}}} \times(-2 x)=-\frac{-x}{-\sqrt{4-x^{2}}}=-\frac{x}{y}(\because-\sqrt{4-x}=y)$

Example 2: Find $\frac{d y}{d x}$.if $y^{2}+x^{2}-4 x=5$.
Solution: Given that $y^{2}+x^{2}-4 x=5$
Differentiating both sides of (i) w.r.t. ' $x$ ', we get

$$
\begin{aligned}
& \frac{d}{d x}\left[y^{2}+x^{2}-4 x\right]=\frac{d}{d x}(5) \\
& \text { or } \quad 2 y \frac{d y}{d x}+2 x-4=0 \quad\left[\because \frac{d}{d x}\left(y^{2}\right)=\frac{d}{d x}\left(y^{2}\right) \frac{d y}{d x}=2 y \frac{d y}{d x}\right]
\end{aligned}
$$

$$
\Rightarrow \quad 2 y \frac{d y}{d x}=4-2 x \quad \Rightarrow \frac{d y}{d x}=\frac{2(2-x)}{2 y}=\frac{2-x}{y}
$$

Note: Solving (i) for $y$, we have

$$
y^{2}=5+4 x-x \quad \Rightarrow \quad y= \pm \sqrt{5+4 x-x^{2}}
$$

Thus $y=\sqrt{5+4 x-x^{2}}$
(ii)
or $\quad y=-\sqrt{5+4 x-x^{2}}$
(iv)

Each of these equations (iii) and (iv) defines a function.
Let $y=f_{1}(x)=\sqrt{5+4 x-x^{2}}$
and $y=f_{1}(x)=-\sqrt{5+4 x-x^{2}}$.
Differentiation (v) w.r.t. ' $x$ ', we get

$$
f_{1}^{\prime}(x)=\frac{1}{2}\left(5+4 x-x^{2}\right)^{-\frac{1}{2}} \times(4-2 x)=\frac{2-x}{\sqrt{5+4 x-x^{2}}}
$$

From (v), $\sqrt{5+4 x-x^{2}}=y, \quad$ so $\quad f_{1}^{\prime}(x) \quad \frac{2-x}{y}$
Also $f_{2}^{\prime}(x)=-\frac{1}{2}\left(5+4 x-x^{2}\right)^{-\frac{1}{2}} \times(4-2 x)=\frac{2-x}{-\sqrt{5+4 x-x^{2}}}$
From (vi) $-\sqrt{5+4 x-x^{2}}=y, \quad$ so $\quad f_{2}^{\prime}(x) \quad \frac{2-x}{y}$
Thus (ii) represents the derivative of $f_{1}(x)$ as well as that of $f_{2}(x)$.

Example 3: $\quad$ Find $\frac{d y}{d x}$ if $y^{2}-x y-x^{2}+4=0$.
Solution: Given that $y^{2}-x y-x^{2}+4=0$
Differentiating both sides of (i) w.r.t. ' $x$ ', gives

$$
\begin{aligned}
& \frac{d}{d x}\left(y^{2}-x y-x^{2}+4\right)=\frac{d}{d x}(0)=0 \\
& \text { or } \quad 2 y \frac{d y}{d x}-\left(1 . y+x \frac{d y}{d x}\right)-2 x+0=0 \\
& \Rightarrow \quad(2 y-x) \frac{d y}{d x}=2 x \quad y \quad \Rightarrow \frac{d y}{d x}=\frac{2 x+y}{2 y-x}
\end{aligned}
$$

Example 4: $\quad$ Find $\frac{d y}{d x}$ if $y^{2}-2 x y^{2}-x^{2} y+3 x=0$.
Solution: Differentiating both sides of the given equation w.r.t. ' $x$ ' we have

$$
\begin{aligned}
& \frac{d}{d x}\left(y^{2}-2 x y^{2}+x^{2} y+3 x\right)=\frac{d}{d x}(0)=0 \\
& \text { or } \quad \frac{d}{d x}\left(y^{2}\right)-\frac{d}{d x}\left(2 x y^{2}\right)+\frac{d}{d x}\left(x^{2} y\right)+\frac{d}{d x}(3 x)=0 \\
& \frac{d}{d x}\left(y^{2}\right)-2\left[1 . y^{2}+x \frac{d}{d x}\left(y^{2}\right)\right]+\left(2 x y+x^{2} \frac{d y}{d x}\right)+3=0
\end{aligned}
$$

Using the chain rule on $\frac{d}{d x}\left(y^{2}\right)$ and $\frac{d}{d x}\left(y^{2}\right)$, we have

$$
3 y^{2} \frac{d y}{d x}-2\left[y^{2}+x\left(2 x \frac{d y}{d x}\right)\right]+2 x y+x^{2} \frac{d y}{d x}+3=0
$$

or $\quad\left(3 y^{2}-4 x y+x^{2}\right) \frac{d y}{d x}=2 y^{2}-2 x y-3$
$\Rightarrow \quad \frac{d y}{d x}=\frac{2 y^{2}-2 x y-3}{3 y^{2}-4 x y+x^{2}}$
Example 5: Differentiate $x^{2}+\frac{1}{x^{2}}$ w.r.t. $x-\frac{1}{x}$
Solution: Let $y=x^{2} \frac{1}{x^{2}}=$ and $u \quad x \frac{1}{x}$. Then

$$
\begin{aligned}
& \frac{d y}{d x}=2 x+(-2) \frac{1}{x^{2}}=2\left(x-\frac{1}{x^{2}}\right)=\frac{2\left(x^{2}-1\right)}{x^{2}}=\frac{2\left(x^{2}-1\right)\left(x^{2}+1\right)}{x^{2}} \\
& \text { and } \quad \frac{d u}{d x}=1-(-1) \frac{1}{x^{2}}=1+\frac{1}{x^{2}}=\frac{x^{2}+1}{x^{2}} \\
& \text { Thus } \frac{d y}{d u}=\frac{d y}{d x} \frac{d x}{d u}=\frac{2\left(x^{2}-1\right)\left(x^{2}+1\right)}{x^{2}} \times \frac{x^{2}}{x^{2}+1} \quad \frac{2\left(x^{2}-1\right)}{x} \quad 2\left(x \quad \frac{1}{x}\right)
\end{aligned}
$$

## EXERCISE 2.4

1. Find $\frac{d y}{d x}$ by making suitable substitutions in the following functions defined as:
(i) $y=\sqrt{\frac{1-x}{1+x}}$
(ii) $y=\sqrt{x+\sqrt{x}}$
(iii) $y=x \sqrt{\frac{a+x}{a-x}}$
(iv) $y=\left(3 x^{2}-2 x+7\right)^{6}$
(v) $\sqrt{\frac{a^{2}+x^{2}}{a^{2}-x}}$
2. Find $\frac{d y}{d x}$ if:
(i) $3 x+4 y+7=0$
(ii) $x y+y^{2}=2$
(iii) $x^{2}-4 x y-5 y=0$
(iv) $4 x^{2}+2 k x y+b y^{2}+2 g x+2 f y+c=0$
(v) $x \sqrt{1+y}+y \sqrt{1+x}=0$
(vi) $y\left(x^{2}-1\right)=x \sqrt{x^{2}+4}$
3. Find $\frac{d y}{d x}$ of the following parametric functions
(i) $x=\theta+\frac{1}{\theta}$ and $y=\theta+1$
(ii) $x=\frac{a\left(1-t^{2}\right)}{1+t^{2}}, y=\frac{2 b t}{1+t^{2}}$
4. Prove that $y \frac{d y}{d x}+x=0$ if $x=\frac{1-t^{2}}{1+t^{2}}, y=\frac{2 t}{1+t}$

5. Differentiate
(i) $x^{2}-\frac{1}{x^{2}}$ w.r.t $x^{4}$
(ii) $\left(1+x^{2}\right)^{n}$ w.r.t $x^{2}$
(iii) $\frac{x^{2}+1}{x^{2}-1}$ w.r.t $\frac{x-1}{x+1}$
(iv) $\frac{a x+b}{c x+d}$ w.r.t $\frac{a x^{2}+b}{a x^{2}+d}$
(v) $\frac{x^{2}+1}{x^{2}-1}$ w.r.t $x^{3}$