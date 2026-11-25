# Central directed cycles: complete quotient classification and minimality

Internal hand proof. Uses the preceding loopless probability theorem; not Lean-verified or externally reviewed. Literature priority unverified.

For r>=2 let C_r consist of a universal reflexive central vertex c and r peripheral vertices i in Z/rZ, each with exactly two successors c and i+1. Let T_2 be the complete reflexive two-point frame, E_1 the reflexive singleton, and K_2 the central two-point frame with absent peripheral loop. Treat C_1 as T_2 (a peripheral cycle of length one). All targets and edge probabilities are fixed as source size m tends to infinity.

## Quotient theorem

The surjective bounded-morphic images of C_r, up to isomorphism, are exactly E_1, C_d for positive divisors d of r, and K_2 if r is even.

Proof. Given a surjective bounded morphism f, write z=f(c). It is central, since c has all incoming and outgoing arrows. For each peripheral i, the set of successors of f(i) is exactly {z,f(i+1)}, by forth and back. If f(i)=z for some i, the target has at most two vertices, since the successor set of z is the whole target. In the singleton case the target is E_1. In the two-point case write w for the other point. The central row is universal, so only the loop of w is optional. If w has a loop, all source peripheral rows must hit w, implying f(i+1)=w for every i. Thus every peripheral maps to w and none maps to z, contradicting this case. If w has no loop, then every peripheral i must satisfy f(i+1)=w exactly when f(i)=z, and f(i+1)=z exactly when f(i)=w. This is an alternating colouring, possible precisely when r is even. Conversely the alternating colouring and f(c)=z give a bounded morphism onto K_2 for even r, as the successor sets directly verify.

Now suppose no peripheral maps to z. Every other target vertex u has successor set {z,s(u)} for a uniquely determined noncentral vertex s(u), because it is f(i) for some i, and f(i+1) is noncentral. The map s is well-defined by successor-image equality, and f(i+1)=s(f(i)). Its orbit from f(0) covers every noncentral target vertex by surjectivity, and s^r(f(0))=f(0). Hence this orbit is a cycle of length d dividing r, and the target is C_d. Conversely reduction of peripheral indices modulo any divisor d gives a surjective bounded morphism C_r->C_d, sending center to center. The map to E_1 exists by seriality. This proves the theorem.

## Probability and minimality

For r>=2 all peripheral loops are absent and the number of peripheral arrows is r. Apply LOOPLESS_CENTRAL_BIASED_RATE.md, with theta in (0,1), B=1/(1-theta), L=log_B m, b=L-log_B L and coefficient d_r=r(r-2). For r>=3,

    log_B P(G_m ->> C_r) = -r(r-2)*b^2+O_{r,theta}(L).

For r=2 the critical estimate gives O(L^(-1)). Thus all C_r, r>=2, have vanishing image probability. E_1 and T_2 have image probability tending to one by deterministic partitions; K_2 has vanishing image probability.

Consequently C_r is minimal among all vanishing-probability central targets exactly when r is an odd prime: an even r maps to K_2; an odd composite r maps to a smaller C_d with d>=3; an odd prime has only E_1,T_2 as proper quotients. This checks all proper quotient sizes, not only those <=3. Since every image of a central frame is central, there are no other proper images to consider.

For C_3 (four points), the exact leading and second logarithmic coefficients in the fair model are -3 and +6, respectively. Its peripheral matrix, row-major canonical under permutation, is 001100010.

## Logic and independence

Use the ordinary characteristic formulas chi_F^d on R^2-universal frames, as in THREE_POINT_LOGICAL_COROLLARIES.md. All C_r are central and validate ML^r. For odd primes p, chi_{C_p}^d is almost surely valid; each C_p falsifies its own characteristic formula, but validates those of every other odd-prime cycle (different primes do not divide one another). It also validates chi_{K_2}^d, chi_{F0001}^d, chi_{F1001}^d, since its only proper images E_1,T_2 are different from all these frames. Hence the infinite family is independent over ML^r plus these three axioms, via finite countermodels. In fact each prime-cycle formula is independent from the entire set of almost-sure characteristic formulas of nonisomorphic central targets: if its countermodel mapped onto such a target, that would contradict minimality or equal-size bijective isomorphism.

This is a new family within the repository, distinct from the central directed paths in Goranko, AiML 2020, Proposition 4.7 (https://www.aiml.net/volumes/volume13/Goranko.pdf, pp. 264-265). That proposition already gives an infinite independent family of characteristic formulas, so infinitude or independence per se is not a novelty claim. Initial targeted search found no explicit prime-cycle result; this is not a complete literature survey. The primary-source PDF text was accessible; page-image fetch timed out. The result does NOT prove non-finite axiomatizability by arbitrary modal axioms, nor completeness of the characteristic-formula axiomatization (Goranko's Conjectures 4.5 and 4.8).

## Verification

Exhaustive quotient tests for cycles of small sizes and the four-point enumeration can be reproduced by the accompanying finite audit. The general quotient theorem above is a hand proof independent of those finite tests. Recent Lean CI is still unavailable, so no new Lean source or machine-verification claim.
