"""Finite regression audit of the stronger overlap lemma; not an asymptotic proof."""
from itertools import combinations, product


def orientations(r):
    pairs = list(combinations(range(1, r+1), 2))
    for states in product(range(3), repeat=len(pairs)):
        yield {(i,j) if state == 1 else (j,i)
               for (i,j), state in zip(pairs,states) if state}


def balanced_maps(m,r,a):
    target = [m-r*a] + [a]*r
    for labels in product(range(r+1), repeat=m):
        if [labels.count(i) for i in range(r+1)] == target:
            yield labels


def audit():
    total = 0
    selected4 = [
        set(),
        {(1,2),(2,3),(3,4)},
        {(1,2),(2,3),(3,4),(4,1)},
        set(combinations(range(1,5),2)),
        {(1,2),(2,3),(3,1),(4,2),(4,1),(3,4)},
    ]
    for m,r,a in [(4,2,1),(5,2,2),(5,3,1),(6,4,1)]:
        maps = list(balanced_maps(m,r,a))
        patterns = list(orientations(r)) if r < 4 else selected4
        checked = 0
        for edges in patterns:
            Q = (r*r-len(edges))*a*a
            masks = []
            for f in maps:
                U = sum(1 << x for x in range(m) if f[x])
                H = sum(1 << (m*x+y) for x in range(m) for y in range(m)
                        if f[x] and f[y] and (f[x],f[y]) not in edges)
                assert H.bit_count() == Q
                masks.append((U,H))
            for U,H in masks:
                for V,J in masks:
                    k = r*a-(U&V).bit_count()
                    assert 2*(Q-(H&J).bit_count()) >= (r+1)*a*k
                    checked += 1
        total += checked
        print(m,r,a,len(patterns),len(maps),checked)
    assert total == 748332
    print(f"Checked {total} ordered balanced-map pairs across oriented targets.")


if __name__ == "__main__":
    audit()
