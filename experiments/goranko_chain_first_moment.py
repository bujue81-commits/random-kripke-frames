#!/usr/bin/env python3
"""Exact log-space first moment of the necessary witness event for Goranko F_r.

For fixed r >= 2, a bounded morphism onto F_r must:
  (i) have no noncentral edge A_i -> A_j except the chain edges A_i -> A_{i+1};
  (ii) every row in the central fibre A_0 must hit each noncentral fibre A_j.

The script sums the exact expected number of ordered fibre partitions
satisfying just these necessary conditions. It is not a simulation and
does not count full bounded morphisms.
"""

from itertools import combinations
from math import exp, lgamma, log, log1p

LOG2 = log(2.0)


def positive_compositions(total: int, parts: int):
    """Yield ordered compositions of total into positive integer parts."""
    if parts == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - parts + 2):
        for rest in positive_compositions(total - first, parts - 1):
            yield (first,) + rest


def logsumexp(values):
    values = list(values)
    if not values:
        return float("-inf")
    peak = max(values)
    return peak + log(sum(exp(value - peak) for value in values))


def log_expected_witness(m: int, r: int) -> float:
    """Log E[Z_m] for the selected necessary event, exact up to float error."""
    if r < 1 or m <= r:
        raise ValueError("require r >= 1 and m > r")

    terms = []
    for central_size in range(1, m - r + 1):
        noncentral_total = m - central_size
        for sizes in positive_compositions(noncentral_total, r):
            forbidden = noncentral_total**2 - sum(
                sizes[i] * sizes[i + 1] for i in range(r - 1)
            )
            log_partition_count = (
                lgamma(m + 1)
                - lgamma(central_size + 1)
                - sum(lgamma(a + 1) for a in sizes)
            )
            log_probability = -forbidden * LOG2
            log_probability += central_size * sum(
                log1p(-(2.0 ** (-a))) for a in sizes
            )
            terms.append(log_partition_count + log_probability)

    return logsumexp(terms)


def check_small_exact_values() -> None:
    # For m=r+1 every fibre is a singleton.
    # r=2: 3! partitions, each has probability 2^-3 * (1/2)^2.
    assert abs(log_expected_witness(3, 2) - log(6 / 32)) < 1e-12
    # r=3: 4! partitions, each has probability 2^-7 * (1/2)^3.
    assert abs(log_expected_witness(4, 3) - log(24 / 1024)) < 1e-12


def main() -> None:
    check_small_exact_values()
    print("m,r,log_EZ,EZ")
    for r in (2, 3):
        for m in (10, 15, 20, 30, 40, 50, 75, 100):
            value = log_expected_witness(m, r)
            expectation = exp(value) if value > -745 else 0.0
            print(f"{m},{r},{value:.12f},{expectation:.12g}")


if __name__ == "__main__":
    main()
