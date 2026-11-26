# Sharp fixed-bias finite-model threshold for 011010111

Status: internal hand proof, not independently reviewed, Lean-verified, or priority-certified. This is a separate biased-model result; the fair manuscript remains unchanged.

## Theorem

Fix independent ordered edge probability theta in (0,1), with loops included, put rho=1-theta, B=1/rho and L=log_B m. Let F=011010111 have labels C,A,Z,M, with C universal and missing arrows exactly A->A, Z->A, Z->M. Write p_m(F) for the probability of a full surjective bounded morphism G_m ->> F. Define

    rho_* = (3 sqrt(3)-5)/4 = 0.049038105676658...
    theta_* = 1-rho_* = 0.950961894323342...

Then:

- If rho>rho_* (theta<theta_*), limsup p_m(F)=1.
- If 0<rho<=rho_* (theta>=theta_*), p_m(F)->0.

In particular this is an exact threshold for positive limsup, not a classification of the full limit in the positive regime. At theta=1/2 the earlier full-sequence proof gives p_m(F)->1. The boundary rho=rho_* is included in the zero case by a separate polynomial prefactor estimate below.

## 1. Forced sets and reduction to logarithmic sizes

Use the deterministic reduction and exact probability formula of LAST_FOUR_POINT_FORCED_PAIR.md. A is independent including absent loops; Z consists of all rows outside A missing A. Let M0 be all vertices outside A union Z receiving no edge from Z, and C0 its remaining complement outside A union Z. The actual M-fibre is contained in M0. A necessary witness requires all rows to hit Z and all non-Z rows to hit M0. A sufficient witness assigns M=M0 and C=C0 if C0 is nonempty and every row hits C0.

Let a=|A|, z=|Z|, k=|M0|. Set b0=L-3 log_B L and h=ceil(128 L). The tiny-fibre exclusion lemma in NO_SINGLETON_MISS_DEGREE_CRITERION.md applies to every label of F: the only universally incoming columns are C and Z, whose outgoing missing sets are respectively empty and {A,M}; neither misses exactly one label. This lemma does not use the degree hypothesis when it is used only for tiny-fibre exclusion. Except on an event of probability o(1), every successful map has all fibres >=b0. The absent h-by-h rectangle probability is <=B^(2hL-h^2), and outside it a<h by independence. Hence every successful map, apart from o(1) probability, has b0<=a<h, z>=b0 and k>=b0 (because the actual M-fibre is contained in M0).

For a fixed independent a-set A, revealing A columns makes Z forced, with z~Bin(m-a,rho^a). Conditional on this column history, the coordinates Z x ([m] minus (A union Z)) are fresh; hence k~Bin(m-a-z,rho^z). These two binomial laws do not condition on the Z-hit or M-hit events. The expected count of independent a-sets is N_a=binom(m,a)rho^(a^2)<=(e m rho^a/a)^a. On b0<=a<h we have m rho^a<=L^3, a>=L/2 and a<=129 L eventually, so N_a<=exp(400 L ln L) uniformly for sufficiently large m.

Fix K=1000 and u=L+K log_B L. If a>u, the conditional mean of z is <=L^(-K). Thus the probability z>=b0 conditional on independence is <=(e L^(-K)/ceil(b0))^ceil(b0)=exp(-(K+1+o(1))L ln L), by the union bound over ceil(b0) binomial successes. Multiply by N_a and sum O(L) sizes: the probability of any successful map with a>u is o(1). If z>u, conditional on the A-column history the mean of k is <=L^(-K); the same upper tail bound holds for k>=b0, uniformly over these histories. Multiply again by N_a and sum a in the main range. This also gives o(1). No separate enumeration of large Z is necessary because it is uniquely forced by A. Consequently it suffices for an upper existence bound to count necessary witnesses with

    b0<=a,z<=u,   k>=b0.                 (1)

In particular a,z=L+O(log L), and t=m rho^a/L, s=m rho^z/L are between L^(-K-1) and L^2. Both |ln t| and |ln s| are O(ln L).

## 2. Uniform first-moment upper bound on the main range

For fixed a,z let n=m-a-z and lambda_a=m rho^a, lambda_z=m rho^z. By the exact necessary-witness formula, the expected count at these sizes with k>=b0 is

    binom(m,a)binom(m-a,z) rho^(a^2+az)
    * (1-rho^a)^n (1-rho^z)^m
    * E[1_(K0>=b0) (1-rho^K0)^(m-z)],

where K0~Bin(n,rho^z). (Here K0 is a random integer, not the fixed constant K.) Bound the first two lines by

    (lambda_a^a/a!)(lambda_a^z/z!)
    * exp(-lambda_a-lambda_z+O(L^4/m)).       (2)

