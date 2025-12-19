### 2.3 THEOREMS ON DIFFERENTIATION

We have, so far proved the following two formulas:

1. $\frac{d y}{d x}(c)=0$ i.e.. the derivative of a constant function is zero.
2. $\frac{d}{d x}\left(x^{n}\right)=n x^{n-1}$ power formula (or rule) when $n$ is any rational number.
Now we will prove other important formulas (or rules) which are used to determine derivatives of different functions efficiently. Henceforth, in all subsequent discussion, $f, g, h$ etc. all denote functions differentiable at $x$, unless stated otherwise.
3. Derivative of $y=c f(x)$

Proof: Let $y=c f(x)$. Then
(i) $y+\delta y=c f(x+\delta x)$ and
(ii) $y+\delta y-y=c f(x+\delta x)-c f(x)$
or $\delta y=c \mid f(x+\delta x)-f(x) \quad$ (factoring out $c$ )
(iii) $\frac{\delta y}{\delta x}=c\left(\frac{f(x+\delta x)-f(x)}{\delta x}\right)$

Taking limit when $\delta x \rightarrow 0$
(iv) $\lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0}\left[c \frac{f(x+\delta x)-f(x)}{\delta x}\right] \quad c \lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}$

A constant factor can be taken out from a limit sign.
Thus $\frac{d y}{d x}=c f^{\prime}(x)$, that is, $[c f(x)]=c f^{\prime}(x)$
or $\frac{d y}{d x}=c f^{\prime}(x) \quad=\quad[c f(x)]=c f^{\prime}(x)$

Example 1: Calculate $\frac{d}{d x}\left(3 x^{\frac{1}{3}}\right)$
Solution: $\quad \frac{d}{d x}\left(3 x^{\frac{1}{3}}\right)=3 \frac{d}{d x}\left(x^{\frac{1}{3}}\right) \quad$ (Using Formula 3)

$$
=3 \mathrm{x} \frac{4}{3} x^{\frac{1}{3}}=4 x^{\frac{1}{3}} \quad \text { (Using power rule) }
$$

4. Derivative of a sum or a Difference of Functions:

If $f$ and $g$ are differentiable at $x$, then $f+g, f-g$ are also differentiable at $x$ and $[f(x)+g(x)]=f^{\prime}(x)+g^{\prime}(x)$, that is, $\frac{d}{d x}[f(x)+g(x)]=\frac{d}{d x}[f(x)]+\frac{d}{d x}[g(x)]$ Also $[f(x)-g(x)]=f^{\prime}(x)-g^{\prime}(x)$, that is, $\frac{d}{d x}[f(x)-g(x)]=\frac{d}{d x}[f(x)]-\frac{d}{d x}[g(x)]$
Proof: Let $\phi(x)=f(x)+g(x)$. Then
(i) $\phi(x+\delta x)=f(x+\delta x)+g(x+\delta x)$ and
(ii) $\phi(x+\delta x)-\phi(x)=f(x+\delta x)+g(x+\delta x)-[f(x)+g(x)]$
$=[f(x+\delta x)-f(x)]+[g(x+\delta x)-g(x)]$ (rearranging the terms)
(iii) $\frac{\phi(x+\delta x)-\phi(x)}{\delta x}=\frac{f(x+\delta x)-f(x)}{\delta x} \quad \frac{g(x+\delta x)-g(x)}{\delta x}$

Taking the limit when $\delta x \rightarrow 0$
(iv) $\lim _{\delta x \rightarrow 0} \frac{\phi(x+\delta x)-\phi(x)}{\delta x}=\lim _{\delta x \rightarrow 0}\left[\frac{f(x+\delta x)-f(x)}{\delta x} \frac{g(x+\delta x)-g(x)}{\delta x}\right]$
$=\lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x} \lim _{\delta x \rightarrow 0} \frac{g(x+\delta x)-g(x)}{\delta x}$
(The limit of a sum is the sum of the limits)

$$
\phi^{\prime} x=f^{\prime}(x)+g^{\prime}(x), \text { that is }[f(x)+g(x)] \equiv f^{\prime}(x)+g^{\prime}(x)
$$

