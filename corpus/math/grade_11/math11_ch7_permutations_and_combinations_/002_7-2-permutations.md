### 7.2 Permutations

One important application of the fundamental principle of counting is to determine the number of ways that objects can be arranged in order.
Definition: An arrangement of all or part of set of objects in a specific order is called a permutation. Number of permutations of $r(\leq n)$ objects taken from a set of $n$ objects is written as ${ }^{\circ} P_{r}$ or $P\left(n_{r} r_{r}\right)$.

$$
{ }^{\circ} P_{r}=\frac{n!}{(n-r)!} \quad \text { when } r \leq n
$$

According to fundamental principle of counting:
(i) Three books of mathematics for grades 1,2 and 3 can be arranged in a row taken all at a time (if books are distinct)

$$
\begin{aligned}
{ }^{\circ} P_{r} & ={ }^{3} P_{3} & \because n=r \approx 3 \\
& =\frac{3!}{(3-3)!}=\frac{3!}{0!} & \because 0!=1 \\
& =3!=3 \cdot 2 \cdot 1=6 \text { ways }
\end{aligned}
$$

(ii) Number of ways of writing the letters of the WORD taken all at a time
$$
\begin{aligned}
& { }^{n} P_{r}={ }^{4} P_{4} \\
& n=r=4 \\
& n=\text { Total number of things/objects } \\
& =\frac{4!}{(4-4)!}=\frac{4!}{0!} \\
& r=\text { The number of selected things / objects } \\
& =4!=4 \cdot 3 \cdot 2 \cdot 1=24 \text { ways }
\end{aligned}
$$

| Challenge! | Do you know! |
| :-- | :-- |
| Can you make total number of <br> permutations for the "WORD" <br> pictorially? | In 1974, "fimo Rubik" invented a popular <br> puzzle, each turn of the puzzle shows a <br> permutation of the different colours. The <br> name of this puzzle is "Rubik's Cube". |

Theorem: Prove that: ${ }^{n} P_{r}=n(n-1)(n-2) \cdots(n-r+1)=\frac{n!}{(n-r)!}$
Proof: As there are $n$ different objects to fill up $r$ places. So, the first place can be filled in $n$ ways. Since repetitions are not allowed, so after placing one object we are left with $(n-1)$ objects, thus the second place can be filled in $(n-1)$ ways. Similarly the third place can be filled in $(n-2)$ ways, and so on. This continues until the $r^{\text {th }}$ place which can be filled in $n-(r-1)=n-r+1$ ways. Therefore, by the Fundamental Principle of Counting, $r$ places can be filled by $n$ different objects in $n(n-1)(n-2) \cdots(n-r+1)$ ways.

$$
\begin{aligned}
{ }^{n} P_{r} & =n(n-1)(n-2) \ldots(n-r+1) \\
& =\frac{n(n-1)(n-2) \ldots(n-r+1)(n-r)!}{(n-r)!} \\
{ }^{n} P_{r} & =\frac{n!}{(n-r)!}
\end{aligned}
$$

Example 4 How many different 4-digit numbers can be formed out from the digits $1,2,3,4,5,6$, when no digit is repeated?
Solution The total number of digits $=6$
The digits forming each number $=4$
So, the required number of 4-digit numbers is given by:

