### 1.5.8 If $\theta$ is measured in radian, then $\operatorname{Lim}_{\theta} \frac{\sin \theta}{\theta}=1$

Proof: To evaluate this limit, we apply a new technique. Take $\theta$ a positive acute central angle of a circle with radius $r=1$. As shown in the figure, $O A B$ represents a sector of the circle.

Given $|O A|=|O B|=1 \quad$ (radii of unit circle)
$\therefore \ln \pi \Delta O C B, \sin \theta=\frac{|B C|}{|O B|}=|B C| \quad(\because|O B|=1)$
$\ln \pi \Delta O A D, \tan \theta=\frac{|A D|}{|O A|}=|A D| \quad(\because|O A|=1)$
In terms of $\theta$, the areas are expressed as:
Produce OB to $\mathbf{D}$ so that $\mathbf{A D} \perp$ OA. Draw $\mathbf{B C} \perp$ OA. Join $\mathbf{A B}$
(i) Area of $\Delta O A B=\frac{1}{2}|O A||B C|=\frac{1}{2}(1)(\sin \theta)=\frac{1}{2} \sin \theta$
(ii) Area of sector $O A B=\frac{1}{2} r^{2} \theta=\frac{1}{2}(1)(\theta)=\frac{1}{2} \theta \quad(\because \tau=1)$
and (iii) Area of $\Delta O A D=\frac{1}{2}|O A||A D|=\frac{1}{2}(1)(\tan \theta)=\frac{1}{2} \tan \theta$

From the figure we see that
Area of $\triangle O A B<$ Area of sector $O A B<$ Area of $\triangle O A D$

$$
\Rightarrow \quad \frac{1}{2} \sin \theta<\frac{\theta}{2}<\frac{1}{2} \tan \theta
$$

As $\sin \theta$ is positive, so on division by $\frac{1}{2} \sin \theta$, we get

$$
\begin{aligned}
& 1<\frac{\theta}{\sin \theta}<\frac{1}{\cos \theta} \quad\left(0<\theta<\frac{\pi}{2}\right) \\
& \text { i.e., } \quad 1>\frac{\sin \theta}{\theta}>\cos \theta \quad \text { or } \quad \cos \theta<\frac{\sin \theta}{\theta}<1 \\
& \text { when } \theta \rightarrow 0, \cos \theta \rightarrow 1
\end{aligned}
$$

Since $\frac{\sin \theta}{\theta}$ is sandwitched between 1 and a quantity approaching 1 itself.
So, by the sandwitch theorem, it must also approach 1.
i.e., $\lim _{\theta \rightarrow 0} \frac{\sin \theta}{\theta}=1$

Note: The same result holds for $-\pi / 2<\theta<\theta$
Example 6: $\quad$ Evaluate: $\lim _{\theta \rightarrow 0} \frac{\sin 7 \theta}{\theta}$
Solution: Observe the resemblance of the limit with $\lim _{\theta \rightarrow 0} \frac{\sin \theta}{\theta}=1$
Let $\quad x=7 \theta \quad$ so that $\theta=x / 7$
when $\theta \rightarrow 0 \quad, \quad$ we have $x \rightarrow 0$
$\therefore \quad \lim _{\theta \rightarrow 0} \frac{\sin 7 \theta}{\theta}=\lim _{\theta \rightarrow 0} \frac{\sin x}{x / 7}=7 \lim _{\theta \rightarrow 0} \frac{\sin x}{x}=(7)(1)=7$
Example 7: $\quad$ Evaluate: $\lim _{\theta \rightarrow 0} \frac{1-\cos \theta}{\theta}$
Solution: $\frac{1-\cos \theta}{\theta}=\frac{1-\cos \theta}{\theta} \frac{1+\cos \theta}{1+\cos \theta}$

$$
=\frac{1-\cos ^{2} \theta}{\theta(1+\cos \theta})=\frac{\sin ^{2} \theta}{\theta(1+\cos \theta})=\sin \theta\left(\frac{\sin \theta}{\theta}\right)\left(\frac{1}{1+\cos \theta}\right)
$$

$\therefore \quad \lim _{\theta \rightarrow 0} \frac{1-\cos \theta}{\theta}=\lim _{\theta \rightarrow 0} \sin \theta \lim _{\theta \rightarrow 0} \frac{\sin \theta}{\theta} \lim _{\theta \rightarrow 0} \frac{1}{1+\cos \theta}$

$$
\begin{aligned}
& =(0)(1) \frac{1}{1+1} \\
& =(0)
\end{aligned}
$$

## EXERCISE 1.3

