### 1.2 Equality of Two Complex Numbers

The two complex numbers $z_{1}=a+b i$ and $z_{2}=c+d i$ are said to be equal iff their real and imaginary parts are equal i.e., $a+b i=c+d i \Leftrightarrow a=c$ and $b=d$.
Example 4 If $(3+2 i)(x+i y)=5+12 i$, where $x, y \in R$, then find the values of $x$ and $y$.
Solution Given that

$$
(3+2 i)(x+i y)=5+12 i
$$

$$
\begin{aligned}
& \Rightarrow 3 x+3 i y+2 i x+2 i^{2} y=5+12 i \\
& \Rightarrow(3 x-2 y)+(2 x+3 y) i=5+12 i
\end{aligned}
$$

Comparing real and imaginary parts, we have

$$
\begin{aligned}
& 3 x-2 y=5 \\
& 2 x+3 y=12
\end{aligned}
$$

Multiply equation (i) by 3 and equation (ii) by 2 , we have

$$
\begin{aligned}
& 9 x-6 y=15 \\
& 4 x+6 y=24
\end{aligned}
$$

Add the equations

$$
\begin{aligned}
9 x-6 y+4 x+6 y & =15+24 \\
13 x & =39 \\
x & =3
\end{aligned}
$$

Substitute $x=3$ in equation (i), we have

$$
\begin{aligned}
3(3)-2 y & =5 \\
9-2 y & =5 \\
-2 y & =-4 \\
y & =2
\end{aligned}
$$

Thus $x=3, y=2$

# 1.2.1 Square Root of a Complex Number

The square root of a complex number is another complex number that, when squared, gives the original complex number.
Let $w=p+i q$ is a square root of a complex number $z=x+i y$, where $p, q, x, y \in R$, then $w=\sqrt{z} \ldots$ (i), taking square on both sides, we get

$$
\begin{aligned}
w^{2} & =z \\
(p+i q)^{2} & =x+i y \\
p^{2}+2 p q i-q^{2} & =x+i y
\end{aligned}
$$

Equating real and imaginary parts, we have

$$
\begin{aligned}
& x=p^{2}-q^{2} \\
& y=2 p q
\end{aligned}
$$

We know that $\left(p^{2}+q^{2}\right)^{2}=\left(p^{2}-q^{2}\right)^{2}+4 p^{2} q^{2}$
Substitute $x=p^{2}-q^{2}, y=2 p q$ in the above equation, we get

$$
\begin{aligned}
\left(p^{2}+q^{2}\right)^{2} & =x^{2}+y^{2} \\
\Rightarrow \quad p^{2}+q^{2} & =\sqrt{x^{2}+y^{2}}
\end{aligned}
$$

From equations (ii) and (iv), we have $x=p^{2}-q^{2}$ and $p^{2}+q^{2}=\sqrt{x^{2}+y^{2}}$. Solving for the values $p$ and $q$, we have

$$
p= \pm \sqrt{\frac{\sqrt{x^{2}+y^{2}}+x}{2}} \text { and } q= \pm \sqrt{\frac{\sqrt{x^{2}+y^{2}}-x}{2}}
$$

From equation (iii): $y=2 p q$, we have

- $y>0$, if $p$ and $q$ have the same sign
- $y<0$, if $p$ and $q$ have opposite signs
- $y=0$, if $p=0$ or $q=0$

Therefore, the square root of the complex number $z=x+i y$ is given by

$$
\sqrt{z}=\sqrt{x+i y}= \pm\left(\sqrt{\frac{\sqrt{x^{2}+y^{2}}+x}{2}}+\frac{i y}{|y|} \sqrt{\frac{\sqrt{x^{2}+y^{2}}-x}{2}}\right)
$$

or $\sqrt{x}= \pm\left(\sqrt{\frac{|z|+x}{2}}+\frac{i y}{|y|} \sqrt{\frac{|z|-x}{2}}\right) \cdots(\mathrm{v})$, where $|z|=\sqrt{x^{2}+y^{2}} \geq 0$ is modulus of $z$.
Equation (v) is the required formula for square root of the complex number $x+i y$.
Example 5 Find the square root of complex number $5+12 i$ and also represent the square root on an Argand diagram.
Solution Let $x+y i=5+12 i$

$$
\begin{aligned}
\Rightarrow \quad x & =5 \text { and } y=12>0 \\
|z| & =|5+12 i|=\sqrt{5^{2}+12^{2}}=13
\end{aligned}
$$

