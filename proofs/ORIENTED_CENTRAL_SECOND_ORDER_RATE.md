# Second-order logarithmic rate for oriented central targets

Status: internal hand proof, not Lean-formalized, refereed, or novelty-checked. This strengthens CHAIN_SHARP_EXISTENCE_RATE.md and generalizes the argument beyond paths.

## Theorem and scope

Fix r>=2 and a directed graph D on labels 1,...,r with no loops and at most one arrow between any two distinct labels (an oriented graph, not necessarily complete, connected or acyclic). Let e be its number of arrows. Form F(D) by adding vertex 0 with a loop and both arrows between 0 and every other vertex. For the labelled random directed frame G_m, all m^2 ordered edge bits including loops are independent Bernoulli(1/2).

Write L=log_2 m, b=L-log_2 L, q=r^2-e and d=q-r=r(r-1)-e>0. Let X_m count surjective bounded morphisms to F(D), let p_m=P(X_m>0), and let Z_m count surjective maps satisfying only the forbidden noncentral edges and the central-to-noncentral hits. Then, with constants depending on the fixed target,

    log_2 p_m = -d b^2 + O_D(L),
    log_2 E[X_m] = -d b^2 + O_D(L),
    log_2 E[Z_m] = -d b^2 + O_D(L).

Equivalently, for each of these three quantities the log is

    -d L^2 + 2d L log_2 L + O_D(L).

For the chain target e=r-1, d=(r-1)^2. In particular the previously undetermined L log L coefficient for the existence probability is 2(r-1)^2. No coefficient of the order-L term or multiplicative equivalent is claimed. This theorem excludes noncentral loops and bidirectional pairs; it does not establish the corresponding rates for F0001 or F1001. It is not a classification of K^as.

## 1. Fixed-map conditions

For a surjection with fibre sizes a_0,...,a_r>0, let S=sum_{i>=1} a_i, a_0=m-S. The number of forbidden ordered pairs is

    Q(a)=S^2 - sum_{i->j in D} a_i*a_j.

There are no forbidden pairs with a central endpoint. Every source row over label i must hit every fibre j for which i->j is an edge of F(D). These required-hit blocks and all forbidden coordinates are mutually disjoint. Thus the full fixed-map probability is

    2^(-Q) prod_{i->j in F(D)} (1-2^(-a_j))^a_i,

and the weaker witness probability is

    2^(-Q) prod_{j=1}^r (1-2^(-a_j))^a_0.

Linearity of expectation applies without independence between maps. A size vector has multiplicity m!/(a_0!...a_r!). Also p_m<=E[X_m]<=E[Z_m].

## 2. Upper bound on E[Z_m]

All estimates below are for sufficiently large m depending on the fixed target. Put C=8r and b_0=L-3 log_2 L. Split size vectors into three ranges.

### Large support: S>C L

Since D has at most one arrow per unordered pair,

    sum_{i->j} a_i*a_j <= sum_{i<j} a_i*a_j <= S^2/2,

so Q>=S^2/2. The total number of maps of support size S is <=(mr)^S. Dropping hit probabilities, their contribution is <=2^{S(2L-S/2)}<=2^(-S^2/4), using log_2 r<=L and S>=8L. Summing at most m values of S bounds the tail by 2^{L-C^2 L^2/4}, negligible versus 2^{-d b^2+O(L)} since C^2/4>d.

### Small fibre: S<=C L and min a_i<b_0

The central size a_0 is >=m/2. For any such small fibre the hit probability is <= exp(-a_0*2^(-a_i)) <= exp(-L^3/2). The number of maps is at most (m+1)(mr)^{C L}. This part is <=exp(-L^3/2+O_D(L^2)), negligible.

### Main range: S<=C L and every a_i>=b_0

The multinomial is bounded by m^S/prod_{i>=1} a_i!. The elementary inequality ln(k!)>=k ln k-k for k>=1 follows by integrating ln x from 1 to k. Since a_i>=L/2 for sufficiently large L, this gives

    log_2(multinomial) <= S*(L-log_2 L)+O_D(S) = b S+O_D(L).

Define the polynomial P(x)=(sum x_i)^2-sum_{i->j}x_i*x_j-b sum x_i on nonnegative real vectors. At the vector (b,...,b), P=d b^2. Its partial derivative is

    partial_i P=2 sum x_j - sum_{j adjacent to i in D} x_j - b,

where adjacent means one arrow in either direction; each j occurs at most once. If all coordinates are >=b_0, this derivative is >=sum x_j + x_i-b >=(r+1)b_0-b>0 for large L.

Let x_i=max(a_i,b) and delta_i=(b-a_i)_+ (nonnegative part). Monotonicity on coordinates >=b_0 implies P(x)>=P(b,...,b)=d b^2. Along the segments increasing a to x, the total sum is at most (C+r)L, and each partial derivative is at most 2(C+r)L. The mean-value theorem (or direct integration of this polynomial derivative) therefore gives

    P(a) >= d b^2 - 2(C+r)L sum_i delta_i.

This derivative bound explicitly accounts for small departures below b; we do not assume the signed quadratic remainder of a Taylor expansion is nonnegative.

