"""Integer arithmetic certificate of signs at the rational bracketing points.

All bounds are fixed-point integers with scale S. The logarithm series
remainder is bounded analytically. No floating-point computation is used
in the assertions. This checks signs, not the asymptotic proofs.
"""
S = 10**18
N = 60

def ceil_div(a,b):
    return (a+b-1)//b

def log_rat(p,q):
    assert p>0 and q>0
    negative=p<q
    x,y=abs(p-q),p+q
    lo=sum((2*S*x**(2*k+1))//((2*k+1)*y**(2*k+1))
           for k in range(N))
    n=2*N+1
    tail=ceil_div(2*S*x**n*y*y,n*y**n*(y*y-x*x))
    hi=lo+N+tail
    return (-hi,-lo) if negative else (lo,hi)

def evaluate(p,q):
    l,h=log_rat(q,p)
    u=(2*l*q//(q-p),ceil_div(2*h*q,q-p))
    b=(u[0]//4,ceil_div(u[1],4))
    s=(u[0]*p*p//(q*q),ceil_div(u[1]*p*p,q*q))
    t2=(b[0]*q//p,ceil_div(b[1]*q,p))
    def H(t,s):
        assert 0<s[0]<=s[1]<S
        lt=(log_rat(t[0],S)[0],log_rat(t[1],S)[1])
        ls=(log_rat(s[0],S)[0],log_rat(s[1],S)[1])
        return (3*S+2*lt[0]+ls[0]-t[1]-2*s[1],
                3*S+2*lt[1]+ls[1]-t[0]-2*s[0])
    return H(u,s),H(t2,b)

def enclose(bounds,lower,upper):
    # lower, upper in millionths, exact rational comparisons
    assert lower*S < bounds[0]*10**6
    assert bounds[1]*10**6 < upper*S

if __name__=='__main__':
    D251,E251=evaluate(251,1000)
    D252,E252=evaluate(252,1000)
    enclose(D251,-3005,-3004)
    enclose(D252,3020,3022)
    enclose(E251,1577,1578)
    print("Certified D(.251)<0<D(.252) and E(.251)>0.")
    print("Scaled integer intervals:",D251,D252,E251)
