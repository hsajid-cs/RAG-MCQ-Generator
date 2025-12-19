### 10.6 Triple Angle Identities

(i) $\sin 3 \alpha=3 \sin \alpha-4 \sin ^{3} \alpha$
(ii) $\cos 3 \alpha=4 \cos ^{3} \alpha-3 \cos \alpha$
(iii) $\tan 3 \alpha=\frac{3 \tan \alpha-\tan ^{3} \alpha}{1-3 \tan ^{3} \alpha}$

Proof: (i) $\sin 3 \alpha=\sin (2 \alpha+\alpha)$

$$
\begin{aligned}
& =\sin 2 \alpha \cos \alpha+\cos 2 \alpha \sin \alpha \\
& =2 \sin \alpha \cos \alpha \cos \alpha+\left(1-2 \sin ^{2} \alpha\right) \sin \alpha \\
& =2 \sin \alpha \cos ^{2} \alpha+\sin \alpha-2 \sin ^{3} \alpha \\
& =2 \sin \alpha\left(1-\sin ^{2} \alpha\right)+\sin \alpha-2 \sin ^{3} \alpha \\
& =2 \sin \alpha-2 \sin ^{3} \alpha+\sin \alpha-2 \sin ^{3} \alpha \\
\sin 3 \alpha & =3 \sin \alpha-4 \sin ^{3} \alpha \\
\text { (ii) } \cos 3 \alpha & =\cos (2 \alpha+\alpha) \\
& =\cos 2 \alpha \cos \alpha-\sin 2 \alpha \sin \alpha \\
& =\left(2 \cos ^{2} \alpha-1\right) \cos \alpha-2 \sin \alpha \cos \alpha \sin \alpha \\
& =2 \cos ^{3} \alpha-\cos \alpha-2 \sin ^{2} \alpha \cos \alpha \\
& =2 \cos ^{3} \alpha-\cos \alpha-2\left(1-\cos ^{2} \alpha\right) \cos \alpha \\
& =2 \cos ^{3} \alpha-\cos \alpha-2 \cos \alpha+2 \cos ^{3} \alpha \\
\cos 3 \alpha & =4 \cos ^{3} \alpha-3 \cos \alpha
\end{aligned}
$$

(iii) $\tan 3 \alpha=\tan (2 \alpha+\alpha)$

$$
=\frac{\tan 2 \alpha+\tan \alpha}{1-\tan 2 \alpha \tan \alpha}
$$

# Unit 10 Trigonometric Identities <193

$$
\begin{aligned}
& =\frac{\frac{2 \tan \alpha}{1-\tan ^{2} \alpha}+\tan \alpha}{1-\frac{2 \tan \alpha}{1-\tan ^{2} \alpha} \cdot \tan \alpha}=\frac{2 \tan \alpha+\tan \alpha-\tan ^{2} \alpha}{1-\tan ^{2} \alpha-2 \tan ^{2} \alpha} \\
& \tan ^{2} \alpha=\frac{3 \tan \alpha-\tan ^{3} \alpha}{1-3 \tan ^{2} \alpha}
\end{aligned}
$$

Example 11 Prove that: $\frac{\sin \theta+\sin 2 \theta}{1+\cos \theta+\cos 2 \theta}=\tan \theta$
Solution

$$
\begin{aligned}
\text { L.H.S. } & =\frac{\sin \theta+2 \sin \theta \cos \theta}{1+\cos \theta+2 \cos ^{2} \theta-1}=\frac{\sin \theta(1+2 \cos \theta)}{\cos \theta(1+2 \cos \theta)} \\
& =\frac{\sin \theta}{\cos \theta}=\tan \theta=\text { R.H.S. }
\end{aligned}
$$

