# Completing the final fair four-point case by a full overlap second moment

Status: internal hand proof, subject to independent review and Lean verification. No priority claim. This completes the fair-model classification conditional on the earlier hand proofs. Fixed independent ordered edge bits, loops included, probability theta=1/2. All logarithms explicitly base 2 or natural as indicated.

## Statement and setup

For target 011010111 relabel vertices C,A,Z,M, where C is universal and the only forbidden arrows are A->A, Z->A, Z->M (M is the B label in the previous notes). Put L=log_2 m, rho=1/2, and choose

    a=round(L-log_2 L-1), z=a+2, k=ceil(L+2 log_2 L),
    s=a+z+k, c=m-s.

Then the probability p_m of a surjective bounded morphism onto this target tends to one.

Use the necessary exact-M witness count Y0 of LAST_FOUR_POINT_GROWING_WITNESSES.md at precisely these sizes. A triple T=(A,Z,M) is three disjoint vertex sets of sizes a,z,k. C is the complement. Write E_T for the following event:

- A x A, Z x A, Z x M are entirely absent.
- Every row outside A union Z hits A.
- Every row hits Z.
- Every row outside Z hits M.
- Each column in C receives at least one edge from Z.

The last two requirements make M precisely the common nonneighbors of Z outside A union Z; likewise Z is exactly the set of outside-A rows missing A. Hence for each A there is at most one successful triple. All the specified forbidden rectangles and the individual row/column hit blocks are mutually disjoint coordinate sets. In particular their probabilities multiply. The forbidden set H_T has size Q=a^2+za+zk, the same for every triple. Write P=P(E_T)=rho^Q times the hit factor R. The hit factor satisfies R=exp(-O(L)), since rho^a,rho^z=Theta(L/m), rho^k<=1/(m L^2), and there are O(m) requirements. Let N=(m)_s/(a!z!k!) be the number of triples.

The previous first moment shows E[Y0]=NP>=exp(0.47 L) for sufficiently large m (E[Y]/E[Y0]=1+o(1), where Y additionally requires every row to hit C). We prove E[Y0^2]/E[Y0]^2=1+o(1). Then concentration and Markov on Y0-Y give Y>0 a.a.s., hence p_m->1.

## 1. Small support overlap: h<=L/2

For two triples T,T' let S=A union Z union M, S'=A' union Z' union M', h=|S intersect S'|, and I=|H_T intersect H_T'|. The joint absence probability is rho^(2Q-I). All forbidden coordinates lie inside (S union S') squared.

For an upper bound on the joint event, retain only hit requirements for rows outside S union S' and for columns outside S union S'. More precisely, each such outside row must hit all six blocks A,Z,M,A',Z',M', and each outside column must receive an edge from both Z and Z'. These row tests and column tests use disjoint families of coordinates, also disjoint from the forbidden coordinates. Different rows are independent, and different columns are independent.

Let ell=min(a,z,k)=L-O(log L). For a given outside row, the probability of missing any one of its six blocks is rho^size. For any pair of these misses the joint probability is <=rho^(2ell-h), since the two blocks overlap in at most h vertices (within one triple they are disjoint). By the two-term Bonferroni bound, the probability of all six hits is at most 1-sum of single miss probabilities +15*rho^(2ell-h). The product of the six single hit probabilities is at least 1-sum of single miss probabilities, and tends uniformly to one. Consequently the ratio of the joint row probability to that product is <=1+O(rho^(2ell-h)). For an outside column the two hit tests from Z,Z' satisfy the same bound by inclusion-exclusion. Thus over at most 2m outside rows and columns the product of these ratios is <=exp(O(m*rho^(2ell-h)))=1+o(1) uniformly for h<=L/2.

