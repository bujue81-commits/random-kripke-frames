# Bounded-Morphic Images of Random Kripke Frames: Complete Small-Frame Classification and Phase Transitions

**Working manuscript, version 0.4 — 26 November 2026.** Author and affiliation to be confirmed. This main text and its [numbered technical appendices](BIASED_PROOF_APPENDICES.md) constitute the integrated draft. Internal hand proofs, not independently refereed or Lean-verified. The fair-model manuscript remains archived unchanged. Priority and authorship are not asserted.

## Abstract

Let each ordered edge, including loops, of a labelled random finite Kripke frame occur independently with fixed probability theta in (0,1). We classify the existence probability of surjective bounded morphisms onto every central frame on at most four vertices. Of the 104 four-vertex central isomorphism types, 92 have probability tending to zero and ten have probability tending to one for every fixed bias. Two remaining types exhibit lattice-phase transitions: one changes from convergence to one to oscillation between zero and one, then to convergence to zero; the other changes from convergence to one to oscillation. Three explicitly characterized transition constants, approximately 0.74850236, 0.93132342 and 0.95096189, determine the complete classification, including critical endpoints. The proof combines forbidden-degree bounds, complete-core signatures, forced-fibre witness counts and overlap second moments. The resulting ordinary almost-sure modal logics have 12 four-point finite models below the largest transition and 11 at or above it. Their characteristic-formula independence counts on at most four vertices are respectively 25 and 26. In particular the high-bias almost-sure logic differs from the fair one. These are bounded-size classifications, not a general zero-one law or a complete axiomatization.

Keywords: modal logic; random directed graphs; bounded morphisms; characteristic formulas; lattice phases; first and second moments.

## 1. Introduction

Almost-sure frame validity differs substantially from almost-sure model validity. The latter is amenable to first-order zero-one laws, whereas validity under all valuations quantifies over subsets of the frame. Le Bars [3] disproved the general modal frame zero-one law. Goranko and Kapron [1] identified the logic ML^r of the countable random frame and its relation to almost-sure frame validity. Goranko [2, Sections 3–4] shows that finite models of ML^r are precisely finite frames with a central point and relates additional almost-sure validities to characteristic formulas of finite targets.

Schamm [4, Sections 3.3.5–3.3.6] considered the first moment of F-partitions and examined the 16 possible three-point central relations computationally. The present project uses this framework, distinguishes expectations from actual existence, and organizes rigorous candidate proofs for the three- and four-point classification. We do not claim that the partition method or the small-target enumeration originated here. Sliusarev [5–7] develops related classifications for restricted classes of random frames; their scope is not identical to unrestricted random relations. Priority of the particular asymptotic conclusions in this manuscript remains under investigation.

Le Bars's *A Sharp Threshold for a Non-monotone Digraph Property* [8, Section 2] studies fixed-bias kernel sizes on a logarithmic scale, using first and second moments and integer-size restrictions. Such methods and the possibility of nonconvergence are established precedents. Our candidate contribution is the specific complete small central-target classification and the precise transitions for the two forced-fibre targets, rather than the general method of lattice optimization or the discovery of frame-validity zero-one failure. Priority for these particular results is not yet established.

## 2. Setting and main theorem

Let F=(V,R) be a nonempty finite directed frame. A point c is central if cRv and vRc for every v in V (including c). For a source G=(W,S), a surjective function f:W->V is a bounded morphism if for each x in W,

    {f(y): x S y} = {v: f(x) R v}.

This is equivalent to the usual forth and back conditions. Denote the existence probability by p_m(F). Throughout fix 0<theta<1, rho=1-theta, B=1/rho, L=log_B m and b=L-log_B L.

Represent a central target with r peripheral labels (all labels other than the chosen center; some may themselves be central) by the r-by-r peripheral adjacency matrix written in row-major bit order. All arrows incident with the distinguished central label 0 are present. Take the lexicographically least encoding under simultaneous peripheral row/column permutation as canonical. This counts unpointed isomorphism classes: any isomorphism sends a central vertex to a central vertex, and any two central vertices can be exchanged by an automorphism, since both their rows and columns are universal.

**Theorem 1 (complete fixed-bias small central-frame classification).** Define the three constants

    theta_c = 1-r_c = 0.7485023647443824...,
    theta_0 = 1-1/(e T) = 0.9313234165433595...,
    theta_* = (9-3 sqrt(3))/4 = 0.950961894323342...,

