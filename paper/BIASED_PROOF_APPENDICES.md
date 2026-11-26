# Technical appendices to Bounded-Morphic Images of Random Kripke Frames

Companion to [the unified manuscript](MANUSCRIPT_BIASED.md), version 0.4. Internal hand proofs, not independently refereed or Lean-verified. The random source, fixed bias, central target and notation are those of the main text. In these appendices all logarithms written ln are natural; B=1/rho and L=log_B m. Each Appendix A–D is a proof component, not a separate research report. Appendix A establishes the necessary-witness formulas, the uniform vanishing threshold, and a triple second moment. Appendix B derives the fixed-phase theorem, with an additional pair second moment. Appendix C resolves the remaining phase coverage question. Appendix D treats the second exceptional frame. Earlier research logs remain archived separately.

## Appendix A. The target 011010111: witness formulas, vanishing and a second moment

Let F have labels C,A,Z,M and only missing arrows A->A, Z->A, Z->M. Write rho_*=(3 sqrt(3)-5)/4. We prove p_m->0 at rho<=rho_* and limsup p_m=1 at rho>rho_*. The latter direction will also serve as the basis for the stronger phase theorem.

### A.0. Deterministic reduction

For a successful surjective bounded morphism, A is independent, and the set of rows outside A missing A is exactly Z. Every row hits Z. For fixed disjoint nonempty A,Z, put

    M0={y outside A union Z: no row in Z has an edge to y},
    C0=[m] minus (A union Z union M0).

Then The actual M-fibre is a nonempty subset of M0, and every row outside Z must hit M0. In particular M0 nonempty is necessary. These conditions give a necessary witness depending on the pair A,Z, with Z uniquely determined by A.

A sufficient witness is obtained by using M=M0 and C=C0: additionally require C0 nonempty and every row to hit C0. Then all four labels have exactly the successor images dictated by the missing arrows. Any row in Z misses A and M0, every other row except A hits A, and A misses A by independence. Every non-Z row hits M, and all rows hit Z,C0. This is exactly a surjective bounded morphism.

The necessary witness does not automatically give the sufficient witness: enlarging the actual M-fibre to M0 might remove some of the original C successors. We therefore keep distinct counts Y_necess and Y_suff, for which

    P(Y_suff>0)<=p_m<=P(Y_necess>0)<=E[Y_necess].

#### Exact expectations

Let a=|A|, z=|Z|, n=m-a-z. For each fixed disjoint A,Z with a,z>=1, n>=1, the probability of independence of A, the exact definition of Z, and every row hitting Z is

    H(a,z)=rho^(a^2+a*z)*(1-rho^a)^n*(1-rho^z)^m.

These events use only columns ending in A or Z. The remaining coordinates Z x ([m] minus (A union Z)) are independent and make |M0| distributed as Bin(n,rho^z). Conditional on M0 and the Z-row column tests, the edges from rows outside Z to M0 are fresh; the probability all these rows hit M is (1-rho^k)^(m-z) when k=|M0|.

Thus the necessary witness expectation is exactly

    E[Y_necess] =
      sum_{a,z>=1,a+z<m} binom(m,a)*binom(m-a,z)*H(a,z)
        * sum_{k=1}^n binom(n,k)*rho^(z*k)*(1-rho^z)^(n-k)
                       *(1-rho^k)^(m-z).

For sufficient witnesses, restrict 1<=k<=n-1 and let c=n-k. In addition to the previous factors multiply by

    (1-rho^c)^(m-z) * J(z,c),

where

    J(z,c)=sum_{j=0}^z (-1)^j binom(z,j)
               *((rho^j-rho^z)/(1-rho^z))^c.

Indeed, all rows outside Z must hit C0, using fresh disjoint row/fibre blocks. For Z rows, conditional on M0, each C0 column has a nonempty vector of edges from Z, independent across those columns. For a specified j rows of Z the probability all j rows miss one such column is (rho^j-rho^z)/(1-rho^z), because the column is required nonempty. Inclusion-exclusion over Z rows failing to hit C0 gives J. Alternatively 1-z*rho^c<=J<=1 by the union bound, since the conditional miss probability for any one row is <=rho^c per column.

There are binom(m,a)binom(m-a,z) pairs. Linearity of expectation suffices; no assumption of independence between pairs is made. These exact formulas are counts of pair witnesses, not counts of arbitrary full maps.

### A.1. Forced sets and reduction to logarithmic sizes

Use Appendix A.0. A is independent including absent loops; Z consists of all rows outside A missing A. Let M0 be all vertices outside A union Z receiving no edge from Z, and C0 its remaining complement outside A union Z. The actual M-fibre is contained in M0. A necessary witness requires all rows to hit Z and all non-Z rows to hit M0. A sufficient witness assigns M=M0 and C=C0 if C0 is nonempty and every row hits C0.

Let a=|A|, z=|Z|, k=|M0|. Set b0=L-3 log_B L and h=ceil(128 L). The tiny-fibre argument in the proof of Theorem 2 of the main text applies to every label of F: the only universally incoming columns are C and Z, whose outgoing missing sets are respectively empty and {A,M}; neither misses exactly one label. This lemma does not use the degree hypothesis when it is used only for tiny-fibre exclusion. Except on an event of probability o(1), every successful map has all fibres >=b0. The absent h-by-h rectangle probability is <=B^(2hL-h^2), and outside it a<h by independence. Hence every successful map, apart from o(1) probability, has b0<=a<h, z>=b0 and k>=b0 (because the actual M-fibre is contained in M0).

For a fixed independent a-set A, revealing A columns makes Z forced, with z~Bin(m-a,rho^a). Conditional on this column history, the coordinates Z x ([m] minus (A union Z)) are fresh; hence k~Bin(m-a-z,rho^z). These two binomial laws do not condition on the Z-hit or M-hit events. The expected count of independent a-sets is N_a=binom(m,a)rho^(a^2)<=(e m rho^a/a)^a. On b0<=a<h we have m rho^a<=L^3, a>=L/2 and a<=129 L eventually, so N_a<=exp(400 L ln L) uniformly for sufficiently large m.

Fix K=1000 and u=L+K log_B L. If a>u, the conditional mean of z is <=L^(-K). Thus the probability z>=b0 conditional on independence is <=(e L^(-K)/ceil(b0))^ceil(b0)=exp(-(K+1+o(1))L ln L), by the union bound over ceil(b0) binomial successes. Multiply by N_a and sum O(L) sizes: the probability of any successful map with a>u is o(1). If z>u, conditional on the A-column history the mean of k is <=L^(-K); the same upper tail bound holds for k>=b0, uniformly over these histories. Multiply again by N_a and sum a in the main range. This also gives o(1). No separate enumeration of large Z is necessary because it is uniquely forced by A. Consequently it suffices for an upper existence bound to count necessary witnesses with

    b0<=a,z<=u,   k>=b0.                 (1)

In particular a,z=L+O(log L), and t=m rho^a/L, s=m rho^z/L are between L^(-K-1) and L^2. Both |ln t| and |ln s| are O(ln L).

