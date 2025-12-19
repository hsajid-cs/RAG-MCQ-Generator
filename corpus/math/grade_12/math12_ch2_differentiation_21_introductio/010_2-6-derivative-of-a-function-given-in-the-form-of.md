### 2.6 DERIVATIVE OF A FUNCTION GIVEN IN THE FORM OF PARAMETRIC EQUATIONS

The equations $x=a t^{2}$ and $y=2 a t$ express $x$ and $y$ as function of $t$. Here the variable $t$ is called a parameter and the equations of $x$ and $y$ in terms of $t$ are called the parametric equations.

Now we explain the method of finding derivatives of functions given in the form of parametric equations by the following examples.

Example 1: $\quad$ Find $\frac{d y}{d x}$ if $x=a t^{2}$ and $y=2 a t$.

Solution: We use the chain rule to find $\frac{d y}{d x}$
Here $\frac{d y}{d t}=\frac{d}{d t}(2 a t)=2 a \cdot 1=2 a$
and $\frac{d x}{d t}=\frac{d}{d t}\left(a t^{2}\right)=a(2 t)=2 a t$
so $\quad \frac{d y}{d x}=\frac{d y}{d t} \cdot \frac{d t}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{2 a}{2 a t}=\frac{2 a}{y} \quad(\because 2 \mathrm{a}=y)$
Eliminating $t$, we get $x=a\left(\frac{y}{2 a}\right)^{2}=a \cdot \frac{y^{2}}{4 a^{2}}=\frac{y^{2}}{4 a} \Rightarrow y^{2}=4 a x$
Differentiating both sides of (i) w.r.t. ' $x$ ' we have

$$
\begin{aligned}
& \frac{d}{d x}\left(y^{2}\right)=\frac{d}{d x}(4 a x) \\
& \frac{d}{d x}\left(y^{2}\right) \cdot \frac{d y}{d x}=4 a \cdot \frac{d}{d x}(x) \quad \Rightarrow 2 x \frac{d y}{d x}=4 a \text { (1) } \\
& \Rightarrow \frac{d y}{d x}=\frac{2 a}{y}
\end{aligned}
$$

Example 2: $\quad$ Find $\frac{d y}{d x}$ if $x 1-t^{2}$ and $y=3 t^{2}-2 t^{2}$.
Solution: Given that $x=1-t^{2} \ldots .$. (i) and $y=3 t^{2}-2 t^{2}$
Differentiating (i) w.r.t. ' $t$ ', we get

$$
\frac{d y}{d t}=\frac{d}{d t}\left(1-t^{2}\right)=\frac{d}{d t}(1)-\frac{d}{d t}\left(t^{2}\right)=0-2 t=-2 t
$$

Differentiating (ii) w.r.t. ' $t$ ', we have

$$
\begin{aligned}
& \frac{d y}{d t}=\frac{d}{d t}\left(3 t^{2}-2 t^{2}\right)=\frac{d}{d t}\left(3 t^{2}\right)=\frac{d}{d t}\left(2 t^{2}\right) \\
& =3(2 t)-2\left(3 t^{2}\right)=6 t-6 t^{2}=6 t(1-t)
\end{aligned}
$$

Applying the formula

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d y}{d t} \frac{d t}{d x}=\frac{\frac{d y}{d t}}{\frac{d t}{d t}} \\
& =\frac{6 t(1-t)}{-2 t}=-3(1-t)=3(t-1)
\end{aligned}
$$

Example 3: $\quad$ Find $\frac{d y}{d x}$ if $x=\frac{1-t^{2}}{1+t^{2}}, y=\frac{2 t}{1+t}$

Solution: Given that $x=\frac{\left(1+t^{2}\right)}{1+t^{2}}$
(i) and $y \quad \frac{2 t}{1+t^{2}}$
(ii)

Differentiating (i) w.r.t. ' $t$ ', we get

$$
\begin{aligned}
& \frac{d x}{d t}=\frac{d}{d t}\left(\frac{1-t^{2}}{1+t^{2}}\right)=\frac{\left(\frac{d}{d t}\left(1-t^{2}\right)\right)\left(1+t^{2}\right)-\left(1-t^{2}\right) \cdot \frac{d}{d t}\left(1+t^{2}\right)}{\left(1+t^{2}\right)^{2}} \\
& =\frac{(-2 t)\left(1+t^{2}\right)-\left(1-t^{2}\right)(2 t)}{\left(1+t^{2}\right)^{2}} \quad \frac{2 t\left(-1-t^{2}-1+t^{2}\right)}{\left(1+t^{2}\right)^{2}} \quad \frac{-4 t}{\left(1+t^{2}\right)^{2}}
\end{aligned}
$$

Differentiating (i) w.r.t. ' $t$ ', we have

$$
\begin{aligned}
\frac{d y}{d t} & =\frac{d}{d t}\left(\frac{2 t}{1+t^{2}}\right) \quad \frac{\left(\frac{d}{d t}(2 t)\right)\left(1+t^{2}\right)-2 t \times \frac{d}{d t}\left(1+t^{2}\right)}{\left(1+t^{2}\right)^{2}} \\
& =\frac{2\left(1+t^{2}\right)-2 t(2 t)}{\left(1+t^{2}\right)^{2}}=\frac{2+2 t^{2}-4 t^{2}}{\left(1+t^{2}\right)^{2}} \quad \frac{2-2 t^{2}}{\left(1+t^{2}\right)^{2}} \quad \frac{2\left(1-t^{2}\right)}{\left(1+t^{2}\right)^{2}} \\
\frac{d y}{d x} & =\frac{d y}{d t} \frac{d t}{d x}=\frac{\frac{d y}{d t}}{\frac{d t}{d x}}=\frac{\frac{2\left(1-t^{2}\right)}{\left(1+t^{2}\right)^{2}}}{\frac{4 t}{\left(1+t^{2}\right)^{2}}}=\frac{2\left(1-t^{2}\right)}{-4 t}=\frac{t^{2}-1}{2 t}
\end{aligned}
$$