# Chapter
# 1
## Complex Numbers

## INTRODUCTION

Complex numbers are an extension of the real numbers designed to solve equations that have no solutions within the realm of real numbers. The history of mathematics shows that man has been developing and enlarging his concept of number according to the saying that "Necessity is the mother of invention". In the remote past they started with the set of counting numbers and invented, by stages, the negative numbers, rational numbers, irrational numbers etc. Since square of a positive as well as negative number is a positive number, the square root of a negative number does not exist in the realm of real numbers. Therefore, square roots of negative numbers were given no attention for centuries together. However, recently, properties of numbers involving square roots of negative numbers have also been discussed in detail and such numbers have been found useful and have been applied in many branches of pure, applied, financial and computational mathematics.

### 1.1 Complex Numbers

The numbers of the form $z=a+i b$, where $a, b \in R$ and $i=\sqrt{-1}$, are called complex numbers. For example, $3+4 i, 2 \frac{5}{7} i,-7-2 i$ etc. are complex numbers and the set of all complex numbers is denoted by $C$.

### 1.1.1 Recognition of Real and Imaginary Parts

Let us start with considering the following equation:

$$
x^{2}+1 \Rightarrow x^{2}=-1 \Rightarrow x= \pm \sqrt{-1}
$$

$\sqrt{-1}$ does not belong to the set of real numbers. We, therefore, for convenience call it imaginary number and denote it by $i$ (read as iota).

## Note

Every real number is a complex number with 0 as its imaginary part.

In the complex number $z=a+i b, a$ is called real part and $b$ is called imaginary part of the complex number. For convenient, real part is denoted by $\operatorname{Re} z$ and imaginary part by $\operatorname{Im} z$ of a complex number $z$. For example, if $z=3+4 i$, then

$$
\operatorname{Re} z=3 \text { and } \operatorname{Im} z=4
$$

The product of a non-zero real number and $i$ is also an imaginary number.
For example, $2 i,-3 i, \sqrt{5} i,-\frac{11}{2} i$ are all imaginary numbers.

Conjugate of Complex Numbers: Let $z=a+i b$ be a complex number, then $a-i b$ is called the complex conjugate of $a+i b$. It is denoted by $\bar{z}$. Thus $5-4 i$ is complex conjugate of $5+4 i$ and $-2-3 i$ is complex conjugate of $-2+3 i$.

# Note A real number is self-conjugate.

### 1.1.2 Operations on Complex Numbers

With a view to develop algebra of complex numbers, we state a few definitions.
The symbols $a, b, c, d, k$, where used, represent real numbers.
(i) Addition: $(a+i b)+(c+i d)=(a+c)+i(b+d)$
(ii) $k(a+i b)=k a+i k b$
(iii) Subtraction: $(a+i b)-(c+i d)=(a+i b)+[-(c+i d)]$

$$
=a+i b+(-c-i d)=(a-c)+i(b-d)
$$

(iv) Multiplication: $(a+i b)(c+i d)=a c+i a d+i b c+i^{2} b d=(a c-b d)+i(a d+b c)$

### 1.1.3 Complex Numbers as Ordered Pairs of Real Numbers

We can define complex numbers also by using ordered pairs.
Let $C$ be the set of ordered pairs belonging to $R \times R$ which are subject to the following properties:
(i) $(a, b)=(c, d) \Leftrightarrow a=c \wedge b=d$
(ii) $(a, b)+(c, d)=(a+c, b+d)$
(iii) $(a, b)(c, d)=(a c-b d, a d+b c)$
(iv) If $k$ is any real number, then $k(a, b)=(k a, k b)$

Then $C$ is called the set of complex numbers. It is easy to see that

$$
(a, b)-(c, d)=(a-c, b-d)
$$

Properties (i), (ii) and (iii) respectively define equality, sum and product of two complex numbers. Property (iv) defines the product of a real number and a complex number.
Example 1 Find the sum, difference and product of the complex numbers $(8,9)$ and $(5,-6)$
Solution $\operatorname{Sum}=(8+5,9-6)=(13,3)$
Difference $=(8-5,9-(-6))=(3,15)$

$$
\begin{aligned}
\text { Product } & =(8.5-9(-6), 8(-6)+9.5) \\
& =(40+54,-48+45)=(94,-3)
\end{aligned}
$$

# 1.1.4 Properties of the Fundamental Operations on Complex Numbers

It can be easily verified that the set $C$ satisfies all the field axioms i.e., it possesses the properties of real numbers.
By way of explanation of some points we observe as follows:
(i) The additive identity in $C$ is $(0,0)$.
(ii) Every complex number $(a, b)$ has the additive inverse $(-a,-b)$ i.e., $(a, b)+(-a,-b)=(0,0)$
(iii) The multiplicative identity is $(1,0)$ i.e.,

$$
\begin{aligned}
(a, b) \cdot(1,0) & =(\alpha \cdot 1-b \cdot 0, b \cdot 1+\alpha \cdot 0)=(a, b) \\
& =(1,0) \cdot(a, b)
\end{aligned}
$$

(iv) Every non-zero complex number \{i.e., number not equal to $(0,0)\}$ has a multiplicative inverse. The multiplicative inverse of $(a, b)$ is

$$
\left(\frac{a}{a^{2}+b^{2}}, \frac{-b}{a^{2}+b^{2}}\right)
$$

$\because \quad(a, b)\left(\frac{a}{a^{2}+b^{2}}, \frac{-b}{a^{2}+b^{2}}\right)=(1,0)$, the identity element

