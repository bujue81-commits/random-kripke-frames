# First-moment proof for F0001

## Theorem

Let \(G_n=([n],R_n)\) be the labelled random directed frame in which all \(n^2\) ordered edges, including loops, are independent Bernoulli\((1/2)\) variables. Let

\[
F_0=(\{c,a,b\},R_0),\qquad
M_0=\begin{pmatrix}1&1&1\\1&0&0\\1&0&1\end{pmatrix}.
\]

Then the first-moment argument below gives the quantitative bound
\[
\Pr(G_n\twoheadrightarrow F_0)=O(1/\sqrt{\ln n}),
\]
and hence convergence to zero.

This proof is a probability statement about the specified labelled model. The logical consequence for the characteristic formula uses the Jankov--Fine correspondence separately.

## 1. A necessary-condition witness count

Suppose \(h:G_n\twoheadrightarrow F_0\) is a surjective bounded morphism and write its nonempty fibres as
\[
A=h^{-1}(a),\quad B=h^{-1}(b),\quad C=h^{-1}(c).
\]
Set \(a=|A|,b=|B|,c=|C|\).

The forth condition and the target matrix imply
\[
R_n\cap(A\times A)=\varnothing,
\]
\[
R_n\cap(A\times B)=R_n\cap(B\times A)=\varnothing.
\]
The back condition also implies
\[
\forall x\in A\;\exists y\in C\;(xR_ny),
\qquad
\forall x\in C\;\exists y\in A\;(xR_ny).
\]

These are only selected necessary conditions. We do not claim they are sufficient for a bounded morphism. Let \(Z_n\) be the number of ordered nonempty partitions \((A,B,C)\) satisfying precisely these conditions. Then
\[
\{G_n\twoheadrightarrow F_0\}\subseteq\{Z_n\geq1\}.
\]

For a fixed partition with sizes \((a,b,c)\), the three forbidden edge rectangles are disjoint and contain \(a^2+2ab\) ordered pairs. The two required nonempty-neighbour conditions use the disjoint rectangles \(A\times C\) and \(C\times A\). Independence therefore gives
\[
\Pr((A,B,C)\text{ is counted})
=2^{-a^2-2ab}(1-2^{-c})^a(1-2^{-a})^c.
\]

Consequently,
\[
\mathbb E Z_n=
\sum_{\substack{a+b+c=n\\a,b,c\geq1}}
\binom{n}{a,b,c}
2^{-a^2-2ab}
(1-2^{-c})^a(1-2^{-a})^c.
\tag{1}
\]

## 2. Reduction to a one-dimensional sum

Drop the factor \((1-2^{-c})^a\leq1\). For fixed \(a\), put
\[
q=2^{-a},\qquad N=n-a.
\]
Summing over all \(b=0,\ldots,N\), which only enlarges the original sum, yields
\[
\begin{aligned}
\mathbb E Z_n
&\leq\sum_{a=1}^{n-2}
\binom na2^{-a^2}
\sum_{b=0}^{N}\binom Nb q^{2b}(1-q)^{N-b}\\
&=\sum_{a=1}^{n-2}
\binom na2^{-a^2}(1-q+q^2)^{n-a}.
\end{aligned}
\tag{2}
\]

Define
\[
\lambda_a=n2^{-a}=nq.
\]
Since
\[
\binom na2^{-a^2}
\leq\frac{n^a2^{-a^2}}{a!}
=\frac{\lambda_a^a}{a!}
\]
and
\[
1-q+q^2=1-q(1-q)\leq e^{-q(1-q)},
\]
we have
\[
\mathbb E Z_n
\leq
\sum_{a=1}^{n-2}
\frac{\lambda_a^a}{a!}
e^{-(n-a)2^{-a}(1-2^{-a})}.
\tag{3}
\]

## 3. Small values of the fibre size

Let
\[
A_n=\left\lfloor\frac12\log_2n\right\rfloor.
\]
For \(1\leq a\leq A_n\), we have
\[
\lambda_a\leq n,\qquad
2^{-a}\geq n^{-1/2},\qquad
1-2^{-a}\geq\frac12,
\]
and, for sufficiently large \(n\), \(n-a\geq n/2\). Thus the \(a\)-th summand in (3) is at most
\[
n^a e^{-\sqrt n/4}.
\]
There are at most \(O(\log n)\) such indices, and
\[
\sum_{a\leq A_n}n^ae^{-\sqrt n/4}
\leq O(\log n)
\exp\left(O((\ln n)^2)-\frac{\sqrt n}{4}\right)
\longrightarrow0.
\tag{4}
\]

