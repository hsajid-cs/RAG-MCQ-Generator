# Chapter
# 2

## Functions and Graphs

## INTRODUCTION

Functions are of fundamental importance in mathematics, describing relationships between inputs and outputs through a rule of correspondence. Understanding key concepts such as domain, co-domain and range is essential for analyzing different types of functions, including one-to-one, onto and bijective functions. Graphical representation helps in identifying intersecting points, such as where a linear function meets the coordinate axes, where two linear functions intersect or where a linear and a quadratic function cross. These intersections provide valuable insights into solving equations visually. Additionally, exploring square root and cube root function graphs allows for a deeper understanding of their unique properties and behaviour. This unit will enhance problem-solving skills by combining algebraic and graphical approaches to functions.

### 2.1 Concept of Function

The term function was recognized by a German Mathematician Leibniz (1646-1716) to describe the dependence of one quantity on another. The following examples illustrate how this term is used:
(i) The area $A$ of a square depends on one of its sides $x$ by the formula $A=x^{2}$, so we say that $A$ is a function of $x$.
(ii) The volume " $V$ " of a sphere depends on its radius $r$ by the formula $V=\frac{4}{3} \pi r^{3}$, so we say that $V$ is a function of $r$.
A function is a rule of correspondence, relating two sets in such a way that each element in the first set corresponds to one and only one element in the second set.
Thus in, (i) above, a square of a given side has only one area and in, (ii) above, a sphere of a given radius has only one volume.
Now we have a formal definition:

### 2.1.1 Definition (Function, Domain, Codomain, Range)

A function $f$ from a set $X$ to a set $Y$ is a rule of a correspondence that assigns to each element $x$ in $X$ a unique element $y$ in $Y$. The set $X$ is called the domain of $f$.
The set of corresponding elements $y$ in $Y$ is called the range of $f$. While the codomain of a function is the set $Y$ in which function's output values (range) lie.
Unless stated to the contrary, we shall assume hereafter that the set $X$ and $Y$ consist of real numbers.

Note Co-domain is the set of all possible outputs but the range is the actual set of outputs produced by the function under the given domain that is range set is always a subset of co-domain.

# 2.1.2 Notation and Value of a Function

If a variable $y$ depends on a variable $x$ in such a way that each value of $x$ determines exactly one value of $y$, then we say that " $y$ is a function of $x$ ".
Swiss mathematician Euler (1707 - 1783) invented a symbolic way to write the statement " $y$ is a function of $x$ " as $y=f(x)$, which is read as " $y$ is equal to $f$ of $x$ ".
A function can be thought as a computing machine $f$ that takes an input $x$, operates on it in some way and produces exactly one output $f(x)$. This output $f(x)$ is called the value of $f$ at $x$ or image of $x$ under $f$.
The output $f(x)$ is denoted by a single letter, say $y$ and we write $y=f(x)$.
The variable $x$ is called the independent variable of $f$ and the variable $y$ is called the dependent variable of $f$. For now onward we shall only consider the function in which the variables are real numbers and we say that $f$ is a real valued function of real numbers.
Example 1 Given $f(x)=x^{3}-2 x^{2}+4 x-1$, find:
(i) $f(0)$
(ii) $f(1)$
(iii) $f(-2)$
(iv) $f(1+x)$
(v) $f\left(\frac{1}{x}\right), x \neq 0$

Solution $f(x)=x^{3}-2 x^{2}+4 x-1$
(i) $f(0)=0-0+0-1=-1$
(ii) $f(1)=(1)^{3}-2(1)^{2}+4(1)-1=1-2+4-1=2$
(iii) $f(-2)=(-2)^{3}-2(-2)^{2}+4(-2)-1=-8-8-8-1=-25$
(iv) $f(1+x)=(1+x)^{3}-2(1+x)^{2}+4(1+x)-1$

$$
\begin{aligned}
& =1+3 x+3 x^{2}+x^{3}-2-4 x-2 x^{2}+4+4 x-1 \\
& =x^{3}+x^{2}+3 x+2
\end{aligned}
$$

(v) $f\left(\frac{1}{x}\right)=\left(\frac{1}{x}\right)^{3}-2\left(\frac{1}{x}\right)^{2}+4\left(\frac{1}{x}\right)-1=\frac{1}{x^{2}}-\frac{2}{x^{2}}+\frac{4}{x}-1, x \neq 0$

Example 2 Find the domain and range of $f(x)=x^{2}$.
Solution For every real number $x, f(x)=x^{2}$ is a non-negative real number. So, Domain $f=$ set of all real numbers ; Range $f=$ set of all non-negative real numbers.

