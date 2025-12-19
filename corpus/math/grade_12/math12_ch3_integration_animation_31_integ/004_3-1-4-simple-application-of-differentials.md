### 3.1.4 Simple application of differentials

Use of differentials for approximation is explained in the following examples.
Example 1: Use differentials to approximate the value of $\sqrt{17}$.
Solution: Let $f(x)=\sqrt{x}$
Then $f(x+\delta x)=\sqrt{x+\delta x}$
As the nearest perfect square root to 17 is 16 , so we take $x=16$
and $\delta x=d x=1$
Then $y=f(16)=\sqrt{16}=4$
Using $f(x+\delta x) \approx f(x)+d y$

$$
\approx f(x)+f^{\prime}(x) d x \text {. we have }
$$

$$
\begin{aligned}
f(16+1) & \approx f(16)+\frac{1}{2 \sqrt{16}} \times(1) \quad\left(\because f^{\prime}(x)=\frac{1}{2 \sqrt{x}}\right) \\
& \approx 4+\frac{1}{2 \times 4}=4+\frac{1}{8}=4.125
\end{aligned}
$$

Hence $\sqrt{17} \approx 4.125$
Example 2: Use differentials to approximate the value of $\sqrt[3]{8.6}$
Solution: Let $f(x)=\sqrt[3]{x} \quad$ then

$$
y+\delta y=f(x+\delta x)=\sqrt[3]{x+\delta x}=\sqrt[3]{x+d x} \quad(\because \delta x=d x) \text { and } f^{\prime}(x) \frac{1}{3 x^{3}}
$$

As the nearest perfect cube root to 8.6 is 8 , so we take $x=8$ and $d x=0.6$, then

$$
\begin{aligned}
& f(8)=\sqrt[3]{8}=2 \quad \text { and } \quad f^{\prime}(8)=\frac{1}{3(8)^{2}} \quad \frac{1}{3 \times 4} \quad \frac{1}{12} \\
& \text { so } \quad d y=f^{\prime}(x) d x=\frac{1}{12} \times(0.6)=0.05 \\
& \text { Using } f(x+\delta x)=f(x)+d y \text {, we have } \\
& f(8+0.6)=f(8)+0.05 \\
& \quad \neq 2 \quad 0.05 \quad 2.05
\end{aligned}
$$

But using calculator, we find that $\sqrt[3]{8.6}$ is approximately equal to 2.0488 .

## Example 3: Using differentials, find the approximate value of $\sin 46^{\circ}$

Solution: Let $y=\sin x$, then

$$
y+\delta y=\sin (x+\delta x)=\sin (x+d x) \quad(\delta x=d x)
$$

We take $x=45^{\circ}=\frac{\pi}{4} \quad$ and $d x=1^{\circ} \quad=0.01745$

$$
\text { Hence } d y=\cos x d x \quad\left(-\frac{d}{d x}(\sin x)=\cos x\right)
$$

$$
\begin{aligned}
& \approx\left(\cos 45^{\circ}\right)(0.01745)=\frac{1}{\sqrt{2}}(0.01745) \\
& \approx 0.7071(0.01745) \\
& \approx 0.01234 \\
& \text { Using } f(x+\delta x) \approx f(x)+d y \text { we have } \\
& \sin \left(46^{\circ}\right) \approx \sin 45^{\circ}+d y \approx 0.7071+0.01234=0.71944 \\
& \approx 0.7194
\end{aligned}
$$

Using calculator, we find $\sin 46^{\circ}$ is approximately equal to 0.71934 .
Example 4: The side of a cube is measured to be 20 cm with a maximum error of 12 cm in its measurement. Find the maximum error in the calculated volume of the cube.

Solution: Let $x$ be the side and $V$ be the volume of the cube, then

$$
V=x^{3} \quad \text { and } \quad d V=\left(3 x^{2}\right) d x
$$

Taking $x=20(\mathrm{~cm})$ and $d x=0.12(\mathrm{~cm})$, we get

$$
d V=[3(20)^{2}](0.12)=1200 x(0.12)=144(\text { cubic } \mathrm{cm})
$$

The error 144 cubic cm in volume calculation of a cube is either positive or negative.

## EXERCISE 3.1

1. Find $\delta y$ and $d y$ in the following cases:
(i) $y=x^{2}-1$
when $x$ changes from 3 to 3.02
(ii) $y=x^{2}+2 x$
when $x$ changes from 2 to 1.8
(iii) $y=\sqrt{x}$
when $x$ changes from 4 to 4.41
2. Using differentials find $\frac{d y}{d x}$ and $\frac{d x}{d y}$ in the following equations
(i) $x y+x=4$
(ii) $x^{2}+2 y^{2}=16$
(iii) $x^{4}+y^{2}=x y^{2}$
(iv) $x y-\ln x=c$
3. Use differentials to approximate the values of
(i) $\sqrt[3]{17}$
(ii) $(31)^{1 / 5}$
(iii) $\cos 29^{\circ}$
(iv) $\sin 61^{\circ}$
4. Find the approximate increase in the volume of a cube if the length of its each edge changes from 5 to 5.02 .
5. Find the approximate increase in the area of a circular disc if its diameter is ?