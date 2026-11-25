"""Exhaustive finite check of the overlap lemma; not an asymptotic proof."""
from itertools import product


def balanced_maps(m, r, a):
    target = [m-r*a] + [a]*r
    for labels in product(range(r+1), repeat=m):
        if [labels.count(i) for i in range(r+1)] != target:
            continue
        U = sum(1 << x for x in range(m) if labels[x])
        H = sum(1 << (m*x+y) for x in range(m) for y in range(m)
                if labels[x] and labels[y] and labels[y] != labels[x]+1)
        yield U, H


def audit():
    total = 0
    for m,r,a in [(4,2,1),(5,2,2),(6,2,2),(5,3,1),(7,3,2),(6,4,1)]:
        maps = list(balanced_maps(m,r,a))
        Q = (r*r-r+1)*a*a
        s = r*a
        for U,H in maps:
            assert H.bit_count() == Q
            for V,J in maps:
                k = s-(U & V).bit_count()
                assert (H & J).bit_count() <= Q-a*k
                total += 1
        print(m,r,a,len(maps),len(maps)**2)
    assert total == 539244
    print(f"Checked {total} ordered balanced-map pairs.")


if __name__ == "__main__":
    audit()
