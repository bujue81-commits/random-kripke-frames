# Sharp lattice-phase classification for the two-stage target 011011101

Status: internal hand proof, not independently reviewed or Lean-verified. Strengthens HIGH_BIAS_FOUR_POINT_OSCILLATION.md and TWO_STAGE_FORCED_FIBRE_POSITIVE.md. The fair-model paper is unchanged. No priority claim.

## Theorem

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

## 1. Necessary conditions and uniform logarithmic size bound

Use the label-specific tiny-fibre and dominating-set exclusions in HIGH_BIAS_FOUR_POINT_OSCILLATION.md. Except with probability o(1), every successful map has b=|V| in [b0,h), where b0=L-3log_B L, h=ceil(128L), and z=|Z|>=b0. Here V is independent, A is exactly the outside rows missing V, and Z is exactly the outside-(A union V) rows missing A. All rows hit Z. For a fixed b-subset V conditional on independence, reveal its columns; then a=|A| is Bin(m-b,rho^b). Conditional on this history the columns of A are fresh and z is Bin(m-b-a,rho^a). The independent-set mean

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

## 2. Exact zero phases, including endpoints

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

Multiplying by N_b bounds the count by O(j^-1) exp(j(2+2ln t-t)), which tends to zero for t>=T, including the equality case. The argument includes the z>=b0 exception from Section 1. Sum the finitely many offsets. If no lattice value lies in (1/e,T), the necessary witness count tends to zero after removing o(1) exceptions, so p_m->0. At endpoints a zero leading exponent alone would not justify this conclusion; the exact fixed-phase prefactors are essential.

## 3. Positive phases: choose a sublogarithmic-margin A-size

Suppose t is strictly in (1/e,T), with b=j+i and m rho^b/L->t, either along the exact phase or along an arbitrary sequence of normalized phases tending to v. Choose a fixed alpha in (0,1) so that

    R(t,alpha)=1+ln t + alpha(1+ln(t/alpha))-t >0.

Such an alpha always exists. For t<1 take alpha=t, yielding R=1+ln t>0. For 1<=t<T, at alpha=1 the expression is 2+2ln t-t>0 (including t=1), so by continuity a sufficiently close alpha<1 works. Set a=floor(alpha L). These sizes are positive and b=L+O(log L); a/L->alpha<1.

For disjoint sets V,A of sizes b,a, let E_(V,A) be the event that V is independent and A is exactly the outside-V rows missing V. This uses only V columns and is the conjunction of the absent rectangles V x V, A x V and independent nonempty row-hit blocks to V for all other rows. A successful pair is uniquely determined by V. Write X for the number of such pairs. Its exact mean is

    E[X]=binom(m,b)binom(m-b,a)rho^(b^2+ab)
                       (1-rho^b)^(m-b-a).

Falling factorial estimates and Stirling yield ln E[X]/L->R(t,alpha)>0. Explicitly the leading factors are (lambda^b/b!)(lambda^a/a!)exp(-lambda+o(1)); b/L->1,a/L->alpha and lambda/L->t.

## 4. Pair second moment with unequal fibre scales

For two pairs let S=V union A, S'=V' union A', h'=|S intersect S'|, I the number of common forbidden ordered coordinates. The individual probability is rho^(b^2+ab) times exp(-O(L)). Let D=max(b,a)=b=L+O(log L). The supports have size a+b=O(L).

