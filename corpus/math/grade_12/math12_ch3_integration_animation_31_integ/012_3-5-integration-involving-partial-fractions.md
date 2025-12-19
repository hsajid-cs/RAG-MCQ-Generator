### 3.5 INTEGRATION INVOLVING PARTIAL FRACTIONS

If $P(x), Q(x)$ are polynomial functions and the denominator $Q(x)(\neq 0)$, in the rational function $\frac{P(x)}{Q(x)}$, can be factorized into linear and quadratic (irreducible) factors, then the rational function is written as a sum of simpler rational functions, each of which can be integrated by methods already known to us.

Here we will give examples of the following three cases when the denominator $Q(x)$ contains

Case I. Non-repeated linear factors.
Case II. Repeated and non-repeated linear factors.
Case III. Linear and non-repeated irreducible quadratic factors or non repeated irreducible quadratic factors.

## EXAMPLES OF CASE I

Example 1: $\quad$ Evaluate $\int \frac{-x+6}{2 x^{2}-7 x+6} d x, \quad(x>2)$
Solution: $\quad$ The denominator $2 x^{2}-7 x+6=(x-2)(2 x-3)$,
Let

$$
\frac{-x+6}{(x-2)(2 x-3)}=\frac{\mathrm{A}}{x-2}+\frac{\mathrm{B}}{2 x-3}
$$

or

$$
-x+6=A(2 x-3)+B(x-2) \text { which is true for all } x
$$

Putting $x=2$, we get

$$
-2+6=A(4-3)+B \times 0 \Rightarrow A=4
$$

and Putting

$$
x=\frac{3}{2}, \text { we get }-\frac{3}{2}+6=A(0)+B\left(\frac{3}{2}-2\right)
$$

or

$$
\frac{9}{2}=B\left(-\frac{1}{2}\right) \Rightarrow B=-9
$$

Thus $\int \frac{-x+6}{(x-2)(2 x-3)} d x=\int\left(\frac{4}{x-2}+\frac{-9}{2 x-3}\right) d x$

$$
\begin{aligned}
& =4 \int(x-2)^{-1} 1 \cdot d x-\frac{9}{2} \int(2 x-3)^{-1} \cdot 2 d x \\
& =4 \ln (x-2)-\frac{9}{2} \ln (2 x-3)+c,(x>2)
\end{aligned}
$$

Example 2: $\quad$ Evaluate $\int \frac{2 x^{3}-9 x^{2}+12 x}{2 x^{2}-7 x+6} d x, \quad(x>2)$
Solution: After performing the division by the denominator, we get

$$
\begin{aligned}
\int \frac{2 x^{3}-9 x^{2}+12 x}{2 x^{2}-7 x+6} d x & =\int\left(x-1+\frac{-x+6}{2 x^{2}-7 x+6}\right) d x \\
& =\int x d x-\int 1 d x+\int \frac{4}{(x-2)} d x+\int \frac{-9}{2 x-3} d x, \quad \text { (See the Example 1) } \\
& =\frac{x^{2}}{2}-x+4 \ln (x-2)-\frac{9}{2}(2 x-3)+c,(x>2)
\end{aligned}
$$

Example 3: Evaluate (i) $\int \frac{2 a}{x^{2}-a^{2}} d x,(x>a)$
(ii) $\int \frac{2 a}{a^{2}-x^{2}} d x,(x<a)$

Solution: (i) The denominator $x^{2}-a^{2}=(x-a)(x+a)$,
Let $\frac{2 a}{(x-a)(x+a)}=\frac{A}{x-a}+\frac{B}{x+a}$

$$
=\frac{1}{x-a}-\frac{1}{x+a}, \text { (Applying the method of partial fractions) }
$$

Thus $\int \frac{2 a}{(x-a)(x+a)} d x=\int\left(\frac{1}{x-a}-\frac{1}{x+a}\right) d x=\int(x-a)^{-1} \cdot 1 d x+(x-a)^{-1} \cdot 1 d x$

$$
=\ln |x-a|-\ln |x+a|+c=\ln \frac{|x-a|}{|x+a|}+c, \quad(x>a)
$$

(ii) It is left as an exercise.

## EXAMPLES OF CASE II

Example 4: Evaluate $\int \frac{7}{(x-1)} \frac{1}{(x+1)} d x \quad(x \quad 1)$
Solution: We write