Hence $\frac{\sin \theta+\sin 2 \theta}{1+\cos \theta+\cos 2 \theta}=\tan \theta$.
Example 12 Show that: (i) $\sin 2 \theta=\frac{2 \tan \theta}{1+\tan ^{2} \theta}$ (ii) $\cos 2 \theta=\frac{1-\tan ^{2} \theta}{1+\tan ^{2} \theta}$
Solution (i) $\sin 2 \theta=2 \sin \theta \cos \theta=\frac{2 \sin \theta \cos \theta}{1}=\frac{2 \sin \theta \cos \theta}{\cos ^{2} \theta+\sin ^{2} \theta}$

$$
=\frac{\frac{2 \sin \theta \cos \theta}{\cos ^{2} \theta}}{\frac{\cos ^{2} \theta+\sin ^{2} \theta}{\cos ^{2} \theta}}=\frac{2 \frac{\sin \theta}{\cos \theta}}{\frac{\cos ^{2} \theta}{\cos ^{2} \theta}+\frac{\sin ^{2} \theta}{\cos ^{2} \theta}}
$$

$$
\sin 2 \theta=\frac{2 \tan \theta}{1+\tan ^{2} \theta}
$$

(ii) $\cos 2 \theta=\cos ^{2} \theta-\sin ^{2} \theta=\frac{\cos ^{2} \theta-\sin ^{2} \theta}{1}=\frac{\cos ^{2} \theta-\sin ^{2} \theta}{\cos ^{2} \theta+\sin ^{2} \theta}$

$$
=\frac{\frac{\cos ^{2} \theta-\sin ^{2} \theta}{\cos ^{2} \theta}}{\frac{\cos ^{2} \theta+\sin ^{2} \theta}{\cos ^{2} \theta}}=\frac{\frac{\cos ^{2} \theta}{\cos ^{2} \theta}-\frac{\sin ^{2} \theta}{\cos ^{2} \theta}}{\frac{\cos ^{2} \theta}{\cos ^{2} \theta}+\frac{\sin ^{2} \theta}{\cos ^{2} \theta}}
$$

$\cos 2 \theta=\frac{1-\tan ^{2} \theta}{1+\tan ^{2} \theta}$

Example 13 Reduce $\cos ^{4} \theta$ to an expression involving only function of multiples of $\theta$, raised to the first power.
Solution We know that:

$$
\begin{aligned}
2 \cos ^{2} \theta & =1+\cos 2 \theta \quad \Rightarrow \cos ^{2} \theta=\frac{1+\cos 2 \theta}{2} \\
\cos ^{4} \theta & =\left(\cos ^{2} \theta\right)^{2}=\left[\frac{1+\cos 2 \theta}{2}\right]^{2} \\
& =\frac{1+2 \cos 2 \theta+\cos ^{2} 2 \theta}{4} \\
& =\frac{1}{4}\left[1+2 \cos 2 \theta+\cos ^{2} 2 \theta\right] \\
& =\frac{1}{4}\left[1+2 \cos 2 \theta+\frac{1+\cos 4 \theta}{2}\right] \\
& =\frac{1}{4 \times 2}[2+4 \cos 2 \theta+1+\cos 4 \theta] \\
& =\frac{1}{8}[3+4 \cos 2 \theta+\cos 4 \theta]
\end{aligned}
$$

# EXERCISE 10.3

1. Find the values of $\sin 2 \alpha, \cos 2 \alpha$ and $\tan 2 \alpha$, when:
(i) $\sin \alpha=\frac{3}{5}$
(ii) $\cos \alpha=\frac{4}{5}$, where $0<\alpha<\frac{\pi}{2}$
2. Prove the following identities:
(i) $\cot \alpha-\tan \alpha=2 \cot 2 \alpha$
(ii) $\frac{\sin 2 \alpha}{1+\cos 2 \alpha}=\tan \alpha$
(iii) $\frac{1-\cos \alpha}{\sin \alpha}=\tan \frac{\alpha}{2}$
(iv) $\frac{\cos \alpha-\sin \alpha}{\cos \alpha+\sin \alpha}=\sec 2 \alpha-\tan 2 \alpha$
(v) $\sqrt{\frac{1+\sin \alpha}{1-\sin \alpha}}=\frac{\sin \frac{\alpha}{2}+\cos \frac{\alpha}{2}}{\sin \frac{\alpha}{2}-\cos \frac{\alpha}{2}}$
(vi) $\frac{\operatorname{cosec} \theta+2 \operatorname{cosec} 2 \theta}{\sec \theta}=\cot \frac{\theta}{2}$
(vii) $1+\tan \alpha \tan 2 \alpha=\sec 2 \alpha$
(viii) $\frac{2 \sin \theta \sin 2 \theta}{\cos \theta+\cos 3 \theta}=\tan 2 \theta \tan \theta$

