### 13.3.2 Finding $f^{\prime}(x)$ by Definition of Derivative

Given a function $f$, then $f^{\prime}(x)$ if it exists, can be found by the following four steps:
Step I: Find $f(x+\delta x)$
Step II: Simplify $f(x+\delta x)-f(x)$
Step III: Divide $f(x+\delta x)-f(x)$ by $\delta x$ to get $\frac{f(x+\delta x)-f(x)}{\delta x}$ and simplify it.
Step IV: Find $\operatorname{Lim}_{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}$
The method of finding derivatives by this process is called differentiation by definition or by ab-initio or from first principle.

Example 3 Find the derivative of the following functions by definition
(a) $f(x)=c$
(b) $f(x)=x^{2}$

Solution
(a) $f(x)=c$
(i) $f(x+\delta x)=c$
(ii) $f(x+\delta x)-f(x)=c-c=0$
(iii) $\frac{f(x+\delta x)-f(x)}{\delta x}=\frac{0}{\delta x}=0$
(iv) $\operatorname{Lim}_{k \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}=\operatorname{Lim}_{k \rightarrow-0}(0)=0$

Thus, $f^{\prime}(x)=0$, that is, $\frac{d}{d x}(c)=0$
(b) $f(x)=x^{2}$
(i) $f(x+\delta x)=(x+\delta x)^{2}$
(ii) $f(x+\delta x)-f(x)=(x+\delta x)^{2}-x^{2}=x^{2}+2 x \delta x+(\delta x)^{2}-x^{2}=(2 x+\delta x) \delta x$
(iii) $\frac{f(x+\delta x)-f(x)}{\delta x}=\frac{(2 x+\delta x) \delta x}{\delta x}=2 x+\delta x ;(\delta x \neq 0)$
(iv) $\operatorname{Lim}_{k \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}=\operatorname{Lim}_{k \rightarrow 0}(2 x+\delta x)=2 x$
i.e., $\quad f^{\prime}(x)=2 x$

Example 4 Find the derivative of $\sqrt{x}$ at $x=a$ from first principle.
Solution If $f(x)=\sqrt{x}$, then
(i) $f(x+\delta x)=\sqrt{x+\delta x}$ and
(ii) $f(x+\delta x)-f(x)=\sqrt{x+\delta x}-\sqrt{x}$

$$
=\frac{(\sqrt{x+\delta x}-\sqrt{x})(\sqrt{x+\delta x}+\sqrt{x})}{\sqrt{x+\delta x}+\sqrt{x}} \quad \text { (rationalizing the } \text { numerator })
$$

$$
=\frac{x+\delta x-x}{\sqrt{x+\delta x}+\sqrt{x}}
$$

i.e., $f(x+\delta x)-f(x)=\frac{\delta x}{\sqrt{x+\delta x}+\sqrt{x}}$
(iii) Dividing both sides of (1) by $\delta x$, we have

$$
\begin{aligned}
\frac{f(x+\delta x)-f(x)}{\delta x} & =\frac{\delta x}{\delta x(\sqrt{x+\delta x}+\sqrt{x})} \\
& =\frac{1}{\sqrt{x+\delta x}+\sqrt{x}},(\delta x \neq 0)
\end{aligned}
$$

(iv) Taking limit of both the sides as $\delta x \rightarrow 0$, we have

$$
\lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}=\operatorname{Lim}_{\delta x \rightarrow 0}\left(\frac{1}{\sqrt{x+\delta x}+\sqrt{x}}\right)
$$

i.e., $\quad f^{\prime}(x)=\frac{1}{\sqrt{x}+\sqrt{x}}=\frac{1}{2 \sqrt{x}},(x>0)$ and $f^{\prime}(a)=\frac{1}{2 \sqrt{a}}$

Alternate method: Putting $x=a$ in $f(x)=\sqrt{x}$, gives $f(a)=\sqrt{a}$

$$
\text { So, } \quad f(x)-f(a)=\sqrt{x}-\sqrt{a}
$$

Using alternative form for the definition of the derivative, we have

