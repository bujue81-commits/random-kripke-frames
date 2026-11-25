"""Exact finite regression for two peripheral vertices with optional loops."""
from itertools import product


def allowed(i,j,ea,eb):
    return i == 0 or j == 0 or (i == j and (not ea if i == 1 else not eb))


def overlap_audit():
    checked = 0
    for m,a in [(3,1),(4,1),(5,2),(6,2),(7,3)]:
        maps = [f for f in product(range(3), repeat=m)
                if [f.count(i) for i in range(3)] == [m-2*a,a,a]]
        for ea,eb in product(range(2), repeat=2):
            Q = (2+ea+eb)*a*a
            masks = []
            for f in maps:
                U = sum(1 << x for x in range(m) if f[x])
                H = sum(1 << (m*x+y) for x in range(m) for y in range(m)
                        if not allowed(f[x],f[y],ea,eb))
                assert H.bit_count() == Q
                masks.append((U,H))
            for U,H in masks:
                for V,J in masks:
                    k = 2*a-(U&V).bit_count()
                    assert (H&J).bit_count() <= Q-a*k
                    checked += 1
    assert checked == 115120
    print(f"Checked {checked} ordered map pairs.")


def probability_audit():
    checked = 0
    for f in [(0,1,2),(0,0,1,2),(0,1,1,2),(0,1,2,2),(0,0,1,1,2,2)]:
        m = len(f)
        a = [f.count(i) for i in range(3)]
        for ea,eb in product(range(2), repeat=2):
            Q = 2*a[1]*a[2]+ea*a[1]**2+eb*a[2]**2
            for h,den in [(1,2),(1,3),(2,3),(1,4),(3,4)]:
                u = den-h
                full = witness = u**Q
                hit = 0
                for i,j in product(range(3), repeat=2):
                    if allowed(i,j,ea,eb):
                        full *= (den**a[j]-u**a[j])**a[i]
                        if i == 0 and j:
                            witness *= (den**a[j]-u**a[j])**a[0]
                            hit += a[0]*a[j]
                witness *= den**(m*m-Q-hit)
                exact_full = exact_witness = 1
                for i in f:
                    row_f = row_w = 0
                    for mask in range(1 << m):
                        seen = {f[y] for y in range(m) if mask & (1 << y)}
                        n = mask.bit_count()
                        weight = h**n*u**(m-n)
                        if all((j in seen) == allowed(i,j,ea,eb) for j in range(3)):
                            row_f += weight
                        if ({1,2} <= seen if i == 0
                                else all(allowed(i,j,ea,eb) for j in seen)):
                            row_w += weight
                    exact_full *= row_f
                    exact_witness *= row_w
                assert (full,witness) == (exact_full,exact_witness)
                checked += 1
    assert checked == 100
    print(f"Checked {checked} exact biased probability cases.")


if __name__ == "__main__":
    overlap_audit()
    probability_audit()
