# All loopless noncentral digraphs: biased model and critical regime

Status: internal hand proof, not Lean-formalized, independently refereed or novelty-checked. This removes the orientation restriction in ORIENTED_CENTRAL_SECOND_ORDER_RATE.md and also treats fixed non-fair edge probabilities. In the critical case the logarithmic estimate alone does not imply convergence to zero; a separate Poisson bound does.

## Theorem

Fix an integer r>=1, and any loopless directed graph D on 1,...,r, allowing both opposite arrows between distinct vertices. Let e be its number of arrows and let F(D) be obtained by adding a reflexive vertex 0 with all arrows from and to every vertex. Let G_m have m labelled vertices and independently present ordered edges (including loops) with fixed probability theta in (0,1). Put

    rho=1-theta, B=1/rho>1,
    L=log_B(m), b=L-log_B(L),
    q=r^2-e, d=q-r=r(r-1)-e>=0.

Let X_m count all surjective bounded morphisms onto F(D), Z_m count the weaker surjective witnesses requiring only forbidden noncentral edges and central-to-noncentral hits, and p_m=P(X_m>0). For every fixed D and theta,

    log_B p_m = -d b^2 + O_{D,theta}(L),
    log_B E[X_m] = -d b^2 + O_{D,theta}(L),
    log_B E[Z_m] = -d b^2 + O_{D,theta}(L).

Equivalently the logarithms are -d L^2+2d L log_B L+O(L). If d=0 (all distinct noncentral pairs have both arrows), then additionally

    p_m <= E[X_m] <= E[Z_m] = O_{r,theta}(L^(-r/2)).

Thus p_m tends to zero for every target in the stated class, including the critical case. When d=0 the first display only gives a polynomial-in-m lower bound, not a matching polylogarithmic lower bound. Neither display claims a limit for a rescaled probability or a multiplicative equivalent.

For theta=1/2 the logarithms are base 2. Noncentral loops, varying theta, and growing r are excluded. Characteristic-formula and almost-sure-logic consequences still require the exact Jankov-Fine convention; no classification of K^as is claimed.

## 1. Exact probabilities

Fix a surjection with positive fibre sizes a_0,...,a_r, S=sum_{i>=1} a_i, a_0=m-S. The number Q of forbidden ordered edge coordinates is

    Q=sum_{i=1}^r a_i^2 + sum_{i!=j, i->j absent in D} a_i*a_j.

In particular Q>=sum a_i^2>=S^2/r by Cauchy-Schwarz. The fixed-map full probability and selected-witness probability are respectively

    rho^Q prod_{i->j in F(D)} (1-rho^{a_j})^{a_i},
    rho^Q prod_{j=1}^r (1-rho^{a_j})^{a_0}.

Indeed the forbidden coordinates and every individual required-hit row/fibre block are disjoint, and all coordinates are independent. A hit block of size k has probability 1-rho^k. These formulas do not assert independence between maps. Each size vector has multiplicity m!/(a_0!...a_r!). By linearity and Markov, p_m<=E[X_m]<=E[Z_m].

## 2. Uniform first-moment upper bound

All asymptotic estimates are for sufficiently large m, with constants allowed to depend on D,theta. Set C=8r and b_0=L-3 log_B L.

Large S>C L: the number of maps for fixed S is at most (mr)^S. Since log_B r<=L eventually, their contribution is at most

    B^{2LS-S^2/r} <= B^{-S^2/(2r)}.

Summing at most m possible values of S gives B^{L-C^2 L^2/(2r)}, negligible because C^2/(2r)=32r may be smaller than d for large fixed r. To avoid this issue choose instead C=8r^2 throughout, so C^2/(2r)=32r^3>d. With this choice the displayed inequality still holds.

Small fibre with S<=C L and some a_i<b_0: a_0>=m/2 eventually and m rho^{a_i}>L^3. The corresponding hit factor is at most exp(-L^3/2). There are at most (m+1)(mr)^{C L} maps in this range. Their total contribution is exp(-L^3/2+O(L^2)), negligible.

Main range: S<=C L and all a_i>=b_0. The multinomial is at most m^S/prod_i a_i!, and ln(k!)>=k ln k-k. Since all a_i>=L/2 eventually,

    log_B(multinomial) <= b S+O(L).

For nonnegative real x define

    P(x)=sum_i x_i^2+sum_{i!=j, i->j absent} x_i*x_j-b sum_i x_i.

At x=(b,...,b), P=d b^2. All off-diagonal coefficients are nonnegative. The partial derivative with respect to x_i is

    2x_i + sum_{j!=i} c_ij x_j - b,

where c_ij is the number of absent directed arrows between i and j (0,1,2). On the region x_i>=b_0 for all i, each derivative is >=2b_0-b>0 eventually. Write x_i=max(a_i,b) and delta_i=(b-a_i)_+. Then P(x)>=d b^2. On the segments from a to x each derivative is at most 2(C+r)L, because the total sum is <=(C+r)L. Integrating yields

    P(a)>=d b^2-2(C+r)L sum_i delta_i.

The base-B logarithm of the selected hit product is at most

    -a_0/(ln B) sum_i rho^{a_i}
      <= -L/(2 ln B) sum_{i:a_i<b} B^{delta_i},

using m rho^b=L and a_0>=m/2. Therefore the logarithm of each size-vector summand is at most

    -d b^2+O(L)+L sum_{i:a_i<b}
             [2(C+r)delta_i-B^{delta_i}/(2 ln B)].

