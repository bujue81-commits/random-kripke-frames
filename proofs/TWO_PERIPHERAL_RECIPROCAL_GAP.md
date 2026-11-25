# Two nonadjacent peripheral vertices with optional loops

Status: internal hand proof, not Lean-verified or externally refereed. Literature priority is unverified. This connects the original F0001/F1001 targets to the later second-order rate results.

## Theorem

Let F have vertices c,A,B; c is reflexive and joined in both directions to every vertex. Neither A->B nor B->A is present. Each peripheral loop may be present or absent independently. Write epsilon_A,epsilon_B in {0,1} for absence of the corresponding loop, and d=epsilon_A+epsilon_B. Thus F0001 has d=1, F1001 has d=0, and the two-loopless target has d=2.

Use the labelled independent ordered-edge model including loops, with fixed edge probability theta in (0,1). Set rho=1-theta, B=1/rho, L=log_B m, b=L-log_B L. Let p_m be the probability that a surjective bounded morphism onto F exists; X_m counts such maps, and Z_m counts surjective maps satisfying only all forbidden rectangles and all central rows hitting each peripheral fibre.

For each fixed target and theta,

    log_B p_m = -d b^2+O_theta(L),
    log_B E[X_m] = -d b^2+O_theta(L),
    log_B E[Z_m] = -d b^2+O_theta(L).

For d>0 this determines the leading and second logarithmic coefficients. In particular F0001 in the fair model has

    log_2 p_m = -(log_2 m)^2
                 +2 log_2 m log_2(log_2 m)+O(log m).

This substantially strengthens the earlier O(1/sqrt(log m)) upper bound. For d=0 additionally

    p_m<=E[X_m]<=E[Z_m]=O_theta(1/L).

Along m_k nearest to k B^k, the two expectations for d=0 are both asymptotic to 1/(2 pi k). Along n_k nearest to c k B^k, for any fixed 1<c<B, both are <=exp(-delta L) for some delta>0. These subsequence claims concern expectations, not an established matching lower bound on p_m. The result for d=0 gives only a polynomial lower bound on p_m from the general logarithmic estimate.

## 1. Exact fixed-map event

Denote the fibre sizes by u,v,w=m-u-v, all positive. The forbidden-coordinate count is

    Q=2uv+epsilon_A*u^2+epsilon_B*v^2.

The selected probability is

    rho^Q (1-rho^u)^w (1-rho^v)^w.

The full probability is this times (1-rho^w)^m and, for each present peripheral loop, its additional self-hit factor: (1-rho^u)^u if epsilon_A=0 and (1-rho^v)^v if epsilon_B=0. This follows from independence of mutually disjoint forbidden coordinate rectangles and required-hit row/fibre blocks. Multiply by m!/(u!v!w!) and sum to obtain the two expectations. Markov gives p_m<=E[X_m]<=E[Z_m].

## 2. First-moment upper bound, including the large-support issue

The argument for loopless noncentral graphs cannot simply be reused: Q need not control (u+v)^2 when a peripheral loop is present. Instead split according to the smaller and larger peripheral fibres. Write i=min(u,v), j=max(u,v), b_0=L-3 log_B L, C=8. For asymptotic inequalities take m sufficiently large. Constants may depend on theta.

### Small minimum i<b_0

Drop all forbidden terms except the two cross rectangles and retain only the central hit factor for the fibre of size i. Put t=rho^i. For a fixed choice of which label has the smaller fibre, the contribution for i is at most

    binom(m,i) sum_{j>=i} binom(m-i,j) t^{2j}(1-t)^{m-i-j}
    <= binom(m,i) binom(m-i,i) t^{2i}(1-t+t^2)^{m-2i}.

In the sum j<=m-i; extending to include empty central fibres only enlarges it. The inequality follows by choosing i elements of the second fibre, which counts each j-subset binom(j,i)>=1 times, then applying the binomial theorem. Here i<=L, m-2i>=m/2, t<=rho<1 and m t>L^3. Bounding binomial coefficients by m^i and t^{2i}<=1, the result is at most

    exp(2i ln m -(1-rho)L^3/2).

After summing over O(L) small i and two label choices, this is exp(-Omega_theta(L^3)), negligible even relative to B^{-2 b^2}.

### Large maximum j>C L, with i>=b_0

For each vector the multinomial is <=m^{i+j}. Dropping hits and optional self-forbidden squares,

    log_B(summand) <= (i+j)L-2ij
                    = j[L-(2-L/j)i].

Since j>8L and i>=b_0>=0.9 L eventually, (2-L/j)i-L >= (15/8)*0.9 L-L >= L/2. Thus the summand is <= B^{-jL/2} <= B^{-4L^2}. Summing over at most m^2 vectors gives at most B^{-4L^2+2L}, negligible for d<=2.

### Main range b_0<=u,v<=C L

Factorial bounds ln(k!)>=k ln k-k give

    log_B(multinomial) <= b(u+v)+O(L)

uniformly. Define P(u,v)=Q-b(u+v) on positive reals. At (b,b), P=d b^2. Its partial derivatives are 2v+2 epsilon_A u-b and 2u+2 epsilon_B v-b; both are positive on u,v>=b_0 for large L. If delta_u=(b-u)_+ and delta_v=(b-v)_+, clipping each coordinate upward to at least b and integrating the derivatives (which are <=4(C+1)L along these segments) yields

    P(u,v)>=d b^2-4(C+1)L(delta_u+delta_v).

Also w>=m/2 and m rho^b=L. The log_B of the selected hit product is <= -(L/(2 ln B))*sum_{x in {u,v}, x<b} B^{b-x}. The sum is over the two labelled coordinates, counted with multiplicity. The negative exponential terms absorb the positive linear deficit terms because K delta-B^delta/(2 ln B) is bounded above on delta>=0 for fixed K. Hence the log of each main-range summand is <= -d b^2+O(L), uniformly. There are O(L^2) vectors. Together with the tails this proves the upper bound for E[Z_m].

