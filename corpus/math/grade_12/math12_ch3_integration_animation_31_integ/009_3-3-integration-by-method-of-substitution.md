### 3.3 INTEGRATION BY METHOD OF SUBSTITUTION

Sometimes it is possible to convert an integral into a standard form or to an easy integral by a suitable change of a variable. Now we evaluate $\int f(x) d x$ by the method of substitution. Let $x$ be a function of a variable $t$, that is,

$$
\begin{aligned}
& \text { if } \\
& x=\phi(t), \quad \text { then } \quad d x=\phi^{\prime}(t) d t \\
& \text { Putting } \quad x=\phi(t) \quad \text { and } \quad d x=\phi^{\prime}(t) d t \text {, we have } \\
& \int f(x) d x=\int f(\phi(t) \phi^{\prime}(t)) d t .
\end{aligned}
$$

Now we explain the procedure with the help of some examples.
Example 1: $\quad$ Evaluate $\int \frac{a d t}{2 \sqrt{a t+b}} \quad(a t+b>0)$
Solution: $\quad$ Let $a t+b=u$. Then

$$
a d t=d u
$$

Thus $\int \frac{a d t}{2 \sqrt{a t+b}}=\int \frac{d u}{2 \sqrt{u}}=\frac{1}{2} \int u^{\frac{1}{2}} d u$

$$
=\frac{1}{2}\left(\frac{u^{-\frac{1}{2}+1}}{-\frac{1}{2}+1}\right)+c=\frac{1}{2}\left(\frac{u^{\frac{1}{2}}}{1}\right)+c=u^{\frac{1}{2}}+c=\sqrt{a t+b}+c
$$

Example 2: $\quad$ Evaluate $\int \frac{x}{\sqrt{4+x^{2}}} d x$.
Solution: Put $4+x^{2}=t$

$$
\begin{aligned}
& \Rightarrow 2 x d x=d t \text { or } x d x=\frac{1}{2} d t \text {, therefore } \\
& \int \frac{x}{\sqrt{4+x^{2}}} d x=\int \frac{1}{\sqrt{t}}\left(\frac{1}{2}\right) d t \quad \frac{1}{2} \int t^{\frac{-1}{2}} d t \quad+\frac{1}{2} \frac{t^{1 / 2}}{1 / 2} \quad c \\
& =\sqrt{t}+c=\sqrt{4+x^{2}}+c
\end{aligned}
$$

Example 3: $\quad$ Evaluate $\int x \sqrt{x-a} d x, \quad(x>a)$
Solution: $\quad$ Let $x-a=t \Rightarrow x=a+t$

$$
\Rightarrow d x=d t
$$

Thus $\int x \sqrt{x-a} d x=\int(a+t) \sqrt{t} d t$

$$
\begin{aligned}
& =\int\left(a t^{\frac{1}{2}}+t^{\frac{1}{2}}\right) d t=a \int t^{\frac{1}{2}} d t+\int t^{\frac{1}{2}} d t \\
& =a \frac{t^{\frac{1}{2}}}{3}+\frac{t^{\frac{1}{2}}}{2}+c=\frac{2 a}{3} t^{\frac{1}{3}}+\frac{2}{5} t^{\frac{1}{3}}+c \\
& =2 t^{\frac{1}{3}}\left(\frac{a}{3}+\frac{1}{3} t\right)+c=2(x-a)^{\frac{1}{3}}\left(\frac{a}{3}+\frac{1}{5}(x-a)\right)+c \\
& =2(x-a)^{\frac{1}{3}}\left(\frac{5 a+3(x-a)}{15}\right) \quad \propto \quad \frac{2}{15}(x-a)^{\frac{1}{3}}(5 a \quad 3 x \quad 3 a) \quad c \\
& =\frac{2}{15}(x-a)^{\frac{1}{3}}(2 a+3 x)+c
\end{aligned}
$$

Example 4: $\quad$ Evaluate $\int \frac{\cot \sqrt{x}}{x} d x . \quad(x>0)$.
Solution: $\quad$ Put $\sqrt{x}=z$,
then $d(\sqrt{x})=\infty d z \quad \frac{1}{2 \sqrt{x}} d x \quad d z$
or $\quad \frac{1}{\sqrt{x}} d x=2 d z$
thus $\int \frac{\cot \sqrt{x}}{\sqrt{x}} d x=\int \cot \sqrt{x} \frac{1}{\sqrt{x}} d x \quad \int \cot z .(2 d z)$

