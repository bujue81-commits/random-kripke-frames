# Fixed lattice phases for the last four-point target

Status: internal hand proof, not externally reviewed or Lean-verified. This strengthens LAST_FOUR_POINT_BIAS_THRESHOLD.md for F=011010111, with C universal and missing arrows A->A, Z->A, Z->M. Preserve the fair manuscript. Fix rho in (0,1), theta=1-rho, B=1/rho and L=log_B m.

## 1. Statement

Define

    H(t,s)=2+2 ln t-t-s                  for s>=1,
          =3+2 ln t+ln s-t-2s           for s<=1,

and for v>0,

    P_rho(v)=max_{i,l in Z} H(v rho^i,v rho^l).

The maximum is attained: every nonempty superlevel set of H is contained in a compact subset of the positive quadrant (proof below). This phase function is invariant under v -> v B. It is continuous, since locally only finitely many indices can attain the maximum.

For each fixed v>0, on the integer subsequence m_j=round(v j B^j), j->infinity,

    p_(m_j)(F) -> 1  if P_rho(v)>0,
    p_(m_j)(F) -> 0  if P_rho(v)<=0.

The equality case is included, but only for the stated fixed-v subsequences. For arbitrary sequences of m with normalized lattice phase converging to a strictly positive P_rho(v), the probability tends to 1. A corresponding strict negative phase gives probability tending to 0. No claim about arbitrary approach rates to a zero phase is needed for the following exact full-sequence criterion:

- rho<=rho_*=(3sqrt(3)-5)/4: p_m->0 by the earlier threshold theorem.
- rho>rho_* and P_rho(v)>0 for all v in [1,B]: p_m->1.
- rho>rho_* and P_rho(v)<=0 for some v in [1,B]: liminf p_m=0 and limsup p_m=1.

Thus there is a finite, one-dimensional interval-coverage test at every fixed bias. This is an implicit criterion, not a proved closed-form critical rho for full-sequence convergence.

## 2. Upper bound outside finitely many lattice offsets

The size reduction in LAST_FOUR_POINT_BIAS_THRESHOLD.md, Section 1, gives, except with probability o(1), a,z between L-3log_B L and L+1000log_B L, and |M0|>=L-3log_B L, where A is independent, Z is the set of outside-A rows missing A, and M0 is the common nonneighbor set of Z outside A union Z. The actual M-fibre is contained in M0. All rows must hit Z and all non-Z rows must hit M0. The expected necessary count at a,z, with that size restriction on M0, is bounded by

    exp(L H(t_m,s_m)+O((ln L)^2)),
    t_m=m rho^a/L, s_m=m rho^z/L,

uniformly. This is the previous first-moment bound including the binomial upper tail for M0.

To justify compactness, write H(t,s)=2+2ln t-t+J(s), where J(s)=-s for s>=1 and J(s)=1+ln s-2s for s<=1. J is continuous, has maximum -ln 2, and tends to minus infinity at 0 and infinity. The function 2+2ln t-t also tends to minus infinity at both ends and has finite maximum. Hence H tends uniformly below any fixed bound when either coordinate leaves a sufficiently large compact subinterval of (0,infinity).

For fixed v and m_j=round(v j B^j), L=j+log_B j+O(1). Write a=j+i, z=j+l. Then t_m=(v+o(1))rho^i, s_m=(v+o(1))rho^l, with the same relative error for all offsets. For sufficiently large fixed N, whenever |i|>N or |l|>N, at least one of the coordinates is outside the compact interval required for H>=-1. Such sizes contribute at most O((ln L)^2)exp(-L+O((ln L)^2))=o(1). The same compactness argument works for normalized phases in any compact positive interval. In particular the maximum defining P is attained and is a finite maximum locally (use the value at i=l=0 as a continuous lower bound). Its continuity follows.

## 3. Fixed-phase zero result, including critical phases

For the finitely many remaining fixed offsets i,l set t=v rho^i, s=v rho^l. The Poisson means satisfy

    lambda_a=m_j rho^(j+i)=t j+o(1),
    lambda_z=m_j rho^(j+l)=s j+o(1).

