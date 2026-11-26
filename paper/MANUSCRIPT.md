# Almost-Sure Bounded-Morphic Images of Random Kripke Frames: A Complete Classification of Central Frames on at Most Four Vertices

**Working manuscript, version 0.1 — 26 November 2026.** Author and affiliations to be confirmed by the researcher. Not submitted or independently refereed. The present manuscript is a consolidated main text with linked detailed proofs; the next editorial stage is to integrate the proofs into a standalone typeset submission. The finite census has been independently recomputed; the probability arguments remain hand proofs. Novelty is not asserted until the literature audit is complete.

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

A detailed version including constants is in [Proof supplement A](../proofs/NO_SINGLETON_MISS_DEGREE_CRITERION.md). The older loopless and reciprocal-gap estimates are contained at the level of existence probability in this theorem; their unrestricted first-moment and resonance results are separate, optional material.

## 4. Positive criterion

**Theorem 3 (complete-core signatures).** Suppose the target admits a partition U,S with U nonempty and complete reflexive, such that every subset J of S is the outgoing S-neighborhood of some u_J in U that receives all S arrows. Then at every fixed bias p_m(F)>=1-exp(-c m) for some c>0 and sufficiently large m.

**Proof.** If S is empty a balanced deterministic partition suffices by union bound. Otherwise choose singleton S-fibres in a fixed reserve W of half the source vertices: examine disjoint ordered tuples until one realizes the induced S-relation. This succeeds with exponentially high probability. For every nonselected vertex x record its outgoing and incoming signatures relative to the selected tuple, J(x) and I(x). Outside W all 4^|S| exact signature pairs occur linearly many times, except with exponentially small probability. Allocate a disjoint linear-size group of exact signatures (J_u,I_u) to each u in U, splitting groups as needed. Assign all leftover vertices of signature J to u_J, which accepts every incoming signature. The exact groups guarantee each required S-to-U hit and exclude every forbidden one.

Conditional on the tuple tests (inside W) and signature exposures (incident to the selected tuple), all edges from nonselected rows to vertices outside W are fresh: none of these coordinates was tested. Every U-fibre has a linear-size part outside W, so all U-to-U hits hold with exponentially high probability by union bound. Tuple tests handle S-to-S; signatures handle U-to-S and S-to-U. This produces a full surjective bounded morphism. QED.

Detailed exposure argument: [Proof supplement B](../proofs/COMPLETE_LARGE_CORE_SIGNATURE_CRITERION.md).

## 5. Exceptional targets

The following five canonical four-point cases have neither a smaller vanishing quotient nor a classification by Theorems 2–3. We give their precise conclusions and proof locations. For the two negative cases the bound is not asserted sharp.

### 5.1. Forced independent fibres: 001011101 and 001101011

Relabel so B is independent and A is precisely the set outside B of rows missing B. The missing arrows in the first case are A->B, B->A, B->B, Z->A; in the second they are A->A, A->B, B->B, Z->A. No universal-incoming label misses exactly B, so the tiny-fibre exclusion proof forces b_B=|B|>=L-3 log_B L except on a negligible event; independence forces b_B=O(L).

For the first target B also misses the forced A. Averaging over A gives the necessary count at size b_B at most binom(m,b_B) rho^(b_B^2)(1-rho^b_B+rho^(2b_B))^(m-b_B). On the main range this is bounded by (1+o(1))pi_{m rho^b_B}(b_B). Geometric decay of the normalized Poisson mean as b_B increases and Stirling give p_m=O(L^(-1/2)).

For the second target A is independent and B hits A. Set a=|A|, lambda=m rho^b_B, t=lambda/b_B. Its necessary count is at most (1+o(1))pi_lambda(b_B)t^a pi_{b_B rho^a}(a). Summing first over a=O(log L), then using the narrow resonance window |t-1|<=L^(-1/4) and the second Poisson sum gives p_m=O((L log L)^(-1/2)). The complementary size ranges are negligible. Details of both tail bounds: [Proof supplement C, Section 1](../proofs/FORCED_FIBRES_AND_DOMINATING_RESERVE.md).

### 5.2. One-row missing star: 100111111

Only Z->A_i are missing (two such destinations in this case). In a half-size reserve W select a t-subset D hit by every source row, t=ceil(L-1.5 log_B L). Its count has normalized second moment 1+o(1): overlap j<=t/2 has joint/independent ratio 1+o(1); the remaining overlap has probability exp(-Omega(L^2)) with ratio <=exp(O(L^1.5)). The selected D is measurable in edges ending in W. Fresh D-to-outside-W coordinates yield Theta(L^1.5) common nonneighbors, from which choose disjoint fibres of size ceil(2L) for the A_i. All rows outside D hit these and the central remainder with high probability using fresh edges. Every row hits D, and D hits the remainder. Thus p_m->1, at any fixed bias and any fixed number of missing star arrows. Full proof: [supplement C, Section 2](../proofs/FORCED_FIBRES_AND_DOMINATING_RESERVE.md).

