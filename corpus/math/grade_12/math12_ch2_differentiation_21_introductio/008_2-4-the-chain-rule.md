### 2.4 THE CHAIN RULE

The composition fog of functions $f$ and $g$ is the function whose values $f(g(x))$, are found for each $x$ in the domain of $g$ for which $g(x)$ is in the domain of $f(f(g(x)))$ is read as $f$ of $g$ of $x$ ).

Theorem. If $g$ is differentiable at the point $x$ and $f$ is differentiable at the point $g(x)$ then the composition function fog is differentiable at the point $x$ and $(\text { fog })^{*}(x)=f^{*}[g(x)] \cdot g^{*}(x)$. The proof of the chain rule is beyond the scope of this book.

$$
\begin{aligned}
& \text { If } y=(\text { fog })(x)=f[g(x)], \text { then } \\
& \qquad(\text { fog })^{*}(x)=\frac{f}{2} f[g(x)]^{\frac{1}{2}} \cdot \frac{d y}{d x} \\
& \Rightarrow \frac{d y}{d x}=f^{*}[g(x)] \cdot g^{*}(x) \\
& \text { Let } u=g(x) \\
& \text { Then } y=f(u)
\end{aligned}
$$

Differentiating (ii) and (iii) w.r.t $x$ and $u$ respectively, we have.

$$
\frac{d u}{d x}=\frac{d}{d x}[g(x)]=g^{*}(x)
$$

and $\frac{d y}{d u}=\frac{d}{d u}[f(u)]=f^{*} u$
Thus (i) can be written in the following forms
(a) $\frac{d}{d x}(f(u))=f^{*}(u) \frac{d u}{d x}$
(b) $\frac{d y}{d u}=\frac{d y}{d u} \frac{d u}{d x}$

The proof of the Chain rule is beyond the scope of this book.

$$
\begin{aligned}
& \text { Note: 1. Let } y=\frac{1}{2} g(x)^{\frac{1}{2}} \text { and } u \quad g(x) \\
& \text { Then } y=u^{4} \text { and } \frac{d y}{d u}=n u^{n-1} \quad \text { (power rule) } \\
& \text { But } \frac{d y}{d x}=\frac{d y}{d u} \frac{d u}{d x}=n u^{n-1} \frac{d u}{d x} \\
& \text { or } \frac{d}{d x}[g(x)]^{n}=n[g(x)]^{\frac{n-1}{2}} \cdot g^{*}(x) \quad\left(1 \cdot \frac{d u}{d x}=g^{*}(x)\right)
\end{aligned}
$$

2. Reciprocal rule can be written as

$$
\begin{aligned}
\frac{d}{d x}\left(\frac{1}{g(x)}\right)=\frac{d}{d x}[g(x)]^{-1} & =-1 \cdot[g(x)]^{-1.5} \cdot g^{*}(x) \\
& =(-1)[g(x)]^{-1} \cdot g^{*}(x)
\end{aligned}
$$

Example 1: Find the derivative of $\left(x^{2}+1\right)^{n}$ with respect to

Solution: $\quad$ Let $y=\left(x^{2}-1\right)^{2}+$ and $u \neq 1$ Then $y \quad u^{n}$

$$
\text { Now } \frac{d u}{d x}=a x^{2} \text { and } \frac{d y}{d u} \quad 9 u^{4}
$$

Using the formula $\frac{d y}{d x}=9 u^{2} \frac{d u}{d x}$, we have
or $\quad \frac{d}{d x}\left(x^{2}+1\right)^{4}=9\left(x^{2}+1\right)^{4}\left(3 x^{2}\right) \quad\left(\because u=x^{2}+1\right.$ and $\left.\frac{d u}{d x}=3 x^{2}\right)$

$$
=27 x^{2}\left(x^{2}+1\right)^{4}
$$

