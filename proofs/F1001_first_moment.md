# First-moment proof draft for F1001

## Theorem

Let \(G_n=([n],R_n)\) be the labelled random directed frame in which all \(n^2\) ordered edges, including loops, are independent Bernoulli\((1/2)\) variables. Let
\[
F_1=(\{c,a,b\},R_1),\qquad
M_1=\begin{pmatrix}1&1&1\\1&1&0\\1&0&1\end{pmatrix}.
\]
Then
\[
\Pr(G_n\twoheadrightarrow F_1)\longrightarrow0.
\]

The proof below is a hand-proof draft. The estimates are made explicit so that they can be independently checked and later formalized. This document does not claim Lean verification.

## 1. Exact first moment

For a surjective bounded morphism \(h:G_n\to F_1\), let
\[
A=h^{-1}(a),\quad B=h^{-1}(b),\quad C=h^{-1}(c)
\]
with sizes \(a,b,c\geq1\), \(a+b+c=n\).

The forth condition forces
\[
R_n\cap(A\times B)=R_n\cap(B\times A)=\varnothing.
\]
The back condition forces:
- every vertex of \(A\cup C\) to have an outgoing edge into \(A\);
- every vertex of \(B\cup C\) to have an outgoing edge into \(B\);
- every vertex of \([n]\) to have an outgoing edge into \(C\).

These conditions are also sufficient when combined with the two forbidden rectangles: they are exactly the row-wise forth/back requirements for the target matrix \(M_1\).

Let \(X_n\) count the ordered labelled partitions \((A,B,C)\) satisfying these conditions. For a fixed partition:
- the two forbidden rectangles contribute \(2^{-2ab}\);
- the \(n\) independent source rows must each hit \(C\), contributing \((1-2^{-c})^n\);
- the \(n-b\) rows in \(A\cup C\) must each hit \(A\), contributing \((1-2^{-a})^{n-b}\);
- the \(n-a\) rows in \(B\cup C\) must each hit \(B\), contributing \((1-2^{-b})^{n-a}\).

The edge sets involved are disjoint by target fibre, so these events are independent. Hence
\[
\mathbb E X_n=
\sum_{\substack{a+b+c=n\\a,b,c\geq1}}
T_{n,a,b},
\]
where
\[
T_{n,a,b}=
\binom{n}{a,b,c}
2^{-2ab}
(1-2^{-c})^n
(1-2^{-a})^{n-b}
(1-2^{-b})^{n-a}.
\tag{1}
\]
Since \(G_n\twoheadrightarrow F_1\) iff \(X_n\geq1\),
\[
\Pr(G_n\twoheadrightarrow F_1)\leq\mathbb E X_n.
\tag{2}
\]
The summand is symmetric in \(a,b\), so it suffices to sum over \(1\leq a\leq b\), multiplying by at most two.

## 2. The scale of the fibre sizes

Put
\[
\lambda_j=n2^{-j},\qquad r_j=\frac{\lambda_j}{j}=\frac{n}{j2^j}.
\]
Let
\[
m_n=\min\{j\geq1:r_j\leq1\},\qquad
L_n=\left\lceil4\log_2\ln n\right\rceil.
\]
Then
\[
\frac{r_{j+1}}{r_j}=\frac{j}{2(j+1)}<\frac12.
\tag{3}
\]
For sufficiently large \(n\), \(m_n\to\infty\) and
\[
\frac13<r_{m_n}\leq1.
\tag{4}
\]
Indeed \(r_{m_n-1}>1\), and
\(r_{m_n}=r_{m_n-1}(m_n-1)/(2m_n)>(m_n-1)/(2m_n)\), which is greater than \(1/3\) once \(m_n\geq3\).

In particular,
\[
m_n=\log_2 n-\log_2\ln n+O(1).
\tag{5}
\]

We split the sum over \(a\leq b\) into small, middle, and large \(a\).

## 3. Small fibres: \(a\leq m_n-L_n\)

Write \(q=2^{-a}\) and \(N=n-a\). In (1), discard the factors
\((1-2^{-c})^n\) and \((1-2^{-b})^{n-a}\), and retain
\((1-q)^{n-b}\). Since \(2^{-2ab}=q^{2b}\),
\[
T_{n,a,b}
\leq \binom na\binom Nb q^{2b}(1-q)^{N-b}.
\]
For \(b\geq a\), use
\[
\binom Nb
=\binom Na\binom{N-a}{b-a}/\binom ba
\leq\binom Na\binom{N-a}{b-a}.
\]
Summing over \(b\geq a\) and applying the binomial theorem gives
\[
\sum_{b\geq a}T_{n,a,b}
\leq
\binom na\binom{n-a}{a}q^{2a}
(1-q+q^2)^{n-2a}.
\tag{6}
\]
Now
\[
\binom na\binom{n-a}{a}q^{2a}
\leq
\frac{n^{2a}2^{-2a^2}}{(a!)^2}
=\frac{\lambda_a^{2a}}{(a!)^2}.
\]
Also
\[
1-q+q^2=1-q(1-q)\leq e^{-q(1-q)}.
\]
For \(a\leq m_n-L_n=O(\ln n)\), eventually \(n-2a\geq n/2\), while \(q\leq1/2\). Thus
\[
(1-q+q^2)^{n-2a}\leq e^{-\lambda_a/4}.
\]
By (3) and (4),
\[
r_a\geq r_{m_n}2^{m_n-a}
\geq\frac13(\ln n)^4.
\]
Using \(a!\geq(a/e)^a\) and \(r_a\leq n\), (6) is bounded by
\[
\exp\left(2a(1+\ln n)-\frac{a(\ln n)^4}{12}\right).
\]
The sum of this expression over all small \(a\) tends to zero.

