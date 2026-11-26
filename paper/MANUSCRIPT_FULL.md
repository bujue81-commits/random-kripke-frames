# Almost-Sure Bounded-Morphic Images of Random Kripke Frames: A Complete Classification of Central Frames on at Most Four Vertices

**Working manuscript, version 0.2 — 26 November 2026.** Author and affiliations to be confirmed by the researcher. Not submitted or independently refereed. The present text includes the complete probability arguments and the finite classification algorithm. The finite census has been independently recomputed; the probability arguments remain hand proofs. Novelty is not asserted until the literature audit is complete. The source is Markdown; a compiled typeset edition is not yet available.

## Abstract

Let G_m be a random labelled Kripke frame on m points, in which each ordered pair, including a loop, is independently an arrow with probability 1/2. For a fixed finite frame F with a central point, we investigate the asymptotic probability that F is a surjective bounded-morphic image of G_m. We give a proof-based classification for central targets on at most four points. Among the 104 isomorphism classes of four-point central frames, 92 have image probability tending to zero and 12 have image probability tending to one. Exactly 22 of the vanishing four-point classes are minimal under proper bounded-morphic images with vanishing probability. Together with the smaller classes, this yields 25 mutually independent characteristic-formula axiom schemes over the modal logic of the countable random frame. The arguments use a forbidden-degree estimate, a two-sided signature construction, and forced-fibre witness counts with conditional second-moment estimates. Several estimates extend to fixed biased edge probabilities. The result is a restricted classification of target images, not a general zero-one law or an axiomatization of the full almost-sure modal logic.

Keywords: modal logic; random directed graphs; bounded morphisms; characteristic formulas; first and second moments; kernel partitions.

## 1. Introduction

Almost-sure frame validity differs substantially from almost-sure model validity. The latter is amenable to first-order zero-one laws, whereas validity under all valuations quantifies over subsets of the frame. Le Bars [3] disproved the general modal frame zero-one law. Goranko and Kapron [1] identified the logic ML^r of the countable random frame and its relation to almost-sure frame validity. Goranko [2, Sections 3–4] shows that finite models of ML^r are precisely finite frames with a central point and relates additional almost-sure validities to characteristic formulas of finite targets.

Schamm [4, Sections 3.3.5–3.3.6] considered the first moment of F-partitions and examined the 16 possible three-point central relations computationally. The present project uses this framework, distinguishes expectations from actual existence, and organizes rigorous candidate proofs for the three- and four-point classification. We do not claim that the partition method or the small-target enumeration originated here. Sliusarev [5–7] develops related classifications for restricted classes of random frames; their scope is not identical to unrestricted random relations. Priority of the particular asymptotic conclusions in this manuscript remains under investigation.

## 2. Setting and main theorem

Let F=(V,R) be a nonempty finite directed frame. A point c is central if cRv and vRc for every v in V (including c). For a source G=(W,S), a surjective function f:W->V is a bounded morphism if for each x in W,

    {f(y): x S y} = {v: f(x) R v}.

This is equivalent to the usual forth and back conditions. Denote the existence probability by p_m(F). Unless otherwise stated the edge probability is theta=1/2. For biased auxiliary results, fix 0<theta<1, rho=1-theta, B=1/rho, L=log_B m and b=L-log_B L.

Represent a central target with r noncentral labels by the r-by-r peripheral adjacency matrix written in row-major bit order. All arrows incident with the distinguished central label 0 are present. Take the lexicographically least encoding under simultaneous peripheral row/column permutation as canonical. This counts unpointed isomorphism classes: any isomorphism sends a central vertex to a central vertex, and any two central vertices can be exchanged by an automorphism, since both their rows and columns are universal.

**Theorem 1 (small central-frame classification).** For every central target on at most four vertices, p_m(F) converges to 0 or 1. The numbers of isomorphism classes and minimal vanishing classes are as follows.

| vertices | all | p->0 | p->1 | minimal p->0 |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 | 0 |
| 2 | 2 | 1 | 1 | 1 |
| 3 | 10 | 7 | 3 | 2 |
| 4 | 104 | 92 | 12 | 22 |

Minimal means no nonisomorphic proper surjective bounded-morphic image has vanishing probability. The canonical minimal two- and three-point encodings are 0, 0001 and 1001. The complete four-point classifier is given in Section 6.

**Proof strategy.** Composition makes vanishing probability propagate from a quotient to its source target: if F ->> H then p_m(F)<=p_m(H). Classify the other targets using Theorems 2 and 3 and the five exceptional encodings in Section 5. The finite orbit and quotient census is a deterministic calculation, with full pseudocode below and a reproducible Python implementation. Every category is covered by a probability proof; numerical experiments do not determine any asymptotic label.

## 3. Vanishing criterion

For a central F with r peripherals put A_ij=1 if the peripheral arrow i->j is missing, 0 otherwise. Write q=sum A_ij and g_i=sum_j(A_ij+A_ji). A missing loop contributes twice to g_i.

**Theorem 2 (no singleton miss and degree).** Assume every g_i>=2, and no label with a universal incoming column has exactly one missing outgoing arrow. Then d=q-r>=0 and

    log_B p_m(F) = -d b^2+O_F,theta(L).

When d=0, moreover p_m(F)=O(L^(-r/2)). In particular every such target vanishes. This holds at every fixed bias.

**Proof.** Fix a large C depending only on r, and put h=ceil(C L), b0=L-3 log_B L. The probability of an empty ordered h-by-h rectangle is at most B^(2hL-h^2). Outside that event, the labels whose fibres have size >=h form a complete reflexive core U. Fix all the other small fibres, whose union has O(L) vertices. If fibre i has size <b0, a row outside the union which misses precisely i among the small fibres and receives an arrow from each small fibre would have a universally incoming target label missing precisely i, contrary to the hypothesis. These independent outside-row tests each succeed with probability >=rho^a_i theta^(2|S|-1), where S is the set of small labels. Their absence has probability exp(-Omega(L^3)); union over B^O(L^2) choices of small fibres leaves a negligible event. The empty-rectangle term is negligible at the stated scale by increasing C.