$$
\begin{aligned}
& \int \frac{7 x-1}{(x-1)^{2}(x+1)} d x=\frac{A}{x-1}+\frac{B}{(x-1)^{2}}+\frac{C}{x+1} \\
& =\frac{2}{x-1}+\frac{3}{(x-1)^{2}}-\frac{2}{x+1} \quad \text { Applying the method } \\
& \text { of Partial Fractions } \\
& \text { Thus } \int \frac{7 x-1}{(x-1)^{2}(x+1)} d x=\int\left[\frac{2}{x-1}+\frac{3}{(x-1)^{2}}-\frac{2}{x+1}\right] d x \\
& =2 \int(x-1)^{-1} \cdot 1 d x+3 \int(x-1)^{-2} \cdot 1 d x-2 \int(x+1)^{-1} \cdot 1 d x \\
& =2 \ln (x-1)+3 \frac{(x-1)^{-2+1}}{-2+1}-2 \ln (x+1)+c \quad(x>1)
\end{aligned}
$$

$$
\begin{aligned}
& =2[\ln (x-1)-\ln (x+1)]+3\left[\frac{(x-1)^{-2}}{-1}\right] \quad c \\
& =2 \ln \left(\frac{x-1}{x+1}\right)-\frac{3}{x-1}+c
\end{aligned}
$$

Example 5: Evaluate $\int \frac{e^{x}\left(x^{2}+1\right)}{(x+1)^{2}} d x$
Solution: $\int \frac{e^{x}\left(x^{2}+1\right)}{(x+1)^{2}} d x=\int e^{x}\left(1-\frac{2}{(x+1)}+\frac{2}{(x+1)^{2}}\right) d x$, (By Partial Fractions)
$\Rightarrow \int \frac{e^{x}\left(x^{2}+1\right)}{(x+1)^{2}} d x=\int e^{x} d x-2 \int \frac{e^{x}}{x+1} d x+2 \int \frac{e^{x}}{(x+1)^{2}} d x$
We integrate by parts the last integral on the right side of (I).

$$
\int e^{x}(x+1)^{-2} d x=\mathrm{e}^{x} \cdot \frac{(x+1)^{-1}}{-1}-\int\left(\frac{(x+1)^{-1}}{-1}\right) \cdot e^{x} d x
$$

or $\int \frac{e^{x}}{(x+1)^{2}} d x=\frac{e^{x}}{x+1} \quad \int \frac{e^{x}}{x+1} d x$
Using (II), (I) becomes

$$
\begin{aligned}
& \int \frac{e^{x}\left(x^{2}+1\right)}{(x+1)^{2}} d x=\int e^{x} d x-2 \int \frac{e^{x}}{x+1} d x+2\left(-\frac{e^{x}}{x+1}+\int \frac{e^{x}}{x+1} d x\right) \\
& =\left(e^{x}+c\right)-2 \int \frac{e^{x}}{x+1} d x-\frac{2 e^{x}}{x+1}+2 \int \frac{e^{x}}{x+1} d x \\
& =e^{x}-\frac{2 e^{x}}{x+1}+c=\frac{x e^{x}+e^{x}-2 e^{x}}{x+1}+c=\frac{e^{x}(x-1)}{x+1}+c
\end{aligned}
$$

Example 6: Evaluate $\int \frac{1}{x^{3}-1} d x$
Solution: The denominator $x^{3}-1=(x-1)\left(x^{2}+x+1\right)$,
version: 1.1

Let $\frac{1}{(x-1)\left(x^{2}+x+1\right)}=\frac{A}{x-1}+\frac{B x+C}{x^{2}+x+1}$

$$
\begin{aligned}
& =\frac{\frac{1}{3}}{x-1}+\frac{\left(-\frac{1}{3}\right) x-\frac{2}{3}}{x^{2}+x+1} \quad \text { (Applying the method of partial fractions) } \\
& =\frac{1}{3} \cdot \frac{1}{x-1} \cdot \frac{1}{3} \cdot \frac{x+2}{x^{2}+x+1}
\end{aligned}
$$

Thus $\frac{1}{(x-1)\left(x^{2}+x+1\right)} d x=\int\left(\frac{1}{3} \cdot \frac{1}{x-1}-\frac{1}{6} \cdot \frac{2 x+4}{x^{2}+x+1}\right) d x$