where T>2 uniquely solves 2+2 ln T-T=0, and r_c is the unique root in (0.251,0.252) of

    3+3 ln u(r)+2 ln r-(1+2r^2)u(r)=0,
    u(r)=2 ln(1/r)/(1-r).

For one, two and three vertices, the numbers of central isomorphism types with p_m->0 and p_m->1 are respectively (0,1), (1,1), (7,3), for every fixed theta. Of the 104 four-point central types, 92 have p_m->0 and ten have p_m->1 at every fixed bias. The two exceptions have the following behavior:

| target | p_m->1 | liminf 0, limsup 1 | p_m->0 |
|---|---|---|---|
| 011010111 | 0<theta<theta_c | theta_c<=theta<theta_* | theta_*<=theta<1 |
| 011011101 | 0<theta<theta_0 | theta_0<=theta<1 | never |

In particular the four-point counts are:

| edge probability | zero limit | one limit | oscillatory |
|---|---:|---:|---:|
| 0<theta<theta_c | 92 | 12 | 0 |
| theta_c<=theta<theta_0 | 92 | 11 | 1 |
| theta_0<=theta<theta_* | 92 | 10 | 2 |
| theta_*<=theta<1 | 93 | 10 | 1 |

All intervals refer to fixed bias as m tends to infinity. The term oscillatory here means exactly liminf zero and limsup one, not periodic convergence at all finite sizes. The constants are specified by their exact definitions, not their decimal approximations.

**Proof strategy.** Composition propagates vanishing probability from a smaller quotient to a target: F ->> H implies p_m(F)<=p_m(H). Theorems 2 and 3 and Section 5.1–5.2 settle all other types except the two forced-fibre targets. Section 5.3 states their fixed-phase theorems; the numbered [technical appendices A–D](BIASED_PROOF_APPENDICES.md) contain the detailed proofs. Section 6 gives the finite orbit and quotient enumeration and identifies all types. Section 7 derives the logical consequences. No probability label is inferred solely from numerical experiments.

## 3. Vanishing criterion

For a central F with r peripherals put A_ij=1 if the peripheral arrow i->j is missing, 0 otherwise. Write q=sum A_ij and g_i=sum_j(A_ij+A_ji). A missing loop contributes twice to g_i.

**Theorem 2 (no singleton miss and degree).** Assume r>=1, every g_i>=2, and no label with a universal incoming column has exactly one missing outgoing arrow. Then d=q-r>=0 and

    log_B p_m(F) = -d b^2+O_F,theta(L).

When d=0, moreover p_m(F)=O(L^(-r/2)). In particular every such target vanishes. This holds at every fixed bias.

**Proof.** Fix a sufficiently large C depending only on r, and put h=ceil(C L), b0=L-3 log_B L. The probability of an empty ordered h-by-h rectangle is at most B^(2hL-h^2). Outside that event, the labels whose fibres have size >=h form a complete reflexive core U. Fix all the other small fibres, whose union has O(L) vertices. If fibre i has size <b0, a row outside the union which misses precisely i among the small fibres and receives an arrow from each small fibre would have a universally incoming target label missing precisely i, contrary to the hypothesis. These independent outside-row tests each succeed with probability >=rho^a_i theta^(2|S|-1), where S is the set of small labels. Their absence has probability exp(-Omega(L^3)); union over B^O(L^2) choices of small fibres leaves a negligible event. The empty-rectangle term is negligible at the stated scale by increasing C.

For remaining peripheral sizes a_i>=b0 and T=sum a_i, the forbidden-coordinate count Q=sum A_ij a_i a_j is at least q b0^2+2b0(T-r b0). Since the multinomial factor is <=m^T, T>CL contributes B^(-d L^2-Omega(L^2)) after summing at most m^r vectors. For T<=CL, the central fibre has size >=m/2 and factorial bounds give log_B multinomial <=bT+O(L). The derivatives of Q-bT are positive on all a_i>=b0. Clip sizes below b upward to b: with delta_i=(b-a_i)_+ this gives Q-bT>=d b^2-O(L)sum delta_i. Central rows must hit each peripheral fibre; the logarithm of this hit factor is at most -L sum_{delta_i>0} B^delta_i/(2 ln B). This absorbs each positive linear deficit since K t-B^t/(2 ln B) is bounded above. Sum O(L^r) vectors for the upper logarithmic rate.