The base-2 log of the selected hit product is bounded above by

    -a_0/(ln 2) * sum_i 2^(-a_i)
      <= -L/(2 ln 2) * sum_{i: a_i<b} 2^(delta_i),

because m*2^(-b)=L and a_0>=m/2. Thus each size-vector summand has log at most

    -d b^2 + O_D(L)
      + L * sum_{i: a_i<b} [2(C+r)delta_i - 2^(delta_i)/(2 ln 2)].

The bracket is uniformly bounded above for all real delta_i>=0, since the exponential dominates the linear function. There are at most r such terms. Hence each summand is <=2^{-d b^2+O_D(L)}, uniformly. The number of main-range size vectors is <=(C L+1)^r, whose log is O_D(log L). Combining all three ranges proves the upper bound.

## 3. Balanced-map expectation lower bound

Choose integer a=ceil(b), s=r*a, and all noncentral fibres of size a; for large m, m-s>=a and s<=m/2. Let M be these balanced maps, N=|M|=(m)_s/(a!)^r. Using (m-s)^s/a^s <= N <= m^s/(a!)^r and the preceding factorial inequality gives

    log_2 N = s*(L-log_2 a)+O_D(L)= r b^2+O_D(L).

Indeed a=b+O(1)=L-log_2 L+O(1), and log_2 a=log_2 L+O(log L/L). Also Q=q*a^2=q*b^2+O_D(L). All hit blocks have size >=a and their number is at most (r+1)m. Since 2^(-a)<=L/m<=1/2, the conditional probability of all hits given forbidden-edge absence is at least

    (1-L/m)^((r+1)m) >= exp(-2(r+1)L) = c_m,

using ln(1-x)>=-2x for 0<=x<=1/2.

For Y counting successful maps in M, E[Y]>=c_m N 2^(-Q). This already matches the upper bound for both E[X_m] and E[Z_m] to order O_D(L).

## 4. Stronger forbidden-set overlap bound

For f,g in M let U_f,U_g be the noncentral supports of size s and k=|U_f minus U_g|. Write H_f,H_g for forbidden ordered-coordinate sets, each of size Q. Let k_i be the number of vertices in the i-th f-fibre outside U_g. Then sum_i k_i=k and 0<=k_i<=a.

Within each f-fibre all pairs are forbidden. The number of such coordinates lost on restricting to U_g is a^2-(a-k_i)^2>=a*k_i. In addition, for each unordered distinct pair i,j of noncentral labels, at least one of the two directed rectangles is forbidden. Choose one such rectangle for each pair. These rectangles and the within-fibre squares are disjoint. In that chosen rectangle the lost coordinates number

    a^2-(a-k_i)(a-k_j) = a(k_i+k_j)-k_i*k_j
      >= (a/2)(k_i+k_j),

because 2 k_i*k_j<=a(k_i+k_j). Every lost coordinate is outside H_g. Summing over all i and unordered pairs i<j gives

    |H_f intersect H_g| <= Q - ((r+1)/2)*a*k.

Equivalently, 2*(Q-|H_f intersect H_g|)>=(r+1)*a*k; this integer form is useful for exact testing. This proof works for any relabelling on the intersection of supports.

Let lambda=(r+1)/2>1. The joint full-success event is contained in the event that all coordinates in H_f union H_g are absent, so

    P(B_f and B_g)<=2^(-Q-lambda*a*k).

## 5. Second moment and matching probability lower bound

For each f and k, at most binom(s,k) binom(m-s,k) r^s maps g have support difference k. Thus

    sum_g P(B_f and B_g)
      <= 2^(-Q) r^s (1+m*2^(-lambda*a))^s.

Now a>=L-log_2 L implies

    m*2^(-lambda*a)<=m^{1-lambda} L^lambda -> 0.

It is therefore <=1 for all sufficiently large m, and E[Y^2]<=N 2^(-Q)(2r)^s. This improvement is why the smaller optimal fibres do not cost an extra L log L term in the second moment. The weaker old overlap bound with lambda=1 would not suffice for this step.

Cauchy-Schwarz gives

    p_m>=P(Y>0)>=E[Y]^2/E[Y^2]
       >= c_m^2 N 2^(-Q)(2r)^(-s).

The logarithms of c_m^2 and (2r)^(-s) are both O_D(L). Together with log_2 N-Q=-d b^2+O_D(L), this gives the matching lower bound for p_m. The upper bound from section 2 proves the theorem.

## 6. Checks and research obligations

- For paths e=r-1; for an empty noncentral graph e=0; for any tournament e=r(r-1)/2. The leading two logarithmic coefficients depend only on r and e within this class. No assertion about equality of actual probabilities for nonisomorphic targets is made.
- The proof uses fixed r, labelled fair ordered-edge bits and the specified central-point convention. It does not cover growing r, noncentral loops, bidirectional noncentral edges, or nonuniform edge probabilities.
- The next precision target is the order-L term, potentially sensitive to rounding of L-log_2 L and overlap multiplicities. It is not resolved here.
- Prioritize an independent proof review and literature search before claiming originality. No Lean proof of this theorem yet; previous CI blocker persists.
