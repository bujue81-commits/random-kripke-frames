#!/usr/bin/env python3
"""Exhaustive bounded-morphism audit for the two three-point frames.

No random sampling is used.  We enumerate all six surjections from a
three-element source to a two-element target and all sixteen target
relations, checking forth and back exactly.
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


def surjections_3_to_2():
    for f in product(range(2), repeat=3):
        if set(f) == {0, 1}:
            yield f


def target_relations_2():
    for bits in product((0, 1), repeat=4):
        yield (bits[:2], bits[2:])


def is_bounded_morphism(source, target, f):
    """Surjective bounded morphism, including forth and back."""
    if set(f) != {0, 1}:
        return False

    for x in range(3):
        # Forth
        for y in range(3):
            if source[x][y] and not target[f[x]][f[y]]:
                return False

        # Back
        for z in range(2):
            if target[f[x]][z] and not any(
                source[x][y] and f[y] == z for y in range(3)
            ):
                return False

    return True


K2 = (
    (1, 1),
    (1, 0),
)

COMPLETE_IRREFLEXIVE_3 = tuple(
    tuple(int(x != y) for y in range(3)) for x in range(3)
)

COLLAPSE_TO_K2 = (0, 0, 1)


def has_nonloop_successor_everywhere(frame):
    return all(
        any(frame[x][y] and not frame[y][y] for y in range(len(frame)))
        for x in range(len(frame))
    )


def has_two_step_reachability(frame):
    return all(
        any(frame[x][y] and frame[y][z] for y in range(len(frame)))
        for x in range(len(frame))
        for z in range(len(frame))
    )


def audit_eta_preservation_counterexample():
    assert is_bounded_morphism(
        COMPLETE_IRREFLEXIVE_3, K2, COLLAPSE_TO_K2
    )
    assert has_nonloop_successor_everywhere(COMPLETE_IRREFLEXIVE_3)
    assert not has_nonloop_successor_everywhere(K2)
    assert has_two_step_reachability(COMPLETE_IRREFLEXIVE_3)
    assert has_two_step_reachability(K2)
    print(
        "Goranko eta counterexample: verified p-morphism, eta source=true, "
        "eta target=false; both frames have two-step reachability."
    )


def audit(name, source):
    witnesses = []
    for f in surjections_3_to_2():
        for target in target_relations_2():
            if is_bounded_morphism(source, target, f):
                witnesses.append((f, target))

    print(f"{name}: {len(witnesses)} (map, target) witnesses")
    for f, target in witnesses:
        print(f"  map={f}, target={target}")

    partitions = {
        tuple(sorted((
            tuple(i for i in range(3) if f[i] == 0),
            tuple(i for i in range(3) if f[i] == 1),
        )))
        for f, _ in witnesses
    }
    print(f"  distinct fibre partitions: {len(partitions)}")
    return witnesses


if __name__ == "__main__":
    w0 = audit("F0001", F0001)
    w1 = audit("F1001", F1001)

    assert len(w0) == 0
    assert len(w1) == 2  # the same partition, with target labels swapped
    assert {w[1] for w in w1} == {
        ((1, 1), (1, 1))
    }
    assert len({
        tuple(sorted((
            tuple(i for i in range(3) if f[i] == 0),
            tuple(i for i in range(3) if f[i] == 1),
        )))
        for f, _ in w1
    }) == 1

    audit_eta_preservation_counterexample()
    print("All finite quotient checks passed.")