$$
=\left(\frac{a}{a^{2}+b^{2}}, \frac{-b}{a^{2}+b^{2}}\right)(a, b)
$$

(v) $(a, b)[(c, d) \pm(e, f)]=(a, b)\left(c, d\right) \pm(a, b)(e, f)$

Example 2 If $z_{1}=(4,2)$ and $z_{2}=(3,-1)$, then find $\frac{z_{1}}{z_{2}}$.
Solution Given $z_{1}=(4,2), z_{2}=(3,-1)$
Now, $\frac{z_{1}}{z_{2}}=\frac{(4,2)}{(3,-1)}=\frac{4+2 i}{3-i}$
Multiply the numerator and denominator by the complex conjugate of $z_{2}=3-i$.

$$
\begin{aligned}
\frac{z_{1}}{z_{2}} & =\frac{4+2 i}{3-i}=\frac{4+2 i}{3-i} \times \frac{3+i}{3+i} \\
& =\frac{(4)(3)+(4)(i)+(2 i)(3)+(2 i)(i)}{(3)^{2}-(i)^{2}}=\frac{12+4 i+6 i+2 i^{2}}{9-i^{2}} \\
& =\frac{12+10 i-2}{9-(-1)}=\frac{10+10 i}{10}=1+i \quad \because \quad i^{2}=-1
\end{aligned}
$$

Thus, $\frac{z_{1}}{z_{2}}=1+i$

# 1.1.5 Argand Diagram

Every complex number is represented by one and only one point of the coordinate plane and every point of the plane represents one and only one complex number. The components of the complex number are be the coordinates of the point representing it. In this representation the $x$-axis is called the real axis and the $y$-axis is called the imaginary axis. The coordinate plane itself is called the complex plane or $z$ - plane. The figure representing one or more complex numbers on the complex plane is called an Argand diagram. The Argand diagram is a way of representing one or more complex numbers on the complex plane. Points on the $x$-axis represent real numbers whereas the points on the $y$-axis represent imaginary numbers.
In an Argand diagram, the complex number $x+i y$ is uniquely represented by the order pair $(x, y)$. In Figure (i), the complex numbers $3+2 i,-2+2 i,-3-2 i$ and $2-2 i$ correspond to the order pairs $(3,2),(-2,2),(-3,-2)$ and $(2,-2)$ respectively have been represented geometrically by the point $A, B, C$ and $D$.
Modulus of a Complex Number: The real number $\sqrt{x^{2}+y^{2}}$ is called the modulus of the complex number $x+i y$ and it is denoted by $|x+i y|$. In Figure (ii), $O A$ represents the modulus of $x+i y$. In other words, the modulus of a complex number is the distance from the origin to the point representing the number.
$$
\begin{aligned}
z & =\frac{(1+2 i)^{2}}{2-i}=\frac{1+4 i+4 i^{2}}{2-i}=\frac{-3+4 i}{2-i} \times \frac{2+i}{2+i}=\frac{-6-3 i+8 i+4 i^{2}}{2^{2}-i^{2}} \\
& =\frac{-6+5 i-4}{4-(-1)}=\frac{-10+5 i}{5} \\
\Rightarrow \quad z & =-2+i
\end{aligned}
$$

Taking conjugate

$$
\bar{z}=\overline{-2+i}=-2-i
$$

$$
\begin{array}{ll}
\text { and } & |\bar{z}|=|-2-i|=\sqrt{(-2)^{2}+(-1)^{2}}=\sqrt{4+1} \\
\Rightarrow & |\bar{z}|=\sqrt{5}
\end{array}
$$

# EXERCISE 1.1

1. Find the multiplicative inverse of each of the following complex numbers:
(i) $(-4,7)$
(ii) $(\sqrt{2},-\sqrt{5})$
(iii) $(1,0)$
2. Separate into real and imaginary parts (write as a simple complex number):
(i) $\frac{2-7 i}{4+5 i}$
(ii) $\frac{(-2+3 i)^{2}}{1+i}$
(iii) $\frac{i}{1+i}$
(iv) $\frac{(4+3 i)^{2}}{4-3 i}$
3. Prove that $\bar{z}=z$ iff $z$ is real.
4. For $z \in C$, show that:
(i) $\frac{z+\bar{z}}{2}=\operatorname{Re}(z)$
(ii) $\frac{z-\bar{z}}{2 i}=\operatorname{Im}(z)$
(iii) $|z|^{2}=z \cdot \bar{z}$
5. If $z_{1}=2+i, z_{2}=3-2 i, z_{3}=1+3 i$, then express $\frac{z_{1} z_{3}}{z_{2}}$ in the form of $a+i b$.
6. If $z_{1}=2+7 i$ and $z_{2}=-5+3 i$, then evaluate the following:
(i) $\left|2 z_{1}-4 z_{2}\right|$
(ii) $\left|3 z_{1}+2 z_{1}\right|$
(iii) $\left|-7 z_{2}+2 z_{2}\right|$
(iv) $\left|\left(z_{1}+z_{2}\right)^{3}\right|$
7. Show that: $i^{n+1}+i^{n+2} \in i^{n+3}+i^{n+4}=0$, for all $n \in N$.
8. Find the least positive value of $n$, if $\left(\frac{1+i}{1-i}\right)^{n}=1$
9. Show that: the value of $i^{n}$ for $n \in N$ and $n>4$ is $i^{r}$, where $r$ is the remainder when $n$ is divided by 4 .

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

