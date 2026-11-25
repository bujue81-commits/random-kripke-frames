# Exact small-n enumeration

The script `experiments/exact_random_frames.py` exhaustively enumerates all labelled directed relations, including loops, and checks every surjection to each target frame using the forth and back conditions.

| n | Target | Source relations admitting a map | Total source relations | Surjective maps summed over all sources |
|---:|---|---:|---:|---:|
| 3 | F0001 | 6 | 512 | 6 |
| 3 | F1001 | 3 | 512 | 6 |
| 4 | F0001 | 1,332 | 65,536 | 1,332 |
| 4 | F1001 | 787 | 65,536 | 1,620 |

The final column is the exact total number of surjective bounded morphisms, summed over every source relation. Dividing it by the total number of source relations gives the exact first moment \(\mathbb E X_n\). For n=3 and n=4 these values agree with the log-stable partition-sum script `experiments/expected_partition_sum.py`.

These are exact finite counts, not Monte Carlo estimates. They do not establish any asymptotic limit. The quotient audit, exact source-frame enumeration, and first-moment numerical audit are run in GitHub Actions.
