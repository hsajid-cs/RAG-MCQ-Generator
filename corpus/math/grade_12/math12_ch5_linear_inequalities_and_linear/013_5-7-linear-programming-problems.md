### 5.7 LINEAR PROGRAMMING PROBLEMS

Convert a linear programming problem to a mathematical form by using variables, then follow the procedure given in Art 5.6.

Example 1: A farmer possesses 100 canals of land and wants to grow corn and wheat. Cultivation of corn requires 3 hours per canal while cultivation of wheat requires 2 hours per canal. Working hours cannot exceed 240. If he gets a profit of Rs. 20 per canal for corn and Rs. 15/- per canal for wheat, how many canals of each he should cultivate to maximize his profit?

Solution: Suppose that he cultivates $x$ canals of corn and $y$ canals of wheat. Then constraints can be written as:

$$ \begin{aligned} & x+y \leq 100 \ & 3 x+2 y \leq 240 \end{aligned} $$

Non-negative constraints are $x \geq 0, y \geq 0$. Let $P(x, y) x^{*}$ be the profit function, then

$$ P(x, y)=20 x+15 y $$

Now the problem is to maximize the profit function $P$ under the given constraints. Graphing the inequalities, we obtain the feasible region which is shaded in the figure 5.71. Solving the equations $x+y=100$ and $3 x+2 y=240$ gives $x=240-2(x+y)=240-200=40$ and $y=100-40=60$, that is; their point of intersection is $(40,60)$. The corner points of the feasible region are $(0,0),(0,100),(40,60)$ and $(80,0)$. Now we find the values of $P$ at the corner points.

|  Corner point | $P(x, y)=20 x+15 y$  |
| --- | --- |
|  $(0,0)$ | $P(0,0)=20 \times 0+15 \times 0=0$  |
|  $(0,100)$ | $P(0,100)=20 \times 0+15 \times 100=1500$  |
|  $(40,60)$ | $P(40,60)=20 \times 40+15 \times 60=1700$  |
|  $(80,0)$ | $P(80,0)=20 \times 80+15 \times 0=1600$  |

From the above table, it follows that the maximum profit is Rs. 1700 at the corner point $(40,60)$. Thus the farmer will get the maximum profit if he cultivates 40 canals of corn and 60 canals of wheat.

Exam ple 2. A factory produces bicycles and motorcycles by using two machines $A$ and B. Machine $A$ has at most 120 hours available and machine $B$ has a maximum of 144 hours available. Manufacturing a bicycle requires 5 hours in machine $A$ and 4 hours in machine $B$ while manufacturing of a motorcycle requires 4 hours in machine $A$ and 8 hours in machine $B$. If he gets profit of Rs. 40 per bicycle and profit of Rs. 50 per motorcycle, how many bicycles and motorcycles should be manufactured to get maximum profit?

Solution: Let the number of bicycles to be manufactured be $x$ and the number of motor cycles to be manufactured be $y$.

Then the time required to use machine $A$ for $x$ bicycles and $y$ motorcycles is $5 x+4 y$ (hours) and the time required to use machine $B$ for $x$ bicycles and $y$ motorcycles in $4 x+8 y$ (hours). Thus the problem constraints are $5 x+4 y \leq 120$

$$ \begin{array}{ll} \text { And } & 4 x+8 y \leq 144 \ \Rightarrow & 2 x+4 y \leq 72 \end{array} $$

Since the numbers of articles to be produced cannot be negative, so $x \geq 0, y \geq 0$. Let $P(x, y)$ be the profit function, then $P(x, y)=40 x+50 y$. Now the problem is to maximize $P$ subject to the constraints:

$$
\begin{aligned}
& 5 x+4 y \leq 120 \\
& 2 x+4 y \leq 72 \quad ; \quad x \geq 0, y \geq 0
\end{aligned}
$$

Solving $5 x+4 y=120$ and $2 x+4 y=72$, gives $3 x=48 \Rightarrow x=16$ and $4 y=72-2 x=72-32=40 \Rightarrow y=10$.

Thus their point of intersection is $(16,10)$. Graphing the linear inequality constraints, the feasible region obtained is depicted in the figure 5.72 by shading. The corner points of the feasible region are $(0,0),(0,18),(16,10)$ and $(24,0)$. Now we find the values of $P$ at the corner points.

|  Corner point | $P(x, y)=40 x+50 y$  |
| --- | --- |
|  $(0,0)$ | $P(0,0)=40 \times 0+50 \times 0=0$  |
|  $(0,18)$ | $P(0,18)=40 \times 0+50 \times 18=900$  |
|  $(16,10)$ | $P(16,10)=40 \times 16+50 \times 10=1140$  |
|  $(24,0)$ | $P(24,0)=40 \times 24+50 \times 0=960$  |

From the above table, it follows, that the maximum profit is Rs. 1140 at the corner point $(16,10)$. Manufacturer gets the maximum profit if he manufactures 16 bicycles and 10 motorcycles.

## EXERCISE 5.3

1. Maximize $f(x, y)=2 x+5 y$ subject to the constraints $2 y-x \leq 8 ; \quad x-y \leq 4 ; \quad x \quad 0 \geq 0 ; \quad y \geq 0$
2. Maximize $f(x, y)=x+3 y$ subject to the constraints $2 x+5 y \leq 30 ; \quad 5 x+4 y \leq 20 ; \quad x \geq 0 ; \quad y \geq 0$
3. Maximize $z=2 x+3 y$; subject to the constraints: $3 x+4 y \leq 12 ; \quad 2 x+y \leq 4 ; \quad 4 x-y \leq 4 ; x \geq 0 ; y \geq 0$
4. Minimize $z=2 x+y$ : subject to the constraints: $x+y \geq 3 ; \quad 7 x+5 y \leq 35 ; \quad x \geq 0 ; \quad y \geq 0$
5. Maximize the function defined as; $f(x, y)=2 x+3 y$ subject to the constraints: $2 x+y \leq 8 ; \quad x+2 y \leq 14 ; \quad x \geq 0 ; \quad y \geq 0$
6. Minimize $z=3 x+y$; subject to the constraints: $3 x+5 y \geq 15 ; \quad x+6 y \geq 9 ; \quad x \geq 0 ; \quad y \geq 0$
7. Each unit of food $X$ costs Rs. 25 and contains 2 units of protein and 4 units of iron while each unit of food $Y$ costs Rs. 30 and contains 3 units of protein and 2 unit of iron. Each animal must receive at least 12 units of protein and 16 units of iron each day. How many units of each food should be fed to each animal at the smallest possible cost?
8. A dealer wishes to purchase a number of fans and sewing machines. He has only Rs. 5760 to invest and has space atmost for 20 items. A fan costs him Rs. 360 and a sewing machine costs Rs. 240. His expectation is that the can sell a fan at a profit of Rs. 22 and a sewing machine at a profit of Rs. 18. Assuming that he can sell all the items that he can buy, how should he invest his money in order to maximize his profit?
9. A machine can produce product $A$ by using 2 units of chemical and 1 unit of a compound or can produce product $B$ by using 1 unit of chemical and 2 units of the compound. Only 800 units of chemical and 1000 units of the compound are available. The profits per unit of $A$ and $B$ are Rs. 30 and Rs. 20 respectively, maximize the profit function.