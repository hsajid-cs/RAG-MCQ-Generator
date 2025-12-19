### 3.5 INTEGRATION BY PARTS

We know that for any two functions $f$ and $g$,

$$
\begin{aligned}
& \frac{d}{d x}[f(x) g(x)]=\not f(x) g(x) \quad f(x) g^{\prime}(x) \\
& \text { or } \quad f(x) g^{\prime}(x) \quad=\frac{d}{d x}[f(x) g(x)] \quad f^{\prime}(x) g(x)
\end{aligned}
$$

Integrating both the sides with respect to $x$, we get,

$$
\begin{aligned}
\int f(x) g^{\prime}(x) d x & =\int\left[\frac{d}{d x}(f(x) g(x)) \quad f^{\prime}(x) g(x)\right] d x \\
& =\int\left(\frac{d}{d x}[f(x) g(x)]\right) d x \quad \int f^{\prime}(x) g(x) d x
\end{aligned}
$$

$$
=f(x) g(x)+c-\int f^{\prime}(x) g(x) d x \quad \text { (By Definition) }
$$

i.e., $\int f(x) g^{\prime}(x)=f(x) g(x) \quad \int g(x) f^{\prime}(x) d x \quad c \quad$ (i)
or $\int f^{\prime}(x) g^{\prime}(x) d x=-f(x) g(x) \quad \int g(x) f^{\prime}(x) d x \quad$ (i)

A constant of integration is written, when $\int g(x) f^{\prime}(x) d x$ is evaluated. The equation (i) or (i)' is known as the formula for integration by parts.

$$
\begin{aligned}
& \text { If we put } u=f(x) \quad \text { and } \quad d v=g^{+}(x) d x \\
& \text { then } \quad d u=f^{\prime}(x) d x \quad \text { and } \quad v=g(x) .
\end{aligned}
$$

The equation (i) and (i)' can be written as

$$
\begin{aligned}
& \int u d v=w v \int v d u \quad c \quad \text { (ii) } \\
& \int u d v=u v-\int v d u \quad \text { (iii) }
\end{aligned}
$$

Example 1. Find $\int x \cos x d x$.
Solution: If $f(x)=x$ and $g^{+}(x)=\cos x$,
then $f^{\prime}(x)=1 \quad$ and $\quad g(x)=\sin x$
Thus $\int x \cos x d x=x \sin x-\int(\sin x)(1) d x$

$$
\begin{aligned}
& =x \sin x-(-\cos x)+c \\
& =-x \sin x+\cos x \quad c
\end{aligned}
$$

Example 2. Find $\int x e^{x} d x$
Solution: Let $u=x$ and $d v=e^{x} d x$,
then $d u=1 . d x$ and $v=e^{x}$
Applying the formula for integration by parts, we have

$$
\int x e^{x} d x=x e^{x} \int e^{x} \times 1 d x=x e^{x} \quad e^{x}+c
$$

## Example 3. Evaluate $\int x \tan ^{2} x d x$

Solution: $\int x \tan ^{2} x d x=\int x\left(\sec ^{2} x-1\right) d x \quad\left(\because 1+\tan ^{2} x=\sec ^{2} x\right)$

$$
=-\int x \sec ^{2} x d x \quad \int x d x
$$

Integrating the fist integral by parts on the right side of (I), we get

$$
\begin{aligned}
\int x \tan ^{2} x d x= & {\left[x \tan x-\int \tan x \cdot 1 d x\right]-\left(\frac{x^{2}}{2}+c_{1}\right) } \\
= & x \tan x-d x+\int \frac{1}{\cos x} \quad(\quad \sin x) d x=\left(\frac{x^{2}}{2}-c\right)-x \tan x+\ln |\cos x| \quad c_{1} \quad \frac{x^{2}}{2} \quad c_{1} \\
= & x \tan x+\ln |\cos x|-\frac{x^{2}}{2}+c, \quad \text { where } c=c_{2}-c_{1}
\end{aligned}
$$

