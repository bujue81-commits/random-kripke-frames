# Sharp logarithmic first moment for the chain target

Status: new internal hand proof; not Lean-formalized, externally refereed or novelty-checked. Uses the chain target defined in GORANKO_CHAIN_FRAMES_FIRST_MOMENT.md and RandomKripke/ChainFrames.lean. No claim of a matching logarithmic rate for the probability of existence.

## Fixed-map probabilities

Fix r>=2. The target has central vertex 0 and noncentral edges i -> i+1 for 1<=i<r. Let a_0,...,a_r be positive fibre sizes with sum m. Write S=sum_{i=1}^r a_i and Q=S^2-sum_{i=1}^{r-1}a_i*a_{i+1}. Ordered edges (including loops) in the labelled source are independent fair bits.

For a fixed surjection, let W be the selected necessary event from the previous hand proof. Its probability is exactly

    P(W)=2^(-Q) prod_{i=1}^r (1-2^(-a_i))^a_0.

The full bounded-morphism event B requires, in addition, every source row to hit the central fibre, and each row in fibre i (1<=i<r) to hit fibre i+1. These extra hit rectangles, the selected central-to-noncentral hit rectangles and the forbidden ordered pairs use disjoint coordinates of the fair-bit sample space. They are independent; each hit block of size k contributes 1-2^(-k). Hence

    P(B)=P(W) (1-2^(-a_0))^m
               prod_{i=1}^{r-1}(1-2^(-a_{i+1}))^a_i.

These are exact fixed-map probabilities. Summing over size vectors with multiplicity m!/(a_0!...a_r!) gives E Z_m and E X_m respectively, where Z counts selected witnesses and X counts full surjective bounded morphisms. By Markov, P(X_m>=1)<=E X_m<=E Z_m.

## Theorem

For each fixed r>=2 and L=log_2(m), as m tends to infinity,

    log_2 E Z_m = -(r-1)^2 L^2 + O_r(L log L),
    log_2 E X_m = -(r-1)^2 L^2 + O_r(L log L).

In particular,

    P(X_m>=1) <= 2^{-(r-1)^2 L^2+O_r(L log L)}.

The O notation in the exponent denotes an upper error bounded by a constant (depending on fixed r) times L log L. Neither expectation result implies a matching lower bound on the existence probability.

## Upper bound for the selected first moment

Write q_r=r^2-r+1, b=L-3 log_2 L and C=4r. Assume m is sufficiently large depending on r, so b>0 and C L<=m/2. Split all positive size vectors into three ranges.

1. Large total S>C L. As in the earlier proof Q>=3S^2/4. The total number of maps with given S is at most (mr)^S. For large m, log_2 r<=L, and S> C L>=8L implies 2L-3S/4 <= -S/4. Dropping all hit factors, the sum for this S is <=2^{-S^2/4}. There are at most m possible values of S, so the total is <=2^{L-C^2 L^2/4}. This is negligible compared with the claimed bound.

2. S<=C L and some a_i<b. The central rows must all hit that fibre. Since a_0>=m/2 and 2^(-a_i)>L^3/m, this probability is <=exp(-L^3/2). There are at most (m+1)(mr)^{C L} maps in the range, so its total is <=exp(-L^3/2+O_r(L^2)), also negligible.

3. S<=C L and all a_i>=b. Write a_i=b+d_i, d_i>=0, D=sum d_i. If deg_i is the degree of vertex i in the undirected r-vertex path (1 at endpoints, 2 otherwise), expansion gives

    Q-S L
      = q_r b^2 - r b L
        + sum_i ((2r-deg_i)b-L)d_i
        + (D^2-sum_i d_i*d_{i+1}).

The coefficients of d_i are nonnegative for all sufficiently large L, since 2r-deg_i>=2 for r>=2 and b/L tends to 1. The final quadratic term is nonnegative by the parity bound (or simply by expanding D^2). Thus Q-S L>=q_r b^2-rbL.

For each size vector the multinomial count is <=m^S (choose and order the S noncentral vertices, then divide by the fibre factorials). Dropping hit factors gives a summand <=2^{-(q_r b^2-rbL)}. There are at most (m+1)^r size vectors, contributing O_r(L) to the base-2 log; also

    q_r b^2-rbL = (r-1)^2 L^2 + O_r(L log L).

The sum of the three ranges yields the desired upper bound on E Z_m, hence also on E X_m.

## Lower bound for the full first moment

Choose all r noncentral sizes equal to a=ceil(L), with a_0=m-ra and S=ra. These are positive for large m. For this size vector,

    Q=q_r a^2,
    multinomial = (m)_S/(a!)^r >= (m-S)^S/a^S.

For S<=m/2, its base-2 log is >= S(L-1-log_2 a) = r L^2-O_r(L log L).

For sufficiently large m, a_0>=a and 2^(-a)<=1/m. The required hit blocks in the full formula number r*a_0+m+(r-1)*a <= (r+1)m, and all their sizes are at least a. The product of their hit probabilities is at least (1-1/m)^((r+1)m)>=exp(-2(r+1)) for m>=2, using ln(1-x)>=-2x for 0<=x<=1/2.

Therefore the single size-vector contribution to E X_m is at least

    2^{r L^2-O_r(L log L)} * 2^{-q_r a^2} * exp(-2(r+1))
      = 2^{-(r-1)^2 L^2-O_r(L log L)}.

Together with E X_m<=E Z_m and the upper bound, this proves both expectation statements.

## Existence probability: a weaker lower bound

The same balanced size vector and any one fixed surjective map give

    P(X_m>=1) >= 2^{-q_r ceil(L)^2} exp(-2(r+1))
               = 2^{-q_r L^2-O_r(L)}.

Thus the negative base-2 logarithm of the existence probability, divided by L^2, has liminf at least (r-1)^2 and limsup at most q_r. The two bounds differ. Proving the actual rate requires controlling overlaps between successful maps, not just their expected count.

## Verification obligations

- Verify the full-map event formula directly against exhaustive enumeration for small fixed fibre maps.
- Formalize coordinate-block counting and independence over uniform Bool-valued finite functions, then the exact expectation.
- Formalize the asymptotic proof only after existing Lean modules actually compile.
- Check literature before claiming originality; this sharp rate is a new derivation within this repository, not a priority claim.
