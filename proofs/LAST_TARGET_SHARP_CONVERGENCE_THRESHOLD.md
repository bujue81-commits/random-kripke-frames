# Sharp convergence threshold for F011010111

Status: internal hand proof, not independently reviewed or Lean-verified. Uses the exact fixed-phase theorem in LAST_FOUR_POINT_PHASE_CLASSIFICATION.md and the sharp positive-limsup threshold in LAST_FOUR_POINT_BIAS_THRESHOLD.md. No priority claim. Fair manuscript unchanged.

## Theorem

Put rho=1-theta, B=1/rho, rho_*=(3sqrt(3)-5)/4. Define

    u(r)=2 ln(1/r)/(1-r),
    D(r)=3+3 ln u(r)+2 ln r-(1+2r^2)u(r).

There is a unique root r_c of D in [1/4,1/3], lying strictly between 251/1000 and 252/1000. Numerically r_c=0.25149763525561764... . Then for the last target F011010111,

    rho>r_c: p_m->1;
    rho_*<rho<=r_c: liminf p_m=0, limsup p_m=1;
    0<rho<=rho_*: p_m->0.

In theta notation the convergence threshold theta_c=1-r_c≈0.7485023647443824 belongs to the oscillatory interval, while theta_*=1-rho_*≈0.950961894323342 belongs to the vanishing interval. This completes the full-sequence classification for this target at all fixed biases.

## 1. Separation of the lattice optimization

The earlier phase function is P_r(v)=max_(i,l integers) H(v r^i,v r^l), where

    H(t,s)=f(t)+J(s),
    f(t)=2+2 ln t-t,
    J(s)=1+ln s-2s if s<=1, -s if s>=1.

Because the integer indices are independent, the maximum is the sum of separate lattice maxima. The continuous function f increases up to 2 and decreases after 2; J increases up to 1/2 and decreases thereafter. The first adjacent comparison is exact:

    f(t)-f(rt)=2 ln(1/r)-(1-r)t=(1-r)(u-t).

Consequently f(t) maximizes f over its lattice whenever r u<=t<=u: comparison with smaller neighbors follows from the positive difference for t<=u, and comparison with larger neighbors from the negative difference for t/r>=u. Repeating the comparisons proves the claim for all integer shifts. Each phase has a representative in [ru,u] because the ratio of the endpoints is B.

The earlier theorem proved p_m->1 for r>=1/3, oscillation for rho_*<r<=1/5, and vanishing for r<=rho_*. It remains to decide [1/5,1/3]. All subsequent symbols r denote rho.

For useful monotonic bounds, u=2 integral_0^1 [r+(1-r)x]^(-1) dx is strictly decreasing in r; ru and r^2u are strictly increasing, by differentiation of each integrand after multiplication by r or r^2 (strict on a positive-measure set). Also u>2, since the integrand is >1 for x<1. Values at endpoints used below follow directly from these formulas.

## 2. No coverage for 1/5<=r<=1/4

Take the phase represented by t=u, or equivalently t0=ru. These have equal f by the adjacent comparison and are f-maximizers. On this range t0 lies between (ln 5)/2 and (2 ln 4)/3, hence 1/2<t0<1. Since J decreases above 1/2, all larger lattice points have worse J. The next smaller lattice point r t0<1/2, and all further smaller ones have worse J than that point. The remaining comparison is

    J(t0)-J(r t0)=ln(1/r)-2(1-r)t0
                =(1-4r)ln(1/r)>=0.

Thus t0 is also a J-maximizer. At this phase

    P_r(u)=H(t0,t0)=3+3 ln t0-3t0<0,

by ln x<x-1 for x!=1. This exact phase therefore supplies a zero subsequence. The earlier positive-limsup theorem supplies a positive subsequence. Hence the entire stated range oscillates, including r=1/4.

## 3. Exactly two switching points for 1/4<=r<=1/3

