"""Finite checks of the forbidden-degree criterion (Theorem 2).

This script checks combinatorial premises and identities, not asymptotic
probability claims. No third-party dependencies.
"""
from itertools import permutations, product
from pathlib import Path
import csv

def matrices(r):
    for bits in product((0,1), repeat=r*r):
        yield [bits[i*r:(i+1)*r] for i in range(r)]

def data(A):
    r = len(A)
    row = [sum(x) for x in A]
    col = [sum(A[i][j] for i in range(r)) for j in range(r)]
    g = [row[i]+col[i] for i in range(r)]
    H1 = all(col[i] or row[i]!=1 for i in range(r))
    H2 = min(g)>=2
    return row,col,g,sum(row),H1,H2

def quadratic(A,a):
    return sum(A[i][j]*a[i]*a[j] for i in range(len(A)) for j in range(len(A)))

def critical_audit():
    result=[]
    for r in range(1,5):
        ps=list(permutations(range(r)))
        counts=[0]*6
        for A in matrices(r):
            row,col,g,q,H1,H2=data(A)
            counts[0]+=1
            counts[1]+=H1 and H2
            if not H2 or q!=r:
                continue
            counts[2]+=1
            counts[3]+=H1
            counts[4]+=any(x!=1 for x in row+col)
            assert all(x==2 for x in g)
            p=next((p for p in ps if all(A[i][i]==(p[i]==i) and
                    all(i==j or A[i][j]+A[j][i]==int(p[i]==j)+int(p[j]==i)
                        for j in range(r)) for i in range(r))),None)
            assert p is not None
            for a in product((1,2,3),repeat=r):
                assert quadratic(A,a)==sum(a[i]*a[p[i]] for i in range(r))
                counts[5]+=1
        result.append(counts)
    assert result==[
        [2,1,1,1,0,3],
        [16,7,2,2,0,18],
        [512,331,12,12,6,324],
        [65536,53457,90,90,66,7290],
    ]
    return result

def geometry_audit():
    cases=rectangles=0
    for r in range(1,4):
        for A in matrices(r):
            _,_,g,q,_,H2=data(A)
            if not H2:
                continue
            for a in range(1,5):
                for k in product(range(a+1),repeat=r):
                    lost=0
                    for i in range(r):
                        for j in range(r):
                            if A[i][j]:
                                loss=a*a-(a-k[i])*(a-k[j])
                                assert 2*loss>=a*(k[i]+k[j])
                                lost+=loss
                                rectangles+=1
                    assert lost>=a*sum(k)
                    assert quadratic(A,[1+x for x in k])>=q+2*sum(k)
                    cases+=1
    assert (cases,rectangles)==(74536,391526)
    return cases,rectangles

def census_audit():
    root=Path(__file__).resolve().parents[1]
    rows=list(csv.DictReader((root/'paper/four_point_classification.csv').open()))
    all_count=labelled=minimal=0
    critical=[]
    for row in rows:
        s=row['encoding']
        A=[[1-int(s[3*i+j]) for j in range(3)] for i in range(3)]
        _,_,_,q,H1,H2=data(A)
        if not (H1 and H2):
            continue
        assert row['limit_fair']=='0'
        all_count+=1
        labelled+=int(row['orbit_size'])
        if row['minimal_vanishing']=='1':
            minimal+=1
            assert 'degree' in row['proof_method']
            if q==3:
                critical.append(s)
    assert (all_count,labelled,minimal)==(69,331,20)
    assert critical==['100110111','101110011']
    return all_count,labelled,minimal,critical

if __name__=='__main__':
    print('Critical quadratic forms:',critical_audit())
    print('Geometry:',geometry_audit())
    print('Four-point census:',census_audit())