$$
\begin{aligned}
& =\int\left[\frac{1}{3} \cdot \frac{1}{x-1} 1 . d x-\frac{1}{6} \cdot \frac{2 x+1}{x^{2}+x+1}-\frac{1}{6} \cdot \frac{3}{x^{2}+x+1}\right) d x \\
& =\frac{1}{2} \int(x-1)^{3} d x-\frac{1}{6} \int\left(x^{2}+x+1\right)^{2}(2 x+1) d x-\frac{1}{2} \int \frac{1}{\left(x+\frac{1}{2}\right)^{2}+\left(\frac{\sqrt{3}}{2}\right)^{2}} d x \\
& =\frac{1}{3} \ln |x-1|-\frac{1}{6} \ln \left(x^{2}+x+1\right)-\frac{1}{2} \cdot \frac{1}{\frac{\sqrt{3}}{2}} \operatorname{Tan}^{-1}\left(\frac{x+\frac{1}{2}}{\frac{\sqrt{3}}{2}}\right) \quad c \\
& =\frac{1}{3} \ln |x-1|-\frac{1}{6} \ln \left(x^{2}+x+1\right)-\frac{1}{\sqrt{3}} \operatorname{Tan}^{-1}\left(\frac{2 x+1}{\sqrt{3}}\right) \quad c
\end{aligned}
$$

## Note: $\quad \mathbf{x}^{2} \times \mathbf{x}+\mathbf{1}$ is positive for real values of $\mathbf{x}$.

Example 7: $\quad$ Evaluate $\int \frac{2 x}{x^{2}-1} d x$
Solution: $\quad$ Put $x^{2}=t$, then $2 x d x=d t$ and

$$
\begin{aligned}
\int \frac{2 x}{x^{2}-1} d x & =\int \frac{1}{t^{2}-1} d t=\int \frac{1}{(t-1)\left(t^{2}+t+1\right)} \\
& =\frac{1}{3} \ln |t-1|-\frac{1}{6} \ln \left(t^{2}+t+1\right)-\frac{1}{\sqrt{3}} \operatorname{Tan}^{-1}\left(\frac{2 t+1}{\sqrt{3}}\right) \quad c
\end{aligned}
$$

(See the example 6)

$$
=\frac{1}{3} \ln \left|x^{2}-1\right|-\frac{1}{6} \ln \left(x^{2}+x^{2}+1\right)-\frac{1}{\sqrt{3}} \operatorname{Tan}^{-1}\left(\frac{2 x^{2}+1}{\sqrt{3}}\right) \quad c
$$

Example 8: $\quad$ Evaluate $\int \frac{3}{x\left(x^{2}-1\right)} d x, x \neq 0, x \neq-1$

Solution: Let $\frac{3}{x\left(x^{2}-1\right)}=\frac{A}{x} \quad \frac{B}{x-1} \quad \frac{C x+D}{x+x+1}$

$$
=\frac{-3}{x} \quad \frac{1}{x-1} \quad \frac{2 x+1}{x^{2}+x+1} \quad \text { (By the method of partial fractions) }
$$

Let $\int \frac{3}{x(x-1)\left(x^{2}+x+1\right)} d x=\int\left(\frac{-3}{x}+\frac{1}{x-1}+\frac{2 x+1}{x^{2}+x+1}\right) d x$

$$
\begin{aligned}
& =-3 \int(x)^{-1} 1 . d x+\int(x-1)^{-1} 1 . d x+\int\left(x^{2}+x+1\right)^{-1}(2 x+1) d x \\
& =-3 \ln |x|+\ln |x-1|+\ln \left(x^{2}+x+1\right)+c \\
& =-3 \ln |x|+\ln |x-1|\left(x^{2}+x+1\right)+c \\
& =-3 \ln |x|+\ln \left|x^{2}-1\right|+c
\end{aligned}
$$

Example 9: $\quad$ Evaluate $\int \frac{2 x^{2}+6 x}{\left(x^{2}+1\right)(x+2 x+3)} d x$
Solution: We write
Let $\frac{2 x^{2}+6 x}{\left(x^{2}+1\right)\left(x^{2}+2 x+3\right)}=\frac{A x+B}{x^{2}+1}+\frac{C x+D}{x^{2}+2 x+3}$

$$
=\frac{2 x+1}{x^{2}+1}-\frac{2 x+3}{x^{2}+2 x+3} \text { (Applying the method of partial fractions) }
$$

