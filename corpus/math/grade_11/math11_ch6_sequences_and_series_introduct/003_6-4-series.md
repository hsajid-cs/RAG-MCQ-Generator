### 6.4 Series

The sum of the terms of a sequence is called the series of the corresponding sequence.
For example, $1+2+3+\cdots+n$ is a finite series of first $n$ natural numbers.
The sum of first $n$ terms of series is denoted by $S_{n}$.
We write, $S_{n}=a_{1}+a_{2}+\cdots+a_{n}$.
Here, $\quad S_{1}=a_{1}$

$$
\begin{aligned}
& S_{2}=a_{1}+a_{2} \\
& S_{3}=a_{1}+a_{2}+a_{3} \\
& S_{n}=a_{1}+a_{2}+a_{3}+\cdots+a_{n} \text { is known as } n^{\text {th }} \text { partial sum. }
\end{aligned}
$$

The sum of the terms of an arithmetic sequence is called an arithmetic series.
To develop a formula for the sum of any arithmetic series, consider

$$
\begin{aligned}
S_{n} & =a_{1}+\left(a_{1}+d\right)+\left(a_{1}+2 d\right)+\cdots+\left(a_{n}-2 d\right)+\left(a_{n}-d\right)+a_{n} \\
S_{n} & =a_{n}+\left(a_{n}-d\right)+\left(a_{n}-2 d\right)+\cdots+\left(a_{1}+2 d\right)+\left(a_{1}+d\right)+a_{1}
\end{aligned}
$$

Thus, $\quad 2 S_{n}=\left(a_{1}+a_{n}\right)+\left(a_{1}+a_{n}\right)+\left(a_{1}+a_{n}\right)+\cdots+\left(a_{1}+a_{n}\right)+\left(a_{1}+a_{n}\right)+\left(a_{1}+a_{n}\right)$

$$
=n\left(a_{1}+a_{n}\right) \quad\left[\text { We have } n \text { terms of }\left(a_{1}+a_{n}\right)\right]
$$

$$
S_{n}=\frac{n}{2}\left(a_{1}+a_{n}\right)
$$

But, $\quad a_{n}=a_{1}+(n-1) d$
Thus, $\quad S_{n}=\frac{n}{2}\left[a_{1}+a_{1}+(n-1) d\right]=\frac{n}{2}\left[2 a_{1}+(n-1) d\right]$

Example 7 Find the sum of the first 100 positive integers.
Solution The series is $1+2+3+\cdots+100$.
Since we can see that $a_{1}=1, a_{n}=100$ and $d=1$.

## Method-1

$$
\begin{aligned}
& S_{n}=\frac{n}{2}\left(a_{1}+a_{n}\right) \\
& S_{100}=\frac{100}{2}(1+100) \\
& S_{100}=50(101) \\
& S_{100}=5050
\end{aligned}
$$

## Method-2

$$
\begin{aligned}
& S_{n}=\frac{n}{2}\left[2 a_{1}+(n-1) d\right] \\
& S_{100}=\frac{100}{2}[2(1)+(100-1) 1] \\
& S_{100}=50(101) \\
& S_{100}=5050
\end{aligned}
$$

Example 8 Find the $19^{\text {th }}$ term and the partial sum of 19 terms of the arithmetic series:

$$
2+\frac{7}{2}+5+\frac{13}{2}+\cdots
$$

Solution Here, $a_{1}=2, a_{2}=\frac{7}{2}$ and $d=a_{2}=a_{1}=\frac{7}{2}-2=\frac{3}{2}$
Using $\quad a_{n}=a_{1}+(n-1) d$
Substitute $n=19$

$$
\begin{aligned}
& a_{19}=2+(19-1) \frac{3}{2} \\
& 2+18\left(\frac{3}{2}\right)=2+27=29
\end{aligned}
$$

Using $\quad S_{n}=\frac{n}{2}\left(a_{1}+a_{n}\right)$

$$
S_{19}=\frac{19}{2}\left(a_{1}+a_{19}\right)
$$

$$
S_{19}=\frac{19}{2}(2+29)=\frac{19}{2}(31)=\frac{589}{2}
$$

Example 9 Find the arithmetic series if its fifth term is 19 and $S_{4}=a_{9}+1$.
Solution Given that $a_{5}=19$, that is,

$$
a_{1}+4 d=19
$$

Using the other given condition, we have

$$
S_{4}=\frac{4}{2}\left[2 a_{1}+(4-1) d\right]=a_{9}+1
$$

$$
\begin{aligned}
4 a_{1}+6 d & =a_{1}+8 d+1 \\
3 a_{1}-1 & =2 d
\end{aligned}
$$

Substituting $2 d=3 a_{1}-1$ in (i), we have

$$
\begin{aligned}
a_{1}+2\left(3 a_{1}-1\right) & =19 \\
7 a_{1}=21 & \Rightarrow a_{1}=3
\end{aligned}
$$

From (i), we have,

$$
\begin{aligned}
4 d & =19-a_{1}=19-3=16 \\
\Rightarrow \quad d & =4
\end{aligned}
$$

