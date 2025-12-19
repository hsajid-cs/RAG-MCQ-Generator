### 2.2 FINDING $\mathbf{f}^{\prime}(\mathbf{x})$ FROM DEFINITION OF DERIVATIVE

Given a function $f, f^{\prime}(x)$ if it exists, can be found by the following four steps Step I Find $f(x+\delta x)$ Step II Simplify $f(x+\delta x)-f(x)$ Step III Divide $f(x+\delta x)-f(x)$ by $\delta x$ to get $\frac{f(x+\delta x)-f(x)}{\delta x}$ and simplify it Step IV Find $\lim _{x \rightarrow \infty} \frac{f(x+\delta x)-f(x)}{\delta x}$ The method of finding derivatives by this process is called differentiation by definition or by ab-initio or from first principle.

Example 1: Find the derivative of the following functions by definition (a) $f(x)=\infty$ (b) $f(x) \quad x^{2}$

Solution: (a) For $f(x)=c$ (i) $f(x+\delta x)=c$ (ii) $f(x+\delta x)-f(x)=c-c=0$ (iii) $\frac{f(x+\delta x)-f(x)}{\delta x}=\frac{0}{\delta x}=0$ (iv) $\lim _{x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}=\lim _{x \rightarrow 0}(0)=0$

Thus $\quad f^{\prime}(x)=0$, that is, $\frac{d}{d x}(c)=0$ (b) For $f(x)=x^{2}$ (i) $f(x+\delta x)=(x+\delta x)^{2}$ (ii) $f(x+\delta x)-f(x)=(x+\delta x)^{2}-x^{2}=x^{2}+2 x \delta x+(\delta x)^{2}-x^{2}$ ${ }^{\infty} 2 x \delta x+(\delta x)^{2}=(2 x+\delta x) \delta x$ version: 1.1

(ii) $\frac{f(x+\delta x)-f(x)}{\delta x}=\frac{(2 x+\delta x) \delta x}{\delta x}=\mathbf{2} x \quad \delta x, \quad\left(\begin{array}{ll}\delta \mathrm{x} & 0\end{array}\right)$
(iv) $\lim _{x \rightarrow a} \frac{f(x+\delta x)-f(x)}{\delta x}=\lim _{x \rightarrow a}(2 x+\delta x)=2 x$
i.e.,

$$
f^{\prime}(x)=2 x
$$

Example 2: Find the derivative of $\sqrt{x}$ at $x=a$ from first principle.

Solution: If $\quad f(x)=\sqrt{x}$, then
(i) $\quad f(x+\delta x)=\sqrt{x+\delta x}$ and
(ii) $f(x+\delta x)-f(x)=\sqrt{x+\delta x}-\sqrt{x}$

$$
\begin{aligned}
& =\frac{(\sqrt{x+\delta x}-\sqrt{x})(\sqrt{x+\delta x}+\sqrt{x})}{\sqrt{x+\delta x}+\sqrt{x}}(\begin{array}{c}
\text { rationalizing the } \\
\text { numerator }
\end{array}) \\
& =\frac{(x+\delta x)-x}{\sqrt{x+\delta x}+\sqrt{x}}
\end{aligned}
$$

i.e., $\quad f(x+\delta x)-f(x)=\frac{\delta x}{\sqrt{x+\delta x}+\sqrt{x}}$
(iii) Dividing both sides of(1)by $\delta x$, we have

$$
\frac{f(x+\delta x)-f(x)}{\delta x}=\frac{\delta x}{\delta x(\sqrt{x+\delta x}+\sqrt{x})} \cdot \frac{1}{\sqrt{x+\delta x}+\sqrt{x}}(\because \delta x \quad 0)
$$

(iv) Taking limit of both the sides as $\delta x \rightarrow 0$, we have

$$
\lim _{x \rightarrow a} \frac{f(x+\delta x)-f(x)}{\delta x}=\lim _{x \rightarrow a}\left(\frac{1}{\sqrt{x+\delta x}+\sqrt{x}}\right)
$$