Set b=u/4. Here 1/2<b<1, ru>=b, r^2u<1/2, and r^2u<=b. For the last bound use r^2<=1/9<1/4. For the stronger r^2u<1/2 use u<=u(1/4)=8 ln 4/3 and hence r^2u<=8 ln 4/27<1/2. Also ru>1/2. These estimates follow by the monotonicity above and elementary endpoint values.

On this range the adjacent J-difference J(s)-J(rs) is strictly decreasing in s. For s<=1 it equals ln B-2(1-r)s; for 1<=s<=1/r its derivative is -1-1/s+2r<0; for s>=1/r it equals -(1-r)s. The pieces match. Its unique zero is b=u/4<1. Therefore a lattice J-maximizer is any s in [r b,b], by the same adjacent-comparison argument as for f.

Choose t in [ru,u] to maximize f. Since t>=ru>=b, the J-maximizer can be chosen to be rt when t<=b/r and r^2t when t>=b/r. Indeed rt ranges between r^2u>=rb (because ru>=b) and b on the first interval. On the second interval r^2t ranges between rb and r^2u<=b. The switch b/r lies in [ru,u] because r^2<=1/4<=r. Thus

    P_r(t)=H(t,rt)      for ru<=t<=b/r,
           H(t,r^2t)   for b/r<=t<=u.

The two functions agree at the switch. On each interval they are strictly concave as functions of t (negative second derivatives in H; or f and J are concave). Thus the minimum over the full period is achieved at one of its endpoints or the switch. The two outer endpoints have equal phase value by periodicity. Hence

    min_v P_r(v)=min(D(r),E(r)),
    D(r)=H(u,r^2u)=f(u)+J(r^2u),
    E(r)=H(b/r,b)=f(b/r)+J(b).

The displayed formula for D follows by substitution since r^2u<1.

Both functions are strictly increasing on [1/4,1/3]. For D, u decreases while u>2, so f(u) increases. Also r^2u increases and stays below 1/2, so J(r^2u) increases. For E, b/r=u/(4r) strictly decreases while remaining >2 (at r=1/3 it equals (9/4)ln 3>2). Consequently f(b/r) increases. And b decreases while remaining >1/2, so J(b) increases. These arguments need no derivative of the phase maximizer.

## 4. Signs and the unique transition

The following strict numerical inequalities can be certified by rational arithmetic with the elementary logarithm series

    ln x = 2 sum_(k=0)^(N-1) y^(2k+1)/(2k+1) + remainder,
    y=(x-1)/(x+1),
    |remainder| <= 2|y|^(2N+1)/((2N+1)(1-y^2)).

For clarity, using N=60 and outward fixed-point rounding at scale 10^18 gives the following conservative rational enclosures (the independent actual integer-arithmetic evaluation obtained narrower intervals):

    -0.003005 < D(251/1000) < -0.003004
     0.003020 < D(252/1000) <  0.003022
     0.001577 < E(251/1000) <  0.001578.

These can be reproduced by taking lower and upper logarithm bounds at the rational endpoints after each arithmetic operation, since ln is increasing. In particular D has exactly one root r_c in (0.251,0.252) by continuity and strict monotonicity. For r<=r_c in [1/4,1/3], D<=0, so the phase u is nonpositive. For r>r_c both D>0 and E>0 (E is increasing and already positive at 0.251). Thus the phase circle is covered precisely when r>r_c. At equality the phase u has P_r(u)=0 (E>0); the exact fixed-phase upper bound of the earlier phase theorem gives a zero subsequence, not an inconclusive leading exponent.

Apply the full-sequence criterion and combine with Section 2 and the earlier outer ranges to prove the theorem.

The approximations r_c≈0.25149763525561764, theta_c≈0.7485023647443824 are from floating-point bisection and are not used in the proof. The sign bracket above is certified by a separate integer-arithmetic computation; the exact root definition is the mathematical statement. Transition windows for sequences with bias changing with m, and arbitrary shrinking approaches to a critical lattice phase, are not claimed. Independent review, Lean verification, and literature priority remain pending.