The errors are exponentially small, since rounding changes m by at most 1. With n=m-a-z, the exact necessary expectation at sizes a,z is at most

    (lambda_a^a/a!)(lambda_a^z/z!) exp(-lambda_a-lambda_z+o(1))
       * E[(1-rho^K0)^(m-z)],

where K0~Bin(n,rho^z). This upper bound drops the earlier size restriction on K0. Stirling with fixed offsets gives

    (lambda_a^a/a!)(lambda_a^z/z!) exp(-lambda_a-lambda_z+o(1))
       = O(j^-1) exp(j(2+2ln t-t-s)).

For example lambda_a^(j+i)/(j+i)! is asymptotic to t^i (2 pi j)^(-1/2) exp(j(1+ln t)); the same formula holds for l. If s>=1, bound the expectation by one, obtaining O(j^-1) exp(j H(t,s)). This tends to zero even at H=0.

If s<1, let b_u=P(K0=u). The mass at j is asymptotic to pi_lambda_z(j) by the relative binomial approximation (j,z=O(L), rho^z=O(L/m)). The forward ratios b_(u+1)/b_u for u>=j are bounded by a fixed q<1, since lambda_z/j->s<1. The backward ratios b_(u-1)/b_u for u<=j are bounded by a fixed Q, since s>0. Thus the upper tail is <=b_j/(1-q), and the lower tail at u=j-d, d>=1, has

    b_(j-d)(1-rho^(j-d))^(m-z) <= b_j Q^d exp(-c j B^d)

for fixed c>0, because (m-z)rho^j~v j. The sum over d>=1 tends to zero after division by b_j: B^d>=1+(B-1)d yields a geometric upper bound with ratio Q exp(-c j(B-1)). Therefore

    E[(1-rho^K0)^(m-z)] = O(pi_lambda_z(j))
       = O(j^-1/2) exp(j(1+ln s-s)).

Consequently the count at the fixed pair is O(j^-3/2) exp(j H(t,s)), again tending to zero if H<=0. If P_rho(v)<=0 every one of the finitely many pairs vanishes; Section 2 and Markov prove p_(m_j)->0. Notice that the polynomial prefactors have been computed relative to j, not L: this avoids an unjustified substitution at the exact phase boundary, where O(log L) errors can matter.

For a varying phase with strictly negative P_rho(v), continuity and the uniform bound of Section 2 give a negative margin for every pair, so p_m->0 without any fixed-phase rate assumption.

## 4. Positive phases: s<=1

Suppose H(t,s)>0 for a fixed integer offset pair. Set a=j+i,z=j+l, k=ceil(L+2log_B L). Then a,z,k=L+O(log L), m rho^a/L->t and m rho^z/L->s, and m rho^k<=L^-2. The exact fixed-size necessary expectation is

    (1+o(1)) (lambda_a^a/a!)(lambda_a^z/z!)
       exp(-lambda_a-lambda_z) pi_lambda_z(k).

Its logarithm divided by L tends to 3+2ln t+ln s-t-2s=H(t,s)>0, including s=1. The sufficient expectation has ratio 1+o(1) to this expectation. The full triple second moment in LAST_FOUR_POINT_BIAS_THRESHOLD.md, Section 5, uses only these logarithmic sizes, rho^a,rho^z=Theta(L/m), m rho^k<=L^-2 and exponential mean growth; it does not require the specific choices z=a+1 or the maximizing t. Therefore p_m->1 for these sizes. This argument also works along any sequence with these normalized means converging to t,s and positive limiting H.

## 5. Positive phases: s>1, pair second moment

For s>1 the typical M0 is larger than L, and unnecessarily forcing it to size L can lose the positive exponent. Instead count pairs T=(A,Z) of disjoint sets with the prescribed a,z satisfying:

- A x A and Z x A entirely absent;
- every row outside A union Z hits A;
- every row hits Z.

