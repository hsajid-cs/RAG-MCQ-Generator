### 2.9 DERIVATIVES OF INVERSE TRIGONOMETRIC FUNCTIONS

Here we want to prove that

1. $\frac{d}{d x}\left[\sin ^{-1} x\right]=\frac{1}{\sqrt{1-x^{2}}}$,
$x \in(-1,1)$ or $-1<x<1$
2. $\frac{d}{d x}\left[\operatorname{Cos}^{-1} x\right]=\frac{1}{\sqrt{1-x^{2}}}$,
$x \in(-1,1)$ or $-1<x<1$
3. $\frac{d}{d x}\left[\operatorname{Tan}^{-1} x\right]=-\frac{1}{1+x^{2}}$,
$x \in R$
4. $\frac{d}{d x}\left[\operatorname{Cosec}^{-1} x\right]=-\frac{1}{|x| \sqrt{x^{2}-1}}$,
$x \in[-1,1]^{4},[-1,1]^{4}=(-\infty,-1) \cup(1, \infty)$
5. $\frac{d}{d x}\left[\operatorname{Sec}^{-1} x\right]=-\frac{1}{|x| \sqrt{x^{2}-1}}$,
$x \in[-1,1]^{4},[-1,1]^{4}=(-\infty,-1) \cup(1, \infty)$
6. $\frac{d}{d x}\left[\operatorname{Cos}^{-1} x\right]=-\frac{1}{1+x^{2}}$,
$x \in R$

Proof of (1). Let $y=\operatorname{Sin}^{-1} x$
(1).

Then $\quad x=\operatorname{Sin} y$ or $x \sin y$ for $y\left[\frac{\pi}{2}, \frac{\pi}{2}\right]$
Differentiating both sides of (ii) w.r.t. ' $x$ ', we get

$$
\begin{aligned}
& 1=\frac{d}{d x}(\sin y)=\frac{d}{d x}(\sin y) \frac{d y}{d x}=\cos y \frac{d y}{d x} \\
& \Rightarrow \quad \frac{d y}{d x}=\frac{1}{\cos y} \text { for } \quad y\left(\frac{\pi}{2}, \frac{\pi}{2}\right) \\
& =\frac{1}{\sqrt{1-\sin ^{2} y}} \quad[\because \cos y \text { is positive for } y \in\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)]
\end{aligned}
$$

Thus $\frac{d}{d x}\left(\sin ^{-1} x\right)=\frac{1}{\sqrt{1-x^{2}}}$ for $1 \quad x \quad 1$
Proof of (2). Let $y=\operatorname{Cos}^{-1} x$
Then $\quad x=\operatorname{Cos} y$ or $x \cos y$ for $y[0, \pi]$
Differentiating both sides of (ii) w.r.t. ' $x$ ', gives

$$
\begin{aligned}
& 1=\frac{d}{d x}(\cos y)=\frac{d}{d x}(\cos y) \frac{d y}{d x}-\sin y \frac{d y}{d x} \\
& \Rightarrow \quad \frac{d y}{d x}=\frac{1}{\sin y} \quad \text { for } \quad y \in(0, \pi) \\
& \quad=\frac{1}{\sqrt{1-\cos ^{2} y}} \quad[\because \sin y \text { is positive for } y \in(0, \pi)]
\end{aligned}
$$

Thus $\frac{d}{d x}\left(\operatorname{Cos}^{-1} x\right)=-\frac{1}{\sqrt{1-x^{2}}}$ for $+ \alpha \quad 4$
Proof of (3). Let $y=\operatorname{Tan}^{-1} x$
Then $\quad x=$ Tan $y$ or $x=\tan y$ for $y\left(\frac{\pi}{2}, \frac{\pi}{2}\right)$
Differentiating both sides of (ii) w.r.t. ' $x$ ', we have

$$
\begin{aligned}
& 1=\frac{d}{d x}(\tan y)=\frac{d}{d x}(\tan y) \frac{d y}{d x}=s e c^{2} y \frac{d y}{d x} \\
\Rightarrow & \frac{d y}{d x}=\frac{1}{\sec ^{2} y} \quad \text { for } \quad y \quad\left(\frac{\pi}{2}, \frac{\pi}{2}\right) \\
& =\frac{1}{1+\tan ^{2} y}=\frac{1}{1+x^{2}} \quad \text { for } \quad x \in R
\end{aligned}
$$