Example 4. Evaluate $\int x^{6} \ln x d x$
Solution: $\int x^{6} \ln x d x=\int(\ln x) x^{6} d x$

$$
\begin{aligned}
& =(\ln x) \frac{x^{6}}{6}-\int \frac{x^{6}}{6} \frac{1}{x} d x=\frac{x^{6}}{6} \ln x-\frac{1}{6} \int x^{6} d x \\
& =\frac{x^{6}}{6} \ln x-\frac{1}{6}\left[\frac{x^{6}}{6}+c_{1}\right] \\
& =\frac{x^{6}}{6} \ln x \quad \frac{x^{6}}{36}+c \quad \text { where } c=\frac{c_{1}}{6}
\end{aligned}
$$

Example 5. Evaluate $\int \ln \left(x+\sqrt{x^{2}+1}\right) d x$

Solution: $\quad$ Let $f(x)=\ln \left(x+\sqrt{x^{2}+1}\right)$ and $g^{\prime}(x)=1$. Then

$$
\begin{aligned}
f^{\prime}(x) & =\frac{1}{x+\sqrt{x^{2}+1}}\left\{1 \quad \frac{1}{2}\left(x^{2} \quad 1\right)^{\frac{1}{2}-1}, 2 x\right) \\
& =-\frac{1}{x+\sqrt{x^{2}+1}} \cdot\left(1 \quad \frac{x}{\sqrt{x^{2}+1}}\right)
\end{aligned}
$$

$$
=\frac{1}{x+\sqrt{x^{2}+1}}-\left(\frac{\sqrt{x^{2}+1}+x}{\sqrt{x^{2}+1}}\right)=\frac{1}{\sqrt{x^{2}+1}} \text { and } g(x)=x
$$

Using the formula $\int f(x) g^{\prime}(x) d x=f(x) g(x)-\int g(x) f^{\prime}(x) d x$, we get

$$
\begin{aligned}
\int \ln \left(x+\sqrt{x^{2}+1}\right) \cdot 1 d x & =\left\{\ln \left(x+\sqrt{x^{2}+1}\right)\right\} \cdot x-\int x \cdot \frac{1}{\sqrt{x^{2}+1}} d x \\
& \int \ln \left(x+\sqrt{x^{2}+1}\right) x-\frac{1}{2} \int\left(x^{2}+1\right)^{\frac{1}{2}}(2 x) d x \\
& =x \ln \left(x+\sqrt{x^{2}+1}\right)-\frac{1}{2}\left[\frac{\left(x^{2}+1\right)^{\frac{1}{2}}}{\frac{1}{2}} \quad c_{1}\right] \\
& =x \ln \left(x+\sqrt{x^{2}+1}\right)-\sqrt{x^{2}+1}+c_{1}, \text { where } c=\frac{1}{2} c_{1}
\end{aligned}
$$

Example 6. Evaluate $\int x^{2} \cdot a e^{a x} d x$
Solution: If we put $f(x)=x^{2} \quad$ and $\quad g^{\prime}(x)=a e^{a x}$, then

$$
f^{\prime}(x)=2 x \quad \text { and } \quad g(x)=e^{a x}
$$

Using the formula $\int f(x) g^{\prime}(x) d x=f(x) g(x)-\int g(x) f^{\prime}(x) d x$, we get

$$
\begin{aligned}
\int x^{2} \cdot a x^{2} d x & =x^{2} e^{a x}-\int e^{a x} \cdot(2 x) d x \\
& =x^{2} e^{a x}-2 \int x e^{a x} d x
\end{aligned}
$$

But $\int x e^{a x} d x=x\left(\frac{e^{a x}}{a}\right)-\int\left(\frac{e^{a x}}{a}\right) \times 1 \cdot d x$

$$
=\frac{1}{a} x e^{a x}-\frac{1}{a} \int e^{a x} d x=\frac{1}{a} x e^{a x}-\frac{1}{a}\left(\frac{e^{a x}}{a}\right)+c_{1}
$$

