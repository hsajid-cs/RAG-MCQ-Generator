### 1.6.3 Continuity of a function at a number

## (a) Continuous Function

A function $f$ is said to be continuous at a number " $c$ " if and only if the following three conditions are satisfied:
(i) $f(c)$ is defined.
(ii) $\operatorname{Lim}_{x \rightarrow c} f(x)$ exists,
(iii) $\operatorname{Lim}_{x \rightarrow c} f(x) \neq f(c)$

## (b) Discontinuous Function

If one or more of these three conditions fail to hold at " $c$ ", then the function $f$ is said to be discontinuous at " $c$ ".

Example 2: Consider the function $f(x)=\frac{x^{2}-1}{x-1}$
Solution: $\quad$ Here $f(1)$ is not defined
$\Rightarrow \quad f(x)$ is discontinuous at 1 .
Further $\quad \lim _{x \rightarrow 1} f(x)=\lim _{x \rightarrow 1} \frac{x^{2}-1}{x-1}=\lim _{x \rightarrow 1}(x+1)=2$ (finite)
Therefore $f(x)$ is continuous at any other number $x \neq 1$
Example 3: $\quad$ For $f(x)=3 x^{2}-5 x+4$, discuss continuity of $f$ at $x=1$

Solution: $\quad \lim _{x \rightarrow 2} f(x)=\lim _{x \rightarrow 2}\left(3 x^{2}-5 x+4\right)=3 \quad=5+4 \quad 2$.
and $f(1)=3-5+4=2$
$\Rightarrow \quad \lim _{x \rightarrow 2} f(x)=f(1)$
$\therefore \quad f(x)$ is continuous at $x=1$
Example 4: $\quad$ Discuss the continuity of the function $f(x)$ and $g(x)$ at $x=3$.
(a) $f(x)= \begin{cases}\frac{x^{2}-9}{x-3} & \text { if } x \neq 3 \\ 6 & \text { if } x=3\end{cases}$
(b) $g(x)=\frac{x^{2}-9}{x-3}$ if $x \neq 3$

Solution: (a) Given $f(3)=6$
$\therefore$ the function $f$ is defined at $x=3$.
Now $\lim _{x \rightarrow 3^{-}} f(x)=\lim _{x \rightarrow 3} \frac{x^{2}-9}{x-3}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 3} \frac{(x+3)(x-3)}{x-3} \\
& =\lim _{x \rightarrow 3}(x+3)=6
\end{aligned}
$$

As $\quad \lim _{x \rightarrow 3^{-}} f(x)=6=f(3)$
$\therefore f(x)$ is continuous at $x=3$

It is noted that there is no break in the graph. (See figure (i))
(b) $g(x)=\frac{x^{2}-9}{x-3}$ if $x \neq 3$

As $g(x)$ is not defined at $x=3$
$\Rightarrow g(x)$ is discontinuous at $x=3 \quad$ (See figure (ii)). It is noted that there is a break in the graph at $x=3$

Example 5: $\quad$ Discuss continuity of $f$ at 3 ,
Fig (ii)
when $f(x)= \begin{cases}x-1, & \text { if } \quad x<3 \\ 2 x+1, & \text { if } \quad 3 \leq x\end{cases}$
Solution: $\quad$ A sketch of the graph of $f$ is shown in the figure (iii). We see that there is a break in the graph at the point when $x=3$

$$
\begin{aligned}
& \text { Now } f(3)=2(3)+1=7 \\
\Rightarrow & \text { Condition (i) is satisfied. } \\
\lim _{x \rightarrow 3^{-}} f(x)=\lim _{x \rightarrow 3^{-}} f(x-1)=3-1=2 \\
\lim _{x \rightarrow 3^{-}} f(x)=\lim _{x \rightarrow 3^{-}} f(2 x+1)=6+1=7 \\
\therefore \quad \lim _{x \rightarrow 3^{-}} f(x) \neq \lim _{x \rightarrow 3^{-}} f(x) \\
& \text { i.e. condition (ii) is not satisfied } \\
\therefore \quad \lim _{x \rightarrow 3^{-}} f(x) \text { does not exist }
\end{aligned}
$$

Hence $f(x)$ is not continuous at $x=3$
Fig (iii)

# EXERCISE 1.4

1. Determine the left hand limit and the right hand limit and then, find the limit of the following functions when $x \rightarrow c$
(i) $f(x)=2 x^{2}+x-5, c=1$
(ii) $f(x)=\frac{x^{2}-9}{x-3}, \quad c=-3$
(iii) $f(x)=|x-5|, \quad c=5$

2. Discuss the continuity of $f(x)$ at $x=c$ :
(i) $f(x)=\left{\begin{array}{cccccc}2 x+5 & \text { if } & x \leq 2 \\ & & & , c=2 \\ 4 x+1 & \text { if } & x & 2\end{array}\right.$
(ii) $f(x)=\left{\begin{array}{cccccc}3 x-1 & \text { if } & x<1 \\ & 4 & \text { if } & x=1, c=1 \\ & 2 x & \text { if } & x>1\end{array}\right.$
3. If $f(x)=\left{\begin{array}{cccccc}3 x & \text { if } & x \leq-2 \\ x^{2}-1 & \text { if } & -2<x<2 \\ & 3 & \text { if } & x \geq 2\end{array}\right.$
Discuss continuity at $x=2$ and $x=-2$
4. If $f(x)=\left{\begin{array}{llllll}x+2 & , & x \leq-1 & \text {, } & \text { find " } c \text { " so that } \frac{\text { Lim }}{c+2}, f(x) \text { exists. } \\ c+2 & , & x>-1\end{array}\right.$
5. Find the values $m$ and $n$, so that given function $f$ is continuous at $x=3$.
(i) $f(x)=\left\{\begin{array}{cccccc}m x & \text { if } & x<3 \\ n & \text { if } & x=3 \\ -2 x+9 & \text { if } & x>3\end{array}\right.$ (ii) $f(x)=\left\{\begin{array}{cccc}m x & \text { if } & x<3 \\ x^{2} & \text { if } & x \geq 3\end{array}\right.$
6. If $f(x)=\left\{\begin{array}{cc}\frac{\sqrt{2 x+5}-\sqrt{x+7}}{x-2}, & x \neq 2 \\ \mathrm{k} & , & x=2\end{array}\right.$

Find value of $k$ so that $f$ is continuous at $x=2$.

# 1.7 Graphs

We now learn the method to draw the graphs of the Explicit Functions like $y=f(x)$, where $f(x)=a^{x}, e^{x}, \log _{a} x$, and $\log _{e} x$.