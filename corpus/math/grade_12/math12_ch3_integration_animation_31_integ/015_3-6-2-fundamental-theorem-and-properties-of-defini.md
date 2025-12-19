### 3.6.2 Fundamental Theorem and Properties of Definite Integrals

The Definite integral $\int_{a}^{b} f(x) d x$
gives the area under the curve $y=f(x)$ from $x=a$ to $x=b$ and the $x$-axis (proof is given in the article 3.6.1)

## (b) Fundamental Theorem of Calculus

If $f$ is continuous on $[a, b]$ and $\phi^{\prime}(x)=f(x)$, that is,
$\phi(x)$ is any anti-derivative of $f$ on $[a, b]$, then

$$
\int f(x) d x=\phi(b)-\phi(a)
$$

Note that the difference $\phi(b)-\phi(a)$ is independent of the choice of anti-derivative of the function $f$.
(c) $\int_{a}^{b} f(x) d x=-\int_{a}^{b} f(x) d x$
(d) $\int_{a}^{b} f(x) d x=\int_{a}^{b} f(x) d x+\int_{a}^{b} f(x) d x, \quad a \quad c \quad b$

## Proof of (c) and (d):

(c) If $\phi^{\prime}(x)=f(x)$, that is, if $\phi$ is an anti-derivative of $f$, then using the Fundamental Theorem of Calculus, we get

$$
\int_{a}^{b} f(x) d x=\phi(b)-\phi(a)=-[\phi(a)-\phi(b)]=-\int_{a}^{b} f(x) d x
$$

(d) If $\phi^{\prime}(x)=f(x)$, that is, if $\phi(x)$ is an anti-derivative of $f(x)$, then applying the Fundamental Theorem of Calculus, we have

$$
\int_{a}^{b} f(x) d x=\phi(c) \quad \phi(a) \text { and } \int_{a}^{b} f(x) d x \quad \phi(b) \quad \phi(c)
$$

Thus $\int_{a}^{b} f(x) d x+\int_{a}^{b} f(x) d x=\phi(c)-\phi(a)+\phi(b)-\phi(c)$

$$
=\phi(b)-\phi(c)=\int_{a}^{b} f(x) d x
$$

Other properties of definite integrals can easily be proved by applying the Fundamental Theorem of Calculus.
Now we evaluate some definite integrals in the following examples.
Example 1: $\quad$ Evaluate (i) $\quad \int_{a}^{b}\left(x^{3}+3 x^{4}\right) d x \quad$ (ii) $\quad \frac{1}{2} \frac{x^{2}+1}{x+1} d x$

## Solution:

(i) $\int_{a}^{b}\left(x^{3}+3 x^{2}\right) d x=\int_{a}^{b} x^{3} d x+\int_{a}^{b} 3 x^{2} d x$

$$
\begin{aligned}
& =\left[\frac{x^{4}}{4}\right]_{1}^{4}+\left[x^{3}\right]_{11}^{4}=\left[\frac{(3)^{4}}{4} \quad \frac{(-1)^{4}}{4}\right] \quad\left[(3)^{2} \quad(1)^{2}\right] \\
& =\left[\frac{81}{4}-\frac{1}{4}\right]+[27-(-1)]=\frac{81-1}{4}+(27+1) \\
& =20+28=48
\end{aligned}
$$

(ii) $\int_{a}^{b} \frac{x^{2}+1}{x+1} d x=\int_{a}^{b} \frac{x^{2}-1+2}{x+1} d x$

$$
\begin{aligned}
& =\int_{a}^{b}\left(\frac{x^{2}-1}{x+1}+\frac{2}{x+1}\right) d x=\int_{a}^{b}\left(x-1+\frac{2}{x+1}\right) d x \\
& =\int_{a}^{b} x d x-\int_{a}^{b} 1 d x+2 \int_{a}^{b} \frac{1}{x+1} d x
\end{aligned}
$$