This follows from the multinomial upper bound m^(a+z)/(a!z!), and n rho^a=lambda_a-O(L^4/m). All errors uniform on (1). Stirling, a,z=L+O(log L), |ln t|=O(log L), give the logarithm of (2) at most

    L(2+2 ln t-t-s)+O((ln L)^2).

If s>=1, bound the expectation in the third line by 1. If s<1, use Chernoff with nonnegative parameter v=ln(1/s), since the binomial mean is <=sL:

    P(K0>=b0) <= exp(sL(e^v-1)-v b0)
              <= exp(L(1-s+ln s)+O((ln L)^2)).

This argument works even when the mean is slightly above b0; the exponential upper bound need not be below 1 in that case. Thus the main-size expected count is at most exp(L H(t,s)+O((ln L)^2)), uniformly, with

    H(t,s) = 2+2 ln t-t-s                  if s>=1,
           = 3+2 ln t+ln s-t-2s           if s<=1.

The integer difference d=z-a implies s/t=r=rho^d exactly. Define

    g(r)=ln(27r/(1+2r)^3).

For 0<r<1, the maximum of H(t,rt) over t>0 is g(r), attained uniquely at t=3/(1+2r), with rt<1. Indeed on rt<=1 the expression is 3+3ln t+ln r-(1+2r)t, strictly concave in t, maximized at the stated point. On rt>=1 the expression is 2+2ln t-(1+r)t, decreasing on t>=1/r because 2r<1+r. Its boundary value equals the preceding expression at t=1/r. For r>1, the region rt<=1 is maximized at its boundary (or can be bounded by g(r)); on rt>=1 the unconstrained maximum is 2ln(2/(1+r))<0, attained at t=2/(1+r). For r=1 both maxima are zero. In particular for r>1 the global maximum is 2ln(2/(1+r)), since on rt<=1 the derivative 3/t-(1+2r) is positive when t<=1/r.

The algebraic identity

    (1+2r)^3-27r=(r-1)(8r^2+20r-1)

implies g(r)>0 iff rho_*<r<1 for 0<r<1, with equality at rho_* and 1. Moreover g'(r)=(1-4r)/(r(1+2r)), so g is increasing for r<1/4. For rho<rho_*, d>=1 implies r<=rho and H<=g(rho)<0. For d<=-1, r>=1/rho>1 gives H<=2ln(2/(1+1/rho))<0. All nonzero differences are therefore uniformly exponentially suppressed in L. For rho=rho_*, the same suppression holds for d>=2 and d<=-1; for d=1 the maximum is exactly zero and is treated in Section 4. There are only O((ln L)^2) pairs in (1), so all uniformly negative cases contribute o(1).

## 3. Equal-size contribution, all fixed biases

If z=a, formula (2) equals (1+o(1))*pi_lambda(a)^2, with lambda=m rho^a and pi_lambda(a)=exp(-lambda)lambda^a/a!. Dropping all conditions on K0 can only increase this bound. The normalized mean lambda/a decreases by a factor strictly less than rho with each increment in a. Thus only O_rho(1) integers have lambda/a in [1/2,2]; their squared Poisson masses are O(1/L) by Stirling. Outside that interval each squared mass is exp(-Omega(L)), since a>=L/2 and the rate x-1-ln x is bounded below by a positive constant. Sum over O(log L) choices of a. This proves that the total diagonal contribution is O(1/L).

Combining Sections 1-3 proves p_m(F)->0 for every rho<rho_*.

## 4. Critical boundary rho=rho_*

It remains to handle d=1, z=a+1. Let t_*=3/(1+2rho_*) and s_*=rho_* t_*=0.1339745962...<1. Section 2 shows that H(t,rho_*t) is uniquely maximized at t_* with value 0; it tends to minus infinity at both endpoints t->0 and t->infinity. Thus outside a fixed closed interval [t_*-eta,t_*+eta] chosen inside (0,1/rho_*), H is bounded above by a strictly negative constant. Those pairs contribute o(1) by the uniform estimate. Choose eta small enough that the normalized means below stay away from 0 and 1.

Inside this interval put v=lambda_a/a and w=lambda_z/a=rho_*v. Since a/L->1 uniformly, v is bounded above and below by positive constants and w lies in a compact subinterval of (0,1). Crucially, now keep the M-hit probability, even for k below a. Let p_j=P(K0=j) for K0~Bin(n,rho^z), with n=m-a-z. Uniformly in this interval, p_a=(1+o(1))*pi_lambda_z(a), by the falling factorial estimate n^a/m^a=1+o(1) and binomial-to-Poisson approximation at size a=O(L).

