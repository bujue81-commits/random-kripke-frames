"""Finite audit of Theorems 4 and 5, including exact rational moments.

No asymptotic proof is inferred from these tests. Run with Python 3.10+.
Source graphs have independent ordered edges including loops.
"""
from itertools import product, permutations
from math import comb

N = 4
ALL = (1 << N) - 1
F3 = ((1,1,1,1),(1,0,1,1),(1,0,1,0),(1,1,1,1))
F2 = ((1,1,1,1),(1,1,0,1),(1,1,0,1),(1,0,1,1))
MAPS = tuple(permutations(range(N)))
EXPECTED = tuple(tuple(sum(v << j for j,v in enumerate(row)) for row in F)
                 for F in (F3,F2))

def valid(rows, f, Q):
    for i, row in enumerate(rows):
        hit = 0
        for j in range(N):
            if row & (1 << j):
                hit |= 1 << f[j]
        if hit != Q[f[i]]:
            return False
    return True

def forced(rows, A):
    return sum(1 << i for i in range(N) if not (A & (1 << i)) and not (rows[i] & A))

def scan():
    stats = [[0,0,0] for _ in range(N*N+1)]
    actual = [0,0]
    example = None
    for mask in range(1 << (N*N)):
        rows = [(mask >> (N*i)) & ALL for i in range(N)]
        e = mask.bit_count()
        ex3,ex2 = (any(valid(rows,f,Q) for f in MAPS) for Q in EXPECTED)
        actual[0] += ex3
        actual[1] += ex2
        nec = suff = pairs = 0
        complete2 = False
        for A in range(1,ALL+1):
            if any(A & (1 << i) and row & A for i,row in enumerate(rows)):
                continue
            Z = forced(rows,A)
            if Z and all(row & Z for row in rows):
                z_out = 0
                for i,row in enumerate(rows):
                    if Z & (1 << i):
                        z_out |= row
                M = ALL & ~(A|Z|z_out)
                C = ALL & ~(A|Z|M)
                if M and all(Z & (1 << i) or row & M for i,row in enumerate(rows)):
                    nec += 1
                    if C and all(row & C for row in rows):
                        suff += 1
            # Here A plays the role of the independent V of the second target.
            V, A2 = A, Z
            if not A2:
                continue
            pairs += 1
            if any((V|A2) & (1 << i) and not row & A2 for i,row in enumerate(rows)):
                continue
            Z2 = forced(rows,A2) & ~V
            C2 = ALL & ~(V|A2|Z2)
            if Z2 and C2 and all(row & Z2 and row & C2 for row in rows):
                complete2 = True
        assert not ex3 or nec
        assert not suff or ex3
        assert complete2 == ex2
        if nec and not ex3 and example is None:
            example = mask,rows
        for i,x in enumerate((nec,suff,pairs)):
            stats[e][i] += x
    assert actual == [24,24]
    assert [sum(r[i] for r in stats) for i in range(3)] == [1524,24,125504]
    assert example == (4977,[1,7,3,1])
    return stats

def numerator_formula(p,q):
    # A present bit has integer weight p, an absent bit q-p.
    # The common denominator is q^(N*N). No floating point is used.
    r = q-p
    def hit(l):
        return q**l-r**l
    E = [0,0,0]
    for a in range(1,N):
        for z in range(1,N-a):
            n = N-a-z
            for k in range(1,n+1):
                c = n-k
                Q = a*a+a*z+z*k
                ways = comb(N,a)*comb(N-a,z)*comb(n,k)
                factor = ways*r**Q*hit(a)**n*hit(z)**N*hit(k)**(N-z)
                used = Q+n*a+N*z+(N-z)*k+z*c
                E[0] += factor*hit(z)**c*q**(N*N-used)
                if c:
                    J = sum((-1)**j*comb(z,j)*(r**j*(q**(z-j)-r**(z-j)))**c
                            for j in range(z+1))
                    E[1] += factor*J*hit(c)**(N-z)*q**(N*N-used-(N-z)*c)
    for b in range(1,N):
        for a in range(1,N-b+1):
            E[2] += comb(N,b)*comb(N-b,a)*r**(b*b+a*b)*hit(b)**(N-b-a)*q**(N*N-N*b)
    return E

def overlap_audit():
    cases = [
        ((2,2,1,1),((1,1),(2,1),(2,3))),
        ((1,2,2,1),((1,1),(2,1),(2,3))),
        ((2,2,2),((1,1),(2,1))),
        ((3,2,1),((1,1),(2,1))),
        ((2,3,1),((1,1),(2,1))),
    ]
    count = 0
    for sizes,missing in cases:
        first = tuple(i for i,c in enumerate(sizes) for _ in range(c))
        D = max(sizes[1:])
        n = len(first)
        for second in sorted(set(permutations(first))):
            common = [i for i in range(n) if first[i] and second[i]]
            h = len(common)
            x,y,w = (sum(first[i]==k for i in common) for k in (1,2,3))
            u,v,r = (sum(first[i]==1 and second[i]==k for i in range(n)) for k in (1,2,3))
            F = {(i,j) for i,j in product(range(n),repeat=2) if (first[i],first[j]) in missing}
            F2 = {(i,j) for i,j in product(range(n),repeat=2) if (second[i],second[j]) in missing}
            I = len(F & F2)
            R = sum(i in common and j in common for i,j in F)
            assert R == x*x+y*x+(y*w if len(sizes)==4 else 0)
            lower = x*(D-x)+y*(D-x)+w*(D-y)
            assert D*h-I >= lower
            assert I <= h*h
            assert R-I >= v*v+r*r+u*(v+r)
            keep = {i for i in range(n) if first[i]==second[i]==1}
            added = {i for i in range(n) if second[i]==1 and first[i]!=1}
            d = len(added)
            e = sum(first[i]==2 for i in added)
            cross = set(product(keep,added)) | set(product(added,keep))
            assert len(cross-F) == u*(2*d-e)
            count += 1
    assert count == 570
    return count

if __name__ == "__main__":
    stats = scan()
    for p,q in ((1,10),(3,10),(1,2),(7,10),(9,10),(24,25)):
        exact = [sum(row[i]*p**e*(q-p)**(16-e) for e,row in enumerate(stats))
                 for i in range(3)]
        assert exact == numerator_formula(p,q)
        print(f"theta={p}/{q}: exact expectation numerators {exact}, denominator {q**16}")
    print(f"65536 graphs; {overlap_audit()} overlap checks; all finite tests passed.")
