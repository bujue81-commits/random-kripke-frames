# Two-stage forced-fibre positive construction for 011011101

Internal hand proof; not Lean-verified, externally refereed, or novelty-checked. The result covers the original fair model and a specified open interval of fixed biases, not every fixed edge probability.

## Statement

Let F have universal reflexive center c and peripheral relation 011011101 in row-major order. Relabel A=old peripheral 2, B=old peripheral 1, Z=old peripheral 3. Its only missing arrows are A->B, B->B, Z->A. All other ordered edges are present.

For independent source edge probability theta with 0<theta<1-e^(-1), including loops, write rho=1-theta, Bbase=1/rho and L=log_Bbase m. Then

    P(G_m ->> F) -> 1.

In particular this holds for theta=1/2. For theta>=1-e^(-1) the proof below gives no conclusion; do not infer a zero limit.

## 1. Independent sets at an appropriate integer scale

Choose a fixed small delta>0 with rho*Bbase^(-delta)>e^(-1), possible by the hypothesis. Take

    b=ceil(L-log_Bbase L+delta), q=rho^b, lambda=m*q.

Thus b/L->1, and rho*Bbase^(-delta)*L <=lambda<=Bbase^(-delta)*L. There exist constants 0<alpha<beta<1 and eta>0 such that for all large m

    alpha<lambda/L<beta, lambda/b>e^(-1)+eta,

with strict margins (choose alpha smaller and beta larger than the indicated bounds).

Let X count b-subsets V with no ordered internal edge, including loops. Its expectation is N*rho^(b^2), N=binom(m,b). The falling factorial estimate (m)_b/m^b=1+o(1) and Stirling give

    ln E[X]=b*(1+ln(lambda/b))-(1/2)ln(2*pi*b)+o(1).

In particular E[X]>=exp(c L) for some c>0.

For independent uniform b-subsets the intersection size j has probability P_j=binom(b,j)binom(m-b,b-j)/binom(m,b). Joint independence of the two sets requires 2b^2-j^2 absent ordered coordinates, so

    E[X^2]/E[X]^2=sum_j P_j*rho^(-j^2).

For 1<=j<=b/2, P_j <= binom(b,j)*(b/(m-b))^j by a union bound for containing a specified j-subset. Hence P_j*rho^(-j^2) <= (b^2*Bbase^(b/2)/(m-b))^j; the base tends to zero, so this range sums to o(1).

For j>b/2 write k=b-j, 0<=k<b/2. Exactly

    P_j*rho^(-j^2)
       = E[X]^(-1)*binom(b,k)*binom(m-b,k)*rho^(2bk-k^2)
       <= E[X]^(-1)*(b*m*rho^(3b/2))^k.

The geometric base tends to zero because b=L-O(log L). Summing gives o(1) since E[X] grows exponentially. The j=0 contribution is <=1. Thus Var(X)/E[X]^2=o(1), and X>=E[X]/2 with probability 1-o(1).

## 2. Complete a fixed independent B-fibre with high conditional probability

Fix one b-subset V and condition only on its internal independence. Define A as all outside vertices missing V by outgoing edges. Conditional on independence, |A| has Bin(m-b,q) distribution, using disjoint coordinates outside V x V. By Chernoff and the strict margins above, except with probability o(1),

    alpha*L <= |A| <= beta*L.

This forces nonempty A. The V-fibre misses itself, A misses V, and every other row hits V, by construction.

Now reveal all edges ending in A. Conditional on the previous history of edges ending in V, these are fresh independent bits, because A is determined by that history and disjoint from V. The probability that some row in A or V misses A is <=(|A|+b)*rho^|A|=o(1) uniformly on the size event. Define Z as the set of all rows outside A union V that miss A. Conditional on the preceding V-column history (before exposing A columns), |Z| is binomial with parameters m-|A|-b and rho^|A|. It is of mean at least (m-O(L))*m^(-beta), and at most m*m^(-alpha). Chernoff for the lower bound and Markov for the upper bound imply, except with probability o(1),

    |Z| >= m^(1-beta)/3, |Z| <= m/4.

The row-hit event for A and V need not be assumed independent of the Z-size event; a union bound suffices. On both events, the rows missing A are exactly Z. Define C as all remaining vertices, so |C|>=m/2 for large m. Both Z and C are disjoint from A,V and their choice is measurable in the exposed V and A column history.

For clarity about adaptive exposure: for fixed V, first reveal all columns ending in V, which determine A. Conditional on those columns, reveal all columns ending in the resulting A. For each realization, the remaining columns ending outside V union A are disjoint fresh coordinates under the product law. The sets Z,C are functions only of the revealed history. Consequently, conditional on the size bounds, the probability any row misses Z or C is <=m*(rho^(m^(1-beta)/3)+rho^(m/2))=o(1).

All rows therefore hit Z and C, precisely the required universal columns. The B-hit status is absent exactly in A and V; the A-hit status is absent exactly in Z. With V as the B-fibre, these are the exact target successor images. All four fibres are nonempty, so the map is a surjective bounded morphism. The conditional probability of failure of this completion for any fixed independent V is o(1), uniformly in V.

## 3. Avoid adaptive-choice bias by counting bad independent sets

Let X_bad count independent b-subsets V for which the deterministic completion rule above fails to produce a surjective bounded morphism. The conditional estimates for each fixed V give E[X_bad]=o(E[X]) by linearity; no independence across different V is needed. Markov yields X_bad<E[X]/2 with probability 1-o(1). Section 1 gives X>=E[X]/2 with probability 1-o(1), so with probability tending to one at least one independent V has a successful completion. We do not select an independent set using arbitrary edge information and then assume its external edges remain fresh. This counting argument proves the theorem.

## 4. Census and scope

In the fair model, this resolves one of the two remaining four-point types positively. The cumulative fair census is 92 zero-limit, 11 one-limit, one unresolved (011010111), total 104 isomorphism types. Labelled counts 454,52,6. The number of known minimal vanishing four-point types remains 22. For the entire fixed-bias interval 0<theta<1-e^(-1) the same census holds; for other biases retain the previous 102/104 census. No classification of the remaining frame or general non-finite axiomatizability is claimed.

The method is related to standard second moments for random graph independent sets and kernels; the directed loop-including model and the forced-fibre extension are proved here directly. Literature priority for this application remains unverified. See also Schamm (2002) and Goranko (2020) in docs/RELATED_WORK.md. Recent CI remains unavailable.