For the lower rate use balanced peripheral fibres of size a=ceil b. Their number N has log_B N=r b^2+O(L). For any fixed map the full success probability is at least c_m rho^(q a^2), c_m=exp(-2(r+1)L), by independence of forbidden rectangles and required-hit row blocks. If k_i vertices of first peripheral fibre i lie outside a second map's peripheral support, the forbidden rectangle ij loses at least a(k_i+k_j)/2 coordinates. Hence the union of forbidden sets has size >=q a^2+a k with k=sum k_i. Count at most binom(ra,k)binom(m-ra,k)r^(ra) second maps per k. The sum of their joint probabilities is at most rho^(q a^2)(2r)^(ra) exp(m rho^a), and m rho^a<=L. Cauchy-Schwarz gives a lower bound with log_B at least -d b^2-O(L).

In the critical case q=r all incidence degrees are two. Orient the degree-two undirected multigraph of missing arrows cyclically component by component; loops and double edges are allowed. This produces a permutation sigma with Q=sum a_i a_sigma(i). With lambda_i=m rho^a_i, the main-range selected expectation is at most (1+o(1)) times the sum of prod_i pi_{lambda_sigma(i)}(a_i), where pi_lambda(k)=e^(-lambda)lambda^k/k!. By Stirling, if any normalized mean lies outside [1/2,2], that term is exponentially small in L. Otherwise every a_i=b+O(1), leaving O(1) integer vectors, each O(L^(-r/2)). The discarded tails remain negligible. This proves the critical bound. QED.

For r=1 the missing peripheral loop satisfies both hypotheses; its image probability is O(L^(-1/2)). The loopless and reciprocal-gap cases are also covered at the level of existence probability, since the only universal incoming column is the center and every peripheral incidence degree is at least two. Their unrestricted first-moment and resonance results are not needed here.

## 4. Positive criterion

**Theorem 3 (complete-core signatures).** Suppose the target admits a partition U,S with U nonempty and complete reflexive, such that every subset J of S is the outgoing S-neighborhood of some u_J in U that receives all S arrows. Then at every fixed bias p_m(F)>=1-exp(-c m) for some c>0 and sufficiently large m.

**Proof.** If S is empty a balanced deterministic partition suffices by union bound. Otherwise choose singleton S-fibres in a fixed reserve W of half the source vertices: examine disjoint ordered tuples until one realizes the induced S-relation. This succeeds with exponentially high probability. For every nonselected vertex x record its outgoing and incoming signatures relative to the selected tuple, J(x) and I(x). Outside W all 4^|S| exact signature pairs occur linearly many times, except with exponentially small probability. Allocate a disjoint linear-size group of exact signatures (J_u,I_u) to each u in U, splitting groups as needed. Assign all leftover vertices of signature J to u_J, which accepts every incoming signature. The exact groups guarantee each required S-to-U hit and exclude every forbidden one.

Conditional on the tuple tests (inside W) and signature exposures (incident to the selected tuple), all edges from nonselected rows to vertices outside W are fresh: none of these coordinates was tested. Every U-fibre has a linear-size part outside W, so all U-to-U hits hold with exponentially high probability by union bound. Tuple tests handle S-to-S; signatures handle U-to-S and S-to-U. This produces a full surjective bounded morphism. QED.

## 5. Exceptional targets

Five four-point canonical targets have neither a smaller vanishing quotient nor a classification by Theorems 2–3. The first three are settled below; the remaining two require the phase analysis in Section 5.3 and Appendices A–D. In the first two cases the displayed bounds need not be sharp.

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

### 5.3. Fixed phases of the two remaining targets

Here a phase v>0 refers to the integer sequence m_j=round(v j B^j), j tending to infinity. Multiplication of v by a power of B leaves the limiting phase classification unchanged. For arbitrary m, set j=floor(L-log_B L) and v_m=m rho^j/L in [1,B). This compact phase parametrization lets us pass from strict positive phase estimates to a full-sequence limit by the subsequence criterion.