For h'<=L/2, retain all forbidden bits and only the two row-hit requirements for rows outside S union S'. These blocks are disjoint from forbidden bits and independent across rows. The joint probability for a row to hit both V,V' is 1-2rho^b+rho^(2b-|V intersect V'|). Compared with (1-rho^b)^2 its ratio is <=1+O(rho^(2b-h')). Across at most m rows this is 1+o(1), since b=L+O(log L). Dropping O(L) other marginal row hits costs only 1+o(1). The joint/marginal squared probability is therefore <=(1+o(1))*B^I. As I<=h'^2, the normalized contribution of positive h'<=L/2 is o(1) using the support intersection bound ((a+b)^2/(m-a-b))^h' and the geometric base ((a+b)^2 B^(L/2)/(m-a-b))->0. The zero-overlap contribution is at most 1+o(1). Notice that no lower bound near L for a is needed in this argument because every hit block ends in V.

For h'>L/2, dropping all hits gives ratio <=B^(I+O(L)); the support-overlap bound is B^(-L h'+O(h' log L)). Therefore pairs with deficit Delta=Dh'-I>=K2 L log_B L give o(1) normalized contribution for sufficiently large fixed K2. For other pairs put x=|V intersect S'| and y=|A intersect S'|. The first forbidden set restricted to the common support has x^2+yx=h'x coordinates, so Delta>=h'(D-x). Thus x=D-O(log L). With u=|V intersect V'|, w=|V intersect A'|, the lost forbidden coordinates include the square w^2 and the rectangle uw (A' is reflexive and V' reaches A'). Hence w^2+uw<=Delta. First w=O(sqrt(L log L)), then u>=L/2 and w=O(log L). Consequently d=|V minus V'|=O(log L).

Condition on the first successful pair. For another independent V' at distance d>=1 let e=|(V' minus V) intersect A|. Independence of V' requires both cross directions between V intersect V' and the added vertices to be absent. Outgoing coordinates from V to added vertices are fresh (they end outside V); reverse coordinates from added vertices outside A are hit-conditioned into V, and those from A already absent. The blocks are disjoint. A block conditioned nonempty has probability at most rho^q that a specified q-bit subset is absent, by its exact conditional formula. Thus the conditional probability of V' independence is at most rho^((b-d)(2d-e)). Sum over possible V' of fixed d by binomial upper bounds to obtain

    [b rho^(b-d)(a+m rho^(b-d))]^d.

For d=O(log L) the base is poly(L)/m and the sum over positive d is o(1). Since V uniquely determines its A, the conditional count of other successful pairs in this near-aligned range is o(1), and identical V contributes exactly one. Thus the remaining pairs contribute at most (1+o(1))*E[X], negligible relative to E[X]^2. The three ranges exhaust the second moment, which is (1+o(1))*E[X]^2.

## 5. Completion of a successful pair

Given a fixed successful V,A pair, all columns outside V are still fresh because the pair event uses V columns only. Expose A columns. Every row in V union A hits A except with probability at most (a+b)rho^a=o(1), since alpha>0. Define Z as all rows outside V union A missing A. Its binomial mean is (m-a-b)rho^a=m^(1-alpha+o(1)). Chernoff gives polynomially growing |Z| and |Z|<=m/4 a.a.s. (e.g. |Z|>=m^((1-alpha)/2) eventually on a high-probability event). Let C be the complement, of size >=m/2. Conditional on the V,A column history, remaining columns ending in Z or C are fresh; their choices are functions of that history. All rows hit both Z and C except with probability at most m(rho^|Z|+rho^|C|)=o(1) on the size event. All four fibres are nonempty and exactly the required successor statuses hold.

The fixed-pair failure probability is o(1), uniformly in the pair. The expected count of failed pairs is o(E[X]); Markov and the preceding concentration of X show at least one successful completed pair a.a.s. This proves p_m->1 whenever t is in the positive interval. As the estimates use only the limiting means with a fixed positive margin, the same result holds for varying phases tending to a positive phase. This is the new step extending the earlier typical-A construction to rare A-sizes.

## 6. Full-sequence transition

The positive interval (1/e,T) is open and has multiplicative ratio e T. Its logarithmic image on the phase circle (modulo ln B) covers that circle exactly when ln(e T)>ln B, equivalently rho>1/(e T). To see this directly, scale any v by integer powers of B to lie in [1/e,B/e). If B<e T then a boundary value 1/e can be moved to B/e which is strictly between 1/e and T; all others already lie inside. If B>=e T the phase v=1/e has no lattice point strictly in the interval, because its next larger value B/e>=T. This remains true at equality. A positive phase, for example v=1/2, exists for every rho.

If the circle is covered, every sequence of m has a further subsequence on which j=floor(L-log_B L) and v_m=m rho^j/L in [1,B) converge in phase to some v in [1,B]. Choose one positive offset and apply Sections 3-5. The subsequence criterion yields p_m->1. If not covered, Section 2 gives a zero subsequence and the positive phase gives a one subsequence. This proves the theorem, including the exact critical bias theta_0. The value T is the unique root greater than 2 because the function 2+2ln T-T decreases strictly there from a positive value to minus infinity.

Together with LAST_TARGET_SHARP_CONVERGENCE_THRESHOLD.md, the earlier 92 uniformly vanishing types and 10 uniformly positive types, this gives the full existence-limit or oscillation classification of all 104 four-point central isomorphism classes at every fixed edge bias. This does not classify the probability along arbitrary shrinking critical phase windows, all larger targets, or the full almost-sure logic. Literature priority, independent review and Lean verification remain pending.