For j>=a, successive ratios p_(j+1)/p_j=((n-j)/(j+1))*rho^z/(1-rho^z) are bounded by a fixed q<1 for large m, because lambda_z/a=w is bounded strictly below 1. Hence sum_(j>=a) p_j <=p_a/(1-q). For j=a-l<a with l>=1, each backward ratio p_(j-1)/p_j=j(1-rho^z)/((n-j+1)rho^z) for j<=a is bounded by a fixed Q, since lambda_z/a is bounded away from zero. Thus p_(a-l)<=p_a Q^l. Also

    (1-rho^(a-l))^(m-z)
       <= exp(-(m-z)rho^a B^l)
       <= exp(-c a B^l)

for some fixed c>0, because lambda_a/a=v is bounded below and z=O(L). The sum over l>=1 of Q^l exp(-c a B^l) tends to zero: B>1, B^l>=1+(B-1)l, giving an exponentially small geometric bound. Therefore even after dropping the restriction K0>=b0 the entire third-line expectation of Section 2 is O(pi_lambda_z(a)), uniformly.

Multiply by (2) and use z=a+1. The resulting count is at most a constant times

    (lambda_a/(a+1)) * (lambda_a^a/a!)^2
        * (lambda_z^a/a!) exp(-lambda_a-2lambda_z)
    <= C a^(-3/2)
         * exp(a[3+2ln v+ln w-v-2w]).

The inequality is Stirling with uniform constants on the compact normalized means. Since w=rho_*v, the exponent in square brackets is <=g(rho_*)=0 for every v>0. Thus each critical size pair contributes O(L^(-3/2)), with at most O(log L) pairs, yielding o(1). Together with Sections 1-3 this proves p_m(F)->0 at the boundary. Merely observing a zero leading exponent would not have sufficed.

## 5. Positive subsequences for every rho>rho_*

Choose t=3/(1+2rho), s=rho*t and let integer j tend to infinity along

    m_j=round(t*j*B^j),   a=j,   z=j+1,
    k=ceil(L+2 log_B L),  c=m-a-z-k.

Then L=j+log_B j+O(1), t_m=m rho^a/L->t, s_m=m rho^z/L->s. All a,z,k=L+O(log L), rho^a,rho^z=Theta(L/m), and m rho^k<=L^(-2). Let Y0 count exact-M necessary triples with these sizes and Y count the sufficient ones (C-hit condition added).

The exact forced-pair formula gives

    E[Y0]=(1+o(1))*(lambda_a^a/a!)*(lambda_a^z/z!)
              *exp(-lambda_a-lambda_z)*pi_lambda_z(k),

uniformly along the chosen subsequence. Here the M-hit factor tends to one because m rho^k<=L^(-2). The binomial approximation is relative 1+o(1) since all sizes are O(L) and probabilities O(L/m); the C-hit factors tend to one by the exact formula and 1-z rho^c<=J(z,c)<=1. Thus E[Y]/E[Y0]->1. Stirling gives

    ln E[Y0]/L -> 3+2ln t+ln s-t-2s = g(rho)>0.

To conclude existence we must use a second moment, not just growing expectation. The argument of LAST_FOUR_POINT_SECOND_MOMENT.md in fact works verbatim with fixed rho in (0,1) and B=1/rho under the size and first-moment hypotheses just established. For self-contained clarity the estimates are summarized and justified here.

For fixed triple T=(A,Z,M0), its event E_T consists of the forbidden rectangles A x A, Z x A, Z x M0, row hits to A from outside A union Z, all row hits to Z, non-Z row hits to M0, and Z-to-C column hits. All coordinate blocks in this event are disjoint. A uniquely determines Z and M0. Let S=A union Z union M0, nS=a+z+k=O(L), and let h'=|S intersect S'| and I be the count of common forbidden ordered coordinates for two triples. The individual probability P equals rho^(a^2+az+zk) R with R=exp(-O(L)).