### 1.3.1 Soiction of Quadratic Equation by Completing the Square

As we learned in previous classes, completing the square is a powerful and systematic method for solving quadratic equations. This technique involves rewriting a quadratic equation in the form $a x^{2}+b x+c=0$ into a perfect square trinomial, which can then be solved by taking the square root of both sides. This method is especially valuable when the quadratic equation does not factor easily. By completing the square, we can solve any quadratic equation, even those with irrational or complex roots, making it a more effective technique in algebra.
Example 10 Solve the equation $2 z^{2}-12 z+50=0$ by completing square method and hence express it as a product of its linear factors.

Solution $2 z^{2}-12 z+50=0$
Dividing both sides by 2

$$
\begin{aligned}
z^{2}-6 z+25 & =0 \\
\Rightarrow \quad z^{2}-2(3) z & =-25
\end{aligned}
$$

Add $3^{2}$ on both sides

$$
\begin{aligned}
z^{2}-2(3) z+3^{2} & =-25+3^{2} \\
(z-3)^{2} & =-16 \\
\Rightarrow \quad z-3 & = \pm \sqrt{-16} \\
\Rightarrow \quad z & =3 \pm 4 i
\end{aligned}
$$

Therefore, $z=3+4$ ior $z=3-4$ iare the required complex roots.
Using the corollary of Fundamental theorem of Algebra the equation can be factorized using the roots $3+4 i$ and $3-4 i$ as:
$2 z^{2}-12 z+50=2\left(z^{2}-6 z+25\right)=2(z-(3+4 i))(z-(3-4 i))=2(z-3-4 i)(z-3+4 i)$
Hence, $2 z^{2}-12 z+50=2(z-3-4 i)(z-3+4 i)$

# EXERCISE 1.3

1. Factorize the following:
(i) $a^{2}+4 b^{2}$
(ii) $9 a^{2}+16 b^{2}$
(iii) $3 x^{2}+3 y^{2}$
(iv) $144 x^{2}+225 y^{2}$
(v) $z^{2}-2 i z-1$
(vi) $z^{2}+6 z+13$
(vii) $z^{2}+4 z+5$
(viii) $2 z^{2}-22 z+65$
2. Factorize the following polynomals into its linear factors:
(i) $z^{3}+8$
(ii) $z^{3}+27$
(iii) $z^{3}-2 z^{2}+16 z-32$
(iv) $z^{4}+21 z^{2}-100$
(v) $z^{4}-16$
(vi) $z^{4}+3 z^{2}-4$
(vii) $z^{4}+5 z^{2}+6$
(viii) $z^{4}-32 z^{2}-3969$
3. Find the roots of $z^{4}+7 z^{2}-144=0$ and hence express it as a product of linear factors.
4. Solve the following complex quadratic equations by completing square method:
(i) $2 z^{2}-3 z+4=0$
(ii) $z^{2}-6 z+30=0$
(iii) $3 z^{2}-18 z+50=0$
(iv) $z^{2}+4 z+13=0$
(v) $2 z^{2}+6 z+9=0$
(vi) $3 z^{2}-5 z+7=0$
5. Solve the following equations:
(i) $2 z^{4}-32=0$
(ii) $3 z^{2}-243 z=0$
(iii) $5 z^{2}-5 z=0$
(iv) $z^{3}-5 z^{2}+z-5=0$
(v) $4 z^{4}-25 z^{2}-21=0$
(vi) $z^{3}+z^{2}+z+1=0$
6. Find a polynomial $P(z)$ of degree 3 with zeros $3,-2 i, 2 i$ and satisfying $P(1)=20$.
7. Find a polynomial $P(z)$ of degree 4 with zeros $2 i,-2 i, 1,-1$, and satisfying $P(2)=240$.
8. Find a polynomial $P(z)$ of degree 4 with zeros $4,-4,1+i, 1-i$ and satisfying $P(2)=72$.

# 1.4 Three Cube Roots of Unity

Let $x$ be a cube root of unity

$$
\begin{aligned}
& \therefore \quad x=(1)^{\frac{1}{3}} \\
& \Rightarrow \quad x^{3}=1 \\
& \Rightarrow \quad x^{3}-1=0 \\
& \Rightarrow \quad(x-1)\left(x^{2}+x+1\right)=0 \\
& \text { Either } \quad x-1=0 \Rightarrow x=1 \\
& \text { or } \quad x^{2}+x+1=0 \\
& \therefore \quad x=\frac{-1 \pm \sqrt{1-4}}{2} \\
& \Rightarrow \quad x=\frac{-1 \pm \sqrt{3} i}{2}
\end{aligned}
$$

## Note

We know that the numbers containing $i$ are called imaginary numbers. So $\frac{-1+\sqrt{3} i}{2}$ and $\frac{-1-\sqrt{3} i}{2}$ are called imaginary cube roots of unity.

Thus, the three cube roots of unity are:

$$
1, \frac{-1+\sqrt{3} i}{2} \text { and } \frac{-1-\sqrt{3} i}{2}
$$

### 1.4.1 Properties of Cube Roots of Unity

(i) Each complex cube root of unity is square of the other

$$
\text { If } \frac{-1+\sqrt{3} i}{2}=\omega \text {, then } \frac{-1-\sqrt{3} i}{2}=\omega^{2}
$$

