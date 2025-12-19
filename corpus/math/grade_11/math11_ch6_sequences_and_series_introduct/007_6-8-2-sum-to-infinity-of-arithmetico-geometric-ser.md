### 6.8.2 Sum to Infinity of Arithmetico-Geometric Series

If $|r|<1$, then $r^{n} \rightarrow 0$ and $n r^{n} \rightarrow 0$ as $n \rightarrow \infty$
Therefore, (iii) reduces to $S_{\infty}=\frac{a b}{1-r}+\frac{d b r}{(1-r)^{2}}$
which is the sum to infinity of arithmetico-geometric series.

Example 19 Sum the series upto $n$ terms: $2 \cdot 1+3 \cdot 2+4 \cdot 4+5 \cdot 8+\cdots$
Solution Let $S_{n}=2 \cdot 1+3 \cdot 2+4 \cdot 2^{2}+5 \cdot 2^{3}+\cdots$ to $n$ terms
$n^{\text {th }}$ term of the A.P., $2,3,4,5, \cdots$ is $a_{1}+(n-1) d=2+(n-1)(1)$

$$
=2+n-1=n+1
$$

$n^{\text {th }}$ term of the G.P., $1,2,2^{2}, 2^{3}, \cdots$ is $a_{1} r^{n-1}=1 \cdot 2^{n-1}=2^{n-1}$
So, $\quad S_{n}=2 \cdot 1+3 \cdot 2+4 \cdot 2^{2}+5 \cdot 2^{3}+\cdots+(n+1) 2^{n-1}$
Multiplying both sides by common ratio of G.P., we get

$$
2 S_{n}=\quad 2 \cdot 2+3 \cdot 2^{2}+4 \cdot 2^{3}+5 \cdot 2^{4}+\cdots+(n) 2^{n-1}+(n+1) 2^{n}
$$

Subtracting (ii) from (i), we get

$$
\begin{aligned}
S_{n}-2 S_{n} & =2 \cdot 1+(3-2) \cdot 2+(4-3) \cdot 2^{2}+(5-4) \cdot 2^{3}+\cdots+(n+1-n) 2^{n-1}-(n+1) 2^{n} \\
-S_{n} & =2 \cdot 1+1 \cdot 2+1 \cdot 2^{2}+1 \cdot 2^{3}+\cdots+1 \cdot 2^{n-1}-(n+1) 2^{n} \\
-S_{n} & =2+\left\{2+2^{2}+2^{3}+\cdots+2^{n-1}\right\}-(n+1) 2^{n} \\
-S_{n} & =2+\frac{2\left(2^{n-1}-1\right)}{2-1}-(n+1) \cdot 2^{n} \\
-S_{n} & =2+2^{n}-2-n \cdot 2^{n}-2^{n} \\
-S_{n} & =-n \cdot 2^{n} \\
S_{n} & =n \cdot 2^{n}
\end{aligned}
$$

Example 20 Sum the series upto $n$ terms: $2+\frac{4}{3}+\frac{6}{9}+\frac{8}{27}+\cdots$
Solution Let $S_{n}=2+\frac{4}{3}+\frac{6}{9}+\frac{8}{27}+\cdots$ to $n$ terms
$n^{\text {th }}$ term of the A.P., $2,4,6,8, \ldots$ is $2+(n-1)(2)$

$$
=2+2 n-2=2 n
$$

$n^{\text {th }}$ term of the G.P., $1, \frac{1}{3}, \frac{1}{9}, \frac{1}{27}, \cdots$ is $(1)\left(\frac{1}{3}\right)^{-1}=\frac{1}{3^{n-1}}$
So, $\quad S_{n}=2+\frac{4}{3}+\frac{6}{9}+\frac{8}{27}+\cdots+\frac{2 n}{3^{n-1}}$

$$
\frac{1}{3} S_{n}=\frac{2}{3}+\frac{4}{9}+\frac{6}{27}+\cdots+\frac{2 n-2}{3^{n-1}}+\frac{2 n}{3^{n}}
$$

Subtracting (ii) from (i), we get