Thus $\int x^{2} a e^{a x} d x=x^{2} e^{a x}-2\left[\frac{1}{a} \cdot x e^{a x}-\frac{1}{a^{2}} e^{a x}+c_{1}\right]$

$$
=x^{2} e^{a x}-\frac{2}{a} \cdot x e^{a x}+\frac{2}{a^{2}} e^{a x}+c_{1} \quad \text { where } c=2 c_{1}
$$

$$
\text { version: } 1.1
$$

Example 7. Find $\int e^{a x} \cos b x d x$.
Solution: $\quad$ Let $f(x)=e^{a x} \quad$ and $\quad g^{\prime}(x)=\cos b x$
then

$$
f^{\prime}(x)=a \cdot e^{a x} \quad \text { and } \quad g(x) \quad \frac{\sin b x}{b}
$$

Thus $\int e^{a x} \cos b x d x=e^{a x} \quad\left(\frac{\sin b x}{b}\right) \quad \int\left(\frac{\sin b x}{b}\right) \quad\left(a e^{a x}\right) d x$

$$
=\frac{1}{b} e^{a x} \sin b x \quad \frac{a}{b} \int e^{a x} \sin b x d x
$$

Integrating $\int e^{a x} \sin b x d x$, by parts, we get

$$
\begin{aligned}
\int e^{a x} \sin b x d x & =e^{a x} \times\left(-\frac{\cos b x}{b}\right)-\int\left(-\frac{\cos b x}{b}\right) \times\left(a e^{a x}\right) d x+c_{1} \\
& =\frac{1}{b} e^{a x} \cos b x \quad \frac{a}{b} \int e^{a x} \cos b x d x \quad c_{1}
\end{aligned}
$$

Putting the value of $\int e^{a x} \sin b x d x$ in (I), we get

$$
\begin{aligned}
& \int e^{a x} \cos b x d x=\frac{1}{b} e^{a x} \sin b x-\frac{a}{b}\left[-\frac{1}{b} e^{a x} \cos b x+\frac{a}{b} \int e^{a x} \cos b x d x \quad c_{1}\right] \\
& =\frac{1}{b} e^{a x} \sin b x+\frac{a}{b^{2}} e^{a x} \cos b x-\frac{a^{2}}{b^{2}} \int e^{a x} \cos b x d x-\frac{a}{b} \cdot c_{1} \\
& \text { or }\left(\frac{a^{2}}{b^{2}}\right) \int e^{a x} \cos b x d x=\frac{1}{b} e^{a x} \sin b x+\frac{a}{b^{2}} e^{a x} \cos b x-\frac{a}{b} \cdot c_{1} \\
& \text { i.e. } \int e^{a x} \cos b x d x=\frac{b^{2}}{a^{2}+b^{2}}\left[\frac{1}{b^{2}} e^{a x} \sin b x-\frac{a}{b^{2}} e^{a x} \cos b x\right] \quad \frac{b^{2}}{a^{2}+b^{2}} \quad \frac{a}{b} \cdot c_{1} \\
& =\frac{e^{a x}}{a^{2}+b^{2}}[b \sin b x+a \cos b x]+c, \quad \text { where } c=\frac{a b}{b\left(a^{2}+b^{2}\right)} c_{1}
\end{aligned}
$$

If we put $a=r \cos \theta \quad$ and $\quad b=r \sin \theta$;
then $a^{2}+b^{2}=r^{2} \Rightarrow r=\sqrt{a^{2}+b^{2}}$

$$
\frac{b}{a}=\frac{r \sin \theta}{r \cos \theta}=\tan \theta \Rightarrow \theta=\tan ^{-1} \frac{b}{a}
$$

and $a \cos b x+b \sin b x=r \cos \theta \cos b x+r \sin \theta \sin b x$

$$
\begin{aligned}
& =r[\cos b x \cos \theta+\sin b x \sin \theta]=r \cos (b x-\theta) \\
& \quad \Rightarrow \sqrt{a^{2} b^{2}} \cos \left(b x \quad \tan ^{-1} \frac{b}{a}\right),=\left(\theta \quad \tan ^{-1} \frac{b}{a}\right)
\end{aligned}
$$

