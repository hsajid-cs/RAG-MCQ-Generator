### 2.15 SUCCESSIVE DIFFERENTIATION (OR HIGHER DERIVATIVES):

Sometimes it is useful to find the differential coefficient of a derived function. If we denote $f^{\prime}$ as the first derivative of $f$, then $\left(f^{\prime}\right)^{\prime}$ is the derivative of $f^{\prime}$ and is called the second derivative of $f$. For convenience we write it as $f^{\prime \prime}$.

Similarly $\left(f^{\prime}\right)^{\prime}$, the derivative of $f^{\prime \prime}$, is called the third derivative of $f$ and is written as $f^{\prime \prime \prime}$. In general, for $n \geq 4$, the $n$th derivative of $f$ is written as $f^{(n)}$. Here we state different notations used for derivatives of higher orders.

|  1st derivative | 2nd derivative | 3rd derivative | $n$th derivative  |
| --- | --- | --- | --- |
|  $y^{\prime}$ | $y^{\prime \prime}$ | $y^{\prime \prime \prime}$ | $y^{(n)}$  |
|  $\frac{d y}{d x}$ | $\frac{d^{2} y}{d x^{2}}$ | $\frac{d^{3} y}{d x^{3}}$ | $\frac{d^{n} y}{d x^{n}}$  |
|  $y_{1}$ | $y_{2}$ | $y_{3}$ | $y_{n}$  |
|  $D_{i}$ | $D^{2}$ | $D^{3}$ | $D^{n}$  |
|  $\frac{d f}{d x}$ | $\frac{d^{2} f}{d x^{2}}$ | $\frac{d^{3} f}{d x^{3}}$ | $\frac{d^{n} f}{d x^{n}}$  |

Example 1: Find higher derivatives of the polynomial

$$ f(x)=\frac{1}{12} x^{4}-\frac{1}{6} x^{2}+\frac{1}{4} x^{3}+2 x+7 $$

Solution: $f^{\prime}(x)=\frac{1}{12}\left(4 x^{4}\right)-\frac{1}{6}\left(3 x^{2}\right)+\frac{1}{4}(2 x)+2+0=\frac{1}{3} x^{2}-\frac{1}{2} x^{2}+\frac{1}{2} x+2$ $f^{\prime \prime \prime}(x)=\frac{1}{3}\left(3 x^{2}\right)-\frac{1}{2}(2 x)+\frac{1}{2}(1)+0=x^{2}-x+\frac{1}{2}$ $f^{\prime \prime \prime}(x)=2 x-1$ $f^{\prime \prime}(x)=2$ All other higher derivatives are zero.

Example 2: $\quad$ Find $\frac{d^{3} y}{d x^{3}}$ if $y=\ln \left(x+\sqrt{x^{2}+a^{2}}\right)$

Solution: Give that $y=\ln \left(x+\sqrt{x^{2}+a^{2}}\right)$ Differentiating both sides of (i) w.r.t. ' $x$ ', we have

$$ \begin{aligned} \frac{d y}{d x} & =\frac{1}{x+\sqrt{x^{2}+a^{2}}} \frac{d}{d x}\left(x \quad \sqrt{x^{2} \quad a^{2}}\right) \ & =+\frac{1}{x+\sqrt{x^{2}+a^{2}}}\left[1 \quad \frac{1+2 x}{2 \sqrt{x^{2}+a^{2}}}\right] \ & =+\frac{1}{x+\sqrt{x^{2}+a^{2}}}\left(\frac{\sqrt{x^{2}+a^{2}}+x}{2 \sqrt{x^{2}+a^{2}}}\right) \end{aligned} $$

That is, $\frac{d y}{d x}=\frac{1}{\sqrt{x^{2}+a^{2}}}$ Differentiating (ii) w.r.t. ' $x$ ', we have

$$ \begin{aligned} \frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left[\left(x^{2}+a^{2}\right)^{-1 / 2}\right] \neq \frac{1}{2}\left(x^{2} \times a^{2}\right)^{-1 / 2} \quad 2 x \ \text { or } \quad \frac{d^{2} x}{d x^{2}} & =-\frac{x}{\left(x^{2}+a^{2}\right)^{1 / 2}} \end{aligned} $$

