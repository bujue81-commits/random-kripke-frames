from itertools import permutations, product

ZERO3=set("0000 0001 0010 0011 0100 0110 0111 1000 1001 1100 1110".split())

def partitions(n):
    def go(f,k):
        if len(f)==n:
            yield f
        else:
            for j in range(k+1):
                yield from go(f+[j],max(k,j+1))
    yield from go([0],1)

def quotient(R,f):
    q=[None]*(max(f)+1)
    for i,row in enumerate(R):
        s=frozenset(f[j] for j,x in enumerate(row) if x)
        if q[f[i]] is not None and q[f[i]]!=s:
            return None
        q[f[i]]=s
    return q

def signature(R):
    n=len(R)
    for flags in product((0,1),repeat=n-1):
        S=[j for j in range(1,n) if flags[j-1]]
        U=[j for j in range(n) if j not in S]
        if all(R[i][j] for i in range(n) for j in U):
            if len({tuple(R[i][j] for j in S) for i in U})==2**len(S):
                return True
    return False

def forbidden_degree(R):
    r=len(R)-1
    A=[[1-R[i+1][j+1] for j in range(r)] for i in range(r)]
    return (all(sum(A[i][j] for i in range(r))>=1 for j in range(r))
            and all(sum(A[i])+sum(A[j][i] for j in range(r))>=2
                    for i in range(r)))

def no_singleton_miss_degree(R):
    r=len(R)-1
    A=[[1-R[i+1][j+1] for j in range(r)] for i in range(r)]
    return (all(sum(A[i])+sum(A[j][i] for j in range(r))>=2 for i in range(r))
            and all(not all(row[i] for row in R) or R[i].count(0)!=1
                    for i in range(len(R))))

def complete_core_signature(R):
    n=len(R)
    for flags in product((0,1),repeat=n-1):
        S=[j for j in range(1,n) if flags[j-1]]
        U=[j for j in range(n) if j not in S]
        if not all(R[i][j] for i in U for j in U):
            continue
        representatives=[u for u in U if all(R[j][u] for j in S)]
        if len({tuple(R[u][j] for j in S) for u in representatives})==2**len(S):
            return True
    return False

def census():
    classes={}
    for bits in product((0,1),repeat=9):
        R=[[1]*4]+[[1]+list(bits[3*i:3*i+3]) for i in range(3)]
        key=min(''.join(str(R[i][j]) for i in p for j in p)
                for p in permutations(range(1,4)))
        bad=False
        for f in partitions(4):
            k=max(f)+1
            if k not in (2,3):
                continue
            q=quotient(R,f)
            if q is None:
                continue
            s=''.join(str(int(j in q[i])) for i in range(1,k) for j in range(1,k))
            bad |= (k==2 and s=='0') or (k==3 and s in ZERO3)
        status=('excluded' if bad else 'cycle' if key=='001100010'
                else 'positive' if signature(R) else 'degree' if forbidden_degree(R)
                else 'no_singleton' if no_singleton_miss_degree(R)
                else 'complete_core' if complete_core_signature(R)
                else 'forced_fibre' if key in {'001011101','001101011'}
                else 'dominating_reserve' if key=='100111111'
                else 'unresolved')
        if key not in classes:
            classes[key]=[0,status]
        assert classes[key][1]==status
        classes[key][0]+=1
    for status,want in [('excluded',(70,339)),('cycle',(1,2)),
                        ('positive',(5,19)),('degree',(11,62)),('no_singleton',(8,39)),('complete_core',(4,24)),('forced_fibre',(2,12)),('dominating_reserve',(1,3)),('unresolved',(2,12))]:
        found=[(s,n) for s,(n,t) in classes.items() if t==status]
        assert (len(found),sum(n for _,n in found))==want
        print(status,want,sorted(s for s,_ in found))

def cycles():
    count=0
    for r in range(2,9):
        R=[[int(i==0 or j==0 or j==i%r+1) for j in range(r+1)] for i in range(r+1)]
        seen=set()
        for f in partitions(r+1):
            count+=1
            q=quotient(R,f)
            if q is None:
                continue
            k=len(q)
            if k==1:
                seen.add('E1')
            elif k==2:
                seen.add('K2' if q[1]=={0} else 'C1')
            else:
                assert all(len(row)==2 and 0 in row for row in q[1:])
                s={i:next(iter(q[i]-{0})) for i in range(1,k)}
                v,orbit=1,set()
                while v not in orbit:
                    orbit.add(v)
                    v=s[v]
                assert v==1 and len(orbit)==k-1
                seen.add('C'+str(k-1))
        expected={'E1'}|{'C'+str(d) for d in range(1,r+1) if r%d==0}
        if r%2==0:
            expected.add('K2')
        assert seen==expected
    assert count==26439
    print(count,'cycle partitions checked')

if __name__=='__main__':
    census()
    cycles()