Thus $\frac{d}{d x}\left(\operatorname{Tan}^{-1} x\right)=\frac{1}{1+x^{2}}$ for $x \quad R$
Proof of (4). Let $y=\operatorname{Cosec}^{-1} x$
Then $\quad x=\operatorname{Gosec} y$ or $x \quad \cos \operatorname{ec} y$ for $y\left[\frac{\pi}{2}, \frac{\pi}{2}\right] \quad\{0\}$
$\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]-\{0\}$ is also written as $\left[-\frac{\pi}{2} 0\right] \cup\left[0, \frac{\pi}{2}\right]$
Differentiating both sides of (ii) w.r.t. ' $x$ ', we get

$$
\begin{aligned}
& 1=\frac{d}{d x}(\operatorname{cosec} y) \quad \frac{d}{d x}\left(\operatorname{cosec} y\right) \frac{d y}{d x} \\
& =\left(-\operatorname{cosec} y \cot y\right) \frac{d y}{d x} \\
\Rightarrow \quad & \frac{d y}{d x}=-\frac{1}{\operatorname{cosec} y \cot y} \quad \text { for } \quad y \in\left[\frac{\pi}{2}, \frac{\pi}{2}\right]-\{0\}
\end{aligned}
$$

When $y \in\left(0, \frac{\pi}{2}\right)$, cosecy and $\cot y$ are positive.
As $\operatorname{cosec} y=x$, so $x$ is positive in this case
and $\cot y=\sqrt{\operatorname{cosec}^{2} y-1}=\sqrt{x^{2}-1} \quad$ for all $x>1$
Thus $\frac{d}{d x}\left(\operatorname{Cosec}^{-1} x\right)=\frac{-1}{x \sqrt{x^{2}-1}} \quad$ for $\quad x \quad 1$

When $y \in\left(-\frac{\pi}{2}, 0\right)$, cosec $y$ and $\cot y$ are negative
As $\operatorname{cosec} y=x$, so $x$ is negative in this case
and $\cot y=-\sqrt{\operatorname{cosec}^{2} y-1}=-\sqrt{x^{2}-1} \quad$ when $x<-1$

$$
\begin{aligned}
& \text { Thus } \frac{d}{d x}\left[\operatorname{Cosec}^{-1} x\right]=\frac{-1}{x\left(-\sqrt{x^{2}-1}\right)} \quad(x \quad 1) \\
& =\frac{-1}{(-x) \sqrt{x^{2}-1}} \quad(x \quad 1) \\
& \frac{d}{d x}\left[\operatorname{cosec}^{-1} x\right]=-\frac{1}{|x| \sqrt{x^{2}-1}} \quad \text { for } \quad x \in[-1,1]^{r}
\end{aligned}
$$

Proof of (5). is left as an exercise
Proof of (6). is similar to that of (4)

Example 1: $\quad$ Find $\frac{d y}{d x}$ if $\quad y=x \operatorname{Sin}^{-1}\left(\frac{x}{a}\right)+\sqrt{a^{2}+x^{2}}$