Differentiating (iii) w.r.t. ' $x$ ', we get

$$ \begin{aligned} \frac{d^{3} y}{d x^{3}} & =\frac{1 \cdot\left(x^{2}+a^{2}\right)^{1 / 2}-x \cdot \frac{3}{2}\left(x^{2}+a^{2}\right)^{1 / 2} \cdot 2 x}{\left(x^{2}+a^{2}\right)^{3 / 2} \mid} \ & =\frac{\left(x^{2}+a^{2}\right)^{1 / 2}\left[\left(x^{2}+a^{2}\right)-3 x^{2}\right]}{\left(x^{2}+a^{2}\right)^{3}} \quad \frac{a^{2}-2 x^{2}}{\left(x^{2}+a^{2}\right)^{3 / 2}} \ \frac{d^{3} y}{d x^{3}} & =\frac{2 x^{2}-a^{2}}{\left(x^{2}+a^{2}\right)^{3 / 2}} \end{aligned} $$

Example 3: $\quad$ Find $\frac{d^{2} y}{d x^{2}}$ if $y^{2}+3 a x^{2}+x^{3}=0$
Solution: Given that $y^{2}+3 a x^{2}+x^{3}=0$
Differentiating both sides of (i) w.r.t. ' $x$ ', gives

$$
\begin{aligned}
\frac{d}{d x}\left[y^{2}+3 a x^{2}+x^{3}\right]=\frac{d}{d x}(0) & =0 \\
3 y^{2} \frac{d y}{d x}+3 a(2 x)+3 x^{2}=0 & \Rightarrow y^{2} \frac{d y}{d x} \propto\left(2 a x \quad x^{2}\right) \\
& \Rightarrow \frac{d y}{d x}=-\frac{2 a x+x^{2}}{y^{2}}
\end{aligned}
$$

Differentiating both sides of (ii) w.r.t. ' $x$ ', gives

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}}= & (1) \frac{d}{d x}\left[\frac{2 a x+x^{2}}{y^{2}}\right]-\frac{(2 a+2 x) y^{2}-\left(2 a x+x^{2}\right)\left(2 y \frac{d y}{d x}\right)}{\left(y^{2}\right)^{2}} \\
= & -\frac{2(a+x) y^{2}-\left(2 a x+x^{2}\right) \cdot 2 y \cdot\left(-\frac{2 a x+x^{2}}{y^{2}}\right)}{y^{2}} \\
= & \frac{2\left[(a+x) y^{2}+\left(2 a x+x^{2}\right)\left(2 a x+x^{2}\right)\right]}{y^{2}} \\
= & \frac{2\left[(a+x) y^{2}+\left(2 a x+x^{2}\right)^{2}\right]}{y^{2} \cdot y} \\
= & \frac{2\left[(a+x)\left(-3 a x^{2}-x^{2}\right)+x^{2}(2 a+x)^{2}\right]}{y^{2}}\left(\because y^{2}=3 a x^{2} \quad x^{2}\right) \\
= & \frac{2 x^{2}\left[-(a+x)(3 a+x)+\left(4 a^{2}+x^{2}+4 a x\right)\right]}{y^{2}} \\
= & \frac{2 x^{2}\left[-\left(3 a^{2}+4 a x+x^{2}\right)+4 a^{2}+x^{2}+4 a x\right]}{y^{2}} \\
= & \frac{2 x^{2}\left[a^{2}\right]}{y^{2}} \quad \frac{-2 a^{2} x^{2}}{y^{2}}
\end{aligned}
$$

$$
\text { version: } 1.1
$$

Example 1: If $x=a(\theta \sin \theta), y \quad a(1 \cos \theta)$. Then
show that $y^{2} \frac{d^{2} y}{d x^{2}}+a=0$
Solution: Given that $x=a(\theta+\sin \theta)$
and $\quad y=a(1+\cos \theta)$
Differentiating (i) and (ii) w.r.t' $\theta^{2}$, we get

