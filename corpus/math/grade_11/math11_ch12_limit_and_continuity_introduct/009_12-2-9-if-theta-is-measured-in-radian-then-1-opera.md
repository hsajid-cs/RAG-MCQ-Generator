### 12.2.9 If $\theta$ is measured in radian, then $1 \operatorname{lin} \sin \theta=1$.

Proof: To evaluate this limit, we apply a new technique. Take $\theta$ be positive acute central angle of a sector of a circle with radius $r=1$. As shown in the figure, $O A B$ represents a sector of a circle. Join $A$ and $B$ and extend $O B$ to $D$ such that $O A \perp \overline{A D}$. Also draw $\overline{B C} \perp \overline{O C}$ on $\overline{O A}$.
Given $|O A|=|O B|=1 \quad$ (radii of unit circle)
In the right $\triangle O C B, \sin \theta=\frac{|\overline{B C}|}{\mid \overline{O B}} \mid=|\overline{B C}|$
In the right $\triangle O A D, \tan \theta=\frac{|\overline{A D}|}{|\overline{O A}|}=|\overline{A D}|$
(i) Area of $\triangle O A B=\frac{1}{2}|\overline{O A}||\overline{B C}|=\frac{1}{2}(1)(\sin \theta)=\frac{1}{2} \sin \theta$
(ii) Area of sector $O A B=\frac{1}{2} r^{2} \theta=\frac{1}{2}(1)(\theta)=\frac{1}{2} \theta \quad$ and
(iii) Area of $\triangle O A D=\frac{1}{2}|\overline{O A}||\overline{A D}|=\frac{1}{2}(1)(\tan \theta)=\frac{1}{2} \tan \theta$

From the figure we see that
Area of $\triangle O A B<$ Area of sector $O A B<$ Area of $\triangle O A D$
Figure 12.4
$\Rightarrow \quad \frac{1}{2} \sin \theta<\frac{\theta}{2}<\frac{1}{2} \tan \theta$

As $\sin \theta$ is positive, so on division by $\frac{1}{2} \sin \theta$, we get

$$
1<\frac{\theta}{\sin \theta}<\frac{1}{\cos \theta} \quad\left(0<\theta<\frac{\pi}{2}\right)
$$

i.e., $\quad 1>\frac{\sin \theta}{\theta}>\cos \theta \quad$ or $\quad \cos \theta<\frac{\sin \theta}{\theta}<1$
when $\theta \rightarrow 0, \cos \theta \rightarrow 1$
Since $\frac{\sin \theta}{\theta}$ is sandwiched between 1 and a quantity approaching 1 itself. So, by the sandwich theorem, it must also approach 1 that is, $\operatorname{Lim}_{\theta \rightarrow 0} \frac{\sin \theta}{\theta}=1$

# Example 7 Evaluate $\operatorname{Lim}_{\theta \rightarrow 0} \frac{\sin 7 \theta}{\theta}$

Solution
Let $x=7 \theta$, so that $\theta=\frac{x}{7}$
when $\theta \rightarrow 0$ we have $x \rightarrow 0$

$$
\therefore \quad \lim _{x \rightarrow 0} \frac{\sin 7 \theta}{\theta}=\operatorname{Lim}_{x \rightarrow 0} \frac{\sin x}{\frac{x}{7}}=7 \operatorname{Lim}_{x \rightarrow 0} \frac{\sin x}{x}=(7)(1)=7
$$

Example 8 Evaluate $\operatorname{Lim}_{\theta \rightarrow 0} \frac{1-\cos \theta}{\theta}$
Solution $\frac{1-\cos \theta}{\theta}=\frac{1-\cos \theta}{\theta} \cdot \frac{1+\cos \theta}{1+\cos \theta}=\frac{1-\cos ^{2} \theta}{\theta(1+\cos \theta)}$

$$
=\frac{\sin ^{2} \theta}{\theta(1+\cos \theta)}=\sin \theta\left(\frac{\sin \theta}{\theta}\right)\left(\frac{1}{1+\cos \theta}\right)
$$

$\operatorname{Lim}_{\theta \rightarrow 0}\left(\frac{1-\cos \theta}{0}\right)=\operatorname{Lim}_{\theta \rightarrow 0} \sin \theta \cdot \operatorname{Lim}_{\theta \rightarrow 0} \frac{\sin \theta}{\theta} \cdot \operatorname{Lim}_{\theta \rightarrow 0}\left(\frac{1}{1+\cos \theta}\right)=(0)(1)\left(\frac{1}{1+1}\right)=0$

## EXERCISE 12.1

1. Find the limit of the following sequences if exists:
(i) $a_{n}=\frac{2 n+3}{n+1}$
(ii) $b_{n}=\frac{2 n+3}{n^{2}+1}$
(iii) $c_{n}=\frac{5 n^{2}}{2 n+3}$
(iv) $d_{n}=\frac{n^{2}-3 n+1}{2 n^{2}+n+4}$

