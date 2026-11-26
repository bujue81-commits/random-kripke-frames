# High-bias oscillation for a four-point central target

Status: new internal hand proof, not Lean-verified or externally refereed; literature priority unverified. This is a separate biased-model result, not a change to the fair-model manuscript.

## Theorem

Let F be the four-point central target with canonical peripheral encoding 011011101. Relabel its points C,A,V,Z (V was called the B-fibre in TWO_STAGE_FORCED_FIBRE_POSITIVE.md). The only missing arrows are A->V, V->V, Z->A. Fix independent ordered source edges, including loops, of probability theta in (0,1). Put rho=1-theta, B=1/rho, L=log_B m, and let p_m(F) be the probability of a full surjective bounded morphism G_m ->> F.

Let T be the unique root greater than 2 of

    2+2 ln T-T=0.

Then T=5.35669398... and 1-1/(e T)=0.9313234165... . For every fixed

    theta > 1-1/(e T),

the image probability has

    liminf p_m(F)=0,     limsup p_m(F)=1.

Indeed the positive subsequence holds for every fixed theta in (0,1). The negative subsequence is proved below whenever one can choose a constant t>T with rho*t<1/e, precisely the stated strict range. No conclusion about the critical boundary or the intervening biases is asserted. At theta=1/2 the earlier proof gives p_m(F)->1.

## 1. Necessary forced fibres and size exclusions

In every successful map the V-fibre is independent, with all its internal ordered edges absent. Given its nonempty vertex set V of size b, the A-fibre is uniquely forced:

    A={x outside V : x has no outgoing edge into V}.

Similarly, outside A union V, the Z-fibre is exactly the rows missing A, and all rows of the entire source hit Z, a universally incoming target label. In particular if a=|A| and z=|Z| then both a,z are positive. In an actual map all rows in A union V must hit A; this additional condition may be dropped for an upper bound.

Let b0=L-3 log_B L, h=ceil(128 L). The probability of an entirely absent h-by-h rectangle is <=B^(2hL-h^2)=exp(-Omega(L^2)). Outside this exceptional event an independent fibre has b<h. Also with probability 1-o(1), no successful map can have b<b0 or z<b0. For b the label-specific tiny-fibre argument of NO_SINGLETON_MISS_DEGREE_CRITERION.md applies: the only universally incoming labels are C,Z, whose missing outgoing signatures are empty and {A}, respectively. Neither misses exactly V. On the complement of the rectangle exception the large labels form a complete core. For any fixed small disjoint fibres (each <h), an outside row that misses precisely V among these fibres and receives an edge from every small fibre would have to have a universal incoming label missing exactly V. Such a witness is impossible under a successful map. Its independent tests over outside vertices have success probability >=rho^b theta^7, and the probability of no witness when b<b0 is exp(-Omega(L^3)). The number of small-fibre configurations is exp(O(L^2)), so a union bound gives o(1). The tests are not conditioned on the rectangle event. For z the simpler union bound suffices: if a set of size z<b0 is hit by every row, its probability for fixed set is (1-rho^z)^m<=exp(-L^3). Summing over <=m^(ceil(b0)+1) such choices gives o(1). Thus, up to a probability o(1), restrict b0<=b<h and z>=b0.

Fix a deterministic b-subset V and condition only on internal independence. Reveal columns ending in V, which determine A, whose size has distribution Bin(m-b,rho^b). Conditional on these columns the columns ending in A are fresh, even though A was selected adaptively: for each revealed outcome A is disjoint from V. Let Z* be all rows outside A union V missing A. Its size conditional on this history has distribution Bin(m-b-a,rho^a). A successful map with V has Z=Z*. Write lambda=m*rho^b. The expected number of independent b-sets is

    N_b=binom(m,b)*rho^(b^2) <= lambda^b/b! <= (e lambda/b)^b.

On the size range b0<=b<h, lambda<=L^3 and b=O(L), so N_b<=exp(O(L ln L)) uniformly.

Fix epsilon>0 and put u=(1+epsilon)L. If a>u, the mean of |Z*| is <=m*rho^a<=m^(-epsilon). The binomial upper-tail bound, obtained by a union bound over subsets of ceil(b0) successes and binom(n,j)<=(en/j)^j, gives

    Pr(|Z*|>=b0 | V-column history)
       <= (e*m^(-epsilon)/ceil(b0))^ceil(b0)
       = exp(-Omega(L^2)).

This is uniform for a>u and b in the main size range. Multiply by N_b, sum O(L) possible b, and include the earlier exceptions. Therefore the probability of any successful map with a>(1+epsilon)L tends to zero for every fixed epsilon>0. This bound is about existence, not a claim that the typical independent set has a small forced A-fibre.

## 2. Positive subsequence

Fix any fixed bias. For integers k->infinity choose

    m_k^+ = round((1/2)*k*B^k).

Then L=k+log_B k+O(1), and b=k gives lambda/L=m_k^+ rho^k/L -> 1/2. Thus the independent set expectation has

    ln N_k = k*(1+ln(lambda/k))-(1/2)ln(2*pi*k)+o(1)
           = (1-ln 2+o(1))*L.

The second-moment computation in TWO_STAGE_FORCED_FIBRE_POSITIVE.md needs only b=L-log_B L+O(1) and N_b growing exponentially in L. For completeness, with overlap j of two independent uniform b-subsets, write P_j for its probability. The normalized second moment of their independent-set count is sum_j P_j rho^(-j^2). For 1<=j<=b/2 use

    P_j rho^(-j^2) <= (b^2 B^(b/2)/(m-b))^j,