Example 3 Find the domain and range of $f(x)=\frac{x}{x^{2}-4}$.
Solution At $x=2$ and $x=-2, f(x)=\frac{x}{x^{2}-4}$ is not defined. So,
Domain $f=$ set of all real numbers except -2 and 2 or $R-\{-2,2\}$
Let $y=\frac{x}{x^{2}-4} \Rightarrow y\left(x^{2}-4\right)=x \Rightarrow x^{2} y-4 y=x$

$$
\begin{aligned}
x^{2} y-x-4 y & =0 \\
x & =\frac{-(-1) \pm \sqrt{(-1)^{2}-4(y)(-4 y)}}{2 y} \\
x & =\frac{1 \pm \sqrt{1+16 y^{2}}}{2 y}, y \neq 0
\end{aligned}
$$

## Remember

There are two types of intervals known as open interval and closed interval. In an open interval $(a, b)$, the endpoints are not included. In a closed interval $[a, b]$, the endpoints are included.

Clearly $x$ is defined for all $y \neq 0$

$$
\text { For } y=0 \text {, we have } 0=\frac{x}{x^{2}-4} \Rightarrow x=0
$$

This is $f(0)=0$
So, range $f=$ set of all real numbers or $(-\infty, \infty)$
Example 4 Find the domain and range of $f(x)=\sqrt{x^{2}-9}$.
Solution As square root of a negative number is not a real number, therefore $x^{2}-9 \geq 0$
(i)

Let $x^{2}-9=0 \Rightarrow x= \pm 3$
Critical points divide the number line into three regions:
Put $x=-4$ in (i), $16-9 \geq 0$ (True)
Put $x=0$ in (i), $0-9 \geq 0$ (False)
Put $x=4$ in (i), $16-9 \geq 0$ (True)
So, domain $f \doteq(-\infty,-3] \cup[3, \infty)$
The smallest value of $x^{2}-9$ is 0 (when $x= \pm 3$ ).
$\Rightarrow y=\sqrt{x^{2}-9}=\sqrt{0}=0$
As $|x|$ increases beyond $3, x^{2}-9$ grows to $+\infty$, so $y$ grows to $+\infty$.
So, range $f=[0, \infty)$

# 2.1.3 Vertical Line Test

The vertical line test is a method used to determine whether a graph represents a function. A graph represents a function if and only if no vertical line intersects the graph more than once. If any vertical line passes through the graph more than once, it is not a function.

Explanation is given in the following figure.
# 2.1.4 Types of Function

## (i) One-to-One (Injective) Function

A function $f: x \rightarrow y$ is one-to-one if different inputs produce different outputs, that is if $f\left(x_{1}\right)=f\left(x_{2}\right)$ implies $x_{1}=x_{2}$. This means that no two different elements of the domain map to the same element of the co-domain.
For example, $f(x)=5 x+7$ is one-to-one because if $5 x_{1}+7=5 x_{2}+7$ implies $x_{1}=x_{2}$.

## (ii) Onto (Surjective) Function

A function $f: X \rightarrow Y$ is called onto (or surjective) function if every element in the co-domain $Y$ has at least one pre-image in the domain $X$. In other words, for every $y$ in $Y$, there exists an $x$ in $X$ such that $f(x)=y$.
For example, $f(x)=2 x+3$, where the domain and co-domain are both real numbers.
Here $y=2 x+3 \Rightarrow x=\frac{y-3}{2}$. Here for each $y$ in $R$, there exists $\frac{y-3}{2}$ in $R$ such that $f\left(\frac{y-3}{2}\right)=y$. Hence $f$ is an onto function.

## (iii) Bijective Function