For remaining peripheral sizes a_i>=b0 and T=sum a_i, the forbidden-coordinate count Q=sum A_ij a_i a_j is at least q b0^2+2b0(T-r b0). Since the multinomial factor is <=m^T, T>CL contributes B^(-d L^2-Omega(L^2)) after summing at most m^r vectors. For T<=CL, the central fibre has size >=m/2 and factorial bounds give log_B multinomial <=bT+O(L). The derivatives of Q-bT are positive on all a_i>=b0. Clip sizes below b upward to b: with delta_i=(b-a_i)_+ this gives Q-bT>=d b^2-O(L)sum delta_i. Central rows must hit each peripheral fibre; the logarithm of this hit factor is at most -L sum_{delta_i>0} B^delta_i/(2 ln B). This absorbs each positive linear deficit since K t-B^t/(2 ln B) is bounded above. Sum O(L^r) vectors for the upper logarithmic rate.

For the lower rate use balanced peripheral fibres of size a=ceil b. Their number N has log_B N=r b^2+O(L). For any fixed map the full success probability is at least c_m rho^(q a^2), c_m=exp(-2(r+1)L), by independence of forbidden rectangles and required-hit row blocks. If k_i vertices of first peripheral fibre i lie outside a second map's peripheral support, the forbidden rectangle ij loses at least a(k_i+k_j)/2 coordinates. Hence the union of forbidden sets has size >=q a^2+a k with k=sum k_i. Count at most binom(ra,k)binom(m-ra,k)r^(ra) second maps per k. The sum of their joint probabilities is at most rho^(q a^2)(2r)^(ra) exp(m rho^a), and m rho^a<=L. Cauchy-Schwarz gives a lower bound with log_B at least -d b^2-O(L).

In the critical case q=r all incidence degrees are two. Orient the degree-two undirected multigraph of missing arrows cyclically component by component; loops and double edges are allowed. This produces a permutation sigma with Q=sum a_i a_sigma(i). With lambda_i=m rho^a_i, the main-range selected expectation is at most (1+o(1)) times the sum of prod_i pi_{lambda_sigma(i)}(a_i), where pi_lambda(k)=e^(-lambda)lambda^k/k!. By Stirling, if any normalized mean lies outside [1/2,2], that term is exponentially small in L. Otherwise every a_i=b+O(1), leaving O(1) integer vectors, each O(L^(-r/2)). The discarded tails remain negligible. This proves the critical bound. QED.

For r=1 the missing peripheral loop satisfies both hypotheses; its image probability is O(L^(-1/2)). The loopless and reciprocal-gap cases are also covered at the level of existence probability, since the only universal incoming column is the center and every peripheral incidence degree is at least two. Their unrestricted first-moment and resonance results are not needed here.

## 4. Positive criterion

**Theorem 3 (complete-core signatures).** Suppose the target admits a partition U,S with U nonempty and complete reflexive, such that every subset J of S is the outgoing S-neighborhood of some u_J in U that receives all S arrows. Then at every fixed bias p_m(F)>=1-exp(-c m) for some c>0 and sufficiently large m.

**Proof.** If S is empty a balanced deterministic partition suffices by union bound. Otherwise choose singleton S-fibres in a fixed reserve W of half the source vertices: examine disjoint ordered tuples until one realizes the induced S-relation. This succeeds with exponentially high probability. For every nonselected vertex x record its outgoing and incoming signatures relative to the selected tuple, J(x) and I(x). Outside W all 4^|S| exact signature pairs occur linearly many times, except with exponentially small probability. Allocate a disjoint linear-size group of exact signatures (J_u,I_u) to each u in U, splitting groups as needed. Assign all leftover vertices of signature J to u_J, which accepts every incoming signature. The exact groups guarantee each required S-to-U hit and exclude every forbidden one.

Conditional on the tuple tests (inside W) and signature exposures (incident to the selected tuple), all edges from nonselected rows to vertices outside W are fresh: none of these coordinates was tested. Every U-fibre has a linear-size part outside W, so all U-to-U hits hold with exponentially high probability by union bound. Tuple tests handle S-to-S; signatures handle U-to-S and S-to-U. This produces a full surjective bounded morphism. QED.

## 5. Exceptional targets

Five four-point canonical targets have neither a smaller vanishing quotient nor a classification by Theorems 2–3. We prove their limits below. In the first two cases the displayed bounds need not be sharp.

### 5.1. Forced independent fibres: 001011101 and 001101011

Relabel the two negative targets as c,A,B,Z with c universal, both c and Z universal incoming, and Z missing only its outgoing arrow to A. For 001011101 use A=old peripheral 2, B=old peripheral 1, Z=old peripheral 3; for 001101011 use A=old 1, B=old 2, Z=old 3. The missing outgoing destinations are:

    canonical      A     B     Z
    001011101      B     A,B   A
    001101011      A,B   B     A

The labels c and Z both hit B; A and B both miss B. Thus for any full successful map, the B-fibre is independent (all internal ordered edges absent), and the A-fibre is exactly the set of vertices outside B that have no outgoing edge into B. In particular after fixing B there is no arbitrary choice of A. Other necessary constraints differ between the two targets.

Write a=|A|, b=|B|, z=|Z|. The same rectangle and witness argument as the tiny-fibre argument in Theorem 2 applies to any particular label i for which no universal-incoming label misses exactly i. It does not require the global degree hypothesis for this restricted conclusion. Here i=B has that property. Taking h=ceil(128 L), the probability of existence with b<b0=L-3 log_B L is bounded by

    B^(2hL-h^2)+exp(-Omega(L^3)).

Indeed on the no-empty-h-rectangle event, large labels form a complete relation. Enumerate all small fibres, and test an outside vertex missing exactly B among small fibres and receiving a hit from each of them. It would require a universal-incoming label missing exactly B, impossible. For fixed small fibres the independent tests over outside vertices succeed with probability >=rho^b*theta^7 (or a larger constant), yielding the bound after union over B^O(L^2) choices. The argument uses unconditional tests and an event implication, not independence conditional on the rectangle event.

Also b<h on the no-empty-rectangle event since B is independent. In the second target A is independent too, so a<h there. All rectangle and tiny-b errors are negligible relative to the claimed bounds.

For a fixed B of size b, let q_b=rho^b, lambda=m q_b. Its internal forbidden coordinates have probability rho^(b^2). The A-fibre forced by B is formed by independent tests on rows outside B with probability q_b; these tests are independent of internal B coordinates. Thus its size has distribution Bin(m-b,q_b) conditional on B independence.

#### 5.1.1. Target 001011101