Example 2: $\quad$ Differentiate $\sqrt{\frac{a-x}{a+x}},(x \neq-a)$ with respect to $x$
Solution: $\quad$ Let $\quad y=\sqrt{\frac{a-x}{a+x}}$ and $u=\frac{a-x}{a+x}$. Then $y \quad u^{\frac{1}{2}}$

$$
\begin{aligned}
& \text { Now } \frac{d y}{d u}=\frac{1}{2} u^{\frac{1}{2}-1}=\frac{1}{2} u^{-\frac{1}{2}} \\
& \text { and } \frac{d u}{d x}=\frac{d}{d x}\left[\frac{a-x}{a+x}\right]=\frac{\left[\frac{d}{d x}(a-x)\right](a+x)-(a-x)\left[\frac{d}{d x}(a+x)\right]}{(a+x)^{2}} \\
& =\frac{(0-1)(a+x)-(a-x)(0+1)}{(a+x)^{2}} \quad \frac{-a-x-a+x}{(a+x)^{2}} \quad \frac{-2 a}{(a+x)^{2}}
\end{aligned}
$$

Using the formula $\quad \frac{d y}{d x}=\frac{d y}{d u} \frac{d u}{d x}$, we have

$$
\begin{aligned}
& \frac{d}{d x}\left(\sqrt{\frac{a-x}{a+x}}\right)=\frac{1}{2} u^{-\frac{1}{2}}\left[\frac{-2 a}{(a+x)^{2}}\right]=\frac{1}{2}\left(\frac{a-x}{a+x}\right)^{-\frac{1}{2}} \times \frac{-2 a}{(a+x)^{2}}\left(\because u=\frac{a-x}{a+x}\right) \\
& \quad=\frac{(a-x)^{-\frac{1}{2}}}{(a+x)^{-\frac{1}{2}}} \times \frac{-a}{(a+x)^{2}}=\frac{-a}{(a-x)^{\frac{1}{2}}(a+x)^{\frac{1}{2}}}
\end{aligned}
$$

Example 3: $\quad$ Find $\frac{d y}{d x}$ if $y=\frac{\sqrt{a+x}+\sqrt{a-x}}{\sqrt{a+x}-\sqrt{a-x}} \quad(x \neq 0)$
Solution: $\quad y=\frac{\sqrt{a+x}}{\sqrt{a+x}-\sqrt{a-x}}$
Multiplying the numerator and the denominator by $\sqrt{a+x}-\sqrt{a-x}$, gives

$$
\begin{aligned}
y & =\frac{(\sqrt{a+x}+\sqrt{a-x})(\sqrt{a+x}-\sqrt{a-x})}{(\sqrt{a+x}-\sqrt{a-x})(\sqrt{a+x}-\sqrt{a-x})} \\
& =\frac{(\sqrt{a+x})^{\frac{1}{2}}-(\sqrt{a-x})^{\frac{1}{2}}}{(a+x)+(a-x)-2 \sqrt{a^{2}-x^{2}}}-\frac{(a+x)-(a-x)}{2 a-2 \sqrt{a^{2}-x^{2}}} \quad \frac{2 x}{2\left(a-\sqrt{a^{2}-x^{2}}\right)}
\end{aligned}
$$

that is, $y=\frac{x}{a-\sqrt{a^{2}-x^{2}}}$
Let $f(x)=x$ and $g(x)=a-\sqrt{a^{2}-x^{2}}$, then
$f(x)^{x}=1$ and $\cdot g^{\prime}(x)=0 \cdot \frac{d}{d x}\left(\mathbf{a}^{2} \quad \mathbf{x}^{2}\right)^{\frac{1}{2}} \quad \frac{1}{2}\left(a^{2}-\mathbf{x}^{2}\right)^{\frac{1}{2}-1} \frac{d}{d x}\left(a^{2} \quad x^{2}\right)$

$$
--=\frac{1}{2 \sqrt{a^{2}-x^{2}}} \times(2 \alpha) \frac{x}{\sqrt{a^{2}-x^{2}}}
$$

