# Related work and novelty audit

## Rainer Franz Schamm (2002): direct precursor

Rainer Franz Schamm, *Zero-One Laws and Almost Sure Validities on Finite Structures*, M.Sc. short dissertation, Rand Afrikaans University, January 2002; supervisor: Valentin Goranko.

The direct overlap is substantial:

1. Section 3.3.5 introduces \(F\)-partitions and gives the general first-moment formula for a fixed target frame and fixed fibre sizes.
2. Section 3.3.6 explicitly says that all 3-vertex frames with a central point were investigated experimentally. There are 16 such frames, corresponding to the 16 possible binary relations on the two non-central points.
3. Figure 4.1 classifies the 16 cases into “No growth”, “Very slow growth”, “Slow growth”, “Medium growth”, “Fast growth”, and “Very fast growth” categories.
4. The appendix gives an analytic first-moment proof for K4, the frame obtained from K3 by adding the arrow \(y_1\to y_2\).

This means the 16-frame candidate search and the use of the first-moment partition expectation are not new contributions of this repository. The current targets F0001 and F1001 are two members of that 16-frame family.

## Exact relation to the old enumeration

Schamm's Java code iterates the four non-central ordered pairs in this order:
\[
(y_1,y_1),\ (y_1,y_2),\ (y_2,y_1),\ (y_2,y_2).
\]
It uses successive binary bits to decide whether each arrow is present. Under that code convention:

- F0001 has bit mask 8 (only \(y_2\to y_2\));
- F1001 has bit mask 9 (both self-loops, no cross-arrows).

The text extraction of Figure 4.1 gives the 4×4 category labels but not the diagrams' full visual ordering. Under the natural row-by-row arrangement of the two adjacency rows, F0001 appears in a “No growth” cell and F1001 appears in a “Slow growth” cell. Treat this cell assignment as provisional until the original figure is inspected visually.

This creates a specific issue to resolve: our exact first-moment sum for F1001 is numerically decreasing over the tested range, and the current hand-proof draft claims that it tends to zero. If the old “Slow growth” label was intended to mean that the expectation grows rather than tends to zero, the new proof would correct an earlier experimental classification. The figure's encoding and the original numerical computation must be reconciled before claiming that correction.

## What remains potentially new

The plausible contribution is not discovering F0001/F1001 as candidates. It is:

- giving rigorous asymptotic first-moment proofs for these specific frames, rather than relying on the 2002 numerical/heuristic classification;
- checking whether the F1001 proof establishes a limit that the old figure classified differently;
- formalizing the finite quotient structure and exact small-n counts in Lean;
- providing reproducible, numerically stable calculations that can audit the earlier experiment.

Schamm's appendix proves K4 analytically, but the thesis does not provide analytic proofs for the two matrices studied here. A later-literature search is still required before making a priority or novelty claim.

## Later synthesis

Goranko's 2020 paper explicitly cites Schamm's empirical study and says that identifying which central-point frames have almost-surely valid characteristic formulas may require difficult combinatorial-probabilistic calculations. It then defines the minimality criterion used in this project: no proper bounded-morphic image F' may itself be a central-point frame with \(\chi_{F'}\in ML^{as}\).

See [THEORY_BACKGROUND.md](THEORY_BACKGROUND.md) for the theorem/page guide.


## Reproducible numerical cross-check

The new log-stable script `experiments/expected_partition_sum.py` evaluates the exact first-moment sum from the general formula in Schamm's Section 3.3.6. It counts all labelled surjective maps, not merely source frames that admit at least one map. Representative values are:

| n | E[X(F0001)] | E[X(F1001)] |
|---:|---:|---:|
| 3 | 0.01171875 | 0.01171875 |
| 50 | 0.000650884 | 0.127916528 |
| 100 | 0.000014376 | 0.092169675 |
| 200 | 0.000000119 | 0.069560675 |
| 500 | 6.30e-11 | 0.050743682 |
| 1,000 | 4.50e-14 | 0.040466990 |

This is a numerical audit only. In particular, F1001's expectation decreases much more slowly than F0001's over this range. It does not establish a limit. It does make the provisional “Slow growth” label for mask 9 in Figure 4.1 worth checking against the original figure ordering and the old Java computation. The asymptotic proof draft, if correct, would show that this expectation nevertheless tends to zero.