and if $\frac{-1-\sqrt{3} i}{2}=\omega$, then $\frac{-1+\sqrt{3} i}{2}=\omega^{2}[\omega$ is read as omega]
(ii) The sum of all the three cube roots of unity is zero i.e., $1+\omega+\omega^{2}=0$
(iii) The product of all the three cube roots of unity is unity i.e., $1 \cdot \omega \cdot \omega^{2}=\omega^{2}=1$, as a consequence of which, each imaginary cube root of unity is the reciprocal of the other, that is, $\omega=\frac{1}{\omega^{2}}, \omega^{2}=\frac{1}{\omega}$.

### 1.4.2 Four Fourth Roots of Unity

Let $x$ be a fourth root of unity

$$
\begin{aligned}
& \therefore \quad x=(1)^{\frac{1}{4}} \quad \Rightarrow \quad x^{4}=1 \quad \Rightarrow \quad x^{4}-1=0 \quad \Rightarrow \quad\left(x^{2}-1\right)\left(x^{2}+1\right)=0 \\
& \Rightarrow x^{2}-1=0 \quad \Rightarrow \quad x^{2}=1 \Rightarrow x= \pm 1 \\
& \text { and } x^{2}+1=0 \Rightarrow x^{2}=-1 \Rightarrow x= \pm i \text {. }
\end{aligned}
$$

Hence four fourth roots of unity are: $1,-1, i,-i$.

# 1.4.3 Properties of four Fourth Roots of Unity

We have found that the four fourth roots of unity are: $1,-1,+i,-i$
(i) Sum of all the four fourth roots of unity is zero

$$
\because \quad 1+(-1)+i+(-i)=0
$$

(ii) The real fourth roots of unity are additive inverses of each other. 1 and -1 are the real fourth roots of unity and $1+(-1)=0=(-1)+1$
(iii) Both the imaginary fourth roots of unity are conjugate of each other. $i$ and $-i$ are imaginary fourth roots of unity, which are obviously conjugates of each other.
(iv) Product of all the fourth roots of unity is -1 i.e., $1 \times(-1) \times i \times(-i)=-1$

Example 11 Prove that: $\left(x^{3}+y^{3}\right)=(x+y)(x+\omega y)\left(x+\omega^{2} y\right)$
Proof: R.H.S $=(x+y)(x+\omega y)\left(x+\omega^{2} y\right)$

$$
\begin{aligned}
& =(x+y)\left[x^{2}+\left(\omega+\omega^{2}\right) y x+\omega^{2} y^{2}\right] \\
& =(x+y)\left(x^{2}-x y+y^{2}\right)=x^{3}+y^{3}=\text { L.H.S. }\left\{\because \omega^{3}=1, \omega+\omega^{2}=-1\right\}
\end{aligned}
$$

Hence proved.

## EXERCISE 1.4

1. Find the three cube roots of:
(i) 8
(ii) -8
(iii) -27
(iv) 64
(v) -125
2. Find the four fourth roots of $16,81,625$. Also show that their sum is zero in each case.
3. If $1, \omega, \omega^{2}$ are the cube roots of unity, show that $1+\omega^{n}+\omega^{2 n}=3$ where $n$ is a multiple of 3 respectively.
4. Evaluate:
(i) $\left(\frac{-1+\sqrt{-3}}{2}\right)^{4}+\left(\frac{-1-\sqrt{-3}}{2}\right)^{7}$
(ii) $(-1+\sqrt{-3})^{5}+(-1-\sqrt{-3})^{5}$
5. Show that $\left(1-\omega+\omega^{2}\right)\left(1-\omega^{2}+\omega^{4}\right)\left(1-\omega^{4}+\omega^{8}\right)\left(1-\omega^{2}+\omega^{10}\right) \ldots$ to $2 n$ factors $-2^{2 n}$
6. Prove that $\left(\frac{i+\sqrt{3}}{2}\right)^{3}+\left(\frac{i-\sqrt{3}}{2}\right)^{6}=-1$.
7. Evaluate $\sum_{k=0}^{5} \omega^{2 k}$, where $\omega$ is an imaginary cube root of unity.
8. If $\omega$ is an imaginary cube roots of unity, prove that $\frac{a+b \omega^{2}+c \omega}{a \omega^{2}+b \omega+c}=\omega$
9. If $\omega$ is a cube root of unity, prove that $\frac{a \omega^{12}+b \omega^{17}+c \omega^{19}}{a \omega^{14}+b \omega^{22}+c \omega^{20}}=\omega$

# 1.4 Polar Coordinates System

Polar coordinates are often more convenient than Cartesian coordinates in situations involving circular or rotational symmetry, or when a problem depends on distance from a fixed point and angle relative to a reference direction. Just as the Cartesian coordinate system uses an ordered pair $(x, y)$ to describe the position of a point, the polar coordinate system determines the position of a point using a directed distance $r$ from a fixed origin $O$ (called the pole) and an angle $\theta$ that the line connecting the origin to the point makes with the polar axis (typically aligned
with the positive $x$-axis).

In polar coordinate system the location of a point $P$ can be described by polar coordinates in the form $(r, \theta)$, where $r$ and $\theta$ are real numbers.
While $r$ is typically considered non-negative ( $r \geq 0$ ), it is also possible for $r$ to be negative $(r<0)$. The value of $r$ changes depending on its sign, and this affects the position of the point in the plane.
When $r>0$, the angle $\theta$ is the measure of any angle in standard position whose terminal side lies along the line connecting the origin to the point $P$, measured from the polar axis (positive $x$-axis).
For example, the polar coordinates $\left(5, \frac{\pi}{4}\right)$ represent a point 5 units away from pole at an angle of $\frac{\pi}{4}$ radians.
When $r<0$, the angle $\theta$ is the measure of any angle in standard position whose terminal side lies along the line connecting the origin to the point $Q$, but the point $Q$ is located $|r|$ units in the opposite direction (i.e., $\theta+\pi$ ) from the polar axis (positive $x$-axis). For example, the polar coordinates $\left(-5, \frac{\pi}{4}\right)$ represents a point 5 units away from the pole, but in the direction of $\frac{\pi}{4}+\pi=\frac{5 \pi}{4}$ radians.

