### 2.8 DERIVATIVES OF TRIGONOMETRIC FUNCTIONS

While finding derivatives of trigonometric functions, we assume that $x$ is measured in radians. The limit theorems $\lim _{x \rightarrow 0} \frac{\sin x}{x}=4$ and $\lim _{x \rightarrow 0} \frac{1-\cos x}{x} \quad 0$ are used to find the derivative formulas for $\sin x$ and $\cos x$.

We prove from first principle that

$$
\frac{d}{d x}(\sin x)=\cos x \text { and } \frac{d}{d x}(\cos x)=-\sin x
$$

Let $y=\sin x$ Then $y+\delta y=\sin (x+\delta x)$
and $\delta y=\sin (x+\delta x)-\sin x$

$$
\begin{aligned}
& =2 \cos \left(\frac{x+\delta x+x}{2}\right) \sin \left(\frac{x+\delta x-x}{2}\right)+2 \cos \left(x \frac{\delta x}{2}\right) \sin \left(\frac{\delta x}{2}\right) \\
& \frac{\delta y}{\delta x}=\frac{2 \cos \left(x+\frac{\delta x}{2}\right) \sin \left(\frac{\delta x}{2}\right)}{\frac{\delta x}{2}} \cdot \cos \left(x \frac{\delta x}{2}\right) \frac{\sin \left(\frac{\delta x}{2}\right)}{\frac{\delta x}{2}} \\
& \lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0}\left[\cos \left(x+\frac{\delta x}{2}\right) \frac{\sin \left(\frac{\delta x}{2}\right)}{\frac{\delta x}{2}}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\lim _{\frac{\delta x}{2} \rightarrow 0} \cos \left(x \frac{\delta x}{2}\right) \lim _{\frac{\delta x}{2} \rightarrow 0} \frac{\sin \left(\frac{\delta x}{2}\right)}{\frac{\delta x}{2}} \cdot\left(\frac{-\frac{\delta x}{2}}{\text { when } \delta x \rightarrow 0}\right) \\
& \text { Thus } \frac{d y}{d x}=\cos x \text { d. }\left(\frac{1-\lim _{\delta x \rightarrow 0} \cos \left(x \frac{\delta x}{2}\right)}{\frac{\delta x}{2}} \cos x \text { and } \lim _{\delta x \rightarrow 0} \frac{\sin \frac{\delta x}{2}}{\frac{\delta x}{2}} 1\right)
\end{aligned}
$$

Let $y=\cos x$, then $y+\delta y=\cos (x+\delta x)$
and $\delta y=\cos (x+\delta x)-\cos x$

$$
\begin{aligned}
& =\cos x \cos \delta x-\sin x \sin \delta x-\cos x \\
& =\sin x \sin \delta x \cos x\left(\frac{1-\cos \delta x}{\delta x}\right) \\
& \frac{\delta y}{\delta x}=(\sin x) \cdot \frac{\sin \delta x}{\delta x} \cos x\left(\frac{1-\cos \delta x}{\delta x}\right) \\
& \lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0}\left[(\sin x) \frac{\sin \delta x}{\delta x} \cos x\left(\frac{1-\cos \delta x}{\delta x}\right)\right] \\
& =\lim _{\delta x \rightarrow 0}\left[(-\sin x) \frac{\sin \delta x}{\delta x}\right]-\lim _{\delta x \rightarrow 0}\left[-\cos x\left(\frac{1-\cos \delta x}{\delta x}\right)\right]
\end{aligned}
$$

Thus $\frac{d y}{d x}=(\sin x) \cdot 1(\cos x)(0)$

