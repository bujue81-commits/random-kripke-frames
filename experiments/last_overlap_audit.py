"""Finite audit of the combinatorial inequalities in the final second moment.
This does not verify the asymptotic estimates.
"""
from itertools import combinations

def forbidden(x,y):
    return (x==1 and y==1) or (x==2 and y in (1,3))

def run():
    checked=0
    for m,a,z,k in ((6,1,2,1),(7,2,2,1),(8,2,2,2),(9,2,3,2),(10,3,2,3)):
        S=set(range(a+z+k))
        A=set(range(a))
        Z=set(range(a,a+z))
        M=S-A-Z
        V=set(range(m))
        H={(i,j) for i in A for j in A}|{(i,j) for i in Z for j in A|M}
        D=max(a,z,k)
        for ap in combinations(V,a):
            Ap=set(ap)
            for zp in combinations(V-Ap,z):
                Zp=set(zp)
                for mp in combinations(V-Ap-Zp,k):
                    Mp=set(mp)
                    Sp=Ap|Zp|Mp
                    Hp={(i,j) for i in Ap for j in Ap}|{(i,j) for i in Zp for j in Ap|Mp}
                    I=len(H&Hp)
                    x,y,w=(len(T&Sp) for T in (A,Z,M))
                    u,v,r=(len(A&T) for T in (Ap,Zp,Mp))
                    h=x+y+w
                    R=x*x+y*x+y*w
                    delta=D*h-I
                    assert I<=R<=D*h
                    assert delta>=x*(D-x)+y*(D-x)+w*(D-y)
                    assert R-I>=v*v+r*r+u*(v+r)
                    checked+=1
    assert checked==36090
    print(f"Checked {checked} labelled overlap configurations.")

if __name__=="__main__":
    run()