$$
\begin{aligned}
\frac{f(x)-f(a)}{x-a} & =\frac{\sqrt{x}-\sqrt{a}}{x-a} \\
& =\frac{(\sqrt{x}-\sqrt{a})(\sqrt{x}+\sqrt{a})}{(x-a)(\sqrt{x}+\sqrt{a})} \quad \text { (rationalizing the numerator) } \\
& =\frac{x-a}{(x-a)(\sqrt{x}+\sqrt{a})}=\frac{1}{\sqrt{x}+\sqrt{a}},(x \neq a)
\end{aligned}
$$

Taking limit of both the sides of (2) as $x \rightarrow a$, gives

$$
\lim _{x \rightarrow \infty} \frac{f(x)-f(a)}{x-a}=\operatorname{Lim}_{x \rightarrow a} \frac{1}{\sqrt{x}+\sqrt{a}}=\frac{1}{\sqrt{a}+\sqrt{a}}
$$

i.e.,

$$
f^{\prime}(a)=\frac{1}{2 \sqrt{a}}
$$

which is the gradient of $f$ at $x=a$.
Example 5 If $y=\frac{1}{x^{2}}$, then find $\frac{d y}{d x}$ at $x=-1$ by ab-initio method.
Solution Here, $y=\frac{1}{x^{2}}$, so

$$
y+\delta y=\frac{1}{(x+\delta y)^{2}}
$$

Subtracting (i) from (ii), we get

$$
\begin{aligned}
\delta y & =\frac{1}{(x+\delta x)^{2}}-\frac{1}{x^{2}}=\frac{x^{2}-(x+\delta x)^{2}}{x^{2}(x+\delta x)^{2}} \\
& =\frac{\{x+(x+\delta x)\}\{x-(x+\delta x)\}}{x^{2}(x+\delta x)^{2}}
\end{aligned}
$$

$$
=\frac{(2 x+\delta x)(-\delta x)}{x^{2}(x+\delta x)^{2}}=\frac{-\delta x(2 x+\delta x)}{x^{2}(x+\delta x)^{2}}
$$

Dividing both sides of (iii) by $\delta x$, we have

$$
\frac{\delta y}{\delta x}=\frac{-\delta x(2 x+\delta x)}{x^{2}(x+\delta x)^{2} \cdot \delta x}=\frac{-(2 x+\delta x)}{x^{2}(x+\delta x)^{2}}, \quad(\delta x \neq 0)
$$

Taking limit as $\delta x \rightarrow 0$, gives

$$
\begin{aligned}
\lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x} & =\lim _{\delta x \rightarrow 0} \frac{-(2 x+\delta x)}{x^{2}(x+\delta x)^{2}} \\
& =\frac{-(2 x)}{x^{2}\left(x^{2}\right)} \quad \text { (Using quotient theorem of limits) }
\end{aligned}
$$

i.e., $\frac{d y}{d x}=\frac{-2}{x^{3}}$ and $\left.\frac{d y}{d x}\right|_{x=-1}=\frac{-2}{(-1)^{3}}=\frac{-2}{-1}=2$

# 13.4 Derivation of $x^{n}$ where $n \in Z$

(a) We find the derivative of $x^{n}$ when $n$ is positive integer.
(b) Let $y=x^{n}$. Then

$$
y+\delta y=(x+\delta y)^{n}
$$

and $\quad \delta y=(x+\delta x)^{n}-x^{n}$
Using the binomial theorem, we have

$$
\begin{aligned}
& \delta y=\left[x^{n}+n x^{n-1} \cdot \delta x+\frac{n(n-1)}{2!} x^{n-2}(\delta x)^{2}+\cdots+(\delta x)^{n}\right]-x^{n} \\
& \text { i.e., } \quad \delta y=\delta x\left[n x^{n-1}+\frac{n(n-1)}{2!} x^{n-2} \cdot \delta x+\cdots+(\delta x)^{n-1}\right]
\end{aligned}
$$

Dividing both sides of (i) by $\delta x$, gives