$$
\begin{aligned}
& \left(1-\frac{1}{3}\right) S_{n}=2+\frac{4-2}{3}+\frac{6-4}{9}+\frac{8-6}{27}+\cdots+\frac{2 n-2 n+2}{3^{n-1}}-\frac{2 n}{3^{n}} \\
& \frac{2}{3} S_{n}=2+\left[\frac{2}{3}+\frac{2}{9}+\frac{2}{27}+\cdots+\frac{2}{3^{n-1}}\right]-\frac{2 n}{3^{n}} \\
& \frac{2}{3} S_{n}=2+\left[\frac{\frac{2}{3}\left\{1-\left(\frac{1}{3}\right)^{n-1}\right\}}{1-\frac{1}{3}}\right]-\frac{2 n}{3^{n}} \\
& =2+\frac{\frac{2}{3}\left\{1-\left(\frac{1}{3}\right)^{n-1}\right\}}{\frac{2}{3}}-\frac{2 n}{3^{n}} \\
& =2+1-\left(\frac{1}{3}\right)^{n-1}-2 n\left(\frac{1}{3}\right)^{n} \\
& \frac{2}{3} S_{n}=3-\left(\frac{1}{3}\right)^{n-1}-2 n\left(\frac{1}{3}\right)^{n} \\
& S_{n}=\frac{9}{2}-\frac{3}{2}\left(\frac{1}{3}\right)^{n-1}-3 n\left(\frac{1}{3}\right)^{n}
\end{aligned}
$$

Example 21 Find the sum to $n$ terms of the series: $1+2 x+3 x^{2}+4 x^{3}+\ldots$ where $x \neq 1$. If $|x|<1$, sum the series to infinity.
Solution Let $S_{n}=1+2 x+3 x^{2}+4 x^{3}+\cdots+n x^{n-1}$

$$
\therefore \quad x S_{n}=\quad x+2 x^{2}+3 x^{3}+\cdots+(n-1) x^{n-1}+n x^{n}
$$

Subtracting (ii) from (i), we get

$$
\begin{aligned}
(1-x) S_{n} & =1+x+x^{2}+x^{3}+\cdots+x^{n-1}-n x^{n} \\
& =\frac{1\left(1-x^{n}\right)}{1-x}-n x^{n} \\
& =\frac{1-x^{n}-n(1-x) x^{n}}{1-x}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1-x^{n}-n x^{n}+n x^{n+1}}{1-x} \\
(1-x) S_{n} & =\frac{1-(n+1) x^{n}+n x^{n+1}}{1-x} \\
S_{n} & =\frac{1-(n+1) x^{n}+n x^{n+1}}{(1-x)^{2}}
\end{aligned}
$$

If $|x|<1$, then $x^{n} \rightarrow 0, n x^{n} \rightarrow 0$ as $n \rightarrow \infty$

$$
\therefore \quad S_{\infty}=\frac{1}{(1-x)^{2}}
$$

# EXERCISE 6.8

1. Find the $8^{\text {th }}$ term of the arithmetico-geometric sequence, where the arithmetic part is $1,4,7, \ldots$ and the geometric part is $5,10,20$.
2. Find the $n^{\text {th }}$ term of the arithmetico-geometric sequence, where the arithmetic part is $3,7,11, \ldots$ and the geometric part is $3,6,18, \cdots$.
3. Consider the arithmetico-geometric sequence defined by arithmetic part:
$a_{n+1}=2 n+5$ and geometric part $b_{n-2}=\frac{1}{9}(-3)^{n}$. Find the $n^{\text {th }}$ term and the sum of first three terms of the arithmetico-geometric sequence.
4. Sum to $n$ terms the following series:
(i) $1 \cdot 2+3 \cdot 4 \pm 5 \cdot 8+7 \cdot 16+\cdots$
(ii) $2 \cdot 3+4 \cdot 3^{2}+6 \cdot 3^{3}+8 \cdot 3^{4}+\ldots$
(iii) $2+\frac{5}{4}+\frac{8}{4^{2}}+\frac{11}{4^{3}}+\cdots$
(iv) $1+\frac{3}{5}+\frac{5}{5^{2}}+\frac{7}{5^{3}}+\cdots$
(v) $1+\frac{4}{3}+\frac{7}{9}+\frac{10}{27}+\cdots$
5. Sum the following infinite series:
(i) $1+\frac{3}{2}+\frac{5}{4}+\frac{7}{8}+\cdots$
(ii) $2+\frac{5}{3}+\frac{8}{9}+\frac{11}{27}+\cdots$
6. Show that $2^{\frac{1}{2}} \cdot 4^{\frac{1}{4}} \cdot 8^{\frac{1}{8}} \cdot 16^{\frac{1}{16}} \cdots \infty=4$
7. Show that $\sqrt{4} \cdot \sqrt[4]{16} \cdot \sqrt[8]{64} \cdot \sqrt[10]{256} \cdots \infty=16$

8. Sum to $n$ terms the series $2+4 x+6 x^{2}+8 x^{3}+\cdots$ where $x \neq 1$
9. Find the sum to $n$ terms of the series: $\frac{2 n+1}{2 n-1}+3\left(\frac{2 n+1}{2 n-1}\right)^{2}+5\left(\frac{2 n+1}{2 n-1}\right)^{3}+\cdots$
10. Prove that $1+2\left(1+\frac{1}{n}\right)+3\left(1+\frac{1}{n}\right)^{2}+\cdots$ to $n$ terms $=n^{2}$
11. Sum the series to $n$ terms $2+5 x+8 x^{2}+11 x^{3}+\cdots$ and deduce the sum to infinity if $|x|<1$.