whose base tends to zero. For j>b/2 put d=b-j and use

    P_j rho^(-j^2) = N_b^(-1) binom(b,d) binom(m-b,d) rho^(2bd-d^2)
                    <= N_b^(-1)*(bm rho^(3b/2))^d.

The base tends to zero and N_b grows. Thus the relative variance tends to zero.

Conditional on a fixed independent V, its forced A has size between alpha L and beta L with probability 1-o(1), for any constants 0<alpha<1/2<beta<1, by Chernoff. After revealing A columns, all rows in A union V hit A except with probability O(L)rho^(alpha L)=o(1). The forced Z has mean between (m-O(L))m^(-beta) and m^(1-alpha), and has size between m^(1-beta)/3 and m/4 a.a.s. The remainder C has size >=m/2. Their columns are unexposed, conditional on the history of V and A columns; every row hits Z and C except with probability <=m(rho^(m^(1-beta)/3)+rho^(m/2))=o(1). Therefore every fixed independent V completes with conditional probability 1-o(1), uniformly. By linearity, the expected number of bad independent V is o(N_b); Markov and concentration of the independent-set count yield at least one successful completion a.a.s. This avoids selecting an independent set using information that might invalidate the fresh-column law.

Hence p_(m_k^+)(F)->1 at every fixed bias.

## 3. Negative subsequence at high bias

Assume t>T and rho*t<1/e. For integers k->infinity put

    m_k^- = round(t*k*B^k).

Again L=k+log_B k+O(1), lambda(k)/L->t, lambda(k+1)/L->rho*t.

We use Section 1 to restrict to b0<=b<h, a<=u=(1+epsilon)L, and z>=b0, where epsilon is a fixed small positive constant chosen below. Separate the integer b at the jump between k and k+1.

### 3a. b>=k+1: independent fibres are too rare

Choose a fixed gamma with rho*t<gamma<1/e. Since lambda(b)=m*rho^b decreases in b, for b>=k+1 and large k, lambda(b)<=gamma L. Uniformly b>=b0=(1-o(1))L, the first-moment bound

    N_b <= (e*lambda(b)/b)^b

is <=exp(-c L) for some c>0 because e gamma<1. There are O(L) possible b<h. Thus no such independent V exists a.a.s.

### 3b. b<=k: the forced A-fibre is too large

Let s=lambda(b)/L. For b<=k we have s>=t-o(1), b<=L eventually and b>=b0. Fix a constant t0 with T<t0<t. Since t0>2, choose small constants epsilon>0, delta>0 such that

    (1-delta)t0 > 2+epsilon,
    F_(epsilon,delta)(t0) < 0,

where

    F_(epsilon,delta)(s)
       = 2+epsilon+(2+epsilon) ln s
         -(1+epsilon) ln(1+epsilon)-(1-delta)s.

Such choices exist by continuity and 2+2 ln t0-t0<0. The derivative (2+epsilon)/s-(1-delta) is negative for s>=t0, so F_(epsilon,delta)(s)<=F_(epsilon,delta)(t0)<0 uniformly.

For a fixed independent V, the forced A-size has binomial mean mu=(m-b)rho^b. Uniformly in the main range b=O(L), for sufficiently large k we have (1-delta)lambda<=mu<=lambda. Thus mu>u=(1+epsilon)L. The binomial lower-tail bound is

    Pr(a<=u | V independent) <= exp(-mu+u+u ln(mu/u)).

It follows directly from Markov applied to exp(-v a) with v=ln(mu/u)>0 and (1-q+q e^(-v))^(m-b)<=exp(mu(e^(-v)-1)). Replacing -mu by -(1-delta)lambda and the logarithm's mu by lambda increases the bound, so

    Pr(a<=u | V independent)
       <= exp(L[-(1-delta)s+(1+epsilon)
                    +(1+epsilon)ln(s/(1+epsilon))]).

Meanwhile, b<=L and lambda=sL>L. The function x(1+ln(lambda/x)) is increasing on 0<x<=L, since its derivative is ln(lambda/x)>0. Hence

    ln N_b <= b(1+ln(lambda/b)) <= L(1+ln s).

Multiplication gives the expected number of independent V with a<=u at size b at most exp(L F_(epsilon,delta)(s)), which is <=exp(-c' L) uniformly over b<=k in the main range. The sum over O(L) sizes tends to zero. With the exclusions in Section 1 and Section 3a this proves p_(m_k^-)(F)->0.

## 4. Threshold and scope

The function 2+2 ln t-t has derivative 2/t-1, is positive at 2, strictly decreases on (2,infinity), and tends to minus infinity. Thus there is exactly one root T>2. A constant t>T with rho*t<1/e exists iff rho<1/(e T). This proves the theorem. For the simple explicit example theta=0.96, B=25, choose t=8; rho*t=0.32<1/e and 2+2 ln 8-8<0. Then the positive subsequence can be m=round(k*25^k/2), the negative m=round(8*k*25^k).

This is a failure of convergence for a fixed four-point central bounded-morphic target at sufficiently high fixed bias; no assertion is made that the displayed threshold is sharp. The fair model classification is unchanged. By the ordinary characteristic-formula translation on R^2 universal frames, the corresponding ordinary modal frame-validity probability also has liminf 0 and limsup 1 at these biases; the exponential R^2 error tends to zero. This is not the first general failure of the modal frame zero-one law: Le Bars already established failure in the fair setting. Prior work on directed kernels and integer-size effects is relevant. A targeted literature search located Goranko 2020 (https://www.aiml.net/volumes/volume13/Goranko.pdf) and Le Bars's random-digraph kernel estimates (https://ndl.ethernet.edu.et/bitstream/123456789/77242/1/25.pdf); it did not establish priority for this particular four-point target or bias interval. No external peer review or Lean verification is claimed.