The answer can be written as:

$$
\int e^{a x} \cos b x d x=\frac{1}{\sqrt{a^{2}-b^{2}}} e^{a x} \cos \left(b x-\tan ^{-1} \frac{b}{a}\right)+c
$$

Example 8. Evaluate $\int \sqrt{a^{2}+x^{2}} d x$
Solution: $\int \sqrt{a^{2}+x^{2}} \cdot 1 d x=\left(\sqrt{a^{2}+x^{2}}\right) x-\int x \cdot \frac{1}{2}\left(a^{2}+x^{2}\right)^{\frac{1}{2}} \cdot 2 x d x$

$$
\begin{aligned}
& =x \sqrt{a^{2}+x^{2}}-\int \frac{x^{2}}{\sqrt{a^{2}+x^{2}}} d x \\
& =x \sqrt{a^{2}+x^{2}}-\int \frac{a^{2}+x^{2}-a^{2}}{\sqrt{a^{2}+x^{2}}} d x \\
& =x \sqrt{a^{2}+x^{2}}-\int \sqrt{a^{2}+x^{2}} d x+\int \frac{a^{2}}{\sqrt{a^{2}+x^{2}}} d x \\
& 2 \int \sqrt{a^{2}+x^{2}} d x=x \sqrt{a^{2}+x^{2}}+a^{2} \cdot \int \frac{1}{\sqrt{a^{2}+x^{2}}} d x \\
& =x \sqrt{a^{2}+x^{2}}+\mathrm{a}^{2}\left[\ln \left(x+\sqrt{a^{2}+x^{2}}\right)+c_{1}\right]
\end{aligned}
$$

(See Example 1 Article 3.4)
$\int \sqrt{a^{2}+x^{2}} d x=\frac{x}{2} \sqrt{a^{2}+x^{2}}+\frac{a^{2}}{2} \ln \left(x+\sqrt{a^{2}+x^{2}}\right)+\mathrm{c}$, where $\mathrm{c}=\frac{a^{2} c_{1}}{2}$
Similarly integrals $\int \sqrt{a^{2}-x^{2}} d x$ and $\int \sqrt{x^{2}-a^{2}}$ can be evaluated.
Example 9. Evaluate $\int \sin ^{4} x d x$.
Solution: $\quad \int \sin ^{4} x d x=\int \sin ^{3} x \nu \sin ^{3} x d x \quad-\int \sin ^{3} x\left(1 \quad \cos ^{3} x\right) d x$

$$
\begin{aligned}
& =-\int \sin ^{3} x d x \quad \int \sin ^{3} x \cos ^{3} x d x \\
& =-\int \frac{1-\cos 2 x}{2} d x \quad \int \sin ^{3} x \cos ^{3} x d x \\
& \text { Integrating } \int \sin ^{3} x \cos ^{3} x d x \text { by parts, we have }
\end{aligned}
$$

$$
\begin{aligned}
& =-\cos x\left(\frac{\sin ^{3} x}{3}\right) \quad \int \frac{\sin ^{3} x}{3} \times(-\sin x) d x \quad[\because \text { If } f(x)=\cos x \text { and } \\
& g^{\prime}(x)=\sin ^{3} x \cos x . \\
& =\frac{1}{3} \cos x \sin ^{3} x \quad \frac{1}{3} \int \sin ^{4} x d x \quad \ldots . .(\mathrm{II})+\text { then } f^{\prime}(x)=\sin x \\
& \text { and } g(x)=\sin ^{3} \frac{\sin ^{3} x}{3}]
\end{aligned}
$$

Putting the value of $\int \sin ^{3} x \cos ^{3} x d x$ in (I), we obtain,

