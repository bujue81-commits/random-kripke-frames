#!/usr/bin/env python3
"""Exact enumeration of labelled random frames for n=3,4.

The graph mask encodes all n^2 ordered edges, including loops.
For each graph, we test every surjection onto the target frame using
bitset versions of the forth and back conditions. No sampling occurs.
"""

from itertools import product

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


def surjections(n, k=3):
    return [
        f for f in product(range(k), repeat=n)
        if len(set(f)) == k
    ]


def exact_count(n, target):
    """Return (number of source relations mapping onto target, total)."""
    maps = surjections(n)
    total = 1 << (n * n)
    full = (1 << n) - 1

    # Precompute target fibres and the forth/back data for each map.
    prepared = []
    for f in maps:
        fibres = [
            sum(1 << y for y in range(n) if f[y] == j)
            for j in range(3)
        ]
        allowed = [
            sum(fibres[j] for j in range(3) if target[i][j])
            for i in range(3)
        ]
        required = [
            tuple(j for j in range(3) if target[i][j])
            for i in range(3)
        ]
        prepared.append((f, fibres, allowed, required))

    count = 0
    for graph in range(total):
        successors = [
            (graph >> (x * n)) & full
            for x in range(n)
        ]

        has_morphism = False
        for f, fibres, allowed, required in prepared:
            valid = True
            for x in range(n):
                row = successors[x]
                target_row = f[x]

                # Forth: no edge may leave the allowed target fibres.
                if row & (full ^ allowed[target_row]):
                    valid = False
                    break

                # Back: every allowed target fibre must be reached.
                for j in required[target_row]:
                    if not (row & fibres[j]):
                        valid = False
                        break

                if not valid:
                    break

            if valid:
                has_morphism = True
                break

        if has_morphism:
            count += 1

    return count, total


if __name__ == "__main__":
    expected = {
        (3, "F0001"): (6, 512),
        (3, "F1001"): (3, 512),
        (4, "F0001"): (1332, 65536),
        (4, "F1001"): (787, 65536),
    }

    for n in (3, 4):
        for name, target in (("F0001", F0001), ("F1001", F1001)):
            result = exact_count(n, target)
            print(f"n={n} {name}: {result[0]}/{result[1]} "
                  f"= {result[0] / result[1]:.9f}")
            assert result == expected[(n, name)]

    print("All exact small-n counts verified.")
