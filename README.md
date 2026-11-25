# Random Kripke Frames

Research project on the almost-sure modal logic of random finite Kripke frames.

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
- Lean 4 definitions and finite theorems for frames and bounded morphisms;
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
```

The CI workflow runs both Python audits and `lake build`.

## Research discipline

- Distinguish proved results, conjectures, and open proof obligations.
- Do not infer asymptotic results from finite computations.
- Lean-checked finite theorems are distinct from hand-written asymptotic probability proofs.
- No `sorry` is used in completed Lean declarations.
- Bibliographic novelty remains to be checked against primary sources.

## Project notes

- [Research status](docs/RESEARCH_STATUS.md)
- [Proof audit](docs/PROOF_AUDIT.md)
- [F0001 first-moment proof](proofs/F0001_first_moment.md)
- [F1001 first-moment proof](proofs/F1001_first_moment.md)
- [Proper images and minimality](proofs/proper_images_and_minimality.md)
- [Exact small-n counts](experiments/results/exact_small_n.md)
