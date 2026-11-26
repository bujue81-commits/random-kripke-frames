"""Independent finite check for the manuscript's fair-model classification.

Uses all 24 permutations and direct forth/back tests on labelled surjections,
rather than the successor-block partition routine in four_point_census.py.
This checks finite categories, NOT asymptotic probability theorems.
"""
from itertools import permutations, product
from collections import Counter

ZERO3=set("0000 0001 0010 0011 0100 0110 0111 1000 1001 1100 1110".split())
MINIMAL4=set("""
000010100 000010101 000011100 000011101
001001001 001010010 001010011 001011001
001011101 001100010 001100011 001101001
001101011 001110001 001110011 001111001
011010011 011010110 100011101 100110101
100110111 101110011
""".split())
POSITIVE4=set("""
001011011 001111011 011010111 011011011
011011101 011011111 100111111 101011011
101110111 101111101 101111111 111111111
""".split())

def enc(R,p):
    return ''.join(str(R[i][j]) for i in p for j in p)

def run():
    marked={}
    unmarked={}
    checks=0
    perms3=list(permutations(range(1,4)))
    perms4=list(permutations(range(4)))
    surjections={k:[f for f in product(range(k),repeat=4)
                    if len(set(f))==k] for k in (2,3)}
    for bits in product((0,1),repeat=9):
        R=[[1]*4]+[[1]+list(bits[3*i:3*i+3]) for i in range(3)]
        key=min(enc(R,p) for p in perms3)
        full=min(enc(R,p) for p in perms4)
        assert unmarked.setdefault(full,key)==key
        inherited=False
        for k in (2,3):
            for f in surjections[k]:
                checks+=1
                Q=[[0]*k for _ in range(k)]
                for i,j in product(range(4),repeat=2):
                    if R[i][j]:
                        Q[f[i]][f[j]]=1
                if any(Q[f[i]][j] and not any(R[i][w] and f[w]==j for w in range(4))
                       for i,j in product(range(4),range(k))):
                    continue
                p=[i for i in range(k) if i!=f[0]]
                code=enc(Q,p)
                inherited |= code=='0' or code in ZERO3
        degrees=[sum(2-R[i][j]-R[j][i] for j in range(1,4)) for i in range(1,4)]
        degree=min(degrees)>=2 and all(not all(row[i] for row in R)
                                     or R[i].count(0)!=1 for i in range(4))
        core=False
        for flags in product((0,1),repeat=3):
            S=[i for i in range(1,4) if flags[i-1]]
            U=[i for i in range(4) if i not in S]
            if all(R[i][j] for i in U for j in U):
                reps=[i for i in U if all(R[j][i] for j in S)]
                core |= len({tuple(R[i][j] for j in S) for i in reps})==2**len(S)
        cat=('inherited' if inherited else 'degree' if degree else 'core' if core
             else 'forced' if key in {'001011101','001101011'}
             else 'exceptional' if key in {'100111111','011011101','011010111'}
             else 'unresolved')
        assert marked.setdefault(key,cat)==cat
    assert len(unmarked)==len(marked)==104
    assert checks==25600
    assert Counter(marked.values())=={'inherited':70,'degree':20,'core':9,
                                      'forced':2,'exceptional':3}
    assert {s for s,t in marked.items() if t in ('degree','forced')}==MINIMAL4
    assert {s for s,t in marked.items() if t in ('core','exceptional')}==POSITIVE4
    print("104 marked/unmarked classes; 25600 direct surjection checks; manuscript lists verified.")

if __name__=='__main__':
    run()