The B-to-A rectangle must be entirely absent as well. Conditional on the tests defining A, these ordered coordinates are fresh, so the additional probability is rho^(ab)=q_b^a. Dropping all other conditions, including nonemptiness of A, the expected number of candidate B-sets of size b is at most

    binom(m,b) rho^(b^2) (1-q_b+q_b^2)^(m-b).

This is the binomial theorem after weighting the forced A-set by q_b^a. For b0<=b<h, q_b<=L^3/m. The expression is bounded by

    (lambda^b/b!) exp(-(m-b)*q_b*(1-q_b))
       <= exp(O(L^6/m)) pi_lambda(b),

where pi_l(k)=exp(-l)l^k/k!, using b=O(L). For the normalized means t_b=lambda/b, the successive ratio is rho*b/(b+1)<rho. Thus O_theta(1) indices have t_b in [1/2,2], and Stirling bounds each mass by O(L^(-1/2)) there. All other O(L) indices contribute exp(-Omega(L)) since t-1-ln t has positive lower bound outside that interval and b>=L/2. Summing and adding negligible exceptions proves p_m=O(L^(-1/2)).

#### 5.1.2. Target 001101011

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

### 5.2. A dominating reserve for a one-row forbidden star: 100111111

For any fixed k>=1 let F_k have labels c,Z,A_1,...,A_k. All arrows are present except the k arrows Z->A_i. (All loops are present.) We show p_m(F_k)->1, which covers 100111111 at k=2.

Theorem 3 does not apply for k>=2: among the universal incoming labels only c and Z realize signatures, and these give only the all-hit and all-miss patterns on the k exceptional destinations. Instead choose a moderately small universally hit fibre Z, and make the other k fibres sufficiently large that accidental misses outside Z are rare.

#### 5.2.1. A small out-dominating destination set

Take a deterministic reserve W of floor(m/2) vertices and t=ceil(L-(3/2)log_B L). We claim that with probability 1-o(1) there is a t-subset D of W hit by every source row (including rows in D). This choice is measurable using only edges ending in W.

Let X count such t-subsets, q=rho^t, N=|W|, and P0=(1-q)^m the success probability of each fixed D. Then E[X]=binom(N,t)P0>0. For two t-subsets with intersection size j, the probability of both hits in each row is 1-2q+rho^(2t-j), so the ratio of their joint success probability to P0^2 is

    [1+(rho^(2t-j)-q^2)/(1-q)^2]^m
        <=exp(4m*rho^(2t-j))

for large m. The formula follows from independence of rows and inclusion-exclusion for the two misses; it includes loops. For j<=t/2, the right side is 1+o(1) uniformly, since m*rho^(3t/2)<=m^(-1/2)*L^(9/4)->0. For j>t/2, the ratio is <=exp(4m q)<=exp(4L^(3/2)). For two independently uniform t-subsets of W, the probability of intersection >t/2 is bounded by

    2^t*(t/(N-t))^ceil(t/2)=exp(-Omega(L^2)).

Indeed fix the first set and union bound over subsets of ceil(t/2) of it; the probability any such subset lies in the second is (t)_ell/(N)_ell <=(t/(N-t))^ell. Therefore E[X^2]/E[X]^2<=1+o(1), with the high-overlap contribution negligible. Cauchy-Schwarz gives P(X>0)>=E[X]^2/E[X^2]=1-o(1). The event and a deterministic selected successful D depend only on edges ending in W.

#### 5.2.2. Construct all fibres using fresh edges

Set Z-fibre=D. Conditional on the edge information ending in W with successful D, expose the coordinates D x ([m] minus W), fresh under this history. Let M be the outside-W vertices receiving no outgoing edge from any row in D. Then |M| is Bin(m-N,q), because the column tests are independent. Its mean is of order L^(3/2), since rho*L^(3/2)<=m*q<=L^(3/2). Chernoff gives |M|>=k*ceil(2L) with probability tending to one. Choose disjoint A_i-fibres of size ceil(2L) deterministically from M. Assign all remaining vertices to c, except D. Thus all required forbidden blocks D x A_i are absent.

Every row hits D by the initial selection. Conditional on all history so far, the edges from rows outside D ending outside W are independent original Bernoulli bits: first-stage tests ended inside W; second-stage tests began in D; the chosen A_i and c-fibre depend only on those tests. Thus every row outside D hits every A_i except with probability at most mk*rho^ceil(2L)<=k/m. The outside-W portion of c has size m-N-k*ceil(2L)>=m/3 eventually. All rows outside D hit it except with probability at most m*rho^(m/3).

For rows in D, any outgoing edge to outside W must end in the c-fibre, because every A_i lies in M. The probability some D-row has no outgoing edge to outside W, conditional on the first-stage selection, is <=t*rho^(m-N), irrespective of the later choices. Hence all D-rows hit c with probability 1-o(1). All fibres are nonempty. Together with the hit to D and the forbidden-block condition, the exact successor-image equalities hold. This proves a.a.s. surjective bounded morphism onto F_k for every fixed k.

This argument uses a dominating destination set of size L-(3/2)log_B L, not an assertion that a deterministic such set already dominates. The second moment is essential. No exponential failure rate for F_k is claimed.

### 5.3. Two-stage forced fibres: 011011101

Let F have universal reflexive center c and peripheral relation 011011101 in row-major order. Relabel A=old peripheral 2, B=old peripheral 1, Z=old peripheral 3. Its only missing arrows are A->B, B->B, Z->A. All other ordered edges are present.

For independent source edge probability theta with 0<theta<1-e^(-1), including loops, write rho=1-theta, Bbase=1/rho and L=log_Bbase m. Then

    P(G_m ->> F) -> 1.

In particular this holds for theta=1/2. For theta>=1-e^(-1) the proof below gives no conclusion; do not infer a zero limit.

#### 5.3.1. Independent sets at an appropriate integer scale

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

#### 5.3.2. Complete a fixed independent B-fibre with high conditional probability

Fix one b-subset V and condition only on its internal independence. Define A as all outside vertices missing V by outgoing edges. Conditional on independence, |A| has Bin(m-b,q) distribution, using disjoint coordinates outside V x V. By Chernoff and the strict margins above, except with probability o(1),

    alpha*L <= |A| <= beta*L.

This forces nonempty A. The V-fibre misses itself, A misses V, and every other row hits V, by construction.