### A.2. Uniform first-moment upper bound on the main range

For fixed a,z let n=m-a-z and lambda_a=m rho^a, lambda_z=m rho^z. By the exact necessary-witness formula, the expected count at these sizes with k>=b0 is

    binom(m,a)binom(m-a,z) rho^(a^2+az)
    * (1-rho^a)^n (1-rho^z)^m
    * E[1_(K0>=b0) (1-rho^K0)^(m-z)],

where K0~Bin(n,rho^z). (Here K0 is a random integer, not the fixed constant K.) Bound the first two lines by

    (lambda_a^a/a!)(lambda_a^z/z!)
    * exp(-lambda_a-lambda_z+O(L^4/m)).       (2)

This follows from the multinomial upper bound m^(a+z)/(a!z!), and n rho^a=lambda_a-O(L^4/m). All errors uniform on (1). Stirling, a,z=L+O(log L), |ln t|=O(log L), give the logarithm of (2) at most

    L(2+2 ln t-t-s)+O((ln L)^2).

If s>=1, bound the expectation in the third line by 1. If s<1, use Chernoff with nonnegative parameter v=ln(1/s), since the binomial mean is <=sL:

    P(K0>=b0) <= exp(sL(e^v-1)-v b0)
              <= exp(L(1-s+ln s)+O((ln L)^2)).

This argument works even when the mean is slightly above b0; the exponential upper bound need not be below 1 in that case. Thus the main-size expected count is at most exp(L H(t,s)+O((ln L)^2)), uniformly, with

    H(t,s) = 2+2 ln t-t-s                  if s>=1,
           = 3+2 ln t+ln s-t-2s           if s<=1.

The integer difference d=z-a implies s/t=r=rho^d exactly. Define

    g(r)=ln(27r/(1+2r)^3).

For 0<r<1, the maximum of H(t,rt) over t>0 is g(r), attained uniquely at t=3/(1+2r), with rt<1. Indeed on rt<=1 the expression is 3+3ln t+ln r-(1+2r)t, strictly concave in t, maximized at the stated point. On rt>=1 the expression is 2+2ln t-(1+r)t, decreasing on t>=1/r because 2r<1+r. Its boundary value equals the preceding expression at t=1/r. For r>1, the region rt<=1 is maximized at its boundary (or can be bounded by g(r)); on rt>=1 the unconstrained maximum is 2ln(2/(1+r))<0, attained at t=2/(1+r). For r=1 both maxima are zero. In particular for r>1 the global maximum is 2ln(2/(1+r)), since on rt<=1 the derivative 3/t-(1+2r) is positive when t<=1/r.

The algebraic identity

    (1+2r)^3-27r=(r-1)(8r^2+20r-1)

implies g(r)>0 iff rho_*<r<1 for 0<r<1, with equality at rho_* and 1. Moreover g'(r)=(1-4r)/(r(1+2r)), so g is increasing for r<1/4. For rho<rho_*, d>=1 implies r<=rho and H<=g(rho)<0. For d<=-1, r>=1/rho>1 gives H<=2ln(2/(1+1/rho))<0. All nonzero differences are therefore uniformly exponentially suppressed in L. For rho=rho_*, the same suppression holds for d>=2 and d<=-1; for d=1 the maximum is exactly zero and is treated in Appendix A.4. There are only O((ln L)^2) pairs in (1), so all uniformly negative cases contribute o(1).

### A.3. Equal-size contribution, all fixed biases

If z=a, formula (2) equals (1+o(1))*pi_lambda(a)^2, with lambda=m rho^a and pi_lambda(a)=exp(-lambda)lambda^a/a!. Dropping all conditions on K0 can only increase this bound. The normalized mean lambda/a decreases by a factor strictly less than rho with each increment in a. Thus only O_rho(1) integers have lambda/a in [1/2,2]; their squared Poisson masses are O(1/L) by Stirling. Outside that interval each squared mass is exp(-Omega(L)), since a>=L/2 and the rate x-1-ln x is bounded below by a positive constant. Sum over O(log L) choices of a. This proves that the total diagonal contribution is O(1/L).

Combining Appendices A.1–A.3 proves p_m(F)->0 for every rho<rho_*.

### A.4. Critical boundary rho=rho_*

It remains to handle d=1, z=a+1. Let t_*=3/(1+2rho_*) and s_*=rho_* t_*=0.1339745962...<1. Appendix A.2 shows that H(t,rho_*t) is uniquely maximized at t_* with value 0; it tends to minus infinity at both endpoints t->0 and t->infinity. Thus outside a fixed closed interval [t_*-eta,t_*+eta] chosen inside (0,1/rho_*), H is bounded above by a strictly negative constant. Those pairs contribute o(1) by the uniform estimate. Choose eta small enough that the normalized means below stay away from 0 and 1.

Inside this interval put v=lambda_a/a and w=lambda_z/a=rho_*v. Since a/L->1 uniformly, v is bounded above and below by positive constants and w lies in a compact subinterval of (0,1). Crucially, now keep the M-hit probability, even for k below a. Let p_j=P(K0=j) for K0~Bin(n,rho^z), with n=m-a-z. Uniformly in this interval, p_a=(1+o(1))*pi_lambda_z(a), by the falling factorial estimate n^a/m^a=1+o(1) and binomial-to-Poisson approximation at size a=O(L).

For j>=a, successive ratios p_(j+1)/p_j=((n-j)/(j+1))*rho^z/(1-rho^z) are bounded by a fixed q<1 for large m, because lambda_z/a=w is bounded strictly below 1. Hence sum_(j>=a) p_j <=p_a/(1-q). For j=a-l<a with l>=1, each backward ratio p_(j-1)/p_j=j(1-rho^z)/((n-j+1)rho^z) for j<=a is bounded by a fixed Q, since lambda_z/a is bounded away from zero. Thus p_(a-l)<=p_a Q^l. Also

    (1-rho^(a-l))^(m-z)
       <= exp(-(m-z)rho^a B^l)
       <= exp(-c a B^l)

for some fixed c>0, because lambda_a/a=v is bounded below and z=O(L). The sum over l>=1 of Q^l exp(-c a B^l) tends to zero: B>1, B^l>=1+(B-1)l, giving an exponentially small geometric bound. Therefore even after dropping the restriction K0>=b0 the entire third-line expectation of Appendix A.2 is O(pi_lambda_z(a)), uniformly.

Multiply by (2) and use z=a+1. The resulting count is at most a constant times

    (lambda_a/(a+1)) * (lambda_a^a/a!)^2
        * (lambda_z^a/a!) exp(-lambda_a-2lambda_z)
    <= C a^(-3/2)
         * exp(a[3+2ln v+ln w-v-2w]).

The inequality is Stirling with uniform constants on the compact normalized means. Since w=rho_*v, the exponent in square brackets is <=g(rho_*)=0 for every v>0. Thus each critical size pair contributes O(L^(-3/2)), with at most O(log L) pairs, yielding o(1). Together with Appendices A.1–A.3 this proves p_m(F)->0 at the boundary. Merely observing a zero leading exponent would not have sufficed.