Applying the square root formula for complex numbers, we get

$$
\begin{aligned}
\sqrt{5+12 i} & = \pm\left(\sqrt{\frac{13+5}{2}}+\frac{12 i}{|12|} \sqrt{\frac{13-5}{2}}\right) \\
& = \pm(\sqrt{9}+i \sqrt{4})= \pm(3+2 i)
\end{aligned}
$$

Thus, the square root of the complex number $5+12 i$ are $3+2 i$ and $-3-2 i$ as shown in above figure.

# EXERCISE 1.2

1. Find the real values of $x$ and $y$ in each of the following:
(i) $x+i y+2-3 i=i(5-i)(3+4 i)$
(ii) $(x+i y)(1-i)=(2-3 i)(-5+5 i)\left(-i \frac{3}{5}\right)$
(iii) $\frac{x}{2+i}+\frac{y}{3-i}=4+5 i$

2. If $z_{1}=-13+24 i$ and $z_{2}=x+y i$, find the real values of $x$ and $y$ such that $z_{1}-z_{2}=-27+15 i$
3. Find the real values of $x$ and $y$ if:
(i) $(x+i y)^{2}=25+60 i$
(ii) $(x+i y)^{2}=64+48 i$
(iii) $(x+i y)^{2}=\frac{2 i-3}{3+i}$
4. If $z_{1}=2+3 i$ and $z_{2}=1-\alpha$, find the real value of $\alpha$ such that $\operatorname{Im}\left(z_{1} z_{2}\right)=7$.
5. If $z_{1}=x+y i$ and $z_{2}=a+b i$, find $x, y, a$ and $b$ such that $z_{1}+z_{2}=10+4 i$ and $z_{1}-z_{2}=6+2 i$.
6. Show that $\forall z_{1}, z_{2} \in C, \overline{z_{1} z_{2}}=\overline{z_{1} z_{2}}$
7. Find the square root of the following complex numbers:
(i) $-7-24 i$
(ii) $8-6 i$
(iii) $-15-36 i$
(iv) $119+120 i$
8. Find the square root of $13-20 \sqrt{3}$ and represent $1 / 3$ on an Argand diagram.
9. Find the real values of $x$ and $y$ if $(-7+i)(x+i y)+(-1-5 i)=i(11-i)$
10. Find the real values of $x$ and $y$ if $(5-2 i)(x+i y)+3=i(11-i)-4 i$
11. Find the real values of $u$ and $v$ if $u=2$ $v=3$
12. If $z_{1}=4+5 i$ and $z_{2}=\alpha-2 i$, find the real values of $\alpha$ such that $\operatorname{Re}\left(z_{1} z_{2}\right)=20$.

# 1.3 Complex Polynomials as a Product of Linear Factors

A complex polynomial $P(z)$ is a polynomial function of the complex variable $z$ with complex coefficients. It is expressed in the general form as:

$$
P(z)=a_{n} z^{n}+a_{n-1} z^{n-1}+\ldots+a_{1} z+a_{0}
$$

where $a_{n}, a_{n-1}, \ldots, a_{1}, a_{0}$ are complex numbers $\left(a_{n} \neq 0\right)$, and $n \geq 0$ is an integer representing the degree of the polynomial.
For examples $P_{1}(z)=(1-i) z+3 i, P_{2}(z)=(5-4 i) z^{2}+(2+i) z+(3-4 i)$ and $P_{3}(z)=(2-i) z^{3}+2 z^{2} i+(5+3 i)$ are the examples of linear, quadratic and cubic complex polynomials respectively. If $n=0$, then $P(z)$ becomes a constant polynomial. A fundamental property of complex polynomials is that they can always be factored into a product of linear factors.
According to the Fundamental theorem of algebra, a polynomial of degree $n \geq 1$ has exactly $n$ roots in complex number system $C$.

A corollary to this theorem states that any polynomial $P(z)$ of degree $n$ can be factored completely into a constant $a$ and $n$ linear factor over $C$ in the form

$$
P(z)=a\left(z-z_{1}\right)\left(z-z_{2}\right) \ldots\left(z-z_{n}\right)
$$