Now reveal all edges ending in A. Conditional on the previous history of edges ending in V, these are fresh independent bits, because A is determined by that history and disjoint from V. The probability that some row in A or V misses A is <=(|A|+b)*rho^|A|=o(1) uniformly on the size event. Define Z as the set of all rows outside A union V that miss A. Conditional on the preceding V-column history (before exposing A columns), |Z| is binomial with parameters m-|A|-b and rho^|A|. It is of mean at least (m-O(L))*m^(-beta), and at most m*m^(-alpha). Chernoff for the lower bound and Markov for the upper bound imply, except with probability o(1),

    |Z| >= m^(1-beta)/3, |Z| <= m/4.

The row-hit event for A and V need not be assumed independent of the Z-size event; a union bound suffices. On both events, the rows missing A are exactly Z. Define C as all remaining vertices, so |C|>=m/2 for large m. Both Z and C are disjoint from A,V and their choice is measurable in the exposed V and A column history.

For clarity about adaptive exposure: for fixed V, first reveal all columns ending in V, which determine A. Conditional on those columns, reveal all columns ending in the resulting A. For each realization, the remaining columns ending outside V union A are disjoint fresh coordinates under the product law. The sets Z,C are functions only of the revealed history. Consequently, conditional on the size bounds, the probability any row misses Z or C is <=m*(rho^(m^(1-beta)/3)+rho^(m/2))=o(1).

All rows therefore hit Z and C, precisely the required universal columns. The B-hit status is absent exactly in A and V; the A-hit status is absent exactly in Z. With V as the B-fibre, these are the exact target successor images. All four fibres are nonempty, so the map is a surjective bounded morphism. The conditional probability of failure of this completion for any fixed independent V is o(1), uniformly in V.

#### 5.3.3. Avoid adaptive-choice bias by counting bad independent sets

Let X_bad count independent b-subsets V for which the deterministic completion rule above fails to produce a surjective bounded morphism. The conditional estimates for each fixed V give E[X_bad]=o(E[X]) by linearity; no independence across different V is needed. Markov yields X_bad<E[X]/2 with probability 1-o(1). Section 1 gives X>=E[X]/2 with probability 1-o(1), so with probability tending to one at least one independent V has a successful completion. We do not select an independent set using arbitrary edge information and then assume its external edges remain fresh. This counting argument proves the theorem.

### 5.4. Exact forced-pair second moment: 011010111

The last target has peripheral labels A=1, Z=2, M=3; the only absent arrows are A->A, Z->A, Z->M. The remaining label C is the universal center. In the following argument the edge probability is 1/2, rho=1/2, and L=log_2 m. Temporarily write B for the fibre assigned to target label M, and M for the full set of common nonneighbors in the first reduction.

#### 5.4.1. Necessary witness and deterministic completion

For a successful surjective bounded morphism, A is independent, and the set of rows outside A missing A is exactly Z. Every row hits Z. For fixed disjoint nonempty A,Z, put

    M={y outside A union Z: no row in Z has an edge to y},
    C0=[m] minus (A union Z union M).

Then B is a nonempty subset of M, and every row outside Z must hit M. In particular M nonempty is necessary. These conditions give a necessary witness depending on the pair A,Z, with Z uniquely determined by A.

A sufficient witness is obtained by using B=M and C=C0: additionally require C0 nonempty and every row to hit C0. Then all four labels have exactly the successor images dictated by the missing arrows. Any row in Z misses A and M, every other row except A hits A, and A misses A by independence. Every non-Z row hits M, and all rows hit Z,C0. This is exactly a surjective bounded morphism.

The necessary witness does not automatically give the sufficient witness: enlarging B to M might remove some of the original C successors. We therefore keep distinct counts Y_necess and Y_suff, for which

    P(Y_suff>0)<=p_m<=P(Y_necess>0)<=E[Y_necess].

#### 5.4.2. Exact expectations

Let a=|A|, z=|Z|, n=m-a-z. For each fixed disjoint A,Z with a,z>=1, n>=1, the probability of independence of A, the exact definition of Z, and every row hitting Z is

    H(a,z)=rho^(a^2+a*z)*(1-rho^a)^n*(1-rho^z)^m.

These events use only columns ending in A or Z. The remaining coordinates Z x ([m] minus (A union Z)) are independent and make |M| distributed as Bin(n,rho^z). Conditional on M and the Z-row column tests, the edges from rows outside Z to M are fresh; the probability all these rows hit M is (1-rho^k)^(m-z) when k=|M|.

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

Indeed, all rows outside Z must hit C0, using fresh disjoint row/fibre blocks. For Z rows, conditional on M, each C0 column has a nonempty vector of edges from Z, independent across those columns. For a specified j rows of Z the probability all j rows miss one such column is (rho^j-rho^z)/(1-rho^z), because the column is required nonempty. Inclusion-exclusion over Z rows failing to hit C0 gives J. Alternatively 1-z*rho^c<=J<=1 by the union bound, since the conditional miss probability for any one row is <=rho^c per column.

There are binom(m,a)binom(m-a,z) pairs. Linearity of expectation suffices; no assumption of independence between pairs is made. These exact formulas are counts of pair witnesses, not counts of arbitrary full maps.

#### 5.4.3. Choice of sizes and first moment

Choose

    a=round(L-log_2 L-1), z=a+2,
    k=ceil(L+2 log_2 L), c=m-a-z-k.

Let Y count sufficient witnesses with precisely these sizes, and Y0 the necessary ones. Define t=m*2^(-a)/L, so sqrt(2)<=t<=2sqrt(2); m*2^(-z)/L=t/4.

For fixed disjoint A,Z, with n=m-a-z, the formula in Section 5.4.2 is

    P(A,Z are sufficient, |M|=k)
     = rho^(a^2+az)*(1-rho^a)^n*(1-rho^z)^m
       * binom(n,k)*rho^(zk)*(1-rho^z)^(n-k)
       * (1-rho^k)^(m-z)*(1-rho^c)^(m-z)*J(z,c),

where J is the conditional probability every Z row hits C. It satisfies 1-z*rho^c<=J<=1. Multiply by binom(m,a)binom(m-a,z). Each A determines Z and M uniquely, so this counts at most one witness per A.

