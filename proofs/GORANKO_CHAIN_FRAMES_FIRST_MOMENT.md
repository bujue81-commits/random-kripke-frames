# A first-moment proof for Goranko's chain frames F_r, r >= 2

Date: 2026-11-25  
Status: internal hand proof; not Lean-formalized or externally refereed.

## Theorem

Fix an integer \(r\geq2\). Let \(F_r=(\{0,1,\ldots,r\},R_r)\), where
\[
R_r=\{(i,0):0\leq i\leq r\}
\cup\{(0,j):0\leq j\leq r\}
\cup\{(i,i+1):1\leq i<r\}.
\]
This is the family used in the proof of Proposition 4.7 of Goranko (2020).

Let \(G_m\) be the labelled random directed frame on \(m\) vertices, with each ordered edge (including loops) independently present with probability \(1/2\). Then, for every fixed \(r\geq2\), there is \(c_r>0\) such that
\[
\Pr(G_m\twoheadrightarrow F_r)
\leq \exp\bigl(-c_r(\ln m)^2\bigr)
\]
for all sufficiently large \(m\). In particular,
\[
\Pr(G_m\twoheadrightarrow F_r)\longrightarrow0.
\]

The constants may depend on the fixed target size \(r\). The case \(r=1\), which is the single-kernel frame \(K_2\), is not covered by this estimate and is already known by Le Bars' result.

## 1. A necessary event for a fixed fibre partition

Suppose \(h:G_m\twoheadrightarrow F_r\) is a surjective bounded morphism. Write
\[
A_i=h^{-1}(i),\qquad a_i=|A_i|,\qquad 0\leq i\leq r.
\]
All \(a_i\) are positive. Put
\[
S=\sum_{i=1}^r a_i,\qquad a_0=m-S.
\]

### Forth constraints

For every \(i\geq1\), the only allowed target edges from \(i\) to a noncentral point are \(i\to i+1\) when \(i<r\). Therefore
\[
R_m\cap(A_i\times A_j)=\varnothing
\quad\text{whenever }1\leq i,j\leq r,\ j\ne i+1.
\]
Here the condition \(j\ne i+1\) is automatically true for every \(j\) when \(i=r\).

The number of forbidden ordered source pairs is
\[
B(a_1,\ldots,a_r)
=\sum_{i=1}^r a_i(S-a_{i+1})
=S^2-\sum_{i=1}^{r-1}a_i a_{i+1},
\]
where \(a_{r+1}=0\).

### Selected back constraints

Since \(0\to j\) in \(F_r\) for every \(j\), the back condition implies that every row in \(A_0\) has at least one outgoing edge into each \(A_j\), \(1\leq j\leq r\).

For a fixed ordered partition \((A_0,\ldots,A_r)\), the probability of all these selected necessary conditions is exactly
\[
2^{-B(a_1,\ldots,a_r)}
\prod_{j=1}^r(1-2^{-a_j})^{a_0}.
\tag{1}
\]
Indeed, the forbidden rectangles have source in \(A_i\) for \(i\geq1\), while the required-hit rectangles have source in \(A_0\); they are disjoint. The hit rectangles for different \(j\) also have disjoint destination fibres. Independence of the edge variables therefore gives (1).

Let \(Z_m\) count ordered nonempty partitions satisfying precisely these selected conditions. Every bounded morphism onto \(F_r\) gives one such partition, so
\[
\Pr(G_m\twoheadrightarrow F_r)
\leq\Pr(Z_m\geq1)
\leq\mathbb E Z_m.
\tag{2}
\]

## 2. A quadratic lower bound on the number of forbidden edges

Let
\[
O=\sum_{\substack{1\leq i\leq r\\i\text{ odd}}}a_i,
\qquad
E=\sum_{\substack{1\leq i\leq r\\i\text{ even}}}a_i.
\]
Every consecutive product \(a_i a_{i+1}\) is one of the nonnegative terms in \(OE\). Hence
\[
\sum_{i=1}^{r-1}a_i a_{i+1}
\leq OE
\leq\frac{(O+E)^2}{4}
=\frac{S^2}{4}.
\]
Consequently,
\[
B(a_1,\ldots,a_r)\geq\frac34S^2.
\tag{3}
\]