# Note $(-5, \pi / 4)$ and $(5,5 \pi / 4)$ represent the same point in the plane

### 1.4.1 The Polar Form of a Complex Nurnber

Consider the adjoining diagram representing the complex number $z=x+i y$. From the diagram, we see that $x=r \cos \theta$ and $y=r \sin \theta$, where $r=|z|$ is modulus and $\theta$ is called an argument of $z$.
Hence $\quad x+i y=r \cos \theta+i r \sin \theta$
where $r=|z|=\sqrt{x^{2}+y^{2}}$ and $\theta=\tan ^{-1} \frac{y}{x}$
Equation (i) is called the polar form of the complex number $z$.
Example 12 Express the complex number $1+i \sqrt{3}$ in polar form.
Solution Step - I: Put $r \cos \theta=1$ and $r \sin \theta=\sqrt{3}$
Step - II: $r^{2}=(1)^{2}+(\sqrt{3})^{2}$

$$
\begin{aligned}
& \Rightarrow r^{2}=1+3=4 \\
& \Rightarrow r=2
\end{aligned}
$$

Step - III: $\quad \theta=\tan ^{-1} \frac{\sqrt{3}}{1}=\tan ^{-1} \sqrt{3}=60^{\circ}$

## Note

- If $x=0, y>0$ then $\theta=90^{\circ}$
- If $x=0, y<0$ then $\theta=-90^{\circ}$
- If $x=0, y=0$ then $\theta$ is undefined.
- If $y=0, x>0$ then $\theta=0^{\circ}$.
- If $y=0, x<0$ then $\theta=180^{\circ}$.

Thus $1+i \sqrt{3}=2 \cos 60^{\circ}+i 2 \sin 60^{\circ}$
Principal Argument: The principal argument $\theta$ of a complex number $z=a+b i$ is the angle between the positive real axis and the line joining $(a, b)$ to the origin in the Argand plane.

$$
\operatorname{Arg} z=\theta=\tan ^{-1}\left(\frac{b}{a}\right) \quad(a \neq 0)
$$

It is denoted by Arg. It is a single, specific value of the argument, typically chosen within a standard range: $\operatorname{Arg} z \in(-\pi, \pi]$.

# 1.3.3 Operations on Complex Numbers in Polar Form

## Addition and Subtraction of Complex number in Polar form

Let $z_{1}=r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)$ and $z_{2}=r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right)$ be two complex numbers in polar form. The addition and subtraction of these numbers can be computed simply as

$$
z_{1}+z_{2}=r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)+r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right)
$$

and $z_{1}-z_{2}=r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)-r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right)$

## Multiplication of Complex number in Polar form

Let $z_{1}=r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)$ and $z_{2}=r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right)$ be two complex number in polar form. The product of these numbers can be derived by multiplying them directly and simplifying

$$
\begin{aligned}
& z_{1} \cdot z_{2}=r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right) \cdot r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right) \\
& z_{1} \cdot z_{2}=r_{1} \cdot r_{2}\left(\cos \theta_{1} \cos \theta_{2}+i \cos \theta_{1} \sin \theta_{2}+i \sin \theta_{1} \cos \theta_{2}+i^{2} \sin \theta_{1} \sin \theta_{2}\right) \\
& z_{1} \cdot z_{2}=r_{1} \cdot r_{2}\left[\left(\cos \theta_{1} \cos \theta_{2}-\sin \theta_{1} \sin \theta_{2}\right)+i\left(\cos \theta_{1} \sin \theta_{2}+\sin \theta_{1} \cos \theta_{2}\right)\right] \quad \because i^{2}=-1 \\
& z_{1} \cdot z_{2}=r_{1} \cdot r_{2}\left[\cos \left(\theta_{1}+\theta_{2}\right)+i \sin \left(\theta_{1}+\theta_{2}\right)\right] \quad \text { (Using trigonometric identities) }
\end{aligned}
$$

Thus, multiplying two complex numbers in polar form involves multiplying their moduli and summing their arguments i.e., $\arg \left(z_{1} \cdot z_{2}\right)=\arg \left(z_{1}\right)+\arg \left(z_{2}\right)$
Example13 Find the product of $5\left(\cos \frac{\pi}{6}+i \sin \frac{\pi}{6}\right)$ and $4\left(\cos \frac{3 \pi}{2}+i \sin \frac{3 \pi}{2}\right)$.
Solution Let $z_{1}=5\left(\cos \frac{\pi}{6}+i \sin \frac{\pi}{6}\right)$ and $z_{2}=4\left(\cos \frac{3 \pi}{2}+i \sin \frac{3 \pi}{2}\right)$
Here, $r_{1}=5$ and $\theta_{1}=\frac{\pi}{6}$, while $r_{2}=4$ and $\theta_{2}=\frac{3 \pi}{2}$
Substitute this value in the product formula