$$
\begin{aligned}
& =\left[\frac{x^{4}}{2}\right]_{a}^{4}-[x]_{a}^{4}+2[\ln (x+1)]_{a}^{4} \\
& =\left[\frac{(2)^{4}}{2}-\frac{(1)^{4}}{2}\right]-[2-1]+2[\ln (2+1)-\ln (1+1)] \\
& =\left(2-\frac{1}{2}\right)-1+2[\ln 3-\ln 2] \\
& =\frac{1}{2}+2 \ln \frac{3}{2}
\end{aligned}
$$

Example 2: $\quad$ Evaluate (i) $\quad \int_{a}^{\infty} \frac{x^{3}+9 x+1}{x^{2}+9} d x \quad$ (ii) $\int_{a}^{\infty} \sec x(\sec x+\tan x) d x$

## Solution:

(i) $\int_{a}^{\infty} \frac{x^{3}+9 x+1}{x^{2}+9} d x=\int_{a}^{\infty}\left(\frac{x^{3}+9 x}{x^{2}+9}+\frac{1}{x^{2}+9}\right) d x$

$$
\begin{aligned}
& =\int_{a}^{\infty}\left(\frac{x\left(x^{2}+9\right)}{x^{2}+9}+\frac{1}{x^{2}+9}\right) d x=\int_{a}^{\infty}\left(x+\frac{1}{x^{2}+9}\right) d x \\
& =\int_{a}^{\infty} x d x+\int_{a}^{\infty} \frac{1}{x^{2}+9} d x \\
& =\left(\frac{x^{2}}{2}\right)_{a}^{\infty}-\left[\frac{1}{3} \operatorname{Tan}^{-1} \frac{x}{3}\right]_{a}^{\infty}\left(\sqrt{ } \int \frac{1}{x^{2}+(3)^{2}} d x=\frac{1}{3} \operatorname{Tan}^{-1} \frac{x}{3} \quad c\right) \\
& =\left(\frac{(\sqrt{3})^{2}}{2}-\frac{(0)^{2}}{2}\right)+\frac{1}{3}\left(\operatorname{Tan}^{-1} \frac{\sqrt{3}}{3}-\operatorname{Tan}^{-1} \frac{0}{3}\right) \\
& =\left(\frac{3}{2}-0\right)+\frac{1}{3}\left(\operatorname{Tan}^{-1} \frac{1}{\sqrt{3}}-\operatorname{Tan}^{-1} 0\right) \\
& =\frac{3}{2}+\frac{1}{3}\left(\frac{\pi}{6}-0\right)=\frac{3}{2}+\frac{\pi}{18}\left(\sqrt{ } \operatorname{Tan}^{-1} \frac{1}{\sqrt{3}}=\frac{\pi}{6} \text { and } \operatorname{Tan}^{-1} 0=0\right)
\end{aligned}
$$

(ii) $\int_{0}^{\pi} \sec x(\sec x+\tan x) d x=\int_{0}^{\pi}\left(\sec ^{2} x+\sec x \tan x\right) d x$

$$
\begin{aligned}
& =+\int_{0}^{\pi} \sec ^{2} x d x \quad \int_{0}^{\pi} \sec x \tan x d x \\
& =\left[\tan x\right]_{x}^{\frac{\pi}{2}}+\left[\sec x\right]_{x}^{\frac{\pi}{2}}=\left(\tan \frac{\pi}{4} \quad \tan 0\right) \quad\left(\sec \frac{\pi}{4} \quad \sec 0\right) \\
& =(1-0)+(\sqrt{2}-1)=\sqrt{2}
\end{aligned}
$$

Example 3: $\quad$ Evaluate $\int_{0}^{\pi} \frac{1}{1-\sin x} d x$
Solution: $\int_{0}^{\pi} \frac{1}{1-\sin x} d x=\int_{\frac{\pi}{2}}^{\pi} \frac{1+\sin x}{(1-\sin x)(1+\sin x)} d x$