### A.5. Positive subsequences for every rho>rho_*

Choose t=3/(1+2rho), s=rho*t and let integer j tend to infinity along

    m_j=round(t*j*B^j),   a=j,   z=j+1,
    k=ceil(L+2 log_B L),  c=m-a-z-k.

Then L=j+log_B j+O(1), t_m=m rho^a/L->t, s_m=m rho^z/L->s. All a,z,k=L+O(log L), rho^a,rho^z=Theta(L/m), and m rho^k<=L^(-2). Let Y0 count exact-M necessary triples with these sizes and Y count the sufficient ones (C-hit condition added).

The exact forced-pair formula gives

    E[Y0]=(1+o(1))*(lambda_a^a/a!)*(lambda_a^z/z!)
              *exp(-lambda_a-lambda_z)*pi_lambda_z(k),

uniformly along the chosen subsequence. Here the M-hit factor tends to one because m rho^k<=L^(-2). The binomial approximation is relative 1+o(1) since all sizes are O(L) and probabilities O(L/m); the C-hit factors tend to one by the exact formula and 1-z rho^c<=J(z,c)<=1. Thus E[Y]/E[Y0]->1. Stirling gives

    ln E[Y0]/L -> 3+2ln t+ln s-t-2s = g(rho)>0.

To conclude existence we must use a second moment, not just growing expectation. We prove the second-moment estimate for arbitrary fixed rho under the size and first-moment hypotheses just established. In fact the following overlap argument only uses a,z,k=L+O(log L), rho^a,rho^z=Theta(L/m), m rho^k<=L^(-2), and exponential growth of the first moment.

For fixed triple T=(A,Z,M0), its event E_T consists of the forbidden rectangles A x A, Z x A, Z x M0, row hits to A from outside A union Z, all row hits to Z, non-Z row hits to M0, and Z-to-C column hits. All coordinate blocks in this event are disjoint. A uniquely determines Z and M0. Let S=A union Z union M0, nS=a+z+k=O(L), and let h'=|S intersect S'| and I be the count of common forbidden ordered coordinates for two triples. The individual probability P equals rho^(a^2+az+zk) R with R=exp(-O(L)).

For h'<=L/2, keep all forbidden coordinates and only hits for rows and columns outside S union S'. These families are disjoint. Put ell=min(a,z,k)=L-O(log L). Two simultaneous misses for a given outside row have probability at most rho^(2ell-h'), even when their target sets overlap; the two-term Bonferroni inequality bounds the joint hit probability divided by the product of marginal hit probabilities by 1+O(rho^(2ell-h')). The analogous bound holds for the two column-hit conditions. Across O(m) outside rows/columns the ratio is 1+o(1), since m rho^(2ell-h')<=m^(-1/2) poly(L). Removing O(L) original hit conditions costs a factor 1+o(1). Consequently joint/marginal squared probability <=(1+o(1))*B^I. Also I<=h'^2, and the support-overlap probability for two uniformly independent triples is <=(nS^2/(m-nS))^h'. Summing over 1<=h'<=L/2 gives o(1) in normalized second moment by the geometric base nS^2 B^(L/2)/(m-nS)->0. The h'=0 contribution is <=1+o(1).

For h'>L/2, put D=max(a,z,k)=L+O(log L) and Delta=D h'-I. Dropping all hits gives ratio <=B^(I+O(L)); support-overlap counting gives B^(-L h'+O(h' log L)). Hence the pairs with Delta>=K1 L log_B L have normalized contribution o(1) for sufficiently large fixed K1. For the remaining large-overlap pairs set x=|A intersect S'|, y=|Z intersect S'|, w0=|M0 intersect S'|. The forbidden rectangles imply

    Delta>=x(D-x)+y(D-x)+w0(D-y).

If x<=D/2 then x+y=O(log L), subsequently w0=O(log L), contradicting h'>L/2. Thus x>=D-O(log L). With u=|A intersect A'|, v0=|A intersect Z'| and r0=|A intersect M0'|, the missing common forbidden coordinates include disjoint squares of sizes v0^2,r0^2 and the rectangle of size u(v0+r0). Thus v0+r0=O(sqrt(L log L)), u>=L/2, and then v0+r0=O(log L). It follows that dA=|A minus A'|=O(log L).

Conditional on E_T, the disjoint blocks remain independent. A hit-conditioned block has probability <=rho^b of absence of any specified b coordinates, by the exact conditional factor (1-rho^(blocksize-b))/(1-rho^blocksize)<=1. For another independent A' at distance dA, let e=|(A' minus A) intersect Z|. Absence of both cross directions between A intersect A' and A' minus A has conditional probability <=rho^((a-dA)(2dA-e)): the direction out of A is fresh or hit-conditioned, and the reverse direction is hit-conditioned for all added vertices outside Z, while those inside Z already miss A. These coordinates do not intersect the Z-to-C column conditions. Summing choices at fixed dA>=1 is bounded by

    [a rho^(a-dA) (z+m rho^(a-dA))]^dA.

For dA=O(log L) the base is poly(L)/m, so the conditional expectation of all other such independent A' is o(1). Since A uniquely determines its triple, the remaining pairs, including identical A, contribute at most (1+o(1))*E[Y0], negligible compared with its square. The normalized second moment is therefore 1+o(1). Chebyshev gives Y0>=E[Y0]/2 a.a.s., and Markov gives Y0-Y<E[Y0]/2 a.a.s. because E[Y]/E[Y0]->1. Hence Y>0 a.a.s. and p_(m_j)(F)->1, as asserted.

## Appendix B. Fixed phases for 011010111

### B.1. Statement

Define

    H(t,s)=2+2 ln t-t-s                  for s>=1,
          =3+2 ln t+ln s-t-2s           for s<=1,

and for v>0,

    P_rho(v)=max_{i,l in Z} H(v rho^i,v rho^l).

The maximum is attained: every nonempty superlevel set of H is contained in a compact subset of the positive quadrant (proof below). This phase function is invariant under v -> v B. It is continuous, since locally only finitely many indices can attain the maximum.

For each fixed v>0, on the integer subsequence m_j=round(v j B^j), j->infinity,

    p_(m_j)(F) -> 1  if P_rho(v)>0,
    p_(m_j)(F) -> 0  if P_rho(v)<=0.

The equality case is included, but only for the stated fixed-v subsequences. For arbitrary sequences of m with normalized lattice phase converging to a strictly positive P_rho(v), the probability tends to 1. A corresponding strict negative phase gives probability tending to 0. No claim about arbitrary approach rates to a zero phase is needed for the following exact full-sequence criterion:

- rho<=rho_*=(3sqrt(3)-5)/4: p_m->0 by the earlier threshold theorem.
- rho>rho_* and P_rho(v)>0 for all v in [1,B]: p_m->1.
- rho>rho_* and P_rho(v)<=0 for some v in [1,B]: liminf p_m=0 and limsup p_m=1.

Thus there is a finite, one-dimensional interval-coverage test at every fixed bias. This is an implicit criterion, not a proved closed-form critical rho for full-sequence convergence.

