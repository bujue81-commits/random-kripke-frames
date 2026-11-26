# Final fair-model target: growing witnesses and a polynomial existence lower bound

Status: partial result, internal hand proof. This does not establish the limit of p_m for 011010111. No Lean, external referee or priority claim. Use the exact forced-pair formulas of LAST_FOUR_POINT_FORCED_PAIR.md. The source is fair independent ordered edges, loops included. Put L=log_2 m, rho=1/2.

## Statement

For the target with missing arrows A->A, Z->A, Z->B, choose sizes

    a=round(L-log_2 L-1),
    z=a+2,
    k=ceil(L+2 log_2 L),
    c=m-a-z-k.

Ties in round can be resolved either way. All sizes are positive for large m. Let Y count sufficient witnesses with these precise sizes (A independent, Z forced, B=M forced as in the prior document, C remaining). Define t=m*2^(-a)/L, so sqrt(2)<=t<=2sqrt(2); m*2^(-z)/L=t/4. Then, with natural logarithms,

    ln E[Y] = L f(t)+O(log L),
    f(t)=3+3 ln t-ln 4-3t/2.

In particular, f(t)>=0.48 on the entire interval and E[Y]>=exp(0.47 L) for all sufficiently large m. This is uniform over the integer-size oscillation; it is not only a subsequence assertion.

Also, writing p_m for existence of any full surjective bounded morphism onto the target,

    p_m >= exp(-3.2 L-O(log L))

for large m. In particular p_m>=m^(-5) eventually, and log_2 p_m=O(L). These are lower bounds only, not a proof of convergence to one, zero, or a nontrivial limit.

## 1. Fixed-size first moment

For fixed disjoint A,Z, with n=m-a-z, the prior exact formula is

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

The function f is concave (f''=-3/t^2), so its minimum on [sqrt(2),2sqrt(2)] is at an endpoint. The values are 3-0.5 ln 2-3 sqrt(2)/2 and 3+2.5 ln 2-3 sqrt(2), respectively; both exceed 0.48. Thus the claimed uniform exponential-in-L growth follows.

## 2. Independent-set comparison gives a nontrivial existence lower bound

Let X count independent a-subsets including absent loops. Y<=X for each realization because both Z and M are uniquely determined by A. The mean is

    E[X]=binom(m,a)*rho^(a^2)
        =(1+o(1))*lambda_a^a/a!,

with ln E[X]=L*(1+ln t)+O(log L), so E[X] grows exponentially in L.

We show E[X^2]/E[X]^2=1+o(1). For two uniformly random a-subsets, let P_j denote the probability their intersection size is j. The normalized second moment is sum_j P_j*rho^(-j^2). For 1<=j<=a/2, the union bound for containing a particular j-subset gives

    P_j*rho^(-j^2) <= (a^2*2^(a/2)/(m-a))^j.

The geometric base tends to zero; sum is o(1). For j>a/2, write d=a-j. The exact intersection count gives

    P_j*rho^(-j^2)
      = E[X]^(-1)*binom(a,d)*binom(m-a,d)*rho^(2ad-d^2)
      <= E[X]^(-1)*(a*m*rho^(3a/2))^d.

Again the geometric base tends to zero, and E[X]->infinity, so the sum is o(1). The j=0 term is <=1; the lower bound 1 follows from nonnegative variance. This proves the second-moment claim.

Now E[Y^2]<=E[X^2], so Cauchy-Schwarz gives

    p_m>=P(Y>0)>=E[Y]^2/E[Y^2]
                 >=(1-o(1))*(E[Y]/E[X])^2.

The log ratio is -L*g(t)+O(log L), where

    g(t)=1+ln t-f(t)=3t/2-2-2 ln t+ln 4.

Convexity (g''=2/t^2) bounds its maximum by the larger endpoint value. At t=sqrt(2) this is 3sqrt(2)/2-2+ln 2; at t=2sqrt(2) it is 3sqrt(2)-2-ln 2. Both are less than 1.6. Therefore ln p_m>=-3.2 L-O(log L). Since 3.2/ln 2<5, the eventual m^(-5) lower bound follows. This rules out the exp(-Omega((ln m)^2)) decay seen in many earlier targets, but does not rule out p_m->0.

## 3. Disjoint-support contribution to the actual second moment

This observation identifies the remaining obstacle to the limit proof. Regard Y as a sum over ordered disjoint triples A,Z,M of the stated sizes, and let Y0 count the corresponding necessary witnesses with M exactly the outside common nonneighbors of Z. Then E[Y]/E[Y0]=1+o(1) by the preceding formula.

For two candidate triples with disjoint supports A union Z union M and A' union Z' union M', their necessary event constraints overlap only on the six blocks Z x A', Z x Z', Z x M', Z' x A, Z' x Z, Z' x M. To see this, a necessary triple event specifies internal A absence, Z->A absence, exact A-hits of outside rows, all row hits of Z, Z->M absence, at least one edge from Z into every outside column in C, and all non-Z row hits of M. No condition is imposed on non-Z rows' edges to C. For disjoint supports the only shared coordinates belong to the six blocks listed. In each such block one event requires every row to hit that block's column set, and the other requires every column to be hit from that block's row set. There are no forbidden rectangles on those blocks.

The joint row-and-column hit probability in each block is 1-o(1) by the union bound, since its dimensions are L+O(log L) and rho^(min dimension)=O(L/m). The marginal row-only and column-only probabilities are likewise 1-o(1). All constraints on coordinates outside these cross blocks are independent between the two events, and independent of the cross blocks. Thus for any two disjoint-support triples,

    P(necessary_1 and necessary_2)
      =(1+o(1))*P(necessary_1)*P(necessary_2)

uniformly. The count of such ordered pairs is (1-o(1)) times the square of the number of triples, as a+z+k=O(L). This means the disjoint-support part of E[Y0^2] equals (1+o(1))*E[Y0]^2. It is not an upper bound on the entire second moment: intersecting supports can have much larger joint probabilities and require separate estimates. If that contribution can be shown o(E[Y0]^2), concentration of Y0 plus E[Y0-Y]=o(E[Y0]) would establish p_m->1.

## Scope and related work

The original fair-model census remains 103/104; no change to the number of minimal frames. For this target the previous exact formulas are now supplemented by uniform growing expected sufficient witnesses and a polynomial existence lower bound. The second moment for intersecting-support witnesses remains unresolved. Independent-set and domination second moments are standard methods in random graph theory; see Wieland and Godbole, On the Domination Number of a Random Graph, and Goranko, The modal logic of almost sure frame validities in the finite (2020). A targeted bibliographic search did not establish priority of these specific estimates. No Lean proof or CI result is claimed.