For fixed \(S\), the number of ordered partitions with \(S\) noncentral vertices is at most
\[
\binom mS r^S:
\]
choose the noncentral set and assign each of its vertices one of the \(r\) noncentral labels. This upper bound deliberately allows empty fibres, so it is valid for the surjective partitions as well.

## 3. Split according to the total noncentral fibre size

Set
\[
L_m=\frac34\log_2m,\qquad S_0=rL_m.
\]
For fixed \(r\), \(S_0=O(\ln m)\), so \(a_0=m-S\geq m/2\) whenever \(S<S_0\) and \(m\) is sufficiently large.

We split the expectation into \(S<S_0\) and \(S\geq S_0\).

### Case I: \(S<S_0\)

At least one noncentral fibre, say \(A_j\), has
\[
a_j<L_m.
\]
Otherwise every \(a_j\geq L_m\), forcing \(S\geq rL_m=S_0\). Thus
\[
2^{-a_j}>m^{-3/4}.
\]
The selected back condition that every row in \(A_0\) hits \(A_j\) has probability
\[
(1-2^{-a_j})^{a_0}
\leq\exp(-a_0\,2^{-a_j})
\leq\exp(-m^{1/4}/2).
\tag{4}
\]
We may drop all other probability factors.

The number of partitions in this range is at most
\[
\sum_{S<S_0}\binom mS r^S
\leq (S_0+1)(rm)^{S_0}
=\exp(O_r((\ln m)^2)).
\tag{5}
\]
Combining (4) and (5), the contribution from Case I is
\[
\exp\bigl(-m^{1/4}/2+O_r((\ln m)^2)\bigr).
\tag{6}
\]

### Case II: \(S\geq S_0\)

Drop the selected back factors and use (3). The contribution is at most
\[
\sum_{S\geq S_0}\binom mS r^S2^{-3S^2/4}.
\tag{7}
\]
Using \(\binom mS\leq(em/S)^S\), each summand in (7) is bounded by
\[
\exp\left(
S\left[\ln\left(\frac{erm}{S}\right)
-\frac34(\ln2)S\right]
\right)
\leq
\exp\left(
S\left[\ln(erm)-\frac34(\ln2)S\right]
\right).
\tag{8}
\]
Since
\[
S_0=\frac{3r}{4\ln2}\ln m,
\]
the bracket in (8), for \(S\geq S_0\), is at most
\[
\left(1-\frac{9r}{16}\right)\ln m+O_r(1).
\]
For \(r\geq2\), \(1-\frac{9r}{16}\leq-\frac18\). Hence, for all sufficiently large \(m\), the bracket is at most \(-\frac1{16}\ln m\). Therefore
\[
(7)\leq
m\exp\left(-\frac{S_0}{16}\ln m\right)
=\exp\bigl(-\Omega_r((\ln m)^2)\bigr).
\tag{9}
\]

## 4. Conclusion

Combining (6) and (9),
\[
\mathbb E Z_m
\leq
\exp\bigl(-m^{1/4}/2+O_r((\ln m)^2)\bigr)
+\exp\bigl(-\Omega_r((\ln m)^2)\bigr)
=\exp\bigl(-\Omega_r((\ln m)^2)\bigr).
\]
By (2) and Markov's inequality,
\[
\boxed{
\Pr(G_m\twoheadrightarrow F_r)
=\exp\bigl(-\Omega_r((\ln m)^2)\bigr)
\longrightarrow0
}
\qquad(r\geq2\text{ fixed}).
\]

This supplies an alternative combinatorial-probabilistic route to the almost-sure validity of \(\chi_{F_r}\) for \(r\geq2\), assuming Goranko's characteristic-formula correspondence. It does not use the invalid preservation claim about \(\eta\).

## 5. Relation to the eta-preservation counterexample

The preceding argument is compatible with the finite counterexample to the claim that
\[
\eta=\forall x\exists y(Rxy\land\neg Ryy)
\]
is preserved under surjective bounded morphisms. The counterexample shows that Goranko's stated shortcut in Proposition 4.7 is invalid. The present first-moment argument instead uses:
1. the forbidden noncentral-to-noncentral edge rectangles forced by forth; and
2. the requirement that every row in the central fibre hit every noncentral fibre, forced by back.

The proof is a hand argument. It should be checked independently before being treated as a settled repair of Proposition 4.7, and it is not formalized in Lean.
