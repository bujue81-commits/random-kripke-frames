# No-singleton-miss forbidden-degree criterion

Status: internal hand proof, not Lean-verified, independently refereed, or novelty-checked. This generalizes FORBIDDEN_DEGREE_CRITERION.md.

## Theorem

Fix a finite target with a universal reflexive center c and r>=1 other vertices. Let A_ij be 1 iff peripheral arrow i->j is absent, q=sum A_ij, and g_i=sum_j(A_ij+A_ji) (loops count twice). Assume:

(H1) No vertex with a universal incoming column has exactly one missing outgoing arrow (among all target vertices).
(H2) Every peripheral g_i>=2.

With fixed independent ordered-edge probability theta in (0,1), including loops, set rho=1-theta, B=1/rho, L=log_B m, b=L-log_B L, d=q-r>=0. If p_m is the probability of a full surjective bounded morphism, then

    log_B p_m = -d*b^2+O_{F,theta}(L).

If d=0, also p_m=O(L^(-r/2)). Thus all such targets have vanishing existence probability. The estimate concerns existence rather than the unrestricted first moment. The previous criterion implies (H1) since then c is the only universal incoming column, and c has no missing arrow. Neither hypothesis is claimed necessary.

## 1. Tiny-fibre exclusion with additional universal columns

Take C=8(r+1)^2, h=ceil(C L), b0=L-3 log_B L. The probability of any entirely absent h-by-h ordered rectangle is <=m^(2h)*rho^(h^2)=B^(2hL-h^2). This includes overlapping row and column sets because the h^2 ordered coordinates are distinct. On the complementary event every pair of labels with fibres of size >=h has an arrow between them, including self-arrows. Call these labels U, and the remaining labels S. U is nonempty for large m.

Suppose some label i has a tiny fibre of size a_i<b0. In particular i belongs to S. Fix the set S and all its small disjoint nonempty fibres. For a vertex x outside these fibres test the following:

- x has no outgoing edge to fibre i;
- x hits every other small fibre by an outgoing edge;
- every small fibre has an incoming edge into x (that is, at least one edge from that fibre to x).

All tested coordinates are mutually disjoint for each outside x, and also between distinct outside x. Each test succeeds with probability

    rho^a_i * prod_{j in S minus {i}}(1-rho^a_j)
             * prod_{j in S}(1-rho^a_j)
    >= rho^a_i * theta^(2|S|-1).

If a successful bounded morphism has these fixed small fibres, any passing x lies in a fibre of label u in U. By forth and the incoming tests, every label in S reaches u; the complete relation on U ensures every label in U reaches u too. Thus u has universal incoming column. By the outgoing tests and forth, u reaches every label in S except possibly i. By the missing hit and back, u cannot reach i. And u reaches all labels in U by completeness. Therefore u has exactly one missing outgoing arrow, contradicting (H1).

Consequently no outside x passes. Since there are m-O(L) outside vertices, the probability is <=exp(-c0*m*rho^a_i)<=exp(-c0*L^3), for fixed c0>0 and sufficiently large m. There are at most 2^(r+1)*(h+1)^(r+1)*m^((r+1)h) choices of S and its small fibres, and at most r+1 choices of i. Union bound yields exp(-Omega(L^3)) plus the absent-rectangle exception. The rectangle exception is negligible compared with B^(-d*b^2+O(L)), as C^2-2C>d. This argument does not condition the independent tests on the rectangle event: the event implication is used before the unconditional union bound. It forces all fibres, in particular all peripheral fibres, to be >=b0 except on the stated negligible existence event.

## 2. Noncritical and critical logarithmic rates

The remainder of sections 2 and 3 in FORBIDDEN_DEGREE_CRITERION.md requires only the peripheral lower bounds from the preceding section and (H2). For completeness:

Q(a)=sum A_ij a_i a_j. For peripheral a_i>=b0, expansion at b0 gives Q>=q*b0^2+2*b0*(T-r*b0), where T=sum a_i, by (H2) and nonnegative quadratic remainder. The multinomial is <=m^T; hence T>C L contributes at most B^(-d L^2-Omega(L^2)) even after at most m^r vectors. For T<=C L, the central size is >=m/2. The factorial estimate gives log_B(multinomial)<=b*T+O(L). Derivatives of Q(x)-b*sum x_i are >=2b0-b>0 throughout x_i>=b0. Clipping sizes below b upward to b shows Q-b*T>=d*b^2-O(L)*sum_i(b-a_i)_+. Central hit penalties at small sizes are <=-L*B^(b-a_i)/(2 ln B) in base-B logarithm; these absorb the linear deficits since K*t-B^t/(2 ln B) is bounded above. Summing O(L^r) main vectors proves the upper rate.