# 6.9 Harmonic Progression (H.P.)

A sequence of numbers is called a Harmonic Sequence or Harmonic Progression if the reciprocals of its terms are in arithmetic progression. The sequence $1, \frac{1}{3}, \frac{1}{5}, \frac{1}{7}$ is a harmonic sequence since their reciprocals $1,3,5,7$ are in A.P.
Remember that the reciprocal of zero is not defined, so zero cannot be the term of a harmonic sequence.

The general form of the harmonic sequence is $\frac{1}{a_{1}}, \frac{1}{a_{1}+d}, \frac{1}{a_{1}+2 d}, \cdots, \frac{1}{a_{1}+(n-1) d}$.
Example 22 Find the $n^{\text {th }}$ and $8^{\text {th }}$ terms of H.P. : $\frac{1}{2}, \frac{1}{5}, \frac{1}{8}, \cdots$
Solution The reciprocals of the terms of the sequence,

$$
\frac{1}{2}, \frac{1}{5}, \frac{1}{8}, \cdots \quad \text { are } 2,5,8, \cdots
$$

The numbers $2,5,8, \cdots$ are in A.P., so

$$
a_{1}=2 \text { and } d=5-2=3
$$

Putting these values in $a_{n}=a_{1}+(n-1) d$, we have

$$
\begin{aligned}
a_{n} & =2+(n-1) 3 \\
& =3 n-1
\end{aligned}
$$

Thus, the $n^{\text {th }}$ term of the given sequence $=\frac{1}{a_{n}}=\frac{1}{3 n-1}$ and substituting $n=8$ in $\frac{1}{3 n-1}$,

we get the $8^{\text {th }}$ term of the given H.P. which is $\frac{1}{3 \times 8-1}=\frac{1}{23}$.
Alternatively, $a_{8}$ of the A.P. $=a_{1}+(8-\mathrm{I}) d$

$$
\begin{aligned}
& =2+7(3) \\
& =23
\end{aligned}
$$

Thus, the $8^{\text {th }}$ term of the given H.P. $=\frac{1}{23}$
Example 23 If the $4^{\text {th }}$ and $7^{\text {th }}$ terms of the H.P. are $\frac{2}{13}$ and $\frac{2}{25}$ respectively, find the sequence.
Solution Since the $4^{\text {th }}$ term of the H.P. $=\frac{2}{13}$ and its $7^{\text {th }}$ term $=\frac{2}{25}$, therefore the $4^{\text {th }}$ and $7^{\text {th }}$ terms of the corresponding A.P. are $\frac{13}{2}$ and $\frac{25}{2}$ respectively.
Now taking $a_{1}$, the first term and $d$, the common difference of the corresponding A.P., we have,

$$
a_{1}+3 d=\frac{13}{2}
$$

and $\quad a_{1}+6 d=\frac{25}{2}$
Subtracting (i) from (ii), gives

$$
3 d=\frac{25}{2}-\frac{13}{2}=6 \Rightarrow d=2
$$

From (i), we get

$$
\begin{aligned}
a_{1} & =\frac{13}{2}-3 d \\
& =\frac{13}{2}-6 \\
& =\frac{1}{2}
\end{aligned}
$$

Thus, $\quad a_{2}$ of the A.P. $=a_{1}+d=\frac{1}{2}+2=\frac{5}{2}$
and $\quad a_{3}$ of the A.P. $=a_{1}+2 d=\frac{1}{2}+2(2)$

$$
\begin{aligned}
& =\frac{1}{2}+4 \\
& =\frac{9}{2}
\end{aligned}
$$

Hence the required H.P. is $\frac{2}{1}, \frac{2}{5}, \frac{2}{9}, \frac{2}{13}, \ldots$

# 6.9.1 Harmonic Mean (H.M.)

A number $H$ is said to be the harmonic mean (H.M.) between two numbers $a$ and $b$ if $a, H, b$ are in H.P.

Let $a, b$ be the two numbers and $H$ be their H.M. Then $\frac{1}{a}, \frac{1}{H}, \frac{1}{b}$ are in A.P.
Therefore, $\quad \frac{1}{H}=\frac{\frac{1}{a}+\frac{1}{b}}{2}=\frac{b+a}{a b}=\frac{a+b}{2 a b}$.
and $\quad H=\frac{2 a b}{a+b}$
For example, H.M. between 3 and 7 is

$$
\frac{2 \times 3 \times 7}{3+7}=\frac{2 \times 21}{10}=\frac{21}{5}
$$