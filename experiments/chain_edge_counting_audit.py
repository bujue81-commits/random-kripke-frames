"""Exhaustive small-map audit; not a substitute for the Lean proof."""
from itertools import product


def audit():
    checked = 0
    for r in range(1, 5):
        for m in range(1, 6):
            for labels in product(range(r + 1), repeat=m):
                noncentral = [x for x in range(m) if labels[x] != 0]
                odd = {x for x in noncentral if labels[x] % 2 == 1}
                even = set(noncentral) - odd
                pairs = set(product(noncentral, repeat=2))
                allowed = {(x, y) for x, y in pairs if labels[y] == labels[x] + 1}
                forbidden = pairs - allowed
                images = {(x, y) if x in odd else (y, x) for x, y in allowed}
                sizes = [labels.count(i) for i in range(1, r + 1)]
                adjacent = sum(a * b for a, b in zip(sizes, sizes[1:]))
                assert images <= set(product(odd, even))
                assert len(images) == len(allowed) == adjacent
                assert len(forbidden) == len(noncentral)**2 - adjacent
                assert 4 * len(forbidden) >= 3 * len(noncentral)**2
                checked += 1
    print(f"checked {checked} fibre maps")


if __name__ == "__main__":
    audit()