For the lower rate use balanced peripheral sizes a=ceil b, with central remainder. Count N=(m)_(ra)/(a!)^r, log_B N=r*b^2+O(L). Q=q*a^2. Each full-map success probability is >=c_m*rho^Q, c_m=exp(-2(r+1)L), by disjoint hit blocks of size >=a. If k_i vertices from fibre i are outside a second balanced map's peripheral support, the forbidden rectangle ij loses at least a*(k_i+k_j)/2 coordinates. Summing gives >=a*sum k_i by (H2), so the joint probability is <=rho^(Q+a*k), k=sum k_i. For fixed first map there are at most binom(ra,k)binom(m-ra,k)r^(ra) second maps with support difference k. Retain k! in binom(m-ra,k)<=m^k/k!, and sum the exponential series. The sum of joint probabilities is <=rho^Q*(2r)^(ra)*exp(L), since m*rho^a<=L. Cauchy-Schwarz gives p_m>=c_m^2*N*rho^Q*(2r)^(-ra)*exp(-L), proving the lower rate including d=0.

## 3. Critical case with universal columns

If d=0, then q=r and sum_i g_i=2q=2r, so (H2) forces all g_i=2. Form an undirected multigraph with one edge for each missing ordered arrow, retaining a loop for i=j and retaining both parallel edges if both directions are missing. Every vertex has degree two (loops contribute two). Each connected component is a single loop, two parallel edges, or a simple cycle. To see the last claim, if a component has neither loops nor parallel edges, it is a finite connected simple 2-regular graph; follow edges without immediate reversal until a vertex repeats. The resulting cycle exhausts the component since its vertices already have degree two. Orient each component cyclically, including the parallel-edge component with opposite directions. This produces a permutation sigma of the peripheral labels, with one outgoing and one incoming edge per label, satisfying

    Q(a)=sum_i a_i*a_sigma(i).

This equality depends only on the symmetric quadratic form Q, not on the original directed orientation. In particular the original A need not be a permutation matrix.

On main sizes a_i>=b0 and T<=CL, let lambda_j=m*rho^a_j. The selected first-moment summand is at most

    exp(T*sum_j rho^a_j) * prod_i pi_{lambda_sigma(i)}(a_i),

where pi_lambda(k)=exp(-lambda)*lambda^k/k!, using the permutation property. The prefactor is 1+o(1) uniformly. By Stirling, pi_{t k}(k)<=K*k^(-1/2)*exp(-k*(t-1-ln t)). If any normalized mean is outside [1/2,2], the O(L^r) terms total exp(-Omega(L)). Otherwise a_i in [L/2,CL] imply lambda_j in [L/4,2CL], and hence every a_j=b+O(1). There are only O(1) vectors and each product is O(L^(-r/2)). Add negligible tails and tiny-fibre exceptions. This proves the critical upper bound.

## 4. Four-point census

Of the 17 previously unresolved canonical peripheral matrices, exactly eight meet the new criterion (all have an additional universal incoming column). Their d values are

    001001001  3
    001011001  2
    001101001  2
    001111001  1
    011010011  1
    011010110  1
    100110101  1
    100110111  0

The seven positive-d types have matching logarithmic rates; the last has O(L^(-3/2)) critical upper bound (its original forbidden arrows form an acyclic orientation of the triangle, not a permutation). By the earlier smaller-quotient census all eight are minimal vanishing targets, conditional on the hand probability theorems. Four-point count: 90 zero-limit types, five one-limit types, nine unresolved, total 104. Labelled count: 442 zero, 19 one, 51 unresolved. At least 20 minimal four-point types (including the previous 12). No complete classification or literature-priority claim.

Remaining canonical types: 001011011,001011101,001101011,001111011,011010111,011011101,100111111,101011011,101110111. They fail at least one of (H1),(H2); this is not evidence of either limit. No new Lean code; recent CI unavailable.
