# Referee-style internal audit: Theorem 2

26 November 2026. This is a same-assistant internal proof reconstruction and finite combinatorial audit, not independent refereeing or Lean verification. Reviewed the general criterion and its unified-manuscript presentation at checkpoint b37759d. No new probability theorem is claimed; the aim is to make the quantifiers and bounds explicit and to identify any actual obstruction.

## 1. Statement and quantifiers

Fix r>=1, a central target F with r peripheral labels, and a fixed theta in (0,1), including loops in the random source. Put rho=1-theta, B=1/rho, L=log_B m, b=L-log_B L. All constants below may depend on F and theta, not m. A_ij is the indicator of a missing peripheral arrow, q=sum A_ij, g_i=sum_j(A_ij+A_ji), d=q-r.

H1: no universally incoming label has exactly one missing outgoing arrow. H2: g_i>=2 for all peripherals. Since sum_i g_i=2q, d>=0. The claim is log_B p_m=-d b^2+O(L) and, at d=0, p_m=O(L^(-r/2)). In particular the O(L) two-sided logarithmic error alone does NOT show decay when d=0; the separate critical upper bound is essential.

For d>0 an equivalent expression is log_B p_m=-d L^2+2d L log_B L+O(L), since (log_B L)^2=o(L). This is a two-term logarithmic estimate, not a sharp multiplicative asymptotic.

## 2. Tiny-fibre exclusion: unconditional union bound

Choose C=8(r+1)^2, h=ceil(C L), b0=L-3log_B L. In the rare-event bound, the exceptional probability must be negligible compared with the claimed rate, not merely o(1). For the empty h-by-h rectangle it is at most B^(2hL-h^2)=B^(-(C^2-2C)L^2+O(L)). Since d<=r^2-r and C^2-2C>d, this is B^(-d L^2-Omega(L^2)). Coordinates remain distinct even when the row and column sets overlap, since edges are ordered and include loops.

On the complement of this exception, all labels with fibres of size >=h form a complete reflexive core U; it is nonempty for sufficiently large m. Fix the small labels S and their disjoint nonempty fibres. If the fibre of i in S has size <b0, test an outside vertex x for absence of all edges from x to i, a hit from x to each other small fibre, and an incoming hit from every small fibre to x. The coordinates across all tests at distinct x are disjoint. For each x the pass probability is at least rho^a_i theta^(2|S|-1), and there are m-O(L) candidates. Under a successful map any passing x would lie over a label u in U with universal incoming column, and outgoing edges to every label except i. Forth gives the positive arrows, back rules out u->i. This violates H1.

Thus existence with a tiny fibre, outside the rectangle exception, implies absence of all passing x for some fixed configuration. The probability of that absence is <=exp(-c L^3), since m rho^a_i>L^3. Union over at most 2^(r+1)(h+1)^(r+1)m^((r+1)h)(r+1)=B^O(L^2) choices preserves exp(-Omega(L^3)). This does not condition independent tests on the no-empty-rectangle event. The two exceptional terms are negligible relative to B^(-d b^2+O(L)) and to every negative power of L. H2 has not been used in this lemma.

## 3. Upper logarithmic rate

For fixed peripheral sizes a_i>=b0 let T=sum a_i, a_c=m-T>0, and Q(a)=sum A_ij a_i a_j. Each absent rectangle consists of disjoint ordered coordinates. The exact success probability for a fixed labelled partition is rho^Q times a product of required row-to-fibre hit probabilities; those hit blocks are disjoint from forbidden rectangles. Retaining only the center-to-peripheral hit blocks gives an upper bound. There are (m)_T/prod_i a_i! labelled partitions, where (m)_T is the falling factorial.

First handle T>CL without requiring the central fibre to be large. Writing a_i=b0+z_i gives

    Q(a)=q b0^2 + b0 sum_i g_i z_i + sum_ij A_ij z_i z_j
         >=q b0^2+2b0(T-rb0).

Using the multinomial bound m^T, the log_B expected count at this vector is at most

    -q b0^2+r b0 L-(2b0-L)(T-rb0).

Here the first two terms are -d L^2+O(L log L), and 2b0-L>=L/2 for large m. For T>CL, T-rb0>=(C-r)L, so the sum over at most m^r vectors is B^(-d L^2-Omega(L^2)), as asserted. This controls even a nearly empty central fibre.