### B.2. Upper bound outside finitely many lattice offsets

The size reduction in Appendix A.1 gives, except with probability o(1), a,z between L-3log_B L and L+1000log_B L, and |M0|>=L-3log_B L, where A is independent, Z is the set of outside-A rows missing A, and M0 is the common nonneighbor set of Z outside A union Z. The actual M-fibre is contained in M0. All rows must hit Z and all non-Z rows must hit M0. The expected necessary count at a,z, with that size restriction on M0, is bounded by

    exp(L H(t_m,s_m)+O((ln L)^2)),
    t_m=m rho^a/L, s_m=m rho^z/L,

uniformly. This is the previous first-moment bound including the binomial upper tail for M0.

To justify compactness, write H(t,s)=2+2ln t-t+J(s), where J(s)=-s for s>=1 and J(s)=1+ln s-2s for s<=1. J is continuous, has maximum -ln 2, and tends to minus infinity at 0 and infinity. The function 2+2ln t-t also tends to minus infinity at both ends and has finite maximum. Hence H tends uniformly below any fixed bound when either coordinate leaves a sufficiently large compact subinterval of (0,infinity).

For fixed v and m_j=round(v j B^j), L=j+log_B j+O(1). Write a=j+i, z=j+l. Then t_m=(v+o(1))rho^i, s_m=(v+o(1))rho^l, with the same relative error for all offsets. For sufficiently large fixed N, whenever |i|>N or |l|>N, at least one of the coordinates is outside the compact interval required for H>=-1. Such sizes contribute at most O((ln L)^2)exp(-L+O((ln L)^2))=o(1). The same compactness argument works for normalized phases in any compact positive interval. In particular the maximum defining P is attained and is a finite maximum locally (use the value at i=l=0 as a continuous lower bound). Its continuity follows.

### B.3. Fixed-phase zero result, including critical phases

For the finitely many remaining fixed offsets i,l set t=v rho^i, s=v rho^l. The Poisson means satisfy

    lambda_a=m_j rho^(j+i)=t j+o(1),
    lambda_z=m_j rho^(j+l)=s j+o(1).

The errors are exponentially small, since rounding changes m by at most 1. With n=m-a-z, the exact necessary expectation at sizes a,z is at most

    (lambda_a^a/a!)(lambda_a^z/z!) exp(-lambda_a-lambda_z+o(1))
       * E[(1-rho^K0)^(m-z)],

where K0~Bin(n,rho^z). This upper bound drops the earlier size restriction on K0. Stirling with fixed offsets gives

    (lambda_a^a/a!)(lambda_a^z/z!) exp(-lambda_a-lambda_z+o(1))
       = O(j^-1) exp(j(2+2ln t-t-s)).

For example lambda_a^(j+i)/(j+i)! is asymptotic to t^i (2 pi j)^(-1/2) exp(j(1+ln t)); the same formula holds for l. If s>=1, bound the expectation by one, obtaining O(j^-1) exp(j H(t,s)). This tends to zero even at H=0.

If s<1, let b_u=P(K0=u). The mass at j is asymptotic to pi_lambda_z(j) by the relative binomial approximation (j,z=O(L), rho^z=O(L/m)). The forward ratios b_(u+1)/b_u for u>=j are bounded by a fixed q<1, since lambda_z/j->s<1. The backward ratios b_(u-1)/b_u for u<=j are bounded by a fixed Q, since s>0. Thus the upper tail is <=b_j/(1-q), and the lower tail at u=j-d, d>=1, has

    b_(j-d)(1-rho^(j-d))^(m-z) <= b_j Q^d exp(-c j B^d)

for fixed c>0, because (m-z)rho^j~v j. The sum over d>=1 tends to zero after division by b_j: B^d>=1+(B-1)d yields a geometric upper bound with ratio Q exp(-c j(B-1)). Therefore

    E[(1-rho^K0)^(m-z)] = O(pi_lambda_z(j))
       = O(j^-1/2) exp(j(1+ln s-s)).

Consequently the count at the fixed pair is O(j^-3/2) exp(j H(t,s)), again tending to zero if H<=0. If P_rho(v)<=0 every one of the finitely many pairs vanishes; Appendix B.2 and Markov prove p_(m_j)->0. Notice that the polynomial prefactors have been computed relative to j, not L: this avoids an unjustified substitution at the exact phase boundary, where O(log L) errors can matter.

For a varying phase with strictly negative P_rho(v), continuity and the uniform bound of Appendix B.2 give a negative margin for every pair, so p_m->0 without any fixed-phase rate assumption.

### B.4. Positive phases: s<=1

Suppose H(t,s)>0 for a fixed integer offset pair. Set a=j+i,z=j+l, k=ceil(L+2log_B L). Then a,z,k=L+O(log L), m rho^a/L->t and m rho^z/L->s, and m rho^k<=L^-2. The exact fixed-size necessary expectation is

    (1+o(1)) (lambda_a^a/a!)(lambda_a^z/z!)
       exp(-lambda_a-lambda_z) pi_lambda_z(k).

Its logarithm divided by L tends to 3+2ln t+ln s-t-2s=H(t,s)>0, including s=1. The sufficient expectation has ratio 1+o(1) to this expectation. The full triple second moment in Appendix A.5 uses only these logarithmic sizes, rho^a,rho^z=Theta(L/m), m rho^k<=L^-2 and exponential mean growth; it does not require the specific choices z=a+1 or the maximizing t. Therefore p_m->1 for these sizes. This argument also works along any sequence with these normalized means converging to t,s and positive limiting H.

### B.5. Positive phases: s>1, pair second moment

For s>1 the typical M0 is larger than L, and unnecessarily forcing it to size L can lose the positive exponent. Instead count pairs T=(A,Z) of disjoint sets with the prescribed a,z satisfying:

- A x A and Z x A entirely absent;
- every row outside A union Z hits A;
- every row hits Z.

Call the event E_T and the count X. It uses only columns ending in A union Z, and its disjoint absence and row-hit blocks have product probability

    P=rho^(a^2+az)(1-rho^a)^(m-a-z)(1-rho^z)^m.

Its exact mean is binom(m,a)binom(m-a,z)P, so

    ln E[X]/L -> 2+2 ln t-t-s=H(t,s)>0.

A uniquely determines Z in a successful pair. We show relative variance tending to zero. For two pairs let S=A union Z, S'=A' union Z', h=|S intersect S'|, I=count of common forbidden ordered coordinates, D=max(a,z)=L+O(log L).

For h<=L/2, retain forbidden bits and only row-hit requirements outside S union S'. For each outside row four hits are required, and the joint probability divided by the product of the four marginal hit probabilities is <=1+O(rho^(2 ell-h)), ell=min(a,z). This follows from two-term Bonferroni for misses, whose pairwise probabilities are bounded by rho^(2 ell-h). Row blocks are disjoint and disjoint from forbidden bits. Removing O(L) marginal hit conditions costs 1+o(1), since miss probabilities are O(L/m). Hence joint/marginal ratio <=(1+o(1))B^I, uniformly, since m rho^(2ell-h)=o(1). For positive h<=L/2 use I<=h^2 and support-overlap probability <=((a+z)^2/(m-a-z))^h; the geometric bound gives total normalized contribution o(1), and h=0 at most 1+o(1).

