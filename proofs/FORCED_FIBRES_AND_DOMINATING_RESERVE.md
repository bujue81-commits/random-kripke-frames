# Forced fibres and dominating reserves: three more four-point limits

Internal hand proof. No Lean verification, independent peer review, or bibliographic priority claim. Fixed independent ordered-edge probability theta in (0,1), including loops. Write rho=1-theta, B=1/rho, L=log_B m.

## Results

Of the five previously unresolved canonical peripheral matrices, the following are resolved:

- 001011101: p_m=O(L^(-1/2)).
- 001101011: p_m=O((L log L)^(-1/2)).
- 100111111: p_m tends to one.

The first two are additional minimal vanishing targets by the earlier quotient census. The upper bounds need not be sharp. The last is an instance of a general positive family, proved below. The two remaining unresolved matrices are 011010111 and 011011101.

## 1. A forced-fibre upper bound

Relabel the two negative targets as c,A,B,Z with c universal, both c and Z universal incoming, and Z missing only its outgoing arrow to A. For 001011101 use A=old peripheral 2, B=old peripheral 1, Z=old peripheral 3; for 001101011 use A=old 1, B=old 2, Z=old 3. The missing outgoing destinations are:

    canonical      A     B     Z
    001011101      B     A,B   A
    001101011      A,B   B     A

The labels c and Z both hit B; A and B both miss B. Thus for any full successful map, the B-fibre is independent (all internal ordered edges absent), and the A-fibre is exactly the set of vertices outside B that have no outgoing edge into B. In particular after fixing B there is no arbitrary choice of A. Other necessary constraints differ between the two targets.

Write a=|A|, b=|B|, z=|Z|. The same rectangle and witness argument as section 1 of NO_SINGLETON_MISS_DEGREE_CRITERION.md applies to any particular label i for which no universal-incoming label misses exactly i. It does not require the global degree hypothesis for this restricted conclusion. Here i=B has that property. Taking h=ceil(128 L), the probability of existence with b<b0=L-3 log_B L is bounded by

    B^(2hL-h^2)+exp(-Omega(L^3)).

Indeed on the no-empty-h-rectangle event, large labels form a complete relation. Enumerate all small fibres, and test an outside vertex missing exactly B among small fibres and receiving a hit from each of them. It would require a universal-incoming label missing exactly B, impossible. For fixed small fibres the independent tests over outside vertices succeed with probability >=rho^b*theta^7 (or a larger constant), yielding the bound after union over B^O(L^2) choices. The argument uses unconditional tests and an event implication, not independence conditional on the rectangle event.

Also b<h on the no-empty-rectangle event since B is independent. In the second target A is independent too, so a<h there. All rectangle and tiny-b errors are negligible relative to the claimed bounds.

For a fixed B of size b, let q_b=rho^b, lambda=m q_b. Its internal forbidden coordinates have probability rho^(b^2). The A-fibre forced by B is formed by independent tests on rows outside B with probability q_b; these tests are independent of internal B coordinates. Thus its size has distribution Bin(m-b,q_b) conditional on B independence.

### 1a. Target 001011101

The B-to-A rectangle must be entirely absent as well. Conditional on the tests defining A, these ordered coordinates are fresh, so the additional probability is rho^(ab)=q_b^a. Dropping all other conditions, including nonemptiness of A, the expected number of candidate B-sets of size b is at most

    binom(m,b) rho^(b^2) (1-q_b+q_b^2)^(m-b).

This is the binomial theorem after weighting the forced A-set by q_b^a. For b0<=b<h, q_b<=L^3/m. The expression is bounded by

    (lambda^b/b!) exp(-(m-b)*q_b*(1-q_b))
       <= exp(O(L^6/m)) pi_lambda(b),

where pi_l(k)=exp(-l)l^k/k!, using b=O(L). For the normalized means t_b=lambda/b, the successive ratio is rho*b/(b+1)<rho. Thus O_theta(1) indices have t_b in [1/2,2], and Stirling bounds each mass by O(L^(-1/2)) there. All other O(L) indices contribute exp(-Omega(L)) since t-1-ln t has positive lower bound outside that interval and b>=L/2. Summing and adding negligible exceptions proves p_m=O(L^(-1/2)).

### 1b. Target 001101011

Here A is independent, and every B-row must hit A. For given B and the forced A-set, these two conditions use disjoint fresh blocks A x A and B x A, also disjoint from the previous B x B and outside-B-to-B tests. For a,b>=1 the expected candidate count is bounded by

    binom(m,b) rho^(b^2) binom(m-b,a) q_b^a
        (1-q_b)^(m-b-a) rho^(a^2) (1-rho^a)^b.

No separate choice of Z or c is counted. Any successful map provides at least one such candidate B. On b0<=b<h, a<h the displayed expression is at most

    exp(O(L^4/m)) pi_lambda(b)
        * (lambda*rho^a)^a/a! * exp(-b*rho^a).

Write t=lambda/b. The last two factors equal t^a*pi_{b*rho^a}(a). The prefactor tends uniformly to 1.

First discard a>K log_B L for fixed K=8. Since lambda<=L^3, lambda^a*rho^(a^2)/a! <= B^(3a log_B L-a^2)<=B^(-a^2/2) for these a, and the other factors are <=1 apart from the uniform prefactor. Summing over O(L^2) pairs yields o((L log L)^(-1/2)).

