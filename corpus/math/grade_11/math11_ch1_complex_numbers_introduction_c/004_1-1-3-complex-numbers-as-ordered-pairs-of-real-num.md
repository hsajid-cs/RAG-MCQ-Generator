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