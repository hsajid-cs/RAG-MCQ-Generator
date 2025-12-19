### 3.2.3 Anti-Derivatives of $[f(x)]^{\circ} f^{\prime}(x)$ and $[f(x)]^{-1} f^{\prime}(x)$

$$
\begin{aligned}
& \text { Prove that: (i) } \int[f(x)]^{\circ} f^{\prime}(x) d x=+\frac{[f(x)]^{n+1}}{n+1} \quad \text { c. } \quad(n \neq-1) \\
& \text { (ii) } \int[f(x)]^{-1} f^{\prime}(x) d x=\ln f(x)+c . \quad(f(x)>0)
\end{aligned}
$$

Proof:
(i) Since $\frac{d}{d x}\left([f(x)^{n+1}\right)=(n+1)[f(x)]^{\circ} f^{\prime}(x)$
$\therefore \quad$ by definition, $\int(n+1)[f(x)]^{\circ} f^{\prime}(x) d x=[f(x)]^{n+1}+c$,
$(n+1) \int[f(x)]^{\circ} f^{\prime}(x) d x=\frac{1}{2} f(x)]^{n+1} \quad c$, (by theorem I)
or $\int[f(x)]^{\circ} f^{\prime}(x) d x=\frac{[f(x)]^{n+1}}{n+1}+c \quad$ where $\quad c \quad \frac{c}{n+1}(n \quad 1)$

(ii) Since $\frac{d}{d x}\{\ln f(x)\}=\frac{1}{f(x)} \cdot f^{\prime}(x)$

By definition, we have
$\int \frac{1}{f(x)} \cdot f^{\prime}(x) d x=\ln f(x) \quad$ ( $\left.\neq(x) 0\right)$
or $\int[f(x)]^{-1} f^{\prime}(x) d x=\ln f(x)+c$.
Thus we can prove that
(i) $\int x^{n} d x=\frac{x^{n+1}}{n+1}+c, \quad(n \neq-1)$
(ii) $\int(a x+b)^{n} d x=\frac{(a x+b)^{n+1}}{a(n+1)}+c, \quad(a \neq 0, n \neq-1)$
(iii) $\int \frac{1}{x} d x=\ln |x|+c$
(iv) $\int \frac{1}{a x+b} d x=\frac{1}{c_{1}} \ln |a x+b|+c, \quad(a \neq 0)$

Examples: Evaluate
(i) $\int(x+1)(x-3) d x$
(ii) $\int x \sqrt{x^{2}-1} d x$
(iii) $\int \frac{x}{x+2} d x, \quad(x>-2)$
(iv) $\int \frac{1}{\sqrt{x}(\sqrt{x+1})} d x, \quad(x>0)$
(v) $\int \frac{d x}{\sqrt{x+1}-\sqrt{x}}, \quad(x>0)$
(vi) $\int \frac{\sin x+\cos ^{2} x}{\cos ^{2} x \sin x} d x$
(vii) $\int \frac{3-\cos 2 x}{1+\cos 2 x} d x, \quad(\cos 2 x \neq-1)$

# Solution:

(i) $\int(x+1)(x-3) d x=\int\left(x^{2}-2 x-3\right) d x$

$$
\begin{aligned}
& =\int x^{2} d x-2 \int x d x-3 \int 1 d x \quad \text { (By theorems I and II) } \\
& =\frac{x^{3}}{3}-2 \cdot \frac{x^{2}}{2}-3 \cdot x+c \quad \cup \int x^{n} d x=\frac{x^{n+1}}{n+1}+c_{1} \text { and }
\end{aligned}
$$

$$
=\frac{1}{3} x^{2}-x^{2}-3 x+c \quad \int 1 d x=x^{0}=d x \quad \frac{x^{n+1}}{1} \quad c_{2}
$$

(ii) $\int x \sqrt{x^{2}-1} d x=\int\left(x^{2}-1\right)^{\frac{1}{2}} x d x$

$$
\begin{aligned}
& =\int[f(x)] \frac{1}{2} f^{\prime}(x) d x \quad \text { (If } f(x)=x^{2}-1 \\
& =\frac{1}{2} \int[f(x)]^{\frac{1}{2}} f^{\prime}(x) \quad \text { then } f^{\prime}(x)+2 x \Rightarrow x=\frac{1}{2} f^{\prime}(x)) \\
& =\frac{1}{2} \frac{[f(x)]^{\frac{1}{2}}}{2}+c=\frac{1}{3}\left(x^{2}+1\right)^{\frac{1}{2}}+c
\end{aligned}
$$

(iii) $\int \frac{x}{x+2} d x=\int \frac{x+2-2}{x+2} d x, \quad(x>-2)$

$$
=\int\left(1-\frac{2}{x+2}\right) d x=\int d x-2 \int(x+2)^{-1} \cdot 1 d x=x-2 \ln (x+2)+c
$$

(iv) $\int \frac{1}{\sqrt{x}(\sqrt{x}+1)} d x=\frac{1}{\sqrt{x}+1} \frac{1}{\sqrt{x}} d x \quad(x \quad 0)$

