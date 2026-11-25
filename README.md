# Random Kripke Frames

Research project on rigorous first-moment proofs and Lean formalization for selected three-point central frames in random finite Kripke frames. The candidate search itself has a 2002 precursor; see the related-work audit.

## Probability model

For each n, let

\[
G_n=([n],R_n),\qquad \Pr(xR_ny)=1/2
\]

independently for every ordered pair (x,y), including loops. The sample space is labelled.

For a fixed finite frame F, write

\[
p_n(F)=\Pr(G_n\twoheadrightarrow F),
\]

where the arrow denotes a surjective bounded morphism. Under the Jankov–Fine characteristic-formula correspondence,

\[
\mu_n(\chi_F)=1-p_n(F).
\]

## Current research target

Three-point central frames with vertex order (c,a,b):

\[
F_{0001}=\begin{pmatrix}1&1&1\\1&0&0\\1&0&1\end{pmatrix},
\qquad
F_{1001}=\begin{pmatrix}1&1&1\\1&1&0\\1&0&1\end{pmatrix}.
\]

The repository contains:
- Lean 4 definitions and finite theorems for frames and bounded morphisms (`RandomKripke/FiniteFrames.lean`);
- Lean equivalence between F1001 bounded morphisms and fibrewise partition conditions (`RandomKripke/F1001Characterization.lean`);
- Lean implication from an F0001 bounded morphism to the weaker witness event used in its first-moment estimate (`RandomKripke/F0001Witness.lean`);
- a finite Lean counterexample to the eta-preservation step in Goranko (2020), Proposition 4.7 (`RandomKripke/GorankoEtaCounterexample.lean`);
- a hand first-moment proof for the chain frames F_r, r≥2 (`proofs/GORANKO_CHAIN_FRAMES_FIRST_MOMENT.md`);
- Lean exact n=3 labelled source-frame counts (`RandomKripke/ExactSmallN.lean`);
- exact Python quotient audits;
- exact small-n random-frame enumeration;
- hand-proof drafts for the first-moment estimates;
- an audit of proper bounded-morphic images and minimality.

## Build and reproduce

```bash
lake exe cache get
lake build
python3 experiments/finite_quotient_audit.py
python3 experiments/exact_random_frames.py
python3 experiments/expected_partition_sum.py
python3 experiments/goranko_chain_first_moment.py
# Optional larger-n audit (requires: pip install numpy scipy)
python3 experiments/large_n_audit_numpy.py
```

The CI workflow runs all three Python audits, the standard `lake build`, and explicit builds of `RandomKripke.ExactSmallN`, `RandomKripke.F1001Characterization`, `RandomKripke.F0001Witness`, and `RandomKripke.GorankoEtaCounterexample`.

## Current hand-proof bounds

The current asymptotic proof drafts claim

\[
\Pr(G_n\twoheadrightarrow F_{0001})=O(1/\sqrt{\ln n}),\qquad
\Pr(G_n\twoheadrightarrow F_{1001})=O(1/\ln n).
\]

These are hand proofs, not Lean-verified probability theorems or externally refereed results. The Goranko chain-family estimate is also a hand proof: for each fixed r≥2 it claims exp(-Ω_r((ln m)^2)).

## Research discipline

- Distinguish proved results, conjectures, and open proof obligations.
- Do not infer asymptotic results from finite computations.
- Lean-checked finite theorems are distinct from hand-written asymptotic probability proofs.
- No `sorry` is used in completed Lean declarations.
- Bibliographic novelty remains to be checked against primary sources.

## Project notes

- [Theory background: Goranko's framework and minimality](docs/THEORY_BACKGROUND.md)
- [Related work and novelty audit](docs/RELATED_WORK.md)
- [Research status](docs/RESEARCH_STATUS.md)
- [Proof audit](docs/PROOF_AUDIT.md)
- [Independent F0001/F1001 proof audit](proofs/INDEPENDENT_PROOF_AUDIT_2026-11-25.md)
- [Goranko Proposition 4.7 eta-preservation counterexample](proofs/GORANKO_2020_PROP_4_7_ETA_COUNTEREXAMPLE.md)
- [F0001 first-moment proof](proofs/F0001_first_moment.md)
- [F1001 first-moment proof](proofs/F1001_first_moment.md)
- [Proper images and minimality](proofs/proper_images_and_minimality.md)
- [Exact small-n counts](experiments/results/exact_small_n.md)
- [Bibliography](references.bib)
