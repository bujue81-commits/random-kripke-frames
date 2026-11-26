"""Verify finite certificates in paper/four_point_classification.csv.

The probability limits are mathematical inputs from the manuscript; this
checker verifies the finite orbit, quotient, and proof-coverage assertions.
"""
import csv
from collections import Counter
from itertools import permutations, product
from pathlib import Path

def matrix(code):
    r={1:1,4:2,9:3}[len(code)]
    return [[1]*(r+1)]+[[1]+list(map(int,code[r*i:r*(i+1)])) for i in range(r)]

def canonical(R):
    r=len(R)-1
    return min(''.join(str(R[i][j]) for i in p for j in p)
               for p in permutations(range(1,r+1)))

def morphism(R,Q,f):
    return set(f)==set(range(len(Q))) and all(
        {f[j] for j,e in enumerate(R[i]) if e}
        == {j for j,e in enumerate(Q[f[i]]) if e}
        for i in range(len(R)))

def degree(R):
    r=len(R)-1
    return (all(sum(2-R[i][j]-R[j][i] for j in range(1,r+1))>=2
                for i in range(1,r+1))
            and all(not all(row[i] for row in R) or R[i].count(0)!=1
                    for i in range(r+1)))

def core(R):
    for bits in product((0,1),repeat=3):
        S=[i+1 for i,b in enumerate(bits) if b]
        U=[i for i in range(4) if i not in S]
        if all(R[i][j] for i in U for j in U):
            sig={tuple(R[i][j] for j in S) for i in U
                 if all(R[j][i] for j in S)}
            if len(sig)==2**len(S):
                return True
    return False

def main():
    path=Path(__file__).resolve().parents[1]/'paper/four_point_classification.csv'
    rows=list(csv.DictReader(path.open(newline='',encoding='utf8')))
    orbits=Counter(canonical(matrix(''.join(bits))) for bits in product('01',repeat=9))
    assert len(rows)==len(orbits)==104
    assert len({r['encoding'] for r in rows})==104
    totals=Counter()
    for row in rows:
        code=row['encoding']
        R=matrix(code)
        assert canonical(R)==code
        assert int(row['orbit_size'])==orbits[code]
        proof=row['proof_method']
        limit=int(row['limit_fair'])
        minimal=int(row['minimal_vanishing'])
        assert limit in (0,1) and minimal in (0,1)
        totals[proof]+=1
        lower_images=[]
        for qcode in ('0','0001','1001'):
            Q=matrix(qcode)
            for f in product(range(len(Q)),repeat=4):
                if morphism(R,Q,f):
                    lower_images.append((qcode,f))
        if proof=='smaller_minimal_quotient':
            n,qcode=row['smaller_target_vertices_and_encoding'].split(':')
            Q=matrix(qcode)
            assert len(Q)==int(n) and qcode in ('0','0001','1001')
            f=tuple(map(int,row['quotient_map_f0_f1_f2_f3']))
            assert len(f)==4 and morphism(R,Q,f)
            assert (qcode,f) in lower_images
            assert (limit,minimal)==(0,0)
        else:
            assert not lower_images
            assert not row['smaller_target_vertices_and_encoding']
            assert not row['quotient_map_f0_f1_f2_f3']
            if proof=='forbidden_degree':
                assert degree(R) and (limit,minimal)==(0,1)
            elif proof=='forced_fibre':
                assert code in ('001011101','001101011') and (limit,minimal)==(0,1)
            elif proof=='complete_core':
                assert core(R) and (limit,minimal)==(1,0)
            elif proof=='exceptional_positive':
                assert code in ('100111111','011011101','011010111') and (limit,minimal)==(1,0)
            else:
                raise AssertionError(proof)
    assert totals=={'smaller_minimal_quotient':70,'forbidden_degree':20,
                    'forced_fibre':2,'complete_core':9,'exceptional_positive':3}
    assert sum(int(r['orbit_size']) for r in rows)==512
    assert sum(int(r['minimal_vanishing']) for r in rows)==22
    assert sum(int(r['limit_fair']) for r in rows)==12
    assert sum(int(r['orbit_size'])*int(r['limit_fair']) for r in rows)==58
    print('104 canonical rows and 70 explicit minimal quotient maps verified.')
if __name__=='__main__':
    main()
