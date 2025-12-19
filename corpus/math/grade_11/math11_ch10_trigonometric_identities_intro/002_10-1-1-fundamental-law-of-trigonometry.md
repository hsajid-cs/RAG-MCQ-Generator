### 10.1.1 Fundamental Law of Trigonometry

Let $\alpha$ and $\beta$ be any two angles (real numbers), then

$$
\cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta
$$

which is called the Fundamental Law of Trigonometry.

Proof: For our convenience, let us assume that $\alpha>\beta>0$.
Consider a unit circle with centre at origin $O$.

Let terminal sides of angles $\alpha$ and $\beta$ cut the unit circle at $A$ and $B$ respectively. Evidently $m \angle A O B=\alpha-\beta$

Take a point $C$ on the unit circle such that $m \angle X O C=m \angle A O B=\alpha-\beta$.

Join $A, B$ and $C, D$.
Now angles $\alpha, \beta$ and $\alpha-\beta$ are in standard position.
$\therefore \quad$ The coordinates of $A$ are $(\cos \alpha, \sin \alpha)$.
The coordinates of $B$ are $(\cos \beta, \sin \beta)$
The coordinates of $C$ are $(\cos \alpha-\beta, \sin \alpha-\beta)$
and the coordinates of $D$ are $(1,0)$.
Now $\triangle A O B$ and $\triangle C O D$ are congruent.
Therefore,

$$
|A B|=|C D| \quad \Rightarrow \quad|A B|=|C D|
$$

Using the distance formula, we have:

$$
\begin{aligned}
& (\cos \alpha-\cos \beta)^{2}+(\sin \alpha-\sin \beta)^{2}=[(\cos (\alpha-\beta)-1]^{2}+[\sin (\alpha-\beta)-0]^{2} \\
& \Rightarrow \quad \cos ^{2} \alpha+\cos ^{2} \beta-2 \cos \alpha \cos \beta+\sin ^{2} \alpha+\sin ^{2} \beta-2 \sin \alpha \sin \beta \\
& =\cos ^{2}(\alpha-\beta)+1-2 \cos (\alpha-\beta)+\sin ^{2}(\alpha-\beta) \\
& \Rightarrow \quad 2-2(\cos \alpha \cos \beta+\sin \alpha \sin \beta)=2-2 \cos (\alpha-\beta) \\
& \text { Hence } \quad \cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta .
\end{aligned}
$$

Note Although we have proved this law for $\alpha>\beta>0$, it is true for all values of $\alpha$ and $\beta$.
Suppose we know the values of $\sin$ and $\cos$ of two angles $\alpha$ and $\beta$, we can find $\cos (\alpha-\beta)$ using this law as explained in the following example:
Example 2 Find the value of $\sin \frac{5 \pi}{12}$.
Solution As $\frac{5 \pi}{12}=75^{\circ}=45^{\circ}+30^{\circ}=\frac{\pi}{4}+\frac{\pi}{6}$

$$
\begin{aligned}
\therefore \quad \sin \frac{5 \pi}{12} & =\sin \left(\frac{\pi}{4}+\frac{\pi}{6}\right)=\sin \frac{\pi}{4} \cos \frac{\pi}{6}+\cos \frac{\pi}{4} \sin \frac{\pi}{6} \\
& =\frac{1}{\sqrt{2}} \cdot \frac{\sqrt{3}}{2}+\frac{1}{\sqrt{2}} \cdot \frac{1}{2}=\frac{\sqrt{3}+1}{2 \sqrt{2}}
\end{aligned}
$$

# 10.1.2 Deductions from Fundamental Law

1. We know that:

$$
\cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta
$$

Putting $\alpha=\frac{\pi}{2}$ in it, we get

$$
\begin{aligned}
& \cos \left(\frac{\pi}{2}-\beta\right)=\cos \frac{\pi}{2} \cos \beta+\sin \frac{\pi}{2} \sin \beta \\
& \Rightarrow \quad \cos \left(\frac{\pi}{2}-\beta\right)=0 \cdot \cos \beta+1 \cdot \sin \beta \quad\left(\because \cos \frac{\pi}{2}=0, \sin \frac{\pi}{2}=1\right. \\
& \therefore \quad \cos \left(\frac{\pi}{2}-\beta\right)=\sin \beta
\end{aligned}
$$

2. We know that:

$$
\cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta
$$

Putting $\beta=-\frac{\pi}{2}$ in it, we get

$$
\begin{aligned}
& \cos \left[\alpha-\left(-\frac{\pi}{2}\right)\right]=\cos \alpha \cdot \cos \left(-\frac{\pi}{2}\right)+\sin \alpha \sin \left(-\frac{\pi}{2}\right) \\
& \Rightarrow \quad \cos \left(\alpha+\frac{\pi}{2}\right)=\cos \alpha \cdot 0+\sin \alpha(-1) \\
& \therefore \quad \cos \left(\frac{\pi}{2}+\alpha\right)=-\sin \alpha
\end{aligned}
$$

$$
\begin{aligned}
& \text { (ii) }
\end{aligned}
$$

3. We know that:

$$
\cos \left(\frac{\pi}{2}-\beta\right)=\sin \beta
$$

[(i) above]

Putting $\beta=\frac{\pi}{2}+\alpha$ in it, we get

$$
\cos \left[\frac{\pi}{2}-\left(\frac{\pi}{2}+\alpha\right)\right]=\sin \left(\frac{\pi}{2}+\alpha\right)
$$

$$
\begin{aligned}
& \Rightarrow \quad \cos (-\alpha)=\sin \left(\frac{\pi}{2}+\alpha\right) \\
& \Rightarrow \quad \cos \alpha=\sin \left(\frac{\pi}{2}+\alpha\right) \quad[\because \cos (-\alpha)=\cos \alpha] \\
& \sin \left(\frac{\pi}{2}+\alpha\right)=\cos \alpha
\end{aligned}
$$

4. We know that:

$$
\cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta
$$

Replacing $\beta$ by $-\beta$ we get

$$
\begin{aligned}
& \cos [\alpha-(-\beta)]=\cos \alpha \cos (-\beta)+\sin \alpha \sin (-\beta) \\
& {[\because \cos (-\beta)=\cos \beta, \sin (-\beta)=-\sin \beta]} \\
& \Rightarrow \quad \cos (\alpha+\beta)=\cos \alpha \cos \beta-\sin \alpha \sin \beta
\end{aligned}
$$

5. We know that:

$$
\cos (\alpha+\beta)=\cos \alpha \cos \beta-\sin \alpha \sin \beta
$$

Replacing $\alpha$ by $\frac{\pi}{2}+\alpha$, we get

$$
\begin{aligned}
& \cos \left[\left(\frac{\pi}{2}+\alpha\right)+\beta\right]=\cos \left(\frac{\pi}{2}+\alpha\right) \cos \beta-\sin \left(\frac{\pi}{2}+\alpha\right) \sin \beta \\
& \Rightarrow \quad \cos \left[\frac{\pi}{2}+(\alpha+\beta)\right]=-\sin \alpha \cos \beta-\cos \alpha \sin \beta \\
& \Rightarrow \quad \sin (\alpha+\beta)=-[\sin \alpha \cos \beta+\cos \alpha \sin \beta] \\
& \therefore \quad \sin (\alpha+\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta
\end{aligned}
$$

6. We know that:

$$
\sin (\alpha+\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta \quad \text { [from (v) above] }
$$

Replacing $\beta$ by $-\beta$, we get

$$
\begin{aligned}
& \sin (\alpha-\beta)=\sin \alpha \cos (-\beta)+\cos \alpha \sin (-\beta) \quad \begin{cases}\because & \sin (-\beta)=-\sin \beta \\
& \cos (-\beta)=\cos \beta
\end{cases} \\
& \therefore \quad \sin (\alpha-\beta)=\sin \alpha \cos \beta-\cos \alpha \sin \beta
\end{aligned}
$$

7. We know that:

$$
\cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \cdot \sin \beta
$$

Let $\alpha=2 \pi$ and $\beta=\theta$

$$
\begin{aligned}
\therefore \quad \cos (2 \pi-\theta) & =\cos 2 \pi \cdot \cos \theta+\sin 2 \pi \sin \theta \\
& =1 \cdot \cos \theta+0 \cdot \sin \theta \\
& =\cos \theta
\end{aligned}
$$

8. We know that:

$$
\begin{aligned}
\sin (\alpha-\beta) & =\sin \alpha \cdot \cos \beta-\cos \alpha \cdot \sin \beta \\
\sin (2 \pi-\theta) & =\sin 2 \pi \cdot \cos \theta-\cos 2 \pi \sin \theta \\
& =0 \cdot \cos \theta-1 \cdot \sin \theta \\
& =-\sin \theta
\end{aligned}
$$

$$
\begin{aligned}
& =-\sin \theta \\
& \text { (viii) }
\end{aligned}
$$

9. $\quad \tan (\alpha+\beta)=\frac{\sin (\alpha+\beta)}{\cos (\alpha+\beta)}=\frac{\sin \alpha \cos \beta-\cos \alpha \sin \beta}{\cos \alpha \cos \beta-\sin \alpha \sin \beta}$

$$
=\frac{\frac{\sin \alpha \cos \beta}{\cos \alpha \cos \beta}+\frac{\cos \alpha \sin \beta}{\cos \alpha \cos \beta}}{\frac{\cos \alpha \cos \beta}{\cos \alpha \cos \beta}-\frac{\sin \alpha \sin \beta}{\cos \alpha \cos \beta}} \quad \begin{aligned}
& \text { Dividing } \\
& \text { numerator and } \\
& \text { denominator by } \\
& \cos \alpha \cos \beta
\end{aligned}
$$

$$
\tan (\alpha+\beta)=\frac{\tan \alpha+\tan \beta}{1-\tan \alpha \tan \beta}
$$

10. $\quad \tan (\alpha-\beta)=\frac{\sin (\alpha-\beta)}{\cos (\alpha-\beta)}=\frac{\sin \alpha \cos \beta-\cos \alpha \sin \beta}{\cos \alpha \cos \beta+\sin \alpha \sin \beta}$

$$
=\frac{\frac{\sin \alpha \cos \beta}{\cos \alpha \cos \beta}-\frac{\cos \alpha \sin \beta}{\cos \alpha \cos \beta}}{\frac{\cos \alpha \cos \beta}{\cos \alpha \cos \beta}+\frac{\sin \alpha \sin \beta}{\cos \alpha \cos \beta}} \quad \begin{aligned}
& \text { Dividing } \\
& \text { numerator and } \\
& \text { denominator by } \\
& \cos \alpha \cos \beta
\end{aligned}
$$

$$
\tan (\alpha-\beta)=\frac{\tan \alpha-\tan \beta}{1+\tan \alpha \tan \beta}
$$

# 10.2 Trigonometric Ratios of Allied Angles

Two angles $\alpha$ and $\beta$ are said to be allied, if $\alpha \pm \beta=n\left(90^{\circ}\right), n \in z$
For example, $\pm \alpha, 90^{\circ} \pm \alpha, 180^{\circ} \pm \alpha, 270^{\circ} \pm \alpha$ and $360^{\circ} \pm \alpha$ are some allied angles of $\alpha$. Using fundamental law of trigonometry, $\cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta$ and its deductions, we derive the following identities:

$$
\begin{aligned}
& \sin \left(\frac{\pi}{2}-\theta\right)=\cos \theta, \cos \left(\frac{\pi}{2}-\theta\right)=\sin \theta, \tan \left(\frac{\pi}{2}-\theta\right)=\cot \theta \\
& \sin \left(\frac{\pi}{2}+\theta\right)=\cos \theta, \cos \left(\frac{\pi}{2}+\theta\right)=-\sin \theta, \tan \left(\frac{\pi}{2}+\theta\right)=-\cot \theta \\
& \left\{\begin{array}{l}
\sin (\pi-\theta)=\sin \theta, \cos (\pi-\theta)=-\cos \theta, \tan (\pi-\theta)=-\tan \theta \\
\sin (\pi+\theta)=-\sin \theta, \cos (\pi+\theta)=-\cos \theta, \tan (\pi+\theta)=\tan \theta
\end{array}\right. \\
& \sin \left(\frac{3 \pi}{2}-\theta\right)=-\cos \theta, \cos \left(\frac{3 \pi}{2}-\theta\right)=-\sin \theta, \tan \left(\frac{3 \pi}{2}-\theta\right)=\cot \theta \\
& \sin \left(\frac{3 \pi}{2}+\theta\right)=-\cos \theta, \cos \left(\frac{3 \pi}{2}+\theta\right)=\sin \theta, \tan \left(\frac{3 \pi}{2}+\theta\right)=-\cot \theta \\
& \sin (2 \pi-\theta)=-\sin \theta, \cos (2 \pi-\theta)=\cos \theta, \tan (2 \pi-\theta)=-\tan \theta \\
& \sin (2 \pi+\theta)=\sin \theta, \cos (2 \pi+\theta)=\cos \theta, \tan (2 \pi+\theta)=\tan \theta
\end{aligned}
$$

Note
The above results also apply to the reciprocals of sine, cosine and tangent. These results are to be applied frequently in the study of trigonometry and they can be remembered by using the following device:

1. If $\theta$ is added to or subtracted from odd multiple of right angle, the trigonometric ratios change into co-ratios and vice versa.
i.e., $\sin \longleftrightarrow \cos , \tan \longleftrightarrow \cot , \sec \longleftrightarrow \operatorname{cosec}$
e.g.

$$
\sin \left(\frac{\pi}{2}-\theta\right)=\cos \theta \quad \text { and } \quad \cos \left(\frac{3 \pi}{2}+\theta\right)=\sin \theta
$$

2. If $\theta$ is added to or subtracted from an even multiple of $\frac{\pi}{2}$, the trigonometric ratios shall remain the same.
3. So far as the sign of the results is concerned, it is determined by the quadrant in which the terminal arm of the angle lies.
e.g. $\sin (\pi-\theta)=\sin \theta, \quad \tan (\pi+\theta)=\tan \theta, \quad \cos (2 \pi-\theta)=\cos \theta$.

| Measure of the angle | Quad. |
| :--: | :--: |
| $\frac{\pi}{2}-\theta$ | I |
| $\frac{\pi}{2}+\theta$ or $\pi-\theta$ | II |
| $\pi+\theta$ or $\frac{3 \pi}{2}-\theta$ | III |
| $\frac{3 \pi}{2}+\theta$ or $2 \pi-\theta$ | IV |

(a) $\quad \ln \sin \left(\frac{\pi}{2}-\theta\right), \sin \left(\frac{\pi}{2}+\theta\right), \sin \left(\frac{3 \pi}{2}-\theta\right)$ and $\sin \left(\frac{3 \pi}{2}+\theta\right)$ odd multiplies of $\frac{\pi}{2}$ are involved.

Therefore, sin will change into cos.
Moreover, the angle of measure
(i) $\left(\frac{\pi}{2}-\theta\right)$ will have terminal side in Quad. I,

$$
\text { So, } \sin \left(\frac{\pi}{2}-\theta\right)=\cos \theta
$$

(ii) $\left(\frac{\pi}{2}+\theta\right)$ will have terminal side in Quad. II,

$$
\text { So, } \sin \left(\frac{\pi}{2}+\theta\right)=\cos \theta
$$

(iii) $\left(\frac{3 \pi}{2}-\theta\right)$ will have terminal side in Quad. III,

$$
\text { So, } \sin \left(\frac{3 \pi}{2}-\theta\right)=-\cos \theta
$$

(iv) $\left(\frac{3 \pi}{2}+\theta\right)$ will have terminal side in Quad. IV,

$$
\text { So, } \sin \left(\frac{3 \pi}{2}+\theta\right)=-\cos \theta
$$

(b) In $\cos (\pi-\theta), \cos (\pi+\theta), \cos (2 \pi-\theta)$ and $\cos (2 \pi+\theta)$, even multiples of $\frac{\pi}{2}$ are involved.

Therefore, cos will remain as cos.
Moreover, the angle of measure
(i) $(\pi-\theta)$ will have terminal side in Quad. II, therefore

$$
\cos (\pi-\theta)=-\cos \theta
$$

(ii) $(\pi+\theta)$ will have terminal side in Quad. III, so

$$
\cos (\pi+\theta)=-\cos \theta
$$

(iii) $(2 \pi-\theta)$ will have terminal side in Quad. IV, so

$$
\cos (2 \pi-\theta)=\cos \theta
$$

(iv) $(2 \pi+\theta)$ will have terminal side in Quad. I, so

$$
\cos (2 \pi+\theta)=\cos \theta
$$

Example 3 Without using the tables, write down the values of:
(i) $\sin 225^{\circ}$
(ii) $\tan 600^{\circ}$
(iii) $\cot \left(-225^{\circ}\right)$
(iv) $\operatorname{cosec}\left(-420^{\circ}\right)$

Solution (i) $\sin 225^{\circ}=\sin (180+45)^{\circ}=-\sin 45^{\circ}=-\frac{1}{\sqrt{2}}$
(ii) $\tan 600^{\circ}=\tan (540+60)^{\circ}=\tan (6 \times 90+60)^{\circ}=\tan 60^{\circ}=\sqrt{3}$
(iii) $\cot \left(-225^{\circ}\right)=-\cot 225^{\circ}=-\cot (180+45)^{\circ}=-\cot (2 \times 90+45)^{\circ}=-\left(\cot 45^{\circ}\right)=1$
(iv) $\operatorname{cosec}\left(-420^{\circ}\right)=-\operatorname{cosec} 420^{\circ}=-\operatorname{cosec}(360+60)^{\circ}=-\operatorname{cosec}(4 \times 90+60)^{\circ}$

$$
=-\operatorname{cosec} 60^{\circ}=\frac{-2}{\sqrt{3}}
$$

Example 4 Simplify: $\frac{\sin \left(180^{\circ}-\theta\right) \cos \left(360^{\circ}-\theta\right) \tan \left(90^{\circ}+\theta\right)}{\sin \left(90^{\circ}-\theta\right) \cos \left(180^{\circ}+\theta\right) \tan \left(270^{\circ}-\theta\right)}$

$$
\text { Solution Because }\left\{\begin{array}{l}
\sin \left(180^{\circ}-\theta\right)=\sin \theta, \cos \left(360^{\circ}-\theta\right)=\cos \theta \\
\tan \left(90^{\circ}+\theta\right)=-\cot \theta, \sin \left(90^{\circ}-\theta\right)=\cos \theta \\
\cos \left(180^{\circ}+\theta\right)=-\cos \theta, \tan \left(270^{\circ}-\theta\right)=\cot \theta
\end{array}\right.
$$

Therefore, $\frac{\sin \theta \cdot \cos \theta \cdot(-\cot \theta)}{\cos \theta \cdot(-\cos \theta) \cdot \cot \theta}=\frac{-\sin \theta}{-\cos \theta}=\tan \theta$

# EXERCISE 10.1

1. Without using the tables, find the values of:
(i) $\cos \left(-1230^{\circ}\right)$
(ii) $\tan \left(-1035^{\circ}\right)$
(iii) $\sec \left(1140^{\circ}\right)$
(iv) $\operatorname{cosec}\left(-690^{\circ}\right)$
(v) $\cot \left(1320^{\circ}\right)$
(vi) $\cos \left(-240^{\circ}\right)$
2. Express each of the following as a trigonometric function of an angle of positive degree measure of less than $45^{\circ}$.
(i) $\cos 168^{\circ}$
(ii) $\sin 192^{\circ}$
(iii) $\cos 333^{\circ}$
(iv) $\tan 213^{\circ}$
(v) $\cos \left(-435^{\circ}\right)$
(vi) $\sin 219^{\circ}$
(vii) $\tan \left(-597^{\circ}\right)$
(viii) $\cos \left(-111^{\circ}\right)$
(ix) $\sin \left(-390^{\circ}\right)$
3. Prove the following:
(i) $\sin \left(180^{\circ}+\alpha\right) \sin \left(90^{\circ}-\alpha\right)=-\sin \alpha \cos \alpha$
(ii) $\sin 810^{\circ} \sin 630^{\circ}+\cos 135^{\circ} \sin 225^{\circ}=\frac{1}{2}$
(iii) $\tan 150^{\circ} \cot 330^{\circ}-2 \sec 135^{\circ} \operatorname{cosec} 225^{\circ}=-3$
(iv) $\sin 210^{\circ}+\cos 240^{\circ}+\tan 225^{\circ}+\cot 225^{\circ}=1$
4. Prove that:
(i) $\frac{\tan \left(180^{\circ}+\alpha\right) \cot \left(90^{\circ}-\alpha\right)}{\sin \left(360^{\circ}-\alpha\right) \cos \left(270^{\circ}+\alpha\right)}=-\sec ^{2} \alpha$
(ii) $\frac{\sin ^{2}(\pi+\theta) \tan \left(\frac{3 \pi}{2}+\theta\right)}{\cot ^{2}\left(\frac{3 \pi}{2}-\theta\right) \cos ^{2}(\pi-\theta) \operatorname{cosec}(2 \pi-\theta)}=\cos \theta$
(iii) $\frac{\cos \left(90^{\circ}+\theta\right) \sec (-\theta) \tan \left(180^{\circ}-\theta\right)}{\sec \left(360^{\circ}-\theta\right) \sin \left(180^{\circ}+\theta\right) \cot \left(90^{\circ}-\theta\right)}=-1$
5. Show that: $\sec \left(\frac{3 \pi}{2}-\theta\right) \sec \left(\frac{5 \pi}{2}-\theta\right)-\tan \left(\frac{3 \pi}{2}-\theta\right) \tan \left(\frac{5 \pi}{2}+\theta\right)=-1$
6. If $\alpha, \beta, \gamma$ are the angles of a triangle $A B C$, then prove that
(i) $\sin (\alpha+\beta)=\sin \gamma$
(ii) $\sec \left(\frac{\alpha+\beta}{2}\right)=\csc \frac{\gamma}{2}$
(iii) $\operatorname{cosec} \alpha=\frac{1}{\sin (\beta+\gamma)}$
(iv) $\tan (\alpha+\beta)+\tan \gamma=0$.

# 10.3 Further Applications of Basic Identities

Example 5
Prove that: $\sin (\alpha+\beta) \sin (\alpha-\beta)=\sin ^{2} \alpha-\sin ^{2} \beta$

$$
=\cos ^{2} \beta-\cos ^{2} \alpha
$$

Solution L.H.S. $=\sin (\alpha+\beta) \sin (\alpha-\beta)$

$$
\begin{aligned}
& =(\sin \alpha \cos \beta+\cos \alpha \sin \beta)(\sin \alpha \cos \beta-\cos \alpha \sin \beta) \\
& =\sin ^{2} \alpha \cos ^{2} \beta-\cos ^{2} \alpha \sin ^{2} \beta \\
& =\sin ^{2} \alpha\left(1-\sin ^{2} \beta\right)-\left(1-\sin ^{2} \alpha\right) \sin ^{2} \beta \\
& =\sin ^{2} \alpha-\sin ^{2} \alpha \sin ^{2} \beta-\sin ^{2} \beta+\sin ^{2} \alpha \sin ^{2} \beta \\
& =\sin ^{2} \alpha-\sin ^{2} \beta \\
& =\left(1-\cos ^{2} \alpha\right)-\left(1-\cos ^{2} \beta\right) \\
& =1-\cos ^{2} \alpha-1+\cos ^{2} \beta \\
& =\cos ^{2} \beta-\cos ^{2} \alpha
\end{aligned}
$$

Example 6 Without using tables, find the values of all trigonometric functions of $105^{\circ}$
Solution As $105^{\circ}=60^{\circ}+45^{\circ}$

$$
\begin{aligned}
\sin 105^{\circ} & =\sin \left(60^{\circ}+45^{\circ}\right)=\sin 60^{\circ} \cos 45^{\circ}+\cos 60^{\circ} \sin 45^{\circ} \\
& =\left(\frac{\sqrt{3}}{2}\right)\left(\frac{1}{\sqrt{2}}\right)+\left(\frac{1}{2}\right)\left(\frac{1}{\sqrt{2}}\right)=\frac{\sqrt{3}+1}{2 \sqrt{2}} \\
\cos 105^{\circ} & =\cos \left(60^{\circ}+45^{\circ}\right)=\cos 60^{\circ} \cos 45^{\circ}-\sin 60^{\circ} \sin 45^{\circ} \\
& =\left(\frac{1}{2}\right)\left(\frac{1}{\sqrt{2}}\right)-\left(\frac{\sqrt{3}}{2}\right)\left(\frac{1}{\sqrt{2}}\right)-=\frac{1-\sqrt{3}}{2 \sqrt{2}} \\
\tan 105^{\circ} & =\tan \left(60^{\circ}+45^{\circ}\right)=\frac{\tan 60^{\circ}+\tan 45^{\circ}}{1-\tan 60^{\circ} \tan 45^{\circ}} \\
& =\frac{\sqrt{3}+1}{1-\sqrt{3} \cdot 1}=\frac{1+\sqrt{3}}{1-\sqrt{3}} \\
\cot 105^{\circ} & =\frac{1}{\tan 105^{\circ}}=\frac{1-\sqrt{3}}{1+\sqrt{3}} \\
\operatorname{cosec} 105^{\circ} & =\frac{1}{\sin 105^{\circ}}=\frac{2 \sqrt{2}}{\sqrt{3}+1} \\
\text { and } \quad \sec 105^{\circ} & =\frac{1}{\cos 105^{\circ}}=\frac{2 \sqrt{2}}{1-\sqrt{3}}
\end{aligned}
$$

Example 7 Prove that: $\frac{\cos 11^{\circ}+\sin 11^{\circ}}{\cos 11^{\circ}-\sin 11^{\circ}}=\tan 56^{\circ}$
Solution Consider

$$
\begin{aligned}
& \text { R.H.S }=\tan 56^{\circ}=\tan \left(45^{\circ}+11^{\circ}\right)=\frac{\tan 45^{\circ}+\tan 11^{\circ}}{1-\tan 45^{\circ} \tan 11^{\circ}} \\
& =\frac{1+\tan 11^{\circ}}{1-\tan 11^{\circ}}=\frac{1+\frac{\sin 11^{\circ}}{\cos 11^{\circ}}}{1-\frac{\sin 11^{\circ}}{\cos 11^{\circ}}}=\frac{\cos 11^{\circ}+\sin 11^{\circ}}{\cos 11^{\circ}-\sin 11^{\circ}}=\text { L.H.S }
\end{aligned}
$$

Hence $\frac{\cos 11^{\circ}+\sin 11^{\circ}}{\cos 11^{\circ}-\sin 11^{\circ}}=\tan 56^{\circ}$
Example 8 If $\cos \alpha=-\frac{7}{25}, \tan \beta=\frac{12}{5}$, the terminal side of the angle of measure $\alpha$ is in the II quadrant and that of $\beta$ is in the III quadrant, find the values of:
(i) $\sin (\alpha+\beta)$
(ii) $\cos (\alpha+\beta)$

In which quadrant does the terminal side of the angle of measure $(\alpha+\beta)$ lie?
Solution We know that $\sin ^{2} \alpha+\cos ^{2} \alpha=1$
Therefore, $\sin \alpha= \pm \sqrt{1-\cos ^{2} \alpha}= \pm \sqrt{1-\left(-\frac{7}{25}\right)^{2}}= \pm \sqrt{\frac{576}{625}}= \pm \frac{24}{25}$
As the terminal side of the angle of measure of $\alpha$ is in the II quadrant, where $\sin \alpha$ is positive.

So, $\quad \sin \alpha=\frac{24}{25}$
Now $\sec \beta= \pm \sqrt{1+\tan ^{2} \beta}= \pm \sqrt{1+\left(\frac{12}{5}\right)^{2}}= \pm \frac{13}{5}$
As the terminal side of the angle of measure of $\beta$ in the quadrant III, so sec $\beta$ is negative

$$
\begin{aligned}
& \sec \beta=-\frac{13}{5} \quad \text { and } \quad \cos \beta=-\frac{5}{13} \\
& \sin \beta= \pm \sqrt{1-\cos ^{2} \beta}= \pm \sqrt{1-\left(-\frac{5}{13}\right)^{2}}= \pm \sqrt{\frac{144}{169}}= \pm \frac{12}{13}
\end{aligned}
$$

As the terminal arm of the angle of measure $\beta$ is in the III quadrant, so $\sin \beta$ is negative

$$
\sin \beta=-\frac{12}{13}
$$

$\sin (\alpha+\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta$

$$
=\left(\frac{24}{25}\right)\left(-\frac{5}{13}\right)+\left(-\frac{7}{25}\right)\left(-\frac{12}{13}\right)=\frac{-120+84}{325}=-\frac{36}{325}
$$

and $\cos (\alpha+\beta)=\cos \alpha \cos \beta-\sin \alpha \sin \beta$

$$
=\left(-\frac{7}{25}\right)\left(-\frac{5}{13}\right)-\left(\frac{24}{25}\right)\left(-\frac{12}{13}\right)=\frac{35+288}{325}=\frac{323}{325}
$$

As, $\sin (\alpha+\beta)$ is -ve and $\cos (\alpha+\beta)$ is +ve
Thus, the terminal arm of the angle of measure $(\alpha+\beta)$ is in the quadrant IV.
Example 9 If $\alpha, \beta, \gamma$ are the angles of $\triangle A B C$, prove that:
(i) $\tan \alpha+\tan \beta+\tan \gamma=\tan \alpha \tan \beta \tan \gamma$
(ii) $\tan \frac{\alpha}{2} \tan \frac{\beta}{2}+\tan \frac{\beta}{2} \tan \frac{\gamma}{2}+\tan \frac{\gamma}{2} \tan \frac{\alpha}{2}=1$

Solution As $\alpha, \beta, \gamma$ are the angles of $\triangle A B C$, therefore

$$
\begin{aligned}
\alpha+\beta+\gamma & =180^{\circ} \\
\alpha+\beta & =180^{\circ}-\gamma
\end{aligned}
$$

(i) $\tan (\alpha+\beta)=\tan \left(180^{\circ}-\gamma\right)$

$$
\begin{aligned}
& \frac{\tan \alpha+\tan \beta}{1-\tan \alpha \tan \beta}=-\tan \gamma \\
& \tan \alpha+\tan \beta=-\tan \gamma+\tan \alpha \tan \beta \tan \gamma
\end{aligned}
$$

$\tan \alpha+\tan \beta+\tan \gamma=\tan \alpha \tan \beta \tan \gamma$
(ii) As $\alpha+\beta+\gamma=180^{\circ} \Rightarrow \frac{\alpha}{2}+\frac{\beta}{2}+\frac{\gamma}{2}=90^{\circ}$

$$
\begin{aligned}
& \text { so } \quad \frac{\alpha}{2}+\frac{\beta}{2}=90^{\circ}-\frac{\gamma}{2} \\
& \tan \left(\frac{\alpha}{2}+\frac{\beta}{2}\right)=\tan \left(90^{\circ}-\frac{\gamma}{2}\right) \\
& \frac{\tan \frac{\alpha}{2}+\tan \frac{\beta}{2}}{1-\tan \frac{\alpha}{2} \tan \frac{\beta}{2}}=\cot \frac{\gamma}{2}=\frac{1}{\tan \frac{\gamma}{2}} \\
& \tan \frac{\alpha}{2} \tan \frac{\gamma}{2}+\tan \frac{\beta}{2} \tan \frac{\gamma}{2}=1-\tan \frac{\alpha}{2} \tan \frac{\beta}{2} \\
& \tan \frac{\alpha}{2} \tan \frac{\beta}{2}+\tan \frac{\beta}{2} \tan \frac{\gamma}{2}+\tan \frac{\gamma}{2} \tan \frac{\alpha}{2}=1
\end{aligned}
$$

Example16 Express $3 \sin \theta+4 \cos \theta$ in the form $r \sin (\theta+\phi)$, where the terminal side of the angle of measure $\phi$ is in quadrant 1 .

| Solution | Let $3=r \cos \phi$ | (i) |
| :-- | :-- | :-- |
|  | and $4=r \sin \phi$ | (ii) |

Squaring then adding (i) and (ii)

$$
3^{2}+4^{2}=r^{2} \cos ^{2} \phi+r^{2} \sin ^{2} \phi
$$

Dividing (ii) by (i)

$$
\begin{aligned}
& \Rightarrow \quad 9+16=r^{2}\left(\cos ^{2} \phi+\sin ^{2} \phi\right)\left\{\begin{array}{l}
\frac{4}{3}=\frac{r \sin \phi}{r \cos \phi} \\
\frac{4}{3}=\tan \phi \\
\frac{4}{3}=\tan \phi \\
\tan \phi=\frac{4}{3}
\end{array}\right. \\
& 3 \sin \theta+4 \cos \theta=r \cos \phi \sin \theta+r \sin \phi \cos \theta \\
& =r(\sin \theta \cos \phi+\cos \theta \sin \phi) \\
& =r \sin (\theta+\phi) \\
& \text { where } \quad r=5 \quad \text { and } \quad \tan ^{-1} \phi=\frac{4}{3}
\end{aligned}
$$

# EXERCISE 10.2

1. Without using table find the values of the following:
(i) $\sin 15^{\circ}$
(ii) $\cos 15^{\circ}$
(iii) $\tan 15^{\circ}$
(iv) $\sin 105^{\circ}$
(v) $\cos 105^{\circ}$
(vi) $\tan 105^{\circ}$
2. Prove that
(i) $\sin \left(45^{\circ}+\alpha\right)=\frac{1}{\sqrt{2}}(\sin \alpha+\cos \alpha)$
(ii) $\cos \left(\alpha+45^{\circ}\right)=\frac{1}{\sqrt{2}}(\cos \alpha-\sin \alpha)$
3. Prove that:
(i) $\tan \left(45^{\circ}+A\right) \tan \left(45^{\circ}-A\right)=1$
(ii) $\tan \left(\frac{\pi}{4}-\theta\right)+\tan \left(\frac{3 \pi}{4}+\theta\right)=0$
(iii) $\quad \sin \left(\theta+\frac{\pi}{6}\right)+\cos \left(\theta+\frac{\pi}{3}\right)=\cos \theta$
(iv) $\frac{\sin \theta-\cos \theta \tan \frac{\theta}{2}}{\cos \theta+\sin \theta \tan \frac{\theta}{2}}=\tan \frac{\theta}{2}$
(v) $\frac{1-\tan \theta \tan \phi}{1+\tan \theta \tan \phi}=\frac{\cos (\theta+\phi)}{\cos (\theta-\phi)}$

4. Show that: $\cos (\alpha+\beta) \cos (\alpha-\beta)=\cos ^{2} \alpha-\sin ^{2} \beta=\cos ^{2} \beta-\sin ^{2} \alpha$
5. Show that: $\frac{\sin (\alpha+\beta)+\sin (\alpha-\beta)}{\cos (\alpha+\beta)+\cos (\alpha-\beta)}=\tan \alpha$
6. Show that: (i) $\sin ^{2}\left(\alpha+\frac{\beta}{2}\right)-\sin ^{2}\left(\alpha-\frac{\beta}{2}\right)=\sin 2 \alpha \cdot \sin \beta$
(ii) $\sin ^{2} \alpha+\sin ^{2} \beta+\cos ^{2}(\alpha+\beta)+2 \sin \alpha \cdot \sin \beta \cdot \cos (\alpha+\beta)=1$
7. Show that:
(i) $\cos (\alpha-\beta)=\frac{1+\tan \alpha \tan \beta}{\sec \alpha \sec \beta}$
(ii) $\sin (\alpha+\beta)=\frac{1+\cot \alpha \tan \beta}{\cos \sec \alpha \sec \beta}$
(iii) $\cot (\alpha-\beta)=\frac{\cot \alpha \cot \beta+1}{\cot \beta-\cot \alpha}$
(iv) $\frac{\tan \alpha+\tan \beta}{\tan \alpha-\tan \beta}=\frac{\sin (\alpha+\beta)}{\sin (\alpha-\beta)}$
(v) $\cot (\alpha+\beta)=\frac{\cot \alpha \cot \beta-1}{\cot \alpha+\cot \beta}$
8. If $\sin \alpha=\frac{24}{25}$ and $\cos \beta=\frac{20}{29}$, where $0<\alpha<\frac{\pi}{2}$ and $0<\beta<\frac{\pi}{2}$.

Show that $\sin (\alpha-\beta)=\frac{333}{725}$.
9. If $\sin \alpha=-\frac{8}{17}$ and $\cos \beta=-\frac{4}{5}$ where $\frac{3 \pi}{2}<\alpha<2 \pi$ and $\pi<\beta<\frac{3 \pi}{2}$. Find
(i) $\sin (\alpha+\beta)$
(ii) $\cos (\alpha+\beta)$
(iii) $\tan (\alpha+\beta)$
(iv) $\sin (\alpha-\beta)$
(v) $\cos (\alpha-\beta)$
(vi) $\tan (\alpha-\beta)$.

In which quadrants do the terminal sides of the angles of measures $(\alpha+\beta)$ and $(\alpha-\beta)$ lip?
10. Find $\sin (\alpha+\beta)$ and $\cos (\alpha+\beta)$, given that
(i) $\tan \alpha=\frac{3}{4}, \cos \beta=\frac{5}{13}$ and neither the terminal side of the angle of measure $\alpha$ nor that of $\beta$ is in the quadrant I .
(ii) $\tan \alpha=-\frac{15}{8}$ and $\sin \beta=-\frac{7}{25}$ and neither the terminal side of the angle of measure $\alpha$ nor that of $\beta$ is in the quadrant IV.
11. Prove that: $\frac{\cos 19^{\circ}+\sin 19^{\circ}}{\cos 19^{\circ}-\sin 19^{\circ}}=\tan 64^{\circ}$.
12. Prove that: $\cos \left(60^{\circ}+\theta\right) \cos \left(60^{\circ}-\theta\right)+\sin \left(60^{\circ}+\theta\right) \sin \left(60^{\circ}-\theta\right)=\cos 2 \theta$

13. If $\alpha, \beta, \gamma$ are the angles of a triangle $A B C$, show that

$$
\cot \frac{\alpha}{2}+\cot \frac{\beta}{2}+\cot \frac{\gamma}{2}=\cot \frac{\alpha}{2} \cot \frac{\beta}{2} \cot \frac{\gamma}{2}
$$

14. If $\alpha+\beta+\gamma=180^{\circ}$, show that: $\cot \alpha \cot \beta+\cot \beta \cot \gamma+\cot \gamma \cot \alpha=1$
15. Express the following in the form $r \sin (\theta+\phi)$ or $r \sin (\theta-\phi)$ where terminal sides of the angles of measures $\theta$ and $\phi$ are in the first quadrant:
(i) $24 \sin \theta+7 \cos \theta$
(ii) $12 \sin \theta-5 \cos \theta$
(iii) $\sin \theta-\cos \theta$
(iv) $8 \sin \theta-6 \cos \theta$
(v) $\frac{1}{2} \sin \theta+\frac{\sqrt{3}}{2} \cos \theta$
(vi) $13 \sin \theta-84 \cos \theta$

# 10.4 Double Angle Identities

We have discussed the following results:

$$
\begin{aligned}
& \sin (\alpha+\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta \\
& \cos (\alpha+\beta)=\cos \alpha \cos \beta-\sin \alpha \sin \beta \quad \text { and } \quad \tan (\alpha+\beta)=\frac{\tan \alpha+\tan \beta}{1-\tan \alpha \tan \beta}
\end{aligned}
$$

We can use them to obtain the double angle identities as follows:
(i) Put $\beta=\alpha$ in $\sin (\alpha+\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta$
$\sin (\alpha+\alpha)=\sin \alpha \cos \alpha+\cos \alpha \sin \alpha$
Hence $\sin 2 \alpha=2 \sin \alpha \cos \alpha$
(ii) Put $\beta=\alpha$ in $\cos (\alpha+\beta)=\cos \alpha \cos \beta-\sin \alpha \sin \beta$
$\cos (\alpha+\alpha)=\cos \alpha \cos \alpha-\sin \alpha \sin \alpha$
Hence $\cos 2 \alpha=\cos ^{2} \alpha-\sin ^{2} \alpha$
$\cos 2 \alpha=\cos ^{2} \alpha-\sin ^{2} \alpha$
$\cos 2 \alpha=\cos ^{2} \alpha-\left(1-\cos ^{2} \alpha\right) \quad\left(\because \sin ^{2} \alpha=1-\cos ^{2} \alpha\right)$

$$
=\cos ^{2} \alpha-1+\cos ^{2} \alpha
$$

$\cos 2 \alpha=2 \cos ^{2} \alpha-1$
$\cos 2 \alpha=\cos ^{2} \alpha-\sin ^{2} \alpha$
$\cos 2 \alpha=\left(1-\sin ^{2} \alpha\right)-\sin ^{2} \alpha \quad\left(\because \cos ^{2} \alpha=1-\sin ^{2} \alpha\right)$
$\cos 2 \alpha=1-2 \sin ^{2} \alpha$
(iii) Put $\beta=\alpha \ln \tan (\alpha+\beta)=\frac{\tan \alpha+\tan \beta}{1-\tan \alpha \tan \beta}$

$$
\begin{aligned}
\tan (\alpha+\alpha) & =\frac{\tan \alpha+\tan \alpha}{1-\tan \alpha \tan \alpha} \\
\tan 2 \alpha & =\frac{2 \tan \alpha}{1-\tan ^{2} \alpha}
\end{aligned}
$$

# 10.5 Half Angle Identities

The formulas proved above can also be written in the form of half angle identities, in the following way:
(i) $\cos \alpha=2 \cos ^{2} \frac{\alpha}{2}-1 \Rightarrow \cos ^{2} \frac{\alpha}{2}=\frac{1+\cos \alpha}{2} \Rightarrow \cos \frac{\alpha}{2}= \pm \sqrt{\frac{1+\cos \alpha}{2}}$
(ii) $\cos \alpha=1-2 \sin ^{2} \frac{\alpha}{2} \Rightarrow \sin ^{2} \frac{\alpha}{2}=\frac{1-\cos \alpha}{2} \Rightarrow \sin \frac{\alpha}{2}= \pm \sqrt{\frac{1-\cos \alpha}{2}}$
(iii) $\tan \frac{\alpha}{2}=\frac{\sin \frac{\alpha}{2}}{\cos \frac{\alpha}{2}}= \pm \sqrt{\frac{1-\cos \alpha}{2}} \Rightarrow \tan \frac{\alpha}{2}= \pm \sqrt{\frac{1-\cos \alpha}{1+\cos \alpha}}$