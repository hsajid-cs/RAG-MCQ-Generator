### 3.8.2 Initial Conditions

Differential equations occur in numerous practical problems concerning physical, biological, and social sciences.

The arbitrary constants involving the solution of different equations can be determined by the given conditions. Such conditions are called **initial value conditions**.

The general solution of differential equations in variable separable form contains only one variable. Here we shall consider those differential equations which have only one initial value condition.

Note that the general solution of differential equations of order *n* contains *n* arbitrary constants which can be determined by *n* initial value conditions.

**Example 1:** The slope of the tangent at any point of the curve is given by

$$
\frac{dy}{dx} = 2x - 2, \text{ find the equation of the curve if } y = 0 \text{ when } x = -1.
$$

**Solution:** Given that

$$
\frac{dy}{dx} = 2x - 2
$$

(i)

Equation (i) can be written as

$$
\frac{dy}{dx} = (2x - 2) \, dx
$$

(ii)

Integrating either side of (ii) gives

$$
\frac{dy}{dx} = \frac{(2x - 2)}{dx}
$$

(iii)

Applying the given condition, we have

$$
0 = (-1)^2 - 2(-1) + c \Rightarrow c = -3
$$

Thus (iii) becomes

$$
y = x^2 - 2x - 3
$$

which represents a parabola as shown in the adjoining figure.

For *c* = 0, (iii) becomes

$$
y = x^2 - 2x
$$

The graph of

$$
y = x^2 - 2x
$$

is also shown in the figure.

**Note:** The general solution represents a system of parabolas which are vertically above or below each other.

**Example 2:** Solve

$$
\frac{dy}{dx} = \frac{3}{4}x^4 + x - 3, \text{ if } y = 0 \text{ when } x = 2
$$

**Solution:** Given that

$$
\frac{dy}{dx} = \frac{3}{4}x^2 + x - 3
$$

(i)

Separating variables, we have

$$
dy = \left(\frac{3}{4}x^2 + x - 3\right) dx
$$

(ii)

Integrating either side of (ii) gives

$$
\frac{dy}{dx} = \frac{3}{4}x^2 + x - 3
$$

(iii)

We have

$$
\frac{dy}{dx} = \frac{3}{4}x^2 + x - 3
$$

We apply the initial value condition, we have

$$
0 = \frac{1}{4}(8) + \frac{1}{2}(4) - 3(2) + c
$$

$$
\frac{dy}{dx} = 6 - 2 - 2 = 2
$$

Thus (iii) becomes

$$
y = \frac{1}{4}x^3 + \frac{1}{2}x^2 - 3x + 2
$$

$$
\frac{dy}{dx} = 4y = x^2 + 2x^2 - 12x + 8
$$

**Example 3:** A particle is moving in a straight line and its acceleration is given by

$$
a = 2t - 7
$$

(i) Find *v* (velocity) in terms of *t* if *v* = 10 m/sec, when *t* = 0
(ii) Find *s* (distance) in terms of *t* if *s* = 0, when *t* = 0.

Solution: Given that $a=2 t-7$, that is

$$
\begin{aligned}
& \frac{d v}{d t}=2 t \quad 7=\left(\because a \quad \frac{d v}{d t}\right) \\
\Rightarrow & d v=(2 t-7) d t
\end{aligned}
$$

Integrating, we have

$$
\begin{aligned}
& \int d v=\int(2 t-7) d t \\
\Rightarrow & v=t^{2}-7 t+c_{1}
\end{aligned}
$$

Applying the first initial value condition, we get

$$
10=0-0+c_{1} \quad \Rightarrow \quad c_{1}=10
$$

The equation (1) becomes

$$
v=t^{2}-7 t+10 \quad \text { which is the solution of (i) }
$$

Now $\frac{d s}{d t}=t^{3}-7 t+10 \quad\left(\because v=\frac{d s}{d t}\right)$
$\Rightarrow \quad d s=\left(t^{2}-7 t+10\right) d t$
Integrating both sides of (2), we get

