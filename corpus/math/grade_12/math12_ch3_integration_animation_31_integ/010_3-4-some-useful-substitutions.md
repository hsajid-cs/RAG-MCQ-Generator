### 3.4 SOME USEFUL SUBSTITUTIONS

We list below suitable substitutions for certain expressions to be integrated.

## Expression Involving

## Suitable Substitution

(i) $\sqrt{a^{2}-x^{2}}$
$x=a \sin \theta$
(ii) $\sqrt{x^{2}-a^{2}}$
$x=a \sec \theta$
(iii) $\sqrt{a^{2}+x^{2}}$
$x=a \tan \theta$
(iv) $\sqrt{x+a}($ or $\sqrt{x-a})$
$\sqrt{x+a}=t($ or $\sqrt{x-a}=t)$
(v) $\sqrt{2 a x-x^{2}}$
$x-a=a \sin \theta$
(vi) $\sqrt{2 a x+x^{2}}$
$x+a=a \sec \theta$

Example 1. Evaluate $\int \frac{1}{\sqrt{a^{2}+x^{2}}} d x \quad(a>\theta)$

Solution: $\quad$ Let $x=a \tan \theta$ for $-\frac{\pi}{2}<\theta<\frac{\pi}{2}$. Then

$$
d x=a \sec ^{2} \theta d \theta
$$

Thus

$$
\begin{aligned}
\int \frac{1}{\sqrt{a^{2}+x^{2}}} d x & =\int \frac{1}{\sqrt{a^{2}+a^{2}} \tan ^{2} \theta} \times a \sec ^{2} \theta d \theta=\int \frac{a \sec ^{2} \theta d \theta}{a \sqrt{1+\tan ^{2} \theta}} \\
& =\int \frac{a \sec ^{2} \theta d \theta}{a \sec \theta} \int \sec \theta d \theta \\
& =\int \frac{\sec \theta(\sec \theta+\tan \theta)}{\sec \theta+\tan \theta} d \theta \quad \ln (\sec -\theta \quad \tan \theta) \quad c_{1} \\
& =\ln \left(\frac{\sqrt{a^{2}+x^{2}}}{a} \frac{x}{a}\right) \quad v_{1}\left(\sqrt{\sec ^{2} \theta} \quad \llbracket \operatorname{man}^{2} \theta \quad \llbracket \frac{x^{2}}{a^{2}} \quad \frac{a^{2}+x^{2}}{a^{2}}\right. \text { i.e., } \\
& =\ln \left(\frac{\sqrt{a^{2}+x^{2}}+x}{a}\right) \quad c_{1} \quad \sec \theta \quad \frac{\sqrt{a^{2}+x^{2}}}{a} \text { as } \sec \theta \text { is } \\
& =\ln \left(x+\sqrt{a^{2}+x^{2}}\right)-\ln a+c_{1} \quad \text { positive-for }<\frac{\pi}{2}<\theta \quad \frac{\pi}{2}
\end{aligned}
$$

$$
=\ln \left(x+\sqrt{a^{2}+x^{2}}\right)+c \quad \text { where } c=c_{1}-\ln a
$$

Note: $x+\sqrt{a^{2}+x^{2}}$ is always positive for real values of $a$.
Example 2. Evaluate $\int \frac{d x}{\sqrt{2 x+x^{2}}}, \quad(x>0)$
Solution: $\quad \int \frac{d x}{\sqrt{2 x+x^{2}}}=\int \frac{d x}{\sqrt{(x+1)^{2}-1}}$
Let $\quad x+1=\sec \theta$. Then $\quad\left[0<\theta<\frac{\pi}{2}\right]$

$$
d x=\sec \theta \tan \theta d \theta
$$

Thus $\int \frac{d x}{\sqrt{(x+1)^{2}-1}}=\int \frac{\sec \theta \tan d \theta}{\sqrt{\sec ^{2} \theta-1}}=\int \frac{\sec \theta \tan d \theta}{\tan \theta}=\int \sec \theta d \theta$

$$
=\operatorname{ln}(\sec \theta+\tan \theta)+c=\ln \left(x+1+\sqrt{2 x \quad x^{2}}\right)+c_{1}
$$

## EXERCISE 3.3

## Evaluate the following integrals:

1. $\int \frac{-2 x}{\sqrt{4-x^{2}}} d x$
2. $\int \frac{d x}{x^{2}+4 x+13}$
3. $\int \frac{x^{2}}{4+x^{2}} d x$
4. $\int \frac{1}{x \ln x} d x$
5. $\int \frac{e^{x}}{e^{x}+3} d x$
6. $\int \frac{x+b}{(x+2 b x+c)^{\frac{1}{2}}} d x$
7. $\int \frac{\sec ^{2} x}{\sqrt{\tan x}} d x$
8. (a) Show that $\int \frac{d x}{x^{2}-a^{2}}=\ln \left(x+\sqrt{x^{2}-a^{2}}\right)+c$
(b) show that $\int \sqrt{a^{2}-x^{2}} d x=\frac{a}{-} \operatorname{Sin}^{-\frac{x}{a}}+\frac{x}{a} \sqrt{a^{2}-x^{2}}+c$

## Evaluate the following integrals:

9. $\int \frac{d x}{\left(1+x^{2}\right)^{\frac{1}{2}}}$
10. $\int \frac{1}{\left(1+x^{2}\right) \operatorname{Tan}^{-1} x} d x$
11. $\int \sqrt{\frac{1+x}{1-x}} d x$
12. $\int \frac{\sin \theta}{1+\cos ^{2} \theta} d \theta$
13. $\int \frac{a x}{\sqrt{a^{2}-x^{2}}}$
14. $\int \frac{d x}{\sqrt{7-6 x-x^{2}}}$
15. $\int \frac{\cos x}{\sin x \ln \sin x} d x$
16. $\int \cos x\left(\frac{\ln \sin x}{\sin x}\right) d x$
17. $\int \frac{x d x}{4+2 x+x^{2}}$
18. $\int \frac{x}{x^{2}+2 x^{2}+5} d x$
19. $\int\left[\cos \left(\sqrt{x}-\frac{x}{2}\right)\right] \times\left(\frac{1}{\sqrt{x}}-1\right) d x$
20. $\int \frac{x+2}{\sqrt{x}+3} d x$
21. $\int \frac{\sqrt{2}}{\sin x+\cos x} d x$
22. $\int \frac{d x}{\frac{1}{2} \sin x+\frac{\sqrt{3}}{2} \cos x}$