(ix) $\frac{\sin 3 \theta}{\sin \theta}-\frac{\cos 3 \theta}{\cos \theta}=2$
(x) $\frac{\cos 3 \theta}{\cos \theta}+\frac{\sin 3 \theta}{\sin \theta}=4 \cos 2 \theta$
(xi) $\frac{\tan \frac{\theta}{2}+\cot \frac{\theta}{2}}{\cot \frac{\theta}{2}-\tan \frac{\theta}{2}}=\sec \theta$
(xii) $\frac{\sin 3 \theta}{\cos \theta}+\frac{\cos 3 \theta}{\sin \theta}=2 \cot 2 \theta$
(xiii) $\frac{3+\cos 4 \theta}{1-\cos 4 \theta}=\frac{1}{2}\left(\tan ^{2} \theta+\cot ^{2} \theta\right)$
(xiv) $\frac{1+\sin 2 \theta}{1-\sin 2 \theta}=\tan ^{2}\left(\frac{\pi}{4}+\theta\right)$
(xv) $\cos ^{2} \frac{\pi}{8}+\cos ^{2} \frac{3 \pi}{8}+\cos ^{2} \frac{5 \pi}{8}+\cos ^{2} \frac{7 \pi}{8}=2$
3. Show that: $2 \cos \theta=\sqrt{2+\sqrt{2+2 \cos 4 \theta}}$
4. Reduce $\sin ^{4} \theta$ to an expression involving only function of multiples of $\theta$, raised to the first power.
5. Find the values of $\sin \theta$ and $\cos \theta$ without using table or calculator, when $\theta$ is:
(i) $18^{\circ}$
(ii) $36^{\circ}$
(iii) $54^{\circ}$
(iv) $72^{\circ}$

Hence prove that: $\cos 36^{\circ} \cos 72^{\circ} \cos 108^{\circ} \cos 144^{\circ}=\frac{1}{16}$

| Hint | Let $\theta=18^{\circ}$ | Let $\theta=36^{\circ}$ |
| :--: | :--: | :--: |
|  | $5 \theta=90^{\circ}$ | $5 \theta=180^{\circ}$ |
|  | $(3 \theta+2 \theta)=90^{\circ}$ | $3 \theta+2 \theta=180^{\circ}$ |
|  | $3 \theta=90^{\circ}-2 \theta$ | $3 \theta=180^{\circ}-2 \theta$ |
|  | $\sin 3 \theta=\sin \left(90^{\circ}-2 \theta\right)$ etc | $\sin 3 \theta=\sin \left(180^{\circ}-2 \theta\right)$ etc. |

# 10.7 Express the Product (of sines and cosines) as Sums or Differences (of sines and cosines)

We know that:

$$
\begin{aligned}
& \sin (\alpha+\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta \\
& \sin (\alpha-\beta)=\sin \alpha \cos \beta-\cos \alpha \sin \beta \\
& \cos (\alpha+\beta)=\cos \alpha \cos \beta-\sin \alpha \sin \beta \\
& \cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta
\end{aligned}
$$

Adding (i) and (ii) we get

$$
\sin (\alpha+\beta)+\sin (\alpha-\beta)=2 \sin \alpha \cos \beta
$$

Subtracting (ii) from (i) we get

$$
\sin (\alpha+\beta)-\sin (\alpha-\beta)=2 \cos \alpha \sin \beta
$$

Adding (iii) and (iv) we get

$$
\cos (\alpha+\beta)+\cos (\alpha-\beta)=2 \cos \alpha \cos \beta
$$

Subtracting (iv) from (iii), we get

$$
\cos (\alpha+\beta)-\cos (\alpha-\beta)=-2 \sin \alpha \sin \beta
$$

So, we get four identities as:

$$
\begin{aligned}
& 2 \sin \alpha \cos \beta=\sin (\alpha+\beta)+\sin (\alpha-\beta) \\
& 2 \cos \alpha \sin \beta=\sin (\alpha+\beta)-\sin (\alpha-\beta) \\
& 2 \cos \alpha \cos \beta=\cos (\alpha+\beta)+\cos (\alpha-\beta) \\
& -2 \sin \alpha \sin \beta=\cos (\alpha+\beta)-\cos (\alpha-\beta)
\end{aligned}
$$

Now putting $\alpha+\beta=P$ and $\alpha-\beta=Q$, we get

$$
\begin{aligned}
& \alpha=\frac{P+Q}{2} \quad \text { and } \beta=\frac{P-Q}{2} \\
& \begin{aligned}
\sin P+\sin Q & =2 \sin \frac{P+Q}{2} \cos \frac{P-Q}{2} \\
\sin P-\sin Q & =2 \cos \frac{P+Q}{2} \sin \frac{P-Q}{2} \\
\cos P+\cos Q & =2 \cos \frac{P+Q}{2} \cos \frac{P-Q}{2} \\
\cos P-\cos Q & =-2 \sin \frac{P+Q}{2} \sin \frac{P-Q}{2}
\end{aligned}
\end{aligned}
$$

Example 14 Express $2 \sin 7 \theta \cos 3 \theta$ as a sum or difference.
Solution $2 \sin 7 \theta \cos 3 \theta=\sin (7 \theta+3 \theta)+\sin (7 \theta-3 \theta)$

$$
=\sin 10 \theta+\sin 4 \theta
$$

Example 15 Prove without using table / calculator, that

$$
\sin 19^{\circ} \cos 11^{\circ}+\sin 71^{\circ} \sin 11^{\circ}=\frac{1}{2}
$$

Solution L.H.S $=\sin 19^{\circ} \cos 11^{\circ}+\sin 71^{\circ} \sin 11^{\circ}$

$$
\begin{aligned}
& =\frac{1}{2}\left[2 \sin 19^{\circ} \cos 11^{\circ}+2 \sin 71^{\circ} \sin 11^{\circ}\right] \\
& =\frac{1}{2}\left[\left\{\sin \left(19^{\circ}+11^{\circ}\right)+\sin \left(19^{\circ}-11^{\circ}\right)\right\}-\left\{\cos \left(71^{\circ}+11^{\circ}\right)-\cos \left(71^{\circ}-11^{\circ}\right)\right\}\right] \\
& =\frac{1}{2}\left[\sin 30^{\circ}+\sin 8^{\circ}-\cos 82^{\circ}+\cos 60^{\circ}\right] \\
& =\frac{1}{2}\left[\frac{1}{2}+\sin 8^{\circ}-\cos \left(90^{\circ}-8^{\circ}\right)+\frac{1}{2}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{2}\left[\frac{1}{2}+\sin 8^{\circ}-\sin 8^{\circ}+\frac{1}{2}\right] \quad\left(\because \cos 82^{\circ}=\cos \left(90^{\circ}-8^{\circ}\right)=\sin 8^{\circ}\right) \\
& =\frac{1}{2}\left[\frac{1}{2}+\frac{1}{2}\right] \\
& =\frac{1}{2}=\text { R.H.S }
\end{aligned}
$$

Hence, $\sin 19^{\circ} \cos 11^{\circ}+\sin 71^{\circ} \sin 11^{\circ}=\frac{1}{2}$
Example 16 Expresn $\sin 5 x+\sin 7 x$ as a product.
Solution

$$
\begin{aligned}
\sin 5 x+\sin 7 x & =2 \sin \frac{5 x+7 x}{2} \cos \frac{5 x-7 x}{2}=2 \sin 6 x \cos (-x) \\
& =2 \sin 6 x \cos x \quad\left(\because \cos (- \theta)=\cos \theta\right)
\end{aligned}
$$

Example 17 Expresn $\cos \theta+\cos 3 \theta+\cos 5 \theta+\cos 7 \theta$ as a product.
Solution $\cos \theta+\cos 3 \theta+\cos 5 \theta+\cos 7 \theta$

$$
\begin{aligned}
& =(\cos 3 \theta+\cos \theta)+(\cos 7 \theta+\cos 5 \theta) \\
& =2 \cos \frac{3 \theta+\theta}{2} \cos \frac{3 \theta-\theta}{2}+2 \cos \frac{7 \theta+5 \theta}{2} \cos \frac{7 \theta-5 \theta}{2} \\
& =2 \cos 2 \theta \cos \theta+2 \cos 6 \theta \cos \theta \\
& =2 \cos \theta(\cos 6 \theta+\cos 2 \theta) \\
& =2 \cos \theta\left[2 \cos \frac{6 \theta+2 \theta}{2} \cos \frac{6 \theta-2 \theta}{2}\right] \\
& =2 \cos \theta(2 \cos 4 \theta \cos 2 \theta)=4 \cos \theta \cos 2 \theta \cos 4 \theta
\end{aligned}
$$

Example 18 Show that $\cos 20^{\circ} \cos 40^{\circ} \cos 80^{\circ}=\frac{1}{8}$
Solution L.H.S $=\cos 20^{\circ} \cos 40^{\circ} \cos 80^{\circ}$

$$
\begin{aligned}
& =\frac{1}{4}\left(4 \cos 20^{\circ} \cos 40^{\circ} \cos 80^{\circ}\right) \\
& =\frac{1}{4}\left[\left(2 \cos 40^{\circ} \cos 20^{\circ}\right) \cdot 2 \cos 80^{\circ}\right] \\
& =\frac{1}{4}\left[\left(\cos 60^{\circ}+\cos 20^{\circ}\right) \cdot 2 \cos 80^{\circ}\right] \\
& =\frac{1}{4}\left[\left(\frac{1}{2}+\cos 20^{\circ}\right) \cdot 2 \cos 80^{\circ}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{4}\left(\cos 80^{\circ}+2 \cos 80^{\circ} \cos 20^{\circ}\right) \\
& =\frac{1}{4}\left(\cos 80^{\circ}+\cos 100^{\circ}+\cos 60^{\circ}\right) \\
& =\frac{1}{4}\left[\cos 80^{\circ}+\cos \left(180^{\circ}-80^{\circ}\right)+\cos 60^{\circ}\right] \\
& =\frac{1}{4}\left[\cos 80^{\circ}-\cos 80^{\circ}+\frac{1}{2}\right] \quad\left[\because \cos \left(180^{\circ}-\theta\right)=-\cos \theta\right] \\
& =\frac{1}{4}\left(\frac{1}{2}\right)=\frac{1}{8}=\text { R.H.S }
\end{aligned}
$$

Hence, $\cos 20^{\circ} \cos 40^{\circ} \cos 80^{\circ}=\frac{1}{8}$

# EXERCISE 10.4

1. Express the following products as sums or differences:
(i) $2 \sin 3 \theta \cos \theta$
(ii) $2 \cos 5 \theta \sin 3 \theta$
(iii) $\sin 5 \theta \cos 2 \theta$
(iv) $2 \sin 7 \theta \sin 2 \theta$
(v) $\cos (x+y) \sin (x-y)$
(vi) $\cos \left(2 x+30^{\circ}\right) \cos \left(2 x-30^{\circ}\right)$
(vii) $\sin 12^{\circ} \sin 46^{\circ}$
(viii) $\sin \left(x+45^{\circ}\right) \sin \left(x-45^{\circ}\right)$
2. Express the following sums or differences as products:
(i) $\sin 5 \theta+\sin 3 \theta$
(ii) $\sin 8 \theta-\sin 4 \theta$
(iii) $\cos 6 \theta+\cos 3 \theta$
(iv) $\cos 7 \theta-\cos \theta$
(v) $\cos 12^{\circ}+\cos 48^{\circ}$
(vi) $\sin \left(x+30^{\circ}\right)+\sin \left(x-30^{\circ}\right)$
3. Prove the following identities:
(i) $\frac{\sin 3 x-\sin x}{\cos x-\cos 3 x}=\cot 2 x$
(ii) $\frac{\sin 8 x+\sin 2 x}{\cos 8 x+\cos 2 x}=\tan 5 x$
(iii) $\frac{\sin A-\sin B}{\sin A+\sin B}=\tan \frac{A-B}{2} \cot \frac{A+B}{2}$
(iv) $\frac{\sin 80^{\circ}+\sin 40^{\circ}}{\cos 80^{\circ}+\cos 40^{\circ}}=\sqrt{3}$
4. Prove that:
(i) $\cos 15^{\circ}+\cos 105^{\circ}+\cos 195^{\circ}+\cos 160^{\circ}+\cos 285^{\circ}=0$
(ii) $\frac{\sin 2 \theta+\sin 4 \theta+\sin 6 \theta+\sin 8 \theta}{\cos 2 \theta+\cos 4 \theta+\cos 6 \theta+\cos 8 \theta}=\tan 5 \theta$

(iii) $\cos ^{2}\left(\frac{\pi}{4}-\frac{\alpha}{2}\right)-\cos ^{2}\left(\frac{\pi}{4}+\frac{\alpha}{2}\right)=\sin \alpha$
(iv) $\sin \left(\frac{\pi}{4}-\theta\right) \sin \left(\frac{\pi}{4}+\theta\right)=\frac{1}{2} \cos 2 \theta$
(v) $\frac{\sin \theta+\sin 3 \theta+\sin 5 \theta+\sin 7 \theta}{\cos \theta+\cos 3 \theta+\cos 5 \theta+\cos 7 \theta}=\tan 4 \theta$
5. Prove that:
(i) $\cos 20^{\circ} \cos 40^{\circ} \cos 60^{\circ} \cos 80^{\circ}=\frac{1}{16}$
(ii) $\sin \frac{\pi}{9} \sin \frac{2 \pi}{9} \sin \frac{\pi}{3} \sin \frac{4 \pi}{9}=\frac{3}{16}$
(iii) $\sin 10^{\circ} \sin 30^{\circ} \sin 50^{\circ} \sin 70^{\circ}=\frac{1}{16}$
6. Prove that: $\frac{\sin 3 \theta}{1+2 \cos 2 \theta}=\sin \theta$; deduce the value of $\sin 15^{\circ}$
7. Prove that: $\tan 75^{\circ}-\tan 15^{\circ}=2 \sqrt{3}$
8. Prove that: $\cos 15^{\circ}-\sin 15^{\circ}=\frac{1}{\sqrt{2}}$
9. Prove that: $\frac{\sin ^{2} \alpha-\sin ^{2} \beta}{\sin \alpha \cos \alpha-\sin \beta \cos \beta}=\tan (\alpha+\beta)$
10. Prove that:
$\sin \alpha+\sin \beta+\sin \gamma-\sin (\alpha+\beta+\gamma)=4 \sin \left(\frac{\alpha+\beta}{2}\right) \sin \left(\frac{\beta+\gamma}{2}\right) \sin \left(\frac{\gamma+\alpha}{2}\right)$