$$
\left(\frac{1-\lim _{\delta x \rightarrow 0} \frac{\sin \delta y}{\delta x}=1 \text { and }}{\lim _{\delta x \rightarrow 0}\left(\frac{1-\cos \delta x}{\delta x}\right)=0\right)
$$

or $\frac{d}{d x}(\cos x)=-\sin x$
Now using $\frac{d}{d x}(\sin x)=\cos x$ and $\frac{d}{d x}(\cos x)=-\sin x$, we prove that

$$
\frac{d}{d x}(\sec x)=\sec x \tan x \quad \text { and } \quad \frac{d}{d x}(\cot x) \quad \operatorname{cosec}^{2} x
$$

$$
\begin{aligned}
& \text { Proof of } \frac{d}{d x}(s e c x)=s e c x \tan x \\
& \text { Let } \quad y=s e c x=\frac{1}{\cos x}
\end{aligned}
$$

Differentiating (i) w.r.t. ' $x$ ', we have

$$
\begin{aligned}
\frac{d}{d x}(y)= & \frac{d}{d x}\left[\frac{1}{\cos x}\right]=\frac{\left[\frac{d}{d x}(1)\right] \cos x-1 \cdot \frac{d}{d x}(\cos x)}{(\cos x)^{\prime}}\binom{\text { Using }}{\text { quotient }}(\text { formula }) \\
& =\frac{0 \cdot \cos x-1 \cdot(-\sin x)}{\cos ^{2} x} \\
& =\frac{1}{\cos x} \cdot \frac{\sin x}{\cos x} \quad \sec x \tan x
\end{aligned}
$$

Thus $\frac{d}{d x}(s e c x)=s e c x \tan x$
Proof of $\frac{d}{d x}(\cot x)=\cos e c^{2} x$
Let $\quad y=\cot x=\frac{\cos x}{\sin x}$
Differentiating (i) w.r.t. ' $x$ ', we get

$$
\begin{aligned}
\frac{d}{d x}(y)= & \frac{d}{d x}\left[\frac{\cos x}{\sin x}\right]=\frac{\left[\frac{d}{d x}(\cos x)\right] \sin x-\cos x \frac{d}{d x}(\sin x)}{(\sin x)^{\prime}}\binom{\text { Using }}{\text { quotient }}(\text { formula }) \\
& =\frac{(-\sin x) \sin x-\cos x(\cos x)}{\sin ^{2} x} \\
& =\frac{-\left(\sin ^{2} x+\cos ^{2} x\right)}{\sin ^{2} x}=\frac{1}{\sin ^{2} x} \quad \cos e c^{2} x
\end{aligned}
$$

Thus $\frac{d}{d x}(\cot x)=\cos e c^{2} x$

Now we write the derivatives of six trigonometric functions
(1) $\frac{d}{d x}(\sin x)=\cos x$
(2) $\frac{d}{d x}(\cos x)=\sin x$
(3) $\frac{d}{d x}(\tan x)=s e c^{2} x$
(4) $\frac{d}{d x}(\cot x)=-\cos e c^{2} x$
(5) $\frac{d}{d x}(\operatorname{cosec} x)=-\operatorname{cosec} x \cot x$
(6) $\frac{d}{d x}(\sec x)=\sec x \tan x$

Example 1: Find the derivative of $\tan x$ from first principle.
Solution: Let $y=\tan x$, then $+y \quad \delta x \quad \tan (x \quad \delta x)$ and

$$
\begin{aligned}
& \delta y=y+\delta x-y=\tan (x+\delta x)-\tan x \\
& =\frac{\sin (x+\delta x)}{\cos (x+\delta x)} \cdot \frac{\sin x}{\cos x}=\frac{\sin (x+\delta x) \cos x-\cos (x+\delta x) \sin x}{\cos (x+\delta x) \cos x} \\
& =\frac{\sin (x+\delta x-x)}{\cos (x+\delta x) \cdot \cos x} \cdot \frac{\sin \delta x}{\cos (x+\delta x) \cos x} \\
& \frac{\delta y}{\delta x}=\frac{1}{\cos (x+\delta x) \cdot \cos x} \cdot \frac{\sin \delta x}{\delta x} \\
& \text { or } \quad \lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0}\left(\frac{1}{\cos (x+\delta x) \cdot \cos x}\right) \lim _{\delta x \rightarrow 0}\left(\frac{\sin \delta x}{\delta x}\right) \\
& \text { Thus } \frac{d y}{d x}=\frac{1}{(\cos x)(\cos x)} \cdot 1 \quad \sec ^{2} x \quad\left(\because \lim _{\delta x \rightarrow 0} \cos (x+\delta x)=\cos x\right) \\
& \text { and } \lim _{\delta x \rightarrow 0} \frac{\sin \delta x}{\delta x}=1
\end{aligned}
$$

Thus $\frac{d y}{d x}=\sec ^{2} x$
or $\quad \frac{d}{d x}(\tan x)=\sec ^{2} x$

Example 2: Differentiate ab-initio w.r.t. ' $x$ '
(i) $\cos 2 x$
(ii) $\sin \sqrt{x}$
(iii) $\cot ^{2} x$

Solution: (i) Let $y=\cos 2 x$, then $y+\delta y=\cos 2(x+\delta x)$
and $\delta y=\cos (2 x+2 \delta x)-\cos 2 x$

$$
=2 \sin \frac{2 x+2 \delta x+2 x}{2} \sin \frac{2 x+2 \delta x-2 x}{2}=\geqslant \sin (2 x \quad \delta x) \sin \delta x
$$

Now $\frac{\delta y}{\delta x}=\geqslant \sin (2 x \quad \delta x) \cdot \frac{\sin \delta x}{\delta x}$
Thus $\frac{d y}{d x}=\lim _{\delta x \rightarrow 0}\left[\begin{array}{ll}2 \sin (2 x & \delta x) \cdot \frac{\sin \delta x}{\delta x}\end{array}\right]$

$$
=\geqslant \lim _{\delta x \rightarrow 0}(\sin 2 x \quad \delta x) \cdot \lim _{\delta x \rightarrow 0} \frac{\sin \delta x}{\delta x}
$$

$=(2 \sin 2 x) \cdot 1 \quad 2 \sin 2 x\left(\because \lim _{\delta x \rightarrow 0} \sin (2 x+\delta x)=\sin 2 x\right.$ and $\left.\lim _{\delta x \rightarrow 0} \frac{\sin \delta x}{\delta x} 1\right)$
(ii) Let $y=\sin \sqrt{x}$, then $y+\delta y=\sin \sqrt{x \quad \delta x}$
and $\delta y=\sin \sqrt{x+\delta x}-\sin \sqrt{x}$