## 4. Large fibres: \(a\geq m_n+L_n\)

Discard all probability factors in (1) except \(2^{-2ab}=q^{2b}\). Then
\[
\sum_{b\geq a}T_{n,a,b}
\leq
\binom na\sum_{b\geq a}\binom{n-a}{b}q^{2b}.
\]
Put \(x=(n-a)q^2\). Since
\[
\sum_{b\geq a}\binom{N}{b}q^{2b}
\leq\sum_{b\geq a}\frac{x^b}{b!}
\leq e^x\frac{x^a}{a!},
\]
we obtain
\[
\sum_{b\geq a}T_{n,a,b}
\leq e^x\frac{(n x)^a}{(a!)^2}
\leq e^x\left(\frac{e\lambda_a}{a}\right)^{2a}
=e^x(e r_a)^{2a}.
\tag{7}
\]
By (3), \(r_a\leq2^{-L_n}\leq(\ln n)^{-4}\). Also \(\lambda_a\) is decreasing in \(a\), and
\[
\lambda_a\leq\lambda_{m_n}2^{-L_n}
\leq m_n(\ln n)^{-4}=O((\ln n)^{-3}).
\]
Therefore \(x\leq n2^{-2a}=\lambda_a^2/n=o(1)\), uniformly in the large region. Equation (7) is bounded by
\[
e^{o(1)}\left(\frac{e}{(\ln n)^4}\right)^{2a}.
\]
Its sum over the large region tends to zero.

## 5. Middle fibres: Poisson approximation

Suppose
\[
m_n-L_n<a<m_n+L_n,\qquad a\leq b.
\]
Then
\[
a=\Theta(\ln n),\qquad
\lambda_a=O((\ln n)^5).
\tag{8}
\]
For \(b=a\) or \(b=a+1\), the following estimates hold uniformly:
\[
\binom{n}{a,b,c}
=(1+o(1))\frac{n^{a+b}}{a!b!},
\]
\[
(1-2^{-c})^n=1+o(1),
\]
\[
(1-2^{-a})^{n-b}=e^{-\lambda_a}(1+o(1)),
\quad
(1-2^{-b})^{n-a}=e^{-\lambda_b}(1+o(1)).
\]
For example, the logarithmic error in the third expression is
\(O(b2^{-a}+n2^{-2a})=o(1)\), uniformly by (8). Consequently,
\[
T_{n,a,b}
=(1+o(1))\pi_{\lambda_a}(b)\pi_{\lambda_b}(a),
\tag{9}
\]
where
\[
\pi_\lambda(k)=e^{-\lambda}\frac{\lambda^k}{k!}.
\]

We need the following lemma.

### Lemma 5.1 (Poisson cross-sum)

\[
S_n=\sum_{i,j\geq1}
\pi_{n2^{-i}}(j)\pi_{n2^{-j}}(i)
\longrightarrow0.
\]

#### Proof

First consider \(i<j\), and write \(j=i+d\), \(t=n2^{-i}\). The summand is
\[
P_{i,d}(t)=
\frac{2^{-id}t^{2i+d}}{i!(i+d)!}
e^{-(1+2^{-d})t}.
\]
Its maximum over \(t>0\) occurs at
\(t=(2i+d)/(1+2^{-d})\), and equals
\[
M_{i,d}=
\frac{2^{-id}}{i!(i+d)!}
\left(\frac{2i+d}{1+2^{-d}}\right)^{2i+d}
e^{-(2i+d)}.
\tag{10}
\]