$$
\begin{aligned}
\int \sin ^{4} x d x & =-\int\left(\frac{1}{2} \quad \frac{\cos 2 x}{2}\right) d x \quad\left[\frac{1}{3} \cos x \sin ^{3} x \quad \frac{1}{3} \int \sin ^{4} x d x\right] \\
& =\frac{1}{2} \int 1 d x \quad \frac{1}{2} \int \cos 2 x d x \quad \frac{1}{3} \cos x \sin ^{3} x \quad \frac{1}{3} \int \sin ^{4} x d x \\
\text { or }\left(1+\frac{1}{3}\right) \int \sin ^{4} x d x & =\frac{1}{2} \times-\frac{1}{2}\left(\frac{\sin 2 x}{2}\right) \quad e_{1} \quad \frac{1}{3} \cos x \sin ^{3} x \\
\int \sin ^{4} x d x & =\frac{3}{4}\left[\frac{1}{2} \times-\frac{1}{4} \sin 2 x-\frac{1}{3} \cos x \sin ^{3} x \quad c\right] \\
& =\frac{5}{8} x \quad \frac{3}{16} \sin 2 x \quad \frac{1}{4} \cos x \sin ^{3} x \quad c \quad \text { where } c \quad \frac{3}{4} c_{1}
\end{aligned}
$$

