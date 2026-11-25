# Logical consequences of the three-point classification

Status: internal deductions from the preceding hand proofs, not independent peer review or Lean verification. No priority claim.

## Primary source and language

Valentin Goranko, The modal logic of almost sure frame validities in the finite, AiML 2020, pp. 249-268, https://www.aiml.net/volumes/volume13/Goranko.pdf. Definition 2.2 and Lemmas 2.3-2.4 (pp. 255-256) give the universal-modality characteristic formula and its correspondence to full surjective bounded morphisms. Section 3.1 (p. 259) gives the ordinary-modal translation on frames with R^2 universal; Proposition 3.5 (p. 261) identifies finite ML^r frames with central-point frames. Proposition 4.2(ii) and Proposition 4.4 (p. 263) connect the finite models and axioms of ML^as with these characteristic formulas. Primary-source text inspected; attempts to retrieve PDF page images timed out. Schamm's figure ordering remains unverified.

For a finite target F with vertices i, choose distinct atoms p_i. Define Delta as the conjunction of: each p_i is realized somewhere (existential global modality); exactly one p_i holds at each point (under outer universal modality); for every target arrow i->j, p_i implies diamond p_j; for every missing target arrow, p_i implies box not p_j. Set chi_F=not [U]Delta. Failure of this formula is equivalent to a valuation whose labels give a surjective bounded morphism: the partition supplies the function, the required successor hits give back, and the forbidden edges give forth. Conversely any such map supplies that valuation. This derivation does not rely on generated subframes.

In the ordinary modal language replace [U] by box box and its dual by diamond diamond, obtaining chi_F^d. On any frame with R^2 universal this preserves truth at every point by induction. For the random source with fixed edge probability theta, a union bound shows

    P(R^2 not universal) <= m^2 (1-theta^2)^(m-2).

For each ordered x,y, the candidate intermediate vertices z outside {x,y} use disjoint pairs of edge coordinates, including when x=y. Every candidate succeeds with probability theta^2. Thus the error tends to zero exponentially. In particular the limit of ordinary frame validity of chi_F^d equals 1-lim p_m(F) whenever the latter limit exists.

## Complete three-point logical classification

By THREE_POINT_CENTRAL_QUALITATIVE_CLASSIFICATION.md, in the fair model (indeed for every fixed theta), chi_F^d is almost surely valid for the eleven patterns

    0000,0001,0010,0011,0100,0110,0111,1000,1001,1100,1110,

and its frame-validity probability tends to zero for

    0101,1010,1011,1101,1111.

Here the bits are aa,ab,ba,bb; central c is reflexive and bidirectionally universal. Each target itself has universal R^2 and falsifies its own chi_F^d, but validates ML^r by Proposition 3.5. The eleven characteristic formulas therefore lie in ML^as minus ML^r, conditional on the hand probability proofs.

## Minimality among central targets of size at most three

A two-point central target is either K2 (only peripheral loop absent) or the complete reflexive T2. K2 has vanishing image probability (known from Le Bars; our r=1 estimate also proves it); T2 and the reflexive singleton E1 have image probability tending to one by fixed partitions. Any proper surjective image of a three-point central target has size one or two and remains central, since the image of c is central.

To audit two-point quotients, enumerate the three nontrivial bipartitions of {c,a,b}. A bipartition is a bounded-morphic quotient iff points in the same block have identical sets of successor blocks. Label the block containing c by 0; the only possible quotient row masks are (3,1) for K2 or (3,3) for T2. Direct enumeration gives:

| pattern | two-point images |
|---|---|
|0000|K2|
|0001|none|
|0010|K2|
|0011|K2|
|0100|K2|
|0101|T2|
|0110|K2,T2|
|0111|K2,T2|
|1000|none|
|1001|T2|
|1010|T2|
|1011|T2|
|1100|K2|
|1101|T2|
|1110|K2,T2|
|1111|T2|

The central three-point targets with vanishing image probability and no proper image with vanishing probability are precisely 0001,1000,1001. The first two are isomorphic by exchanging peripherals. Thus up to isomorphism exactly two three-point minimal targets are F0001 and F1001, in the sense of Goranko's minimality criterion (not absence of any proper quotient). K2 is the unique two-point minimal target. This does not preclude additional larger minimal targets.

## Relative independence

The frames F0001 and F1001 validate ML^r and chi_K2^d, since neither maps onto K2. They are nonisomorphic of equal finite size, so no surjective bounded morphism exists between them: any bijective bounded morphism is an isomorphism by forth and back. Hence F0001 validates chi_F1001^d but falsifies chi_F0001^d; F1001 validates chi_F0001^d but falsifies chi_F1001^d. Soundness of normal modal deduction establishes independence of these two axiom schemes over ML^r + chi_K2^d. This is a semantic finite-countermodel argument, not a proof that the two additions axiomatize all ML^as.

In fact every central target of size at most three with vanishing image probability either is one of the three minimal types (K2, F0001, F1001), or maps onto K2. In any frame with universal R^2, validation of chi_K2^d excludes all such targets by composition. Thus the characteristic formulas of these three minimal types account for the entire at-most-three-point central classification. No assertion about all finite frames of larger size, completeness, or the zero-one law for arbitrary modal formulas is made.

## Audit and limitations

The new construction in the three-point classification was rechecked: its selected reserve W is deterministic, all adaptive selections are measurable in edges ending in W, and the remaining row hits use only edges ending outside W. The conditional independence argument is valid. The quotient enumeration was independently executed in JavaScript on all 16 matrices and all six labelled two-block surjections. This verifies the finite classification, not the asymptotic proofs. Existing Lean CI remains unavailable. The primary-source text resolves the language convention; priority for the quantitative and qualitative results is still not established.