The bracket has a finite upper bound on delta_i>=0. The number of size vectors in this range is <=(CL+1)^r, whose log is O(log L). Hence the full selected first moment has log at most -d b^2+O(L).

## 3. Balanced-map expectation lower bound

Choose a=ceil(b), s=ra, a_0=m-s. For large m, a_0>=a and s<=m/2. Restrict to maps M with each noncentral fibre of size a. Their number N=(m)_s/(a!)^r satisfies

    log_B N = r b^2+O(L),

as follows by bounding (m)_s between (m-s)^s and m^s and ln(a!) between a ln a-a and a ln a. Also Q=q a^2=q b^2+O(L). The number of required-hit blocks of a full map is at most (r+1)m, each of size >=a. Since rho^a<=L/m<=1/2 eventually, its success probability is at least

    c_m rho^Q, where c_m=exp(-2(r+1)L),

by ln(1-x)>=-2x for 0<=x<=1/2. Let Y count successful balanced maps; E[Y]>=c_m N rho^Q. This establishes the matching expectation lower bounds.

## 4. Second moment without the orientation hypothesis

For balanced maps f,g, let H_f,H_g denote their forbidden coordinate sets and U_f,U_g their noncentral supports, each of cardinality s. Write k=|U_f minus U_g|. For the i-th f-fibre, write k_i for the number of vertices outside U_g. Every ordered pair inside that fibre is forbidden (looplessness of D), and a^2-(a-k_i)^2>=a k_i such pairs have an endpoint outside U_g. They cannot lie in H_g. Summing over the disjoint within-fibre squares,

    |H_f intersect H_g|<=Q-a*k.

Hence joint success probability is at most rho^{Q+ak}. This weaker overlap inequality holds even when both arrows between noncentral labels are present.

For fixed f, at most binom(s,k) binom(m-s,k) r^s choices of g have the specified k. The decisive improvement is to retain k! rather than upper-bound binom(m-s,k) merely by m^k:

    sum_g P(B_f and B_g)
      <= rho^Q r^s sum_{k=0}^s binom(s,k) (m rho^a)^k/k!
      <= rho^Q (2r)^s exp(m rho^a)
      <= rho^Q (2r)^s exp(L).

Here binom(s,k)<=2^s and the truncated exponential series is at most the full series. In particular the second-moment loss has logarithm O(L) without needing a stronger overlap exponent lambda>1. Summing over f gives E[Y^2]<=N rho^Q (2r)^s exp(L).

By Cauchy-Schwarz,

    p_m>=P(Y>0)>=E[Y]^2/E[Y^2]
        >=c_m^2 N rho^Q (2r)^(-s) exp(-L).

Taking logarithms gives -d b^2-O(L) as required. This and section 2 prove the logarithmic estimates, including when d=0.

## 5. Critical case d=0: a separate Poisson bound

Here e=r(r-1), so all distinct noncentral pairs are bidirectionally adjacent and Q=sum_i a_i^2. The large-support and small-fibre contributions bounded in section 2 are exponentially negligible even relative to L^(-r/2).

On the main range, define lambda_i=m rho^{a_i}. Then using the multinomial bound and 1-x<=exp(-x), the selected summand is at most

    prod_i [lambda_i^{a_i} exp(-lambda_i)/a_i!]
       * exp(S sum_i rho^{a_i}).

Uniformly on this range, S<=CL and rho^{a_i}<=L^3/m, so the correction factor is exp(O(L^4/m))<=2 eventually. The main-range sum is bounded by twice the r-th power of

    T_m=sum_{integers a in [b_0,CL]} exp(-lambda_a) lambda_a^a/a!,
    lambda_a=m rho^a.

We show T_m=O(L^(-1/2)). For all such a, a>=L/2 eventually. Put t_a=lambda_a/a. As a increases by one, t_{a+1}/t_a=rho*a/(a+1)<rho. Hence the interval 1/2<=t_a<=2 contains at most 1+ceil(log_B 4) integers. For these terms, Stirling's lower bound a!>=c sqrt(a)(a/e)^a gives

    exp(-lambda_a) lambda_a^a/a!
       <= c^(-1) a^(-1/2) exp[-a(t_a-1-ln t_a)]
       <= c^(-1) a^(-1/2),

since t-1-ln t>=0 for t>0. For t_a outside [1/2,2], the quantity t_a-1-ln t_a is at least min(ln 2-1/2,1-ln 2)>0 by monotonicity on the two sides of 1. Every such term is O(exp(-c' L)), uniformly; there are O(L) terms. Thus T_m=O(L^(-1/2)).

Combining with the negligible tails proves E[Z_m]=O(L^(-r/2)), hence the same upper bound for p_m. This does not assert that the bound is attained: discrete rounding of the critical fibre scale can be important. In particular, the case r=1 includes the two-point central frame; its almost-sure-validity consequence is known in the literature, and priority for this quantitative bound must be checked.

## 6. Further work

- Noncentral looped vertices remain outside this proof. In particular F0001 and F1001 are not covered.
- Critical-case matching lower bounds, arithmetic oscillations, and the order-L coefficient in the noncritical regime are not settled.
- Audit novelty against the literature and obtain independent review.
- Existing Lean CI blocker remains; no claim of machine verification. The fixed-coordinate probability and factorial-based overlap sum are good formalization targets.