$$
\begin{aligned}
& =\int_{0}^{\pi} \frac{1+\sin x}{1-\sin ^{2} x} d x=\int_{\frac{\pi}{2}}^{\pi} \frac{1+\sin x}{\cos ^{2} x} d x \\
& =\int_{0}^{\pi}\left(\frac{1}{\cos ^{2} x}+\frac{\sin x}{\cos ^{2} x}\right) d x=\int_{\frac{\pi}{2}}^{\frac{\pi}{2}}\left(\sec ^{2} x \quad \sec x \tan x\right) d x \\
& =\sqrt{2} \quad \text { \{See the solution of example 2(ii) }\}
\end{aligned}
$$

Example 4: $\quad$ Evaluate $\int_{0}^{\pi}(x+|x|) d x$
Solution: $\int_{0}^{\pi}(x+|x|) d x=\int_{0}^{\pi}(x+|x|) d x+\int_{\frac{\pi}{2}}^{\pi}(x+|x|) d x \quad$ (by property (d))

$$
=\int_{0}^{\pi}[x+(-x)] d x+\int_{0}^{\pi}[x+(x)] d x \quad\binom{\because|x|=x}{=x} \text { if } x \geq 0
$$

version: 1.1

$$
\begin{aligned}
& =\int_{-1}^{0} 0 d x+\int_{0}^{1} 2 x d x=0+2 \int_{0}^{2} x d x \\
& =2\left[\frac{x^{2}}{2}\right]_{0}^{2}=2\left(\frac{4}{2}-\frac{0}{2}\right)=4
\end{aligned}
$$

Example 5: Evaluate $\quad \int_{0}^{\pi} \frac{3 x}{\sqrt{x^{2}+9}} d x$
Solution: Let $f(x)=x^{2}+9$. Then $f^{\prime}(x)=2 x$, so

$$
\begin{aligned}
\int \frac{3 x}{\sqrt{x^{2}+9}} d x & =\int \frac{\frac{3}{2}(2 x)}{\sqrt{x^{2}+9}} d x+\frac{3}{2} \int\left(x^{2} 9\right)^{\frac{1}{2}}(2 x) d x \\
& =\frac{3}{2} \int[f(x)]^{\frac{1}{2}} f(x) d x \\
& =\frac{3}{2} \frac{[f(x)]^{\frac{1}{2} \cdot}}{-\frac{1}{2}+1}=3[f(x)]^{\frac{1}{2}}+c=3\left(x^{2}+9\right)^{\frac{1}{2}}+c
\end{aligned}
$$

Thus $\int_{0}^{\pi} \frac{3 x}{\sqrt{x^{2}+9}} d x=\left[3\left(x^{2}+9\right)^{\frac{1}{2}}\right]_{0}^{\frac{1}{2}}=3\left[(7+9)^{\frac{1}{2}}-(0+9)^{\frac{1}{2}}\right]$

$$
=3\left[(16)^{\frac{1}{2}}-(9)^{\frac{1}{2}}\right]=3(4-3)=3
$$

Example 6: Evaluate $\quad \int_{0}^{\pi} \frac{\operatorname{Sin}^{-1} x}{\sqrt{1-x^{2}}} d x, \quad x \neq-1,1$
Solution: Let $t=\operatorname{Sin}^{-1} x$. Then $x=\sin t$ for $-\frac{\pi}{2} \leq t \leq \frac{\pi}{2}$
and $d x=\cos t d t=\sqrt{1-\sin ^{2} t} d t \quad\left[\because \cos t \text { is +ve for }-\frac{\pi}{2} \leq t \leq \frac{\pi}{2}\right]$

$$
=\sqrt{1-x^{2}} d t
$$