Let lambda_a=m*rho^a=t L and lambda_z=m*rho^z=t L/4. Since a,z,k=L+O(log L), the falling factorial estimates and log(1-x)=-x+O(x^2) imply, uniformly in the chosen sizes,

    E[Y]=(1+o(1))*(lambda_a^a/a!)*(lambda_a^z/z!)
                      * exp(-lambda_a-lambda_z)
                      * pi_{lambda_z}(k),

where pi_l(k)=exp(-l)*l^k/k!. The relative errors in the multinomial and binomial approximations are O(L^2/m): for the latter, n=m-O(L), k=O(L), and rho^z=O(L/m). Also m*rho^k<=L^(-2); hence the M-hit factor tends to 1, the C-hit factors and J do as well because c=m-O(L). These estimates apply to both necessary and sufficient restricted expectations.

For x in a fixed compact positive interval and u=L+O(log L), Stirling's formula gives

    ln((x L)^u/u!)=L*(1+ln x)+O(log L)

uniformly. Substitution yields

    ln E[Y]=L*(3+2 ln t+ln(t/4)-t-2*(t/4))+O(log L)
           =L*f(t)+O(log L).

The function f is concave (f''=-3/t^2), so its minimum on [sqrt(2),2sqrt(2)] is at an endpoint. The values are 3-0.5 ln 2-3 sqrt(2)/2 and 3+2.5 ln 2-3 sqrt(2), respectively; both exceed 0.48. Thus E[Y]>=exp(0.47 L) for sufficiently large m. The restricted necessary and sufficient expectations have ratio tending to one, because the extra C-hit factors tend uniformly to one.

#### 5.4.4. Set-up for the second moment

For target 011010111 relabel vertices C,A,Z,M, where C is universal and the only forbidden arrows are A->A, Z->A, Z->M. Put L=log_2 m, rho=1/2, and choose

    a=round(L-log_2 L-1), z=a+2, k=ceil(L+2 log_2 L),
    s=a+z+k, c=m-s.

Then the probability p_m of a surjective bounded morphism onto this target tends to one.

Use the necessary exact-M witness count Y0 of Sections 5.4.2–5.4.3 at precisely these sizes. A triple T=(A,Z,M) is three disjoint vertex sets of sizes a,z,k. C is the complement. Write E_T for the following event:

- A x A, Z x A, Z x M are entirely absent.
- Every row outside A union Z hits A.
- Every row hits Z.
- Every row outside Z hits M.
- Each column in C receives at least one edge from Z.

The forbidden Z-to-M rectangle and the C-column hit requirement make M precisely the common nonneighbors of Z outside A union Z; likewise Z is exactly the set of outside-A rows missing A. Hence for each A there is at most one successful triple. All the specified forbidden rectangles and the individual row/column hit blocks are mutually disjoint coordinate sets. In particular their probabilities multiply. The forbidden set H_T has size Q=a^2+za+zk, the same for every triple. Write P=P(E_T)=rho^Q times the hit factor R. The hit factor satisfies R=exp(-O(L)), since rho^a,rho^z=Theta(L/m), rho^k<=1/(m L^2), and there are O(m) requirements. Let N=(m)_s/(a!z!k!) be the number of triples.

Section 5.4.3 shows E[Y0]=NP>=exp(0.47 L) for sufficiently large m (E[Y]/E[Y0]=1+o(1), where Y additionally requires every row to hit C). We prove E[Y0^2]/E[Y0]^2=1+o(1). Then concentration and Markov on Y0-Y give Y>0 a.a.s., hence p_m->1.

#### 5.4.5. Small support overlap: h<=L/2

For two triples T,T' let S=A union Z union M, S'=A' union Z' union M', h=|S intersect S'|, and I=|H_T intersect H_T'|. The joint absence probability is rho^(2Q-I). All forbidden coordinates lie inside (S union S') squared.

For an upper bound on the joint event, retain only hit requirements for rows outside S union S' and for columns outside S union S'. More precisely, each such outside row must hit all six blocks A,Z,M,A',Z',M', and each outside column must receive an edge from both Z and Z'. These row tests and column tests use disjoint families of coordinates, also disjoint from the forbidden coordinates. Different rows are independent, and different columns are independent.

Let ell=min(a,z,k)=L-O(log L). For a given outside row, the probability of missing any one of its six blocks is rho^size. For any pair of these misses the joint probability is <=rho^(2ell-h), since the two blocks overlap in at most h vertices (within one triple they are disjoint). By the two-term Bonferroni bound, the probability of all six hits is at most 1-sum of single miss probabilities +15*rho^(2ell-h). The product of the six single hit probabilities is at least 1-sum of single miss probabilities, and tends uniformly to one. Consequently the ratio of the joint row probability to that product is <=1+O(rho^(2ell-h)). For an outside column the two hit tests from Z,Z' satisfy the same bound by inclusion-exclusion. Thus over at most 2m outside rows and columns the product of these ratios is <=exp(O(m*rho^(2ell-h)))=1+o(1) uniformly for h<=L/2.