where $z_{1}, z_{2}, \ldots, z_{n}$ are complex roots of the polynomial equation $P(z)=0$. Once we know the roots of a polynomial equation $P(z)=0$ we can apply equation (1) to factored the polynomial $P(z)$ into $n$ linear factors. Specifically, if $z_{1}$ and $z_{2}$ are roots of the polynomial equation $P(z)=0$, then the equation must be $P(z)=\left(z-z_{1}\right)\left(z-z_{2}\right)$. For examples, the polynomial $P(x)=x^{2}+4$ consists of real coefficient has no real roots, so it cannot be factored into linear polynomials with real coefficients. However, if we considered the polynomial $P(z)=z^{2}+4$ as a complex polynomial, we can easily be factored into two linear factors as:

$$
z^{2}+4=(z+2 i)(z-2 i)
$$

where $2 i$ and $-2 i$ are the complex roots of $z^{2}+4=0$
fif $P(z)$ is a polynomial function, the values of $z$ that satisfy $P(z)=0$ are called the zeros of the function $P(z)$ and roots of the polynomial equation $P(z)=0$.
Example 6 Factorize the polynomial $P(z)=z^{2}+(i-3) z-3 i$.
Solution $P(z)=z^{2}+(i-3) z-3 i$

$$
\begin{aligned}
& =z^{2}+z i-3 z-3 i \\
& =z(z+i)-3(z+i) \\
& =(z+i)(z-3)
\end{aligned}
$$

Example 7 Factorize the polynomial $P(z)=z^{2}-4 i z+12$.
Solution $P(z)=z^{2}-4 i z+12$

$$
\begin{aligned}
& =z^{2}-4 i z-(-12) \\
& =z^{2}-4 i z-i^{2} 12 \quad \because \quad i^{2}=-1 \\
& =z^{2}-6 i z+2 i z-i^{2} 12 \\
& =z(z-6 i)+2 i(z-6 i) \\
& =(z-6 i)(z+2 i)
\end{aligned}
$$

Example 8 Factorize the polynomial $P(z)=z^{3}+(1+i) z^{2}+i z$.
Solution $P(z)=z^{3}+(1+i) z^{2}+i z$

$$
\begin{aligned}
& =z\left[z^{2}+(1+i) z+i\right] \\
& =z\left[z^{2}+z+i z+i\right] \\
& =z[z(z+1)+i(z+1)] \\
& =z[(z+1)(z+i)] \\
& =z(z+1)(z+i)
\end{aligned}
$$

# Key concept

The Rational Root Theorem is a mathematical tool used to find all possible rational roots of a polynomial equation with integer coefficients. According to rational root theorem:
If a polynomial $P(x)=a_{x} x^{x}+a_{x+} x^{x^{2}}+\ldots+a_{1} x+a_{x}$ has integer coefficients, then every rational root $\frac{p}{q}$ (in the simplest terms) satisfies:
(i) $\quad p$ is a factor of the constant term $a_{i y}$ (ii) $q$ is a factor of the leading coefficient $a_{s y}$.

Example 9 Factorize the polynomial $P(z)=z^{3}-3 z^{2}+z+5$.
Solution According to rational root theorem the possible root of the equation are $\pm 1$ and $\pm 5$. On checking, we see that $z=-1$ is the root of $P(z)=0$ because

$$
P(-1)=(-1)^{3}-3(-1)^{2}+(-1)+5=0
$$

So $z+1$ is a factor of the $P(z)$. Using synthetic division

$$
\begin{array}{c|ccc}
-1 & 1 & -3 & 1 & 5 \\
\hline & -1 & -1 & 4 & -5 \\
\hline 1 & -4 & 5 & 0
\end{array}
$$

Therefore, $z^{3}-3 z^{2}+z+5=(z+1)\left(z^{2}-4 z+5\right)$
Next find the factors of $z^{3}-4 z+5$ using quadratic formula

$$
\begin{aligned}
z^{2}-4 z+5 & =0, \text { here } a=1, b=-4, c-5 \\
z & =\frac{-(-4) \pm \sqrt{(-4)^{2}-4(1)(5)}}{2(1)}=\frac{4 \pm \sqrt{16-20}}{2}=\frac{4 \pm \sqrt{-4}}{2}=\frac{4 \pm 2 i}{2} \\
\Rightarrow \quad z & =2 \pm i
\end{aligned}
$$

The quadratic factors of $z^{2}-4 z+5=(z-(2+i))(z-(2-i))=(z-2-i)(z-2+i)$
Substituting in equation (i), we have the

$$
z^{3}-3 z^{2}+z+5=(z+1)(z-2-i)(z-2+i)
$$