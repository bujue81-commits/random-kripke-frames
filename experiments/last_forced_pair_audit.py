"""Exact weighted checks for LAST_FOUR_POINT_FORCED_PAIR.md."""
from math import comb

def run():
    examined=cases=0
    for m in (3,4):
        for a in range(1,m-1):
            for z in range(1,m-a):
                n=m-a-z
                A=range(a)
                Z=range(a,a+z)
                O=range(a+z,m)
                V=range(m)
                count=[[0]*(m*m+1) for _ in range(2)]
                for mask in range(1<<(m*m)):
                    def e(i,j):
                        return bool(mask & (1<<(i*m+j)))
                    if any(e(i,j) for i in A for j in A): continue
                    if any(e(i,j) for i in Z for j in A): continue
                    if any(not any(e(i,j) for j in A) for i in O): continue
                    if any(not any(e(i,j) for j in Z) for i in V): continue
                    M=[j for j in O if not any(e(i,j) for i in Z)]
                    C=[j for j in O if j not in M]
                    if not M or any(not any(e(i,j) for j in M) for i in V if i not in Z): continue
                    k=mask.bit_count()
                    count[0][k]+=1
                    if C and all(any(e(i,j) for j in C) for i in V):
                        count[1][k]+=1
                examined+=1<<(m*m)
                for h,D in ((1,2),(1,3),(2,3),(1,4),(3,4)):
                    u=D-h
                    P=u**(a*a+a*z)*(D**a-u**a)**n*(D**z-u**z)**m
                    f0=f1=0
                    for k in range(1,n+1):
                        c=n-k
                        w=comb(n,k)*u**(z*k)*(D**z-u**z)**c*(D**k-u**k)**(m-z)
                        f0+=P*w*D**((m-z)*c)
                        if c:
                            J=sum((-1)**j*comb(z,j)*(u**j*D**(z-j)-u**z)**c for j in range(z+1))
                            f1+=P*comb(n,k)*u**(z*k)*(D**k-u**k)**(m-z)*(D**c-u**c)**(m-z)*J
                    for i,f in enumerate((f0,f1)):
                        exact=sum(x*h**k*u**(m*m-k) for k,x in enumerate(count[i]))
                        assert exact==f,(m,a,z,h,D,i)
                        cases+=1
    assert (examined,cases)==(197120,40)
    print(examined,"relation/configuration pairs;",cases,"weighted probability cases")

if __name__=="__main__":
    run()