2. Evaluate each limit by using theorems of limits:
(i) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 3}(2 x+4)$
(ii) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 1}\left(3 x^{2}-2 x+4\right)$
(iii) $\underline{\operatorname{Lim}}_{x \rightarrow 3} \sqrt{x^{2}+x+4}$
(iv) $\underline{\operatorname{Lim}}_{x \rightarrow 2} \sqrt{x^{2}+4}$
(v) $\underline{\operatorname{Lim}}_{x \rightarrow 2}\left(\sqrt{x^{2}+1}-\sqrt{x^{2}+5}\right)$
(vi) $\underline{\operatorname{Lim}}_{x \rightarrow-2} \frac{2 x^{3}+5 x}{3 x-2}$
3. Evaluate each limit by using algebraic techniques:
(i) $\quad \underline{\operatorname{Lim}}_{x \rightarrow-1} \frac{x^{3}-x}{x+1}$
(ii) $\underline{\operatorname{Lim}}_{x \rightarrow 3}\left(\frac{x^{2}-5 x+6}{x^{2}-2 x-3}\right)$
(iii) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 2}\left(\frac{x^{3}-8}{x^{2}-5 x+6}\right)$
(iv) $\underline{\operatorname{Lim}}_{x \rightarrow 1} \frac{x^{2}-3 x^{2}+3 x-1}{x^{2}-x}$
(v) $\underline{\operatorname{Lim}}_{x \rightarrow 2}\left(\frac{x^{3}-6 x^{2}+12 x-8}{x^{3}-4 x}\right)$
(vi) $\underline{\operatorname{Lim}}_{x \rightarrow 1}\left(\frac{x^{4}-1}{x^{2}-3 x+2}\right)$
(vii) $\underline{\operatorname{Lim}}_{x \rightarrow 2} \frac{x-2}{\sqrt{x+2}-\sqrt{6-x}}$
(viii) $\underline{\operatorname{Lim}}_{h \rightarrow 0} \frac{\sqrt{x+h}-\sqrt{x}}{h}$
(ix) $\quad \underline{\operatorname{Lim}}_{x \rightarrow \infty} \frac{x^{n}-a^{n}}{x^{n}-a^{m}}$
4. Evaluate the following limits:
(i) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{\sin 5 x}{x}$
(ii) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{\sin x^{\prime \prime}}{x}$
(iii) $\underline{\operatorname{Lim}}_{0 \rightarrow 0} \frac{1-\cos \theta}{\sin \theta}$
(iv) $\underline{\operatorname{Lim}}_{x \rightarrow \frac{\pi}{4}} \frac{\sin x-\cos x}{x-\frac{\pi}{4}}$
(v) $\underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{\cos a x-\cos b x}{x^{2}}$
(vi) $\underline{\operatorname{Lim}}_{x \rightarrow \frac{\pi}{4}} \frac{\tan x-1}{x-\frac{\pi}{4}}$
(vii) $\underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{1-\cos 2 x}{x^{2}}$
(viii) $\underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{\cos a x-\cos b x}{\cos c x-\cos d x}$
(ix) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 1} \frac{x^{3}-1}{x^{2}-1}$
(x) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 3} \frac{x^{2}-x \log x+3 \log x-9}{x-3}$
(xi) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{x\left(2^{x}-1\right)}{1-\cos x}$
5. Express each limit in terms of $e$.
(i) $\quad \underline{\operatorname{Lim}}_{n \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{2 n}$
(ii) $\quad \underline{\operatorname{Lim}}_{n \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{n}$
(iii) $\underline{\operatorname{Lim}}_{n \rightarrow+\infty}\left(1-\frac{1}{n}\right)^{n}$
(iv) $\quad \underline{\operatorname{Lim}}_{n \rightarrow+\infty}\left(1+\frac{1}{3 n}\right)^{n}$
(v) $\quad \underline{\operatorname{Lim}}_{n \rightarrow+\infty}\left(1+\frac{4}{n}\right)^{n}$
(vi) $\underline{\operatorname{Lim}}_{x \rightarrow 0}(1+3 x)^{\frac{2}{x}}$
(vii) $\underline{\operatorname{Lim}}_{x \rightarrow 0}\left(1+2 x^{2}\right)^{\frac{1}{x^{2}}}$
(viii) $\underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{e^{a x}-e^{b x}}{a b x}$
(ix) $\quad \underline{\operatorname{Lim}}_{x \rightarrow \infty}\left(\frac{x}{1+x}\right)^{x}$
(x) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{\frac{1}{x}-1}{e^{\frac{1}{x}}+1}, x<0$
(xi) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{e^{\frac{1}{x}}-1}{e^{x}+1}, x>0$
(xii) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 2} \frac{e^{x}-e^{2}}{x-2}$

# 12.3 Continuity and Discontinuity of Functions 12.3.1 One-Sided Limits

In defining $\operatorname{Lim}_{x \rightarrow c} f(x)$, we restricted $x$ in an open interval containing $c$ i.e., we studied the behaviour of $f$ on both sides of $c$. However, in some cases it is necessary to investigate one sided limits that is, the left hand limit and the right hand limit.

## (i) The Left Hand Limit

$\operatorname{Lim}_{x \rightarrow c^{\prime}} f(x)=L$ is read as the limit of $f(x)$ is equal to $L$ as $x$ approaches $c$ from the left i.e., for all $x$ sufficiently close to $c$, but less than $c$, the value of $f(x)$ can be made as close as we please to $L$.
(ii) The Right Hand Limit
$\operatorname{Lim}_{x \rightarrow c^{\prime}} f(x)=M$ is read as the limit of $f(x)$ is equal to $M$ as $x$ approaches $c$ from the right i.e., for all $x$ sufficiently close to $c$, but greater than $c$, the value of $f(x)$ can be made as close as we please to $M$.