For remaining a<=K log_B L, the last factors are at most exp(O((ln L)^2)) uniformly (use lambda<=L^3 and drop exp(-b*rho^a)). If |t-1|>L^(-1/4), the rate function I(t)=t-1-ln t is >=c L^(-1/2) for a fixed c>0 and sufficiently large L. This follows from its second derivative 1/t^2 on [1/2,2] and positive minima outside that interval. Thus pi_lambda(b)<=O(exp(-c' sqrt(L))) by Stirling since b>=L/2. Even after O(L log L) pairs these terms are negligible.

In the remaining range |t-1|<=L^(-1/4), the decreasing geometric ratio of t_b implies at most one integer b for large L. Also t^a<=exp(O(log L/L^(1/4)))<=2, and pi_lambda(b)=O(L^(-1/2)). Finally, uniformly as b->infinity,

    sum_{a>=1} pi_{b*rho^a}(a)=O((log b)^(-1/2)).

To see this, put H=log_B b. For a<=H/2, the mean is >=sqrt(b), so the Poisson lower-tail Chernoff bound gives exp(-Omega(sqrt(b))) per term for sufficiently large b. For a>H/2, the normalized means b*rho^a/a decrease by factor <rho, so O(1) indices in [1/2,2] contribute O(H^(-1/2)) by Stirling. All others are bounded by O(exp(-c a)) via the same rate function, whose geometric sum is negligible. Since b is of order L, this proves the claimed O((L log L)^(-1/2)) bound after summing and adding the exceptional events.

## 2. A dominating reserve for a one-row forbidden star

For any fixed k>=1 let F_k have labels c,Z,A_1,...,A_k. All arrows are present except the k arrows Z->A_i. (All loops are present.) We show p_m(F_k)->1, which covers 100111111 at k=2.

The earlier complete-core signature construction does not apply for k>=2: among the universal incoming labels only c and Z realize signatures, and these give only the all-hit and all-miss patterns on the k exceptional destinations. Instead choose a moderately small universally hit fibre Z, and make the other k fibres sufficiently large that accidental misses outside Z are rare.

### 2a. A small out-dominating destination set

Take a deterministic reserve W of floor(m/2) vertices and t=ceil(L-(3/2)log_B L). We claim that with probability 1-o(1) there is a t-subset D of W hit by every source row (including rows in D). This choice is measurable using only edges ending in W.

Let X count such t-subsets, q=rho^t, N=|W|, and P0=(1-q)^m the success probability of each fixed D. Then E[X]=binom(N,t)P0>0. For two t-subsets with intersection size j, the probability of both hits in each row is 1-2q+rho^(2t-j), so the ratio of their joint success probability to P0^2 is

    [1+(rho^(2t-j)-q^2)/(1-q)^2]^m
        <=exp(4m*rho^(2t-j))

for large m. The formula follows from independence of rows and inclusion-exclusion for the two misses; it includes loops. For j<=t/2, the right side is 1+o(1) uniformly, since m*rho^(3t/2)<=m^(-1/2)*L^(9/4)->0. For j>t/2, the ratio is <=exp(4m q)<=exp(4L^(3/2)). For two independently uniform t-subsets of W, the probability of intersection >t/2 is bounded by

    2^t*(t/(N-t))^ceil(t/2)=exp(-Omega(L^2)).

Indeed fix the first set and union bound over subsets of ceil(t/2) of it; the probability any such subset lies in the second is (t)_ell/(N)_ell <=(t/(N-t))^ell. Therefore E[X^2]/E[X]^2<=1+o(1), with the high-overlap contribution negligible. Cauchy-Schwarz gives P(X>0)>=E[X]^2/E[X^2]=1-o(1). The event and a deterministic selected successful D depend only on edges ending in W.

### 2b. Construct all fibres using fresh edges

Set Z-fibre=D. Conditional on the edge information ending in W with successful D, expose the coordinates D x ([m] minus W), fresh under this history. Let M be the outside-W vertices receiving no outgoing edge from any row in D. Then |M| is Bin(m-N,q), because the column tests are independent. Its mean is of order L^(3/2), since rho*L^(3/2)<=m*q<=L^(3/2). Chernoff gives |M|>=k*ceil(2L) with probability tending to one. Choose disjoint A_i-fibres of size ceil(2L) deterministically from M. Assign all remaining vertices to c, except D. Thus all required forbidden blocks D x A_i are absent.

Every row hits D by the initial selection. Conditional on all history so far, the edges from rows outside D ending outside W are independent original Bernoulli bits: first-stage tests ended inside W; second-stage tests began in D; the chosen A_i and c-fibre depend only on those tests. Thus every row outside D hits every A_i except with probability at most mk*rho^ceil(2L)<=k/m. The outside-W portion of c has size m-N-k*ceil(2L)>=m/3 eventually. All rows outside D hit it except with probability at most m*rho^(m/3).

For rows in D, any outgoing edge to outside W must end in the c-fibre, because every A_i lies in M. The probability some D-row has no outgoing edge to outside W, conditional on the first-stage selection, is <=t*rho^(m-N), irrespective of the later choices. Hence all D-rows hit c with probability 1-o(1). All fibres are nonempty. Together with the hit to D and the forbidden-block condition, the exact successor-image equalities hold. This proves a.a.s. surjective bounded morphism onto F_k for every fixed k.

This argument uses a dominating destination set of size L-(3/2)log_B L, not an assertion that a deterministic such set already dominates. The second moment is essential. No exponential failure rate for F_k is claimed.

## 3. Updated classification

The previous census had 90 zero, 9 one, 5 unresolved. Adding these results gives 92 zero, 10 one, 2 unresolved of the 104 central four-point isomorphism types. Two new minimal zero types yield at least 22 minimal four-point types. The remaining codes 011010111 and 011011101 are not settled here. No full classification of arbitrary modal formulas or originality claim.