On the main range b0<=a_i, T<=CL, all a_i/L are in [1/2,C] eventually and a_c>=m/2. Thus ln a_i=ln L+O(1) uniformly and the factorial lower bound gives log_B multinomial <=b T+O(L). Let P(x)=Q(x)-b sum_i x_i. On the region x_i>=b0, the derivative in coordinate i is sum_j(A_ij+A_ji)x_j-b>=2b0-b>0. Clip a upward coordinatewise to a'_i=max(a_i,b). Then P(a')>=P(b,...,b)=d b^2. On each clipping segment all coordinates are <=(C+1)L, so each derivative has upper bound 2r(C+1)L, uniform in the sizes. Integrating along these segments gives

    P(a)>=d b^2-K L sum_i delta_i,
    delta_i=max(b-a_i,0), K=2r(C+1).

For a_i<b, m rho^a_i = L B^delta_i. The log_B center-to-i hit factor is at most -a_c rho^a_i/ln B <=-L B^delta_i/(2ln B), using ln(1-x)<=-x. Retain only these penalties and combine with the clipping estimate. Since K t-B^t/(2ln B) is bounded above on t>=0, the total log_B count at each main size vector is <=-d b^2+O(L), uniformly. There are O(L^r) vectors. Taking the logarithm of the sum adds O(log L), absorbed into O(L). Markov, followed by the exceptional-event bounds above, proves the desired upper bound. No bound on the unrestricted first moment is asserted.

## 4. Balanced second moment: lower logarithmic rate

Let a=ceil(b) and t=r a; the center is the remaining m-t vertices. For large m all fibres are nonempty and the center has size >=a. Let Y be the number of successful labelled maps with these fixed sizes. The number of candidate maps is N=(m)_t/(a!)^r. Since t=O(L), (m)_t=m^t exp(O(t^2/m)), and Stirling gives

    log_B N = r a (L-log_B a)+O(L) = r b^2+O(L).

The number of forbidden ordered coordinates is Q=q a^2. Every required row-hit block has length >=a and hence miss probability <=rho^a<=L/m. There are at most (r+1)m such blocks. For large m all miss probabilities <=1/2, so ln(1-x)>=-2x and independence gives

    Pr(f succeeds)>=rho^Q exp(-2(r+1)L)=c_m rho^Q.

For two balanced maps f,g, let k_i be the number of vertices of peripheral f-fibre i outside g's peripheral support, and k=sum_i k_i. The forbidden rectangle i->j of f loses

    a^2-(a-k_i)(a-k_j)
      =a(k_i+k_j)-k_i k_j >= a(k_i+k_j)/2

coordinates when restricted to the second support, because 0<=k_i,k_j<=a implies 2k_i k_j<=a(k_i+k_j). This also applies to loops i=j. These losses occur in disjoint f rectangles and cannot belong to the g forbidden coordinates. Summing over missing arrows gives loss >=(a/2)sum_i g_i k_i>=a k. As both forbidden sets have size Q, their union has size >=Q+a k. Thus joint success is at most rho^(Q+a k), independently of the hit conditions.

For a fixed f and k, the second support is obtained by removing k of its t vertices and adding k from outside, and at most r^t peripheral labellings realize that support (ignoring size constraints only increases the count). Therefore

    sum_g Pr(f and g succeed)
      <= rho^Q r^t sum_(k=0)^t binom(t,k) binom(m-t,k) rho^(ak)
      <= rho^Q (2r)^t sum_(k>=0) (m rho^a)^k/k!
      <= rho^Q (2r)^t exp(L).

Here retaining the factorial k! is essential; replacing it by 1 would yield a much weaker bound. It follows E[Y]>=c_m N rho^Q and E[Y^2]<=N rho^Q (2r)^t exp(L). By Cauchy-Schwarz,

    p_m>=Pr(Y>0)>= (E[Y])^2/E[Y^2]
         >=c_m^2 N rho^Q (2r)^(-t) exp(-L).

Its base-B logarithm is >= r b^2-q a^2-O(L)=-d b^2-O(L), since a=b+O(1). The bound is strictly positive for sufficiently large m; thus the logarithm in the theorem is well-defined. The proof allows d=0 but in that case only supplies an exponential-in-L lower bound. It is not a matching lower bound for the critical polynomial upper estimate.

## 5. Critical case: degree-two undirected multigraph

If q=r then the total degree 2r and H2 force every g_i=2. A useful observation is that H1 is then automatic: a peripheral label with zero missing incoming arrows must have two missing outgoing arrows, not one. The central label has zero missing outgoing arrows.

