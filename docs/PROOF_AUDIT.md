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

The earlier statement in this file that all three partitions work was wrong. The corrected classification is checked by `experiments/finite_quotient_audit.py` and the finite Lean theorems. Latest CI run [45555290042](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45555290042) passed all Python audits and `lake build`.

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

Lean formalizes finite frame data, bounded-morphism facts and composition, finite quotient statements, exact n=3 labelled counts, the F1001 fibrewise characterization, and the implication from an F0001 bounded morphism to the weaker witness event. It does not formalize probability, characteristic formulas, almost-sure validity, or asymptotic limits.

## Reproducible checks

- `experiments/finite_quotient_audit.py`: all six surjections Fin 3 -> Fin 2 and all sixteen possible target relations.
- `experiments/exact_random_frames.py`: exhaustive labelled random source-frame counts for n=3,4.
- `RandomKripke/ExactSmallN.lean`: exact n=3 counts, now explicitly built in CI;
- `RandomKripke/F1001Characterization.lean`: exact F1001 fibrewise characterization;
- `RandomKripke/F0001Witness.lean`: bounded morphisms onto F0001 imply the weaker necessary witness conditions.


## 2026-11-25 independent audit update

See [the detailed audit](../proofs/INDEPENDENT_PROOF_AUDIT_2026-11-25.md). No fatal gap was found in the current F0001 or F1001 first-moment derivations. The F1001 proof has been strengthened with an explicit uniform central-Poisson error and a fully displayed Stirling bound. The generic Python audit's (a,b,c) versus (c,a,b) matrix-order mismatch has been corrected; the aggregate total was invariant under the permutation, but the fixed-fibre term now matches the proof and is checked directly. Large-n exploratory values through n=30,000 are reproducible with the optional NumPy/SciPy script. None of this formalizes the asymptotic proof in Lean.


## Lean build coverage correction

The previous green CI run compiled RandomKripke.FiniteFrames only; its log did not include RandomKripke.ExactSmallN. The exact-count module therefore was not covered by the default lake build. A further source audit found the F1001 count theorem referenced the F0001 source set (claiming that same finite set had both cardinalities 6 and 3). This has been corrected, and the workflow now explicitly invokes lake build RandomKripke.ExactSmallN. The explicit build has now passed: CI run [45567277661](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45567277661) logs the command lake build RandomKripke.ExactSmallN followed by “Build completed successfully”. The corrected exact n=3 count declarations are now Lean-checked.


## Quantitative F1001 conclusion

The F1001 proof now establishes the stronger upper bound (\Pr(G_n\twoheadrightarrow F1001)=O(1/\ln n)), not merely convergence to zero. The refinement sharpens both the Poisson cross-sum to (O(1/m_n)) and the remaining middle tail to (O(1/\ln n)). It remains a hand proof and is not formalized in Lean or externally refereed.


## Lean fibre characterization

RandomKripke/F1001Characterization.lean now proves boundedMorphism_F1001_iff_partitionConditions, translating the F1001 p-morphism definition exactly into the five fibrewise conditions used in the probability calculation. CI run [45568777128](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45568777128) explicitly built this module and RandomKripke.ExactSmallN successfully. This formalizes the finite combinatorial event, not its random probability or asymptotics.


## Quantitative first-moment bounds and current Lean modules

The two current hand-proof bounds are
\[
\Pr(G_n\twoheadrightarrow F_{0001})=O(1/\sqrt{\ln n}),
\qquad
\Pr(G_n\twoheadrightarrow F_{1001})=O(1/\ln n).
\]
For F0001, the large-fibre sum is reduced to Poisson point masses; at most two indices have \(r_a\in[1/2,2]\), each contributing \(O(1/\sqrt{\ln n})\). For F1001, the Poisson cross-sum is \(O(1/m_n)\), and the remaining middle tail is sharpened to \(O(1/\ln n)\) by isolating the at-most-two indices with \(r_a\in[1,4]\). These are hand estimates, not Lean formalizations.

The Lean modules now cover three distinct finite statements:
- ExactSmallN: exact labelled source-frame counts for n=3;
- F1001Characterization: exact equivalence between F1001 bounded morphisms and the fibrewise conditions;
- F0001Witness: implication from a bounded morphism onto F0001 to the weaker event counted in the F0001 first moment.

CI run [45569425119](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45569425119), head c1efeb9418e14505ee287e3093489aa0d5a18cfb, passed the Python audits and explicitly built all three Lean modules. The probability estimates themselves remain unformalized.


The latest CI run [45569425119](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45569425119), head c1efeb9418e14505ee287e3093489aa0d5a18cfb, passed all Python audits and explicitly built all three Lean modules. The asymptotic probability bounds remain hand proofs.


## Side finding: Goranko Proposition 4.7

The preservation assertion used in Proposition 4.7 for \(\eta=\forall x\exists y(Rxy\land\neg Ryy)\) is contradicted by the finite bounded morphism in RandomKripke/GorankoEtaCounterexample.lean. The source is the complete irreflexive three-point frame; the target has edges (0,0),(0,1),(1,0); the map sends 0,1 to 0 and 2 to 1. The source satisfies eta, the target does not, and the map satisfies forth, back, and surjectivity. Both frames have two-step reachability.

This shows a gap in the cited preservation argument, not that Proposition 4.7's final conclusion is false. The current CI build of the new module is pending after replacing the non-executable classical tactic with decide.
