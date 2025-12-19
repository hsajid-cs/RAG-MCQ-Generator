### 2.1.1 AVERAGE RATE OF CHANGE

Suppose a particle (or an object) is moving in a straight line and its positions (from some fixed point) after times $t$ and $t_{1}$ are given by $s(t)$ and $s\left(t_{1}\right)$, then the distance traveled in the time interval $t_{1}-t$ where $t_{1}>t$ is $s\left(t_{1}\right)-s(t)$ and the difference quotient $\frac{s\left(t_{1}\right)-s(t)}{t_{1}-t}$ (i) represents the average rate of change of distance over the time interval $t_{1}-t$. If $t_{1}-t$ is not small, then the average rate of change does not represent an accurate rate of change near $t$. We can elaborate this idea by a moving particle in a straight line whose position in metres after $t$ seconds is given by

$$ s(t)=t^{2}+t $$

We construct a table for different values of $t$ as under:

|  Interval | Average rate of change (i.e. average speed)  |
| --- | --- |
|  $t=3$ secs to $t=5$ secs | $\frac{s(5)-s(3)}{5-3}=\frac{(25+5)-(9+3)}{2}=\frac{30-12}{2}=9$  |
|  $t=3$ secs to $t=4$ secs | $\frac{s(4)-s(3)}{4-3}=\frac{(16+4)-12}{1}=\frac{20-12}{1}=8$  |
|  $t=3$ secs to $t=3.5$ secs | $\frac{s(3.5)-s(3)}{3.5-3}=\frac{\left(\frac{49}{4}+\frac{7}{2}\right)-12}{0.5}=\frac{\frac{15}{4}}{0.5}=7.5$  |

We see that none of average rates of change approximates to the actual speed of the particle after 3 seconds.

Now we construct a table by taking small intervals.

|  Interval | Average rate of change  |
| --- | --- |
|  $t=3$ secs to $t=3.1 \mathrm{secs}$ | $\frac{((3.1)^{2}+3.1)-12}{3.1-3}=\frac{12.71-12}{0.1}=\frac{0.71}{0.1}=7.1$  |
|  $t=3$ secs to $t=3.01 \mathrm{secs}$ | $\frac{((3.01)^{2}+3.01)-12}{3.01-3}=\frac{12.0701-12}{0.01}=\frac{0.0701}{0.01}=7.01$  |
|  $t=3$ secs to $t=3.001 \mathrm{secs}$ | $\frac{((3.001)^{2}+3.001)-12}{3.001-3}=\frac{12.007001-12}{0.001}=\frac{0.007001}{0.001}=7.001$  |

The above table shows that the average rate of change after 3 seconds approximates to 7 metre/sec. as the length of the interval becomes very very small. In other words, we can say that the speed of the particle is 7 metre/sec. after 3 seconds.

If $t_{i}=t+\delta t$ then the difference quoteint (i) becomes

$$
\frac{s(t+\delta t)-s(t)}{\delta t}
$$

which represents the average rate of change of distance over the interval $\delta t$ and

$$
\lim _{t \rightarrow \infty} \frac{s(t+\delta t)-s(t)}{\delta t}, \text { provided this limit exists, is called the instantaneous rate of change }
$$

of distance 's' at time $t$.