$$
\begin{aligned}
& \int d s=\int\left(t^{3}-7 t+10\right) d t \\
\Rightarrow & s=\frac{t^{3}}{3}-7 \frac{t^{2}}{2}+10 t+c_{2}
\end{aligned}
$$

Applying the second initial value condition, gives

$$
0=0-0+0+c_{2} \quad \Rightarrow c_{2}=0
$$

Thus is $\quad s=\frac{1}{3} t^{3}-\frac{7}{2} t^{2}+10 t \quad$ the solution of (ii)
Example 4: In a culture, bacteria increases at the rate proportional to the number of bacteria present. If bacteria are 100 initially and are doubled in 2 hours, find the number of bacteria present four hours later.

Solution: Let $p$ be the number of bacteria present at time $t$, then

$$
\frac{d p}{d t} \Rightarrow k p, \quad(k \quad 0)
$$

$$
\begin{aligned}
& \text { or } \quad \frac{1}{p} d p=k d t \quad \Rightarrow \ln p=k t+c_{1} \\
& \Rightarrow \quad p=e^{k t+c_{1}}=e^{k t} \cdot e^{c_{1}} \\
& \text { or } p \Rightarrow c e^{k t} \quad \text { (i) (where } e^{c_{1}} \quad c \text { ) }
\end{aligned}
$$

Applying the given condition, that is $p=100$ when $t=0$, we have

$$
100=c e^{100}=c \quad\left(\because e^{0}=1\right)
$$

Putting $c=100$, (i) becomes $p=100 e^{k t}$
$p$ will be 200 when $t=2$ (hours), so (ii) gives

$$
200=100 e^{2 k} \quad \Rightarrow \quad e^{2 k}=2
$$

or $2 k=\ln 2 \quad \Rightarrow k=\frac{1}{2} \ln 2$
Subsituting $\quad=-\ln 2$ in (ii), we get

$$
\begin{aligned}
& p=100 e^{\left(\frac{1}{2} \ln 2\right)} \quad \Rightarrow 100 e^{\frac{1}{2} \ln 2} \quad 100 e^{\left(\ln 2^{2}\right)} \\
& p=100\left(2^{\frac{1}{2}}\right)
\end{aligned}
$$

If $t=4$ (hours), then $p=100\left(2^{\frac{4}{2}}\right) \quad 100 \quad 4 \quad 400$.
Example 5: A ball is thrown vertically upward with a velocity of $1470 \mathrm{~cm} / \mathrm{sec}$ Neglecting air resistance, find
(i) velocity of ball at any time $t$
(ii) distance traveled in any time $t$
(iii) maximum height attained by the ball.

## Solution.

(i) Let $v$ be the velocity of the ball at any time $t$, then by Newton's law of motion, we have

$$
\begin{aligned}
& \frac{d v}{d t} \Rightarrow g \Rightarrow \quad \Rightarrow g d t \\
& \text { or } \quad \int d v=\int-g d t \quad \text { (integrating either side of (i)) } \\
& v=-g t+c_{1}
\end{aligned}
$$

Given that $v=1470(\mathrm{~cm} / \mathrm{sec})$ when $t=0$, so

$$
1470=-g(0)+c_{1} \Rightarrow c_{1}=1470
$$

Thus (ii) becomes $v=-g t+1470=1470-980 t$ (taking $g=980$ )
(ii) Let $h$ be the height of the ball at any time $t$, then

$$
\frac{d h}{d t}=1470-980 t \quad\left(\because v=\frac{d h}{d t}\right)
$$

or $\quad d h=(1470-980 t) d t$

$$
h=1470 t-980 \frac{t^{2}}{2}+c_{2}=1470 t-490 t^{2}+c_{2}
$$

$h=0$ when $t=0$, so we have