$$
\begin{aligned}
z_{1} \cdot z_{2} & =r_{1} \cdot r_{2}\left[\cos \left(\theta_{1}+\theta_{2}\right)+i \sin \left(\theta_{1}+\theta_{2}\right)\right] \\
& =5 \times 4\left[\cos \left(\frac{\pi}{6}+\frac{3 \pi}{2}\right)+i \sin \left(\frac{\pi}{6}+\frac{3 \pi}{2}\right)\right]=20\left(\cos \frac{5 \pi}{3}+i \sin \frac{5 \pi}{3}\right)
\end{aligned}
$$

Thus, the required product is $20\left(\cos \frac{5 \pi}{3}+i \sin \frac{5 \pi}{3}\right)$

# Division of Complex Number in Polar Form

Let $z_{1}=r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)$ and $z_{2}=r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right)$ be two complex numbers in polar form. The formula for division of these numbers in polar form can be derived as below:
$\frac{z_{1}}{z_{2}}=\frac{r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)}{r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right)}$
$\frac{z_{1}}{z_{2}}=\frac{r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)}{r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right) \cdot\left(\cos \theta_{2}-i \sin \theta_{2}\right) \quad$ (Multiply and divide the R.H.S by conjugate of $\cos \theta_{2}+i \sin \theta_{2}$ )
$\frac{z_{1}}{z_{2}}=\frac{r_{1}}{r_{2}} \frac{\left(\cos \theta_{1} \cos \theta_{2}+\sin \theta_{1} \sin \theta_{2}\right)+i\left(\sin \theta_{1} \cos \theta_{2}-\cos \theta_{1} \sin \theta_{2}\right)}{\cos ^{2} \theta_{2}+\sin ^{2} \theta_{2}}$
$\frac{z_{1}}{z_{2}}=\frac{r_{1}}{r_{2}}\left[\cos \left(\theta_{1}-\theta_{2}\right)+i \sin \left(\theta_{1}-\theta_{2}\right)\right] \quad$ (Using trigonometric identities)
Thus, the modulus of the division of two complex numbers equals the quotient of their moduli, while the arguments of the quotient is the difference between their arguments.
Thus, when dividing two complex numbers, the modulus of the result is the ratio of their moduli, and the argument of the result is the difference between their arguments i.e., $\arg \left(\frac{z_{1}}{z_{2}}\right)=\arg \left(z_{1}\right)-\arg \left(z_{2}\right)$

Example 14 Divide $\frac{2}{7}\left(\cos \frac{7 \pi}{6}+i \sin \frac{7 \pi}{6}\right)$ by $\frac{3}{5}\left(\cos \left(-\frac{\pi}{2}\right)+i \sin \left(-\frac{\pi}{2}\right)\right)$.
Solution Let $z_{1}=\frac{2}{7}\left(\cos \frac{7 \pi}{6}+i \sin \frac{7 \pi}{6}\right)$ and $z_{2}=\frac{3}{5}\left(\cos \left(-\frac{\pi}{2}\right)+i \sin \left(-\frac{\pi}{2}\right)\right)$
Here, $\quad r_{1}=\frac{2}{7}, \theta_{1}=\frac{7 \pi}{6}, r_{1}=\frac{3}{5}$ and $\theta_{2}=-\frac{\pi}{2}$.
Substitute value in the quotient formula

$$
\begin{aligned}
\frac{z_{1}}{z_{2}} & =\frac{r_{1}}{r_{2}}\left[\cos \left(\theta_{1}-\theta_{2}\right)+i \sin \left(\theta_{1}-\theta_{2}\right)\right] \\
& =\frac{2}{7} \times \frac{5}{3}\left[\cos \left(\frac{7 \pi}{6}-\left(-\frac{\pi}{2}\right)\right)+i \sin \left(\frac{7 \pi}{6}-\left(-\frac{\pi}{2}\right)\right)\right] \\
\frac{z_{1}}{z_{2}} & =\frac{10}{21}\left(\cos \frac{5 \pi}{3}+i \sin \frac{5 \pi}{3}\right)
\end{aligned}
$$

Example 15 If $z=x+i y$, then write the equation $|3 z-i|=|3 z+7|$ in terms of $x$ and $y$.
Solution Given $|3 z-i|=|3 \bar{z}+7|$
$|3 z-i|=|3(x+i y)-i|=|3 x+i(3 y-1)|=\sqrt{(3 x)^{2}+(3 y-1)^{2}}$
$|3 \bar{z}+7|=|3 x+3 i y+7|=|3 x-3 i y+7|=|3 x+7+i(-3 y)|=\sqrt{(3 x+7)^{2}+(-3 y)^{2}}$
Substitutes these values in (i)

$$
\sqrt{(3 x)^{2}+(3 y-1)^{2}}=\sqrt{(3 x+7)^{2}+(-3 y)^{2}}
$$

Taking square on both sides

$$
\begin{aligned}
(3 x)^{2}+(3 y-1)^{2} & =(3 x+7)^{2}+(-3 y)^{2} \\
9 x^{2}+9 y^{2}-6 y+1 & =9 x^{2}+42 x+49+9 y^{2} \\
\Rightarrow \quad-6 y+1 & =42 x+49 \\
\Rightarrow \quad-6 y & =42 x+48 \\
\text { or } \quad y & =-7 x-8
\end{aligned}
$$