For h>L/2 use crude ratio B^(I+O(L)), since individual hit factors are exp(-O(L)). Support-overlap probability is B^(-Lh+O(h log L)). Hence pairs with deficit Delta=Dh-I>=K L log_B L are negligible for sufficiently large fixed K. Put x=|A intersect S'|, y=|Z intersect S'|. Restriction of first forbidden set to common support has size x^2+yx, giving

    Delta >= (x+y)(D-x).

For remaining pairs, h>L/2 implies x>=D-O(log L). Put u=|A intersect A'|, w=|A intersect Z'|. Forbidden coordinates lost by the second pair include w^2 from its reflexive Z' and uw from A' to Z'. They are disjoint, and their sum is <=Delta. Thus w=O(sqrt(L log L)), then u>=L/2, and then w=O(log L). In particular d=|A minus A'|=O(log L).

Conditional on E_T, absence requirements and nonempty row-hit blocks remain independent. For independent A' at distance d>=1, with e=|(A' minus A) intersect Z|, the cross coordinates from A intersect A' into added vertices are fresh or hit-conditioned, and the reverse cross coordinates from added vertices outside Z are hit-conditioned into A; the other reverse coordinates are already absent. As in the triple proof the conditional probability of independence is at most rho^((a-d)(2d-e)). Summing over d=O(log L) bounds the conditional expected number of other such independent A' by the geometric sum with base

    a rho^(a-d)(z+m rho^(a-d))=poly(L)/m.

This tends to zero uniformly. A'=A allows only the original Z, so all remaining pairs contribute <=(1+o(1)) E[X], negligible against E[X]^2. Hence E[X^2]/E[X]^2->1.

Now complete a fixed successful pair. Conditional on E_T the untested columns outside A union Z are fresh. The common nonneighbor set M0 of Z among those columns has binomial size with mean (m-a-z)rho^z~sL. For any fixed 1<s0<s, Chernoff gives |M0|>=s0 L and |M0|=O(L) except with probability o(1). Conditional on the Z-row column tests determining M0, edges from non-Z rows to M0 and C0 are fresh. The chance some non-Z row misses M0 is at most m rho^(s0 L)=m^(1-s0)->0, and all non-Z rows hit C0, of size m-O(L), except with probability o(1). The conditional Z-to-C0 law consists of independent nonempty column blocks, so the probability some Z row misses C0 is at most z rho^|C0|=o(1). Thus a fixed successful pair completes with conditional probability 1-o(1), uniformly. Count the failed pairs: their mean is o(E[X]); Markov plus the second-moment concentration yields a successful completion a.a.s. This avoids conditioning fresh bits on the outcome of selecting an arbitrary successful pair.

Combining Appendices B.4 and B.5 proves the positive phase assertion, even for varying sequences with the stated limiting normalized means.

### B.6. Full-sequence convergence and interval coverage

For arbitrary m use j=floor(L-log_B L), v_m=m rho^j/L in [1,B). If P_rho(v)>0 for every v in [1,B], any subsequence of m has a further subsequence on which v_m->v in that interval. Fix a positive pair of offsets for v and use Appendices B.4 or B.5 with a=j+i,z=j+l. Their size and mean assumptions hold. Thus p_m->1 on the further subsequence. The subsequence criterion for convergence gives p_m->1 on the whole sequence. Conversely a phase v with P_rho(v)<=0 supplies the exact zero subsequence by Appendix B.3. If rho>rho_* the earlier threshold theorem guarantees a positive subsequence. This proves the full-sequence criterion in Appendix B.1.

For explicit evaluation only d=l-i>0 with r=rho^d>rho_* can give positive H. Indeed the maximization in the threshold theorem yields a nonpositive maximum for d<=0 or rho^d<=rho_*. For each remaining d, the function H(t,rt) is strictly concave on t>0: the two pieces have negative second derivatives and matching first derivatives at rt=1. It has a unique positive maximum and tends to minus infinity at both ends, hence a unique open positivity interval (alpha_d,beta_d), whose endpoints are the two roots H(t,rt)=0. Define the logarithmic intervals

    I_d=(log_B alpha_d, log_B beta_d) modulo 1.

Then P_rho(v)>0 exactly when log_B v modulo 1 lies in the union of these finitely many open intervals on the phase circle. Coverage of the entire circle is equivalent to p_m->1 in the rho>rho_* regime. A missing point implies oscillation. This includes exact endpoint gaps, because Appendix B.3 supplies fixed-phase zero even at equality.

### B.7. Explicit consequences without numerical root assumptions

At rho=1/10 (theta=0.9) only d=1 can yield a positive value since rho^2=0.01<rho_*. Its positivity interval lies strictly inside (1,B)=(1,10): H(1,rho)=2-2rho+ln rho<0 and H(B,1)=1+2ln B-B<0; the unique maximum occurs between 1 and B. In particular v=1 has no positive lattice pair. The zero phase m_j=round(j*10^j) contrasts with the positive phase m_j=round(2.5*j*10^j), since 3/(1+2rho)=2.5 and g(rho)>0. Thus the last target oscillates at theta=0.9, although its finite-model membership is positive there. More generally for rho_*<rho<=1/5, only d=1 can be positive (rho^2<=0.04<rho_*); H(1,rho)<0 since 2-2rho+ln rho increases on this range and at 1/5 equals 1.6-ln 5<0. H(B,1)<0 for B>=5 by its decreasing derivative and value 2ln 5-4<0. The maximizer lies between 1 and B; hence v=1 is a zero phase throughout this interval. Thus liminf=0,limsup=1 for 4/5<=theta<theta_*.

For rho>=1/3 (theta<=2/3), d=1 alone covers the phase circle. Indeed H(1,rho)=2-2rho+ln rho>0 for 1/3<=rho<1 by concavity and its endpoint values (at 1/3, 4/3-ln 3>0, at 1, zero). Also H(B,1)=1+2ln B-B>0 for 1<B<=3 by concavity and endpoint values (at 1, zero, at 3, 2ln 3-2>0). Strict concavity implies H(t,rho*t)>0 throughout [1,B]. Hence p_m->1 for every 0<theta<=2/3. These explicit ranges are not asserted sharp; the interval criterion above is exact. The fair-model theorem is consistent with this result.

The phase-circle test does not classify arbitrary transition sequences approaching a zero endpoint at shrinking distance. Such scaling windows, remain natural subsequent questions. Appendices C and D give the exact fixed-bias transitions for both exceptional targets. The previous finite-model threshold and counts are unchanged.

## Appendix C. Sharp convergence threshold for 011010111

### C.0. Theorem

Put rho=1-theta, B=1/rho, rho_*=(3sqrt(3)-5)/4. Define

    u(r)=2 ln(1/r)/(1-r),
    D(r)=3+3 ln u(r)+2 ln r-(1+2r^2)u(r).