$$
\begin{aligned}
\frac{d x}{d \theta} & =a(1+\cos \theta) \\
\text { and } \frac{d y}{d \theta} & =a(-\sin \theta)
\end{aligned}
$$

Using $\frac{d y}{d x}=\frac{d y}{d \theta} \cdot \frac{d \theta}{d x}=\frac{d y}{d \theta}$ we have
$=\frac{-a \sin \theta}{a(1+\cos \theta)} \quad \frac{-\sin \theta}{1+\cos \theta}$
That is, $\frac{d y}{d x}=-\frac{\sin \theta}{1+\cos \theta}$
Differentiating (v) w.r.t. ' $x$ '

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left(-\frac{\sin \theta}{1+\cos \theta}\right) \quad \frac{d}{d \theta}\left(\frac{\sin \theta}{1+\cos \theta}\right) \quad \frac{d \theta}{d x} \\
& =-\frac{\cos \theta(1+\cos \theta)-\sin \theta(-\sin \theta)}{(1+\cos \theta)^{2}} \quad \frac{d \theta}{d x} \\
\frac{d^{2} y}{d x^{2}} & =-\frac{\cos \theta+\cos ^{2} \theta+\sin ^{2} \theta}{(1+\cos \theta)^{2}} \quad \frac{d \theta}{d x} \\
& =\frac{1+\cos \theta}{(1+\cos \theta)^{2}} \quad \frac{1}{a(1+\cos \theta)} \quad\left(\because \frac{d x}{d \theta}=a(1+\cos \theta)\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{a} \frac{1}{(1+\cos \theta)^{2}} \quad \frac{1}{a} \frac{1}{\left(\frac{y}{a}\right)^{2}} \quad \quad \left(\because 1+\cos \theta=\frac{y}{a}\right) \\
& =-\frac{1}{a} \times \frac{a^{2}}{y^{2}}=-\frac{a}{y^{2}} \\
& \text { or } \quad y^{2} \frac{d^{2} y}{d x^{2}}=-a \quad \Rightarrow y^{2} \frac{d^{2} y}{d x^{2}}+a=0
\end{aligned}
$$

Example 5: Find the first four derivatives of $\cos (a x+b)$.
Solution: Let $y=\cos (a x+b)$, then

$$
\begin{aligned}
y_{1} & =\frac{d}{d x}[\cos (a x+b)]=\sin (a x \quad b) \cdot \frac{d}{d x}\left(a x \quad b\right) \\
& =-\sin (a x+b) \times(a+0)=-\mathrm{a} \sin (a x+b) \\
y_{2} & =-\mathrm{a} \frac{a}{d x}[\sin (a x+b)]=(-\mathrm{a})[\cos (a x+b) \times(a+0)] \\
& =\mathrm{a}^{2} \cos (a x \quad b) \\
y_{3} & =-a^{2} \frac{d}{d x}[\cos (a x+b)]=\left(-a^{2}\right)[-\sin (a x+b) \times(a+0)] \\
& =a^{2} \sin (a x+b) \\
y_{4} & =a^{2} \frac{d}{d x}[\sin (a x+b)]=\left.a^{2} \times[\cos (a x+b)] \times a\right\}=a^{4} \cos (a x+b)
\end{aligned}
$$

Example 6: If $y=e^{-a x} \neq$ thenshow that $\frac{d^{2} y}{d x^{2}} \quad a^{2} y \quad 0$

Solution: As $y=e^{-a x}$, so $\frac{d y}{d x}=\frac{d}{d x}\left(e^{-a x}\right)=e^{-a x} \frac{d}{d x}(-a x)=e^{-a x} \cdot(-a)$
That is $\frac{d y}{d x}=-a y$

$$
\left(\because e^{-a x}=y\right)
$$

