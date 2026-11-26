# Last fair-model four-point case: exact forced-pair reduction

Internal partial result, not a proof of a probability limit. Target 011010111 has peripheral labels A=old 1, Z=old 2, B=old 3; its only absent arrows are A->A, Z->A, Z->B. The remaining label C is the universal reflexive center. Fix theta in (0,1), rho=1-theta, and m labelled vertices with independent ordered edges including loops.

## Necessary witness and deterministic completion

For a successful surjective bounded morphism, A is independent, and the set of rows outside A missing A is exactly Z. Every row hits Z. For fixed disjoint nonempty A,Z, put

    M={y outside A union Z: no row in Z has an edge to y},
    C0=[m] minus (A union Z union M).

Then B is a nonempty subset of M, and every row outside Z must hit M. In particular M nonempty is necessary. These conditions give a necessary witness depending on the pair A,Z, with Z uniquely determined by A.

A sufficient witness is obtained by using B=M and C=C0: additionally require C0 nonempty and every row to hit C0. Then all four labels have exactly the successor images dictated by the missing arrows. Any row in Z misses A and M, every other row except A hits A, and A misses A by independence. Every non-Z row hits M, and all rows hit Z,C0. This is exactly a surjective bounded morphism.

The necessary witness does not automatically give the sufficient witness: enlarging B to M might remove some of the original C successors. We therefore keep distinct counts Y_necess and Y_suff, for which

    P(Y_suff>0)<=p_m<=P(Y_necess>0)<=E[Y_necess].

## Exact expectations

Let a=|A|, z=|Z|, n=m-a-z. For each fixed disjoint A,Z with a,z>=1, n>=1, the probability of independence of A, the exact definition of Z, and every row hitting Z is

    H(a,z)=rho^(a^2+a*z)*(1-rho^a)^n*(1-rho^z)^m.

These events use only columns ending in A or Z. The remaining coordinates Z x ([m] minus (A union Z)) are independent and make |M| distributed as Bin(n,rho^z). Conditional on M and the Z-row column tests, the edges from rows outside Z to M are fresh; the probability all these rows hit M is (1-rho^k)^(m-z) when k=|M|.

Thus the necessary witness expectation is exactly

    E[Y_necess] =
      sum_{a,z>=1,a+z<m} binom(m,a)*binom(m-a,z)*H(a,z)
        * sum_{k=1}^n binom(n,k)*rho^(z*k)*(1-rho^z)^(n-k)
                       *(1-rho^k)^(m-z).

For sufficient witnesses, restrict 1<=k<=n-1 and let c=n-k. In addition to the previous factors multiply by

    (1-rho^c)^(m-z) * J(z,c),

where

    J(z,c)=sum_{j=0}^z (-1)^j binom(z,j)
               *((rho^j-rho^z)/(1-rho^z))^c.

Indeed, all rows outside Z must hit C0, using fresh disjoint row/fibre blocks. For Z rows, conditional on M, each C0 column has a nonempty vector of edges from Z, independent across those columns. For a specified j rows of Z the probability all j rows miss one such column is (rho^j-rho^z)/(1-rho^z), because the column is required nonempty. Inclusion-exclusion over Z rows failing to hit C0 gives J. Alternatively 1-z*rho^c<=J<=1 by the union bound, since the conditional miss probability for any one row is <=rho^c per column.

There are binom(m,a)binom(m-a,z) pairs. Linearity of expectation suffices; no assumption of independence between pairs is made. These exact formulas are counts of pair witnesses, not counts of arbitrary full maps.

## What remains

This removes the free choice of B and C from the necessary event, making a substantially smaller counting problem. The asymptotic behavior of the expectation and any matching second moment remain open here. Growth of the expectation alone would not settle existence. The full fair-model census stands at 103/104 (92 zero, 11 one, this single unresolved type). For biases outside the interval in TWO_STAGE_FORCED_FIBRE_POSITIVE.md, another type also remains unresolved. No novelty or Lean verification claim.
