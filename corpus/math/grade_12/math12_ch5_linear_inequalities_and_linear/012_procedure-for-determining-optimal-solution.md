#### Procedure for determining optimal solution:

(i) Graph the solution set of linear inequality constraints to determine feasible region.

(ii) Find the corner points of the feasible region.

(iii) Evaluate the objective function at each corner point to find the optimal solution.

**Example 1.** Find the maximum and minimum values of the function defined as:

$$f(x, y) = 2x + 3y \qquad \text{subject to the constraints;}$$

$$x - y \leq 2 \qquad x + y \leq 4 \qquad 2x - y \leq 6, \quad x \geq 0$$

**Solution.** The graphs of $$x - y \leq 2$$ is the closed half plane on the origin side of $$x - y = 2$$ and the graph of $$x + y \leq 4$$ is the closed half-plane not on the origin side of $$x + y = 4$$. The graph of the system

$$x - y \leq 2, x + y \geq 4$$

*version: 1.1*

including the non-negative constraints *x* ≥ 0 is partially displayed as shaded region in the figure 5.61. The graph of 2*x* − *y* ≤ 6 consists of the graph of the line 2*x* − *y* = 6 and the half plane on the origin side of the line 2*x* − *y*=6. A portion of the solution region of the given system of inequalities is shaded in the figure 5.62.

We see that feasible region is unbounded upwards and its corner points are *A*(0, 4), *B*(3, 1) and *C*(4, 2). Note that the point at which the lines *x* + *y* = 4 and 2*x* − *y* = 6 intersect is not a corner point of the feasible region.

It is obvious that the expression 2*x* + 3*y* does not possess a maximum value in the feasible region because its value can be made larger than any number by increasing *x* and *y*. We calculate the values of *f* at the corner points to find its minimum value:

$$
\begin{array}{rcl}
f(0, 4) & = & 2(0) + 3 \times 4 & = & 12 \\
f(3, 1) & = & 2 \times 3 + 3 \times 1 & = & 6 + 3 = 9 \\
f(4, 2) & = & 2 \times 4 + 3 \times 2 & = & 8 + 6 = 14
\end{array}
$$

Thus the minimum value of 2*x* + 3*y* is 9 at the corner point (3, 1).

**Notes:** If *f*(*x*, *y*) = 2*x* + 3*y*, then *f*(0, 4) = 2*x* 0 + 2*x* 4 = 8, *f*(3, 1) = 2*x* 3 + 2*x* 4 = 6 + 2 = 9 and (4, 2) = 2*x* 4 + 2*x* 2 = 8 + 4 = 12. The minimum value of 2*x* + 3*y* is the same, at two corner points (0, 4) and (3, 1).

We observe that the minimum value of 2*x* + 2*y* at each point of the line segment *AB* is 8 as:

$$
\begin{array}{rcl}
f(x, y) & = & 2x + 2(4 - x) \qquad \qquad \qquad \qquad \qquad \qquad ( \cdot \quad x + y = 4 \Rightarrow y = 4 - x) \\
& = & 2x + 8 - 2x = 8
\end{array}
$$

**Example 2.** Find the minimum and maximum values of *f* and *φ* defined as:

$$
f(x, y) = 4x + 5y, \qquad \phi(x, y) = 4x + 6y
$$

under the constraints

$$
2x - 3y \leq 6 \qquad 2x + y \geq 2 \qquad 2x + 3y \leq 12 \qquad x \geq 0, \quad y \geq 0
$$

**Solution.** The graphs of 2*x* − 3*y* ≤ 6, 2*x* + *y* ≥ 2, are displayed in the example 3 of Art. 5.5. Joining the points (6, 0) and (0, 4), we obtain the graph of the line 2*x* + 3*y* = 12. As 2(0) + 3(0) = 0 < 12, so the graph of 2*x* + 3*y* < 12 is the half plane below the line 2*x* + 3*y* = 12. Thus the graph of 2*x* + 3*y* ≤ 12 consists of the graph of the line 2*x* + 3*y* = 12 and the half plane below the line 2*x* + 3*y* = 12. The solution region of 2*x* − 3*y* ≤ 6, 2*x* + *y* ≥ 2 and 2*x* + 3*y* ≤ 12 is the triangular region *PQR* shown in figure 5.63. The non-negative constraints *x* ≥ 0, *y* ≥ 0 indicated the first quadrant. Thus the feasible region satisfying all the constraints is shaded in the figure 5.63 and its corner points are (1, 0), (0, 2), (0, 4), (9, 2, 1) and (3, 0).

We find values of *f* at the corner points.

|  Corner point | *f*(*x*, *y*) = 4*x* + 5*y*  |
| --- | --- |
|  (1, 0) | *f*(1, 0) = 4 *x* 1 + 5.0 = 4  |
|  (0, 2) | *f*(0, 2) = 4 *x* 0 + 5.2 = 10  |
|  (0, 4) | *f*(0, 4) = 4 *x* 0 + 5.4 = 20  |
|  (9/2, 1) | *f*(9/2, 1) = 4 *x* 9/2 + 5.1 = 23  |
|  (3, 0) | *f*(3, 0) = 4 *x* 3 + 5.0 *x* 0 = 12  |

From the above table, it follows that the minimum value of *f* is 4 at the corner point (1, 0) and maximum value of *f* is 23 at the corner point (9, 2, 1). The values of *φ* at the corner points are given below in tabular form.

|  Corner point | *φ*(*x*, *y*) = 4*x* + 5*y*  |
| --- | --- |
|  (1, 0) | *φ*(1, 0) = 4.1 + 6.0 = 4  |
|  (0, 2) | *φ*(0, 2) = 4.0 + 6.2 = 12  |
|  (0, 4) | *φ*(0, 4) = 4.0 + 6.4 = 24  |
|  (9/2, 1) | *φ*(9/2, 1) = 4.9/2 + 6.1 = 24  |
|  (3, 0) | *φ*(3, 0) = 4 *x* 3 + 6.0 = 12  |

The minimum value of *φ* is 4 at the point (1, 0) and maximum value of *φ* is 24 at the corner points (0, 4) and (9, 2, 1). As observed in the above example, it follows that the function *φ* has maximum value at all the points of the line segment between the points

(0, 4) and $\left(\frac{9}{3}, 1\right)$.

Note 1. Some times it may happen that each point of constraint line gives the optimal value of the objective function.

Note 2. For different value of $k$, the equation $4 x+5 y=k$ represents lines parallel to the line $4 x+5 y=0$. For a certain admissible value of $k$, the intersection of $4 x+5 y=k$ with the feasible region gives feasible solutions for which the profit is $k$.