In each individual E_T (and E_T') all the original hit blocks are independent. The requirements dropped in this upper bound number O(s) per event: they are row hits for rows in the union of supports and column hits for columns in that union. Their product of probabilities is 1-o(1), because each miss has probability <=rho^ell=O(L/m). Therefore uniformly for h<=L/2,

    P(E_T and E_T') / P^2 <= (1+o(1))*rho^(-I).

For h=0, this is <=1+o(1). For h>=1, I<=h^2 because every common forbidden coordinate has both endpoints in the intersection of supports. For uniformly independent triples, their supports are uniformly independent s-subsets. By the union bound for containment of specified h vertices,

    P(|S intersect S'|=h) <= binom(s,h)*(s/(m-s))^h
                            <= (s^2/(m-s))^h.

For 1<=h<=L/2, the product of this bound and 2^(h^2) is at most (s^2*2^(L/2)/(m-s))^h. The base tends to zero, and the geometric series over positive h is o(1). Hence all pairs with h<=L/2 contribute at most (1+o(1))*E[Y0]^2.

#### 5.4.6. Large overlaps with a deficit

Let D=max(a,z,k)=L+O(log L). Write x=|A intersect S'|, y=|Z intersect S'|, w=|M intersect S'|, so x+y+w=h. Restrict H_T to (S intersect S') squared. Its size is exactly x^2+yx+yw, so

    I <= x^2+yx+yw <= D h,
    D h-I >= x(D-x)+y(D-x)+w(D-y).

The same statements hold on exchanging T,T'. Denote the deficit D h-I by Delta.

For arbitrary pairs, dropping all hits gives the crude ratio P(E_T and E_T')/P^2 <=rho^(-I)*R^(-2)=2^(I+O(L)), uniformly. The support intersection counting bound above gives, for any h>=1,

    P(|S intersect S'|=h) <= 2^(-L h+O(h log L)).

Here s=O(L). Therefore pairs with h>L/2 and Delta>=K L log_2 L contribute o(E[Y0]^2), for any sufficiently large fixed K. Indeed I=D h-Delta, (D-L)h=O(L log L), and one can choose K strictly larger than the fixed constants in all O(L log L) upper bounds, so the normalized sum over O(L) sizes is at most O(L)*2^(-L log_2 L) eventually. No independence of these pairs is assumed.

#### 5.4.7. Structural lemma for the remaining large overlaps

Suppose h>L/2 and Delta<K L log_2 L. Then x>=D-O(log L). To prove this, if x<=D/2 the displayed deficit inequality gives x+y<=2 Delta/D=O(log L), and subsequently w<=Delta/(D-y)=O(log L). This contradicts h>L/2. Thus x>D/2, and x(D-x)<=Delta implies D-x<=2 Delta/D=O(log L). In particular a-x=O(log L).

We need alignment of the A labels, not merely overlap of supports. Let

    u=|A intersect A'|, v=|A intersect Z'|, r=|A intersect M'|,

so u+v+r=x. Every coordinate in (A intersect Z') squared and in (A intersect M') squared belongs to H_T restricted to the common support but not H_T', because Z' and M' are reflexive target labels. These two sets are disjoint. Their total v^2+r^2 is bounded by the lost coordinates x^2+yx+yw-I, which is at most Delta. Hence v+r=O(sqrt(L log L)), implying u=x-v-r>=L/2 eventually. Further, all coordinates from A intersect A' to A intersect (Z' union M') are forbidden by T but not by T', as A' forbids only arrows to A'. Thus u(v+r)<=Delta, implying v+r=O(log L). It follows that

    d=|A minus A'|=a-u=O(log L).

All constants are uniform in the pairs, depending only on the fixed K and the chosen sizes. Fix K1 such that d<=K1 log_2 L for all these pairs and large m.

#### 5.4.8. Conditional bound for near-identical A sets

Fix T and condition on E_T. Since the event is a conjunction of disjoint coordinate-block constraints, these blocks remain independent conditional on E_T; untested coordinates remain fresh. Within a row-hit block conditioned to contain at least one present edge, the probability that any specified subset of b coordinates is absent is <=rho^b, since its exact probability is rho^b*(1-rho^(blocksize-b))/(1-rho^blocksize). This also covers a whole block (probability zero).

For A' of size a with d=|A minus A'|>=1, write F=A intersect A' (size a-d) and G=A' minus A (size d). Let e=|G intersect Z|. Independence of A' requires all F x G and G x F coordinates absent. Conditional on E_T:

- For rows in F (subset of A), edges to G lie in hit blocks into Z and M, and unrestricted coordinates into C. All these blocks are disjoint, so probability of absence of all F x G is <=rho^((a-d)d).
- For rows in G outside Z, these rows are outside A union Z, and their edges into A are conditioned to hit A. Probability of absence of their edges into F is <=rho^((a-d)(d-e)).
- Rows in G intersect Z already miss A. The coordinate blocks used in the first two items are distinct even though their endpoints may overlap: the former have source in A and destination outside A, the latter source outside A and destination in A. No column constraint from Z to C intersects either group (source in the former is A; destination in the latter is A).

It follows that P(A' independent | E_T)<=rho^((a-d)(2d-e)). We have ignored other constraints on A' and thus obtained an upper bound.

Sum this bound over all A' with 1<=d<=K1 log_2 L. For each d,e, at most binom(a,d)binom(z,e)binom(m-a-z,d-e) choices. Using binom(n,j)<=n^j and the binomial theorem (whose coefficients are >=1), the sum for a fixed d is bounded by

    [a*rho^(a-d)*(z+m*rho^(a-d))]^d.

Uniformly for d<=K1 log_2 L, rho^(a-d)<=O(L^(K1+1)/m), so the base is bounded by a fixed power of L divided by m, tending to zero. Sum the geometric series: conditional on any E_T, the expected number of *other* independent A' within this distance is o(1). Since a successful triple T' is uniquely determined by its A', the expected number of other successful triples in this range is likewise o(1). The d=0 case has at most one successful triple, namely T itself. Thus all remaining large-overlap pairs contribute at most

    (1+o(1))*sum_T P(E_T)=(1+o(1))*E[Y0]=o(E[Y0]^2).

This conditional calculation is the essential improvement over bounding the entire second moment by the independent-set count. It uses only the exact block law given the first witness, not an unjustified independence of adaptively selected sets.

#### 5.4.9. Conclusion

Sections 5.4.5–5.4.8 exhaust all ordered pairs. They show E[Y0^2]<=(1+o(1))*E[Y0]^2; the reverse asymptotic lower bound follows from variance nonnegativity. Chebyshev gives Y0>=E[Y0]/2 a.a.s. From the preceding fixed-size first moment, E[Y0-Y]=o(E[Y0]) because the added C hits fail with probability o(1) given E_T (uniformly, with c=m-O(L)). Markov gives Y0-Y<E[Y0]/2 a.a.s. Consequently Y>0 a.a.s.; a sufficient witness yields the desired surjective bounded morphism.

Thus p_m(F011010111)->1 in the fair model. QED.

## 6. Exhaustive classification

### 6.1. One, two and three vertices

The singleton is reflexive and the source is serial with probability at least 1-m*rho^m. The two-point target with peripheral loop is complete and satisfies Theorem 3. The other two-point target (encoding 0, denoted K2) satisfies Theorem 2 with r=1,d=0. Its only proper quotient is the reflexive singleton, so K2 is minimal.

For three vertices the ten canonical peripheral encodings and their proper two-point images are as follows. T2 denotes the complete two-point target. The singleton is always a quotient by seriality.

| encoding | two-point images | limit | proof |
|---|---|---:|---|
| 0000 | K2 | 0 | quotient |
| 0001 | none | 0 | Theorem 2 |
| 0010 | K2 | 0 | quotient |
| 0011 | K2 | 0 | quotient |
| 0101 | T2 | 1 | Theorem 3 |
| 0110 | K2,T2 | 0 | quotient |
| 0111 | K2,T2 | 0 | quotient |
| 1001 | T2 | 0 | Theorem 2 |
| 1011 | T2 | 1 | Theorem 3 |
| 1111 | T2 | 1 | Theorem 3 |

Each image is found by the three nontrivial bipartitions of the vertex set. The only two minimal vanishing types are 0001 and 1001. The five labelled positive matrices are 0101,1010,1011,1101,1111; all other eleven labelled matrices vanish.

### 6.2. Four vertices and reproducible enumeration

Burnside's lemma gives the isomorphism counts directly. On the four ordered pairs of two peripherals the transposition has two orbits, so the three-point count is (16+4)/2=10. On nine ordered pairs of three peripherals each transposition has five orbits and each 3-cycle three orbits. The four-point count is therefore (512+3*32+2*8)/6=104. The equivalence between marked and unmarked classes was proved in Section 2.

For four points the 12 positive canonical encodings are

    001011011 001111011 011010111 011011011
    011011101 011011111 100111111 101011011
    101110111 101111101 101111111 111111111

Of the other 92, exactly the following 22 are minimal (20 are covered by Theorem 2; two starred encodings by Section 5.1):

    000010100 000010101 000011100 000011101
    001001001 001010010 001010011 001011001
    001011101* 001100010 001100011 001101001
    001101011* 001110001 001110011 001111001
    011010011 011010110 100011101 100110101
    100110111 101110011

The remaining 70 all map onto a smaller vanishing target. Here is a complete finite enumeration procedure; a canonical encoding is taken with the distinguished central point omitted. A quotient of a central frame remains central: surjectivity and forth imply all arrows to and from the image of the center.

```text
Z3 = {0000,0001,0010,0011,0100,0110,0111,
      1000,1001,1100,1110}
F = empty dictionary
for bits in {0,1}^9:
    R = 4 by 4 matrix with row 0 and column 0 all 1
    fill remaining entries with bits, in row-major order
    key = minimum peripheral encoding over all 6 permutations
    inherited = false
    for k in {2,3}:
        for each surjection f: {0,1,2,3} -> {0,...,k-1}:
            Q = zero k by k matrix
            for each i,j with R[i,j]=1: Q[f(i),f(j)]=1
            if exists i,v with Q[f(i),v]=1
               but no j with R[i,j]=1 and f(j)=v: continue
            code = peripheral encoding of Q omitting f(0)
            if (k=2 and code=0) or (k=3 and code in Z3):
                inherited = true
    degree = every peripheral missing incidence degree >=2
             and no label with universal incoming column has one missing outgoing arrow
    core = false
    for S subset of {1,2,3}:
        U = {0,1,2,3} minus S
        if U induces a complete relation:
            J = {outgoing S-neighborhood of u:
                 u in U and every j in S has j->u}
            core = core or (|J|=2^|S|)
    if inherited: category = inherited-zero
    else if degree: category = Theorem 2
    else if core: category = Theorem 3
    else if key in {001011101,001101011}: category = Section 5.1
    else if key in {100111111,011011101,011010111}:
         category = Sections 5.2-5.4
    else: fail (unclassified)
    assert existing category of key, if any, equals category
    increment multiplicity of key and store category
```

The explicit construction of Q is forced by surjectivity and the two bounded-morphism conditions: every source arrow gives a target arrow, and each target arrow has a source witness at every vertex of its preimage. Thus the displayed back test is exact. All surjections are included; equivalently one could enumerate the 13 partitions into two or three blocks and test equality of successor-block sets. The table of counts by proof method is

| method | isomorphism classes | labelled matrices (central label fixed) |
|---|---:|---:|
| smaller vanishing quotient | 70 | 339 |
| Theorem 2 | 20 | 103 |
| forced negative cases | 2 | 12 |
| Theorem 3 | 9 | 43 |
| remaining positive cases | 3 | 15 |
| total | 104 | 512 |

There are 454 labelled negative and 58 labelled positive matrices, with central label fixed. These are not counts of all labelled central frames with the center unspecified. The Python reproducibility script [four_point_census.py](../experiments/four_point_census.py) uses a finer partition of proof methods. For each of the 104 canonical encodings the accompanying [classification certificate](four_point_classification.csv) records its orbit size, limit, minimality status and proof method. Each of the 70 inherited-zero classes includes an explicit surjection onto one of the smaller minimal vanishing targets (0, 0001, or 1001); all 70 such certificates have been checked by direct successor-image equality. The separate checker [verify_paper_certificate.py](../experiments/verify_paper_certificate.py) verifies the finite certificates and exhaustively excludes smaller minimal images for the other classes. The asymptotic limits are supplied by the proofs above, not by the finite checker. The independent audit checked all 24 permutations (not just the six peripheral permutations) and all 25,600 labelled surjections to 2- or 3-point sets for the 512 matrices. The two algorithms agree.

## 7. Modal consequences and independence

Let p_i be distinct propositional variables indexed by the vertices i of F. In the modal language with universal modality [U] and its dual <U>, define

    Delta_F =
      (AND_i <U> p_i)
      AND (OR_i p_i)
      AND (AND_{i<j} NOT(p_i AND p_j))
      AND (AND_{i R j} (p_i -> diamond p_j))
      AND (AND_{not i R j} (p_i -> box NOT p_j)).

    chi_F = NOT [U] Delta_F.

The global existence and partition clauses define a surjective label map. The required diamond clauses are back and the forbidden box clauses are forth. Hence a valuation falsifying chi_F exists exactly when the full source frame admits a surjective bounded morphism onto F; the converse follows by pulling each label back to its fibre. This definition is equivalent to the characteristic-formula convention in [2, Definition 2.2 and Lemmas 2.3–2.4]. No generated-subframe restriction is needed.

Write chi_F^d for the ordinary-modal translation [U]=box box and <U>=diamond diamond. On frames with universal R^2 this translation is exact by induction on formula complexity. For random G_m,

    Pr(R^2 not universal)<=m^2(1-theta^2)^(m-2).

For a fixed ordered pair (x,y), the two edges through each intermediate vertex outside {x,y} are distinct, independent, and disjoint across intermediates, including when x=y. Each path succeeds with probability theta^2. Union over the m^2 ordered pairs proves the bound. Thus Pr(G_m validates chi_F^d) differs from 1-p_m(F) by at most the displayed error.

By [2, Proposition 3.5], all finite central targets validate ML^r. For any almost-surely valid formula phi and target F with p_m(F)->1, F must validate phi: otherwise each source with a bounded morphism onto F would falsify phi by preservation of frame validity, contradicting almost-sure validity. Conversely p_m(F)->0 makes chi_F^d almost surely valid and false in F. Therefore the 1,1,3,12 positive central types on one through four vertices are exactly the finite models of ML^as in these sizes within the central class (and noncentral finite frames cannot validate ML^r). This strengthens the characteristic-formula census to a finite-model census in these sizes only.

There are 25 minimal vanishing types on at most four points. For distinct minimal types F,H, no surjective bounded morphism F->H exists, by minimality if H is smaller, impossibility of surjection if H is larger, and bijective bounded morphism implying isomorphism if sizes agree. Every F thus validates ML^r and all the other minimal types' translated characteristic formulas, but falsifies its own. Normal modal soundness proves mutual independence of these 25 axiom schemes over ML^r. This is not an axiomatization of all ML^as.

### 7.1. A prime-cycle family

For r>=2 let C_r consist of a universal reflexive central vertex c and r peripheral vertices i in Z/rZ, each with exactly two successors c and i+1. Let T2=C_1 be the complete reflexive two-point frame, E1 the reflexive singleton, and K2 the two-point target with absent peripheral loop.

#### Quotient classification for central cycles

The surjective bounded-morphic images of C_r, up to isomorphism, are exactly E_1, C_d for positive divisors d of r, and K_2 if r is even.

Proof. Given a surjective bounded morphism f, write z=f(c). It is central, since c has all incoming and outgoing arrows. For each peripheral i, the set of successors of f(i) is exactly {z,f(i+1)}, by forth and back. If f(i)=z for some i, the target has at most two vertices, since the successor set of z is the whole target. In the singleton case the target is E_1. In the two-point case write w for the other point. The central row is universal, so only the loop of w is optional. If w has a loop, all source peripheral rows must hit w, implying f(i+1)=w for every i. Thus every peripheral maps to w and none maps to z, contradicting this case. If w has no loop, then every peripheral i must satisfy f(i+1)=w exactly when f(i)=z, and f(i+1)=z exactly when f(i)=w. This is an alternating colouring, possible precisely when r is even. Conversely the alternating colouring and f(c)=z give a bounded morphism onto K_2 for even r, as the successor sets directly verify.

Now suppose no peripheral maps to z. Every other target vertex u has successor set {z,s(u)} for a uniquely determined noncentral vertex s(u), because it is f(i) for some i, and f(i+1) is noncentral. The map s is well-defined by successor-image equality, and f(i+1)=s(f(i)). Its orbit from f(0) covers every noncentral target vertex by surjectivity, and s^r(f(0))=f(0). Hence this orbit is a cycle of length d dividing r, and the target is C_d. Conversely reduction of peripheral indices modulo any divisor d gives a surjective bounded morphism C_r->C_d, sending center to center. The map to E_1 exists by seriality. This proves the theorem.

For C_r, q=r^2-r, d=r(r-2), and both hypotheses of Theorem 2 hold. Hence p_m(C_r)->0 for all r>=2, with the critical bound O(L^(-1)) when r=2. An even r has the vanishing proper image K2, and an odd composite r has a smaller vanishing C_d. An odd prime r has only E1,T2 as proper images. Thus precisely the odd prime lengths yield minimal vanishing cycles, and their characteristic formulas are mutually independent by the same finite-countermodel argument.

Goranko [2, Proposition 4.7] already considers an infinite independent path family; infinitude is not claimed as novel here. Independence of characteristic formulas alone does not imply non-finite axiomatizability by arbitrary modal formulas.

## 8. Limitations, reproducibility and further work

The main census is proved for fair edges, not all fixed biases. In particular Sections 5.3 and 5.4 leave biases outside their stated ranges unresolved. All probability arguments are internal hand proofs, not formally verified or externally refereed. Finite scripts corroborate exact combinatorial counts but not asymptotic statements. Previously verified Lean modules concern smaller finite structural facts; the latest workflow-run query returned no runs and the newer chain modules have not been verified. Before a submission, typeset and compile the present integrated text, independently review the probability proofs, complete primary-source priority checks, and formally verify the finite census. No claim of the general zero-one law, complete axiomatization, or first discovery is made. Authorship and any required AI-use disclosure must be settled by the researcher before release.

## References

[1] V. Goranko and B. Kapron. The Modal Logic of the Countable Random Frame. Archive for Mathematical Logic 42 (2003), 221–243. https://doi.org/10.1007/s001530100135

[2] V. Goranko. The modal logic of almost sure frame validities in the finite. Advances in Modal Logic 13 (2020), 249–268. https://www.aiml.net/volumes/volume13/Goranko.pdf (mirror https://titan.dcs.bbk.ac.uk/volumes/volume13/Goranko.pdf).

[3] J.-M. Le Bars. The 0-1 law fails for frame satisfiability of propositional modal logic. LICS 2002, 225–234. https://doi.org/10.1109/LICS.2002.1029831

[4] R. F. Schamm. Zero-One Laws and Almost Sure Validities on Finite Structures. MSc short dissertation, Rand Afrikaans University, 2002. Sections 3.3.5–3.3.6; Figure 4.1; appendix. (The figure ordering has not been visually verified; do not claim a correction of a specific cell.)

[5] V. V. Sliusarev. Modal Logics of Almost Sure Validities and Zero-One Laws in Horn Classes. Doklady Mathematics 110 (2024), 442–449. https://doi.org/10.1134/S1064562424601446

[6] V. Sliusarev. Modal logics of almost sure validities in some classes of euclidean and transitive frames. https://arxiv.org/abs/2406.10770 (2024 preprint; later publication details to verify).

[7] V. V. Sliusarev. Modal Logic of Random Kripke Frames. PhD thesis, 2026. English summary (2025), https://www.hse.ru/data/2025/10/24/1949835949/2resume_en.pdf ; defence record https://www.hse.ru/sci/diss/1034821759 .

Further bibliography and evidence status: [RELATED_WORK](../docs/RELATED_WORK.md).