or $\frac{d}{d x}[f(x)+g(x)]=\frac{d}{d x}[f(x)]+\frac{d}{d x}[g(x)]$
The proof for the second part is similar.

Note: Sum or difference formula can be extended to find derivative of more than two functions.

Example 1: Find the derivative of $y=\frac{3}{4} x^{4}+\frac{2}{3} x^{3}+\frac{1}{2} x^{2}+2 x+5$ w.r.t. $x$.

Solution: $y=\frac{3}{4} x^{4}+\frac{2}{3} x^{3}+\frac{1}{2} x^{2}+2 x+5$
Differentiating with respect to $x$, we have
$\frac{d y}{d x}\left[\frac{3}{4} x^{4}+\frac{2}{3} x^{3}+\frac{1}{2} x^{2}+2 x+5\right]=\frac{d}{d x}\left[\frac{3}{4} x^{4}\right]+\frac{d}{d x}\left[\frac{2}{3} x^{3}\right]+\frac{d}{d x}\left[\frac{1}{2} x^{2}\right]+\frac{d}{d x}(2 x)+\frac{d}{d x}(5)$
(Using formula 4)
$=\frac{3}{4} \frac{d}{d x}\left(x^{4}\right)+\frac{2}{3} \frac{d}{d x}\left(x^{3}\right)+\frac{1}{2} \frac{d}{d x}\left(x^{2}\right)+2 \frac{d}{d x}(x)+0 \quad$ (Using formula 3 and 1)
$=\frac{3}{4}\left(4 x^{4-1}\right)+\frac{2}{3}\left(3 x^{3-1}\right)+\frac{1}{2}\left(2 x^{3-1}\right)+2\left(1 . x^{2-1}\right) \quad$ (By power formula)
$=3 x^{3}+2 x^{2}+x+2$

Example 2: Find the derivative of $y=\left(x^{2}+5\right)\left(x^{3}+7\right)$ with respect to $x$.
Solution: $y=\left(x^{2}+5\right)\left(x^{3}+7\right) \quad=x^{2}+5 x^{3}+7 x^{2}+35$
Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left[x^{2}+5 x^{3}+7 x^{2}+35\right] \\
= & \frac{d}{d x}\left[x^{2}\right]+5 \frac{d}{d x}\left(x^{2}\right)+7 \frac{d}{d x}\left(x^{2}\right)+\frac{d}{d x}(35) \text { (Using formulas } 3 \text { and } 4 \text { ) } \\
= & 5 x^{3-1}+5 \times 3 x^{3-1}+7 \times 2 x^{2-1}+0 \\
= & 5 x^{4}+15 x^{2}+14 x
\end{aligned}
$$

Example 3: $\quad$ Find the derivative of $y=(2 \sqrt{x}+2)(x-\sqrt{x})$ with respect to $x$.

Solution: $y=(2 \sqrt{x}+2)(x-\sqrt{x})$

$$
\begin{aligned}
& =2(\sqrt{x}+1) \sqrt{x}(\sqrt{x}-1)=2 \sqrt{x}(\sqrt{x}+1)(\sqrt{x}-1) \\
& =2 \sqrt{x}(x+1)=2\left(x^{\frac{1}{2}}-x^{\frac{1}{2}}\right)
\end{aligned}
$$

Differentiating with respect to $x$, we have

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left[2\left(x^{\frac{1}{2}}-x^{\frac{1}{2}}\right)\right] \\
& =2\left[\frac{d}{d x}\left(x^{\frac{1}{2}}\right)-\frac{d}{d x}\left(x^{\frac{1}{2}}\right)\right]=2\left[\frac{3}{2} x^{\frac{1}{2}-1}-\frac{1}{2} x^{\frac{1}{2}-1}\right] \\
& =3 x^{\frac{1}{2}}-x^{\frac{1}{2}}=3 \sqrt{x}-\frac{1}{\sqrt{x}}=\frac{3 x-1}{\sqrt{x}}
\end{aligned}
$$

## 5. Derivative of a product. (The product Rule)

If $f$ and $g$ are differentiable at $x$, then $f g$ is also differentiable at $x$ and

