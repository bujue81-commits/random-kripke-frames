#!/usr/bin/env python3
"""Numerically audit the exact first-moment sums for F0001 and F1001.

For each positive fibre-size triple (a,b,c), the summand is the exact
probability that the corresponding fixed surjective map is a bounded
morphism, multiplied by the multinomial number of labelled partitions.
All calculations are performed in log space.
"""

from math import exp, lgamma, log, log1p

F0001 = (
    (1, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
)

F1001 = (
    (1, 1, 1),
    (1, 1, 0),
    (1, 0, 1),
)

# Both matrices above use vertex order (c, a, b).
LOG2 = log(2.0)


def log_fixed_partition_term(n, target, sizes):
    """Log probability that one fixed map is a bounded morphism.

    The sizes must follow the target matrix's vertex order (c, a, b).
    """
    value = lgamma(n + 1) - sum(lgamma(k + 1) for k in sizes)
    for i, ki in enumerate(sizes):
        for j, kj in enumerate(sizes):
            if target[i][j]:
                value += ki * log1p(-(2.0 ** (-kj)))
            else:
                value -= ki * kj * LOG2
    return value


def logsumexp(values):
    values = list(values)
    peak = max(values)
    return peak + log(sum(exp(value - peak) for value in values))


def log_expected_morphisms(n, target):
    """Log of E[number of surjective bounded morphisms G_n -> target]."""
    terms = []

    for a in range(1, n - 1):
        for b in range(1, n - a):
            c = n - a - b
            # The target matrices are ordered (c,a,b), whereas the
            # proof variables are the non-central fibre sizes (a,b,c).
            sizes = (c, a, b)
            terms.append(log_fixed_partition_term(n, target, sizes))

    return logsumexp(terms)


def main():
    print("n,F0001_logE,F0001_E,F1001_logE,F1001_E")
    for n in (3, 50, 100, 200, 500, 1000):
        l0 = log_expected_morphisms(n, F0001)
        l1 = log_expected_morphisms(n, F1001)
        e0 = exp(l0) if l0 > -745 else 0.0
        e1 = exp(l1) if l1 > -745 else 0.0
        print(f"{n},{l0:.12f},{e0:.12g},{l1:.12f},{e1:.12g}")

    # Termwise check: for F1001 in (c,a,b) order, the exact fixed-map
    # probability agrees with the formula in the hand proof.
    n, a, b = 30, 4, 5
    c = n - a - b
    term = log_fixed_partition_term(n, F1001, (c, a, b))
    direct = (
        lgamma(n + 1) - lgamma(a + 1) - lgamma(b + 1) - lgamma(c + 1)
        - 2 * a * b * LOG2
        + n * log1p(-(2.0 ** (-c)))
        + (n - b) * log1p(-(2.0 ** (-a)))
        + (n - a) * log1p(-(2.0 ** (-b)))
    )
    assert abs(term - direct) < 1e-12

    # Cross-check the exact first moments against brute-force enumeration.
    exact_map_counts = {
        (3, "F0001"): (6, 512),
        (3, "F1001"): (6, 512),
        (4, "F0001"): (1332, 65536),
        (4, "F1001"): (1620, 65536),
    }
    for (n, name), (maps, total) in exact_map_counts.items():
        target = F0001 if name == "F0001" else F1001
        expected_log = log(maps / total)
        assert abs(log_expected_morphisms(n, target) - expected_log) < 1e-12

    print("n=3,4 first moments agree with exact labelled map counts.")


if __name__ == "__main__":
    main()
