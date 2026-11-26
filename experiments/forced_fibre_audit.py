"""Finite check of the two forced-fibre witness probability formulas."""
from math import comb


def run():
    cases = examined = 0
    for m in (2,3,4):
        for b in range(1,m):
            counts = [[0]*(m*m+1) for _ in range(2)]
            for mask in range(1 << (m*m)):
                def edge(i,j):
                    return bool(mask & (1 << (i*m+j)))
                if any(edge(i,j) for i in range(b) for j in range(b)):
                    continue
                A = [i for i in range(b,m) if not any(edge(i,j) for j in range(b))]
                k = mask.bit_count()
                if not any(edge(i,j) for i in range(b) for j in A):
                    counts[0][k] += 1
                if (A and not any(edge(i,j) for i in A for j in A)
                        and all(any(edge(i,j) for j in A) for i in range(b))):
                    counts[1][k] += 1
            examined += 1 << (m*m)
            for h,D in ((1,2),(1,3),(2,3),(1,4),(3,4)):
                u = D-h
                for mode in range(2):
                    exact = sum(n*h**k*u**(m*m-k)
                                for k,n in enumerate(counts[mode]))
                    formula = 0
                    for a in range(mode,m-b+1):
                        p = comb(m-b,a)*u**(b*b+a*b)*(D**b-u**b)**(m-b-a)
                        if mode==0:
                            p *= u**(a*b)*D**(m*m-m*b-a*b)
                        else:
                            p *= u**(a*a)*(D**a-u**a)**b*D**(m*m-m*b-a*a-a*b)
                        formula += p
                    assert exact==formula,(m,b,h,D,mode)
                    cases += 1
    assert (examined,cases)==(197648,60)
    print(f"Examined {examined} relations (with fixed B choices); checked {cases} exact biased witness probabilities.")

if __name__=="__main__":
    run()