$$
\begin{aligned}
& \text { or } \frac{1}{\sqrt{1-x^{2}}} d x=d t \quad(x \neq-1,1) \\
& \text { if } \quad x=\frac{1}{2}, \text { then } \frac{1}{2}=S \text { in } t \quad \Rightarrow t=\operatorname{Sin}^{-1} \frac{1}{2}=\frac{\pi}{6} \\
& \text { and if } x=\frac{\sqrt{3}}{2} \text {, then } \frac{\sqrt{3}}{2}=\operatorname{Sin} t \quad \Rightarrow t=\operatorname{Sin}^{-1} \frac{\sqrt{3}}{2}=\frac{1}{3} \\
& \text { Thus } \int_{1}^{\sqrt{3}} \frac{\operatorname{Sin}^{-1} x}{\sqrt{1-x^{2}}} d x=\int_{\frac{1}{2}}^{\sqrt{3}}\left(\operatorname{Sin}^{-1} x\right) \cdot \frac{1}{\sqrt{1-x^{2}}} d x \\
& =\int_{\frac{1}{2}}^{\pi} t d t \Rightarrow\left(\because x=\operatorname{Sin} t \quad \operatorname{Sin}^{-1} x \quad t\right) \\
& =\left[\frac{t^{2}}{2}\right]_{\frac{1}{2}}^{\frac{1}{2}}=\frac{1}{2}\left[\left(\frac{\pi}{3}\right)^{2}-\left(\frac{\pi}{6}\right)^{2}\right]=\frac{1}{2}\left(\frac{\pi^{2}}{9}-\frac{\pi^{2}}{36}\right) \\
& =\frac{1}{2}\left(\frac{4 \pi^{2}-\pi^{2}}{36}\right)=\frac{3 \pi^{2}}{72}=\frac{\pi^{2}}{24}
\end{aligned}
$$

Example 7: $\quad$ Evaluate $\int_{0}^{\pi} x \cos x d x$
Solution: $\quad$ Applying the formula

$$
\begin{aligned}
\int f(x) \phi^{\prime}(x) d x & =f(x) \phi(x)-\int \phi(x) f^{\prime}(x) d x, \text { we have } \\
\int x \cos x d x & =x \sin x-\int(\sin x)(1) d x \\
& =x \sin x-\left[\left(-\cos x\right)+c_{x}\right] \\
& =x \sin x+\cos x+c \quad \text { where } c=-c_{x}
\end{aligned}
$$

Thus $\int_{0}^{\pi} x \cos x d x=[x \sin x+\cos x]_{x}^{2}$

$$
\begin{aligned}
& =\left(\frac{\pi}{6} \sin \frac{\pi}{6}+\cos \frac{\pi}{6}\right)-(0 \sin 0+\cos 0) \\
& =\frac{\pi}{6} \cdot \frac{1}{2}+\frac{\sqrt{3}}{2}-(0+1)=\frac{\pi}{12}+\frac{\sqrt{3}}{2}-1
\end{aligned}
$$

Example 8: $\quad$ Evaluate $\int x \operatorname{In} x d x$
Solution: $\quad$ Applying the formula

$$
\begin{aligned}
\int f(x) \phi^{\prime}(x) d x & =f(x) \phi(x)-\int \phi(x) f^{\prime}(x) d x, \text { we have } \\
\int(\ln x) x d x= & (\ln x) \cdot \frac{x^{2}}{2}-\int\left(\frac{x^{2}}{2}\right) \cdot \frac{1}{x} d x \\
= & \frac{1}{2} x^{2} \ln x-\frac{1}{2} \int x d x=\frac{1}{2} x^{2} \ln x \cdot \frac{1}{2}\left(\frac{x^{2}}{2}\right) \quad c
\end{aligned}
$$

Thus $\int_{1} x \operatorname{In} x d x=\left[\frac{1}{2} x^{2} \ln x-\frac{x^{2}}{4}\right]_{x}^{c}$

$$
\begin{aligned}
& =\left(\frac{1}{2} e^{2} \ln e-\frac{e}{4}\right)-\left(\frac{1}{2}(1)^{2} \ln 1-\frac{(1)^{2}}{4}\right) \\
& =\left(\frac{e^{2}}{2} \cdot 1-\frac{e^{2}}{4}\right)-\left(\frac{1}{2} \cdot 0-\frac{1}{4}\right) \quad(\because \operatorname{In} e=1 \text { and } \operatorname{In} 1=0) \\
& =\frac{e^{2}}{4}+\frac{1}{4}
\end{aligned}
$$

