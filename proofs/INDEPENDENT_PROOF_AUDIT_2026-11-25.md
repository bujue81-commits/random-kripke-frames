# Independent proof audit: F0001 and F1001

Date: 2026-11-25  
Scope: internal mathematical audit of the current first-moment drafts and their numerical implementation. This is not an external referee report.

## Executive verdict

- **F0001:** the selected necessary-condition event is correctly defined. Its probability factors over disjoint edge rectangles, the one-dimensional reduction is valid, and the Poisson point-mass sum is summably dominated. The quantitative estimate is \(\Pr(G_n\twoheadrightarrow F_0)=O(1/\sqrt{\ln n})\). Lean checks that every bounded morphism onto F0001 satisfies the selected witness conditions; it does not formalize their probability.
- **F1001:** the exact bounded-morphism event and first-moment formula are correct. The small-fibre and large-fibre bounds are valid. The Poisson cross-sum admits the quantitative bound \(S_n=O(1/m_n)\), and the refined remaining middle tail is \(O(1/\ln n)\). Together these give the hand-proof upper bound \(\Pr(G_n\twoheadrightarrow F_1)=O(1/\ln n)\). Lean checks the exact fibrewise characterization, not the asymptotic estimates.
- **Numerical code:** a fibre-order mismatch was found in the generic audit script. The target matrices use vertex order (c,a,b), whereas the summation variables are named (a,b,c). Because the script sums over every positive triple, permuting all three coordinates leaves the final total unchanged. Nevertheless, the per-triple terms were not aligned with the proof. The script now passes (c,a,b) to the matrix and includes a termwise F1001 formula check.
- These checks support the hand proofs but do **not** constitute Lean formalization, independent peer review, or a bibliographic priority claim.

## 1. F1001: exact bounded-morphism event

The target matrix is written in vertex order (c,a,b):
\[
M_1=\begin{pmatrix}1&1&1\\1&1&0\\1&0&1\end{pmatrix}.
\]
Let the fibres over a,b,c be A,B,C, of sizes a,b,c.

Forth forbids exactly A×B and B×A, contributing \(2^{-2ab}\).

Back is equivalent to:
- every source row hits C;
- every row in A∪C hits A;
- every row in B∪C hits B.

These three destination rectangles are disjoint from each other and from the two forbidden rectangles. Their probabilities multiply, giving
\[
T_{n,a,b}=
\binom{n}{a,b,c}2^{-2ab}
(1-2^{-c})^n
(1-2^{-a})^{n-b}
(1-2^{-b})^{n-a}.
\]
The ordered fibre partition is exactly one surjective map, so
\[
\Pr(G_n\twoheadrightarrow F_1)\leq
\mathbb E X_n=\sum_{a+b+c=n,\ a,b,c\geq1}T_{n,a,b}.
\]

## 2. F1001: small and large fibres

Put \(r_j=n/(j2^j)\), \(m=\min\{j:r_j\leq1\}\), and
\(L=\lceil4\log_2\ln n\rceil\). The identity
\(r_{j+1}/r_j=j/(2(j+1))<1/2\) gives
\(1/3<r_m\leq1\) for large n, and
\(m=\log_2 n-\log_2\ln n+O(1)\).

For small \(a\leq m-L\), the binomial identity used in the draft is exact:
\[
\binom{n-a}{b}
=\binom{n-a}{a}
\binom{n-2a}{b-a}\big/\binom ba.
\]
Since \(\binom ba\geq1\), summing the resulting binomial series yields
\[
\sum_{b\geq a}T_{n,a,b}
\leq
\binom na\binom{n-a}{a}2^{-2a^2}
(1-2^{-a}+2^{-2a})^{n-2a}.
\]
The prefactor is at most \((e r_a)^{2a}\), while the last factor is at most \(e^{-a r_a/4}\). Since \(r_a\geq(\ln n)^4/3\), the sum over the small range tends to zero.

For large \(a\geq m+L\), retaining only the forbidden-rectangle factor and using the exponential tail bound gives
\[
\sum_{b\geq a}T_{n,a,b}
\leq e^x(e r_a)^{2a},\qquad x=(n-a)2^{-2a}.
\]
Here \(r_a\leq(\ln n)^{-4}\), \(\lambda_a=ar_a=O((\ln n)^{-3})\), and \(x\leq\lambda_a^2/n=o(1)\). The sum over the large range tends to zero.

## 3. F1001: central Poisson terms

In the middle range, \(a=\Theta(\ln n)\) and
\(2^{-a}=O((\ln n)^5/n)\). For \(b=a\) or \(a+1\), the multinomial coefficient has relative error \(1+O((\ln n)^2/n)\) when replaced by \(n^{a+b}/(a!b!)\). The logarithmic errors in the two self-hit factors are bounded by
\[
b2^{-a}+n2^{-2a}=O((\ln n)^{10}/n),
\]
and the C-hit factor differs from 1 by \(O(n2^{-c})\). Thus the approximation to
\[
\pi_{\lambda_a}(b)\pi_{\lambda_b}(a),\qquad
\lambda_j=n2^{-j},
\]
is uniform with relative error \(1+O((\ln n)^{10}/n)\).