There is a unique root r_c of D in [1/4,1/3], lying strictly between 251/1000 and 252/1000. Numerically r_c=0.25149763525561764... . Then for the last target F011010111,

    rho>r_c: p_m->1;
    rho_*<rho<=r_c: liminf p_m=0, limsup p_m=1;
    0<rho<=rho_*: p_m->0.

In theta notation the convergence threshold theta_c=1-r_c≈0.7485023647443824 belongs to the oscillatory interval, while theta_*=1-rho_*≈0.950961894323342 belongs to the vanishing interval. This completes the full-sequence classification for this target at all fixed biases.

### C.1. Separation of the lattice optimization

The phase function from Appendix B is P_r(v)=max_(i,l integers) H(v r^i,v r^l), where

    H(t,s)=f(t)+J(s),
    f(t)=2+2 ln t-t,
    J(s)=1+ln s-2s if s<=1, -s if s>=1.

Because the integer indices are independent, the maximum is the sum of separate lattice maxima. The continuous function f increases up to 2 and decreases after 2; J increases up to 1/2 and decreases thereafter. The first adjacent comparison is exact:

    f(t)-f(rt)=2 ln(1/r)-(1-r)t=(1-r)(u-t).

Consequently f(t) maximizes f over its lattice whenever r u<=t<=u: comparison with smaller neighbors follows from the positive difference for t<=u, and comparison with larger neighbors from the negative difference for t/r>=u. Repeating the comparisons proves the claim for all integer shifts. Each phase has a representative in [ru,u] because the ratio of the endpoints is B.

Appendix B.7 proved p_m->1 for r>=1/3, oscillation for rho_*<r<=1/5, and vanishing for r<=rho_*. It remains to decide [1/5,1/3]. All subsequent symbols r denote rho.

For useful monotonic bounds, u=2 integral_0^1 [r+(1-r)x]^(-1) dx is strictly decreasing in r; ru and r^2u are strictly increasing, by differentiation of each integrand after multiplication by r or r^2 (strict on a positive-measure set). Also u>2, since the integrand is >1 for x<1. Values at endpoints used below follow directly from these formulas.

### C.2. No coverage for 1/5<=r<=1/4

Take the phase represented by t=u, or equivalently t0=ru. These have equal f by the adjacent comparison and are f-maximizers. On this range t0 lies between (ln 5)/2 and (2 ln 4)/3, hence 1/2<t0<1. Since J decreases above 1/2, all larger lattice points have worse J. The next smaller lattice point r t0<1/2, and all further smaller ones have worse J than that point. The remaining comparison is

    J(t0)-J(r t0)=ln(1/r)-2(1-r)t0
                =(1-4r)ln(1/r)>=0.

Thus t0 is also a J-maximizer. At this phase

    P_r(u)=H(t0,t0)=3+3 ln t0-3t0<0,

by ln x<x-1 for x!=1. This exact phase therefore supplies a zero subsequence. Appendix A.5 supplies a positive subsequence. Hence the entire stated range oscillates, including r=1/4.

### C.3. Exactly two switching points for 1/4<=r<=1/3

Set b=u/4. Here 1/2<b<1, ru>=b, r^2u<1/2, and r^2u<=b. For the last bound use r^2<=1/9<1/4. For the stronger r^2u<1/2 use u<=u(1/4)=8 ln 4/3 and hence r^2u<=8 ln 4/27<1/2. Also ru>1/2. These estimates follow by the monotonicity above and elementary endpoint values.

On this range the adjacent J-difference J(s)-J(rs) is strictly decreasing in s. For s<=1 it equals ln B-2(1-r)s; for 1<=s<=1/r its derivative is -1-1/s+2r<0; for s>=1/r it equals -(1-r)s. The pieces match. Its unique zero is b=u/4<1. Therefore a lattice J-maximizer is any s in [r b,b], by the same adjacent-comparison argument as for f.

Choose t in [ru,u] to maximize f. Since t>=ru>=b, the J-maximizer can be chosen to be rt when t<=b/r and r^2t when t>=b/r. Indeed rt ranges between r^2u>=rb (because ru>=b) and b on the first interval. On the second interval r^2t ranges between rb and r^2u<=b. The switch b/r lies in [ru,u] because r^2<=1/4<=r. Thus

    P_r(t)=H(t,rt)      for ru<=t<=b/r,
           H(t,r^2t)   for b/r<=t<=u.

The two functions agree at the switch. On each interval they are strictly concave as functions of t (negative second derivatives in H; or f and J are concave). Thus the minimum over the full period is achieved at one of its endpoints or the switch. The two outer endpoints have equal phase value by periodicity. Hence

    min_v P_r(v)=min(D(r),E(r)),
    D(r)=H(u,r^2u)=f(u)+J(r^2u),
    E(r)=H(b/r,b)=f(b/r)+J(b).

The displayed formula for D follows by substitution since r^2u<1.

Both functions are strictly increasing on [1/4,1/3]. For D, u decreases while u>2, so f(u) increases. Also r^2u increases and stays below 1/2, so J(r^2u) increases. For E, b/r=u/(4r) strictly decreases while remaining >2 (at r=1/3 it equals (9/4)ln 3>2). Consequently f(b/r) increases. And b decreases while remaining >1/2, so J(b) increases. These arguments need no derivative of the phase maximizer.

### C.4. Signs and the unique transition

The following strict numerical inequalities can be certified by rational arithmetic with the elementary logarithm series

    ln x = 2 sum_(k=0)^(N-1) y^(2k+1)/(2k+1) + remainder,
    y=(x-1)/(x+1),
    |remainder| <= 2|y|^(2N+1)/((2N+1)(1-y^2)).

For clarity, using N=60 and outward fixed-point rounding at scale 10^18 gives the following conservative rational enclosures (the independent actual integer-arithmetic evaluation obtained narrower intervals):

    -0.003005 < D(251/1000) < -0.003004
     0.003020 < D(252/1000) <  0.003022
     0.001577 < E(251/1000) <  0.001578.

These can be reproduced by taking lower and upper logarithm bounds at the rational endpoints after each arithmetic operation, since ln is increasing. In particular D has exactly one root r_c in (0.251,0.252) by continuity and strict monotonicity. For r<=r_c in [1/4,1/3], D<=0, so the phase u is nonpositive. For r>r_c both D>0 and E>0 (E is increasing and already positive at 0.251). Thus the phase circle is covered precisely when r>r_c. At equality the phase u has P_r(u)=0 (E>0); the exact fixed-phase upper bound of Appendix B gives a zero subsequence, not an inconclusive leading exponent.

Apply the full-sequence criterion and combine with Appendix C.2 and the outer ranges in Appendix B.7 to prove the theorem.

The approximations r_c≈0.25149763525561764, theta_c≈0.7485023647443824 are from floating-point bisection and are not used in the proof. The sign bracket above is certified by a separate integer-arithmetic computation; the exact root definition is the mathematical statement. Transition windows for sequences with bias changing with m, and arbitrary shrinking approaches to a critical lattice phase, are not claimed. Independent review, Lean verification, and literature priority remain pending.

## Appendix D. Sharp phase theorem for 011011101