Example 10. Evaluate $\int \frac{e^{x^{2}}(1+\sin x)}{1+\cos x} d x$.
Solution: $\quad \int \frac{e^{x^{2}}(1+\sin x)}{1+\cos x} d x=\int \frac{e^{x}\left(1+2 \sin \frac{x}{2} \cos \frac{x}{2}\right.}{2 \cos ^{2} \frac{x}{2}} d x\left[\because 1+\cos x=1+2 \cos ^{2} \frac{x}{2} \quad 1\right]$

i.e. $\int \frac{e^{x}(1+\sin x)}{1+\cos x} d x=+\int e^{x}\left(\frac{1}{2} \sec ^{2} \frac{x}{2} \quad \tan \frac{x}{2}\right) d x$

$$
=+\frac{1}{2} \int e^{x} \sec ^{2} \frac{x}{2} d x \quad \int e^{x} \tan \frac{x}{2} d x
$$

But $\int\left(\tan \frac{x}{2}\right) \cdot e^{x} d x=\left(\tan \frac{x}{2}\right) \cdot e^{x} \int e^{x}\left(\sec ^{2} \frac{x}{2}\right) \cdot \frac{1}{2} d x \quad c$, (Integrating by parts)
i.e. $\int e^{x} \tan \frac{x}{2} d x=e^{2} \tan \frac{x}{2} \quad \frac{1}{2} \int e^{x} \sec ^{2} \frac{x}{2} d x \quad c$
Putting the value of $\int e^{x} \tan \frac{x}{2} d x$ in (I), we get
$\int \frac{e^{x}(1+\sin x)}{1+\cos x} d x=\frac{1}{2} \int e^{x} \sec ^{2} \frac{x}{2} d x \quad\left[e^{x} \tan \frac{x}{2} \quad \frac{1}{2} \int e^{x} \sec ^{2} \frac{x}{2} d x=c\right] \quad e^{x} \tan \frac{x}{2} \quad c$
Example 11. Show that $\int e^{a x}\left[a f(x)+f^{\prime}(x)\right] d x=e^{a x} f(c)+c$.
Solution: $\int e^{a x}\left[a f(x)+f^{\prime}(x)\right] d x=\int e^{a x} \cdot a f(x) d x+\int e^{a x} \cdot f^{\prime}(x) d x \quad \ldots$ (i)
In the second integral, let $\varphi(x)=e^{a x}$ and $g^{\prime}(x)=f^{\prime}(x)$,
then

$$
\varphi^{\prime}(x)=\left(e^{a x}\right) \times a \text { and } g(x)=f(x)
$$

so

$$
\int e^{a x} \cdot f^{\prime}(x) d x=e^{a x} \times f(x)-\int f(x) \times\left(a e^{a x}\right) d x+c
$$

$$
=e^{a x} f(x) \quad \int a e^{a x} f(s i) d x \quad c
$$

thus $\int e^{a x}\left[a f(x)+f^{\prime}(x)\right] d x=\int a e^{a x} f(x) d x+\int e^{a x} f^{\prime}(x) d x+c$

$$
\begin{aligned}
& =\int a e^{a x} f(x) d x+\left[e^{a x} f(x)-\int a e^{a x} f(x) d x+c\right] \\
& =e^{a x} f(x)+c
\end{aligned}
$$

## EXERCISE 3.4

1. Evaluate the following integrals by parts add a word representing all the functions are defined.
(i) $\int x \sin x d x$
(ii) $\int \ln x d x$
(iii) $\int x \ln x d x$
(iv) $\int x^{2} \ln x d x$
(v) $\int x^{2} \ln x d x$
(vii) $\int \operatorname{Tan}^{-1} x d x$
(viii) $\int x^{2} \sin x d x$
(ix) $\int x^{2} \operatorname{Tan}^{-1} x d x$
(xi) $\int x^{3} \operatorname{Tan}^{-1} x d x$
(xiii) $\int \operatorname{Sin}^{-1} x d x$
(xiv) $\int x \operatorname{Sin}^{-1} x d x$
(xv) $\int e^{x} \sin x \cos x d x$
(xvi) $\int x \sin x \cos x d x$
(xvii) $\int x \cos ^{2} x d x$
(xviii) $\int x \sin ^{2} x d x$
(xix) $\int(\ln x)^{3} d x$
(xx) $\int(\ln (\tan x) \sec ^{3} x d x$
(xxi) $\int \frac{x \operatorname{Sin}^{-1} x}{\sqrt{1-x^{2}}} d x$
2. Evaluate the following integral.
(i) $\int \tan ^{4} x d x$
(ii) $\int \sec ^{4} x d x$
(iii) $\int e^{x} \sin 2 x \cos x d x$
(iv) $\int \tan ^{3} x \sec x d x$
(v) $\int x^{2} e^{3 x} d x$
(vi) $\int e^{-x} \sin 2 x d x$
(vii) $\int e^{2 x} \cos 3 x d x$
(viii) $\int \operatorname{cosec}^{3} x d x$
3. Show that $\int e^{a x} \sin b x d x=\frac{1}{\sqrt{a^{2}+b^{2}}} e^{a x} \sin \left(b x+\operatorname{Tan}^{2} \frac{b}{a}\right) \quad c$.
4. Evaluate the following indefinite integrals.
(i) $\int \sqrt{a^{2}-x^{2}} d x$
(ii) $\int \sqrt{x^{2}-\mathrm{a}^{2}} d x$
(iii) $\int \sqrt{4-5 x^{2}} d x$
(iv) $\int \sqrt{3-4 x^{2}} d x$
(v) $\int \sqrt{x^{2}+4} d x$
(vi) $\int x^{2} e^{a x} d x$

5. Evaluate the following integrals.
(i) $\int e^{x}\left(\frac{1}{x}+\ln x\right) d x$
(ii) $\int e^{x}(\cos x+\sin x) d x$
(iii) $\int e^{x x}\left[a \operatorname{Sec}^{-1} x+\frac{1}{x \sqrt{x^{2}-1}}\right] d x$
(iv) $\int e^{x x}\left[\frac{3 \sin x-\cos x}{\sin ^{2} x}\right] d x$
(v) $\int e^{x x}[-\sin x+2 \cos x] d x$
(vi) $\int \frac{x e^{x}}{(1+x)^{2}} d x$
(vii) $\int e^{-x}(\cos x-\sin x) d x$
(viii) $\int \frac{e^{a \cdot 2 \cdot a x^{2} x}}{\left(1+x^{2}\right)} d x$
(ix) $\int \frac{2 x}{1-\sin x} d x$
(x) $\int \frac{e^{x}(1+x)}{(2+x)^{2}} d x$
(xi) $\int\left(\frac{1-\sin x}{1-\cos x}\right) e^{x} d x$