Solution: Given that $y=x \operatorname{Sin}^{-1}\left(\frac{x}{a}\right)+\sqrt{a^{2}+x^{2}}$
Differentiating w.r.t. $x$, we have

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left[x \operatorname{Sin}^{-1} \frac{x}{a}+\sqrt{a^{2}+x^{2}}\right]=\frac{d}{d x}\left[x \operatorname{Sin}^{-1} \frac{x}{a}\right]+\frac{d}{d x}\left(a^{2}+x^{2}\right)^{1 / 2} \\
& =1 \cdot \operatorname{Sin}^{-1} \frac{x}{a}+x \cdot \frac{1}{\sqrt{1-\left(\frac{x}{a}\right)^{2}}} \cdot \frac{d}{d x}\left(\frac{x}{a}\right) \cdot \frac{1}{2}\left(\omega^{2} \quad x^{2}\right)^{\frac{1}{2}-1} \cdot \frac{d}{d x}\left(\omega^{2} \quad x^{2}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \operatorname{Sin}^{-1} \frac{x}{a}+x \frac{1}{\sqrt{1-\frac{x^{2}}{a^{2}}}} \frac{1}{a}+\frac{1}{2 \sqrt{a^{2}-x^{2}}}(-2 x) \\
& \operatorname{Sin}^{-1} \frac{x}{a}+x \frac{a}{\sqrt{a^{2}-x^{2}}} \frac{1}{a}-\frac{1}{\sqrt{a^{2}-x^{2}}}=\operatorname{Sin}^{-1} \frac{x}{a}
\end{aligned}
$$

Example 2: If $y=\tan \left(2 \operatorname{Tan}^{-1} \frac{x}{2}\right)$, show that $\frac{d y}{d x}-\frac{4\left(1+y^{2}\right)}{4+x^{2}}$

Solution: Let $u=2 \operatorname{Tan}^{-1} \frac{x}{2}$, then

$$
y=\tan u \Rightarrow \frac{d y}{d u}=\sec ^{2} u=1+\tan ^{2} u=1+y^{2}
$$

and $\frac{d u}{d x}=\frac{d}{d x}\left(2 \sqrt{\tan ^{-1} \frac{x}{2}}\right) \cdot \mathbb{2} \frac{1}{1+\left(\frac{x}{2}\right)^{2}} \frac{d}{d x}\left(\frac{x}{2}\right)-\frac{2}{1+\frac{x^{2}}{4}} \frac{1}{2}-\frac{4}{4+x^{2}}$
Thus $\frac{d y}{d x}=\frac{d y}{d u} \frac{d u}{d x}=\left(1 \quad y^{2}\right) \cdot \frac{4}{4+x^{2}}-\frac{4\left(1+y^{2}\right)}{4+x^{2}}$

## EXERCISE 2.5

1. Differentiate the following trigonometric functions from the first principle,
(i) $\sin x$
(ii) $\tan 3 x$
(iii) $\sin 2 x+\cos 2 x$
(iv) $\cos x^{2}$
(v) $\tan ^{2} x$
(vi) $\sqrt{\tan x}$
(vii) $\cos \sqrt{x}$
2. Differentiate the following w.r.t. the variable involved
(i) $x^{2} \sec 4 x$
(ii) $\tan ^{2} \theta \sec ^{2} \theta$
(iii) $(\sin 2 \theta-\cos 3 \theta)^{2}$
(iv) $\cos \sqrt{x}+\sqrt{\sin x}$
version: 1.1
3. Find $\frac{d y}{d x}$ if
(i) $y=x \cos y$
(ii) $x=y \sin y$
4. Find the derivative w.r.t. $x$
(i) $\cos \sqrt{\frac{1+x}{1+2 x}}$
(ii) $\sin \sqrt{\frac{1+2 x}{1+x}}$
5. Differentiate
(i) $\sin x$ w.r.t. $\cot x$
(ii) $\sin ^{2} x$ w.r.t. $\cos ^{4} x$
6. If $\tan y(1+\tan x)=1 \tan x$, show that $\frac{d y}{d x}=1$
7. If $y=\sqrt{\tan x+\sqrt{\tan x+\sqrt{\tan x}}}+\ldots \infty$, prove that $\cdot(2 y \quad \frac{1}{2} \frac{d y}{d x} \quad \sec ^{2} x$.
8. If $x=a \cos ^{3} \theta, y=b \sin ^{3} \theta$, show that $a \frac{d y}{d x} \approx b \tan \theta \quad 0$
9. Find $\frac{d y}{d x}$ if $x=a(\cos t+\sin t), y=a(\sin t-t \cos t)$
10. Differentiate w.r.t. $x$
(i) $\operatorname{Cos}^{-1} \frac{x}{a}$
(ii) $\operatorname{Cot}^{-1} \frac{x}{a}$
(iii) $\frac{1}{a} \operatorname{Sin}^{-1} \frac{a}{x}$
(iv) $\operatorname{Sin}^{-1} \sqrt{1-x^{2}}$
(v) $\operatorname{Sec}^{-1}\left(\frac{x^{2}+1}{x^{2}-1}\right)$
(vi) $\operatorname{Cot}^{-1}\left(\frac{2 x}{1-x^{2}}\right)$
(vii) $\operatorname{Cos}^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right)$
11. $\frac{d y}{d x}=\frac{y}{x}$ if $\frac{y}{x}=\operatorname{Tan}^{-1} \frac{x}{y}$
12. If $y=\tan \left(\varphi \operatorname{Tan}^{-1} \varphi\right)$, show that $\left(1 \quad x^{2}\right) y, \quad p\left(1 \quad y^{2}\right) \quad 0$