$$
\begin{aligned}
& {[f(x) g(x)]=f^{\prime}(x) g(x)+f(x) g^{\prime}(x), \text { that is, } } \\
& \frac{d}{d x}[f(x) g(x)]=\left[\frac{d}{d x}[f(x)]\right] g(x) \quad f(x)\left[\frac{d}{d x}[g(x)]\right]
\end{aligned}
$$

Proof: Let

$$
\phi(x)=f(x) g(x) \text {. Then }
$$

(i) $\quad \phi(x+\delta x)=f(x+\delta x) g(x+\delta x)$
(ii) $\quad \phi(x+\delta x)-\phi(x)=f(x+\delta x) g(x+\delta x)-f(x) g(x)$

Subtracting and adding $f(x) g(x+\delta x)$ in step (ii), gives
$\phi(x+\delta x)-\phi(x)=f(x+\delta x) g(x+\delta x)-f(x) g(x+\delta x)+f(x) g(x+\delta x)-f(x) g(x)$

$$
=[f(x+\delta x)-f(x)] g(x+\delta x)+f(x)[g(x+\delta x)-g(x)]
$$

(iii) $\frac{\phi(x+\delta x)-\phi(x)}{\delta x}=\left[\frac{f(x+\delta x)-f(x)}{\delta x}\right] g(x \delta x) \quad f(x)\left[\frac{g(x+\delta x)-g(x)}{\delta x}\right]$

Taking limit when $\delta x \rightarrow 0$
(iv) $\lim _{\delta x \rightarrow 0} \frac{\phi(x+\delta x)-\phi(x)}{\delta x}$

$$
\begin{aligned}
& =\lim _{\delta x \rightarrow 0}\left[\frac{f(x+\delta x)-f(x)}{\delta x} g(x+\delta x)+f(x) \cdot \frac{g(x+\delta x)-g(x)}{\delta x}\right] \\
& =\lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x} \cdot \lim _{\delta x \rightarrow 0} g(x+\delta x)+\lim _{\delta x \rightarrow 0} f(x) \cdot \lim _{\delta x \rightarrow 0} \frac{g(x+\delta x)-g(x)}{\delta x}
\end{aligned}
$$

(Using limit theorems)
Thus $\phi^{\prime}(x)=f^{\prime}(x) g(x)+f(x) g^{\prime}(x) \quad\left[\because \lim _{\delta x \rightarrow 0} g(x+\delta x)=g(x)\right]$
or $\quad \frac{d}{d x}[f(x) \cdot g(x)]=\frac{d}{d x}[f(x)] \cdot g(x) \quad f(x)\left[\frac{d}{d x} g(x)\right]$
Example: Find derivative of $y=(2 \sqrt{x}+2)(x-\sqrt{x})$ with respect to $x$

Solution: $y=(2 \sqrt{x}+2)(x-\sqrt{x})$

$$
=2(\sqrt{x}+1)(x-\sqrt{x})
$$

Differentiating with respect to $x$, we get

