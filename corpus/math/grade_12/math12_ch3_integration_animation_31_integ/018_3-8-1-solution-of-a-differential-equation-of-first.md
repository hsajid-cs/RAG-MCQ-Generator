### 3.8.1 Solution of a Differential Equation of first order:

$$
\begin{aligned}
& \text { Consider the equation } \\
& y=A x^{2}+4 \\
& \text { where } A \text { is a real constant } \\
& \text { Differentiating (iii) with respect to } x \text { gives } \\
& \qquad \frac{d y}{d x}=2 A x \\
& \text { (iv) }
\end{aligned}
$$

From (iii) $A=\frac{y-4}{x^{2}}$, so putting the value of $A$ in (iv), we get

$$
\begin{aligned}
& \frac{d y}{d x}=2\left(\frac{y-4}{x^{2}}\right) x \\
\Rightarrow \quad & x \frac{d y}{d x}=2 y-8 \text { which is free of constant } A \\
\Rightarrow \quad & 2 y-x \frac{d y}{d x}=8
\end{aligned}
$$

Substituting the value of $y$ and its derivative in (v), we see that it is satisfied, that is.
$2\left(A x^{2}+4\right)-x(2 A x)=2 A x^{2}+8-2 A x^{2}=8$
which shows that (iii) is asolution of (v)
Giving a particular value to $A$. say $A=-1$. we get

$$
y=-x^{2}+4
$$

We see that (v) is satisfied if we put $y=-x^{2}+4$ and $\frac{d y}{d x}=-2 x$, so $y=-x^{2}+4$ is also a solution of (v).

For different values of $A$, (iii) represents different parabolas with vertex at $(0,4)$ and the axis along the $y$-axis. We have drawn two members of the family of parabolas.

$$
y=A x^{2}+4 \quad \text { for } \quad A=-1,1
$$

All solutions obtained from (iii) by putting different values of $A$, are called particular solutions of (v) while the solution (iii) itself is called the general solution of (v).

A solution of differential equation is a relation between the variables (not involving derivatives) which satisfies the differential equation.

Here we shall solve differential equations of first order with variables separable in the forms

$$
\frac{d y}{d x}=\frac{f(x)}{g(y)} \quad \text { or } \quad \frac{d y}{d x}=\frac{g(y)}{f(x)}
$$

Example 1: Solve the differential equation $(x-1) d x+y d y=0$
Solution: Variables in the given equation are in separable form, so integrating either terms, we have

$$
\begin{gathered}
\int(x-1) d x+\int y d y=c_{1}, \quad \text { where } c_{1} \text { is a constant } \\
\text { or }\left(\frac{x^{2}}{2}-x\right)+\frac{y^{2}}{2}=c_{1}, \quad \text { which gives }
\end{gathered}
$$

Thus the required general solution is $x^{2}+y^{2}-2 x=c, \quad$ where $c=2 c_{1}$
Example 2: Solve differential equation

$$
x^{2}(2 y+1) \frac{d y}{d x}-1=0
$$

Solution: The given differential equation can be written as

$$
x^{2}(2 y+1) \frac{d y}{d x}=1
$$

Dividing by $x^{2}$, we have $(2 y+1) \frac{d y}{d x}=\frac{1}{x^{2}}, \quad(x \neq 0)$
Multiplying both sides of (i) by $d x$, we get

$$
(2 y+1)\left(\frac{d y}{d x} d x\right)=\frac{1}{x^{2}} d x
$$

or $\quad(2 y+1) d y=\frac{1}{x^{2}} d x \quad\left(\because \frac{d y}{d x} d x=d y\right)$
Integrating either side gives

$$
\int(2 y+1) d y=\int \frac{1}{x^{2}} d x
$$

or $\quad y^{2}+y=-\frac{1}{x}+c \quad\left(\because \int x^{-2} d x=\frac{x^{-1}}{-1}+c\right)$
Thus $y^{2}+y=c-\frac{1}{x}$ is the general solution of the given differential equation.

## Example 3: Solve the differential equation

$$
\frac{1}{x} \frac{d y}{d x}-2 y=0 \quad x \neq 0, y>0
$$

Solution: Multiplying the both sides of the given equation by $\frac{x}{y} d x$, gives

