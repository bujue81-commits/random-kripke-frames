"""Finite regression for LOOPLESS_CENTRAL_BIASED_RATE.md, not an asymptotic proof."""
from itertools import product


def graphs(r):
    pairs = [(i,j) for i in range(1,r+1) for j in range(1,r+1) if i != j]
    for mask in range(1 << len(pairs)):
        yield {p for k,p in enumerate(pairs) if mask & (1 << k)}


def balanced_maps(m,r,a):
    target = [m-r*a] + [a]*r
    for labels in product(range(r+1), repeat=m):
        if [labels.count(i) for i in range(r+1)] == target:
            yield labels


def overlap_audit():
    checked = 0
    for m,r,a in [(3,1,1),(4,2,1),(5,2,2),(5,3,1)]:
        maps = list(balanced_maps(m,r,a))
        for edges in graphs(r):
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
                    assert (H&J).bit_count() <= Q-a*k
                    checked += 1
    assert checked == 234585
    print(f"Checked {checked} ordered map pairs.")


def probability_audit():
    checked = 0
    for f in [(0,1),(0,0,1),(0,1,2),(0,0,1,2),(0,1,1,2),
              (0,1,2,2),(0,1,2,3)]:
        m,r = len(f),max(f)
        a = [f.count(i) for i in range(r+1)]
        for edges in graphs(r):
            for h,den in [(1,2),(1,3),(2,3),(1,4),(3,4)]:
                u = den-h
                def allowed(i,j):
                    return i == 0 or j == 0 or (i,j) in edges
                Q = sum(a[i]*a[j] for i in range(1,r+1)
                        for j in range(1,r+1) if not allowed(i,j))
                full = witness = u**Q
                hit = 0
                for i in range(r+1):
                    for j in range(r+1):
                        if allowed(i,j):
                            full *= (den**a[j]-u**a[j])**a[i]
                            if i == 0 and j:
                                witness *= (den**a[j]-u**a[j])**a[0]
                                hit += a[0]*a[j]
                witness *= den**(m*m-Q-hit)
                # Both formula numerators have denominator den**(m*m).
                # Independently enumerate every row and multiply its exact weight.
                exact_full = exact_witness = 1
                for i in f:
                    row_f = row_w = 0
                    for mask in range(1 << m):
                        seen = {f[y] for y in range(m) if mask & (1 << y)}
                        n = mask.bit_count()
                        weight = h**n * u**(m-n)
                        if all((j in seen) == allowed(i,j) for j in range(r+1)):
                            row_f += weight
                        if (set(range(1,r+1)) <= seen if i == 0
                                else all(allowed(i,j) for j in seen)):
                            row_w += weight
                    exact_full *= row_f
                    exact_witness *= row_w
                assert (full,witness) == (exact_full,exact_witness)
                checked += 1
    assert checked == 410
    print(f"Checked {checked} exact fixed-map probability cases.")


if __name__ == "__main__":
    overlap_audit()
    probability_audit()
