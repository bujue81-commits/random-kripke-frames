# Sharp logarithmic existence probability for fixed chain targets

Status: internal hand proof, not Lean-formalized or externally refereed; originality relative to published literature is unverified. This strengthens CHAIN_SHARP_FIRST_MOMENT.md by matching the leading exponent for the existence probability, rather than merely for its first moment.

## Statement

Let G_m be the labelled random directed frame with independent fair ordered edges, including loops. Fix r>=2 and let F_r have central vertex 0 with edges in both directions to all vertices (including its loop), and exactly the noncentral arrows i -> i+1 for 1<=i<r. Write L=log_2 m and p_m=Pr(G_m admits a surjective bounded morphism onto F_r). Then

    log_2 p_m = -(r-1)^2 L^2 + O_r(L log L).

In particular, -log_2(p_m)/L^2 tends to (r-1)^2.

## Upper bound (previous result)

The preceding first-moment proof, CHAIN_SHARP_FIRST_MOMENT.md, establishes

    log_2 E[X_m] = -(r-1)^2 L^2 + O_r(L log L),

where X_m counts all surjective bounded morphisms. Markov gives p_m<=E[X_m]. Here we prove the matching lower bound. We use only balanced maps and a bound on intersections of their forbidden coordinate sets; no independence of map-success events is assumed.

## Balanced maps and their individual probabilities

Set a=ceil(L), s=r*a and q_r=r^2-r+1. For all sufficiently large m, s<=m/2 and m-s>=a. Let M be the set of maps with each of the r noncentral fibres of size a, the remaining m-s vertices forming the central fibre. Its size N=(m)_s/(a!)^r satisfies

    log_2 N = r L^2 + O_r(L log L).

Indeed (m-s)^s/a^s <= N <= m^s. Every f in M has the same forbidden ordered-coordinate set size

    Q=q_r*a^2.

Let D_f be the event that every coordinate in this set is absent, and B_f the event that f is a full bounded morphism. Thus B_f implies D_f, and P(D_f)=2^(-Q). Conditional on D_f, the required hit blocks are disjoint from the forbidden coordinates and from one another. Each contains at least a edge coordinates and there are at most (r+1)m blocks. Since 2^(-a)<=1/m, the fixed-map formula yields

    c_r*2^(-Q) <= P(B_f) <= 2^(-Q),
    c_r=exp(-2(r+1)),

using ln(1-x)>=-2x for 0<=x<=1/2.

Define Y=sum_{f in M} 1_{B_f}. Hence

    c_r N 2^(-Q) <= E[Y] <= N 2^(-Q).

In particular log_2 E[Y]=-(r-1)^2 L^2+O_r(L log L).

## Overlap lemma for forbidden coordinates

For f,g in M, let U_f and U_g be their noncentral vertex sets, each of size s, and put t=|U_f intersect U_g| and k=s-t. Let H_f be the set of forbidden ordered coordinates for f and H_g the analogous set for g.

Every pair in H_f intersect H_g must have both endpoints in U_f intersect U_g, since H_f lies in U_f x U_f and H_g lies in U_g x U_g. In the i-th noncentral f-fibre let b_i count vertices in U_g, so 0<=b_i<=a, sum b_i=t and sum(a-b_i)=k.

Every ordered pair inside any single noncentral f-fibre is forbidden, including loops. In that fibre, a^2-b_i^2 such coordinates have an endpoint outside U_g and therefore cannot belong to H_g. These sets for different i are disjoint. It follows that

    |H_f intersect H_g|
       <= Q-sum_i(a^2-b_i^2)
       <= Q-a*sum_i(a-b_i)
       = Q-a*k.

The key inequality a^2-b_i^2=(a-b_i)(a+b_i)>=a(a-b_i) uses only b_i<=a. It remains true if f and g label their common noncentral vertices differently. In particular no alignment of the individual fibres is assumed.

Consequently |H_f union H_g|=2Q-|H_f intersect H_g| >= Q+a*k, and independence of the edge bits gives

    P(B_f and B_g) <= P(D_f and D_g) <= 2^(-Q-a*k).

This upper bound deliberately drops all hit requirements.

## Counting overlapping maps and the second moment

Fix f. For a given k between 0 and s, a map g with |U_f minus U_g|=k has a noncentral set formed by removing k vertices of U_f and choosing k vertices outside U_f. For each such set, there are at most r^s assignments of its vertices to the r labels; allowing assignments with incorrect fibre sizes increases the bound. Hence the number of such g is at most

    binom(s,k) binom(m-s,k) r^s.

Using binom(m-s,k)<=m^k and a>=log_2 m,

    sum_{g in M} P(B_f and B_g)
      <= 2^(-Q) r^s sum_{k=0}^s binom(s,k) m^k 2^(-a*k)
      <= 2^(-Q) r^s 2^s.

Summing over the N choices of f,

    E[Y^2] <= N 2^(-Q) (2r)^s
            <= c_r^(-1) (2r)^s E[Y].

The diagonal terms f=g are included, and the sum is over ordered pairs of maps. The bound uses only the shared forbidden coordinates, not any assumption that the hit events for f and g are independent.

By Cauchy-Schwarz applied to Y*1_{Y>0},

    p_m >= P(Y>0) >= E[Y]^2/E[Y^2]
        >= c_r (2r)^(-s) E[Y]
        >= c_r^2 (2r)^(-s) N 2^(-Q).

Taking base-2 logarithms and substituting log_2 N=r L^2+O_r(L log L), Q=q_r L^2+O_r(L), and s=O_r(L), we obtain

    log_2 p_m >= -(q_r-r)L^2-O_r(L log L)
              = -(r-1)^2 L^2-O_r(L log L).

Combined with Markov's upper bound, this proves the statement. The coefficient is exact for the logarithmic existence rate, not merely the expectation rate.

## Limits and future work

- r is fixed, not growing with m. The probability itself is not determined up to a multiplicative constant; the subleading terms remain open here.
- This is a theorem for the explicitly defined labelled fair-edge model and target. The characteristic-formula consequence requires the correct Jankov-Fine convention; the proof does not classify K^as.
- The overlap argument depends crucially on all within-noncentral-fibre coordinates being forbidden (no noncentral loops in the target).
- Bibliographic priority of the sharp probability rate is not established.
- Lean formalization: first complete the blocked builds of ChainFrames and ChainEdgeCounting; then prove fixed-coordinate counts, the forbidden-set overlap bound, the balanced-map count, and the finite second-moment inequality. Do not describe this hand proof as machine-verified.