The equation $y=-7 x-8$ represents a straight line in the complex plane.
Example 16 Show that $(x+2)^{2}+y^{2}=8$ if $\arg \left(\frac{z+2 i}{z-2 i}\right)=\frac{3 \pi}{4}$ for $z=x+i y$.
Solution $\frac{z+2 i}{z-2 i}=\frac{x+i y+2 i}{x+i y-2 i}=\frac{x+i(y+2)}{x+i(y-2)}=\frac{x+i(y+2)}{x+i(y-2)} x \frac{x-i(y-2)}{x-i(y-2)}$
$\Rightarrow \quad \frac{z+2 i}{z-2 i}=\frac{\left(x^{2}+y^{2}-4\right)+4 i x}{x^{2}+(y-2)^{2}}=\frac{x^{2}+y^{2}-4}{x^{2}+(y-2)^{2}}+i \frac{4 x}{x^{2}+(y-2)^{2}}$
As

$$
\arg \left(\frac{z+2 i}{z-2 i}\right)=\frac{3 \pi}{4}
$$

$\Rightarrow \quad \tan ^{-1}\left(\frac{4 x}{\frac{x^{2}+(y-2)^{2}}{x^{2}+y^{2}-4}}\right)=\frac{3 \pi}{4} \quad \Rightarrow \quad \frac{4 x}{x^{2}+y^{2}-4}=\tan \frac{3 \pi}{4}=-1$
$\Rightarrow \quad 4 x=-1\left(x^{2}+y^{2}-4\right) \quad \Rightarrow \quad x^{2}+4 x+y^{2}=4$
Completing the square for $x^{2}$, we have

$$
(x+2)^{2}+y^{2}=8
$$

# 1.5 Complex Numbers in the Real World (Voltage, Current and Resistance)

Ohm's Law is a fundamental principle in physics that describes the relationship between voltage $V$, current $I$ and resistance $R$ in an electrical circuit. Mathematically Ohm's Law can be expressed by the formula $V=I R$.
When dealing with alternating current (AC) circuits, resistance generalizes to impedance ( $Z$ ). Resistance in a circuit is due to inductor $\left(X_{L}\right)$ and capacitor $\left(X_{C}\right)$. Their difference is reactance $X=\left(X_{L}\right)-\left(X_{C}\right)$. Geometrically it is shown in the adjacent figure. Here $Z=R+i X$.
Then for AC circuits, Ohm's Law in Terms of Impedance is expressed by the formula $V=I \cdot Z$.
Example 17 If the impedance of circuit is $11\left(\cos 55.35^{\circ}+i \sin 55.35^{\circ}\right)$ ohms at a voltage of $25\left(\cos 30^{\circ}+i \sin 30^{\circ}\right) V$, find the value of current in the circuit.
Solution Substitute the voltage $25\left(\cos 30^{\circ}+i \sin 30^{\circ}\right)$ and impedance $11\left(\cos 55.35^{\circ}+i \sin 55.35^{\circ}\right)$ into the equation $V=I Z$, where $V$ is voltage, $I$ denote the current and $Z$ is impedance.