## 3. Balanced maps and the second-moment lower bound

Choose a=ceil(b) and restrict to maps with both peripheral fibres of size a. Their count N=(m)_{2a}/(a!)^2 satisfies log_B N=2b^2+O(L) by factorial bounds; Q=(2+d)a^2=(2+d)b^2+O(L). The central fibre has at least a vertices for sufficiently large m. The number of required row hits for any full map is at most 3m, each has at least a available edge coordinates, and rho^a<=L/m. Thus its success probability is >= c_m rho^Q, with c_m=exp(-6L), by ln(1-x)>=-2x for x<=1/2.

For maps f,g let H_f,H_g be their forbidden sets and let k be the number of noncentral f-vertices outside the noncentral g-support. Write k_A,k_B for those counts in f's two peripheral fibres. Each of the two forbidden cross rectangles loses a^2-(a-k_A)(a-k_B) coordinates on restriction to g's support. Both sets of lost coordinates are disjoint and outside H_g. Consequently

    Q-|H_f intersect H_g|
      >= 2a(k_A+k_B)-2 k_A k_B
      >= a(k_A+k_B)=a k,

since 2 k_A k_B<=a(k_A+k_B). Optional missing loop rectangles only add more lost coordinates. This is valid with arbitrary relabelling of the common support.

Therefore joint success probability <=rho^{Q+a k}. For fixed f the number of g with support difference k is at most binom(2a,k)binom(m-2a,k)2^{2a}. Retaining the factorial in the second binomial gives

    sum_g P(B_f and B_g)
      <= rho^Q 2^{2a} sum_k binom(2a,k)(m rho^a)^k/k!
      <= rho^Q 4^{2a} exp(L).

Let Y count successful balanced maps. Then E[Y]>=c_m N rho^Q and E[Y^2]<=N rho^Q 4^{2a} exp(L). By Cauchy-Schwarz,

    p_m>=P(Y>0)>=c_m^2 N rho^Q 4^{-2a} exp(-L).

Taking logs proves the matching lower bound -d b^2-O(L) for p_m; the expectation lower bounds follow as well. No independence between map-success events was assumed.

## 4. Critical F1001: Poisson cross-sum, uniform bound and lattice subsequences

Suppose d=0, so Q=2uv. The tails in section 2 are negligible. In the main range define lambda_j=m rho^j. The selected size-vector summand is at most

    exp((u+v)(rho^u+rho^v))
      * pi_{lambda_u}(v) pi_{lambda_v}(u),

where pi_l(k)=exp(-l) l^k/k!. This follows by bounding the multinomial by m^{u+v}/(u!v!) and the hit factors by exp(-w(rho^u+rho^v)). The correction factor is 1+O(L^4/m), uniformly, since u+v<=2CL and rho^u,rho^v<=L^3/m. In fact both the full and selected summands equal the Poisson product times 1+o(1) uniformly on this range: the falling factorial relative error is O(L^2/m); log hit approximation errors are O(L^6/m); the central hit and extra self-hit factors tend uniformly to 1. For the latter, m rho^{m-2CL}->0 and CL rho^{b_0}->0.

For off-diagonal u<v put j=v-u>=1. The ratio of the two normalized means is

    (lambda_u/v)/(lambda_v/u)=B^j*u/(u+j).

For all u>=b_0 and large m, B^j*u/(u+j) is strictly increasing with integer j>=1 (the successive ratio is B*(u+j)/(u+j+1)>1), and its value at j=1 is bounded below by sqrt(B)>1. Thus at least one of the two normalized means lies outside [B^(-1/8),B^(1/8)]; if both belonged to that interval their ratio would be <=B^(1/4). By Stirling,

    pi_{tk}(k) <= C0*k^(-1/2) exp[-k I(t)],
    I(t)=t-1-ln t>=0.

Outside the displayed interval I(t) has a positive lower bound depending only on B, and u,v>=L/2. Hence each off-diagonal term is exponentially small in L, even after summing O(L^2) terms. The same argument applies when v<u.

On the diagonal put t_u=lambda_u/u. It decreases by a factor strictly less than rho per unit step, so only O_theta(1) indices have t_u in [1/2,2]. Each squared Poisson mass is O(1/L) there; every other term is exponentially small by the same rate-function estimate. This proves the uniform O(1/L) bound.

For m_k nearest integer to k B^k, lambda_k=k+O(rho^k), L/k->1, and the balanced diagonal summand is (1+o(1))/(2 pi k) by Stirling and the uniform approximation. All other diagonal t_u stay bounded away from 1: the immediate neighbours tend to B and 1/B, and t_u is strictly decreasing. Their sum and all off-diagonal terms are exponentially small. Therefore both E[X_{m_k}] and E[Z_{m_k}] are asymptotic to 1/(2 pi k).

For n_k nearest to c k B^k with fixed 1<c<B, t_k->c and t_{k+1}->c/B. Every diagonal t_u stays away from 1; all diagonal and off-diagonal contributions are exponentially small. Thus both expectations are <=exp(-delta L) for some delta>0. This concludes the theorem.

## 5. Limits

- Does not treat asymmetric cross adjacency (only one or neither direction absent), additional peripheral vertices, or varying edge probability.
- For F1001 the resonant existence-probability lower bound remains unresolved. No matching lower bound of order 1/L is claimed.
- Does not establish novelty, characteristic-formula conventions, or a classification of almost-sure modal logic.
- No machine verification; CI access remains blocked. The proof should receive independent review before publication.