In each individual E_T (and E_T') all the original hit blocks are independent. The requirements dropped in this upper bound number O(s) per event: they are row hits for rows in the union of supports and column hits for columns in that union. Their product of probabilities is 1-o(1), because each miss has probability <=rho^ell=O(L/m). Therefore uniformly for h<=L/2,

    P(E_T and E_T') / P^2 <= (1+o(1))*rho^(-I).

For h=0, this is <=1+o(1). For h>=1, I<=h^2 because every common forbidden coordinate has both endpoints in the intersection of supports. For uniformly independent triples, their supports are uniformly independent s-subsets. By the union bound for containment of specified h vertices,

    P(|S intersect S'|=h) <= binom(s,h)*(s/(m-s))^h
                            <= (s^2/(m-s))^h.

For 1<=h<=L/2, the product of this bound and 2^(h^2) is at most (s^2*2^(L/2)/(m-s))^h. The base tends to zero, and the geometric series over positive h is o(1). Hence all pairs with h<=L/2 contribute at most (1+o(1))*E[Y0]^2.

## 2. Large overlaps with a deficit

Let D=max(a,z,k)=L+O(log L). Write x=|A intersect S'|, y=|Z intersect S'|, w=|M intersect S'|, so x+y+w=h. Restrict H_T to (S intersect S') squared. Its size is exactly x^2+yx+yw, so

    I <= x^2+yx+yw <= D h,
    D h-I >= x(D-x)+y(D-x)+w(D-y).

The same statements hold on exchanging T,T'. Denote the deficit D h-I by Delta.

For arbitrary pairs, dropping all hits gives the crude ratio P(E_T and E_T')/P^2 <=rho^(-I)*R^(-2)=2^(I+O(L)), uniformly. The support intersection counting bound above gives, for any h>=1,

    P(|S intersect S'|=h) <= 2^(-L h+O(h log L)).

Here s=O(L). Therefore pairs with h>L/2 and Delta>=K L log_2 L contribute o(E[Y0]^2), for any sufficiently large fixed K. Indeed I=D h-Delta, (D-L)h=O(L log L), and one can choose K strictly larger than the fixed constants in all O(L log L) upper bounds, so the normalized sum over O(L) sizes is at most O(L)*2^(-L log_2 L) eventually. No independence of these pairs is assumed.

## 3. Structural lemma for the remaining large overlaps

Suppose h>L/2 and Delta<K L log_2 L. Then x>=D-O(log L). To prove this, if x<=D/2 the displayed deficit inequality gives x+y<=2 Delta/D=O(log L), and subsequently w<=Delta/(D-y)=O(log L). This contradicts h>L/2. Thus x>D/2, and x(D-x)<=Delta implies D-x<=2 Delta/D=O(log L). In particular a-x=O(log L).

We need alignment of the A labels, not merely overlap of supports. Let

    u=|A intersect A'|, v=|A intersect Z'|, r=|A intersect M'|,

so u+v+r=x. Every coordinate in (A intersect Z') squared and in (A intersect M') squared belongs to H_T restricted to the common support but not H_T', because Z' and M' are reflexive target labels. These two sets are disjoint. Their total v^2+r^2 is bounded by the lost coordinates x^2+yx+yw-I, which is at most Delta. Hence v+r=O(sqrt(L log L)), implying u=x-v-r>=L/2 eventually. Further, all coordinates from A intersect A' to A intersect (Z' union M') are forbidden by T but not by T', as A' forbids only arrows to A'. Thus u(v+r)<=Delta, implying v+r=O(log L). It follows that

    d=|A minus A'|=a-u=O(log L).

All constants are uniform in the pairs, depending only on the fixed K and the chosen sizes. Fix K1 such that d<=K1 log_2 L for all these pairs and large m.

## 4. Conditional bound for near-identical A sets

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

## 5. Conclusion and logical consequence

Sections 1-4 exhaust all ordered pairs. They show E[Y0^2]<=(1+o(1))*E[Y0]^2; the reverse asymptotic lower bound follows from variance nonnegativity. Chebyshev gives Y0>=E[Y0]/2 a.a.s. From the preceding fixed-size first moment, E[Y0-Y]=o(E[Y0]) because the added C hits fail with probability o(1) given E_T (uniformly, with c=m-O(L)). Markov gives Y0-Y<E[Y0]/2 a.a.s. Consequently Y>0 a.a.s.; a sufficient witness yields the desired surjective bounded morphism.

Thus F011010111 has p_m->1 in the fair model. Its ordinary-modal characteristic formula has validity probability tending to zero by the earlier R^2 translation. The complete fair central four-point census is 92 zero-limit and 12 one-limit isomorphism classes (454 and 58 labelled matrices). Exactly 22 minimal vanishing four-point classes, as 70 of the zero classes have smaller vanishing quotients and 22 do not. This is a full classification for four-point central targets, not the whole almost-sure logic. The proof uses fair-model size choices; no extension to arbitrary theta asserted. Earlier high-bias gap for 011011101 remains open. Independent review, literature priority, and machine verification remain pending.