$$
\frac{1}{y}\left(\frac{d y}{d x} d x\right)-2 x d x=0 \quad \text { or } \quad \frac{1}{y} d y \quad 2 x d x \quad\left(\because \frac{d y}{d x} d x \quad d y\right)
$$

Now integrating either side gives $\ln y=x^{2}+c_{1} \quad$ where $c_{1}$ is a constant
or $y=\mathrm{e}^{x^{2}+c_{1}}=\mathrm{e}^{x^{2}} \cdot e^{x_{1}}$
Thus $y=c e^{x^{2}}$ where $\quad e^{c_{1}}=c$
is the required general solution of the given differential equation.
Example 4: $\quad$ Solve $\frac{d y}{d x}=\frac{y^{2}+1}{e^{-x}}$
Solution: Separating the variables, we have

$$
\frac{1}{y^{2}+1} d y=\frac{1}{e^{-x}} d x=e^{x} d x
$$

Now integrating either side gives

$$
\operatorname{Tan}^{-1} y=\mathrm{e}^{x}+\mathrm{c}, \quad \text { where } \mathrm{c} \text { is a constant, }
$$

or $\quad y=\operatorname{Tan}\left(\mathrm{e}^{x}+\mathrm{c}\right)$
which is the general solution of the given differential equation.

$$
\text { version: } 1.1
$$

Example 5: $\quad$ Solve $2 e^{x} \tan y d x+\left(1-e^{x}\right) \sec ^{2} y d y=0\left(\begin{array}{c}0<y<\frac{\pi}{2} \\ \text { or } \pi<y<\frac{3 \pi}{2}\end{array}\right)$
Solution: Given that: $2 e^{x} \tan y d x+\left(1-e^{x}\right) \sec ^{2} y d y=0$
Dividing either term of (i) by $\tan y\left(1-e^{x}\right)$, we get

$$
\begin{aligned}
& \frac{2 e^{x}}{1-e^{x}} d x+\frac{\sec ^{2} y}{\tan y} d y=0 \\
& \text { or } \quad \frac{-2 e^{x}}{e^{x}-1} d x+\frac{\sec ^{2} y}{\tan y} d y=0
\end{aligned}
$$

Integrating, we have

$$
\int-2\left(\frac{e^{x}}{e^{x}-1}\right) d x+\int\left(\frac{\sec ^{2} y}{\tan y}\right) d y=c_{1} \quad\left(e^{x}-1>0\right)
$$

or $\quad-2 \ln \left(e^{x}-1\right)+\ln (\tan y)=c_{1}$
$\Rightarrow \quad \ln \left(e^{x}-1\right)^{-2}+\ln (\tan y)=\ln c, \quad$ where $c_{1}=\ln c$
or $\quad \ln \left[\left(e^{x}-1\right)^{-2} \tan y\right]=\ln c$
$\Rightarrow \quad\left(e^{x}-1\right)^{-2} \tan y=c \quad \Rightarrow \quad \tan y=c\left(e^{x}-1\right)^{2}$.
Example 6: Solve $(\sin y+y \cos y) d y=[x(2 \ln x+1)] d x$
Solution: $(\sin y+y \cos y) d y=(2 x \ln x+x) d x$
(i)

$$
\begin{aligned}
& \text { or } \quad(1 \cdot \sin y+y \cos y) d y=\left(2 x \ln x+x^{2} \cdot \frac{1}{x}\right) d x \\
& \Rightarrow\left(\frac{d}{d y}(y \sin y)\right) d y=\left(\frac{d}{d x}\left(x^{2} \ln x\right)\right) d x\left(\because \frac{d}{d y}(y \sin y)=1 \cdot \sin y \quad y \cos y \text { and }\right. \\
& \left.\frac{d}{d x}\left(x^{2} \ln x\right) 2 x \ln x+x^{2} \cdot \frac{1}{x}\right)
\end{aligned}
$$

Integrating, we have

$$
\int\left(\frac{d}{d y}(y \sin y)\right) d y=+\int\left(\frac{d}{d x}\left(x^{2} \ln x\right)\right) d x
$$

$$
\Rightarrow \quad y \sin y = x^2 \ln x + c
$$