For the cross-sum
\[
S_n=\sum_{i,j\geq1}\pi_{n2^{-i}}(j)\pi_{n2^{-j}}(i),
\]
write \(j=i+d\) off the diagonal and \(t=n2^{-i}\). The summand is
\[
P_{i,d}(t)=
\frac{2^{-id}t^{2i+d}}{i!(i+d)!}
e^{-(1+2^{-d})t}.
\]
Its maximum over \(t>0\) is the \(M_{i,d}\) in the proof. The displayed bounds are summable:
- \(M_{1,d}\leq(d+2)2^{-d}\);
- for \(i\geq2\), \(d=1\) and \(d=2\) have geometric bounds in \(i\);
- for \(i\geq2,d\geq3\), \(\sum_{i\geq2}M_{i,d}\leq2^{5-d}\).

For each fixed \((i,d)\), \(t\to\infty\), so dominated convergence applies. On the diagonal, \(r_i=n/(i2^i)\) decreases by a factor less than \(1/2\), so at most two indices lie in \([1/2,2]\). Their point masses are \(O(i^{-1/2})\), and outside this band the Chernoff bounds in the draft give a summable exponential majorant. Hence \(S_n\to0\).

## 4. F1001: remaining middle tail

For \(b\geq a+2\), the draft's estimate
\[
\sum_{b\geq a+2}T_{n,a,b}
\leq
e^{x+q(a+2)}
\frac{n^{-2}\lambda_a^{2a+4}e^{-\lambda_a}}
{a!(a+2)!},
\quad q=2^{-a},\quad x=nq^2e^q
\]
is valid. Uniformly in the middle range,
\(x=O((\ln n)^{10}/n)\) and
\(q(a+2)=O((\ln n)^6/n)\).

Using
\(k!\geq\sqrt{2\pi k}(k/e)^k\) for \(k=a,a+2\), and \(n=ar2^a\), gives the explicit bound
\[
\frac{n^{-2}\lambda_a^{2a+4}e^{-\lambda_a}}
{a!(a+2)!}
\leq
\frac{e^2}{2\pi}\frac{r^2}{a}
e^{a(2+2\ln(r/2)-r)}.
\]
The function \(r^2e^{a(2+2\ln(r/2)-r)}\) is at most 16 for all \(r>0,a\geq1\). Therefore the total middle-tail contribution is
\(O(1/\ln n)\).

## 5. F0001 audit

For F0001, the event counted by \(Z_n\) is deliberately weaker than a full bounded morphism. The inclusion
\(\{G_n\twoheadrightarrow F_0\}\subseteq\{Z_n\geq1\}\)
is correct. The forbidden rectangles \(A×A,A×B,B×A\) and required rectangles \(A×C,C×A\) are pairwise disjoint, so the probability formula in the proof is correct.

The binomial summation over \(b\) enlarges the range and is a valid upper bound. The small-\(a\) exponential suppression is stronger than the \(O((\ln n)^2)\) logarithm of the prefactor. In the large-\(a\) range, the exponent differs from \(-\lambda_a\) by at most \(1+o(1)\); the central-index and Chernoff argument for \(\sum_{a>A_n}\pi_{\lambda_a}(a)\) is valid. No fatal gap was found in this first-moment proof.

## 6. Numerical reproducibility and code correction

experiments/expected_partition_sum.py now explicitly uses matrix order (c,a,b) and tests the fixed-fibre F1001 expression against the hand formula. The total sum was unchanged by the correction, since all positive triples are summed, but the previous per-triple interpretation was inconsistent.

experiments/large_n_audit_numpy.py provides an optional vectorized audit (requires NumPy and SciPy). It cross-checks exact n=3,4 first moments against the exhaustive enumeration before computing larger n. Representative F1001 values are:

| n | E[X_n] |
|---:|---:|
| 1,000 | 0.040466991 |
| 2,000 | 0.032340597 |
| 5,000 | 0.026380675 |
| 10,000 | 0.021771903 |
| 20,000 | 0.017459042 |
| 30,000 | 0.016048503 |

These are finite numerical values, not a proof of convergence.

## 7. Prior-work status

Schamm (2002), Sections 3.3.5–3.3.6, already gives the general F-partition first-moment framework and an experimental survey of all 16 three-point central-point frames; Appendix 5.1 proves K4. The present proof work therefore does not discover the candidate family. The possible contribution is a rigorous proof for a case treated experimentally in that dissertation, together with a reproducible Lean/Python audit.