Call the event E_T and the count X. It uses only columns ending in A union Z, and its disjoint absence and row-hit blocks have product probability

    P=rho^(a^2+az)(1-rho^a)^(m-a-z)(1-rho^z)^m.

Its exact mean is binom(m,a)binom(m-a,z)P, so

    ln E[X]/L -> 2+2 ln t-t-s=H(t,s)>0.

A uniquely determines Z in a successful pair. We show relative variance tending to zero. For two pairs let S=A union Z, S'=A' union Z', h=|S intersect S'|, I=count of common forbidden ordered coordinates, D=max(a,z)=L+O(log L).

For h<=L/2, retain forbidden bits and only row-hit requirements outside S union S'. For each outside row four hits are required, and the joint probability divided by the product of the four marginal hit probabilities is <=1+O(rho^(2 ell-h)), ell=min(a,z). This follows from two-term Bonferroni for misses, whose pairwise probabilities are bounded by rho^(2 ell-h). Row blocks are disjoint and disjoint from forbidden bits. Removing O(L) marginal hit conditions costs 1+o(1), since miss probabilities are O(L/m). Hence joint/marginal ratio <=(1+o(1))B^I, uniformly, since m rho^(2ell-h)=o(1). For positive h<=L/2 use I<=h^2 and support-overlap probability <=((a+z)^2/(m-a-z))^h; the geometric bound gives total normalized contribution o(1), and h=0 at most 1+o(1).

For h>L/2 use crude ratio B^(I+O(L)), since individual hit factors are exp(-O(L)). Support-overlap probability is B^(-Lh+O(h log L)). Hence pairs with deficit Delta=Dh-I>=K L log_B L are negligible for sufficiently large fixed K. Put x=|A intersect S'|, y=|Z intersect S'|. Restriction of first forbidden set to common support has size x^2+yx, giving

    Delta >= (x+y)(D-x).

For remaining pairs, h>L/2 implies x>=D-O(log L). Put u=|A intersect A'|, w=|A intersect Z'|. Forbidden coordinates lost by the second pair include w^2 from its reflexive Z' and uw from A' to Z'. They are disjoint, and their sum is <=Delta. Thus w=O(sqrt(L log L)), then u>=L/2, and then w=O(log L). In particular d=|A minus A'|=O(log L).

Conditional on E_T, absence requirements and nonempty row-hit blocks remain independent. For independent A' at distance d>=1, with e=|(A' minus A) intersect Z|, the cross coordinates from A intersect A' into added vertices are fresh or hit-conditioned, and the reverse cross coordinates from added vertices outside Z are hit-conditioned into A; the other reverse coordinates are already absent. As in the triple proof the conditional probability of independence is at most rho^((a-d)(2d-e)). Summing over d=O(log L) bounds the conditional expected number of other such independent A' by the geometric sum with base

    a rho^(a-d)(z+m rho^(a-d))=poly(L)/m.

This tends to zero uniformly. A'=A allows only the original Z, so all remaining pairs contribute <=(1+o(1)) E[X], negligible against E[X]^2. Hence E[X^2]/E[X]^2->1.

Now complete a fixed successful pair. Conditional on E_T the untested columns outside A union Z are fresh. The common nonneighbor set M0 of Z among those columns has binomial size with mean (m-a-z)rho^z~sL. For any fixed 1<s0<s, Chernoff gives |M0|>=s0 L and |M0|=O(L) except with probability o(1). Conditional on the Z-row column tests determining M0, edges from non-Z rows to M0 and C0 are fresh. The chance some non-Z row misses M0 is at most m rho^(s0 L)=m^(1-s0)->0, and all non-Z rows hit C0, of size m-O(L), except with probability o(1). The conditional Z-to-C0 law consists of independent nonempty column blocks, so the probability some Z row misses C0 is at most z rho^|C0|=o(1). Thus a fixed successful pair completes with conditional probability 1-o(1), uniformly. Count the failed pairs: their mean is o(E[X]); Markov plus the second-moment concentration yields a successful completion a.a.s. This avoids conditioning fresh bits on the outcome of selecting an arbitrary successful pair.

