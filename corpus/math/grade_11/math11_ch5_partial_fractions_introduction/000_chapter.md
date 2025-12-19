# Chapter
# 5
## Partial Fractions

## INTRODUCTION

We have learnt in the previous classes how to add two or more rational fractions into a single rational fraction. For example,
(i) $\frac{1}{x-1}+\frac{2}{x+2}=\frac{3 x}{(x-1)(x+2)}$
and
(ii) $\frac{2}{x+1}+\frac{1}{(x+1)^{2}}+\frac{3}{x-2}=\frac{5 x^{2}+5 x-3}{(x+1)^{2}(x-2)}$

In this unit we shall learn how to reverse the order in (i) and (ii) that is to express a single rational fraction as a sum of two or more single rational fractions which are called Partial Fractions.
Expressing a rational fraction as a sum of partial fractions is called Partial Fraction
Resolution. It is an extremely valuable tool in the study of calculus to decompose a complex rational fraction into a sum of simpler fractions.
An open sentence formed by using the sign of equality ' $=$ ' is called an equation. The equations can be divided into the following two kinds:
Conditional equation: It is an equation in which two algebraic expressions are equal for particular values of the variable e.g.,
(a) $2 x=3$ is a conditional equation and it is true only if $x=\frac{3}{2}$.
(b) $x^{2}+x-6=0$ is a conditional equation and it is true for $x=2,-3$ only.

## Note

For simplicity, a conditional equation is called an equation.
Identity: It is an equation which holds good for all values of the variable e.g.,
(a) $(a+b) x=a x+b x$ is an identity and its two sides are equal for all values of $x$.
(b) $(x+3)(x+4)=x^{2}+7 x+12$ is also an identity which is true for all values of $x$. For convenience, the symbol '"=0" shall be used both for equation and identity.

# 5.1 Rational Fraction

An expression of the form $\frac{P(x)}{Q(x)}$, where $P(x)$ and $Q(x)$ are polynomials in $x$ with real coefficients and $Q(x) \neq 0$, is called a rational fraction. A rational fraction is of two types.

### 5.1.1 Proper Rational Fraction

A rational fraction $\frac{P(x)}{Q(x)}$ is called a Proper Rational Fraction if the degree of the polynomial $P(x)$ in the numerator is less than the degree of the polynomial $Q(x)$ in the denominator. For example, $\frac{3}{x+1}, \frac{2 x-5}{x^{2}+4}$ and $\frac{9 x^{2}}{x^{3}-1}$ are proper rational fractions or proper fractions.

### 5.1.2 Improper Rational Fraction

A rational fraction $\frac{P(x)}{Q(x)}$ is called an Improper Rational Fraction if the degree of the polynomial $P(x)$ in the numerator is equal to or greater than the degree of the polynomial $Q(x)$ in the denominator.

For example, $\frac{x}{2 x-3}, \frac{(x-2)(x+1)}{(x-1)(x+4)}, \frac{x^{2}-3}{3 x+1}$ and $\frac{x^{3}-x^{2}+x+1}{x^{2}+5}$
are improper rational fractions or improper fractions.
Any improper rational fraction can be reduced by division to a mixed form, consisting of the sum of a polynomial and a proper rational fraction.
For example, $\frac{3 x^{2}+1}{x-2}$ is an improper rational fraction.
By long division we obtain $\frac{3 x^{2}+1}{x-2}=3 x+6+\frac{13}{x-2}$, that is an improper rational fraction $\frac{3 x^{2}+1}{x-2}$ has been reduced to the sum
of a polynomial $3 x+6$ and a proper rational fraction $\frac{13}{x-2}$.

$$
\begin{gathered}
\frac{3 x+6}{x-2} / 3 x^{2}+1 \\
\pm 3 x^{2} \mp 6 x \\
\hline 6 x+1 \\
\pm 6 x+12 \\
\hline 13
\end{gathered}
$$

When a rational fraction is separated into partial fractions, the result is an identity; i.e., it is true for all values of the variable in the domain of the identity.

