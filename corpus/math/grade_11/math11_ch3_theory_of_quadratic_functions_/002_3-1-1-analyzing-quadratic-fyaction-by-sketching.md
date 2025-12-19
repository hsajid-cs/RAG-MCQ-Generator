### 3.1.1 Analyzing Quadratic Fyaction by Sketching

As we know shape of the graph of a quadratic function $f(x)=a x^{2}+b x+c$ is a parabola. The parabola opens upward or downward, depending on the sign of the leading coefficient $a$, as shown in the given figure.
The tip of the parabola, labeled as $V$ in the diagrams above, is known as the vertex having coordinates $(h, k)$. The vertical line passing through the vertex serves as the axis of symmetry for the parabola. The vertex represents a turning point, where the graph changes direction.

- If $a>0$, then the vertex is a minimum point.
- If $a<0$, then the vertex is a maximum point.

For sketching the quadratic function, we need to find the $x$-intercept, $y$-intercept and the vertex. For analyzing the sketch of quadratic function, we find whether the vertex is a minimum or a maximum point and indicate the intervals where the function is increasing or decreasing.

Example 1 Sketch and analyze $y=-x^{2}-2 x+3$.
Solution $y=-x^{2}-2 x+3$
The $y$-intercept is $y=-(0)^{2}-2(0)+3=3$
The $x$-intercepts are found by solving the equation:

$$
\begin{aligned}
-x^{2}-2 x+3 & =0 \text { or } x^{2}+2 x-3=0 \\
x^{2}+3 x-x-3 & =0 \\
x(x+3)-1(x+3) & =0 \\
(x+3)(x-1) & =0 \\
x+3=0, x-1 & =0 \\
x & =-3, x=1
\end{aligned}
$$

Now, we find the vertex

$$
h=\frac{-b}{2 a}=-\frac{(-2)}{2(-1)}=-1
$$

$k=-(-1)^{2}-2(-1)+3=-1+2+3=4$
So, the vertex $(-1,4)$ is a maximum point. The function $y$ is increasing on $(-\infty,-1)$ and decreasing on $(-1, \infty)$.
# 3.1.2 Finding Maximum and Minimum Values of Quadratic

## Functions by Completing Square

Completing the square is a technique used to rewrite a quadratic function $f(x)=a x^{2}+b x+c$ in the following vertex form:

$$
f(x)=a(x-h)^{2}+k
$$

where vertex $=(h, k), h=-\frac{b}{2 a}$ and $k=c-\frac{b^{2}}{4 a}$

- If $a>0$, the minimum value of $f(x)$ at $x=h$ is $k$.
- If $a<0$, the maximum value of $f(x)$ at $x=h$ is $k$.

Example 2 Find the maximum or minimum value of $f(x)=-2 x^{2}+4 x+3$ by completing square.
Solution

$$
\begin{aligned}
& f(x)=-2\left(x^{2}-2 x\right)+3 \\
& f(x)=-2\left(x^{2}-2 x+1-1\right)+3 \\
& f(x)=-2\left[(x-1)^{2}-1\right]+3 \\
& f(x)=-2(x-1)^{2}+2+3 \\
& f(x)=-2(x-1)^{2}+5
\end{aligned}
$$

Here $a=-2<0$
Therefore, the maximum value is 5 , which occurs when $x=1$.
Example 3 Find the maximum or minimum value of $f(x)=x^{2}-2 x-3$.
Solution Given that $f(x)=x^{2}-2 x-3$
Here $a=1, b=-2, c=-3$

$$
h=-\frac{b}{2 a}=-\frac{(-2)}{2(1)}=1
$$

and

$$
k=c-\frac{b^{2}}{4 a}=-3-\frac{(-2)^{2}}{4(1)}=-4
$$

Here $a=1>0$
Therefore, the minimum value of $f(x)$ at $x=1$ is -4 .

# 3.2 Inverse of Quadratic Function

Quadratic functions are typically not one-to-one over their entire domain. To find an inverse for a quadratic function, we must restrict its domain to a portion where it is one-to-one. Commonly, we restrict the domain to either $x \geq h$ (where $h$ is the $x$-coordinate of the vertex) or $x \leq h$.
Example 4 Find the inverse of $f(x)=x^{2}+4 x+3, x \geq-2$. Also find its domain and range.
Solution $f(x)=x^{2}+4 x+3, \quad x \geq-2$
Let

$$
\begin{aligned}
y & =x^{2}+4 x+3 \\
x & =y^{2}+4 y+3 \\
y^{2}+4 y+3-x=0 & \text { (Interchange } x \text { and } y \text { ) } \\
y & =\frac{-4 \pm \sqrt{(4)^{2}-4(1)(3-x)}}{2(1)} \\
y & =\frac{-4 \pm \sqrt{16-12+4 x}}{2} \\
y & =\frac{-4 \pm \sqrt{4+4 x}}{2} \\
y & =\frac{-4 \pm 2 \sqrt{1+x}}{2} \\
f^{-1}(x) & =-2 \pm \sqrt{1+x}
\end{aligned}
$$

(Replace $y$ with $f^{-1}(x)$ )
The above inverse function has both a positive and a negative component. To determine which is the inverse, we find domain and range of the given function.

$$
\text { Domain } f=[-2, \infty)
$$

To find range, we proceed as:

$$
\begin{aligned}
& f(x)=x^{2}+4 x+3 \\
& \Rightarrow \quad f(x)=(x+2)^{2}-1
\end{aligned}
$$

Therefore, minimum value of $f(x)$ is -1 and hence

$$
\text { Range } f=[-1, \infty)
$$

Domain $f^{-1}=[-1, \infty)$, Range $f^{-1}=[-2, \infty)$
Now, we substitute any value of $x$ that falls within the domain of $f^{-1}(x)$. We choose the value $x=0$.

$$
\begin{aligned}
& f^{-1}(0)=-2+\sqrt{1+0}=-1 \\
& f^{-1}(0)=-2-\sqrt{1+0}=-3
\end{aligned}
$$

We notice only -1 lies in the range of $f$. Therefore, we discard negative component.
Hence $f^{-1}(x)=-2+\sqrt{1+x}$

# 3.3 Absolute Value

The absolute value of $x$, is defined as

$$
|x|=\left\{\begin{array}{ll}
x & , x \geq 0 \\
-x, & x<0
\end{array}\right.
$$