### 5.3. Two-stage forced fibres: 011011101

Only A->B, B->B, Z->A are missing. For theta<1-1/e choose an independent B-set of size ceil(L-log_B L+delta) with constant delta>0 so rho B^(-delta)>1/e (here B in the power is the logarithm base). Its expected count grows exponentially in L and its normalized second moment tends to one. For a fixed independent B-set the forced A consists of all outside rows missing B. With high conditional probability its size lies between alpha L and beta L for fixed 0<alpha<beta<1. Expose A columns: Z is the set of remaining rows missing A, and grows polynomially in m; all rows in A and the independent B-set hit A. Fresh columns verify all remaining hits. Count the independent sets with failed completions: their mean is o(the mean of all independent sets). Chebyshev and Markov give a successful completion a.a.s. Thus p_m->1 in particular for the fair model. [Proof supplement D](../proofs/TWO_STAGE_FORCED_FIBRE_POSITIVE.md).

### 5.4. Exact forced pair and overlap argument: 011010111

Only A->A, Z->A, Z->M are missing. Choose a=round(L-log_2 L-1), z=a+2, k=ceil(L+2 log_2 L), L=log_2 m. A sufficient witness has an independent A, Z precisely the outside rows missing A, M precisely the common nonneighbors of Z outside A union Z, of these three sizes, and C the remainder. All rows hit Z and C; every non-Z row hits M. Define Y0 by dropping only the C-hit requirement. Each A determines at most one witness.

With t=m 2^(-a)/L in [sqrt(2),2sqrt(2)], the exact count yields

    ln E[Y0]=L(3+3 ln t-ln 4-1.5 t)+O(log L),
    E[Y]/E[Y0]->1.

The concave exponent is bounded below by 0.48 throughout the interval. To prove concentration divide pairs by support intersection h and forbidden-coordinate intersection I. If h<=L/2, comparing external hit probabilities by inclusion-exclusion gives joint/marginal ratio <=(1+o(1))2^I; the count of overlaps and I<=h^2 makes positive small overlaps negligible. For h>L/2, let D=max(a,z,k). Pairs with D h-I>=K L log L have negligible contribution by the crude forbidden-edge bound. In the remaining pairs, if x,y,w are intersections of A,Z,M with the second support, the deficit bounds

    D h-I >= x(D-x)+y(D-x)+w(D-y).