One must not conclude that the original A is a permutation matrix. An acyclic orientation of a triangle is a counterexample (for example the missing-edge matrix of peripheral encoding 100110111). What is true is the symmetric quadratic identity. Interpret missing ordered arrows as undirected multiedges, retaining loops and both opposite arrows as parallel edges. Every component has degree two and hence is a loop, double edge, or simple cycle. Reorient each component cyclically to produce one outgoing and one incoming edge at each vertex. This gives a permutation sigma with the same loop counts and unordered off-diagonal multiplicities, so for all real vectors x

    Q(x)=sum_i x_i x_sigma(i).

The permutation is a counting device for Q only; it need not preserve the original target's missing-arrow relation.

For main sizes use the exact central-hit upper bound and the multinomial estimate:

    (m)_T/prod_i a_i! * rho^Q * prod_j (1-rho^a_j)^(m-T)
      <= exp(T sum_j rho^a_j) prod_i pi_(lambda_sigma(i))(a_i),

where lambda_j=m rho^a_j and pi_lambda(k)=exp(-lambda)lambda^k/k!. To verify: (m)_T<=m^T, rho^Q=prod_i (rho^a_sigma(i))^a_i, the hit product is <=exp(-(m-T)sum_j rho^a_j), and sum_i lambda_sigma(i)=sum_j lambda_j. The prefactor is 1+o(1) uniformly since T<=CL and rho^a_j<=L^3/m.

Stirling bounds each Poisson mass by K a_i^(-1/2) exp(-a_i [x-1-ln x]), x=lambda_sigma(i)/a_i. If any x is outside [1/2,2], the corresponding rate is bounded below by min(ln 2-1/2,1-ln 2)>0. Other Poisson masses are <=1. Since a_i>=L/2, the O(L^r) such vectors contribute exp(-Omega(L)), after absorbing the polynomial factor. Otherwise every lambda_j is in [L/4,2CL] by bijectivity of sigma. Taking logarithms gives a_j=L-log_B L+O(1)=b+O(1), uniformly for all j. Hence only O_{F,theta}(1) integer size vectors remain, and their products are O(L^(-r/2)). All discarded exceptions decay faster. This supplies the separate vanishing claim at d=0.

## 6. Independent finite combinatorial checks

Actual JS computation enumerated all missing-arrow matrices with 1,2,3,4 peripheral vertices, respectively 2,16,512,65536 (66066 total). Counts satisfying both hypotheses were 1,7,331,53457. Critical matrices with q=r and H2 numbered 1,2,12,90. Every one had H1 and an explicit permutation with identical diagonal and unordered off-diagonal multiplicities. Of the critical matrices, 0,0,6,66 were NOT already permutation matrices. Tested the quadratic identity for every a in {1,2,3}^r (7635 checks); all passed.

For every missing-arrow matrix with r<=3 and H2, for balanced sizes a=1..4 and every k_i in [0,a], evaluated the individual rectangle loss inequality, the total degree-loss bound, and the nonnegative quadratic expansion lower bound at b0=1 (by homogeneity). 74,536 size/overlap configurations and 391,526 individual forbidden rectangle inequalities passed. The general inequalities are analytic; finite enumeration is corroboration, not proof of arbitrary r.

Re-read the actual 104-row classification CSV and independently evaluated H1/H2 on every canonical encoding. 69 canonical classes (331 labelled peripheral matrices) satisfy the criterion directly, all recorded as vanishing. Of these, 20 are minimal vanishing types, precisely the 20 assigned to the degree proof in the paper's precedence-ordered classifier. The two critical minimal four-point encodings are 100110111 and 101110011. The remaining 49 degree-covered canonical types already inherit a smaller vanishing quotient; do not add these to the 70 inherited cases in the disjoint census. The reproduction script experiments/degree_criterion_audit.py is committed; equivalent JS executed, Python not yet executed in CI.

## 7. Assessment

No fatal gap identified in this reconstruction. The most delicate points are now explicit: negligible exceptional events at the rare-event scale, clipping on a uniformly bounded size box, the factorial in the second-moment sum, and cyclic reorientation only of the undirected quadratic form. None of these finite tests establishes the limit theorem without the mathematical proof above. No claim of independent peer review, Lean compilation, priority, or a submission-ready PDF. The original theorem and all counts are unchanged.