**Theorem 4 (three forced small fibres).** For F=011010111 use labels C,A,Z,M with C universal and exactly A->A, Z->A, Z->M absent. Define

    H(t,s)=2+2 ln t-t-s             if s>=1,
          =3+2 ln t+ln s-t-2s      if s<=1,
    P_rho(v)=max_{i,l in Z} H(v rho^i,v rho^l).

Along the fixed phase m_j the image probability tends to one if P_rho(v)>0 and to zero otherwise. The maximum is attained, continuous in v and invariant under v->vB. For arbitrary sequences with normalized phase approaching a strictly positive phase the image probability also tends to one. If rho<=rho_*=(3 sqrt(3)-5)/4 then p_m->0 on the full sequence. If rho>rho_* there is a one-limit subsequence; the full sequence tends to one exactly when rho>r_c, with r_c as in Theorem 1.

The proof exploits the fact that the independent A-fibre determines Z uniquely as the outside rows missing A. The common nonneighbor set M0 of Z outside A union Z contains the actual M-fibre and may serve as that fibre if the remaining center is hit by all rows. The exact necessary and sufficient witness counts appear in Appendix A. The uniform first-moment estimate reduces relevant sizes to a,z=L+O(log L). Optimizing the resulting exponent over t with s=r t gives, for 0<r<1, the maximum ln(27r/(1+2r)^3); r=rho^(z-a) is restricted to integer powers. The factorization (1+2r)^3-27r=(r-1)(8r^2+20r-1) yields rho_*. At equality a polynomial prefactor estimate is essential to full-sequence vanishing. For positive phases with s<=1 we count exact triples and use a full overlap second moment. For s>1 we count pairs, then complete the typical larger M0 using fresh edges; see Appendices A.5 and B. The phase-circle coverage problem reduces to two adjacent lattice switches in Appendix C, giving the exact r_c and an integer-arithmetic certificate for the root bracket.

**Theorem 5 (two-stage forced fibres).** For F=011011101 use labels C,A,V,Z with missing arrows A->V, V->V, Z->A. Along m_j=round(v j B^j), the image probability tends to one precisely when some t=v rho^i, i in Z, belongs to the open interval (1/e,T); otherwise it tends to zero. Strict positive phases extend to varying normalized phases. The full sequence tends to one if rho>1/(e T), and otherwise has liminf zero and limsup one.

Here V is independent, A is forced by missing V, and Z is forced by missing A. The first-moment exponent for necessary witnesses is bounded by 1+ln t when t<=1 and 2+2ln t-t when t>=1. Positive phases permit a forced A-size alpha L with alpha<1, even when this size is atypical. The pair second moment proves existence of these rare witnesses, followed by completion using fresh columns. The critical endpoints have vanishing fixed-phase expected counts by fixed-offset Stirling estimates. The open interval covers the logarithmic phase circle exactly when B<eT. Appendix D gives all details.

These theorems concern fixed bias, not critical windows with bias depending on m. They establish both exceptional classifications in Theorem 1.

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

For four points the following 12 canonical encodings have positive limsup at the fair bias (the two exceptional types are identified in Section 5.3):

    001011011 001111011 011010111 011011011
    011011101 011011111 100111111 101011011
    101110111 101111101 101111111 111111111

Of the other 92, which vanish at all fixed biases, exactly the following 22 are minimal (20 are covered by Theorem 2; two starred encodings by Section 5.1):

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
| remaining exceptional cases | 3 | 15 |
| total | 104 | 512 |

The ten uniformly positive types account for 46 labelled matrices, and the two bias-dependent types each have six. The uniformly vanishing types account for 454. The fixed-central-label counts (zero, one, oscillatory) across the four successive bias intervals of Theorem 1 are (454,58,0), (454,52,6), (454,46,12), and (460,46,6). For theta>=theta_* the code 011010111 is an additional minimal vanishing type because it has no smaller vanishing quotient; hence there are 23 minimal four-point vanishing types rather than 22. These are not counts of all labelled central frames with the center unspecified. The Python reproducibility script [four_point_census.py](../experiments/four_point_census.py) uses a finer partition of proof methods. For each of the 104 canonical encodings the accompanying [classification certificate](four_point_classification.csv) records its orbit size, fair-model limit, fair-model minimality status and proof method. Each of the 70 inherited-zero classes includes an explicit surjection onto one of the smaller minimal vanishing targets (0, 0001, or 1001); all 70 such certificates have been checked by direct successor-image equality. The separate checker [verify_paper_certificate.py](../experiments/verify_paper_certificate.py) verifies the finite certificates and exhaustively excludes smaller minimal images for the other classes. The asymptotic limits are supplied by the proofs above, not by the finite checker. The independent audit checked all 24 permutations (not just the six peripheral permutations) and all 25,600 labelled surjections to 2- or 3-point sets for the 512 matrices. The two algorithms agree.

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