Thus, the series is $3+7+11+\cdots$.
Example10 How many terms of the series $-9-6-3+0+\ldots$ amount to 66 ?
Solution Here, $a_{1}=-9$ and $d=-6-(-9)=3$.

$$
\text { Let } S_{n}=66
$$

Using $S_{n}=\frac{n}{2}\left[2 a_{1}+(n-1) d\right]$, we have

$$
\begin{aligned}
& 66=\frac{n}{2}[2(-9)+(n-1) 3] \\
& 132=n[3 n-21] \Rightarrow 132=3 n(n-7) \Rightarrow 44=n(n-7) \\
& n^{2}-7 n-44=0 \\
& \Rightarrow \quad n=\frac{7 \pm \sqrt{49+176}}{2} \\
& =\frac{7 \pm \sqrt{225}}{2}=\frac{7 \pm 15}{2} \Rightarrow n=11,-4
\end{aligned}
$$

But $n$ cannot be negative in this case, so $n=11$, that is, the sum of eleven terms is 66 .
Example11 Find the first three terms of an arithmetic series in which $a_{1}=9, a_{n}=105$ and $S_{n}=741$.
Solution Step - I: Since we know $a_{1}, a_{n}$ and $S_{n}$,
We use $S_{n}=\frac{n}{2}\left(a_{1}+a_{n}\right)$ to find $n$.

$$
741=\frac{n}{2}(9+105)
$$

$$
741=57 n
$$

$$
13=n
$$

Step - II: Find $d$.

$$
\begin{aligned}
& a_{n}=a_{1}+(n-1) d \\
& 105=9+(13-1) d \\
& 96=12 d \\
& 8=d
\end{aligned}
$$

Step - III: Use $d$ to determine $a_{2}$ and $a_{3}$.

$$
a_{2}=9+8=17, \quad a_{3}=17+8=25
$$

The first three terms are 9,17 and 25 .

# EXERCISE 6.4

1. Sum the series:
(i) $3+6+9+\cdots+a_{20}$
(ii) $\frac{4}{\sqrt{5}}+\sqrt{5}+\frac{6}{\sqrt{5}}+\cdots+a_{n}$
2. Find $S_{n}$ for each arithmetic series:
(i) $a_{1}=4, n=25, a_{n}=100$
(ii) $a_{1}=40, n=20, d=-1$
(iii) $a_{n}=52, n=21, d=-4$
3. Find $a_{1}$ for the arithmetic series: $d=8, n=19, S_{n}=1786$.
4. How many terms of the series: $96+93+90+\sim$ amount to 1071.
5. If the three sides of a right-angled triangle having perimeter 36 cm are in A.P., find them.
6. Sum the series
(i) $3+5-7+9+11-13+15+17-19+\cdots$ to $3 n$ terms.
(ii) $1+4-7+10+13-16+19+22-25+\cdots$ to $3 n$ terms.
7. Find the sum of 20 terms of the series whose $r^{\text {th }}$ term is $3 r+1$.
8. The $5^{\text {th }}$ and $9^{\text {th }}$ term of an A.P. are 11 and 17 respectively. Find the sum of 20 terms.
9. Obtain the sum of all integers in the first 1000 positive integers which are neither divisible by 5 nor by 2 .
10. The sum of 9 terms of an A.P. is 171 and its eighth term is 31 . Find the series.
11. The $5^{\text {th }}$ term of an arithmetic progression is 21 and the sum of first six terms is 90 . Find the $18^{\text {th }}$ term.
12. The sum of three numbers in an A.P. is 24 and their product is 440 . Find the numbers.
13. The first four terms of an A.P. are $2,6,10$ and 14 . Find the least number of terms needed so that the sum of the terms is greater than 2000.
14. Find four numbers in A.P. whose sum is 32 and the sum of whose squares is 276.
15. Find the five numbers in A.P. whose sum is 25 and the sum of whose squares is 135 .
16. If $\frac{1}{a+b} \cdot \frac{1}{c+a} \cdot \frac{1}{b+c}$ are in A.P. then show that $a^{2}, b^{2}, c^{2}$ are in A.P.

17. The sum of the first four terms of an A.P. is 56 . The sum of the last four terms is 112. If its first term is 11 , then find number of terms.
18. The first, second and last terms of an A.P. are $a, b$ and $c$ respectively. Show that the sum of A.P. is $\frac{(b+c-2 a)(c+a)}{2(b-a)}$.
19. Show that the sum of $n$ A.Ms. between $a$ and $b$ is $n$ times the single A.M. between them.

# 6.5 Geometric Progression (G.P.)

A geometric progression or geometric sequence is a sequence fixed in which each term after the first is found by multiplying the previous term by a non-zero constant $r$ called common ratio.
Like arithmetic progression, we can label the terms of a geometric sequence as $a_{1}, a_{2}, a_{3}$ and so on, $a_{1} \neq 0$. The $n^{\text {th }}$ term is $a_{n}$ and the previous term is $a_{n-1}$. So, $a_{n}=r\left(a_{n-1}\right)$. Thus, $r=\frac{a_{n}}{a_{n-1}}$. That is, the common ratio can be found by dividing any term by its previous term.