$$
\frac{\delta y}{\delta x}=n x^{n-1}+\frac{n(n-1)}{2!} x^{n-2} \cdot \delta x+\cdots+(\delta x)^{n-1}
$$

Note that each term on the right hand side of (ii) involves $\delta x$ except the first term, so taking the limit as $\delta x \rightarrow 0$, we get $\frac{d y}{d x}=n x^{n-1}$

$$
\text { As } y=x^{n} \text {, so } \frac{d}{d x}\left(x^{n}\right)=n \cdot x^{n-1}
$$

(b) Let $y=x^{n}$ where $n$ is negative integer.

Let $n=-m$ ( $m$ is a positive integer). Then

$$
\begin{aligned}
y=x^{-m} & =\frac{1}{x^{m}} \\
\text { and } y+\delta y & =\frac{1}{(x+\delta x)^{m}}
\end{aligned}
$$

Subtracting (i) from (ii), gives

$$
\begin{aligned}
\delta y & =\frac{1}{(x+\delta x)^{m}}-\frac{1}{x^{m}}=\frac{x^{m}-(x+\delta x)^{m}}{x^{m}(x+\delta x)^{m}} \\
& =\frac{x^{m}-\left[x^{m}+m x^{m-1} \delta x+\frac{m(m-1)}{2!} x^{m-2}(\delta x)^{2}+\ldots \pm(\delta x)^{m}\right]}{x^{m}(x+\delta x)^{m}}
\end{aligned}
$$

(expanding $(x+\delta x)^{m}$ by binomial theorem)

$$
=-\delta x \frac{\left(m x^{m-1}+\frac{m(m-1)}{2!} x^{m-2} \delta x+\cdots+(\delta x)^{m-1}\right)}{x^{m}(x+\delta x)^{m}}
$$

and

$$
\frac{\delta y}{\delta x}=\frac{-1}{x^{m}(x+\delta x)^{m}} \cdot\left(m x^{m-1}+\frac{m(m-1)}{2!} x^{m-2} \cdot \delta x+\cdots+(\delta x)^{m-1}\right)
$$

Taking limit when $\delta x \rightarrow 0$, we get

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{-1}{x^{m} \cdot x^{m}} \cdot m x^{m-1} \text { (all terms contaning } \delta x \text { vanish) } \\
& =-m x^{m-1} \cdot x^{-2 m} \\
& =-m x^{(-m)-1} \\
& \frac{d x}{d x}=n x^{n-1} \quad[\because-m=n] \\
& \text { or } \quad \frac{d(x)}{d x}=n x^{n-1}
\end{aligned}
$$

$$
\begin{aligned}
& \text { [1:- } m=n \text { ] } \\
& \text { So, we have proved that } \frac{d}{d x}\left(x^{n}\right)=n x^{n-1} \text {, if } n \in Z
\end{aligned}
$$

The above rule also holds if $n \in Q-Z$, i.e. for rational powers.
For example, $\frac{d}{d x}\left(x^{\frac{2}{3}}\right)=\frac{2}{3} x^{\frac{2}{3}-1}=\frac{2}{3 x^{\frac{1}{3}}}$
The proof of $\frac{d}{d x}\left(x^{n}\right)=n x^{n-1}$ when $n \in Q-Z$ is left as an exercise.

# 13.5 Connection Between Derivatives and Continuity

Calculus is a powerful branch of mathematics that allows us to study change and motion. Two of its foundational concepts of continuity and derivatives are deeply connected. While each concept has its own definition and application, understanding how they relate to each other is essential for solving real-world problems in mathematics.
As discussed in previous units, a function is continuous at a point if its graph has no breaks, jumps, or holes at that point. On the other hand, the derivative of a function at a point measures the instantaneous rate of change or equivalently, the slope of the tangent line at that point. However, this definition depends on the function being wellbehaved around the point. This leads to a well-known result:
If a function is differentiable at a point, it must also be continuous there. This means that differentiability implies continuity, but the reverse is not necessarily true. For example, consider the function $f(x)=|x|$, clearly this function is continuous at $x=0$ (see Figure 13.3). Now we check the differentiability of $f(x)=|x|$ at $x=0$.