Write ML^as_theta for ordinary modal formulas with frame-validity probability tending to one in the fixed-bias model. By [2, Proposition 3.2(ii)], each formula of ML^r follows at the frame level from a finite extension axiom. Every fixed extension axiom holds asymptotically almost surely at every fixed bias: for a prescribed pattern of edges to and from a fixed finite tuple of distinct vertices, and a prescribed loop, each candidate outside the tuple realizes that pattern with a fixed positive probability, bounded below by min(theta,rho)^(2k+1) for tuple length k. Distinct candidates use disjoint coordinates. Union over O(m^k) tuples and finitely many patterns gives failure probability tending to zero. Thus ML^r is contained in ML^as_theta for every fixed theta. By [2, Proposition 3.5] the finite ML^r models are exactly the central frames.

**Theorem 6 (finite models at fixed bias).** For every finite central target F,

    F models ML^as_theta iff limsup_m p_m(F)>0.

Indeed if the upper limit is positive and phi fails in F, preservation of validity under surjective bounded morphisms gives Pr(G_m invalidates phi)>=p_m(F). Thus phi cannot be almost surely valid. If the upper limit is zero then p_m(F)->0, so chi_F^d is almost surely valid by the R^2 estimate, but F falsifies its own characteristic formula (centrality makes R^2 universal). This is the direct fixed-bias ordinary-language version of [2, Proposition 4.2(ii)], not a new characterization in principle.

By Theorem 1, the finite-model counts on one through four points are 1,1,3,12 when theta<theta_* and 1,1,3,11 when theta>=theta_*. Noncentral finite frames are excluded by the inclusion of ML^r. Thus the characteristic formula of 011010111 belongs to ML^as_theta exactly when theta>=theta_*; in particular the high-bias logic differs from the fair logic. The earlier two convergence transitions do not by themselves imply changes to the full almost-sure logic.

At theta<theta_* there are 25 minimal vanishing types on at most four points; at theta>=theta_* there are 26. For two distinct such types F,H, no surjective bounded morphism F->H exists by minimality if H is smaller, cardinality if larger, and bijective bounded morphism implying isomorphism if equal size. Thus each F validates ML^r and all the other corresponding translated characteristic formulas, but falsifies its own. Normal modal soundness proves mutual independence of these 25 or 26 axiom schemes over ML^r, at the specified bias. This does not show that they axiomatize all ML^as_theta.

### 7.1. A prime-cycle family

For r>=2 let C_r consist of a universal reflexive central vertex c and r peripheral vertices i in Z/rZ, each with exactly two successors c and i+1. Let T2=C_1 be the complete reflexive two-point frame, E1 the reflexive singleton, and K2 the two-point target with absent peripheral loop.

#### Quotient classification for central cycles

The surjective bounded-morphic images of C_r, up to isomorphism, are exactly E_1, C_d for positive divisors d of r, and K_2 if r is even.

Proof. Given a surjective bounded morphism f, write z=f(c). It is central, since c has all incoming and outgoing arrows. For each peripheral i, the set of successors of f(i) is exactly {z,f(i+1)}, by forth and back. If f(i)=z for some i, the target has at most two vertices, since the successor set of z is the whole target. In the singleton case the target is E_1. In the two-point case write w for the other point. The central row is universal, so only the loop of w is optional. If w has a loop, all source peripheral rows must hit w, implying f(i+1)=w for every i. Thus every peripheral maps to w and none maps to z, contradicting this case. If w has no loop, then every peripheral i must satisfy f(i+1)=w exactly when f(i)=z, and f(i+1)=z exactly when f(i)=w. This is an alternating colouring, possible precisely when r is even. Conversely the alternating colouring and f(c)=z give a bounded morphism onto K_2 for even r, as the successor sets directly verify.