For h'<=L/2, keep all forbidden coordinates and only hits for rows and columns outside S union S'. These families are disjoint. Put ell=min(a,z,k)=L-O(log L). Two simultaneous misses for a given outside row have probability at most rho^(2ell-h'), even when their target sets overlap; the two-term Bonferroni inequality bounds the joint hit probability divided by the product of marginal hit probabilities by 1+O(rho^(2ell-h')). The analogous bound holds for the two column-hit conditions. Across O(m) outside rows/columns the ratio is 1+o(1), since m rho^(2ell-h')<=m^(-1/2) poly(L). Removing O(L) original hit conditions costs a factor 1+o(1). Consequently joint/marginal squared probability <=(1+o(1))*B^I. Also I<=h'^2, and the support-overlap probability for two uniformly independent triples is <=(nS^2/(m-nS))^h'. Summing over 1<=h'<=L/2 gives o(1) in normalized second moment by the geometric base nS^2 B^(L/2)/(m-nS)->0. The h'=0 contribution is <=1+o(1).

For h'>L/2, put D=max(a,z,k)=L+O(log L) and Delta=D h'-I. Dropping all hits gives ratio <=B^(I+O(L)); support-overlap counting gives B^(-L h'+O(h' log L)). Hence the pairs with Delta>=K1 L log_B L have normalized contribution o(1) for sufficiently large fixed K1. For the remaining large-overlap pairs set x=|A intersect S'|, y=|Z intersect S'|, w0=|M0 intersect S'|. The forbidden rectangles imply

    Delta>=x(D-x)+y(D-x)+w0(D-y).

If x<=D/2 then x+y=O(log L), subsequently w0=O(log L), contradicting h'>L/2. Thus x>=D-O(log L). With u=|A intersect A'|, v0=|A intersect Z'| and r0=|A intersect M0'|, the missing common forbidden coordinates include disjoint squares of sizes v0^2,r0^2 and the rectangle of size u(v0+r0). Thus v0+r0=O(sqrt(L log L)), u>=L/2, and then v0+r0=O(log L). It follows that dA=|A minus A'|=O(log L).

Conditional on E_T, the disjoint blocks remain independent. A hit-conditioned block has probability <=rho^b of absence of any specified b coordinates, by the exact conditional factor (1-rho^(blocksize-b))/(1-rho^blocksize)<=1. For another independent A' at distance dA, let e=|(A' minus A) intersect Z|. Absence of both cross directions between A intersect A' and A' minus A has conditional probability <=rho^((a-dA)(2dA-e)): the direction out of A is fresh or hit-conditioned, and the reverse direction is hit-conditioned for all added vertices outside Z, while those inside Z already miss A. These coordinates do not intersect the Z-to-C column conditions. Summing choices at fixed dA>=1 is bounded by

    [a rho^(a-dA) (z+m rho^(a-dA))]^dA.

For dA=O(log L) the base is poly(L)/m, so the conditional expectation of all other such independent A' is o(1). Since A uniquely determines its triple, the remaining pairs, including identical A, contribute at most (1+o(1))*E[Y0], negligible compared with its square. The normalized second moment is therefore 1+o(1). Chebyshev gives Y0>=E[Y0]/2 a.a.s., and Markov gives Y0-Y<E[Y0]/2 a.a.s. because E[Y]/E[Y0]->1. Hence Y>0 a.a.s. and p_(m_j)(F)->1, as asserted.

## 6. Consequence: complete biased finite-model census up to four points

The criterion H models ML^as_theta iff limsup p_m(H)>0 for finite central targets was explained in HIGH_BIAS_FOUR_POINT_OSCILLATION.md (direct adaptation of Goranko's known characterization). Combining the present theorem with earlier fixed-bias results:

- For every fixed 0<theta<theta_*, the four-point central finite models of ML^as_theta are exactly the 12 fair-model positive types.
- For every fixed theta_*<=theta<1, they are exactly the 11 types obtained by deleting 011010111 from those 12.
- The other 92 central types vanish at all fixed biases; hence the counts of excluded four-point central types are 92 and 93, respectively.
- The 1-, 2-, and 3-point central finite-model counts remain 1, 1, 3 for all fixed biases.
- The finite quotient census shows that 011010111 has no smaller vanishing central quotient (equivalently no quotient onto one of 0, 0001, 1001). Consequently it becomes a 23rd minimal vanishing four-point type at theta>=theta_*; the existing 22 stay minimal since the smaller classification does not change. The independent characteristic-formula family on at most four points then has 26 types rather than 25. These statements concern minimal vanishing targets, not arbitrary axiom bases.

In particular the finite-model theory at this size is NOT independent of the edge bias. Since chi_F^d is invalid in F, it is almost surely valid precisely for theta>=theta_* and not for theta<theta_*. The latter assertion uses a positive limsup, not a full probability limit. This also witnesses that ML^as_theta differs from the fair logic at theta>=theta_*. Nothing here claims equality of the full logics within either interval, or a full existence-limit census for all biases. The previous fair-model paper is unchanged.

Literature context: Goranko, AiML 2020, https://www.aiml.net/volumes/volume13/Goranko.pdf, and Le Bars's random directed kernel estimates (including nonconvergent variants) are relevant. Targeted searches did not establish priority of this exact threshold; no first-discovery claim. Independent review and Lean verification pending.