$$
\begin{aligned}
& =2 \int \cot z d z \quad 2 \int \frac{\cos z}{\sin z} d z \quad 2 \int(\sin z)^{-1} \cos z d z \\
& =2 \ln |\sin z|+c, \quad \overline{(z>0} \text { as } x>0) \\
& =\mathbb{R} \ln |\sin \sqrt{x}| \quad c
\end{aligned}
$$

Example 5: Evaluate (i) $\int \cos \varepsilon x d x \quad$ (ii) $\int \sec x d x$
Solution: $\int \cos \varepsilon x d x=\int \frac{\cos \varepsilon x(\cos \varepsilon x-\cot x)}{\cos \varepsilon x-\cot x} d x$
Put $\cos \varepsilon x \cot x=t$, then $\left(\cos \varepsilon x \cot x \quad \cos \varepsilon^{2} x\right) \cdot d x \quad d t$
or $\cos \varepsilon x(\cos \varepsilon x-\cot x) d x=d t$
so $\int \frac{\cos \varepsilon x(\cos \varepsilon x-\cot x)}{(\cos \varepsilon x-\cot x)} d x=\int \frac{1}{t} d t=\ln |t|+c$
Thus $\cos \varepsilon x d x=\ln \left|\cos \varepsilon x-\cot x\right|+c \quad[\because t=\cos \varepsilon x-\cot x]$
(ii) $\int \sec x d x=\int \frac{\sec x(\sec x+\tan x)}{(\sec x+\tan x)} d x$

Put $\sec x+\tan x=t$, then $\left(\sec x \tan x+\sec ^{2} x\right) d x=d t$
or $\sec x(\sec x+\tan x) d x=d t$
so $\int \frac{\sec x(\sec x-\tan x)}{(\sec x-\tan x)} d x=\int \frac{1}{t} d t=\ln |t|+c$
Thus $\int \sec x d x=\ln |\sec x+\tan x|+c \quad(\because t=\sec x+\tan x)$
Example 6: Evaluate $\int \cos ^{3} x \sqrt{\sin x} d x .(\sin x>0)$.
Solution: $\quad$ Put $\sqrt{\sin x}=t$, then $d t=\left[\frac{1}{2 \sqrt{\sin x}} \cdot \cos x\right] d x$
or $2 t d t==\cos x d x \quad[\because \sqrt{\sin x} \quad t]$
Putting $\sqrt{\sin x}==t$ and $\cos x d x \quad 2 t d t$ in the integral, we have,
$\int \cos ^{2} x \sqrt{\sin x} \cos x d x=\int\left(1-t^{4}\right) \cdot t=2 t d t, \quad\left(\because \cos ^{2} x=1 \approx \sin ^{2} x \quad 1 \quad t^{4}\right)$

$$
=2 \int\left(t^{2}-t^{4}\right) d t=2 \int t^{2} d t-2 \int t^{6} d t
$$

$$
=2 \cdot \frac{t^{3}}{3}-2 \frac{t^{3}}{7}+c
$$

$$
=\frac{2}{3}(\sin x)^{\frac{3}{2}}-\frac{2}{3}(\sin x)^{\frac{3}{2}}+c=\frac{2}{3} \sin ^{\frac{3}{2}} x-\frac{2}{7} \sin ^{\frac{3}{2}} x+c
$$

Version: 1.1

Example 7: Evaluate $\int \sqrt{1+\sin x} d x .\left(-\frac{\pi}{2}<x<\frac{\pi}{2}\right)$
Solution: $\int \sqrt{1+\sin x} d x=\int \sqrt{1} \sin x \frac{\sqrt{1-\sin x}}{\sqrt{1-\sin x}} d x=\int \frac{\sqrt{1-\sin ^{2} x}}{\sqrt{1-\sin x}} d x$

$$
=\int \frac{\cos x}{\sqrt{1-\sin x}} d x
$$

Put $\sin x=t$, then $\cos x d x=d t$, therefore