### D.0. Theorem

Let F=011011101, with labels C,A,V,Z, and missing arrows exactly A->V, V->V, Z->A. Fix edge probability theta in (0,1), including loops, and put rho=1-theta, B=1/rho, L=log_B m. Let T>2 be the unique root of 2+2 ln T-T=0. Then

    theta_0=1-1/(e T)=0.9313234165433595...,

and the complete fixed-bias classification is

    0<theta<theta_0: p_m(F)->1;
    theta_0<=theta<1: liminf p_m(F)=0, limsup p_m(F)=1.

In particular the endpoint belongs to the oscillatory range, and no fixed bias gives a zero full-sequence limit.

More precisely, for fixed v>0 and m_j=round(v j B^j),

    p_(m_j)(F)->1  iff  exists i in Z with 1/e < v rho^i < T;
    p_(m_j)(F)->0  otherwise.

If the phase is strictly positive, the same limit one holds along arbitrary sequences with normalized phase tending to v. Exact zero phases are proved for fixed-v subsequences, not all shrinking boundary approaches.

### D.1. Necessary conditions and uniform logarithmic size bound

Let b0=L-3 log_B L, h=ceil(128 L). The probability of an entirely absent h-by-h rectangle is <=B^(2hL-h^2)=exp(-Omega(L^2)). Outside this exceptional event an independent fibre has b<h. Also with probability 1-o(1), no successful map can have b<b0 or z<b0. For b the label-specific tiny-fibre argument in the proof of Theorem 2 of the main text applies: the only universally incoming labels are C,Z, whose missing outgoing signatures are empty and {A}, respectively. Neither misses exactly V. On the complement of the rectangle exception the large labels form a complete core. For any fixed small disjoint fibres (each <h), an outside row that misses precisely V among these fibres and receives an edge from every small fibre would have to have a universal incoming label missing exactly V. Such a witness is impossible under a successful map. Its independent tests over outside vertices have success probability >=rho^b theta^7, and the probability of no witness when b<b0 is exp(-Omega(L^3)). The number of small-fibre configurations is exp(O(L^2)), so a union bound gives o(1). The tests are not conditioned on the rectangle event. For z the simpler union bound suffices: if a set of size z<b0 is hit by every row, its probability for fixed set is (1-rho^z)^m<=exp(-L^3). Summing over <=m^(ceil(b0)+1) such choices gives o(1). Thus, up to a probability o(1), restrict b0<=b<h and z>=b0.

Consequently the label-specific exclusions apply. Except with probability o(1), every successful map has b=|V| in [b0,h), where b0=L-3log_B L, h=ceil(128L), and z=|Z|>=b0. Here V is independent, A is exactly the outside rows missing V, and Z is exactly the outside-(A union V) rows missing A. All rows hit Z. For a fixed b-subset V conditional on independence, reveal its columns; then a=|A| is Bin(m-b,rho^b). Conditional on this history the columns of A are fresh and z is Bin(m-b-a,rho^a). The independent-set mean

    N_b=binom(m,b)rho^(b^2)<=(e lambda/b)^b, lambda=m rho^b,

is uniformly <=exp(400 L ln L) on [b0,h) for large m because lambda<=L^3 and b<=129L.

Take K=1000 and u=L+K log_B L. If a>u then the conditional mean of z is <=L^(-K). By the binomial upper-tail bound, the probability of z>=b0 is <=exp(-(K+1+o(1))L ln L), uniformly. Multiplication by N_b and summing O(L) sizes shows that such a cannot occur in a successful map except with probability o(1). Also if b>u then lambda<=L^(-K), and the independent-set mean itself is exp(-Omega(L ln L)), with a summable bound over O(L) sizes. Thus restrict b to [b0,u], a<=u, z>=b0.

Write t=lambda/L. Then b=L+O(log L) and |ln t|=O(log L) uniformly. Stirling gives

    ln N_b <= L(1+ln t)+O((ln L)^2).

If t<=1, drop the a condition; if t>=1, use the binomial lower-tail exponential Markov bound with parameter ln t (valid even if u exceeds the mean):

    Pr(a<=u | V independent)
       <= exp(mu(1/t-1)+u ln t),
       mu=(m-b)rho^b.

Since mu=tL-O(L^4/m), the log bound is L(1-t+ln t)+O((ln L)^2), uniformly for t>=1. Thus the expected necessary count at size b, keeping only a<=u, is <=exp(L G(t)+O(log^2 L)), where

    G(t)=1+ln t                 if t<=1,
         2+2 ln t-t             if t>=1.

G is continuous, tends to minus infinity at both ends, and is positive precisely on (1/e,T). For fixed v and b=j+i, t=(v+o(1))rho^i; the relative error is independent of i. All but finitely many offsets i give G(t)<-1 uniformly, and their count is negligible by the bound just proved and the O(log L) size range.

### D.2. Exact zero phases, including endpoints

Along m_j=round(v j B^j), for a fixed remaining offset i put t=v rho^i. Then lambda=t j+o(1), b=j+i, L=j+log_B j+O(1). In particular

    N_b=O(j^-1/2) exp(j(1+ln t))

by the falling factorial approximation and Stirling with fixed offset. If t<=1/e this tends to zero, including at equality.

For t>=T we need to control the forced A-size more precisely than a<=u. Choose a fixed positive integer K1 so large that v rho^K1 is sufficiently small. Conditional on the V-column history with a>j+K1, the mean of z is <=m rho^(j+K1)=(v rho^K1+o(1))j. Since b0/j->1, the binomial upper-tail bound for z>=b0 gives

    Pr(z>=b0 | V-column history) <= exp(-c j),

where c can be made arbitrarily large by increasing K1 (from (e mu/ceil(b0))^ceil(b0)). Take c>1+ln t. Multiplying by N_b gives negligible expected count for this large-a range. This uses the conditional z law before exposing A columns, not conditioning on successful completion.

On a<=j+K1, the binomial mean of a is (m-b)rho^b=t j+o(1), with t>=T>1. The mass at j+K1 is (1+o(1)) times its Poisson mass of parameter lambda; this follows by relative binomial approximation for size O(j), q=rho^b=O(j/m). All backward ratios of consecutive masses below j+K1 are bounded by a fixed q0<1, since (j+K1)/lambda->1/t<1. Thus

    Pr(a<=j+K1 | V independent)
       <= C pi_lambda(j+K1)
       = O(j^-1/2) exp(j(1+ln t-t)).

Multiplying by N_b bounds the count by O(j^-1) exp(j(2+2ln t-t)), which tends to zero for t>=T, including the equality case. The argument includes the z>=b0 exception from Appendix D.1. Sum the finitely many offsets. If no lattice value lies in (1/e,T), the necessary witness count tends to zero after removing o(1) exceptions, so p_m->0. At endpoints a zero leading exponent alone would not justify this conclusion; the exact fixed-phase prefactors are essential.

### D.3. Positive phases: choose an A-size strictly below L