Using the formula $\frac{d y}{d x}=\frac{f^{\prime}(x) g(x)-f(x) g^{\prime}(x)}{[g(x)]^{4}}$, we have

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{1 \cdot\left(a-\sqrt{a^{2}-x^{2}}\right)-x \cdot \sqrt{a^{2}-x^{2}}}{\left(a-\sqrt{a^{2}-x^{2}}\right)} \\
& =\frac{a \sqrt{a^{2}-x^{2}}-\left(a^{2}-x^{2}\right)-x^{2}}{\sqrt{a^{2}-x^{2}}\left(a-\sqrt{a^{2}-x^{2}}\right)^{2}}-\frac{a \sqrt{a^{2}-x^{2}}-a^{4}}{\sqrt{a^{2}-x^{2}}\left(a-\sqrt{a^{2}-x^{2}}\right)^{4}}
\end{aligned}
$$

$$
=\frac{-a\left(a-\sqrt{a^{2}-x^{2}}\right)}{\sqrt{a^{2}-x^{2}}\left(a-\sqrt{a^{2}-x^{2}}\right)^{2}}=\frac{-a}{\sqrt{a^{2}-x^{2}}\left(a-\sqrt{a^{2}-x^{2}}\right)^{2}}
$$

Example 4: $\quad$ Find $\frac{d y}{d x}$ if $y=(1+2 \sqrt{x})^{\frac{1}{2}} \cdot x^{\frac{3}{2}}$
Solution: $y=\left(\begin{array}{lll}1 & \text { a } \sqrt{\pi}\end{array}\right)^{\frac{1}{2}} \cdot x^{\frac{3}{2}}\left[\left(\begin{array}{lll}1 & 2 \sqrt{x}\end{array}\right)\left(x^{\frac{1}{2}}\right)\right]^{\frac{1}{2}}$
Let $\quad u=(1+2 \sqrt{x}) \cdot x^{\frac{1}{2}}$
Then $\quad y=u^{3}$
Differentiating (ii) with respect to $u$, we have

$$
\frac{d y}{d x}=3 u^{2} \quad 3\left[\left(\begin{array}{ll}
1 & 2 \sqrt{x}
\end{array}\right) x^{\frac{1}{2}}\right]^{2} \quad 3\left(\begin{array}{ll}
1 & 2 \sqrt{x}
\end{array}\right)^{2} \cdot x
$$

Differentiating (i) with respect to $x$, gives

$$
\begin{aligned}
& \frac{d u}{d x}=\left(0+2 \cdot \frac{1}{2 \sqrt{x}}\right) x^{\frac{1}{2}}+(1+2 \sqrt{x}) \frac{1}{2 \sqrt{x}} \\
& \quad=1 \quad \frac{1+2 \sqrt{x}}{2 \sqrt{x}} \quad \frac{2 \sqrt{x}+1+2 \sqrt{x}}{2 \sqrt{x}} \quad \frac{1+4 \sqrt{x}}{2 \sqrt{x}}
\end{aligned}
$$

Using the formula $\frac{d y}{d x}=\frac{d y}{d u} \frac{d u}{d x}$, we have

$$
\begin{aligned}
\frac{d}{d x}\left[(1+2 \sqrt{x})^{2} \cdot x^{\frac{1}{2}}\right] & =3\left(\begin{array}{ll}
1 & 2 \sqrt{x}
\end{array}\right)^{2} \cdot x \cdot x\left(\frac{1+4 \sqrt{x}}{2 \sqrt{x}}\right) \\
& =\frac{3}{2}\left(\begin{array}{ll}
1 & 2 \sqrt{x}
\end{array}\right)^{2} \sqrt{x}\left(\begin{array}{ll}
1 & 4 \sqrt{x}
\end{array}\right) \\
& =-\left(\begin{array}{ll}
1 & 2 \sqrt{x}
\end{array}\right) \cdot\left(\begin{array}{ll}
\sqrt{x} & 4 x
\end{array}\right)
\end{aligned}
$$

