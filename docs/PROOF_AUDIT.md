# Proof audit: three-point central frames

## Finite quotient classification

Use vertex order (c,a,b).

For
```text
F0001:
c -> {c,a,b}
a -> {c}
b -> {c,b}
```
there is no surjective bounded morphism onto any two-point frame.

For
```text
F1001:
c -> {c,a,b}
a -> {c,a}
b -> {c,b}
```
there is exactly one two-block fibre partition, up to swapping target labels, that defines a bounded morphism:
```text
{c} | {a,b}
```
The quotient is T2, the complete reflexive two-point frame. The other two partitions fail the back condition. For example, under {a}|{c,b}, the quotient relation from the second fibre to {a} is forced by c->a, but b has no edge to a. The third partition fails symmetrically.

The earlier statement in this file that all three partitions work was wrong. The corrected classification is checked by `experiments/finite_quotient_audit.py` and the finite Lean theorems. Latest CI run [45554576671](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45554576671) passed all Python audits and `lake build`.

## F0001 first moment

For fibres A, B, C corresponding to a, b, c in F0001, forth forbids A->A, A->B, and B->A. The selected necessary-condition event additionally requires every A-vertex to reach C and every C-vertex to reach A.

These are only necessary conditions, not the complete back condition. The random variable Z_n counts partitions satisfying precisely this weaker event, so
`{G_n admits F0001 as an image} subseteq {Z_n >= 1}`.
The displayed expectation in `proofs/F0001_first_moment.md` is therefore the expectation of Z_n, not the expected number of all bounded morphisms.

I checked the edge rectangles in this expectation: the forbidden rectangles A×A, A×B, B×A and required rectangles A×C, C×A are pairwise disjoint. The binomial reduction and the small/large Poisson point-mass split are consistent with the stated labelled G(n,1/2) directed-frame model. The argument is a hand proof, not a Lean theorem.

## F1001 first moment

For fibres A, B, C corresponding to a, b, c in F1001, forth forbids A->B and B->A. The back condition is equivalent to:
- each row in A∪C hits A;
- each row in B∪C hits B;
- every row hits C.

The three destination rectangles are disjoint, so the product in the exact first-moment formula is justified by independence. I rechecked the small-fibre binomial reduction, large-fibre tail bound, Poisson cross-sum maximum, and remaining middle-tail Stirling estimate. The displayed majorant M_{i,d} is summable over i,d; the diagonal Poisson point-mass estimate is also summable off its at-most-two central indices.

This supports the proposed hand proof under the exact model stated in the document. It remains a hand proof: constants and uniformity should be written out in a referee-ready version, and no asymptotic theorem is formalized in Lean.

## 0101 and 1011

The earlier construction sketches rely on choosing a set A from one block of edge variables and then claiming independence of edges used to construct B and C. The precise sigma-algebras must be written down. The 1011 second-moment calculation must include all overlap classes and verify the constants in the exponent. Neither asymptotic claim is currently accepted.

## Logic and minimality claims

The characteristic-formula argument requires:
1. the Jankov–Fine theorem for the exact modal language and frame-validity convention;
2. the precise characterization of finite frames validating ML^r;
3. proof that the two target frames validate ML^r;
4. the correct bounded-morphism direction.

Do not infer independence merely from non-isomorphism. The proposed independence argument uses F0001 and F1001 as countermodels in opposite directions, subject to the cited characterization and characteristic-formula theorem.

## Formalization boundary

Lean currently formalizes finite frame data, bounded-morphism facts, and finite enumeration only. It does not formalize probability, characteristic formulas, almost-sure validity, or asymptotic limits.

## Reproducible checks

- `experiments/finite_quotient_audit.py`: all six surjections Fin 3 -> Fin 2 and all sixteen possible target relations.
- `experiments/exact_random_frames.py`: exhaustive labelled random source-frame counts for n=3,4.
- `RandomKripke/ExactSmallN.lean`: exact n=3 counts, currently being checked by CI after replacing a noncomputable existential filter with a finite Boolean search.
