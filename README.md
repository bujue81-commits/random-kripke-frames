# Random Kripke Frames

Research project on the almost-sure modal logic of random finite Kripke frames.

## Scope

The probability model is the labelled random directed frame
\[
G_n=([n],R_n),\qquad \Pr(xR_ny)=1/2
\]
independently for every ordered pair \((x,y)\), including loops.

The project studies probabilities of surjective bounded morphisms
\[
p_n(F)=\Pr(G_n\twoheadrightarrow F)
\]
and their connection with almost-sure frame validity.

## Research discipline

- Distinguish proved results, conjectures, and open proof obligations.
- Do not infer asymptotic results from finite computations.
- Do not mark Lean declarations as verified until the project builds successfully.
- Do not use `sorry` in completed formal proofs.
- Record exact model definitions and cite primary sources.

## Current status

The repository is being initialized. The initial research branch will contain a conservative scaffold and an audit of the three-point central-frame claims. In particular, the proposed proof for the frame encoded as `1001` is not treated as established until its asymptotic estimates have been independently checked.