1. Evaluate each limit by using theorems of limits:
(i) $\lim _{x \rightarrow 3^{-}}(2 x+4)$
(ii) $\lim _{x \rightarrow 3^{-}}\left(3 x^{2}-2 x+4\right)$
(iii) $\lim _{x \rightarrow 3^{-}} \sqrt{x^{2}+x+4}$
(iv) $\lim _{x \rightarrow 3^{-}} \sqrt{x^{2}-4}$
(v) $\lim _{x \rightarrow 3^{-}}\left(\sqrt{x^{2}+1}-\sqrt{x^{2}+5}\right)$
(vi) $\lim _{x \rightarrow 3^{-}} \frac{2 x^{3}+5 x}{3 x-2}$
2. Evaluate each limit by using algebraic techniques.
(i) $\lim _{x \rightarrow 3^{-}} \frac{x^{3}-x}{x+1}$
(ii) $\lim _{x \rightarrow 0^{-}}\left(\frac{3 x^{3}+4 x}{x^{2}+x}\right)$
(iii) $\lim _{x \rightarrow 0^{-}} \frac{x^{3}-8}{x^{2}+x-6}$
(iv) $\lim _{x \rightarrow 3^{-}} \frac{x^{3}-3 x^{2}+3 x-1}{x^{3}-x}$
(v) $\lim _{x \rightarrow 0^{-}}\left(\frac{x^{3}+x^{2}}{x^{2}-1}\right)$
(vi) $\lim _{x \rightarrow 0^{-}} \frac{2 x^{3}-32}{x^{2}-4 x^{2}}$
(vii) $\lim _{x \rightarrow 0^{-}} \frac{\sqrt{x}-\sqrt{2}}{x-2}$
(viii) $\lim _{x \rightarrow 0^{-}} \frac{\sqrt{x+h}-\sqrt{x}}{h}$
(ix) $\lim _{x \rightarrow 0^{-}} \frac{x^{n}-a^{n}}{x^{m}-a^{m}}$
3. Evaluate the following limits
(i) $\lim _{x \rightarrow 0^{-}} \frac{\sin 7 x}{x}$
(ii) $\lim _{x \rightarrow 0^{-}} \frac{\sin x^{n}}{x}$
(iii) $\lim _{x \rightarrow 0^{-}} \frac{1-\cos \theta}{\sin \theta}$
(iv) $\lim _{x \rightarrow 0^{-}} \frac{\sin x}{\pi-x}$
(v) $\lim _{x \rightarrow 0^{-}} \frac{\sin a x}{\sinh x}$
(vi) $\lim _{x \rightarrow 0^{-}} \frac{-\pi}{\tan x}$
(vii) $\lim _{x \rightarrow 0^{-}} \frac{1-\cos 2 x}{x^{2}}$
(viii) $\lim _{x \rightarrow 0^{-}} \frac{1-\cos x}{\sin ^{2} x}$
(ix) $\lim _{\theta \rightarrow 0^{-}} \frac{\sin ^{2} \theta}{\theta}$
(x) $\lim _{x \rightarrow 0^{-}} \frac{\sec x-\cos x}{x}$
(xi) $\lim _{\theta \rightarrow 0^{-}} \frac{1-\cos p \theta}{1-\cos q \theta}$
(xii) $\lim _{\theta \rightarrow 0^{-}} \frac{\tan \theta-\sin \theta}{\sin ^{2} \theta}$
4. Express each limit in terms of $e$ :
(i) $\lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{2 n}$
(ii) $\lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{\frac{n}{2}}$
(iii) $\lim _{n \rightarrow \infty}\left(1-\frac{1}{n}\right)^{n}$
(iv) $\lim _{n \rightarrow \infty}\left(1+\frac{1}{3 n}\right)^{n}$
(v) $\lim _{n \rightarrow \infty}\left(1+\frac{4}{n}\right)^{n}$
(vi) $\lim _{x \rightarrow 0^{-}}(1+3 x)^{\frac{1}{n}}$

(vii) $\operatorname{Lim}_{x \rightarrow 0}\left(1+2 x^{2}\right)^{\frac{1}{x^{2}}}$
(viii) $\operatorname{Lim}_{x \rightarrow 0}(1-2 h)^{\frac{1}{x}}$
(ix) $\operatorname{Lim}_{x \rightarrow x}\left(\frac{x}{1+x}\right)^{x}$
(x) $\operatorname{Lim}_{x \rightarrow 0} \frac{e^{2 / x}-1}{e^{2 / x}+1} \cdot x<0$
(xi) $\operatorname{Lim}_{x \rightarrow 0} \frac{e^{2 / x}-1}{e^{2 / x}+1} \cdot x>0$