$$
\begin{aligned}
f(x) & =|x| \\
f(0) & =|0|=0 \text { and } \\
f(0+\delta x) & =|0+\delta x|=|\delta x| \\
f(0+\delta x)-f(0) & =|\delta x|-0 \\
f(0+\delta x)-f(0) & =|\delta x| \\
& =\frac{|\delta x|}{\delta x}
\end{aligned}
$$

so

$$
f^{\prime}(x)=\lim _{\delta x \rightarrow 0} \frac{\delta x}{\delta x}
$$

Thus $f^{\prime}(x)=\lim _{\delta x \rightarrow 0} \frac{\delta x}{\delta x}$
Because $|\delta x|=\delta x$ when $\delta x>0$
and $|\delta x|=-\delta x$ when $\delta x<0$,
Figure 13.3
so, we consider one-sided limits
$\operatorname{Lim}_{\delta x \rightarrow 0} \frac{|\delta x|}{\delta x}=\operatorname{Lim}_{\delta x \rightarrow 0} \frac{\delta x}{\delta x}=1$ and $\operatorname{Lim}_{\delta x \rightarrow 0} \frac{|\delta x|}{\delta x}=\operatorname{Lim}_{\delta x \rightarrow 0} \frac{-\delta x}{\delta x}=-1$
The right hand and left hand limits are not equal, therefore, the $\operatorname{Lim}_{\delta x \rightarrow 0} \frac{\delta x}{\delta x}$ does not exist. This implies that derivative of $f$ at $x=0$ does not exist, and thus, there is no tangent line to the graph of $f$ at this point (see Figure 13.3). However, the derivative exists at all other points of $f$ i.e., it is 1 on the right side and -1 on the left side. A function can be continuous at a point but not necessarily differentiable there.

# EXERCISE 13.1

1. Find by definition, the derivatives w.r.t. ' $x$ ' of the following functions defined as:
(i) $2 x^{2}+1$
(ii) $2-\sqrt{x}$
(iii) $\frac{1}{\sqrt{x}}$
(iv) $x(x-3)$
2. Find $\frac{d y}{d x}$ from first principle and find gradient of the curve at the given point:
(i) $\sqrt{x+2}$ at $x=6$
(ii) $\frac{1}{\sqrt{x+a}}$ at $x=a$
3. (i) Find the derivative of $x^{2}$ at $x=8$ from the first principle.
(ii) Find the derivative of $x^{2}+2 x+3$ by definition.
4. Find from first principle, the derivatives of the following expressions w.r.t. their respective independent variables:
(i) $(3 x-2)^{2}$
(ii) $(2 t+3)^{3}$
(iii) $(a w+b)^{7}$
5. Find the gradient and equation of the tangent line to $y=3 x^{2}-4 x+1$ at $x=2$.
6. For the function $f(x)=2 x^{2}+x$, calculate the equation of the tangent line at $x=-1$.
7. Find the coordinates of the point of tangency and the equation of the tangent line for $f(x)=x^{3}-2 x+1$ at $x=1$.
8. Find the gradient of the curve $f(x)=3 x^{2}+2 x$ at $x=1$.
9. Find the gradient and an equation of tangent line to the graph of $f(x)=\sqrt{x}$ at $x=9$
10. The position of a car after $t$ hours is given by: $s(t)=2 t^{2}-3 t^{2}+t$ (in kilometres)
(i) Find the average velocity over the interval $[1,4]$
(ii) Find the instantaneous velocity at $t=2$
11. A stone is thrown upwards and its height after $t$ seconds is given by: $s(t)=-16 t^{2}+32 t+10$ (in feet), Find the instantaneous velocity at $t=1$
12. The outdoor temperature (in ${ }^{\circ} \mathrm{C}$ ) over time is modeled by: $T(t)=-t^{2}+12 t+10$, where $t$ is the time in hours. Find the instantaneous rate of change at $t=2$.