### 7.1 Fundamental Principle of Counting

Danish wants to prepare invitation cards of 5 different colours (red, blue, green, orange and yellow) by changing any of 3 shapes (circle, square and rectangle). How many cards can Danish make?
The problem is to count the total number of ways in which Danish can make cards. One way to find the solution is by making tree diagram. Let us discuss another scenario: Danish's father wants to buy a table and has asked his son to help him decide. He narrowed down his options for manufacturer, types of material (wood, plastic, glass and marble) and types of shape (circle, square and rectangle). Find the total number of table choices from the above options.
Again the problem is to count the total number of ways in which Danish's father can choose a table.

$1^{\text {st }}$ Way: By making tree diagram.
From tree diagram, it is clearer there are 12 choices for Danish's father to buy a table with one type of material and one type of shape.
$2^{\text {nd }}$ Way: By multiplying, Danisth's father can find the total number of table choices to buy a table with one kind of material and shape.
Total number of table choices $=$ Total types of material $\times$ Total types of shape

$$
=4 \times 3=12 \text { choices }
$$

These examples show that when making a choice involving multiple stages or categories, we can find the total number of outcomes by multiplying the number of options at each stage.

# Statement

Suppose $A$ and $B$ are two events, the event $A$ occurs in $m$ different ways, and the event $B$ occurs in $n$ different ways then the total number of ways that the two events one after another can occur in $m \times n$ ways.

$$
\text { Total number of ways }=m n
$$

Proof: Let $A=\left\{a_{1}, a_{2}, a_{3}, \cdots, a_{m}\right\}$ and $B=\left\{b_{1}, b_{2}, b_{3}, \cdots, b_{n}\right\}$. Let $P$ denotes the event that both events $A$ and $B$ occur together then $P=\left\{\left(a_{i}, b_{j}\right): a_{i} \in A, b_{j} \in B, 1 \leq i \leq m\right.$, $1 \leq j \leq n\}=A \times B$. Hence the number of ways in which both events $A$ and $B$ can occur is the number of elements in $A \times B$ which is $m n$.
This principle can be extended to three or more events. For instance, if event $A$ can occur in $m$ ways, event $B$ can occur in $n$ ways and event $C$ can occur in $k$ ways, the number of ways that three events can occur all together is the

## Try yourself!

If three dice are rolled together, how many total numbers of ways occur?

product $m \cdot n \cdot k$.

## Factorial (I)

Suppose there are four chairs to be occupied by four students and we are interested in counting all the possible ways the students can be seated.
To occupy the first chair there are 4 options. For the second chair, only 3 students remain, so there are 3 options. Similarly, for the third and fourth chairs, there are 2 and 1 options respectively.

In this way, we have to perform four independent events with $4,3,2$, and 1 options respectively.
By the Fundamental Principle of Counting, the total number of ways to occupy all the chairs is $4 \cdot 3 \cdot 2 \cdot 1=24$
Such problems frequently occur in daily life, where we have to multiply the first $n$ natural numbers: $1,2,3, \cdots, n$.
We call this product the factorial of $n$ and denote it by $n!$ or $\mid n$, thus for a natural number $n$ :

$$
n!\text { or } \quad \underline{n}=n(n-1)(n-2) \cdots 3 \cdot 2 \cdot 1
$$

For some reason we also define $0!=1$. In general, if $n$ is a non-negative integer, then its factorial is denoted and defined as

$$
n!=\mid \underline{n}= \begin{cases}1 & \text { if } n=0 \\ n(n-1)(n-2) \ldots 3 \cdot 2 \cdot 1 & \text { if } n \geq 1\end{cases}
$$

For example,

$$
\begin{aligned}
& 1!=1 \\
& 2!=2 \cdot 1=2 \\
& 3!=3 \cdot 2 \cdot 1=6 \\
& 4!=4 \cdot 3 \cdot 2 \cdot 1=24 \\
& 5!=5 \cdot 4 \cdot 3 \cdot 2 \cdot 1=120 \\
& 6!=6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1=720
\end{aligned}
$$

Challenged
Can you find out $\frac{81}{3!}$ ?

It can be easily observed that

$$
n!=n(n-1)!\text { for } n \geq 1
$$

Example 1 Evaluate $\frac{8!}{6!}$
Solution $\frac{8!}{6!}=\frac{8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}=56$
Example 2 Write $8 \cdot 7 \cdot 6 \cdot 5$ in the factorial form.

Solution $8 \cdot 7 \cdot 6 \cdot 5=\frac{8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{4 \cdot 3 \cdot 2 \cdot 1}=\frac{8!}{4!}$ or $\frac{9!}{6!3!}=\frac{9 \cdot 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 \cdot 3 \cdot 2 \cdot 1}=84$

# EXERCISE 7.1

1. Evaluate each of the following:
(i) $\frac{10!}{0!8!}$
(ii) $\frac{12!}{3!(12-3)!}$
(iii) $\frac{1440}{3!4!}+\frac{2400}{5!2!}$
(iv) $\frac{(n+2)!}{(n+1)!}$
2. Write each of the following in the factorial form:
(i) $n^{2}-n$
(ii) $n(n-1)(n-2) \cdots(n-r+1)$
3. Find $n$, if $(n+4)!=3024 \cdot n!$.
4. If $\frac{1}{7!}+\frac{1}{8!}=\frac{x}{9!}$, find $x$.
5. Prove that: $\frac{(2 n+1)!}{n!}=[1 \cdot 3 \cdot 5 \cdots(2 n-1)(2 n+1)] 2^{n}$
6. Express as a single fraction: $\frac{(n+2)!}{(r+2)!}+\frac{(n+1)!}{(r+1)!}$.
7. There are four distinct colored balls and four boxes of same colors as those of the balls. Determine the number of possible ways the balls, one each in a box, can be placed such that a ball does not go to a box of its own colour?