$$
0=1470 \times 0-490(0)^{2}+c_{2} \Rightarrow c_{2}=0
$$

Putting $c_{2}=0$ in (iii), we have

$$
h=1470 t-490 t^{2}
$$

(iii) The maximum height will be attained when $v=0$, that is

$$
1470-980 t=0 \quad \Rightarrow t=\frac{1470}{980}=\frac{3}{2}(\sec )
$$

Thus the maximum height attained in (cms) $=1470 \times\left(\frac{3}{2}\right)-490 \times\left(\frac{3}{2}\right)^{2}$

$$
=2205-1102.5=1102.5
$$

## EXERCISE 3.8

1. Check that each of the following equations written against the differential equation is its solution.
(i) $x \frac{d y}{d x}=1+y$
(ii) $x^{2}(2 y+1) \frac{d y}{d x}-1=0$
(iii) $y \frac{d y}{d x}-e^{2 x}=1$
(iv) $\frac{1}{x} \frac{d y}{d x}-2 y=0$
(v) $\frac{d y}{d x}=\frac{x^{2}+1}{e^{-x}}$
$\begin{array}{ll}\text { , } & y=c x-1 \\ \text {, } & y^{2}+y=c-\frac{1}{x} \\ & y^{2}=e^{2 x}+2 x+c \\ & y=c e^{x^{2}}\end{array}$
$\begin{array}{ll}\text {, } & y=\tan \left(e^{x}+c\right) \\ \text {, } & y=\tan \left(e^{x}+c\right)\end{array}$

Solve the following differential equations:
2. $\frac{d y}{d x}=-y$
3. $y d x+x d y=0$
4. $\frac{d y}{d x}=\frac{1-x}{y}$
5. $\frac{d y}{d x}=\frac{y}{x^{2}}:(y>0)$
6. $\sin y \cos \sec x \frac{d y}{d x}=1$
7. $x d y+y(x-1) d x=0$
8. $\frac{x^{2}+1}{y+1} \Rightarrow \frac{x}{y} \frac{d y}{d x} \cdot(x, y \quad 0)$
9. $\frac{1}{x} \frac{d y}{d x}=\frac{1}{2}\left(1+y^{2}\right)$
10. $2 x^{2} y \frac{d y}{d x}=x^{2}-1$
11. $\frac{d y}{d x}+\frac{2 x y}{2 y+1}=x$
12. $\left(x^{2}-y x^{2}\right) \frac{d y}{d x}+y^{2}+x y^{2}=0$
13. $\sec ^{2} x \tan y d x+\sec ^{2} y \tan x d y=0$
14. $\left(y-x \frac{d y}{d x}\right)=2\left(y^{2}+\frac{d y}{d x}\right)$
15. $1+\cos x \tan y \frac{d y}{d x}=0$
16. $y-x \frac{d y}{d x}=3\left(1+x \frac{d y}{d x}\right)$
17. $\sec x+\tan y \frac{d y}{d x}=0$
18. $\left(e^{x}+e^{-x}\right) \frac{d y}{d x}=e^{x} \quad e^{-x}$
19. Find the general solution of the equation $\frac{d y}{d x}-x=x y^{2}$ Also find the particular solution if $y=1$ when $x=0$.
20. Solve the differential equation $\frac{d y}{d t}=2 x$ given that $x=4$ when $t=0$.
21. Solve the differential equation $\frac{d x}{d t}+2 x t=0$. Also find the particular solution if $s=4 e$, when $t=0$.
22. In, a culture, bacteria increases at the rate proportional to the number of bacteria present. If bacteria are 200 initially and are doubled in 2 hours, find the number of bacteria present four hours later.
23. A ball is thrown vertically upward with a velocity of $2450 \mathrm{~cm} / \mathrm{sec}$. Neglecting air resistance, find
(i) velocity of ball at any time $t$
(ii) distance traveled in any time $t$
(iii) maximum height attained by the ball.