$$
\begin{aligned}
\int \sqrt{1+\sin x} d x & =\int \frac{1}{\sqrt{1-\sin x}} \cdot \cos x d x=\int \frac{d t}{\sqrt{1-t}}=\int(1-t)^{\frac{1}{2}} d t \\
& =\frac{(1-t)^{\frac{1}{2}} \cdot \cdot}{\left(-\frac{1}{2}+1\right)(-1)+c}=-2 \sqrt{1-t}+c \\
& =\frac{2 \sqrt{1} \quad \sin x}{2 \sqrt{1}}
\end{aligned}
$$

Example 8: Find $\int \frac{d x}{x(\ln 2 x)}, \quad(x>0)$
Solution: Put $\ln 2 x=t$, then

$$
\begin{aligned}
& \frac{1}{2 x} \cdot 2 d x=d t \quad \text { or } \quad \frac{1}{x} d x=d t \\
& \text { Thus } \int \frac{1}{(\ln 2 x)^{3}} \cdot \frac{1}{x} d x=\int \frac{1}{t^{2}} \cdot d t=\int t^{-1} d t=\frac{t^{-2}}{-2}+c \\
& \quad=-\frac{1}{2 t^{2}}+c=-\frac{1}{2(\ln 2 x)^{2}}+c
\end{aligned}
$$

Example 9: Find $\int a^{a^{2}} x d x . \quad(a>0, a \neq 1)$
Solution: Put $x^{2}=t$, then $x d x=\frac{1}{2} d t$
Thus $\int a^{a^{2}} x d x=\int a^{2} \times \frac{1}{2} d t$

$$
=\frac{1}{2} \int a^{c} d t=\frac{1}{2} \frac{a^{t}}{l n a}+c=\frac{a^{x^{2}}}{2 l n a}+c
$$

Example 10: Evaluate
(i) $\int \frac{1}{\sqrt{a^{2}-x^{2}}} d x, \quad(-a<x<a)$
(ii) $\int \frac{1}{x \sqrt{x^{2}-a^{2}}} d x,(x>a$ or $x<-a)$

## where $a$ is positive.

Solution: (i) Let $\quad x=a \operatorname{Sin} \theta, \quad$ that is,

$$
x=a \operatorname{Sin} \theta \quad \text { for }-\frac{\pi}{2}<\theta<\frac{\pi}{2}, \quad \text { then } d x=a \cos \theta d \theta
$$

Thus $\int \frac{d x}{\sqrt{a^{2}-x^{2}}}=\int \frac{a \cos \theta d \theta}{\sqrt{a^{2}-a^{2}} \sin ^{2} \theta}$

$$
\begin{aligned}
& =\int \frac{a \cos \theta d \theta}{a \sqrt{1-\sin ^{2} \theta}} \int \frac{a \cos \theta d \theta}{a \cos \theta} \\
& =\int 1 d \theta=\theta+c \\
& =\operatorname{Sin}^{-1}\left(\frac{x}{a}\right) \quad c \quad\left(\sqrt{-\frac{x}{a}} \quad \operatorname{Sin} \theta\right)
\end{aligned}
$$

(ii) Put $x=a \operatorname{Sec} \theta$ i.e., $x=a \sec \theta \quad$ for $\theta<\theta<\frac{\pi}{2}$ or $\frac{\pi}{2}<\theta<\pi$. Then $d x=a \sec \theta \tan \theta d \theta$

$$
\begin{aligned}
& \text { Thus } \int \frac{d x}{x \sqrt{x^{2}-a^{2}}}=\int \frac{a \sec \theta \tan \theta d \theta}{a \sec \theta \sqrt{a^{2} \sec ^{2} \theta-a^{2}}} \\
& =\int \frac{a \sec \theta \tan \theta d \theta}{a \sec \theta a \tan \theta} \quad\left(\sqrt{\sqrt{a^{2}\left(\sec ^{2} \theta \quad 1\right)}}\right. \\
& =\frac{1}{a} \int 1 d \theta=\frac{1}{a} \quad \theta+c \quad=\sqrt{a^{2} \tan ^{2}}=a \tan \theta) \\
& =\frac{1}{a} \operatorname{Sec}^{-1} \frac{x}{a} \quad c . \quad\left(\sqrt{\operatorname{Sec} \theta} \quad \frac{x}{a}\right)
\end{aligned}
$$

version: 1.1