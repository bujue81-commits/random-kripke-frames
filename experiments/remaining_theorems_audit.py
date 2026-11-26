"""Finite regression for the remaining internal proof audits.
Checks only finite identities and semantics, not asymptotic theorems.
"""
from itertools import product, permutations
from math import comb
from pathlib import Path
import csv

def target(code):
    return [[1 if i==0 or j==0 else int(code[3*(i-1)+j-1])
             for j in range(4)] for i in range(4)]

def images(rows,f,k):
    hits=[]
    for row in rows:
        h=0
        for j,v in enumerate(f):
            if row & (1<<j):
                h |= 1<<v
        hits.append(h)
    return hits

def direct(rows,Q):
    n,k=len(rows),len(Q)
    q=[sum(v<<j for j,v in enumerate(row)) for row in Q]
    maps=permutations(range(n)) if k==n else product(range(k),repeat=n)
    for f in maps:
        if len(set(f))==k and all(h==q[f[i]] for i,h in enumerate(images(rows,f,k))):
            return True
    return False

def forced_negative():
    stats=[[0,0] for _ in range(17)]
    qs=[target(c) for c in ('001011101','001101011')]
    success=[0,0]
    for mask in range(65536):
        rows=[(mask>>(4*i))&15 for i in range(4)]
        found=[0,0]
        for B in range(1,16):
            if any(B&(1<<i) and row&B for i,row in enumerate(rows)):
                continue
            A=sum(1<<i for i,row in enumerate(rows) if not B&(1<<i) and not row&B)
            found[0]+=all(not B&(1<<i) or not row&A for i,row in enumerate(rows))
            found[1]+=bool(A and all(not A&(1<<i) or not row&A for i,row in enumerate(rows))
                           and all(not B&(1<<i) or row&A for i,row in enumerate(rows)))
        for k,Q in enumerate(qs):
            ex=direct(rows,Q)
            assert not ex or found[k]
            success[k]+=ex
            stats[mask.bit_count()][k]+=found[k]
    assert success==[24,24]
    assert [sum(row[k] for row in stats) for k in range(2)]==[71977,15830]
    for p,q in ((1,10),(3,10),(1,2),(7,10),(9,10),(24,25)):
        r=q-p
        formula=[0,0]
        def hit(k): return q**k-r**k
        for b in range(1,5):
            for a in range(5-b):
                base=comb(4,b)*comb(4-b,a)*r**(b*b+a*b)*hit(b)**(4-b-a)
                formula[0]+=base*r**(a*b)*q**(16-4*b-a*b)
                if a:
                    formula[1]+=base*r**(a*a)*hit(a)**b*q**(16-4*b-a*a-a*b)
        assert formula==[sum(row[k]*p**e*r**(16-e) for e,row in enumerate(stats)) for k in range(2)]
    print('Forced negative: 65536 sources, 12 exact rational moment equalities.')

def core():
    path=Path(__file__).resolve().parents[1]/'paper/four_point_classification.csv'
    covered=[];labelled=signature_tests=0
    for row in csv.DictReader(path.open()):
        Q=target(row['encoding'])
        ok=False
        for mask in range(1,16):
            U=[i for i in range(4) if mask&(1<<i)]
            S=[i for i in range(4) if i not in U]
            if not all(Q[i][j] for i in U for j in U): continue
            patterns=list(product((0,1),repeat=len(S)))
            witnesses=[next((u for u in U if all(Q[u][s]==bit and Q[s][u] for s,bit in zip(S,J))),None) for J in patterns]
            if None in witnesses: continue
            ok=True
            for J,u in zip(patterns,witnesses):
                for I in patterns:
                    assert all(Q[u][s]==j and (not i or Q[s][u]) for s,i,j in zip(S,I,J))
                    signature_tests+=1
        if ok:
            assert row['limit_fair']=='1'
            covered.append(row['encoding']);labelled+=int(row['orbit_size'])
    assert len(covered)==9 and labelled==43 and signature_tests==33
    print('Core signatures:',covered)

def modal():
    frames=nonuniversal=pairs=valuations=0
    for n in range(1,4):
        full=(1<<n)-1
        for mask in range(1<<(n*n)):
            rows=[(mask>>(n*i))&full for i in range(n)]
            def dia(X): return sum(1<<i for i,row in enumerate(rows) if row&X)
            def box(X): return full^dia(full^X)
            if dia(dia(1))!=full or any(dia(dia(1<<i))!=full for i in range(n)):
                nonuniversal+=1;continue
            frames+=1
            for k in range(1,n+1):
                for bits in product((0,1),repeat=(k-1)**2):
                    Q=[[1 if i==0 or j==0 else bits[(i-1)*(k-1)+j-1] for j in range(k)] for i in range(k)]
                    found=False
                    for P in product(range(full+1),repeat=k):
                        delta=full;union=0
                        for i in range(k):
                            delta &= dia(dia(P[i]));union|=P[i]
                            for j in range(i): delta &= full^(P[i]&P[j])
                        delta &= union
                        for i in range(k):
                            for j in range(k):
                                delta &= (full^P[i]) | (dia(P[j]) if Q[i][j] else box(full^P[j]))
                        found |= bool(box(box(delta)))
                        valuations+=1
                    assert found==direct(rows,Q)
                    pairs+=1
    assert (frames,nonuniversal,pairs,valuations)==(77,453,1397,608054)
    print('Modal truth-set audit: 1397 source/target pairs, 608054 valuations.')

def partitions(n,f=(0,),top=0):
    if len(f)==n:
        yield f
    else:
        for x in range(top+2):
            yield from partitions(n,f+(x,),max(x,top))

def cycles():
    totals=[];valids=[]
    for r in range(2,8):
        n=r+1
        rows=[(1<<n)-1]+[1|(1<<(1+i%r)) for i in range(1,n)]
        count=valid=0;types=set()
        for f in partitions(n):
            count+=1;k=max(f)+1
            q={}
            ok=True
            for i,h in enumerate(images(rows,f,k)):
                if f[i] in q and q[f[i]]!=h: ok=False;break
                q[f[i]]=h
            if not ok:continue
            valid+=1
            if k==1: types.add('E1')
            elif k==2 and q[1]==1:types.add('K2')
            else:
                d=k-1
                assert r%d==0 and all(f[i]!=0 for i in range(1,n))
                orbit=[];u=1
                while u not in orbit:
                    orbit.append(u);s=q[u]&~1
                    assert s and s&(s-1)==0
                    u=s.bit_length()-1
                assert u==1 and len(orbit)==d
                types.add('C'+str(d))
        expected={'E1'}|{'C'+str(d) for d in range(1,r+1) if r%d==0}
        if r%2==0:expected.add('K2')
        assert types==expected
        totals.append(count);valids.append(valid)
    assert totals==[5,15,52,203,877,4140] and valids==[5,3,6,3,7,3]
    print('Cycle quotient audit: 5292 partitions.')

if __name__=='__main__':
    core()
    forced_negative()
    modal()
    cycles()
