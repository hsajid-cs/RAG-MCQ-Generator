### 2.11 DERIVATIVE OF THE LOGARITHMIC FUNCTION

## Logarithmic Function:

If $a>0 \quad a \neq 1$ and $x=a$, then the function defind by

$$
y=\log _{a}{ }^{x} \quad(x \quad 0)
$$

is called the logarithm of $x$ to the base a.
The logarithmic functions $\log _{a}{ }^{x}$ and $\log _{10}{ }^{x}$ are called natural and common logarithms respectively, $y=\log _{a}{ }^{x}$ is written as $y=\ln x$.

We first find $\frac{d}{d x}(\ln x)$.
Let $y=\ln x$ Then

$$
\begin{aligned}
& y+\delta y=\ln (x+\delta x) \quad \text { and } \\
& \delta y=\ln (x+\delta x)-\ln x=\left(\frac{x+\delta x}{x}\right)=\ln \left(1+\frac{\delta x}{x}\right)
\end{aligned}
$$

Now $\quad \frac{\delta y}{\delta x}=\frac{1}{\delta x} \ln \left(1+\frac{\delta x}{x}\right)$

$$
=\frac{1}{x} \frac{x}{\delta x} \ln \left(1+\frac{\delta x}{x}\right)=\frac{1}{x} \ln \left(1+\frac{\delta x}{x}\right)^{\frac{x}{d x}}
$$

Thus $\lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0}\left[\frac{1}{x} \ln \left(1+\frac{\delta x}{x}\right)^{\frac{x}{d x}}\right]=\frac{1}{x} \lim _{\delta x \rightarrow 0}\left[\ln \left(1+\frac{\delta x}{x}\right)^{\frac{x}{d x}}\right]$

$$
\frac{d y}{d x}=\frac{1}{x} \cdot \ln \left[\lim _{\frac{x}{x} \rightarrow 0}\left(1 \cdot \frac{\delta x}{x}\right)^{\frac{x}{d x}}\right]
$$

$\left(\because \frac{\delta x}{x} \rightarrow 0\right.$ when $\left.\delta x \rightarrow 0\right)$

$$
\begin{aligned}
& =\frac{1}{x} \ln e \quad\left[\because \lim _{z \rightarrow 0}(1+z)^{\frac{x}{z}}=e\right] \\
& =\frac{1}{x} \cdot 1=\frac{1}{e} \quad=\left(\because \log _{e}^{e} 1\right)
\end{aligned}
$$

Now we find derivative of the general logarithmic function.
Let $\quad y=\log _{a}{ }^{x}$ then

$$
\begin{aligned}
& y+\delta y=\log _{a}(x+\delta x) \text { and } \\
& \delta y=\log _{a}(x+\delta x)-\log _{a}{ }^{x}=\log \left(\frac{x+\delta x}{x}\right)=\log _{a}\left(1+\frac{\delta x}{x}\right) \\
& \frac{\delta y}{\delta x}=\frac{1}{\delta x} \log _{a}\left(1+\frac{\delta x}{x}\right)=\frac{1}{x} \cdot \frac{x}{\delta x} \log _{a}\left(1+\frac{\delta x}{x}\right) \\
&=\frac{1}{x} \log _{a}\left(1+\frac{\delta x}{x}\right)^{\frac{x}{d x}}
\end{aligned}
$$

Thus $\frac{d y}{d x}=\lim _{\delta x \rightarrow 0}\left[\frac{1}{x} \log _{a}\left(1+\frac{\delta x}{x}\right)^{\frac{x}{d x}}\right]=\frac{1}{x} \lim _{\delta x \rightarrow 0}\left[\log _{a}\left(1+\frac{\delta x}{x}\right)^{\frac{x}{d x}}\right]$

$$
=\frac{1}{x} \log _{a}\left[\frac{\lim _{\frac{\delta x}{x} \rightarrow 0}}{\frac{\delta x}{x} \rightarrow 0}\left(1 \cdot \frac{\delta x}{x}\right)^{\frac{x}{d x}}\right]
$$

$$
\begin{aligned}
& =\frac{1}{x} \log _{a}^{x} \quad\left(\because \lim _{z \rightarrow 0}(1+z)^{\frac{1}{x}}=e\right) \\
& \text { or } \frac{d}{d x}\left[\log _{a}^{x}\right]=\frac{1}{x} \cdot \frac{1}{\ln \mathrm{a}} \quad\left(\because \log _{a}^{x}=\frac{1}{\log _{a}^{x}} \cdot \frac{1}{\ln \mathrm{a}}\right)
\end{aligned}
$$

Example 1: $\quad$ Find $\frac{d y}{d x}$ if $y=\log _{a x}\left(a x^{2}+b x+c\right)$
Solution: Let $u=a x^{2}+b x+c$ Then

$$
\begin{aligned}
& y=\log _{a x}^{u} \Rightarrow \frac{d y}{d u}=\frac{1}{u} \cdot \frac{1}{\ln 10} \\
& \text { and } \frac{d u}{d x}=\frac{d}{d x}(a x+b x+c)=a(2 x)+b(1)=2 a x+b \\
& \text { Thus } \frac{d y}{d x}=\frac{d y}{d u} \cdot \frac{d u}{d x}=\left(\frac{1}{u} \cdot \frac{1}{\ln 10}\right) \frac{d u}{d x} \\
& =\frac{1}{\left(a x^{2}+b x+c\right) \ln 10}(2 a x \quad b) \\
& \text { or } \frac{d}{d x}\left[\log _{a x}\left(a x^{2}+b x+c\right)\right]=\frac{2 a x+b}{\left(a x^{2}+b x+c\right) \ln 10}
\end{aligned}
$$

Example 2: $\quad$ Differentiate $\ln \left(x^{2}+2 x\right)$ w.r.t.' $x^{\prime}$.
Solution: Let $\quad y=\ln \left(x^{2}+2 x\right)$, then

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left[\ln \left(x^{2}+2 x\right)\right]=\frac{1}{\left(x^{2}+2 x\right)} \cdot \frac{d}{d x}\left(x^{2}+2 x\right) \quad \text { (Using chain rule) } \\
& =\frac{1}{x^{2}+2 x}(2 x+2)=\frac{2(x+1)}{x^{2}+2 x} \\
\text { Thus } \frac{d}{d x}\left[\ln \left(x^{2}+2 x\right)\right] & =\frac{2(x+1)}{x^{2}+2 x}
\end{aligned}
$$

version: 1.1