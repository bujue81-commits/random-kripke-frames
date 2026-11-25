# Proof audit: three-point central frames

## Important correction

The earlier conversation described the F1001 two-point quotient as arising from a unique partition. That is false. For the frame

```text
c -> {c,a,b}
a -> {c,a}
b -> {c,b}
```

all three nontrivial two-block partitions of the three-element carrier induce a quotient isomorphic to the complete reflexive two-point frame. The correct structural statement is that every two-point bounded-morphic image is isomorphic to T2, not that there is a unique quotient partition.

## F0001 necessary conditions

For fibres A, B, C corresponding to a, b, c in F0001, the forbidden blocks are A->A, A->B, B->A. The forth/back conditions additionally require every A-vertex to reach C and every C-vertex to reach A. These conditions are necessary but not sufficient: the omitted back requirements for B and C must be included for an exact count. A first-moment upper bound may count only necessary conditions, but its event and expectation must be stated accordingly.

The previously displayed exact expectation formula for Z_n is the expectation for the selected necessary-condition event, not the expectation of all p-morphisms. This distinction must remain explicit.

## F1001 first moment

For fibres A, B, C corresponding to a, b, c in F1001:

- A->B and B->A are forbidden;
- every vertex in each fibre must reach every target fibre allowed by its row in the target frame.

The formula in the previous chat is a candidate exact first moment for the number of labelled fibre partitions. It must be independently re-derived from the complete event table before use.

The claimed Poisson cross-sum lemma is not accepted in this repository until each bound is proved with a summable majorant uniform in both indices. In particular, an asserted bound on M_{i,d} and the diagonal estimate require independent checking.

## 0101 and 1011

The previous construction sketches rely on choosing a set A from one block of edge variables and then claiming independence of edges used to construct B and C. The precise sigma-algebras must be written down. The 1011 second-moment calculation must include all overlap classes and verify the constants in the exponent. Neither asymptotic claim is currently accepted.

## Current formalization boundary

The Lean module currently formalizes only finite frame data and elementary structural properties. It does not formalize probability, characteristic formulas, almost-sure validity, or asymptotic limits.