Combining Sections 4 and 5 proves the positive phase assertion, even for varying sequences with the stated limiting normalized means.

## 6. Full-sequence convergence and interval coverage

For arbitrary m use j=floor(L-log_B L), v_m=m rho^j/L in [1,B). If P_rho(v)>0 for every v in [1,B], any subsequence of m has a further subsequence on which v_m->v in that interval. Fix a positive pair of offsets for v and use Sections 4 or 5 with a=j+i,z=j+l. Their size and mean assumptions hold. Thus p_m->1 on the further subsequence. The subsequence criterion for convergence gives p_m->1 on the whole sequence. Conversely a phase v with P_rho(v)<=0 supplies the exact zero subsequence by Section 3. If rho>rho_* the earlier threshold theorem guarantees a positive subsequence. This proves the full-sequence criterion in Section 1.

For explicit evaluation only d=l-i>0 with r=rho^d>rho_* can give positive H. Indeed the maximization in the threshold theorem yields a nonpositive maximum for d<=0 or rho^d<=rho_*. For each remaining d, the function H(t,rt) is strictly concave on t>0: the two pieces have negative second derivatives and matching first derivatives at rt=1. It has a unique positive maximum and tends to minus infinity at both ends, hence a unique open positivity interval (alpha_d,beta_d), whose endpoints are the two roots H(t,rt)=0. Define the logarithmic intervals

    I_d=(log_B alpha_d, log_B beta_d) modulo 1.

Then P_rho(v)>0 exactly when log_B v modulo 1 lies in the union of these finitely many open intervals on the phase circle. Coverage of the entire circle is equivalent to p_m->1 in the rho>rho_* regime. A missing point implies oscillation. This includes exact endpoint gaps, because Section 3 supplies fixed-phase zero even at equality.

## 7. Explicit consequences without numerical root assumptions

At rho=1/10 (theta=0.9) only d=1 can yield a positive value since rho^2=0.01<rho_*. Its positivity interval lies strictly inside (1,B)=(1,10): H(1,rho)=2-2rho+ln rho<0 and H(B,1)=1+2ln B-B<0; the unique maximum occurs between 1 and B. In particular v=1 has no positive lattice pair. The zero phase m_j=round(j*10^j) contrasts with the positive phase m_j=round(2.5*j*10^j), since 3/(1+2rho)=2.5 and g(rho)>0. Thus the last target oscillates at theta=0.9, although its finite-model membership is positive there. More generally for rho_*<rho<=1/5, only d=1 can be positive (rho^2<=0.04<rho_*); H(1,rho)<0 since 2-2rho+ln rho increases on this range and at 1/5 equals 1.6-ln 5<0. H(B,1)<0 for B>=5 by its decreasing derivative and value 2ln 5-4<0. The maximizer lies between 1 and B; hence v=1 is a zero phase throughout this interval. Thus liminf=0,limsup=1 for 4/5<=theta<theta_*.

For rho>=1/3 (theta<=2/3), d=1 alone covers the phase circle. Indeed H(1,rho)=2-2rho+ln rho>0 for 1/3<=rho<1 by concavity and its endpoint values (at 1/3, 4/3-ln 3>0, at 1, zero). Also H(B,1)=1+2ln B-B>0 for 1<B<=3 by concavity and endpoint values (at 1, zero, at 3, 2ln 3-2>0). Strict concavity implies H(t,rho*t)>0 throughout [1,B]. Hence p_m->1 for every 0<theta<=2/3. These explicit ranges are not asserted sharp; the interval criterion above is exact. The fair-model theorem is consistent with this result.

The phase-circle test does not classify arbitrary transition sequences approaching a zero endpoint at shrinking distance. Such scaling windows, a closed-form or rigorous interval-based analysis of the exact full-sequence transition in rho, and the corresponding phase classification for F011011101 remain natural subsequent questions. The previous finite-model threshold and counts are unchanged. No novelty or machine-verification claim.
