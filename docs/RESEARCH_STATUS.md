# Research status and proof obligations

Date: 2026-11-25

## Probability model

For each n, the sample space consists of all Boolean relations on Fin n. Every ordered pair, including loops, is independently present with probability 1/2. The sample space is labelled. Frame validity quantifies over all valuations; it is not truth at one selected valuation.

For a fixed finite frame F, write p_n(F) = P(G_n admits a surjective bounded morphism onto F). If chi_F is the appropriate Jankov–Fine characteristic formula, then mu_n(chi_F) = 1 - p_n(F).

## Three-point central frames

Use vertex order (c,a,b) and matrices

F0001 = [[1,1,1],[1,0,0],[1,0,1]]

F1001 = [[1,1,1],[1,1,0],[1,0,1]].

The following finite structural facts are elementary and are intended for Lean formalization:

- Both frames have central point c.
- Both frames are serial.
- F0001 has no surjective bounded morphism onto any two-point frame.
- Every surjective bounded morphism from F1001 onto a two-point frame has complete reflexive two-point target.
- F1001 maps onto the complete reflexive two-point frame.
- Both frames map onto the reflexive singleton.

The claim that F1001 has a unique two-point quotient partition is not correct: all three nontrivial two-block partitions of its three-element carrier induce the complete reflexive two-point quotient. The correct statement is uniqueness of the quotient target up to isomorphism (indeed, it is the complete reflexive two-point frame).

## Asymptotic claims: NOT YET VERIFIED

Detailed hand-proof drafts are now present in `proofs/F0001_first_moment.md` and `proofs/F1001_first_moment.md`.

- F0001: the first-moment count uses a deliberately weaker necessary-condition event; its exact expectation and one-dimensional reduction are written out, including uniform Poisson tail control.
- F1001: the exact fibre-partition expectation is written out. The proof uses a small/middle/large fibre decomposition, a Poisson cross-sum lemma with an explicit summable majorant, and a remaining middle-tail estimate.

These are now complete hand-proof drafts, but they have not yet been independently referee-checked or formalized in Lean. They should not be labelled machine-verified.

## Other three-point types

The proposed claims for types 0101, 1011, and 1111 also remain proof obligations. The independent-set and second-moment constructions need full conditional-independence checks, including whether the partition is selected using edge variables later assumed independent.

## Logic claims: conditional

The independence argument for characteristic formulas requires:

1. a correct Jankov–Fine theorem for the exact language and frame-validity convention;
2. the precise characterization of finite frames validating ML^r;
3. proof that the two frames validate ML^r;
4. the correct quotient/ bounded-morphism direction.

Do not infer independence merely from non-isomorphism.

## Lean status

The Lean files in this branch are source drafts only. No lake build has yet been run in this environment. Only finite combinatorial definitions and decidable finite claims are targeted initially. No asymptotic probability theorem is formalized.

## Next proof tasks

1. Build the Lean project and fix elaboration errors.
2. Independently verify finite quotient statements by exhaustive enumeration.
3. Re-derive the F0001 expectation and tail bounds.
4. Replace the F1001 Poisson lemma with a fully explicit, correctly dominated estimate.
5. Verify the 0101 and 1011 constructions.
6. Complete primary-source audit and novelty check.

## Exact small-n computation

The repository now contains `experiments/exact_random_frames.py`, which exhaustively enumerates all labelled source relations for n=3 and n=4 and checks every surjective map with bitset implementations of forth/back. The exact counts are recorded in `experiments/results/exact_small_n.md`: F0001 has 6/512 and 1332/65536 source frames mapping onto it; F1001 has 3/512 and 787/65536. These finite counts are reproducibility checks only, not evidence by themselves for an asymptotic limit. Both exhaustive scripts are included in CI.