The evaluation of the coefficients of the partial fractions is based on the following theorem:
"If two polynomials are equal for all values of the variable, then the polynomials have same degree and the coefficients of like powers of the variable in both the polynomials must be equal".
For example,
If $p x^{3}+q x^{3}-a x+b=2 x^{3}-3 x^{2}-4 x+5, \forall x$ then $p=2, q=-3, a=4$ and $b=5$.

# 5.1.3 Resolution of a Rational Fraction $\frac{P(x)}{Q(x)}$ into Partial Freations

Following are the main points of resolving a rational fraction $\frac{P(x)}{Q(x)}$ into partial fractions:
(i) The degree of $P(x)$ must be less than that of $Q(x)$. If not, divide and work with the remainder theorem.
(ii) Factorize the denominator $Q(x)$ into its irreducible factors, write the rational fraction into partial fractions.
(iii) Multiply the identity with the denominator of left hand side.
(iv) Equate the coefficients of like terms (powers of $x$ ).
(v) Solve the resulting equations for the coefficients.

We now discuss the following cases of partial fractions resolution.
Case I: Resolution of $\frac{P(x)}{Q(x)}$ into partial fractions when $Q(x)$ has only nonrepeated linear factors:
The polynomial $Q(x)$ may be written as:

$$
\begin{aligned}
& Q(x)=\left(x-a_{1}\right)\left(x-a_{2}\right) \ldots\left(x-a_{n}\right) \text {, where } a_{1} \neq a_{2} \neq \ldots \neq a_{n} \\
& \therefore \quad \frac{P(x)}{Q(x)}=\frac{A_{1}}{x-a_{1}}+\frac{A_{2}}{x-a_{2}}+\cdots+\frac{A_{n}}{x-a_{n}} \text { is an identity. }
\end{aligned}
$$

Where $A_{1}, A_{2}, \ldots, A_{n}$ are numbers to be found.
The method is explained by the following examples:
Example 1 Resolve $\frac{7 x+25}{(x+3)(x+4)}$ into partial fractions.
Solution Suppose $\frac{7 x+25}{(x+3)(x+4)}=\frac{A}{x+3}+\frac{B}{x+4}$

Multiplying both sides by $(x+3)(x+4)$, we get

$$
\begin{aligned}
7 x+25 & =A(x+4)+B(x+3) \\
\Rightarrow \quad 7 x+25 & =A x+4 A+B x+3 B \\
\Rightarrow \quad 7 x+25 & =(A+B) x+4 A+3 B
\end{aligned}
$$

this is an identity in $x$.
So, equating the coefficients of like powers of $x$ we have

$$
7=A+B \quad \text { and } \quad 25=4 A+3 B
$$

Solving these equations, we get $A=4$ and $B=3$.
Hence the partial fractions are: $\frac{4}{x+3}+\frac{3}{x+4}$.
Alternative method
Suppose $\quad \frac{7 x+25}{(x+3)(x+4)}=\frac{A}{x+3}+\frac{B}{x+4}$
$\Rightarrow \quad 7 x+25=A(x+4)+B(x+3)$
As two sides of the identity are equal for all values of $x$,
Let us put $x=-3$ and $x=-4$ in it.
For $A$, putting $x+3=0$ i.e., $x=-3$, we get

$$
\begin{aligned}
& -21+25=A(-3+4) \\
& \Rightarrow \quad A=4
\end{aligned}
$$

For $B$, putting $x+4=0$ i.e., $x=-4$, we get

$$
\begin{aligned}
& -28+25=B(-4+3) \\
& \Rightarrow \quad B=3
\end{aligned}
$$

Hence the partial fractions are: $\frac{4}{x+3}+\frac{3}{x+4}$
Example 2 Resolve $\frac{x^{2}-10 x+13}{(x-1)\left(x^{2}-5 x+6\right)}$ into partial fractions.
Solution The polynomial $x^{2}-5 x+6$ in the denominator can be factorized and its factors are $x-3$ and $x-2$.
$\therefore \quad \frac{x^{2}-10 x+13}{(x-1)\left(x^{2}-5 x+6\right)}=\frac{x^{2}-10 x+13}{(x-1)(x-2)(x-3)}$
Suppose $\frac{x^{2}-10 x+13}{(x-1)(x-2)(x-3)}=\frac{A}{x-1}+\frac{B}{x-2}+\frac{C}{x-3}$

