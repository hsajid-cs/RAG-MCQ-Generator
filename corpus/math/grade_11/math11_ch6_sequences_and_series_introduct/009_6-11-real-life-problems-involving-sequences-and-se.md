### 6.11 Real Life Problems involving Sequences and Series

## Example 27 Vehicle Arrival Sequence

Vehicles arrive at a toll booth at a rate of 4 cars every 5 minutes. Represent the number of cars arriving over time as a sequence and predict the total number of cars after an hour.
Solution The sequence of car arrivals is:

$$
4,8,12,16, \ldots
$$

This is an $A: P$, with
$a_{1}=4, d=4, n=\frac{60}{5}=12, a_{12}=?$
Using the formula for arithmetic sequence

$$
\begin{aligned}
a_{n} & =a_{1}+(n-1) d \\
a_{12} & =4+(12-1)(4) \\
& =4+11(4) \\
& =4+44=48
\end{aligned}
$$

Thus, after one hour there will be 48 cars.

Simple Interest on Loan (Arithmetic Sequence with Particular Term)
Example 28 To buy furniture for a new apartment Tayyab borrowed Rs. 50,000 at $8 \%$ simple interest for 11 years. How much interest will he pay?
Solution Since $8 \%$ is the yearly interest rate, we have

$$
\begin{aligned}
& \text { Interest after one year }=\text { Rs. } 50,000 \times \frac{8}{100} \times 1=\text { Rs. } 4000 \\
& \text { Interest after two years }=\text { Rs. } 50,000 \times \frac{8}{100} \times 2=\text { Rs. } 8000
\end{aligned}
$$

Therefore, we have the A.P.

$$
4000,8000,12000, \ldots
$$

Here, $a_{1}=4000, a_{2}=8000, d=a_{2}-a_{1}=4000, n=11$
Using the formula

$$
\begin{aligned}
a_{n} & =a_{1}+(n-1) d \\
a_{11} & =4000+(11-1)(4000) \\
& =4000+10(4000) \\
& =4000+40000 \\
& =\text { Rs. } 44000
\end{aligned}
$$

Thus, Tayyab will pay a total interest of Rs. 44000 on borrowed amount of Rs 50,000 after 11 years.
Compound Interest on Loan (Geometric Sequence with Particular Term)
Example 29 Amna invests Rs. 200000 at $5 \%$ interest compounded annually. What total amount will she get after 10 years?
Solution Let the principal amount be $P$. Then,
The interest for the first year $=P \times \frac{5}{100}=P(0.05)$
The total amount after first year $=P+P(0.05)=P(1+0.05)$
The interest for the second year $=P(1+0.05) \times 0.05$
The total amount after second year $=P(1+0.05)+P(1+0.05) \times 0.05$

$$
\begin{aligned}
& =P(1+0.05)(1+0.05) \\
& =P(1+0.05)^{2}
\end{aligned}
$$

Similarly, the total amount after third year $=P(1+0.05)^{3}$
Thus, we have sequence of amounts

$$
P(1.05), P(1.05)^{2}, P(1.05)^{3}, \ldots
$$

which is clearly a G.P., with

$$
a_{1}=P(1.05), r=1.05, n=10, a_{10}=?
$$

Using the geometric sequence formula

$$
\begin{aligned}
a_{n} & =a_{1} r^{n-1} \\
a_{10} & =a_{1} r^{10-1} \\
& =P(1.05) \times(1.05)^{9} \\
& =(200000)(1.05)^{10} \quad P=200000 \\
& =(200000)(1.62889) \\
& =325778.92
\end{aligned}
$$

Thus, the total amount Amna will get after 10 years will be Rs. 325778.92
Grid Column Distribution (Arithmetic Series Sum of Terms)
Example 30 A web designer is using a 12 -column grid system where each column increases in width by 10px from the previous one. The first column width is 50px wide. Find the total width occupied by all 12 columns.
Solution This follows an arithmetic series with:
First term $=a_{1}=50$, Common difference $=d=10$
Number of terms $=n=12$
Using the formula for the sum of an arithmetic series:

$$
\begin{aligned}
S_{n} & =\frac{n}{2}\left[2 a_{1}+(n-1) d\right] \\
S_{12} & =\frac{12}{2}[2(50)+(12-1)(10)] \\
& =6[100+110]=6[210] \\
& =1260 p x
\end{aligned}
$$

Thus, the total width of all 12 columns is 1260 px .
Example 31 Motor Vehicle Leasing Using Arithmetic Sequence
A company leases a motor vehicle with the following terms:

- The first monthly payment is Rs. 15,000
- Each subsequent payment increases by Rs. 500 due to inflation adjustments.
- The lease term is 24 months.

Find:
(i) What is the payment in the $24^{\text {th }}$ month?
(ii) What is the total amount paid over 24 months?
(iii) If the company can only afford to pay a total of Rs. 400,000 , can they complete the 24 -months lease?
(iv) Find maximum months $n$ such that total, payment $S_{n} \leq 400,000$.

# Solution Given:

$$
\begin{aligned}
\text { First term }=a_{1} & =15000 \\
\text { Common difference } & =d=500 \\
\text { Number of terms } & =n=24
\end{aligned}
$$

