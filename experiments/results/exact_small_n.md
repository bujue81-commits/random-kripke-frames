# Exact small-n enumeration

The script `experiments/exact_random_frames.py` exhaustively enumerates all labelled directed relations, including loops, and checks every surjection to each target frame using the forth and back conditions.

| n | Target | Successful source frames | Total source frames | Exact probability |
|---:|---|---:|---:|---:|
| 3 | F0001 | 6 | 512 | 6/512 = 0.01171875 |
| 3 | F1001 | 3 | 512 | 3/512 = 0.005859375 |
| 4 | F0001 | 1,332 | 65,536 | 1,332/65,536 = 0.02032470703125 |
| 4 | F1001 | 787 | 65,536 | 787/65,536 = 0.0120086669921875 |

These are exact finite counts, not Monte Carlo estimates. They do not establish any asymptotic limit. Both this script and the finite quotient audit are run in GitHub Actions.