i.e., $\quad f^{\prime}(x)=\frac{1}{\sqrt{x}+\sqrt{x}}=\frac{1}{2 \sqrt{x}} \quad(x>0)$
and $\quad f^{\prime}(a)=\frac{1}{2 \sqrt{a}}$
or
Putting $\quad x=a$ in $f(x)=\sqrt{x}$, gives $\quad f(a) \quad \sqrt{a}$
So $\quad f(x)-f(a)=\sqrt{x}-\sqrt{a}$
Using alternative form for the definition of a derivative, we have

$$
\begin{aligned}
& \frac{f(x)-f(a)}{x-a}=\frac{\sqrt{x}-\sqrt{a}}{x-a} \\
& =\frac{(\sqrt{x}-\sqrt{a})(\sqrt{x}+\sqrt{a})}{(x-a)(\sqrt{x}+\sqrt{a})} \text { (rationalizing the numerator) } \\
& =\frac{x-a}{(x-a)(\sqrt{x}+\sqrt{a})} \cdot \frac{1}{\sqrt{x}+\sqrt{a}} \quad(x \quad a)
\end{aligned}
$$

Taking limit of both the sides of (II)as $x \rightarrow a$, gives

$$
\lim _{x \rightarrow a} \frac{f(x)-f(a)}{x-a}=\lim _{x \rightarrow a} \frac{1}{\sqrt{x}+\sqrt{a}} \cdot \frac{1}{\sqrt{a}+\sqrt{a}}
$$

i.e.,

$$
f^{\prime}(a)=\frac{1}{2 \sqrt{a}}
$$

Example 3: If $y=\frac{1}{x^{2}}$, then find $\frac{d y}{d x}$ at $x=-1$ by ab-initio method.

Solution: Here $y=\frac{1}{x^{2}}$, so

$$
y+\delta y=\frac{1}{(x+\delta x)^{2}}
$$

Subtracting (i) from (ii), we get

$$
\begin{aligned}
\delta y & =\frac{1}{(x+\delta x)^{2}} \cdot \frac{1}{x^{2}}=\frac{x^{2}-(x+\delta x)^{2}}{x^{2}(x+\delta x)^{2}} \\
& =\frac{(x+(x+\delta x))(x-(x+\delta x))}{x^{2}(x+\delta x)^{2}}
\end{aligned}
$$

$$
=\frac{(2 x+\delta x)(-\delta x)}{x^{2}(x+\delta x)^{2}} \cdot \frac{-\delta x(2 x+\delta x)}{x^{2}(x+\delta x)^{2}}
$$

Dividing both sides of (iii) by $\delta x$, we have

$$
\frac{\delta y}{\delta x}=\frac{-\delta x(2 x+\delta x)}{x^{2}(x+\delta x)^{2} \delta x} \cdot \frac{-(2 x+\delta x)}{x^{2}(x+\delta x)^{2}} \quad(\delta x \quad 0)
$$

Taking limit as $\delta x \rightarrow 0$, gives

$$
\begin{aligned}
& \lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0} \frac{-(2 x+\delta x)}{x^{2}(x+\delta x)^{2}} \\
& =\frac{-(2 x)}{x^{2}\left(x^{2}\right)} \quad \quad \text { (Using quotient theorem of limits) } \\
& \text { i.e., } \quad \frac{d y}{d x}=\frac{-2}{x^{2}} \text { and } \quad \frac{d y}{d x} \mathrm{~b}_{x-1} \quad \frac{-2}{(-1)^{2}} \quad \frac{-2}{-1} \quad 2
\end{aligned}
$$

Note: The value of $\frac{d y}{d x}$ at $(x-1)$ is written as $\frac{d y}{d x} \frac{1}{x-1}$.

Example 4: Find the derivative of $x^{\frac{3}{2}}$ and also calculate the value of derivative at $x=8$.

Solution: Let $f(x)=x^{\frac{3}{2}}$. Then