$$
=2 \cos \left(\frac{\sqrt{x+\delta x}+\sqrt{x}}{2}\right) \sin \left(\frac{\sqrt{x+\delta x}-\sqrt{x}}{2}\right)
$$

As $(\sqrt{x+\delta x}+\sqrt{x})(\sqrt{x+\delta x}-\sqrt{x})=(x+\delta x)-x=\delta x$,
So $\frac{\delta y}{\delta x}=2 \cos \left(\frac{\sqrt{x+\delta x}+\sqrt{x}}{2}\right) \frac{\sin \left(\frac{\sqrt{x+\delta x}-\sqrt{x}}{2}\right)}{\delta x}$

$$
=\frac{2 \cos \left(\frac{\sqrt{x+\delta x}+\sqrt{x}}{2}\right) \sin \left(\frac{\sqrt{x+\delta x}-\sqrt{x}}{2}\right)}{(\sqrt{x+\delta x}+\sqrt{x})(\sqrt{x+\delta x}-\sqrt{x})}
$$

version: 1.1

$$
\frac{\cos \left(\frac{\sqrt{x+\delta x}+\sqrt{x}}{2}\right)}{\sqrt{x+\delta x}+\sqrt{x}} \frac{\sin \left(\frac{\sqrt{x+\delta x}-\sqrt{x}}{2}\right)}{\frac{\sqrt{x+\delta x}-\sqrt{x}}{2}}
$$

Thus $\frac{d y}{d x}=\lim _{\delta x \rightarrow 0}\left(\frac{\cos \frac{\sqrt{x+\delta x}+\sqrt{x}}{2}}{\sqrt{x+\delta x}+\sqrt{x}}\right) \frac{\lim _{\sqrt{x+\delta x}-\sqrt{x}}}{2} \quad 0\left(\frac{\sin \left(\frac{\sqrt{x+\delta x}-\sqrt{x}}{2}\right)}{\frac{\sqrt{x+\delta x}-\sqrt{x}}{2}}\right)$
$\frac{d y}{d x}=\left(\frac{\cos \frac{\sqrt{x}+\sqrt{x}}{2}}{\sqrt{x+\sqrt{x}}}\right) \cdot 1 \quad \frac{\cos \sqrt{x}}{2 \sqrt{x}} \quad\left(\because \frac{\sqrt{x+\delta x}-\sqrt{x}}{2} \rightarrow 0\right.$ when $)$
(iii) Let $y=\cot ^{2} x$, then

$$
\begin{aligned}
& y+\delta y=\cot ^{2}(x+\delta x) \\
& \delta y=\cot ^{2}(x+\delta x)-\cot ^{2} x=[\cot (x+\delta x)+\cot x] \times[\cot (x-\delta x) \cot x] \\
&=[\cot (x+\delta x)+\cot x]\left(\frac{\cos (x+\delta x)}{\sin (x+\delta x)} \frac{\cos x}{\sin x}\right) \\
&=[\cot (x+\delta x)+\cot x] \times \frac{\sin x \cos (x+\delta x)-\cos x \sin (x+\delta x)}{\sin (x+\delta x) \sin x} \\
& \frac{\delta y}{\delta x}=\left(\frac{\cot (x+\delta x)+\cot x}{\sin (x+\delta x) \sin x}\right) \frac{-\sin \delta x}{\delta x}\binom{\sin x \cos (x+\delta x)-\cos x \sin (x+\delta x)}{=\sin (x-(x+\delta x))=\sin (-\delta x)=-\sin \delta x} \\
& \lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0}\left(\frac{\cot (x+\delta x)+\cot x}{\sin (x+\delta x) \sin x} \cdot(1) \frac{\sin \delta x}{\delta x}\right) \\
& \text { Thus } \quad \frac{d y}{d x}=\frac{\cot x+\cot x}{\sin x \sin x} \cdot(1) \cdot 1 \quad\left(\frac{\because \lim _{\delta x \rightarrow 0} \cot (x+\delta x)=\cot x}{\text { and } \lim _{\delta x \rightarrow 0} \sin (x+\delta x)=\sin x}\right) \\
& =\frac{-2 \cot x}{\sin ^{2} x} \cdot 1=-2 \cot x \cos \sec ^{2} x
\end{aligned}
$$

Example 3: Differentiate $\sin ^{3} x$ w.r.t. $\cos ^{2} x$
Solution: Let $y=\sin ^{3} x$ and $u \cos ^{2} x$

$$
\begin{aligned}
& \text { Now } \quad \frac{d y}{d x}=3 \sin ^{4} x \cos x \quad \text { and } \quad \frac{d u}{d x}-2 \cos x(\sin x) \\
& \text { Thus } \frac{d y}{d u}=\frac{d y}{d x} \frac{d x}{d u}=\left(3 \sin ^{4} x \cos x\right) \cdot \frac{1}{-2 \cos x \sin x}\left(\because \frac{d x}{d u} \cdot \frac{1}{\frac{d x}{d u}}\right) \\
& =-\frac{3}{2} \sin x .
\end{aligned}
$$