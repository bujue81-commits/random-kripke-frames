#!/usr/bin/env python3
"""Optional large-n numerical audit (requires numpy and scipy).

This evaluates the exact first-moment sum in log space using vectorized
rows. The target matrices and fibre sizes are both interpreted in the
vertex order (c,a,b), while the mathematical summation variables are
the sizes a=|h^-1(a)|, b=|h^-1(b)|, c=|h^-1(c)|.
"""

import math
import numpy as np
from scipy.special import gammaln, logsumexp


def log_expected(n: int, target: str) -> float:
    log_hit = np.empty(n + 1, dtype=np.float64)
    log_hit[0] = -np.inf
    k = np.arange(1, n + 1, dtype=np.float64)
    log_hit[1:] = np.log1p(-np.exp2(-k))

    log_n_fact = gammaln(n + 1)
    log_two = math.log(2.0)
    row_sums = []

    for a in range(1, n - 1):
        b = np.arange(1, n - a, dtype=np.int64)
        c = n - a - b
        value = (
            log_n_fact
            - gammaln(a + 1)
            - gammaln(b + 1)
            - gammaln(c + 1)
        )

        if target == "F1001":
            # 2^{-2ab} (1-2^{-c})^n
            #          (1-2^{-a})^{n-b} (1-2^{-b})^{n-a}
            value += (
                -2.0 * a * b * log_two
                + n * log_hit[c]
                + (n - b) * log_hit[a]
                + (n - a) * log_hit[b]
            )
        elif target == "F0001":
            # 2^{-a^2-2ab} (1-2^{-c})^n
            #              (1-2^{-a})^c (1-2^{-b})^{n-a}
            value += (
                -(a * a + 2.0 * a * b) * log_two
                + n * log_hit[c]
                + c * log_hit[a]
                + (n - a) * log_hit[b]
            )
        else:
            raise ValueError("target must be F0001 or F1001")

        row_sums.append(logsumexp(value))

    return float(logsumexp(row_sums))


def check_exact_small_n() -> None:
    expected = {
        (3, "F0001"): (6, 512),
        (3, "F1001"): (6, 512),
        (4, "F0001"): (1332, 65536),
        (4, "F1001"): (1620, 65536),
    }
    for (n, target), (maps, total) in expected.items():
        got = log_expected(n, target)
        want = math.log(maps / total)
        assert abs(got - want) < 1e-10, (n, target, got, want)


def main() -> None:
    check_exact_small_n()
    print("n,F0001_E,F1001_E")
    for n in (1000, 2000, 5000, 10000, 20000, 30000):
        e0 = math.exp(log_expected(n, "F0001"))
        e1 = math.exp(log_expected(n, "F1001"))
        print(f"{n},{e0:.12g},{e1:.12g}")


if __name__ == "__main__":
    main()