$\Rightarrow \quad x^{2}-10 x+13=A(x-2)(x-3)+B(x-1)(x-3)+C(x-1)(x-2)$
which is an identity in $x$.
For $A$, putting $x-1=0$ i.e., $x=1$, we get

$$
\begin{aligned}
& (1)^{2}-10(1)+13=A(1-2)(1-3)+B(1-1)(1-3)+C(1-1)(1-2) \\
& \Rightarrow \quad 1-10+13=A(-1)(-2)+B(0)(-2)+C(0)(-1) \\
& 4=2 A \\
& \therefore \quad A=2
\end{aligned}
$$

For $B$, putting $x-2=0$ i.e., $x=2$, we get

$$
\begin{aligned}
& (2)^{2}-10(2)+13=A(0)(2-3)+B(2-1)(2-3)+C(2-1)(0) \\
& \Rightarrow \quad 4-20+13=B(1)(-1) \\
& \Rightarrow \quad-3=-B \\
& \therefore \quad B=3
\end{aligned}
$$

For $C$, putting $x-3=0$ i.e., $x=3$, we get

$$
\begin{aligned}
& (3)^{2}-10(3)+13=A(3-2)(0)+B(3-1)(0)+C(3-1)(3-2) \\
& \Rightarrow \quad 9-30+13=C(2)(1) \\
& \Rightarrow \quad-8=2 C \\
& \therefore \quad C=-4
\end{aligned}
$$

Hence, $\frac{x^{2}-10 x+13}{(x-1)\left(x^{2}-5 x+6\right)}=\frac{2}{x-1}+\frac{3}{x-2}-\frac{4}{x-3}$
Example 3 Resolve $\frac{2 x^{3}+x^{2}-x-3}{x(2 x+3)(x-1)}$ into partial fractions.
Solution $\frac{2 x^{3}+x^{2}-x-3}{x(2 x+3)(x-1)}$ is an improper fraction so, first transform it into mixed form.
Denominator $=x(2 x+3)(x-1)=2 x^{3}+x^{2}-3 x$
$\therefore$ Dividing $2 x^{3}+x^{2}-x-3$ by $2 x^{3}+x^{2}-3 x$,
we have
Quotient $=1$ and Remainder $=2 x-3$

$$
\begin{aligned}
& 2 x^{3}+x^{2}-3 x \longdiv { 2 x ^ { 3 } + x ^ { 2 } - x - 3 } \\
& -2 x^{3} \pm x^{2} \mp 3 x \\
& 2 x-3
\end{aligned}
$$

$\therefore \quad \frac{2 x^{3}+x^{2}-x-3}{x(2 x+3)(x-1)}=1+\frac{2 x-3}{x(2 x+3)(x-1)}$
Suppose $\quad \frac{2 x-3}{x(2 x+3)(x-1)}=\frac{A}{x}+\frac{B}{2 x+3}+\frac{C}{x-1}$

$$
\Rightarrow \quad 2 x-3=A(2 x+3)(x-1)+B(x)(x-1)+C(x)(2 x+3)
$$

which is an identity in $x$.
For $A$, putting $x=0$ in the identity, we get $A=1$
For $B$, putting $2 x+3=0 \Rightarrow x=-\frac{3}{2}$ in the identity, we get $B=-\frac{8}{5}$
For $C$, putting $x-1=0 \Rightarrow x=1$ in the identity, we get $C=-\frac{1}{5}$
Hence, $\frac{2 x^{3}+x^{2}-x-3}{x(2 x+3)(x-1)}=1+\frac{1}{x}-\frac{8}{5(2 x+3)}-\frac{1}{5(x-1)}$
Case II: When $Q(x)$ has repeated linear factors:
If the polynomial $Q(x)$ has a repeated linear factors $(x-a)^{n}, n \geq 2$ and $n$ is $a$ positive integer, then $\frac{P(x)}{Q(x)}$ may be written as the following identity:

$$
\frac{P(x)}{Q(x)}=\frac{A}{(x-a)}+\frac{A_{2}}{(x-a)^{2}}+\cdots+\frac{A_{n}}{(x-a)^{n}}
$$