Now $\frac{d y}{d x}\left[\frac{d y}{d x}\right]=\frac{d}{d x}[-a y] \Rightarrow \frac{d^{2} y}{d x^{2}}=-\frac{d y}{d x}(-a)(-a y)\left(\begin{array}{lll}a & \frac{d y}{d x} & a y\end{array}\right)$
or $\frac{d^{2} y}{d x^{2}}=a^{2} y$
Differentiating (i) w.r.t. ' $x$ ' we get

$$
\begin{aligned}
& \frac{d}{d x}\left[\frac{d^{2} y}{d x^{2}}\right]=\frac{d}{d x}\left[a^{2} y\right] \Rightarrow \frac{d^{2} y}{d x^{2}}=a^{2} \frac{d y}{d x}=a^{2}(-a y)=a^{3} y \\
& \text { Thus } \frac{d^{2} y}{d x^{2}}+a^{2} y=0
\end{aligned}
$$

Example 7: If $y=S i n^{-1} \frac{x}{a}$, then show that $y_{3} \rightarrow\left(a^{2} \quad x^{2}\right)$

Solution: $y=\sin ^{-1} \frac{x}{a}$, so

$$
\begin{aligned}
y_{1}=\frac{d y}{d x} & =\frac{d}{d x}\left[\operatorname{Sin}^{-1} \frac{x}{a}\right] \frac{1}{\sqrt{1-\left(\frac{x}{a}\right)^{2}}} \frac{d}{d x}\left(\frac{x}{a}\right) \\
& =\frac{1}{\sqrt{\frac{a^{2}-x^{2}}{a^{2}}}} \frac{1}{a} \frac{a}{\sqrt{a^{2}-x^{2}}} \frac{1}{a}\left(a^{2} \quad x^{2}\right)^{-1 / 2} \\
y_{2}=\frac{d}{d x}\left[\left(a^{2}-x^{2}\right)^{-1 / 2}\right] & =-\frac{1}{2}\left(a^{2}-x^{2}\right)^{-1 / 2} \times(-2 x)=x\left(a^{2}-x^{2}\right)^{-1 / 2}
\end{aligned}
$$

## EXERCISE 2.7

1. Find $y_{1}$ if
(i) $y=2 x^{3}-3 x^{4}+4 x^{3}+x-2$
(ii) $y=(2 x+5)^{3 / 2}$
(iii) $y=\sqrt{x}+\frac{1}{\sqrt{x}}$
2. Find $y_{2}$ if
(i) $y=x^{2} \cdot e^{-x}$
(ii) $y=\ln \left(\frac{2 x+3}{3 x+2}\right)$
3. Find $y_{3}$ if
(i) $x^{2}+y^{2}=a^{2}$
(ii) $x^{3}-y^{3}=a$
(iii) $x=a \cos \theta, y=a \sin \theta$
(iv) $x=a t^{2}, y=b t^{4}$
(v) $x^{3}+y^{3}+2 g x+2 f y+c=0$
4. Find $y_{4}$ if
(i) $y=\sin 3 x$
(ii) $y=\cos ^{3} x$
(iii) $y=\ln \left(x^{2}-9\right)$
5. If $x=\operatorname{Sin} \theta, y=\operatorname{Sin} m \theta$. Show that $\left(1 \quad x \frac{1}{2}\right) y_{2} \quad \propto y_{1} \quad m^{2} y \quad 0$
6. If $y=e^{x} \sin x$, show that $\frac{d^{2} y}{d x^{2}}=2 \frac{d y}{d x} \quad 2 y \quad 0$
7. If $y=e^{x y} \sin b x$, show that $\frac{d^{2} y}{d x^{2}}=2 a \frac{d y}{d x} \quad\left(a^{2} \quad b^{2}\right) y \quad 0$
8. If $y=\left(\cos ^{-1} x\right)^{2}$, prove that $\left(1 \quad x^{2}\right) y_{2} \quad x y_{1} \quad 2 \quad 0$
9. If $y=a \cos (l n x)+b \sin (l n x)$, prove that $x^{2} \frac{d^{2} y}{d x^{2}}+b \frac{d y}{d x}+y=0$.