A function $f: X \rightarrow Y$ is called bijective if it is both one-to-one and onto.
Piecewise Function
A piecewise function is a function that is defined by different expressions (or "pieces") over different intervals of its domain. Each piece applies to a specific part of the domain.
For example, $\quad f(x)=\left\{\begin{array}{l}2 x+1 \text { if } x<0 \\ x^{2}-1 \text { if } x \geq 0\end{array}\right.$
For $x<0$, the function behaves as $2 x+1$ and for $x \geq 0$, it behaves as $x^{2}-1$
Example 5 Show that the function $f(x)=x+1$, where the domain and co-domain are all real numbers, is bijective.
Solution A function is bijective if it is both one-to-one and onto.
A function is one-to-one if $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow x_{1}=x_{2}$ for $f(x)=x+1$
Suppose $f\left(x_{1}\right)=f\left(x_{2}\right)$

$$
\begin{aligned}
& \Rightarrow \quad x_{1}+1=x_{2}+1 \\
& \Rightarrow \quad x_{1}=x_{2}
\end{aligned}
$$

So, the given function is one-to-one.
It is also onto because for every real number $y$, there is a real number $x$ (specifically $x=y-1$ ) such that $f(y-1)=y-1+1=y$. Hence, $f(x)$ is bijective.
Exemple 6 Show that the function $f(x)=x^{2}-2$, where the domain and co-domain are all real numbers, is neither one-to-one nor onto.
Solution As $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow x_{1}^{2}-2=x_{2}^{2}-2 \Rightarrow x_{1}^{2}=x_{2}^{2}$
Taking square root, we get $x_{1}=x_{2}$ or $x_{1}=-x_{2}$
This does not imply that $x_{1}=x_{2}$, for example $x_{1}=2, x_{2}=-2 \Rightarrow x_{1} \neq x_{2}$ and $f(2)=2=f(-2)$.
Thus, $f$ is not one-to-one.
Also, the element -2 in the co-domain $R$ is the smallest value that $f(x)=x^{2}-2$ can attain, and it is only achieved when $x=0$. However, any number less than -2 (in co-domain $R$ ) is not the image of any real number $x$ in domain $R$. For example, $f(x)=-3 \Rightarrow x^{2}-2=-3$ has no
real root. Hence, $f(x)$ is nether one-to-one nor onto.

# EXERCISE 2.1

1. Given that:
(a) $f(x)=x^{2}-1$
(b) $f(x)=\sqrt{2 x+3}$
Find:
(i) $f(-3)$
(ii) $f(0)$
(iii) $f(x-2)$
(iv) $f\left(x^{2}+3\right)$
2. Find $\frac{f(a+h)-f(a)}{h}$ and simplify where,
(i) $f(x)=4 x+7$
(ii) $f(x)=\sin x$
(iii) $f(x)=x^{3}+x^{2}-1$
(iv) $f(x)=\tan x$

3. Express the following:
(a) The area $A$ of a square as a function of its perimeter $P$.
(b) The circumference $C$ of a circle as a function of its area $A$.
(c) The surface area $S$ of a cube as a function of its volume $V$.
4. Find the domain and the range of the function $g$ defined below:
(i) $g(x)=5-x$
(ii) $g(x)=\sqrt{x+2}$
(iii) $g(x)= \begin{cases}6 x+7, & x \leq-2 \\ 4-3 x, & x>-2\end{cases}$
(iv) $g(x)=|x-5|$
(v) $g(x)=\frac{x+2}{3-x}$
5. Given $f(x)=x^{3}-a x^{2}+b x+1$. If $f(2)=-3$ and $f(-1)=0$. Find the values of $a$ and $b$.
6. A stone falls from a height of 60 m on the ground, the height $h$ after $x$ seconds is approximately given by $h(x)=40-10 x^{2}$.
(i) What is the height of stone when:
(a) $x=1 \mathrm{sec}$ ?
(b) $x=1.5 \mathrm{sec}$ ?
(c) $x=1.7 \mathrm{sec}$ ?
(ii) When does the stone strike the ground?
7. Consider the function $f(x)=3 x-5$.
(i) Determine the domain and range of $f(x)$.
(ii) Is the function $f$ one-to-one? Justify your answer.
(iii) Is the function $f$ onto if the co-domain is all real numbers? Explain.
8. Let $f: R \rightarrow R$ be defined by $f(x)=\frac{2 x-3}{x+1}$.
(i) Find the domain and range of $f(x)$. (ii) Determine whether $f(x)$ is onto.
(iii) Prove that $f(x)$ is one-to-one.
9. Consider the function $f: \mathrm{R}^{+} \rightarrow \mathrm{R}^{+}$defined by $f(x)=e^{-x}$. Show that $f(x)$ is a bijective.
10. Let $g: R \rightarrow R$ be given by $g(x)=x^{3}-3 x$. Determine if $g(x)$ is injective and/or surjective.

# 2.2 Finding the Intersecting Point(s) Graphically

The point of intersection is a point where two or more graphs meet on the coordinate plane. This point represents the solution to the equation of the given function.

### 2.2.1 Intersection of a Linear Function and Coordinate Axes

As we know that linear function is a function in which the highest power of the variable is one. While the coordinate axes refers to $x$-axis and $y$-axis in the Cartesian coordinate system.

Example 7 Find the points of intersection of a linear function $y=2 x+6$ and coordinate axes graphically.
Solution Table of values of $y=2 x+6$ are given below:

| $x$ | $y=2 x+6$ |
| :--: | :--: |
| -1 | 4 |
| 0 | 6 |
| 1 | 8 |

Hence, from the above graph, the points $(-3,0)$ and $(0,6)$ are the points of intersection of $y=2 x+6$ and coordinate axes.

# 2.2.2 Intersection of Two Linear Functions

The point of intersection of two linear functions is the point where their graphs cross each other. This means the two functions have the same $x$ and $y$ values at that point.
Example 8 Find the point of intersection of $y=3 x+2$ and $y=-x+6$ graphically.
Solution Table of different values of $x$ and $y$ is given below:

| $x$ | $y=3 x+2$ | $y=-x+6$ |
| :--: | :--: | :--: |
| -1 | -1 | 7 |
| 0 | 2 | 6 |
| 1 | 5 | 5 |

By plotting the above points, we see that $(1,5)$ is the point of intersection of both the straight lines as shown in figure.
### 2.2.3 Intersection of a Linear Function and a Quadratic Function

A line and a parabola can either intersect at two points, one point or not as intersect at all. If there are two solutions, the system has two points of intersection. A single solution indicates that there is only one intersection point, suggesting that the line may be tangent to the parabola. If no solution exists, it means the line and the

parabola do not intersect.
Example 9 Solve the linear function $y=-x+3$ and quadratic function $y=x^{2}-6 x+3$ graphically.
Solution Clearly $(3,0)$ and $(0,3)$ are the $x$-intercept and $y$-intercept respectively of $y=-x+3$.

$$
y=x^{2}-6 x+3
$$

Put $x=0$ in (i), so $(0,3)$ is the $y$-intercept.
Put $y=0$ in (i), we have

$$
\begin{aligned}
0 & =x^{2}-6 x+3 \\
x & =\frac{-(-6) \pm \sqrt{(-6)^{2}-4(1)(3)}}{2(1)} \\
& =\frac{6 \pm \sqrt{36-12}}{2}=\frac{6 \pm \sqrt{24}}{2} \\
& =\frac{6 \pm 2 \sqrt{6}}{2}=3 \pm \sqrt{6} \\
& =3-\sqrt{6}, 3+\sqrt{6}=0.6,5.4
\end{aligned}
$$

So $(0.6,0)$ and $(5.4,0)$ are the $x$-intercepts.
Now we find vertex $(h, k)$ of the parabola

$$
\begin{aligned}
& h=-\frac{b}{2 a}=-\frac{-6}{2(1)}=3 \\
& k=(3)^{2}-6(3)+3=-6
\end{aligned}
$$

So, the vertex is $(3,-6)$.
Hence $(0,3)$ and $(5,-2)$ are the solutions (points of intersection) of the given functions.

# 2.3 Graph of the Square Root Function

Example 10 Graph the square root function $y=2 \sqrt{x}+1$
Solution Clearly the domain of $y=2 \sqrt{x}+1$ is $x \geq 0$, as the square root of a negative number is not a real number. The range of $y=2 \sqrt{x}+1$ is $y \geq 1$,
Table of values and the graph of the function are given below:

| $\boldsymbol{x}$ | $\boldsymbol{y}=\mathbf{2} \sqrt{\boldsymbol{x}}+\mathbf{1}$ |
| :--: | :--: |
| 0 | 1 |
| 1 | 3 |
| 2 | 3.8 |
| 3 | 4.5 |
| 4 | 5 |
| 5 | 5.5 |
| 6 | 5.9 |
| 7 | 6.3 |
| 8 | 6.7 |
| 9 | 7 |
| 10 | 7.3 |

### 2.4 Graph of the Cube Root Function

Example 11 Graph the cube root function $y=\sqrt[3]{x-1}$
Solution Table of values and the graph of the function are given below:

| $\boldsymbol{x}$ | $\boldsymbol{y}=\sqrt[3]{\boldsymbol{x}-1}$ |
| :--: | :--: |
| -5 | $-1.8$ |
| -4 | $-1.7$ |
| -3 | $-1.6$ |
| -2 | $-1.4$ |
| -1 | $-1.3$ |
| 0 | -1 |
| 1 | 0 |
| 2 | 1 |
| 3 | 1.3 |
| 4 | 1.4 |
| 5 | 1.6 |

# 2.5 Real Life Applications

## Growth and Decay in Finance (Predicting Long-Term Stock Prices)

When something increases in quantity or size over time, it is called growth. For example, money in a bank account earning interest (it grows larger), a population of rabbits is increasing over months.
When something decreases in quantity or size over time, it is called decay. For example, a radioactive substance is losing its strength over years, a cup of hot coffee is cooling down over time.
Example 12 The value of a stock follows the exponential growth model $P(t)=P_{0} e^{r t}$, where $P_{0}$ is the initial stock price, $r$ is the growth rate per year and $t$ is the time in years. Suppose a stock is currently valued at Rs. 5,000 , and it is expected to grow at a rate of $5 \%$ per year.
(i) Find the value of the stock after 10 years.
(ii) After how many years will the stock double in value?

Solution (i) The formula for the exponential growth is:

$$
P(t)=P_{0} e^{r t}
$$

Given $\quad P_{0}=5000, r=0.05(5 \%$ growth rate), and $t=10$ years.

$$
P(10)=5000 e^{0.05 \times 10}=5000 e^{0.5}
$$

Using $e^{0.5} \approx 1.6487$

$$
P(10)=5000 \times 1.6487=8244
$$

So, the value of the stock after 10 years is approximately Rs. 8244
(ii) We want to find $t$ when the stock doubles, i.e., when $P(t)=2 P_{0}$. Using the equation:

$$
2 P_{0}=P_{0} e^{r t}
$$

Dividing both sides by $P_{0}$, we have $2=e^{r t}$
Taking the natural logarithm on both sides: $\ln 2=r t$

$$
\text { and } \quad t=\frac{\ln 2}{r}
$$

$$
\begin{aligned}
& =\frac{0.6931}{0.05} \\
& =13.86
\end{aligned}
$$

So, the stock will double in value i.e., approximately 14 years.

Example 13 The concentration of a pollutant in a lake, in parts per million (ppm), decays over time according to the function

$$
C(t)=\frac{100}{\sqrt{t+1}}
$$

where $t$ is the time in days since the pollutant was introduced.
(i) What is the concentration of the pollutant after 4 days?
(ii) After how many days will the concentration drop below 10 ppm ?

Solution (i) The pollutant concentration function is $C(t)=\frac{100}{\sqrt{t+1}}$, where $t$ is the time in days.
Concentration after 4 days:

$$
\begin{aligned}
C(4) & =\frac{100}{\sqrt{4+1}} \\
& =\frac{100}{\sqrt{5}} \\
& \approx 44.72 \mathrm{ppm}
\end{aligned}
$$

The concentration after 4 days is about 44.72 ppm .
(ii) When will the concentration drop below 10 ppm ? Set $C(t)=10$ :

$$
\begin{aligned}
& 10=\frac{100}{\sqrt{t+1}} \\
& \Rightarrow \sqrt{t+1}=10 \\
& \Rightarrow \quad t+1=100 \\
& \Rightarrow \quad t=99
\end{aligned}
$$

After 99 days, the concentration will drop below 10 ppm .

# EXERCISE 2.2

1. Find the point of intersection of the coordinate axes and the following linear functions graphically:
(i) $y=-5 x+10$
(ii) $y=2 x-1$
(iii) $y=\frac{1}{2} x-3$
(iv) $y=3 x+\frac{3}{2}$
2. Find the point(s) of intersection of the following functions graphically:
(i) $f(x)=2 x+5, g(x)=-x+5$
(ii) $f(x)=3 x-2, g(x)=10-x$

(iii) $f(x)=2 x-4, g(x)=3 x-1$
(iv) $f(x)=-3 x-4, g(x)=\frac{1}{2} x+3$
(v) $f(x)=x-1, g(x)=x^{2}-4 x+3$
(vi) $f(x)=3 x+4, g(x)=x^{2}+2 x-8$
(vii) $f(x)=-2 x-1, g(x)=x^{2}-4 x$
(viii) $f(x)=-x^{2}-3 x+2, g(x)=x+6$
3. Graph the following functions:
(i) $y=\sqrt{3 x}$
(ii) $y=\sqrt{x}+5$
(iii) $y=-\frac{1}{2} \sqrt{x}$
(iv) $y=-\sqrt{x+1}+2$
(v) $y=\sqrt[3]{2 x+1}$
(vi) $y=2 \sqrt[3]{x}-3$
(vii) $y=\sqrt[3]{x^{2}+x-2}$
4. A building's height over time is modeled by $\mathrm{H}(t)=100+20 t$ which is in metres and $t$ is the time in months. The height of a growing tree nearby is given by $T(t)=50+10 t+t^{2}$.
(i) At what time will the building and tree have the same height?
(ii) What will that height be?

Sketch the graphs of both functions and determine the time when the tree will overtake the height of the building.
5. A radioactive substance has a half-life ( $h$ ) of 2 years. If the initial quantity $Q_{0}$ is 200 grams and the exponential decay function is $Q(t)=Q_{0}\left(\frac{1}{2}\right)^{t}$, then find the remaining quantity after 6 years graphically.