## 4. Large values and Poisson point probabilities

For \(a>A_n\), set \(q=2^{-a}\). Then \(q<n^{-1/2}\). Moreover,
\[
\lambda_a-(n-a)q(1-q)
=aq+(n-a)q^2
\leq aq+nq^2.
\]
Since \(a2^{-a}\) decreases for \(a\geq1\),
\[
\sup_{a>A_n}aq
\leq(A_n+1)2^{-(A_n+1)}
=O\left(\frac{\log n}{\sqrt n}\right),
\]
while \(nq^2<1\). Hence, uniformly for \(a>A_n\),
\[
\lambda_a-(n-a)q(1-q)\leq1+o(1).
\]
Writing
\[
\pi_\lambda(k)=e^{-\lambda}\frac{\lambda^k}{k!},
\]
the corresponding summand in (3) is bounded by
\[
e^{1+o(1)}\pi_{\lambda_a}(a),
\tag{5}
\]
where the \(o(1)\) is uniform in this range.

It remains to prove
\[
\sum_{a>A_n}\pi_{\lambda_a}(a)\longrightarrow0.
\tag{6}
\]

Put
\[
r_a=\frac{\lambda_a}{a}=\frac{n}{a2^a}.
\]
Then
\[
\frac{r_{a+1}}{r_a}=\frac{a}{2(a+1)}<\frac12.
\tag{7}
\]
Thus at most two indices can satisfy
\[
\frac12\leq r_a\leq2.
\]
Every such index tends to infinity with \(n\), since for bounded \(a\) the ratio \(n/(a2^a)\) tends to infinity. Stirling's inequality gives, for \(r\in[1/2,2]\),
\[
\pi_{ra}(a)
\leq\frac{C}{\sqrt a}
\exp\{-a(r-1-\ln r)\}
\leq\frac{C}{\sqrt a}.
\]
The contribution from these at most two indices therefore tends to zero.

For \(r_a<1/2\), the Poisson upper-tail Chernoff bound gives
\[
\pi_{\lambda_a}(a)
\leq\Pr(\operatorname{Pois}(\lambda_a)\geq a)
\leq e^{-\gamma a},
\]
where
\[
\gamma=\ln2-\frac12>0.
\]
For \(r_a>2\), the lower-tail Chernoff bound gives
\[
\pi_{\lambda_a}(a)
\leq\Pr(\operatorname{Pois}(\lambda_a)\leq a)
\leq e^{-a/4}
\leq e^{-\gamma a}.
\]
Therefore
\[
\sum_{\substack{a>A_n\\r_a\notin[1/2,2]}}
\pi_{\lambda_a}(a)
\leq\sum_{a>A_n}e^{-\gamma a}
\longrightarrow0.
\]
Together with the central-index estimate this proves (6). More quantitatively,
the central contribution is at most
\[
\frac{2C}{\sqrt{A_n+1}}=O(1/\sqrt{\ln n}),
\]
and the noncentral contribution is
\(O(e^{-\gamma A_n})\). Thus
\[
\sum_{a>A_n}\pi_{\lambda_a}(a)=O(1/\sqrt{\ln n}).
\tag{7}
\]

## 5. Conclusion

The small-fibre contribution (4) is \(o(1/\sqrt{\ln n})\), and
(5), (7) show that the large-fibre contribution is
\(O(1/\sqrt{\ln n})\). Hence
\[
\mathbb E Z_n=O(1/\sqrt{\ln n}).
\]
By Markov's inequality and the necessary-condition inclusion,
\[
\boxed{\Pr(G_n\twoheadrightarrow F_0)=O(1/\sqrt{\ln n}).}
\]
This proves the theorem. \(\square\)

## 6. Logical corollary

If \(\chi_{F_0}\) is the Jankov--Fine characteristic formula in a language for which
\[
G\models_{\rm frame}\chi_{F_0}
\quad\Longleftrightarrow\quad
G\not\twoheadrightarrow F_0,
\]
then
\[
\Pr(G_n\models_{\rm frame}\chi_{F_0})\longrightarrow1.
\]

This corollary is conditional only on the cited characteristic-formula theorem and its language conventions; it is not an additional probabilistic estimate.


## Prior-work note

Schamm (2002), Section 3.3.6, already includes this frame in the experimental classification of all 16 three-point central-point frames. Under the bit order in his Java code, this target has mask 8. The natural reading of Figure 4.1 places it in a “No growth” cell. The present document should therefore be treated as an attempt to make that candidate's first-moment argument rigorous, not as discovery of a new candidate.