For \(i=1\), the inequality
\((d+1)!\geq((d+1)/e)^{d+1}\) gives
\[
M_{1,d}
\leq 2^{-d}\frac{d+2}{e}
\left(1+\frac1{d+1}\right)^{d+1}
\leq(d+2)2^{-d}.
\tag{11}
\]
For \(i\geq2\), use
\(i!\geq(i/e)^i\), \((i+d)!\geq((i+d)/e)^{i+d}\), and
\[
(x+y)^{x+y}\leq2^{x+y}x^xy^y\qquad(x,y>0),
\]
with \(x=i,y=i+d\). This yields
\[
M_{i,d}
\leq
\frac{2^{2i+d-id}}{(1+2^{-d})^{2i+d}}.
\tag{12}
\]
The right-hand side is summable over \(i\geq2,d\geq1\). Indeed:
- for \(d=1\), it is \(\frac43(8/9)^i\);
- for \(d=2\), it is \(\frac{64}{25}(16/25)^i\);
- for \(d\geq3\), it is at most \(2^{d-i(d-2)}\), whose sum over \(i\geq2\) is at most \(2^{4-d}/(1-2^{-(d-2)})\leq2^{5-d}\).

The bound (11) is also summable over \(d\). For each fixed pair \((i,d)\), \(t=n2^{-i}\to\infty\), so \(P_{i,d}(t)\to0\). Dominated convergence proves that the off-diagonal sum tends to zero.

For the diagonal, put \(r_i=n/(i2^i)\). Then
\[
r_{i+1}/r_i=i/(2(i+1))<1/2,
\]
so at most two indices satisfy \(1/2\leq r_i\leq2\). Each such index tends to infinity with \(n\), and Stirling's inequality gives
\(\pi_{r_i i}(i)\leq C/\sqrt i\); their squared contribution tends to zero.

Outside this central interval, Poisson Chernoff bounds give
\[
\pi_{r_i i}(i)\leq
\begin{cases}
e^{-\gamma i},&r_i<1/2,\\
e^{-i/4},&r_i>2,
\end{cases}
\qquad \gamma=\ln2-\tfrac12>0.
\]
Thus the squares are dominated by the summable sequence \(e^{-2\gamma i}\). For each fixed \(i\), \(r_i\to\infty\) and \(\pi_{n2^{-i}}(i)\to0\). Dominated convergence proves that the diagonal sum tends to zero. This proves the lemma. \(\square\)

By (9), the contribution of \(b=a\) and \(b=a+1\) in the middle region is bounded by \((1+o(1))S_n\), hence tends to zero.

## 6. The remaining middle tail \(b\geq a+2\)

Let \(q=2^{-a}\) and \(x=nq^2e^q\). From (1), discard all factors except \((1-q)^{n-b}\), and use
\[
\binom{n}{a,b,c}\leq\frac{n^{a+b}}{a!b!},
\qquad
(1-q)^{n-b}\leq e^{-\lambda_a+bq}.
\]
Then
\[
T_{n,a,b}
\leq
\frac{n^a}{a!}e^{-\lambda_a}\frac{x^b}{b!}.
\]
Summing over \(b\geq a+2\) gives
\[
\sum_{b\geq a+2}T_{n,a,b}
\leq
\frac{n^a}{a!}e^{-\lambda_a}
e^x\frac{x^{a+2}}{(a+2)!}.
\]
Uniformly in the middle region, \(x=o(1)\) and \(q(a+2)=o(1)\), so this is
\[
(1+o(1))
\frac{n^{-2}\lambda_a^{2a+4}e^{-\lambda_a}}
{a!(a+2)!}.
\tag{13}
\]

Put \(r=\lambda_a/a\) and
\[
g(r)=2+2\ln(r/2)-r.
\]
Stirling's lower bound, together with
\(n=a r2^a\), transforms (13) into
\[
\frac{C r^2}{a}e^{a g(r)}
\tag{14}
\]
for an absolute constant \(C\).

Now \(g(r)\leq0\), with equality only at \(r=2\). If \(r\leq1\), then \(g(r)\leq g(1)<0\) and \(r^2\leq1\). If \(r\geq4\), then \(g(r)\leq g(4)<0\), and the function \(r\mapsto r^2e^{ag(r)}\) is decreasing on \([4,\infty)\). Finally, at most two indices can satisfy \(1<r_a<4\), by (3); each contributes \(O(1/a)\). Since all middle indices have \(a=\Theta(\ln n)\), and there are \(O(\ln\ln n)\) of them, the sum of (14) tends to zero.

## 7. Conclusion

The small-fibre, large-fibre, central Poisson, and remaining middle-tail contributions all tend to zero. Hence
\[
\mathbb E X_n\longrightarrow0.
\]
By (2) and Markov's inequality,
\[
\boxed{\Pr(G_n\twoheadrightarrow F_1)\longrightarrow0.}
\]
\(\square\)

## 8. Logical consequence

If \(\chi_{F_1}\) is the Jankov--Fine characteristic formula in a language satisfying
\[
G\models_{\rm frame}\chi_{F_1}
\quad\Longleftrightarrow\quad
G\not\twoheadrightarrow F_1,
\]
then
\[
\Pr(G_n\models_{\rm frame}\chi_{F_1})\longrightarrow1.
\]

This is a hand-proof draft, not a Lean-verified theorem or a claim of bibliographic novelty.