This forces x=D-O(log L). The loss of forbidden coordinates from assigning A-vertices to other labels then implies |A minus A'|=O(log L). Conditional on the first witness, an alternative independent A' at distance d requires absence of at least (a-d)(2d-e) fresh or hit-conditioned bits, where e=|(A' minus A) intersect Z|. Summing over A' gives a geometric bound with base a rho^(a-d)(z+m rho^(a-d))=poly(L)/m. Thus the conditional expected number of other near-identical A' is o(1); identical A determines the original witness. These pairs contribute O(E[Y0]) rather than its square. Hence E[Y0^2]/E[Y0]^2->1. Chebyshev and the negligible mean loss E[Y0-Y] prove p_m->1.

For the exact witness formulas and all uniform overlap estimates, see [supplement E1](../proofs/LAST_FOUR_POINT_FORCED_PAIR.md), [E2](../proofs/LAST_FOUR_POINT_GROWING_WITNESSES.md), and [E3](../proofs/LAST_FOUR_POINT_SECOND_MOMENT.md). This final proof as written is fair-specific.

## 6. Exhaustive classification

For a three-point target the canonical positive encodings are 0101, 1011, 1111. All other canonical encodings vanish: 7 by orbit count, of which 0001 and 1001 are minimal. The sixteen labelled cases are covered by Theorems 2–3 and quotients onto the two-point target 0. More explicitly the five labelled positive matrices are 0101,1010,1011,1101,1111. See [three-point proof](../proofs/THREE_POINT_CENTRAL_QUALITATIVE_CLASSIFICATION.md).

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

The remaining 70 all map onto a smaller vanishing target. To check the computation, for every 9-bit matrix enumerate all peripheral permutations and calculate its canonical encoding. For each nontrivial partition of four labels into 2 or 3 blocks, a quotient exists precisely if rows in the same block have equal sets of successor blocks. Mark the frame inherited-zero if the quotient encoding is 0 or a vanishing three-point encoding. Otherwise apply the degree criterion, then complete-core signatures, then the five exceptional proofs. The table of counts by proof method is

| method | isomorphism classes | labelled matrices (central label fixed) |
|---|---:|---:|
| smaller vanishing quotient | 70 | 339 |
| Theorem 2 | 20 | 103 |
| forced negative cases | 2 | 12 |
| Theorem 3 | 9 | 43 |
| remaining positive cases | 3 | 15 |
| total | 104 | 512 |

There are 454 labelled negative and 58 labelled positive matrices, with central label fixed. These are not counts of all labelled central frames with the center unspecified. The Python reproducibility script [four_point_census.py](../experiments/four_point_census.py) uses a finer partition of proof methods. Independent audit this turn checked all 24 permutations (not just the six peripheral permutations) and all 25,600 labelled surjections to 2- or 3-point sets for the 512 matrices. The two algorithms agree.

## 7. Modal consequences and independence

Write chi_F for the universal-modality characteristic formula that negates the conjunction of the existence of each label, the global partition condition and the exact successor-label conditions. A falsifying valuation is precisely a surjective bounded morphism onto F. In ordinary modal language write chi_F^d for the translation [U]=box box and <U>=diamond diamond. On frames with universal R^2 this translation is exact; for random G_m,

    Pr(R^2 not universal)<=m^2(1-theta^2)^(m-2).

Thus Pr(G_m validates chi_F^d) differs from 1-p_m(F) by at most the displayed error.

By [2, Proposition 3.5], all finite central targets validate ML^r. For any almost-surely valid formula phi and target F with p_m(F)->1, F must validate phi: otherwise each source with a bounded morphism onto F would falsify phi by preservation of frame validity, contradicting almost-sure validity. Conversely p_m(F)->0 makes chi_F^d almost surely valid and false in F. Therefore the 1,1,3,12 positive central types on one through four vertices are exactly the finite models of ML^as in these sizes within the central class (and noncentral finite frames cannot validate ML^r). This strengthens the characteristic-formula census to a finite-model census in these sizes only.

There are 25 minimal vanishing types on at most four points. For distinct minimal types F,H, no surjective bounded morphism F->H exists, by minimality if H is smaller, impossibility of surjection if H is larger, and bijective bounded morphism implying isomorphism if sizes agree. Every F thus validates ML^r and all the other minimal types' translated characteristic formulas, but falsifies its own. Normal modal soundness proves mutual independence of these 25 axiom schemes over ML^r. This is not an axiomatization of all ML^as.

Further family: for a central directed peripheral r-cycle, all quotient images are the reflexive singleton, central cycles of divisor length d|r (length one means complete two-point), and K2 exactly when r is even. Theorem 2 gives vanishing for all r>=2. Odd prime cycles therefore form an infinite family of minimal vanishing types. See [cycle quotient proof](../proofs/CENTRAL_CYCLES_MINIMALITY.md). Goranko [2, Proposition 4.7] already considers an infinite independent path family; infinitude is not claimed as novel here. Independence of characteristic formulas alone does not imply non-finite axiomatizability by arbitrary modal formulas.

## 8. Limitations, reproducibility and further work

The main census is proved for fair edges, not all fixed biases. In particular Sections 5.3 and 5.4 leave biases outside their stated ranges unresolved. All probability arguments are internal hand proofs, not formally verified or externally refereed. Finite scripts corroborate exact combinatorial counts but not asymptotic statements. Previously verified Lean modules concern smaller finite structural facts; the latest workflow-run query returned no runs and the newer chain modules have not been verified. Before a submission, integrate all detailed supplements into a single manuscript, independently review the probability proofs, complete primary-source priority checks, and formally verify the finite census. No claim of the general zero-one law, complete axiomatization, or first discovery is made. Authorship and any required AI-use disclosure must be settled by the researcher before release.

## References

[1] V. Goranko and B. Kapron. The Modal Logic of the Countable Random Frame. Archive for Mathematical Logic 42 (2003), 221–243. https://doi.org/10.1007/s001530100135

[2] V. Goranko. The modal logic of almost sure frame validities in the finite. Advances in Modal Logic 13 (2020), 249–268. https://www.aiml.net/volumes/volume13/Goranko.pdf (mirror https://titan.dcs.bbk.ac.uk/volumes/volume13/Goranko.pdf).

[3] J.-M. Le Bars. The 0-1 law fails for frame satisfiability of propositional modal logic. LICS 2002, 225–234. https://doi.org/10.1109/LICS.2002.1029831

[4] R. F. Schamm. Zero-One Laws and Almost Sure Validities on Finite Structures. MSc short dissertation, Rand Afrikaans University, 2002. Sections 3.3.5–3.3.6; Figure 4.1; appendix. (The figure ordering has not been visually verified; do not claim a correction of a specific cell.)

[5] V. V. Sliusarev. Modal Logics of Almost Sure Validities and Zero-One Laws in Horn Classes. Doklady Mathematics 110 (2024), 442–449. https://doi.org/10.1134/S1064562424601446

[6] V. Sliusarev. Modal logics of almost sure validities in some classes of euclidean and transitive frames. https://arxiv.org/abs/2406.10770 (2024 preprint; later publication details to verify).

[7] V. V. Sliusarev. Modal Logic of Random Kripke Frames. PhD thesis, 2026. English summary (2025), https://www.hse.ru/data/2025/10/24/1949835949/2resume_en.pdf ; defence record https://www.hse.ru/sci/diss/1034821759 .

Further bibliography and evidence status: [RELATED_WORK](../docs/RELATED_WORK.md).