(i) Payment in $24^{\text {th }}$ month:

Using the formula

$$
\begin{aligned}
a_{n} & =a_{1}+(n-1) d \\
a_{24} & =15000+(24-1)(500) \\
& =15000+23 \times 500 \\
& =15000+11500=\text { Rs. } 26500
\end{aligned}
$$

(ii) Total payment over 24 months using the formula

$$
\begin{aligned}
S_{n} & =\frac{n}{2}\left(a_{1}+a_{n}\right) \\
& =\frac{24}{2}(15000+26500)=12(41500)=\text { Rs. } 498000
\end{aligned}
$$

(iii) Can the company afford the lease? No, total payments (Rs. 498000) exceed the budget of Rs. 400,000 by Rs. 98,000 .
(iv) Using: $S_{n}=\frac{n}{2}\left[2 a_{1}+(n-1) d\right] \leq 400,000$

Substituting the values:

$$
\begin{aligned}
& \frac{n}{2}[2(15000)+(n-1)(500)] \leq 400,000 \\
& n[15000+250 n-250] \leq 400,000 \\
& n(250 n+14750) \leq 400,000 \\
& 250 n^{2}+14750 n-400000 \leq 0 \\
& n^{2}+59 n-1600 \leq 0
\end{aligned}
$$

Associated equation is $n^{2}+59 n-1600=0$

$$
\begin{aligned}
& n=\frac{-59 \pm \sqrt{(59)^{2}-4(1)(-1600)}}{2(1)} \\
& n=\frac{-59 \pm 99.4}{2} \\
& n=\frac{-59-99.4}{2}, n=\frac{-59+99.4}{2} \\
& n=-79.2, n=20.2
\end{aligned}
$$

Clearly $n=20$ satisfy the inequality.
So, $n=20$ is the maximum months such that payment $S_{n} \leq 400,000$.

# EXERCISE 6.11

1. A sum of Rs. 10400 is paid off in 40 instalment such that each instalment is Rs. 10 more than the preceding instalment. Calculate the value of the first instalment.
2. An investor invests Rs. 150000 at an annual compound interest rate of $6 \%$ for 8 years. Find the total amount will he get after 8 years.
3. The population of a town is 4084101 at present and five years ago it was 3200000 . Find its rate of increase if it increased geometrically.
4. Determine the total worth of a yearly Rs. 5000 investment after 20 years if the interest rate is $5 \%$ compounded annually.
5. A water tank has a leakage. Each week, the tank loses 5 gallons of water due to the leakage. Initially, the tank is full and contains 2000 gallons.
(i) How many gallons are in the tank 20 weeks later?
(ii) How many weeks until the tank is half-full?
(iii) How many weeks until the tank is empty?
6. A drug company has manufactured 7 million doses of a vaccine to date. They promise additional production at a rate of 1.4 million doses/month over the next year.
(i) How many doses of the vaccine, in total, will have been produced after a year?
(ii) The general term $a_{n}$ describes the total number of doses of the vaccine produced. Describe the meaning of the variable $n$ in the context of this problem. Find the general term $a_{n}$
(iii) Find the value of $a_{10}$ and interpret its meaning in words.
7. At a toll-bent, the number of vehicles passing through during the first minute is 100 . Due to road congestion, each minute only $80 \%$ of the vehicles from the previous minute manage to pass.
(i) Represent the number of vehicles passing each minute as a sequence.
(ii) Find the total number of vehicles that pass through in 15 minutes.
(iii) What is the maximum number of vehicles that can pass in the long run (as time $t \rightarrow \infty$ )
8. A sum of Rs. 5000 is inverted at $8 \%$ simple interest per year. Calculate the interest at the end of each year. Do these interests form an A.P.? If so find the interest at the end of 20 years making use of this fact.

9. A machine is purchased for Rs.20,000. Depreciates at 6% per annum for the first four years and after that 8% per annum for the next six years. Depreciation being calculated on diminishing value. Find the value of the machine after a period of 10 years.
10. Two cars start together in the same direction from the same place. The first goes with uniform speed of 20km/h. The second goes at a speed of 12km/h in the first hour and increases the speed by 1 km/h each succeeding hour. After how many hours will the second car overtake the first car if both cars go non-stop?
11. 150 workers were engaged to finish a piece of work in a certain number of days. Five workers dropped the second day, five more workers dropped the third day and so on. It takes 10 more days to finish the work now. Find the number of days in which the work was completed.
12. A radioactive product has a half life of 5 years. If the radioactivity level is 68 microcuries after 20 years. Determine the original level of radioactivity.
13. An object moving in a line is given an initial velocity of 4.5 m/s and a constant acceleration of 2.5 m/s². How long will it take the object to reach a velocity of 20m/s?
14. In an integrated circuit with an initial current of 1080 mA, the temperature in the components decreases from 20% to 17% to 14%. Assuming that each temperature decrease is caused by a decrease in the initial current, what is the value of the current at fourth measurement?
15. Show that the amount of a certain sum of money at compound interest of r% per year for n years form a G.P.