$$
\begin{aligned}
25\left(\cos 30^{\circ}+i \sin 30^{\circ}\right) & =I .11\left(\cos 55.35^{\circ}+i \sin 55.35^{\circ}\right) \\
\text { or } \quad I & =\frac{25\left(\cos 30^{\circ}+i \sin 30^{\circ}\right)}{11\left(\cos 55.35^{\circ}+i \sin 55.35^{\circ}\right)} \\
I & =\frac{25}{11}\left[\cos \left(30^{\circ}-55.35^{\circ}\right)+i \sin \left(30^{\circ}-55.35^{\circ}\right)\right. \\
I & =2.27\left[\cos \left(-25.35^{\circ}\right)+i \sin \left(-25.35^{\circ}\right)\right.
\end{aligned}
$$

Express into rectangular form

$$
I=2.27[0.90+i(-0.42)]=2.04-0.95 i
$$

Thus, current is $2.04-0.95 i A$.
Cryptography: It is the science of securing information by transforming readable messages called plaintext into secret code called ciphertext using mathematical algorithms and encryption keys. It consists of two main processes i.e., encryption to lock message with complex math, and decryption to unlock it with the right key.
Example 18 Encrypt the word "MATH" by multiplying it with a complex number $k=2+3 i$ and then decrypted back to its original form using the concept of multiplicative inverse in complex numbers.
Each letter of the alphabet is assigned a numerical value as follows:

$$
A=1, B=2, C=3, \ldots, Z=26
$$

# Unit 4 Complex Numbers

Solution First, we assign each letter in the word "MATH" a complex number with zero imaginary part. The encryption and decryption are shown in the table below

| Letter | Complex Number (x) | $z$ encrypted $-z \times k$ | $z$ decrypled $-z$ encrypted $/ k$ | Letter |
| :--: | :--: | :--: | :--: | :--: |
| M | $13+0 i$ | $(13+0 i)(2+3 i)=26+39 i$ | $(26+39 i) /(2+3 i)=13+0 i$ | M |
| A | $1+0 i$ | $(1+0 i)(2+3 i)=2+3 i$ | $(2+3 i) /(2+3 i)=1+0 i$ | A |
| T | $20+0 i$ | $(20+0 i)(2+3 i)=40+60 i$ | $(40+60 i) / 2+3 i=20+0 i$ | T |
| H | $8+0 i$ | $(8+0 i)(2+3 i)=16+24 i$ | $16+24 i / 2+3 i=8+0 i$ | H |

## EXERCISE 1.5

1. Plot the following points:
(i) $(2,75)$
(ii) $(-3,120)$
(iii) $\left(2, \frac{\pi}{6}\right)$
(iv) $\left(5, \frac{5 \pi}{6}\right)$
(v) $\left(-\frac{5}{2}, \frac{\pi}{3}\right)$
(vi) $\left(-3,-\frac{2 \pi}{3}\right)$
(vii) $\left(-\frac{9}{2},-\frac{19 \pi}{12}\right)$
(viii) $\left(-\frac{5}{2}, \frac{5 \pi}{12}\right)$
2. Express the following complex numbers in polar form:
(i) $4+3 i$
(ii) $1+i$
(iii) $\frac{1}{2}+\frac{\sqrt{3}}{2} i$
(iv) $-\frac{5}{2}-\frac{5 \sqrt{3}}{2} i$
(v) $\frac{1-i}{1+i}$
(vi) $\frac{\sqrt{3}+i}{1+\sqrt{3} i}$
(vii) $\frac{3+4 i}{4+3 i}$
3. Convert each of the complex number $z$ in the rectangular form $x+i y$ :
(i) $4\left(\cos \frac{5 \pi}{3}+i \sin \frac{5 \pi}{3}\right)$
(ii) $\frac{3}{2}\left(\cos \frac{7 \pi}{6}+i \sin \frac{7 \pi}{6}\right)$
(iii) $|z|=7, \arg (z)=\frac{23 \pi}{12}$
(iv) $|z|=11, \arg (z)=-\frac{11 \pi}{12}$
(v) $|z|=\frac{10}{3}, \arg (z)=-\frac{17 \pi}{12}$
(vi) $2 \cos (-33)+i 2 \sin (-33)$
4. If $z_{1}=9\left(\cos \frac{5 \pi}{4}+i \sin \frac{5 \pi}{4}\right)$ and $z_{2}=5\left(\cos \frac{\pi}{3}+i \sin \frac{\pi}{3}\right)$ then find
(i) $z_{1}+z_{2}$
(ii) $z_{1}-z_{2}$
(iii) $z_{1} \cdot z_{2}$
(iv) $\frac{z_{1}}{z_{2}}$
5. If $z_{1}=7\left(\cos \frac{23 \pi}{12}+i \sin \frac{23 \pi}{12}\right)$ and $z_{2}=11\left(\cos \frac{11 \pi}{12}+i \sin \frac{11 \pi}{12}\right)$ then find the following and express the result into $x+i y$ form
(i) $z_{1}+z_{2}$
(ii) $z_{1}-z_{2}$
(iii) $z_{1} \cdot z_{2}$
(iv) $\frac{z_{1}}{z_{2}}$

6. If $z_{1}$ and $z_{2}$ are two complex numbers, show that
(i) $\operatorname{Arg}\left(z_{1} z_{2}\right)=\operatorname{Arg} z_{1}+\operatorname{Arg} z_{2}$
(ii) $\operatorname{Arg}\left(\frac{z_{1}}{z_{2}}\right)=\operatorname{Arg} z_{1}-\operatorname{Arg} z_{2}$
7. Divide $z_{1}=6\left(\cos 150^{\circ}+i \sin 150^{\circ}\right)$ by $z_{2}=3\left(\cos 30^{\circ}+i \sin 30^{\circ}\right)$ and express in $x+i y$ form.
8. Multiply $z_{1}=2\left(\cos 60^{\circ}+i \sin 60^{\circ}\right)$ and $z_{2}=5\left(\cos 90^{\circ}+i \sin 90^{\circ}\right)$ and express in $x+i y$ form.
9. Find the modulus and argument of $z=-2-2 i$.
10. Write the equation $\arg (\bar{z}-2+i)=\frac{2 \pi}{3}$ in cartesian form, if $z=x+i y$.
11. If $z=x+i y$ and $\arg \left(\frac{\bar{z}-1+2 i}{\bar{z}+1-2 i}\right)=\frac{9 \pi}{4}$, show that $x^{2}+y^{2}+4 x+2 y-5=0$.
12. If $z=x+i y$ and $\arg (z-2-3 i)-\arg (z+2+3 i)=2 \pi$, show that $2 y=3 x$.
13. Solve the equation $|z-2 i|=|\bar{z}+2|$ for $z=x+i y$.
14. For $z=x+i y$, solve the equation $\left|5 z+4+i\right|=5 \bar{z}-3+2 i$.
15. Determine the set of points $z=x+i y$ that satisfy the equation $3 \bar{z}-2+i|=3 z+i|$.
16. If $z=x+i y$ and $w=\frac{1-i z}{z-z}$ show that $|w|=1 \Rightarrow z$ is real.
17. If $z_{1}$ and $z_{2}$ are different complex numbers with $\left|z_{2}\right|=1$, find $\left|\frac{z_{2}-z_{1}}{1-z_{1} z_{2}}\right|$.
18. An AC source supplies a voltage of $V=120\left(\cos \frac{\pi}{4}+i \sin \frac{\pi}{4}\right)$ volts to a circuit with impedance $Z=\frac{1+i \sqrt{3}}{2}$ ohms. Calculate the current in polar form.
19. An AC circuit has an impedance of $Z=3-6 i$ ohms and is connected to a voltage source of $V=90+30 i$ volts. Find the current in both rectangular and polar form.
20. Encrypt the word "CODE" by multiplying the complex encryption key $k=2-i$. Then decrypt it back to the original word.
21. Consider the complex encryption key $k=3-3 i$. Encrypt the word "QUIZ", and then recover the original word using the inverse of the key.
22. Encrypt the word "CLASS" by adding the complex encryption key $k=-3+4 i$. Then decrypt it back to the original word.