Example 5: If $y=(a x+b)^{n}$ where $n$ is a negative integer, find $\frac{d y}{d x}$ using quotient theorem
Solution: Let $n=-m$ where $m$ is a positive integer. Then
version: 1.1

$$
y=(a x+b)^{n}=(a x+b)^{-m}=\frac{1}{(a x+b)^{m}}
$$

We first find $\frac{d}{d x}(a x+b)^{m}$. Let $u=a x \quad b$. Then

$$
\begin{aligned}
& \frac{d}{d x}(a x+b)^{m}=\frac{d}{d x}\left(u^{m}\right)=\frac{d}{d x}\left(u^{m}\right) \frac{d u}{d x} \quad \text { (using chain rule) } \\
& \quad=m u^{m-1} \times \mathrm{a}=\mathrm{m}\left(\begin{array}{ll}
a x & b
\end{array}\right)^{m-1} \cdot a \quad\left(\because \frac{d}{d x}(a x+b)=a\right)
\end{aligned}
$$

Now differentiating (i) w.r.t. ${ }^{x}$, we have

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left[\frac{1}{(a x+b)^{m}}\right] \frac{\frac{d}{d x}(1) \cdot(a x+b)^{m}-1 \cdot \frac{d}{d x}(a x+b)^{m}}{\left[(a x+b)^{m}\right]^{m}} \\
& =\frac{0 \cdot(a x+b)^{m}-1 \cdot m(a x+b)^{m-1} \cdot a}{(a x+b)^{1 / m}} \\
& \quad-=\left(\begin{array}{ll}
m(a x & b)^{m-1} \cdot a
\end{array}\right) \times(a \neq b)^{-2 / m}+m(a x \quad b)^{m-1-2 / m} \cdot a \\
& \quad=(-m)(a x+b)^{-m-1} \cdot a+=n(a x \quad b)^{n-1} \cdot a=(\because \cdot m \quad n)
\end{aligned}
$$

Example 6: $\quad$ Find $\frac{d y}{d x}$ if $y=x^{n}$ where $n=\frac{p}{q}, q \neq 0$
Solution: Given that $y=x^{n}$ where $n=\frac{p}{q}, q \quad 0$, putting $n \quad \frac{p}{q}$, we have

$$
y=x^{\frac{p}{q}}
$$

Taking qth power of both sides of (i), we get

$$
y^{q}=x^{p}
$$

Differentiating both sides of (ii) w.r.t. ${ }^{x} x^{x}$, gives

$$
\begin{aligned}
& \frac{d}{d x}\left(y^{p}\right)=\frac{d}{d x}\left(x^{p}\right) \text { or } \frac{d}{d y}\left(y^{q}\right) \cdot \frac{d y}{d x}=\frac{d}{d x}\left(x^{p}\right) \text { (Using chain rule) } \\
& \Rightarrow \mathrm{q} \mathrm{y}^{p-1} \frac{d y}{d x}=\mathrm{px}^{p-1}
\end{aligned}
$$

Multiplying both sides of (iii) by $y$, we have

$$
\begin{aligned}
& q \cdot y^{p} \frac{d y}{d x}=p y x^{p-1} \text { or } \quad \text { q. } x^{p} \frac{d y}{d x}=p \cdot x^{p} \quad x^{p-1} \quad \text { (using (i) and (ii)) } \\
& \Rightarrow \frac{d y}{d x}=\frac{p}{q} \cdot \frac{1}{x^{p}} \cdot \frac{p}{x^{p}} x^{p-1}=\frac{p}{q} \times x^{\frac{p}{q} \times q \cdot x \cdot p} \\
& \quad \times \frac{p}{q} \times \frac{p}{q-1}=\mathrm{nx}^{n-1}\left[\cdot \frac{p}{q}=\mathrm{n}\right] \\
& \text { Thus } \frac{d}{d x}\left(x^{n}\right) \mathrm{n} x^{n-1} \text {. }
\end{aligned}
$$