where $A_{1}, A_{2}, \ldots, A_{n}$ are numbers to be found.
The method is explained by the following examples:
Example 4 Resolve $\frac{x^{3}+x-1}{(x+2)^{3}}$ into partial fractions.
Solution Suppose $\frac{x^{3}+x-1}{(x+2)^{3}}=\frac{A}{x+2}+\frac{B}{(x+2)^{2}}+\frac{C}{(x+2)^{3}}$

$$
\begin{aligned}
& \Rightarrow x^{2}+x-1=A(x+2)^{2}+B(x+2)+C \\
& \Rightarrow x^{2}+x-1=A\left(x^{2}+4 x+4\right)+B(x+2)+C
\end{aligned}
$$

For C , putting $x+2=0$, i.e., $x=-2$ in (i), we get

$$
\begin{aligned}
& (-2)^{2}+(-2)-1=A(0)+B(0)+C \\
& \Rightarrow \quad 1=C
\end{aligned}
$$

Equating the coefficients of $x^{2}$ and $x$ in (ii), we get $A=1$

$$
\text { and } \quad 1=4 A+B
$$

$$
\Rightarrow \quad 1=4+B \Rightarrow B=-3
$$

Hence, $\frac{x^{2}+x-1}{(x+2)^{3}}=\frac{1}{x+2}-\frac{3}{(x+2)^{2}}+\frac{1}{(x+2)^{3}}$
Example 5 Resolve $\frac{1}{(x+1)^{2}\left(x^{2}-1\right)}$ into partial fractions.
Solution Here denominator $=(x+1)^{2}\left(x^{2}-1\right)$

$$
=(x+1)^{2}(x+1)(x-1)=(x+1)^{2}(x-1)
$$

$$
\therefore \quad \frac{1}{(x+1)^{2}\left(x^{2}-1\right)}=\frac{1}{(x+1)^{3}(x-1)}
$$

Suppose $\quad \frac{1}{(x-1)(x+1)^{3}}=\frac{A}{x-1}+\frac{B}{x+1}+\frac{C}{(x+1)^{2}}+\frac{D}{(x+1)^{3}}$

$$
\begin{aligned}
& \Rightarrow \quad 1=A(x+1)^{3}+B(x+1)^{2}(x-1)+C(x-1)(x+1)+D(x-1) \\
& \Rightarrow \quad 1=A\left(x^{3}+3 x^{2}+3 x+1\right)+B\left(x^{3}+x^{2}-x-1\right)+C\left(x^{2}-1\right)+D(x-1) \\
& \Rightarrow \quad 1=(A+B) x^{3}+(3 A+B+C) x^{2}+(3 A-B+D) x+(A-B-C-D)
\end{aligned}
$$

For $A$, putting $x-1=0 \Rightarrow x=1$ in (i), we get

$$
1=A(2)^{3} \quad \Rightarrow A=\frac{1}{8}
$$

For $D$, putting $x+1=0 \Rightarrow x=-1$ in (i), we get

$$
1=D(-1-1) \quad \Rightarrow \quad D=-\frac{1}{2}
$$

Equating the coefficients of $x^{3}$ and $x^{2}$ in (ii), we get

$$
0=A+B \quad \Rightarrow \quad B=-A \quad \Rightarrow \quad B=-\frac{1}{8}
$$

and

$$
0=3 A+B+C \Rightarrow 0=\frac{3}{8}-\frac{1}{8}+C \Rightarrow C=-\frac{1}{4}
$$

Hence the partial fractions are:

$$
\frac{\frac{1}{8}}{x-1}+\frac{-\frac{1}{8}}{x+1}+\frac{-\frac{1}{4}}{(x+1)^{2}}+\frac{-\frac{1}{2}}{(x+1)^{3}}=\frac{1}{8(x-1)}-\frac{1}{8(x+1)}-\frac{1}{4(x+1)^{2}}-\frac{1}{2(x+1)^{3}}
$$

# EXERCISE 5.1

## Resolve the following into partial fractions:

1. $\frac{2}{x^{2}-1}$
2. $\frac{a-b}{(x-a)(x-b)},(a \neq b)$
3. $\frac{x^{2}+1}{(x+1)(x-1)}$
4. $\frac{2 x+3}{(x+1)(x+2)(x+3)}$
5. $\frac{x^{2}+4 x+5}{(x+1)\left(x^{2}+5 x+6\right)}$
6. $\frac{4 x^{3}+5 x^{3}-3 x-2}{x^{2}-1}$
7. $\frac{3 x^{2}-12 x+11}{(x-1)(x-2)(x-3)}$
8. $\frac{(x-1)(x-2)(x-3)}{(x-4)(x-5)(x-6)}$
9. $\frac{x^{2}}{\left(x^{2}+a\right)\left(x^{2}+b\right)\left(x^{2}+c\right)}$
10. $\frac{x+1}{(x-1)^{2}}$
11. $\frac{x^{2}+x}{\left(x^{2}-1\right)^{2}}$
12. $\frac{3 x^{2}+4 x-5}{(x-1)^{3}}$
13. $\frac{1}{x(x+1)^{3}}$
14. $\frac{4 x^{2}-3 x+1}{(x+1)(x-1)^{2}}$
15. $\frac{12 x^{2}-48}{(x-2)^{2}(x+2)^{2}}$

## Case III: When $Q(x)$ contains non-repeated irreducible quadratic factors

Definition: A quadratic factor is irreducible if it cannot be written as the product of two linear factors with real coefficients. For example, $x^{2}+x+1$ and $x^{2}+3$ are irreducible quadratic factors.

If the polynomial $Q(x)$ contains non-repeated irreducible quadratic factors then $\frac{P(x)}{Q(x)}$ may be written as the identity having partial fractions of the form:

$$
\frac{A x+B}{a x^{2}+b x+c} \text { where } A \text { and } B \text { are the numbers to be found. }
$$

The method is explained by the following examples:
Example 6 Resolve $\frac{3 x-11}{\left(x^{2}+1\right)(x+3)}$ into partial fractions.
Solution Suppose $\frac{3 x-11}{\left(x^{2}+1\right)(x+3)}=\frac{A x+B}{x^{2}+1}+\frac{C}{x+3}$

$$
\begin{aligned}
& \Rightarrow \quad 3 x-11=(A x+B)(x+3)+C\left(x^{2}+1\right) \\
& \Rightarrow \quad 3 x-11=(A+C) x^{2}+(3 A+B) x+(3 B+C)
\end{aligned}
$$

For $C$, putting $x+3=0 \quad \Rightarrow \quad x=-3$ in (i), we get

$$
-9-11=C(9+1) \quad \Rightarrow \quad C=-2
$$

Equating the coefficients of $x^{2}$ and $x$ in (ii), we get

$$
\begin{aligned}
& 0=A+C \Rightarrow A=-C \quad \Rightarrow A=2 \\
& \text { and } \quad 3=3 A+B \Rightarrow B=3-3 A \Rightarrow B=3-6 \Rightarrow B=-3 \\
& \text { Hence, } \frac{3 x-11}{\left(x^{2}+1\right)(x+3)}=\frac{2 x-3}{x^{3}+1}-\frac{2}{x+3}
\end{aligned}
$$

Example 7 Resolve $\frac{4 x^{2}+8 x}{x^{4}+2 x^{2}+9}$ into partial fractions.
Solution Here, denominator $=x^{4}+2 x^{2}+9=\left(x^{2}+2 x+3\right)\left(x^{2}-2 x+3\right)$

$$
\therefore \quad \frac{4 x^{2}+8 x}{x^{4}+2 x^{2}+9}=\frac{4 x^{2}+8 x}{\left(x^{2}+2 x+3\right)\left(x^{2}-2 x+3\right)}
$$

Suppose

$$
\begin{aligned}
& \frac{4 x^{2}+8 x}{\left(x^{2}+2 x+3\right)\left(x^{2}-2 x+3\right)}=\frac{A x+B}{x^{2}+2 x+3}+\frac{C x+D}{x^{2}-2 x+3} \\
& \Rightarrow \quad 4 x^{2}+8 x=(A x+B)\left(x^{2}-2 x+3\right)+(C x+D)\left(x^{2}+2 x+3\right) \\
& \Rightarrow \quad 4 x^{2}+8 x=(A+C) x^{3}+(-2 A+B+2 C+D) x^{2} \\
&+(3 A-2 B+3 C+2 D) x+3 B+3 D
\end{aligned}
$$