$$
\begin{aligned}
& =\int[f(x)]^{-1} \cdot 2 f^{\prime}(x) d x \quad \cup f^{\prime}(x) \quad \frac{1}{2 \sqrt{x}} \quad \text { if } f(x) \quad \sqrt{x} \quad 1 \\
& =-2 \int[f(x)]^{-1} f^{\prime}(x) d x \quad \text { or } \frac{1}{\sqrt{x}} \quad 2 f^{\prime}(x) \\
& =2 \ln f(x)+c=2 \ln (\sqrt{x}+1)+c
\end{aligned}
$$

(v) $\int \frac{d x}{\sqrt{x+1}-\sqrt{x}}, \quad(x>0)$

Rationalizing the denominator, we have

$$
\int \frac{d x}{\sqrt{x+1}-\sqrt{x}}=\int \frac{\sqrt{x+1}+\sqrt{x}}{(\sqrt{x+1}-\sqrt{x})(\sqrt{x+1}+\sqrt{x})} d x
$$

$$
\begin{aligned}
& =\int \frac{\sqrt{x+1}+\sqrt{x}}{x+1-x} d x=\int\left[(\# \quad 1)^{\frac{1}{2}} \quad x^{\frac{1}{2}}\right] d x \\
& =\int(x \quad 1)^{\frac{1}{2}} d x \quad \int x^{\frac{1}{2}} d x \\
& =\frac{(x+1)^{\frac{1}{2}}}{2}+\frac{x^{\frac{1}{2}}}{2}+c=\frac{2}{3}(x+1)^{\frac{1}{2}}+\frac{2}{3} x^{\frac{1}{2}}+c
\end{aligned}
$$

(vi) $\int \frac{\sin x+\cos ^{2} x}{\cos ^{2} x \sin x} d x$

Solution: $\int \frac{\sin x+\cos ^{2} x}{\cos ^{2} x \sin x} d x=+\int\left(\frac{\sin x}{\cos ^{2} x \sin x} \quad \frac{\cos ^{2} x}{\cos ^{2} x \sin x}\right) d x$

$$
\begin{aligned}
& =\int\left(\frac{1}{\cos ^{2} x}+\frac{\cos x}{\sin x}\right) d x \\
& =\int \sec ^{2} x d x+\int \cot x d x \\
& =\tan x \quad \ln |\sin | \quad c
\end{aligned}
$$

(vii) $\int \frac{3-\cos 2 x}{1+\cos 2 x} d x, \quad(\cos 2 x \neq-1)$

Solution: $\int \frac{3-\cos 2 x}{1+\cos 2 x}=\int \frac{4-\left(1+\cos 2 x\right)}{1+\cos 2 x} d x \quad \int\left(\frac{4}{1+\cos 2 x} \quad 1\right) d x$

$$
\begin{aligned}
& =\int \frac{4}{2 \cos ^{2} x} d x-\int 1 d x=\int 2 \sec ^{2} x d x-\int 1 d x \\
& =2 \tan x-x+c
\end{aligned}
$$

## EXERCISE 3.2

## 1. Evaluate the following indefinite integrals

(i) $\int\left(3 x^{2}-2 x+1\right) d x$
(ii) $\int\left(\sqrt{x}+\frac{1}{\sqrt{x}}\right) d x, \quad(x>0)$
(iii) $\int x(\sqrt{x}+1) d x, \quad(x>0)$
(iv) $\int(2 x+3)^{\frac{1}{2}} d x$
(v) $\int(\sqrt{x}+1)^{3} d x, \quad(x>0)$
(vi) $\int\left(\sqrt{x}-\frac{1}{\sqrt{x}}\right)^{3} \mathrm{dx}, \quad(x>0)$
(vii) $\int \frac{3 x+2}{\sqrt{x}} d x, \quad(x>0)$
(viii) $\int \frac{\sqrt{y}(y+1)}{y} d y,(y>0)$
(ix) $\int \frac{(\sqrt{\theta}-1)^{3}}{\sqrt{\theta}} d \theta,(\theta>0)$
(x) $\int \frac{(1-\sqrt{x})^{3}}{\sqrt{x}} d x, \quad(x>0)$
(xi) $\int \frac{e^{2 x}+e^{x}}{e^{x}} d x$

## 2. Evaluate

(i) $\int \frac{d x}{\sqrt{x+a}+\sqrt{x+b}}\left(\frac{x+a>0}{x+b>0}\right)$
(ii) $\int \frac{1-x^{2}}{1+x^{2}} d x$
(iii) $\int \frac{d x}{\sqrt{x+a}+\sqrt{x}},(x>0, a>0)$
(iv) $\int(a-2 x)^{\frac{1}{2}} d x$
(v) $\int \frac{\left(1+e^{x}\right)^{3}}{e^{x}} d x$
(vi) $\int \sin (a+b) x d x$
(vii) $\int \sqrt{1-\cos 2 x} d x,(1-\cos 2 x>0)$
(viii) $\int(\ln x) \times \frac{1}{x} d x,(x>0)$
(ix) $\int \sin ^{2} x d x$
(x) $\int \frac{1}{1+\cos x} d x,\left(-\frac{\pi}{2}<x<\frac{\pi}{2}\right)$
(xi) $\int \frac{a x+b}{a x^{2}+2 b x+c} d x$
(xii) $\int \frac{\cos 2 x-1}{1+\cos 2 x} d x,(1+\cos 2 x \neq 0)$
(xiv) $\int \tan ^{2} x d x$