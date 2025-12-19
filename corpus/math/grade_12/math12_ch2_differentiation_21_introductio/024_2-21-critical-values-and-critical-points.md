### 2.21 CRITICAL VALUES AND CRITICAL POINTS

If $c \in D f$ and $f^{\prime}(c)=0$ or $f^{\prime}(c)$ does not exist, then the number $c$ is called a critical value for $f$ while the point $(c, f(c))$ on the graph of $f$ is named as a critical point.

Note: There are functions which have extrema (maxima or minima) at the points where their derivatives do not exist. For example, the derivatives of the function $f$ and $\phi$ defined as.

$$
\begin{gathered}
f(x)=|x| \\
\text { and } \phi(x)=\left[\begin{array}{l}
2-x \quad x>0 \\
2+x \quad x \leq 0
\end{array}\right.
\end{gathered}
$$

do not exist at $(0,0)$ and $(0,2)$ respectively.
But $f$ has minima at $(0,0)$ and $\phi$ has maxima at $(0,2)$. See the adjoining figures.

Those critical points on the graph of $f$ at which $f^{\prime}(x)=0$ are called stationary points of $f$.

Now we discuss relative maxima and relative minima of the differentiable function $f$ defined as:

$$
y=f(x)=x^{3}-3 x^{2}+4 \ldots(1)
$$

Graph of $f$ is drawn with the help of some ordered pairs tabulated as below:

| $X$ | $-3 / 2$ | -1 | $-1 / 2$ | 0 | $1 / 2$ | 1 | $3 / 2$ | 2 | $5 / 2$ | 3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $Y$ | $-49 / 8$ | 0 | $25 / 8$ | 4 | $27 / 8$ | 2 | $5 / 8$ | 0 | $7 / 8$ | 4 |

Now differentiating (i) w.r.t. ' $x$ ' we get

$$
\begin{aligned}
& f^{\prime}(x)=3 x^{2}-6 x=3 x(x-2) \\
& f^{\prime}(x)=0 \quad \Rightarrow 3 x(x-2)=0 \quad \Rightarrow x=0 \text { or } x=2
\end{aligned}
$$

Now we consider an interval $(-\delta x, \delta x)$ in the neighbourhood of $x=0$. Let $0-\varepsilon$ is a point in the interval $(-\delta x, 0)$ We see that

$$
\begin{aligned}
& f^{\prime}(0-\varepsilon)=3(-\varepsilon)(-\varepsilon-2) \\
& =3 \varepsilon(\varepsilon+2)>0 \quad(\because \varepsilon>0, \varepsilon+2>0) \\
& \text { That is } f^{\prime}(x) \text { is positive for all } x \in(-\delta x, 0) \text {. } \\
& \text { Let } 0+\varepsilon_{i} \text { is a point in the interval }(0, \delta x) \text {, then we have } \\
& f^{\prime}\left(0+\varepsilon_{i}\right)=3\left(\varepsilon_{i}\right)\left(\varepsilon_{i}-2\right) \\
& =3 \varepsilon_{i}\left(2 \varepsilon_{i}\right) 0\left(\because 2-\varepsilon_{i}>0, \varepsilon_{i}>0\right), \text { that is, } \\
& f^{\prime}(x) \text { is negative for all } x \in(0, \delta x)
\end{aligned}
$$

We note that $f^{\prime}(x)>0$ before $x=0, f^{\prime}(x)=0$ at $x \ll 0$ and $f^{\prime}(x) \quad 0$ after $x=0$.
The graph of $f$ shows that it has relative maxima at $x=0$.
Thus we conclude that a function has relative maxima at $x=c$ if $f^{\prime}(x)>0$, before $x=c f^{\prime}(c)=0$ and $f^{\prime}(x)<0$ after $x=c$.

Considering an interval $(2-\delta x, 2+\delta x)$ in the neighbourhood of $x=2$ we find the values of $f^{\prime}(2-\varepsilon)$ and $f^{\prime}(2+\varepsilon)$ when $2-\varepsilon \in(2-\delta x, 2)$ and $2+\varepsilon \in(2,2+\delta x)$

$$
\begin{aligned}
f^{\prime}(2-\varepsilon) & =3(2-\varepsilon)(2-\varepsilon-2) & {\left[\because f^{\prime}(x)=3 x(x-2)\right]} \\
& =3(2-\varepsilon)(-\varepsilon) & \\
& =-3 \varepsilon(2-\varepsilon)<0 & (\because \varepsilon>0,2-\varepsilon>0) \\
\text { and } f^{\prime}(2+\varepsilon) & =3(2+\varepsilon)(2+\varepsilon-2) & \\
& =3 \varepsilon(2+\varepsilon)>0 & (\because \varepsilon>0,2+\varepsilon>0)
\end{aligned}
$$

We see that $f^{\prime}(x)<0$ before $x=2, f^{\prime}(x)=0$ at $x=2$ and $f^{\prime}(x)>0$ after $x=2$.
It is obvious from the graph that it has relative minima at $x=2$.
Thus we conclude that a function has relative minima at $x=c$ if $f^{\prime}(x)<0$ before $x=c, f^{\prime}(x)=0$ at $x=c$ and $f^{\prime}(x)>0$ after $x=c$.

## First Derivative Rule:

Let $f$ be differentiable in neighbourhood of $c$ where $f^{\prime}(c)=0$.

1. If $f^{\prime}(x)$ changes sign from positive to negative as $x$ increases through $c$, then $f(c)$ the relative maxima of $f$.
2. If $f^{\prime}(x)$ changes sign from negative to positive as $x$ increases through $c$, then $f(c)$ is the relative minima of $f$.

Note: 1. A stationary point is called a turning point if it is either a maximum point or a minimum point.
2. If $f^{\prime}(x)>0$ before the point $x=a, f^{\prime}(x)=0$ at $x=0$ and $f^{\prime}(x)>0$ after $x=0$, then $f$ does not has a relative maxima.
See the graph of $f(x)=x^{3}$. In this case, we have

$$
\begin{aligned}
& f^{\prime}(x)=3 x^{2}, \text { that is, } \\
& f^{\prime}(0-\varepsilon)=3(-\varepsilon)^{2}=3 \varepsilon^{2}>0 \\
& \text { and } f^{\prime}(0+\varepsilon)=3(\varepsilon)^{2}=3 \varepsilon^{2}>0
\end{aligned}
$$

The function $f$ is increasing before $x=0$ and also it is increasing after $x=0$.
Such a point of the function is called the point of inflexion.
## Second Derivative Test:

We have noticed that the first derivative $f^{\prime}(x)$ of a function changes its sign from positive to negative at the point where $f$ has relative maxima, that is, $f^{\prime}$ is a decreasing function in the neighbouring interval containing the point where $f$ has relative maxima.

Thus $f^{\prime \prime}(x)$ is negative at the point where $f$ has a relative maxima.
But $f^{\prime}(x)$ of a function $f$ changes its sign from negative to positive at the point where $f$ has relative minima, that is, $f^{\prime}$ is an increasing function in the neighbouring interval containing the point where $f$ has relative minima.

Thus $f^{\prime \prime}(x)$ is positive at the point where $f$ has relative minima.

## Second Derivative Rule

Let $f$ be differential function in a neighbourhood of $c$ where $f^{\prime}(c)=0$. Then

1. $f$ has relative maxima at $c$ if $f^{\prime \prime}(c)<0$.
2. $f$ has relative minima at $c$ if $f^{\prime \prime}(c)>0$.

Example 1: $\quad$ Examine the function defined as

$$
f(x)=x^{3}-6 x^{2}+9 x \text { for extreme values. }
$$

Solution: $f^{\prime}(x)=3 x^{2}-12 x+9$

$$
=3\left(x^{2}-4 x+3\right)=3(x-1)(x-3)
$$

## First Method

If $x=1-\varepsilon$ where $\varepsilon$ is very very small positive number, then

$$
\begin{aligned}
& (x-1)(x-3)=(1-\varepsilon-1)(1-\varepsilon-3)=(-\varepsilon)(-\varepsilon-2)=\varepsilon(2+\varepsilon)>0 \text { that is } \\
& f^{\prime}(x)>0 \text { before } x=1 . \text { For } x=1 \quad \varepsilon \text {, we have } \\
& (x-1)(x-3)=(1+\varepsilon-1)(1+\varepsilon-3)=( \varepsilon)(-2+\varepsilon)=-\varepsilon(2-\varepsilon)<0
\end{aligned}
$$

That is, $f^{\prime}(x)<0$ after $x=1$
As $f^{\prime}(x)>0$ before $x=1, f^{\prime}(x)=0$ at $x \quad 1$ and $f^{\prime}(x)<0$ after $x \quad 1$
Thus $f$ has relative maxima at $x=1$ and $f(1)=-1-6+9=4$.
Let $x=3-\varepsilon$, then

$$
(x-1)(x-3)=(3-\varepsilon-1)(3-\varepsilon-3)=(2-\varepsilon)(-\varepsilon)=-\varepsilon(2-\varepsilon)<0
$$

That is $f^{\prime}(x)<0$ before $x=3$.
For $x=3+\varepsilon$

$$
(x-1)(x-3)=(3+\varepsilon-1)(3+\varepsilon-3)=(2+\varepsilon)(\varepsilon)>0
$$

That is, $f^{\prime}(x)>0$ after $x=3$.
As $f^{\prime}(x)<0$ before $x=3, f^{\prime}(x)$ at $x=3$ and $f^{\prime}(x)>0$ after $x=3$,
Thus $f$ has relative minima at $x=3$. and $f(3)=3(3)^{2}-12(3)+9=0$
Second Method: $f^{\prime \prime}(x)=3(2 x-4)=6(x-2)$

$$
f^{\prime \prime}(1)=6(1-2)=-6<0 \text {, therefore, }
$$

$f$ has relative maxima at $x=1$ and $f(1)=(1)^{2}-6(1)^{2}+9(1)$

$$
=1-6+9=4
$$

$f^{\prime \prime}(3)=6(3-2)=6>0$, therefore $f$ has relative minima at $x=3$ and $f(3)=27-54+27=0$

Example 2: Examine the function defined as $f(x)=1+x^{3}$ for extreme values
Solution: Given that $f(x)=1+x^{3}$
Differentiating w.r.t. ' $x$ ' we get $f^{\prime}(x)=3 x^{2}$

$$
\begin{array}{ll}
f^{\prime}(x)=0 & \Rightarrow 3 x^{2}=0 \\
f^{\prime \prime}(x)=6 x & \text { and } f^{\prime \prime}(0)=6(0)=0
\end{array}
$$

The second derivative does not help in determining the extreme values.

$$
\begin{aligned}
& f^{\prime}(0-\varepsilon)=3(0-\varepsilon)^{2}=3 \varepsilon^{2}>0 \\
& f^{\prime}(0+\varepsilon)=3(0+\varepsilon)^{2}=3 \varepsilon^{2}>0
\end{aligned}
$$

As the first derivative does not change sign at $x=0$, therefore $(0,0)$ is a point of inflexion.

Example 3: Discuss the function defined as $f(x)=\sin x+\frac{1}{2 \sqrt{2}} \cos 2 x$ for extreme values in the interval $(0,2 \pi)$.

Solution: Given that $f(x)=\sin x+\frac{1}{2 \sqrt{2}} \cos 2 x$

$$
\begin{aligned}
& f^{\prime}(x)=\cos x+\frac{1}{2 \sqrt{2}}(-2 \sin 2 x)=\cos x-\frac{1}{\sqrt{2}} \sin 2 x \\
& =\cos x \quad \frac{1}{\sqrt{2}}(2 \sin x-\cos x) \quad \cos x \quad \sqrt{2} \sin x \cos x \\
& =\cos x(1-\sqrt{2} \sin x)
\end{aligned}
$$

Now $f^{\prime}(x)=0 \quad \Rightarrow \cos x(1-\sqrt{2} \sin x)=0$

$$
\Rightarrow \cos x=0 \quad \Rightarrow x=\frac{\pi}{2} \cdot \frac{3 \pi}{2}
$$

or $\quad 1-\sqrt{2} \sin x=0 \quad \Rightarrow \sin x=\frac{1}{\sqrt{2}} \quad \Rightarrow x=\frac{\pi}{4} \cdot \frac{3 \pi}{4}$
Differentiating (i) w.r.t. ' $x$ ', we have

$$
f^{\prime \prime \prime}(*)=\sin x \quad \frac{1}{\sqrt{2}}(\cos 2 x) \cdot 2-\sin x \quad \sqrt{2} \cos 2 x
$$

As $f^{\prime \prime \prime}\left(\frac{\pi}{2}\right)=-\sin \frac{\pi}{2}-\sqrt{2} \cos \pi=-1-\sqrt{2} \times(-1)=\sqrt{2}-1>0$
and $f^{\prime \prime \prime}\left(\frac{3 \pi}{2}\right)=-\sin \frac{3 \pi}{2}-\sqrt{2} \cos 3 \pi=-(-1)-\sqrt{2}(-1)=1+\sqrt{2}>0$
Thus $f(x)$ has minimum values for $x=\frac{\pi}{2}$ and $x=\frac{3 \pi}{2}$
As $f^{\prime \prime \prime}\left(\frac{\pi}{4}\right)=\sin \frac{\pi}{4} \quad \sqrt{2} \cos \frac{\pi}{2}-\frac{1}{\sqrt{2}} \cdot \sqrt{2}<0 \quad \frac{1}{\sqrt{2}} \quad 0$
and $f^{\prime \prime \prime}\left(\frac{3 \pi}{4}\right)=\sin \frac{3 \pi}{4} \quad \sqrt{2} \cos \frac{3 \pi}{2}-\frac{1}{\sqrt{2}} \cdot \sqrt{2}<0 \quad \frac{1}{\sqrt{2}} \quad 0$
Thus $f(x)$ has minimum values for $x=\frac{\pi}{4}$ and $x=\frac{3 \pi}{4}$

## EXERCISE 2.9

1. Determine the intervals in which $f$ is increasing or decreasing for the domain mentioned in each case.
(i) $f(x)=\sin x$
; $\quad x \in(-\pi, \pi)$
(ii) $f(x)=\cos x$
; $\quad x \in\left(\frac{-\pi}{2}, \frac{\pi}{2}\right)$
(iii) $f(x)=4-x^{2}$
; $\quad x \in(-2,2)$
(iv) $f(x)=x^{2}+3 x+2$
; $\quad x \in(-4,1)$
2. Find the extreme values for the following functions defined as:
(i) $f(x)=1-x^{3}$
(ii) $f(x)=x^{2}-x-2$
(iii) $f(x)=5 x^{2}-6 x+2$
(iv) $f(x)=3 x^{2}$
(v) $f(x)=3 x^{2}-4 x+5$
(vi) $f(x)=2 x^{2}-2 x^{2}-36 x+3$

(vii) $f(x)=x^{x}-4 x^{2}$
(viii) $f(x)=(x-2)^{2}(x-1)$
(ix) $f(x)=5+3 x-x^{2}$
3. Find the maximum and minimum values of the function defined by the following equation occurring in the interval $[0.2 \pi]$
$f(x)=\sin x+\cos x$.
4. Show that $y=\frac{\ln x}{x}$ has maximum value at $x=e$.
5. Show that $y=x^{e}$ has a minimum value at $x=\frac{1}{e}$.

## Application of Maxima and Minima

Now we apply the concept of maxima and minima to the practical problems. We first form the functional relation of the form $y=f(x)$ from the given information and find the maximum or minimum value of $f$ as required. Here we solve some examples relating to maxima and minima problems.

Example 1: Find two positive integers whose sum is 9 and the product of one with the square of the other will be maximum.

Solution: Let $x$ and $9-x$ be the two required positive integers such that

$$
x(9-x)^{2} \text { will be maximum. }
$$

Let $f(x)=x(9-x)^{2}$. Then

$$
\begin{aligned}
f^{\prime}(x) & =1 \cdot(9-x)^{2}+x \cdot 2(9-x) \times(-1) \\
& =(9-x)[9-x-2 x]=(9-x)(9-3 x)=3(9-x)(3-x) \\
f^{\prime}(x) & =0 \Rightarrow 3(9-x)(3-x)=0 \Rightarrow x=9 \text { or } x=3
\end{aligned}
$$

In this case $x=9$ is not possible because

$$
\begin{aligned}
& 9-x=9-9=0 \text { which is not positive integer. } \\
& f^{\prime \prime}(x)=3 \frac{1}{(}-1)(3-x)+(9-x) \times(-1) \frac{1}{}=3 \frac{1}{}-3+x-9+x \frac{1}{}
\end{aligned}
$$

$$
=3 \frac{1}{2 x}-12 \frac{1}{}=6(x-6)
$$

As $f^{\prime \prime}(3)=6(3-6)=6(-3)=-18$ which is negative.
Thus $f(x)$ gives the maximum value if $x=3$, so the other positive integer is 6 because $9-3=6$.

Example 2: What are the dimensions of a box of a square base having largest volume if the sum of one side of the base and its height is 12 cm .

Solution: Let the length of one side of the base (in cm ) be $x$ and the height of the box (in cm ) be h , then $\mathrm{V}=x^{2} h$

It is given that $x+h=12 \quad \Rightarrow h=12-x$
Thus $\mathrm{V}=x^{2}(12-x)$ and

$$
\begin{aligned}
\frac{d V}{d x}= & 2 x(12-x)+x^{2}(-1)=24 x-3 x^{2}=3 x(8-x) \\
& \frac{d V}{d x}=0 \Rightarrow 3 x(8-x)=0 . \text { In this case } \mathrm{x} \text { cannot be zero, } \\
\text { so } \quad & 8-x=0 \Rightarrow x=8 . \\
& \frac{d^{2} V}{d x^{2}}=24-6 x \text { which is negative for } x=8
\end{aligned}
$$

Thus $V$ is maximum if $x=8(c m)$ and $h=12-8=4(c m)$
Example 3: The perimeter of a triangle is 20 centimetres. If one side is of length 8 centimetres, what are lengths of the other two sides for maximum area of the triangle?

Solution: Let the length of one unknown side (in cm ) be $x$, then the length of the other unknown side (in cm ) will be $20-x-8=12-x$.

Let $y$ denote the square of the area of the triangle, then we have

$$
\begin{aligned}
& y=10(10-8)(10-x)(10-12+x) \quad\left(1 / x-\frac{20}{2}-10 \text { and area of the triangle } \sqrt{x(x-a)(x-b)(x-c)}\right) \\
& =10.2(10-x)(x-2)=20\left(-x^{2}+12 x-20\right)
\end{aligned}
$$

$$
\begin{aligned}
& \frac{d y}{d x}=20(-2 x+12)=-40(x-6) \\
& \frac{d y}{d x}=0 \quad \Rightarrow x=6
\end{aligned}
$$

As $\frac{d^{2} y}{d x^{2}}$ is $-\mathrm{ve}, \mathrm{so} x=6$ gives the maximum area of the triangle.
The length of other unknown side $=12-6=6(\mathrm{~cm})$
Thus the lengths of the other two sides are 6 cm and 6 cm .
Example 4: An open box of rectangular base is to be made from 24 cm by 45 cm cardboard by cutting out square sheets of equal size from each corner and bending the sides. Find the dimensions of corner squares to obtain a box having largest possible volume.

Solution: Let $x$ (in cm ) be the length of a side of each square sheet to be cut off from each comer of the cardboard. Then the length and breadth of the resulting box (in cm ) will be $45-2 x$ and $24-2 x$ respectively. Obviously the height of the box (in cm ) will be $x$. Thus the volume $V$ of the box (in cubic cm ) will be given by

$$
\begin{aligned}
V & =x(24-2 x)(45-2 x)=2 x(12-x)(45-2 x) \\
& =2 x\left(540-69 x+2 x^{2}\right)
\end{aligned}
$$

and $\quad \frac{d V}{d x}=2\left[1 .\left(2 x^{2}-69 x+540\right)+x(4 x-69)\right]$

$$
\begin{aligned}
& =2\left(6 x^{2}-138 x+540\right) \\
= & 12\left(x^{2}-23 x+90\right)=12(x-5)(x-18) \\
& \frac{d V}{d x}=0 \quad \Rightarrow 12(x-5)(x-18)=0 \quad \Rightarrow x=5 \text { or } x=18 \\
& \Rightarrow x=5[\because \text { if } x=18, \text { then } 12-x=12-18=-6, \text { that is, }
\end{aligned}
$$

$V$ is negative which is not possible]
$\frac{d^{2} y}{d x^{2}}=12(2 x-23)$
$\frac{d^{2} V}{d x^{2}}$ is negative for $x=5$ because $12(2 \times 5-23)=12(-13)$
Thus V will be maximum if the length of a side of the corner square to be cut off is 5 cm .
Example 5: Find the point on the graph of the curve $y=4-x^{2}$ which is closest to the point $(3,4)$.

Solution: Let $l$ be distance between a point $(x, y)$ on the curve $y=4-x^{2}$ and the point $(3$, 4). Then $l=\sqrt{(x-3)^{2}+(y-4)^{2}}$

$$
\begin{aligned}
& =\sqrt{(x-3)^{2}+\left(4-x^{2}-4\right)^{2}} \quad\left(\because(x, y) \text { is on the curve } y=4-x^{2}\right) \\
& =\sqrt{(x-3)^{2}+x^{4}}
\end{aligned}
$$

Now we find $x$ for which $l$ is minimum.

$$
\begin{aligned}
\frac{d l}{d x} & =\frac{1}{2 \sqrt{(x-3)^{2}+x^{4}}} \cdot\left[\left(\begin{array}{lll}
2(x & 3 & 4 x^{2}
\end{array}\right)\right] \\
& =\frac{1}{2 l} \cdot 2\left(2 x^{2}+x-3\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{l}\left(2 x^{2}+x-3\right) \\
& =\frac{1}{l}(x-1)\left(2 x^{2}+x-3\right) \\
& \frac{d l}{d x}=0 \Rightarrow \frac{1}{l}(x-1)\left(2 x^{2}+2 x+3\right)=0 \Rightarrow x-1=0 \text { or } 2 x^{2}+2 x+3=0 \\
& \Rightarrow x=1 \quad\left(\because 2 x^{2}+2 x+3=0\right) \\
& l \text { is positive for } 1-\varepsilon \text { and } 1+\varepsilon \text { where } \varepsilon \text { is very very small positive real number. } \\
& \text { Also } 2 x^{2}+2 x+3=2\left(x^{2}+x+\frac{1}{4}\right)+\frac{5}{2}=2\left(x+\frac{1}{2}\right)^{2}+\frac{5}{2} \text { is positive, for } x=1-\varepsilon \\
& \text { and } x=1+\varepsilon
\end{aligned}
$$

The sign of $\frac{d l}{d x}$ depends on the factor $x-1$.
$x-1$ is negative for $x=1-\varepsilon$ because $x-1=1-\varepsilon-1=-\varepsilon \quad \ldots . .($ ii)
$x-1$ is positive for $x=1+\varepsilon$ because $x-1=1+\varepsilon-1=\varepsilon \quad \ldots .$. (ii)
From (i) and (ii), we conclude that $\frac{d l}{d x}$ changes sign from -ve to +ve at $x=1$.
Thus $l$ has a minimum value at $x=1$.
Putting $x=1$ in $y=4-x^{2}$, we get the $y$-coordinate of the required point which is $4-(1)^{2}=3$
Hence the required point on the curve is $(1,3)$.

## EXERCISE 2.10

1. Find two positive integers whose sum is 30 and their product will be maximum.
2. Divide 20 into two parts so that the sum of their squares will be minimum.
3. Find two positive integers whose sum is 12 and the product of one with the square of the other will be maximum.
4. The perimeter of a triangle is 16 centimetres. If one side is of length 6 cm , what are length of the other sides for maximum area of the triangle?
5. Find the dimensions of a rectangle of largest area having perimeter 120 centimetres.
6. Find the lengths of the sides of a variable rectangle having area $36 \mathrm{~cm}^{2}$ when its perimeter is minimum.
7. A box with a square base and open top is to have a volume of 4 cubic dm . Find the dimensions of the box which will require the least material.
8. Find the dimensions of a rectangular garden having perimeter 80 metres if its area is to be maximum.
9. An open tank of square base of side $x$ and vertical sides is to be constructed to contain a given quantity of water. Find the depth in terms of $x$ if the expense of lining the inside of the tank with lead will be least.
10. Find the dimensions of the rectangle of maximum area which fits inside the semi-circle of radius 8 cm as shown in the figure.
11. Find the point on the curve $y=x^{2}-1$ that is closest to the point $(3,-1)$.
12. Find the point on the curve $y=x^{2}+1$ that is closest to the point $(18,1)$.