Now suppose no peripheral maps to z. Every other target vertex u has successor set {z,s(u)} for a uniquely determined noncentral vertex s(u), because it is f(i) for some i, and f(i+1) is noncentral. The map s is well-defined by successor-image equality, and f(i+1)=s(f(i)). Its orbit from f(0) covers every noncentral target vertex by surjectivity, and s^r(f(0))=f(0). Hence this orbit is a cycle of length d dividing r, and the target is C_d. Conversely reduction of peripheral indices modulo any divisor d gives a surjective bounded morphism C_r->C_d, sending center to center. The map to E_1 exists by seriality. This proves the theorem.

For C_r, q=r^2-r, d=r(r-2), and both hypotheses of Theorem 2 hold. Hence p_m(C_r)->0 for all r>=2, with the critical bound O(L^(-1)) when r=2. An even r has the vanishing proper image K2, and an odd composite r has a smaller vanishing C_d. An odd prime r has only E1,T2 as proper images. Thus precisely the odd prime lengths yield minimal vanishing cycles, and their characteristic formulas are mutually independent by the same finite-countermodel argument.

Goranko [2, Proposition 4.7] already considers an infinite independent path family; infinitude is not claimed as novel here. Independence of characteristic formulas alone does not imply non-finite axiomatizability by arbitrary modal formulas.

## 8. Limitations, reproducibility and further work

This classification concerns independent ordered edges including loops, at every fixed theta strictly between zero and one, and finite central targets of size at most four. It does not determine arbitrary shrinking critical-phase windows, the model theory of larger frames, or the full axiomatic theory of ML^as_theta. The three transition constants are transitions in fixed-bias limiting behavior, not claims about the width of a varying-bias sharp threshold window. All asymptotic arguments are internal hand proofs; no independent refereeing or machine verification is claimed. Finite numerical checks support the enumeration and root signs only. The previously verified Lean modules address smaller finite structural facts; newer modules await actual compilation. The present Markdown main text and technical appendices have not been compiled as a unified LaTeX PDF. Before release, complete independent mathematical review, primary-source priority checking, notation and typesetting, and authorship/AI-use disclosure. No submission or merge is made.

## References

[1] V. Goranko and B. Kapron. The Modal Logic of the Countable Random Frame. Archive for Mathematical Logic 42 (2003), 221–243. https://doi.org/10.1007/s001530100135

[2] V. Goranko. The modal logic of almost sure frame validities in the finite. Advances in Modal Logic 13 (2020), 249–268. https://www.aiml.net/volumes/volume13/Goranko.pdf (mirror https://titan.dcs.bbk.ac.uk/volumes/volume13/Goranko.pdf).

[3] J.-M. Le Bars. The 0-1 law fails for frame satisfiability of propositional modal logic. LICS 2002, 225–234. https://doi.org/10.1109/LICS.2002.1029831

[4] R. F. Schamm. Zero-One Laws and Almost Sure Validities on Finite Structures. MSc short dissertation, Rand Afrikaans University, 2002. Sections 3.3.5–3.3.6; Figure 4.1; appendix. (The figure ordering has not been visually verified.)

[5] V. V. Sliusarev. Modal Logics of Almost Sure Validities and Zero-One Laws in Horn Classes. Doklady Mathematics 110 (2024), 442–449. https://doi.org/10.1134/S1064562424601446

[6] V. Sliusarev. Modal logics of almost sure validities in some classes of euclidean and transitive frames. https://arxiv.org/abs/2406.10770 (2024 preprint; later publication details to verify).

[7] V. V. Sliusarev. Modal Logic of Random Kripke Frames. PhD thesis, 2026. English summary (2025), https://www.hse.ru/data/2025/10/24/1949835949/2resume_en.pdf ; defence record https://www.hse.ru/sci/diss/1034821759 .

[8] J.-M. Le Bars. A Sharp Threshold for a Non-monotone Digraph Property. In *Trends in Mathematics*, Birkhäuser, 2002, pp. 197–211. https://ndl.ethernet.edu.et/bitstream/123456789/77242/1/25.pdf (Section 2, kernel size estimates and first/second moments; bibliographic volume title to verify).

Further bibliography and evidence status: [RELATED_WORK](../docs/RELATED_WORK.md).