$$
\begin{aligned}
\frac{d y}{d x} & =2 \frac{d}{d x}[(\sqrt{x}+1)(x-\sqrt{x})] \\
& =2\left[\left(\frac{d}{d x}(\sqrt{x}+1)\right)(x-\sqrt{x})+(\sqrt{x}+1) \frac{d}{d x}(x-\sqrt{x})\right] \\
& =2\left[\left(\frac{1}{2} x^{\frac{1}{2}-1}+0\right)(x-\sqrt{x})+(\sqrt{x}+1) \times\left(1-\frac{1}{2} x^{\frac{1}{2}-1}\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
& =2\left[\frac{1}{2 \sqrt{x}}(x-\sqrt{x})+(\sqrt{x}+1) \times\left(1-\frac{1}{2 \sqrt{x}}\right)\right] \\
& =2\left[\frac{x-\sqrt{x}}{2 \sqrt{x}}+(\sqrt{x}+1)\left(\frac{2 \sqrt{x}-1}{2 \sqrt{x}}\right)\right] \\
& =\frac{1}{\sqrt{x}}[x-\sqrt{x}+2 x-\sqrt{x}+2 \sqrt{x}-1] \\
& =\frac{3 x-1}{\sqrt{x}}
\end{aligned}
$$

## 6. Derivative of a Quotient (The Quotient Rule)

If $f$ and $g$ are differentiable at $x$ and $g(x) \neq 0$, for any $x \in D(g)$ then $\frac{f}{g}$ is differentiable at $x$ and $\left(\frac{f(x)}{g(x)}\right)=\frac{f^{\prime}(x) g(x)-f(x) g^{\prime}(x)}{[g(x)]^{2}}$
that is, $\frac{d}{d x}[\frac{f(x)}{g(x)}]=\frac{\left[\frac{d}{d x}[f(x)]\right] g(x)-f(x)\left[\frac{d}{d x}[g(x)]\right]}{[g(x)]^{2}}$
Proof: Let $\phi(x)=\frac{f(x)}{g(x)}$ Then
(i) $\phi(x+\delta x)=\frac{f(x+\delta x)}{g(x+\delta x)}$
(ii) $\phi(x+\delta x)-\phi(x)=\frac{f(x+\delta x)}{g(x+\delta x)} \cdot \frac{f(x)}{g(x)}=\frac{f(x+\delta x) g(x)-f(x) g(x+\delta x)}{g(x) g(x+\delta x)}$

Subtracting and adding $f(x) g(x)$ in the numerator of step (ii), gives

$$
\begin{aligned}
\phi(x+\delta x)-\phi(x) & =\frac{f(x+\delta x) g(x)-f(x) g(x)-f(x) g(x+\delta x)+f(x) g(x)}{g(x) g(x+\delta x)} \\
& =\frac{1}{g(x) g(x+\delta x)}[(f(x+\delta x)-f(x)) g(x)-f(x)(g(x+\delta x)-g(x))]
\end{aligned}
$$

(iii) $\frac{\phi(x+\delta x)-\phi(x)}{\delta x}=\frac{1}{g(x) g(x+\delta x)}\left[\frac{f(x+\delta x)-f(x)}{\delta x} g(x) \quad f(x) \cdot \frac{g(x+\delta x)-g(x)}{\delta x}\right]$

Taking limit when $\delta x \rightarrow 0$
(iv) $\lim _{\delta x \rightarrow 0} \frac{\phi(x+\delta x)-\phi(x)}{\delta x}$
$\lim _{\delta \rightarrow 0}\left[\frac{1}{g(x) g(x+\delta x)}\left(\frac{f(x+\delta x)-f(x)}{\delta x} \cdot g(x)-f(x) \cdot \frac{g(x+\delta x)-g(x)}{\delta x}\right)\right]$
Using limit theorems, we have
$\phi^{\prime}(x)=\frac{1}{g(x) \cdot g(x)}\left[f^{\prime}(x) g(x) \quad f(x) g^{\prime}(x)\right]=\left(\because \lim _{\delta x \rightarrow 0} g(x \quad \delta x) \quad g(x)\right)$
Thus $\left(\frac{f(x)}{g(x)}\right)=\frac{f^{\prime}(x) g(x)-f(x) g^{\prime}(x)}{[g(x)]^{2}}$ or $\frac{d}{d x}\left[\frac{f(x)}{g(x)}\right] \cdot\left[\frac{d}{d x}[f(x)]\right] g(x)-f(x)\left[\frac{d}{d x}[g(x)]\right]$
$[g(x)]^{2}$

## First Alternative Proof:

$$
\phi(x)=\frac{f(x)}{g(x)} \text { can be written as } f(x)=\phi(x) g(x)
$$

Using the procedure used to prove product rule, quotient rule can be proved.
Second Alternative Proof: We first prove the reciprocal rule and then use product rule to prove the quotient rule.

The reciprocal rule. If $g$ is differentiable at $x$ and $g(x) \neq 0$, then $\frac{1}{g}$ is differentiable at $x$ and $\frac{d}{d x}\left[\frac{1}{g(x)}\right]=\frac{\frac{d}{d x}[g(x)]}{[g(x)]^{2}}$ (Proof of reciprocal rule is left as an exercise)

Using the product rule to $f(x) \cdot \frac{1}{g(x)}$, we have

$$
\begin{aligned}
& \frac{d}{d x}\left[f(x) \cdot \frac{1}{g(x)}\right]=\left(\frac{d}{d x}[f(x)]\right) \cdot \frac{1}{g(x)} \quad f(x) \cdot \frac{d}{d x}\left[\frac{1}{g(x)}\right] \\
& =\frac{\frac{d}{d x}[f(x)]}{g(x)}+f(x) \cdot \frac{\frac{d}{d x}[g(x)]}{[g(x)]^{2}} \\
& \text { i.e., } \quad \frac{d}{d x}\left[\frac{f(x)}{g(x)}\right]=\frac{\left[\frac{d}{d x}[f(x)]\right] g(x)-f(x)\left[\frac{d}{d x}[g(x)]\right]}{[g(x)]^{2}}
\end{aligned}
$$

Example 2: $\quad$ Find $\frac{d y}{d x}$ if $y=\frac{\left(\sqrt{x}+1\right)\left(x^{\frac{3}{2}}-1\right)}{x^{\frac{1}{2}}-1}, \quad(x \neq 1)$
Solution: Given that

$$
\begin{aligned}
& y=\frac{\left(\sqrt{x}+1\right)\left(x^{\frac{3}{2}}-1\right)}{x^{\frac{1}{2}}-1} \quad \frac{\left(\sqrt{x}+1\right)\left[(\sqrt{x})^{2}-(1)^{2}\right]}{\sqrt{x}-1} \\
& =\frac{(\sqrt{x}+1)(\sqrt{x}-1)(x+1+\sqrt{x})}{\sqrt{x}-1}=(\sqrt{x}+1)(x+1+\sqrt{x}) \\
& =(\sqrt{x}+1)(\sqrt{x}-1)(x+1+\sqrt{x})=(\sqrt{x}+1)^{2}+(\sqrt{x}+1) x \\
& =x+1+2 \sqrt{x}+x \sqrt{x}+x=x^{\frac{3}{2}}+2 x+2 x^{\frac{1}{2}}+1 \\
& \frac{d y}{d x}=\frac{d}{d x}\left(x^{\frac{3}{2}}+2 x+2 x^{\frac{1}{2}}+1\right)=\frac{d}{d x}\left(x^{\frac{3}{2}}\right)+\frac{d}{d x}(2 x)+\frac{d}{d x}\left(2 x^{\frac{1}{2}}\right)+\frac{d}{d x}(1) \\
& =\frac{3}{2} x^{\frac{3}{2}}+2(1)+2 \frac{1}{2 \sqrt{x}}+0=\frac{3}{2} \sqrt{x}+2+\frac{1}{\sqrt{x}}
\end{aligned}
$$

Example 3: Differentiate $\frac{(\sqrt{x}+1)\left(x^{\frac{1}{x}}-1\right)}{x^{\frac{1}{x}}-x^{\frac{1}{x}}}$ with respect to $x$.

Solution: Let $y=\frac{(\sqrt{x}+1)\left(x^{\frac{1}{x}}-1\right)}{\sqrt{x}-x^{\frac{1}{x}}}$

$$
\begin{aligned}
& =\frac{(\sqrt{x}+1)\left(x^{\frac{1}{x}}-1\right)}{\sqrt{x}(x-1)} \\
& =\frac{(\sqrt{x}+1)(\sqrt{x}-1)(x+\sqrt{x}+1)}{\sqrt{x}(\sqrt{x}-1)} \quad \frac{(x-1)(x+\sqrt{x}+1)}{\sqrt{x}(\sqrt{x}-1)} \\
& =\frac{x+\sqrt{x}+1}{\sqrt{x}}
\end{aligned}
$$

Differentiating with respect to $x$, we have

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left[\frac{x+\sqrt{x}+1}{\sqrt{x}}\right] \\
& =\frac{\sqrt{x}}{d x} \frac{d}{(x+\sqrt{x}+1)-(x+\sqrt{x}+1)}=\frac{d}{d x}(\sqrt{x}) \\
& =\frac{\sqrt{x}\left(1+\frac{1}{2} x^{-\frac{1}{2}}+0\right)-(x+\sqrt{x}+1)\left(\frac{1}{2} x^{-\frac{1}{2}}\right)}{x} \\
& =\frac{\sqrt{x}\left(1+\frac{1}{2 \sqrt{x}}\right)-(x+\sqrt{x}+1)}{x}
\end{aligned}
$$

$$
=\frac{\sqrt{x}\left(\frac{2 \sqrt{x}+1}{2 \sqrt{x}}\right)-\frac{x+\sqrt{x}+1}{2 \sqrt{x}}}{x} \quad \frac{2 x+\sqrt{x}-x-\sqrt{x}-1}{x \cdot 2 \sqrt{x}} \quad \frac{x-1}{2 x^{\frac{1}{x}}}
$$

Example 4: Differentiate $\frac{2 x^{3}-3 x^{2}+5}{x^{2}+1}$ with respect to $x$.
Solution: Let $\phi(x)=\frac{2 x^{3}-3 x^{2}+5}{x^{2}+1}$. Then we take

$$
f(x)=2 x^{3}-3 x^{2}+5 \text { and } g(x)=x^{2}+1
$$

Now $\quad f^{\prime}(x)=\frac{d}{d x}\left[2 x^{3}-3 x^{2}+5\right]=2\left(3 x^{2}\right)-3(2 x)+0=6 x^{2}-6 x$
and

$$
g^{\prime}(x)=\frac{d}{d x}\left[x^{2}+1\right]=2 x+0=2 x
$$

Using the quotient formula: $\phi^{\prime}(x)=\frac{f^{\prime}(x) g(x)-f(x) g^{\prime}(x)}{[g(x)]^{3}}$, we obtain

$$
\begin{aligned}
\frac{d}{d x}\left[\frac{2 x^{3}-3 x^{2}+5}{x^{2}+1}\right] & =\frac{\left(6 x^{2}-6 x\right)\left(x^{2}+1\right)-\left(2 x^{3}+3 x^{2}+5\right)(2 x)}{\left(x^{2}+1\right)^{3}} \\
& =\frac{6 x^{4}-6 x^{3}+6 x^{2}-6 x-\left(4 x^{4}-6 x^{3}+10 x\right)}{\left(x^{2}+1\right)^{3}} \\
& =\frac{6 x^{4}-6 x^{3}+6 x^{2}-6 x-4 x^{4}+6 x^{3}-10 x}{\left(x^{2}+1\right)^{3}} \\
& =\frac{2 x^{4}+6 x^{2}-16 x}{\left(x^{2}+1\right)^{3}}
\end{aligned}
$$

## EXERCISE 2.3

Differentiate w.r.t. $x$

1. $x^{4}+2 x^{3}+x^{2}$
2. $x^{-3}+2 x^{-2 / 3}+3$
3. $\frac{a+x}{a-x}$

4. $\frac{2 x-3}{2 x+1}$
5. $(x-5)(3-x)$
6. $\left(\sqrt{x}-\frac{1}{\sqrt{x}}\right)^{2}$
7. $\frac{(1+\sqrt{x})\left(x-x^{2}\right)}{\sqrt{x}}$
8. $\frac{\left(x^{2}+1\right)^{2}}{x^{2}-1}$
9. $\frac{x^{2}+1}{x^{2}-3}$
9. $\frac{\sqrt{1+x}}{\sqrt{1-x}}$
10. $\frac{2 x-1}{\sqrt{x^{2}+1}}$
11. $\sqrt{\frac{a-x}{a+x}}$
12. $\frac{\sqrt{x^{2}+1}}{\sqrt{x^{2}-1}}$
13. $\frac{\sqrt{1+x}-\sqrt{1-x}}{\sqrt{1+x}+\sqrt{1-x}}$
14. $\frac{x \sqrt{a+x}}{\sqrt{a-x}}$
15. If $y=\sqrt{x}-\frac{1}{\sqrt{x}}$, show that $2 \frac{d y}{d x}+y=2 \sqrt{x}$
16. If $y=x^{4}+2 x^{2}+2$, prove that $\frac{d y}{d x}=4 x \sqrt{y-1}$