$$
{ }^{6} P_{4}=\frac{6!}{(6-4)!}=\frac{6!}{2!}=\frac{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{2.1}=6 \cdot 5 \cdot 4 \cdot 3=360
$$

Example 5 In how many ways can a set of 4 different mathematics books, 3 different physics books and 2 different chemistry books be placed on a shelf with a space for 9 books, if:
(a) all the books are kept without any restriction.

(b) all the books of the same subject are kept together.
(c) only the mathematics books are kept together.

# Soiation

(a) all the books are kept without any restriction.
Total number of books $=4+3+2=9$

$$
\begin{aligned}
& { }^{9} P_{2}=9!=9 \cdot 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 \quad 91 \text { ways } \\
& =362880 \text { ways }
\end{aligned}
$$

(b) all the books of the same subject are kept together.

$$
\begin{aligned}
& { }^{4} P_{4} \cdot{ }^{3} P_{3} \cdot{ }^{2} P_{2} \cdot{ }^{3} P_{3}=4!\cdot 3!\cdot 2!\cdot 3! \\
& =24 \cdot 6 \cdot 2 \cdot 6 \\
& =1728 \text { ways }
\end{aligned}
$$

(c) only the mathematics books are kept together.

$$
\begin{aligned}
& { }^{4} P_{4} \cdot{ }^{6} P_{3}=4!\cdot 6! \\
& =24 \cdot 720 \\
& =17280 \text { ways }
\end{aligned}
$$

Example 6 In how many ways 5 people are to be seated on a bench if:
(a) there are no restrictions
(b) two people can sit next to each other
(c) two people cannot sit next to each other.

## Solution

(a) when there is no restriction, then

$$
\text { Number of ways }={ }^{5} P_{2}=5!=120
$$

(b) when two people can sit next to each other, then

$$
\begin{aligned}
& ={ }^{4} P_{4} \cdot{ }^{2} P_{2} \\
& =4!\cdot 2!=24 \cdot 2 \\
& =48 \text { ways }
\end{aligned}
$$

## C D E

51 ways
## Try yourself!

In how many ways 6 people are to seated on a table if 3 cannot sit next to each other?

# EXERCISE 7.2

1. Evaluate the following:
(i) ${ }^{10} P_{2}$
(ii) ${ }^{3} P_{2}$
(iii) ${ }^{7} P_{7}$
(iv) ${ }^{10} P_{2}$
2. Find the value of $n$ when:
(i) ${ }^{n} P_{3}=504$
(ii) ${ }^{15} P_{n}=15 \cdot 14 \cdot 13 \cdot 12 \cdot 11$
(iii) ${ }^{n} P_{3}:^{n-2} P_{2}=540: 1$
3. Prove from the first principle that:
(i) ${ }^{n} P_{r}=n \cdot{ }^{n-1} P_{r-1}$
(ii) ${ }^{n} P_{r}={ }^{n-1} P_{r}+r \cdot{ }^{n-1} P_{r-1}$
4. How many words can be formed from the letters of the following words using all letters when no letter is to be repeated:
(i) PYTHON
(ii) NETWORK
(iii) COMPUTER
5. How many signals can be given by 6 flags of different colours, using 2 flags at a time?
6. How many signals can be given by 5 flags of different colours, when any number of flags are used at a time.
7. How many 4 digit numbers can be formed, with distinct digits, with each digit odd?
8. How many numbers between 100 and 1000 can be formed by using the digits $0,1,2,3,4,5$ without repetition? How many of them are divisible by 5 ?
9. Find the numbers greater than 35000 that can be formed from the digits $1,2,3,4,5,6$, without repeating any digit.
10. Find the number of 5 -digit numbers that can be formed from the digits $1,2,4,6$, 8 (when no digit is repeated), but
(i) the digits 2 and 8 are next to each others;
(ii) the digits 2 and 8 are not next to each other.
11. How many 6-digit numbers can be formed, without repeating any digit from the digits $0,1,2,3,4,5$ ? In how many of them will 0 be at the tens place?
12. How many 5-digit multiples of 5 can be formed from the digits $2,3,5,7,9$, when no digit is repeated.
13. In how many ways can 8 different books including 2 on English be arranged on a shelf in such a way that the English books are never together?
14. Find the number of arrangements of 3 different books on English and 5 different books on Urdu for placing them on a shelf such that the books on the same subject are together.
15. In how many ways can 5 boys and 4 girls be seated on a bench so that the girls and the boys occupy alternate seats?

# 7.3 Permutation of Objects Not All Different

Suppose we have to find the permutations of the letters of the word BITTER using all the letters. The word BIT ${ }_{1} \mathrm{~T}_{2}$ ER consists of 6 different letters which can be permuted among themselves in 6 ! ways.
We can see that all the letters of the word BITTER are not different. It has 2Ts in it. We can see there are 2 ! ways of replacing two $\mathrm{T}_{8}$ :

BITT $T_{1}$ ER
BITT $T_{1}$ ER
The replacement of the two $\mathrm{T}_{8}$ by $\mathrm{T}_{1}$ and $\mathrm{T}_{2}$ in any other permutation will give rise to 2 permutations.
Hence, the number of permutations of the letters of the word BITTER taken all at a time.

$$
\frac{6!}{2!}=\frac{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{2.1}=360 \text { ways }
$$

## Remember!

If there are $n_{1}$ alike objects of one kind, $n_{2}$ alike objects of second kind and $n_{n}$ alike objects are of third kind, then the number of permutations of $n$ objects taken all at a time is given by:

$$
\frac{n!}{n_{1}!\cdot n_{2}!\cdot n_{3}!}=\binom{n}{n_{1}, n_{2}, n_{3}}
$$

Example 7 In how many ways can the letters of the word MISSISSIPPI be arranged when all the letters are to be used?
Solution Total number of letters in the word $=11$

## MISSISSIPPI

I is repeated 4 times $=4$ I ways
$S$ is repeated 4 times $=4$ I ways
$P$ is repeated 2 times $=2$ I ways
$M$ comes once only $=11$ ways
Required number of permutations $=\frac{11!}{4!\cdot 4!\cdot 2!\cdot 1!}=34650$ ways

## Circular Permutations

The permutations in which the object are arranged in a circular order are known as circular permutations.

## Note:

The following circular arrangements are reflection of each other and considered same when anticlockwise and clockwise arrangements are considered identical.
Circular permutations can occur in two cases:
Case-I: When clockwise and anticlockwise arrangements are considered different In a linear arrangement, changing the order of objects results in a new arrangement. However, in a circular arrangement, rotating the entire circle does not produce a new, distinct arrangement.

For example, suppose three people $\mathrm{A}, \mathrm{B}$ and C are sitting around a round table. The following three linear arrangements
$\mathrm{A}-\mathrm{B}-\mathrm{C}, \mathrm{B}-\mathrm{C}-\mathrm{A}$ and $\mathrm{C}-\mathrm{A}-\mathrm{B}$ are considered the same in circular permutations because each one is simply a rotation of the other.
We conclude that:
3 linear permutations gives 1 circular permutation.
3 ! linear permutations gives $\frac{1}{3} \cdot 3!=\frac{3!}{3}=2$ ! permutations.
Generalizing the above idea if $n$ objects are arranged in a circle, the number of distinct circular permutations is $\frac{n!}{n}=(n-1)!$.

Case-II: When clockwise and anticlockwise arrangements are considered identical
In many real-life situations, a circular permutation and its mirror image are not considered different.
For example, if three beads red, blue, and black are arranged in a ring, then an arrangement and its reflection (as shown in the figure) are considered the same.
In such cases, we divide the total number of circular permutations by 2 to eliminate symmetrical duplicates.
Thus, in this case the number of distinct circular permutations is:

$$
\frac{(n-1)!}{2}
$$

Example 8 In how many ways can 4 persons be seated at a round table, while:
(i) clockwise and anticlockwise orders are different
(ii) clockwise and anticlockwise orders are identical.

Solution Let $A, B, C$ and $D$ be the 4 persons.
(i) If clockwise and anticlockwise orders are different

# According to Case-I

The possible number of ways are:

$$
\begin{aligned}
& =(n-1)!\text { ways } \\
& =(4-1)!=3! \\
& =3 \cdot 2 \cdot 1=6 \text { ways. }
\end{aligned}
$$

(ii) If clockwise and anticlockwise orders are identical

According to Case-II
The possible number of ways are $=\frac{(n-1)!}{2}$ ways

$$
\begin{aligned}
& =\frac{(4-1)!}{2}=\frac{31}{2} \\
& =\frac{3 \cdot 2}{2}=3 \text { ways }
\end{aligned}
$$

# EXERCISE 7.3

1. How many arrangements of the letters of the following words, taken all together can be made?
(i) PAKISTAN
(ii) CURRICULUM
(iii) PROBABILITY
2. How many permutations of the letters of the word "BANANA" can be made, if B must be the first letter in each arrangement?
3. How many arrangements of the letters of the word TRIGONOMETRY can be made, if each arrangement begins with T and ends with Y ?
4. Abdullah has a collection of 9 marbles consisting of 4 identical red marbles, 3 identical blue marbles and 2 identical green marbles. If he wants to arrange all of them is a straight row, how many distinct arrangements are possible?
5. In how many different ways can the following persons sit around a round table?
(a) 8 persons
(b) 7 persons
(c) 6 persons
6. In how many ways can 5 couples sit around a round table if no two women are sitting together?
7. How many 6 -digit numbers can be formed from the digits $7,7,8,8,9,9$ ?
8. 15 members of a club form 4 committees of $3,5,4$ and 3 members so that no member is a member of more than one committee. Find the number of committees.
9. The D.C.Os of 11 districts meet to discuss the law-and-order situation in their districts. In how many ways can they be seated at a round table, when two particular D.C.Os insist on sitting together?
10. The Governor of the Punjab calls a meeting of 14 officers. In how many ways can they be seated at a round table?
11. Fatima invites 14 people for a dinner. There are 9 males and 5 females who are seated at two different tables. Guests of one sex sit at one round table and the guests of the other sex sit at the second table. Find the number of ways in which all guests can be seated.

12. Find the number of ways in which 5 men and 5 women can be seated at a round table in such a way that no two persons of the same sex sit together.
13. In how many ways can 8 keys be arranged in a circular key ring?
14. How many necklaces can be made from 10 beads of different colours?

# 7.4 Combinations

Suppose, a teacher uses the names of few students to make a team for a writing competition. Such as Ahmad, Sana, Hamza and Danish. As a combination of team members, (Ahmad, Sana, Hamza and Danish) is equivalent to (Hamza, Ahmad, Danish and Sana). Because same students are in the combination. Consequently, you have the same team because the order of the name of the students does not matter.
So, we are interested in the membership of the

| Ahmad | Sana | Hamza | Danish |
| :-- | :-- | :-- | :-- |
| Hamza | Ahmad | Danish | Sana |

team and not in the ways the students are listed (arranged).

## Definition

A combination of $r$ objects taken out of $n$ objects is a subset of $r$ objects of a set of $n$ objects.
The number of combinations of $n$ different objects taken $r$ at a time is denoted by ${ }^{n} C_{r}$ or $C(n, r)$ or $\binom{n}{r}$ and is given by ${ }^{n} C_{r}=\frac{n!}{r!(n-r)!}$.
Theorem. Prove that ${ }^{n} C_{r}=\frac{n!}{r!(n-r)!}$.
Proof: Elements of a subset of $r$ objects of a set of $n$ objects can be arranged among themselves in $r$ ! ways. So, each combination will give rise to $r$ ! permutation. Thus, there will be ${ }^{n} C_{r} \times r$ ! permutations of $n$ different objects taken $r$ at a time that is:

$$
\begin{aligned}
& { }^{n} C_{r} \times r!={ }^{n} P_{r} \\
& \Rightarrow \quad{ }^{n} C_{r} \times r!=\frac{n!}{(n-r)!} \quad \therefore \quad{ }^{n} C_{r}=\frac{n!}{r!(n-r)!}
\end{aligned}
$$

Which completes the proof.

## Corollary:

(i) If $r=n$, then ${ }^{n} C_{n}=\frac{n!}{n!(n-n)!}=\frac{n!}{n!0!}=1$
(ii) If $r=0$, then ${ }^{n} C_{0}=\frac{n!}{0!(n-0)!}=\frac{n!}{0!n!}=1$

## Remember!

The formulae ${ }^{n} P_{r}$ and ${ }^{n} C_{r}$ are also known as counting formulae. Because, they are used to count the possible number of ways without listing them all.

# 7.4.1 Applications of Combination in Real Life

Example 9 Zain has 8 different fruits. He wants to select 5 fruits out of 8 fruits to make a fruit chat. How many combinations of fruits he can select?
Solution To solve this problem, we have to find the number of combinations of 5 fruits out of 8 fruits. In this situation, $n=8$ and $r=5$.

$$
\begin{aligned}
{ }^{n} C_{r} & =\frac{n!}{r!(n-r)!} \\
\text { After putting values } \\
\begin{aligned}
{ }^{8} C_{3} & =\frac{8!}{5!(8-5)!}=\frac{8!}{5!\cdot 3!} \\
& =\frac{8 \times 7 \times 6 \times 5!}{5!\cdot 3!}=\frac{8 \times 7 \times 6}{3 \cdot 2 \cdot 1} \\
& =8 \times 7=56 \text { ways }
\end{aligned}
$$

Zain has 56 different ways to select 5 different fruits to make a fruit chat.
Example10 In a school, a class consists of 12 girls and 8 boys. The teacher wants to select 5 students for an activity. In how many ways can the students be selected including? (i) 2 girls
(ii) 5 boys
(iii) 2 boys

| Solution | Number of girls $=12$ | Challenge! |
| :--: | :--: | :--: |
|  | Number of boys $=8$ | A restaurant offers 6 flavours of pizza. How many ways are there to select 2 flavours of pizza? |

(i) Now let's find the total number of ways to select students when exactly 2 are girls.
${ }^{12} C_{2}{ }^{8} C_{3}=\frac{12!}{2!10!} \cdot \frac{8!}{3!5!}=\frac{12 \cdot 11 \cdot 10!}{2 \cdot 10!} \cdot \frac{8 \cdot 7 \cdot 6 \cdot 5!}{3 \cdot 2 \cdot 1 \cdot 5!}=3696$
(ii) Let's find total number of ways to select students when exactly 5 students are boys.

$$
{ }^{8} C_{3}=\frac{8!}{5!(8-5)!}=\frac{8!}{5!3!}=\frac{8 \cdot 7 \cdot 6 \cdot 5!}{5!3 \cdot 2 \cdot 1}=56
$$

(iii) Let's find total number of ways to select students when exactly 2 students are boys.

$$
{ }^{8} C_{2}{ }^{12} C_{3}=\frac{8!}{2!6!} \cdot \frac{12!}{3!9!}=\frac{8 \cdot 7 \cdot 6!}{2 \cdot 6!} \cdot \frac{12 \cdot 11 \cdot 10 \cdot 9!}{3 \cdot 2 \cdot 1 \cdot 9!}=36960
$$