The mapping of mask 8/9 to the “No growth”/“Slow growth” cells in Figure 4.1 remains provisional: the text extraction lists the 4×4 labels, and the Java loop iterates masks in row-major bit order, but a direct visual inspection of the figure has not yet been completed. Do not state that the old numerical classification has been corrected until this is resolved.

## 8. Formalization boundary

Lean checks finite frame definitions, bounded-morphism facts and composition, finite quotient statements, exact n=3 labelled counts, the F1001 fibrewise characterization, and the implication from an F0001 bounded morphism to the weaker witness event. It does not formalize the probability spaces, real-valued estimates, dominated-convergence argument, Stirling bounds, or either asymptotic limit.


## 9. Quantitative strengthening of F1001

The Poisson cross-sum lemma can be sharpened from \(S_n=o(1)\) to
\[
S_n=O(1/m_n)=O(1/\ln n).
\]
For the off-diagonal sum, split \(i\geq m_n/2\) and \(i<m_n/2\). On the first range, the summable maximum bounds from (11)–(12) have exponentially small tails in \(m_n\). On the second, \(t_i=n2^{-i}\geq(m_n/3)2^{m_n/2}\); split \(d\leq t_i/2\), where a Poisson lower-tail bound applies, from \(d>t_i/2\), where the second Poisson mean \(t_i2^{-d}\) is tiny. This gives an off-diagonal contribution \(o(1/m_n)\).

For the diagonal, at most two indices have \(r_i\in[1/2,2]\), and each contributes \(O(1/m_n)\). The \(i\geq m_n/2\) noncentral tail is exponentially small; the \(i<m_n/2\) tail has \(r_i\geq 2^{m_n/2}/3\) and is super-exponentially small by a Poisson lower-tail bound.

The remaining middle-tail sum can also be improved from the crude \(O(\ln\ln n/\ln n)\) to \(O(1/\ln n)\): the ratio \(r_{a+1}/r_a<1/2\) permits at most two indices with \(r_a\in[1,4]\), while the factor \(r_a^2e^{ag(r_a)}\) decays exponentially for \(r_a<1\) or \(r_a>4\). The strengthened hand proof now concludes
\[
\mathbb E X_n=O(1/\ln n),\qquad
\Pr(G_n\twoheadrightarrow F_1)=O(1/\ln n).
\]

This is a quantitative upper bound, not an asymptotic equivalent or a lower bound. It is an internal hand proof and remains unformalized in Lean and not externally refereed.


## 10. Quantitative status and latest Lean coverage

The current hand-proof conclusions are:
\[
\Pr(G_n\twoheadrightarrow F_{0001})=O(1/\sqrt{\ln n}),
\qquad
\Pr(G_n\twoheadrightarrow F_{1001})=O(1/\ln n).
\]
These are upper bounds only. No matching lower bounds or asymptotic equivalents are established.

The finite Lean layer now consists of:
- RandomKripke/ExactSmallN.lean: exact labelled n=3 source-frame counts;
- RandomKripke/F1001Characterization.lean: equivalence between an F1001 bounded morphism and the exact fibrewise conditions used in its first-moment summand;
- RandomKripke/F0001Witness.lean: implication from a bounded morphism onto F0001 to the weaker necessary event used in its first-moment upper bound.

The latest head at the time of this audit, c1efeb9418e14505ee287e3093489aa0d5a18cfb, passed CI run [45569425119](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45569425119). The log explicitly records successful builds of all three Lean modules and successful Python finite/numerical audits. None of the asymptotic probability arguments is formalized in Lean.


## 10. Quantitative F0001 bound

The F0001 central Poisson range contains at most two indices, each at least \(A_n+1=\Theta(\ln n)\), and each point mass is \(O(A_n^{-1/2})\). The noncentral terms are bounded by a geometric Chernoff tail, while the small-fibre contribution is exponentially smaller. Thus the current first-moment draft yields
\[
\Pr(G_n\twoheadrightarrow F0001)=O(1/\sqrt{\ln n}).
\]
This is a hand-proof upper bound only, with no matching lower bound or asymptotic equivalent.


## 11. Separate side finding: Goranko Proposition 4.7

The project now contains a finite counterexample to the preservation step used in Goranko (2020), Proposition 4.7. The complete irreflexive three-point frame satisfies \(\eta=\forall x\exists y(Rxy\land\neg Ryy)\). It maps onto the two-point target with relation \(\{(0,0),(0,1),(1,0)\}\) via \(h(0)=h(1)=0,h(2)=1\). The target fails \(\eta\) at point 1. Direct inspection verifies forth, back, and surjectivity. Both frames have two-step reachability.

This is independent of the F0001/F1001 first-moment arguments. It refutes the stated preservation step, and therefore leaves a gap in that proof of Proposition 4.7; it does not alone refute the proposition's final conclusion. The finite statement is in RandomKripke/GorankoEtaCounterexample.lean. The first CI attempt failed at decidability synthesis; the theorem now uses decide, with the corrected module build pending.