$$
f(x+\delta x)=(x+\delta x)^{\frac{3}{2}}
$$

and

$$
f(x+\delta x)-f(x)=(x+\delta x)^{\frac{3}{2}}-x^{\frac{3}{2}}=\frac{\left((x+\delta x)^{\frac{3}{2}}-x^{\frac{3}{2}}\right)\left[(x+\delta x)^{\frac{3}{2}}+(x+\delta x)^{\frac{3}{2}} \cdot x^{\frac{3}{2}}+x^{\frac{3}{2}}\right]}{(x+\delta x)^{\frac{3}{2}}+(x+\delta x)^{\frac{3}{2}} \cdot x^{\frac{3}{2}}+x^{\frac{3}{2}}}
$$

version: 1.1

$$
=\frac{\left[(x+\delta x)^{\frac{3}{2}}\right]^{3}-\left(x^{\frac{3}{2}}\right)^{3}}{(x+\delta x)^{\frac{3}{2}}+(x+\delta x)^{\frac{3}{2}} \cdot x^{\frac{3}{2}}+x^{\frac{3}{2}}} \frac{(x+\delta x)^{2}-x^{2}}{(x+\delta x)^{\frac{3}{2}}+(x+\delta x)^{\frac{3}{2}} \cdot x^{\frac{3}{2}}+x^{\frac{3}{2}}}
$$

i.e., $\quad f(x+\delta x)-f(x)=\frac{\delta x(2 x+\delta x)}{(x+\delta x)^{\frac{3}{2}}+(x+\delta x)^{\frac{3}{2}} \cdot x^{\frac{3}{2}}+x^{\frac{3}{2}}}$
Dividing both the sides of (i) by $\delta x$, we get

$$
\frac{f(x+\delta x)-f(x)}{\delta x}=\frac{2 x+\delta x}{(x+\delta x)^{\frac{3}{2}}+(x+\delta x)^{\frac{3}{2}} \cdot x^{\frac{3}{2}}+x^{\frac{3}{2}}}
$$

Taking limit of both the sides as $\delta x \rightarrow 0$, we have

$$
f^{\prime}(x)=\frac{2 x}{x^{\frac{3}{2}}+x^{\frac{3}{2}} \cdot x^{\frac{3}{2}}+x^{\frac{3}{2}}} \frac{2 x}{3 x^{\frac{3}{2}}} \frac{2}{3 x^{\frac{1}{2}}}
$$

and

$$
f^{\prime}(8)=\frac{2}{3.8 \frac{1}{3}}=\frac{1}{3}
$$

Example 5: Find the derivative of $x^{3}+2 x+3$.
Solution: Let $y=x^{3}+2 x+3$. Then
(i) $y+\delta y=(x+\delta x)^{3}+2(x+\delta x)+3$
(ii) $\delta y=\left[(x+\delta x)^{3}+2(x+\delta x)+3\right]-\left[x^{3}+2 x+3\right]$

$$
\begin{aligned}
& =\left[(x+\delta x)^{3}-x^{3}\right]+2[(x+\delta x)-x]+(3-3) \\
& =[(x+\delta x)-x]\left[(x+\delta x)^{3}+(x+\delta x) x+x^{2}\right]+2 \delta x
\end{aligned}
$$

(iii) $\frac{\delta y}{\delta x}=\frac{\delta x\left[(x+\delta x)^{3}+(x+\delta x) x+x^{2}\right]+2 \delta x}{\delta x}$

$$
=(x+\delta x)^{2}+(x+\delta x) x+x^{2}+2
$$

(iv) $\lim _{x \rightarrow \infty} \frac{\delta y}{\delta x}=\lim _{x \rightarrow \infty}\left[(x+\delta x)^{2}+(x+\delta x) x+x^{2}+2\right]$

$$
\frac{d y}{d x}=(x)^{2}+(x) x+x^{2}+2
$$

i.e., $\frac{d}{d x}\left(x^{2}+2 x+3\right)=3 x^{2}+2$