Thus $\int \frac{2 x^{2}+6 x}{\left(x^{2}+1\right)\left(x^{2}+2 x+3\right)} d x=\int\left(\frac{2 x+1}{x^{2}+1}-\frac{2 x+3}{x^{2}+2 x+3}\right) d x$

$$
=\int \frac{2 x}{x^{2}+1} d x+\int \frac{1}{x^{2}+1}-\int \frac{2 x+2}{x^{2}+2 x+3} d x-\int \frac{1}{x^{2}+2 x+3} d x
$$

$$
\begin{aligned}
& =\int\left(x^{2}+1\right)^{-1}(2 x) d x+\int \frac{1}{x^{2}+1} d x-\int(x+2 x+3)^{-1}(2 x+2) d x-\int \frac{1}{(x+1)^{2}+\sqrt{2} \sqrt{2}} d x \\
& =\ln \left(x^{2}+1\right)+\operatorname{Tan}^{-1} x-\ln \left(x^{2}+2 x+3\right)-\frac{1}{\sqrt{2}} \operatorname{Tan}^{-1} \frac{x+1}{\sqrt{2}} \quad c
\end{aligned}
$$

## EXERCISE 3.5

## Evaluate the following integrals.

1. $\int \frac{3 x+1}{x^{2}-x-6} d x$
2. $\int \frac{5 x+8}{(x+3)(2 x-1)} d x$
3. $\int \frac{x^{2}+3 x-34}{x^{2}+2 x-15} d x$
4. $\int \frac{(a-b) x}{(x-a)(x-b)} d x,(a>b)$
5. $\int \frac{3-x}{1-x-6 x^{2}} d x$
6. $\int \frac{2 x}{x^{2}-a^{2}} d x$
7. $\int \frac{1}{6 x^{2}+5 x-4} d x$
8. $\int \frac{2 x^{2}-3 x^{2}-x-7}{2 x^{2}-3 x-2} d x$
9. $\int \frac{3 x^{2}-12 x+11}{(x-1)(x-2)(x-3)} d x$
10. $\int \frac{2 x-1}{x(x-1)(x-3)} d x$
11. $\int \frac{5 x^{2}+9 x+6}{\left(x^{2}-1\right)(2 x+3)} d x$
12. $\int \frac{4+7 x}{(1+x)^{2}(2+3 x)} d x$
13. $\int \frac{2 x^{2}}{(x-1)^{2}(x+1)} d x$
14. $\int \frac{1}{(x-1)(x+1)^{2}} d x$
15. $\int \frac{x+4}{x^{2}-3 x^{2}+4} d x$
16. $\int \frac{x^{3}-6 x^{2}+25}{(x+1)^{2}(x-2)^{2}} d x$
17. $\int \frac{x^{2}+22 x^{2}+14 x-17}{(x-3)(x+2)^{2}} d x$
18. $\int \frac{x-2}{(x+1)\left(x^{2}+1\right)} d x$
19. $\int \frac{x}{(x-1)\left(x^{2}+1\right)} d x$
20. $\int \frac{9 x-7}{(x+3)\left(x^{2}+1\right)} d x$
21. $\int \frac{1+4 x}{(x-3)\left(x^{2}+4\right)} d x$
22. $\int \frac{12}{+8} d x$
23. $\int \frac{9 x+6}{x^{2}-8} d x$
24. $\int \frac{2 x^{2}+5 x+3}{(x-1)^{2}\left(x^{2}+4\right)} d x$
25. $\int \frac{2 x^{2}-x-7}{(x+2)^{2}\left(x^{2}+x+1\right)} d x$
26. $\int \frac{3 x+1}{\left(4 x^{2}+1\right)\left(x^{2}-x+1\right)} d x$
27. $\int \frac{4 x+1}{\left(x^{2}+4\right)\left(x^{2}+4 x+5\right)} d x$
28. $\int \frac{6 a^{2}}{\left(x^{2}+a^{2}\right)\left(x^{2}+4 a^{2}\right)} d x$
29. $\int \frac{2 x^{2}-2}{\left(x^{4}+x^{2}+1\right)} d x$
30. $\int \frac{3 x-8}{\left(x^{2}-x+2\right)\left(x^{2}+x+2\right)} d x$
31. $\int \frac{3 x^{3}+4 x^{2}+9 x+5}{\left(x^{2}+x+1\right)\left(x^{2}+2 x+3\right)} d x$