which is an identity in $x$.
Equating the coefficients of $x^{3}, x^{2}, x, x^{0}$ in (i), we have

$$
\begin{aligned}
& 0=A+C \\
& 4=-2 A+B+2 C+D \\
& 8=3 A-2 B+3 C+2 D \\
& 0=3 B+3 D
\end{aligned}
$$

Solving (ii), (iii), (iv) and (v), we get

$$
A=1, B=2, C=-1 \text { and } D=-2
$$

Hence, $\frac{4 x^{2}+8 x}{x^{4}+2 x^{2}+9}=\frac{x+2}{x^{2}+2 x+3}+\frac{-x-2}{x^{2}-2 x+3}$
Case IV: When $Q(x)$ has repeated irreducible quadratic factors
If the polynomial $Q(x)$ contains a repeated irreducible quadratic factors $\left(a x^{2}+b x+c\right)^{n}$, $n \geq 2$ and $n$ is a positive integer, then $\frac{P(x)}{Q(x)}$ may be written as the following identity:

$$
\frac{P(x)}{Q(x)}=\frac{A_{1} x+B_{1}}{\alpha x^{2}+b x+c}+\frac{A_{2} x+B_{2}}{\left(a x^{2}+b x+c\right)^{2}}+\ldots+\frac{A_{n} x+B_{n}}{\left(a x^{2}+b x+c\right)^{n}}
$$

where $A_{1}, B_{1}, A_{2}, B_{2}, \ldots, A_{n}, B_{n}$ are numbers to be found. The method is explained through the following example:

Example 5 Resolve $\frac{4 x^{2}}{\left(x^{2}+1\right)^{2}(x-1)}$ into partial fractions.
Solution Let $\frac{4 x^{2}}{\left(x^{2}+1\right)^{2}(x-1)}=\frac{A x+B}{x^{2}+1}+\frac{C x+D}{\left(x^{2}+1\right)^{2}}+\frac{E}{x-1}$
$\Rightarrow 4 x^{2}=(A x+B)\left(x^{2}+1\right)(x-1)+(C x+D)(x-1)+E\left(x^{2}+1\right)^{2}$
$\Rightarrow \quad 4 x^{2}=(A+E) x^{4}+(-A+B) x^{3}+(A-B+C+2 E) x^{2}$

$$
+(-A+B-C+D) x+(-B-D+E)
$$

For $E$, putting $x-1=0 \quad \Rightarrow x=1$ in (i), we get

$$
4=E(1+1)^{2} \quad \Rightarrow \quad E=1
$$

Equating the coefficients of $x^{4}, x^{3}, x^{2}, x$, in (ii), we get

$$
\begin{aligned}
& 0=A+E \quad \Rightarrow \quad A=-E \quad \Rightarrow \quad A=-1 \\
& 0=-A+B \quad \Rightarrow \quad B=A \quad \Rightarrow \quad B=-1 \\
& 4=A-B+C+2 E \\
& \Rightarrow \quad C=4-A+B-2 E=4+1-1-2 \Rightarrow \quad C=2 \\
& \text { and } \quad 0=-A+B-C+D \\
& \Rightarrow \quad D=A-B+C=-1+1+2=2 \quad \Rightarrow \quad D=2
\end{aligned}
$$

Hence, $\frac{4 x^{2}}{\left(x^{2}+1\right)^{2}(x-1)}=\frac{x-1}{x^{2}+1}+\frac{2 x+2}{\left(x^{2}+1\right)^{2}}+\frac{1}{x-1}$

# EXERCISE 5.2

## Resolve into partial fractions:

1. $\frac{2 x^{2}+3 x+3}{(x+1)\left(x^{2}+1\right)}$
2. $\frac{2 x+1}{(x-2)\left(x^{2}+3 x+5\right)}$
3. $\frac{2 x+32}{(x-2)\left(x^{2}+2\right)^{2}}$
4. $\frac{3 x^{2}+3}{x^{3}+1}$
5. $\frac{x^{4}}{x^{4}+2 x^{2}+1}$
6. $\frac{6 x^{4}+40 x^{2}}{\left(4-x^{2}\right)\left(x^{2}+4\right)^{2}}$