Suppose t is strictly in (1/e,T), with b=j+i and m rho^b/L->t, either along the exact phase or along an arbitrary sequence of normalized phases tending to v. Choose a fixed alpha in (0,1) so that

    R(t,alpha)=1+ln t + alpha(1+ln(t/alpha))-t >0.

Such an alpha always exists. For t<1 take alpha=t, yielding R=1+ln t>0. For 1<=t<T, at alpha=1 the expression is 2+2ln t-t>0 (including t=1), so by continuity a sufficiently close alpha<1 works. Set a=floor(alpha L). These sizes are positive and b=L+O(log L); a/L->alpha<1.

For disjoint sets V,A of sizes b,a, let E_(V,A) be the event that V is independent and A is exactly the outside-V rows missing V. This uses only V columns and is the conjunction of the absent rectangles V x V, A x V and independent nonempty row-hit blocks to V for all other rows. A successful pair is uniquely determined by V. Write X for the number of such pairs. Its exact mean is

    E[X]=binom(m,b)binom(m-b,a)rho^(b^2+ab)
                       (1-rho^b)^(m-b-a).

Falling factorial estimates and Stirling yield ln E[X]/L->R(t,alpha)>0. Explicitly the leading factors are (lambda^b/b!)(lambda^a/a!)exp(-lambda+o(1)); b/L->1,a/L->alpha and lambda/L->t.

### D.4. Pair second moment with unequal fibre scales

For two pairs let S=V union A, S'=V' union A', h'=|S intersect S'|, I the number of common forbidden ordered coordinates. The individual probability is rho^(b^2+ab) times exp(-O(L)). Let D=max(b,a)=b=L+O(log L). The supports have size a+b=O(L).

For h'<=L/2, retain all forbidden bits and only the two row-hit requirements for rows outside S union S'. These blocks are disjoint from forbidden bits and independent across rows. The joint probability for a row to hit both V,V' is 1-2rho^b+rho^(2b-|V intersect V'|). Compared with (1-rho^b)^2 its ratio is <=1+O(rho^(2b-h')). Across at most m rows this is 1+o(1), since b=L+O(log L). Dropping O(L) other marginal row hits costs only 1+o(1). The joint/marginal squared probability is therefore <=(1+o(1))*B^I. As I<=h'^2, the normalized contribution of positive h'<=L/2 is o(1) using the support intersection bound ((a+b)^2/(m-a-b))^h' and the geometric base ((a+b)^2 B^(L/2)/(m-a-b))->0. The zero-overlap contribution is at most 1+o(1). Notice that no lower bound near L for a is needed in this argument because every hit block ends in V.

For h'>L/2, dropping all hits gives ratio <=B^(I+O(L)); the support-overlap bound is B^(-L h'+O(h' log L)). Therefore pairs with deficit Delta=Dh'-I>=K2 L log_B L give o(1) normalized contribution for sufficiently large fixed K2. For other pairs put x=|V intersect S'| and y=|A intersect S'|. The first forbidden set restricted to the common support has x^2+yx=h'x coordinates, so Delta>=h'(D-x). Thus x=D-O(log L). With u=|V intersect V'|, w=|V intersect A'|, the lost forbidden coordinates include the square w^2 and the rectangle uw (A' is reflexive and V' reaches A'). Hence w^2+uw<=Delta. First w=O(sqrt(L log L)), then u>=L/2 and w=O(log L). Consequently d=|V minus V'|=O(log L).

Condition on the first successful pair. For another independent V' at distance d>=1 let e=|(V' minus V) intersect A|. Independence of V' requires both cross directions between V intersect V' and the added vertices to be absent. Outgoing coordinates from V to added vertices are fresh (they end outside V); reverse coordinates from added vertices outside A are hit-conditioned into V, and those from A already absent. The blocks are disjoint. A block conditioned nonempty has probability at most rho^q that a specified q-bit subset is absent, by its exact conditional formula. Thus the conditional probability of V' independence is at most rho^((b-d)(2d-e)). Sum over possible V' of fixed d by binomial upper bounds to obtain

    [b rho^(b-d)(a+m rho^(b-d))]^d.

For d=O(log L) the base is poly(L)/m and the sum over positive d is o(1). Since V uniquely determines its A, the conditional count of other successful pairs in this near-aligned range is o(1), and identical V contributes exactly one. Thus the remaining pairs contribute at most (1+o(1))*E[X], negligible relative to E[X]^2. The three ranges exhaust the second moment, which is (1+o(1))*E[X]^2.

### D.5. Completion of a successful pair

Given a fixed successful V,A pair, all columns outside V are still fresh because the pair event uses V columns only. Expose A columns. Every row in V union A hits A except with probability at most (a+b)rho^a=o(1), since alpha>0. Define Z as all rows outside V union A missing A. Its binomial mean is (m-a-b)rho^a=m^(1-alpha+o(1)). Chernoff gives polynomially growing |Z| and |Z|<=m/4 a.a.s. (e.g. |Z|>=m^((1-alpha)/2) eventually on a high-probability event). Let C be the complement, of size >=m/2. Conditional on the V,A column history, remaining columns ending in Z or C are fresh; their choices are functions of that history. All rows hit both Z and C except with probability at most m(rho^|Z|+rho^|C|)=o(1) on the size event. All four fibres are nonempty and exactly the required successor statuses hold.

The fixed-pair failure probability is o(1), uniformly in the pair. The expected count of failed pairs is o(E[X]); Markov and the preceding concentration of X show at least one successful completed pair a.a.s. This proves p_m->1 whenever t is in the positive interval. As the estimates use only the limiting means with a fixed positive margin, the same result holds for varying phases tending to a positive phase. This is the new step extending the earlier typical-A construction to rare A-sizes.

### D.6. Full-sequence transition

The positive interval (1/e,T) is open and has multiplicative ratio e T. Its logarithmic image on the phase circle (modulo ln B) covers that circle exactly when ln(e T)>ln B, equivalently rho>1/(e T). To see this directly, scale any v by integer powers of B to lie in [1/e,B/e). If B<e T then a boundary value 1/e can be moved to B/e which is strictly between 1/e and T; all others already lie inside. If B>=e T the phase v=1/e has no lattice point strictly in the interval, because its next larger value B/e>=T. This remains true at equality. A positive phase, for example v=1/2, exists for every rho.

If the circle is covered, every sequence of m has a further subsequence on which j=floor(L-log_B L) and v_m=m rho^j/L in [1,B) converge in phase to some v in [1,B]. Choose one positive offset and apply Appendices D.3–D.5. The subsequence criterion yields p_m->1. If not covered, Appendix D.2 gives a zero subsequence and the positive phase gives a one subsequence. This proves the theorem, including the exact critical bias theta_0. The value T is the unique root greater than 2 because the function 2+2ln T-T decreases strictly there from a positive value to minus infinity.

Together with Appendix C, the earlier 92 uniformly vanishing types and 10 uniformly positive types, this gives the full existence-limit or oscillation classification of all 104 four-point central isomorphism classes at every fixed edge bias. This does not classify the probability along arbitrary shrinking critical phase windows, all larger targets, or the full almost-sure logic. Literature priority, independent review and Lean verification remain pending.