Example 9: If $\int_{0}^{\frac{1}{2}} f(x) d x=5, \int_{1}^{2} f(x)=3$ and $\int_{0}^{\frac{1}{2}} g(x) d x=4$, then
evaluate the following definite integrals:
(i) $\int_{1}^{2} f(x) d x$
(ii) $\int_{1}^{2}[2 f(x)+3 g(x)] d x$
(iii) $\int_{0}^{1} 3 f(x) d x-\int_{0}^{1} 2 g(x) d x$

Solution: (i) $\int_{a}^{1} f(x) d x=\int_{a}^{1} f(x) d x+\int_{1}^{1} f(x) d x=5+3=8$
(ii) $\int_{a}^{1}[2 f(x)+3 g(x)] d x=\int_{a}^{1} 2 f(x) d x+\int_{a}^{1} 3 g(x) d x$

$$
\begin{aligned}
= & 2 \int_{a}^{1} f(x) d x+3 \int_{a}^{1} g(x) d x \\
= & 2(5)+3(4)=10+12=22
\end{aligned}
$$

(iii) $\int_{a}^{1} 3 f(x) d x-\int_{a}^{1} 2 g(x) d x=3 \int_{a}^{1} f(x) d x-2 \int_{a}^{1} g(x) d x$

$$
=3 \times 5-2 \times 4=15-8=7
$$

## EXERCISE 3.6

## Evaluate the following definite integrals.

1. $\int_{a}^{1}\left(x^{2}+1\right) d x$
2. $\int_{a}^{1}\left(x^{2 / 3}+1\right) d x$
3. $\int_{a}^{1} \frac{1}{(2 x-1)^{2}} d x$
4. $\int_{a}^{2} \sqrt{3-x} d x$
5. $\int_{a}^{2} \sqrt{(2 t-1)} d t$
6. $\int_{a}^{2} x \sqrt{x^{2}-1} d x$
7. $\int_{a}^{3} \frac{x}{x^{2}+2} d x$
8. $\int_{a}^{3}\left(x-\frac{1}{x}\right)^{3} d x$
9. $\int_{a}^{3}\left(x+\frac{1}{x}\right) \sqrt{x^{2}+x+1} d x$
10. $\int_{a}^{3} \frac{d x}{x^{2}+9}$
11. $\int_{a}^{6} \cos t d t$
12. $\int_{a}^{3}\left(x+\frac{1}{x}\right)^{3}\left(1-\frac{1}{x^{2}}\right) d x$
13. $\int_{a}^{2} \ln x d x$
14. $\int_{a}^{3}\left(e^{\frac{x}{2}}-e^{\frac{1}{2}}\right) d x$
15. $\int_{a}^{6} \frac{\cos \theta+\sin \theta}{2 \cos ^{2} \theta} d \theta$
16. $\int_{a}^{6} \cos ^{3} \theta d \theta$
17. $\int_{a}^{6} \cos ^{2} \theta \cot ^{2} \theta d \theta$
18. $\int_{a}^{6} \cos ^{4} t d t$
version: 1.1
19. $\int_{a}^{6} \cos ^{2} \theta \sin \theta d \theta$
20. $\int_{a}^{6}\left(1+\cos ^{2} \theta\right) \tan ^{2} \theta d \theta$
21. $\int_{a}^{6} \frac{\sec \theta}{\sin \theta+\cos \theta} d \theta$
22. $\int_{a}^{1}|x-3| d x$
23. $\int_{1}^{1} \frac{\left(\frac{1}{x^{2}}+2\right)^{3}}{x^{3}} d x$
24. $\int_{a}^{1} \frac{x^{2}-2}{x+1} d x$
25. $\int_{a}^{1} \frac{3 x^{2}-2 x+1}{(x-1)\left(x^{2}+1\right)} d x$
26. $\int_{a}^{6} \frac{\sin x-1}{\cos ^{2} x}$
27. $\int_{a}^{6} \frac{1}{1+\sin x} d x$
28. $\int_{a}^{6} \frac{3 x}{\sqrt{4-3 x}} d x$
29. $\int_{a}^{6} \frac{\cos x}{\sin x(2+\sin x)} d x$
30. $\int_{a}^{6} \frac{\sin x}{(1+\cos x)(2+\cos x)} d x$