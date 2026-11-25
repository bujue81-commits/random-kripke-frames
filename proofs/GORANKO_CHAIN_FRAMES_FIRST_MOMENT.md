# Chain-frame first-moment bound (hand proof)

Status: internal mathematical argument, not Lean-formalized or refereed. Bibliographic priority is unverified. The statement uses the target orientation encoded in the numerical audit; check the original paper's exact frame definition before identifying this with every claim of Proposition 4.7.

## Statement

Fix an integer r >= 2. Let F_r have vertices 0,1,...,r, with 0 central (both directions to every vertex, including itself) and with the only edges between noncentral vertices being i -> i+1 for 1 <= i < r. Let G_m be the labelled directed frame with every ordered edge, including loops, independently present with probability 1/2. Then there are c_r>0 and M_r such that for m>=M_r,

    Pr(G_m admits a surjective bounded morphism onto F_r)
      <= exp(-c_r (ln m)^2).

## Necessary event and exact first moment

For an ordered partition (A_0,...,A_r) into nonempty fibres put a_i=|A_i|, S=sum_{i=1}^r a_i, a_0=m-S. Forth requires the absence of every noncentral ordered edge except those in A_i x A_{i+1}. Back requires every x in A_0 to have an edge to each A_i for i>=1.

The corresponding edge sets are disjoint: forbidden noncentral rectangles have sources outside A_0; the hit events have sources in A_0 and distinct destination fibres. Thus the probability of this weaker event is exactly

    2^{-Q} prod_{i=1}^r (1-2^{-a_i})^{m-S},
    Q = S^2 - sum_{i=1}^{r-1} a_i a_{i+1}.

Let Z count ordered partitions satisfying this event. By linearity,

    E Z = sum_{a_0+...+a_r=m, all a_i>=1}
          m!/(a_0!...a_r!) * 2^{-Q}
          * prod_{i=1}^r (1-2^{-a_i})^{a_0}.

Existence of a surjective bounded morphism implies Z>=1, hence its probability is <= E Z by Markov. No independence between different partitions is required. This is the sum computed by experiments/goranko_chain_first_moment.py.

## Uniform bound on forbidden edges

Let U be the sum of odd-index noncentral fibre sizes and V the sum of even-index sizes. Each adjacent product occurs among the products in U V, with all products nonnegative. Consequently

    sum_{i=1}^{r-1} a_i a_{i+1} <= U V <= (U+V)^2/4 = S^2/4,

so Q >= 3 S^2/4.

For fixed S the number of ordered partitions is at most binom(m,S) r^S <= (mr)^S: choose the noncentral vertices and assign them one of r labels; allowing empty fibres only increases this upper bound.

## Small S

Write L=log_2 m and T=3rL/4. For S<=T, some a_i<=S/r<=3L/4. For sufficiently large m (depending on fixed r), T<=m/2, so

    (1-2^{-a_i})^{m-S}
      <= exp(-(m-S)2^{-a_i})
      <= exp(-m^{1/4}/2).

Dropping other factors, the total expectation from these partitions is at most

    (m+1)(mr)^T exp(-m^{1/4}/2).

Its natural logarithm is at most ln(m+1)+T ln(mr)-m^{1/4}/2 = -m^{1/4}/2+O_r((ln m)^2). In particular it is <= -L^2 for all sufficiently large m.

## Large S

For S>T, discard all hit factors and use Q>=3S^2/4. The contribution for each S is at most

    (mr)^S 2^{-3S^2/4}
      = 2^{S(L+log_2 r-3S/4)}.

Since r>=2, T>=3L/2. For sufficiently large m, log_2 r<=L/16; hence 3S/4>9L/8 and

    L+log_2 r-3S/4 <= -L/16.

Thus each term is <= 2^{-SL/16} <= 2^{-3L^2/32}. Summing at most m terms gives a large-S contribution <= 2^{L-3L^2/32} <= 2^{-3L^2/64} for L>=64/3.

## Conclusion

Combining the two ranges gives

    E Z <= exp(-L^2) + 2^{-3L^2/64}
         <= exp(-c (ln m)^2)

for all sufficiently large m depending on r; for example c=3/(128 ln 2) works after increasing M_r. This proves the stated upper bound. The threshold depends on r; no claim uniform in growing r is made.

The argument does not use preservation of eta under bounded-morphic images. It proves a probability bound, not an entire modal-logic classification or independence theorem. A characteristic-formula consequence additionally requires the appropriate Jankov-Fine theorem and language/frame convention. The r=1 case is not covered by this estimate.

## Formalization milestones

1. Define the target family and necessary event in Lean.
2. Prove bounded morphisms imply the event.
3. Formalize the adjacent-product bound using odd/even fibre sums.
4. Establish finite probability space and the expectation formula.
5. Formalize both asymptotic ranges and the final Markov bound.

The numerical checks are corroboration only, not proofs of these milestones.
