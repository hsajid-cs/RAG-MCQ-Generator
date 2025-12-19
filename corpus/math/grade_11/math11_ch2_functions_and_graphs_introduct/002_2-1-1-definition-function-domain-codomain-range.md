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