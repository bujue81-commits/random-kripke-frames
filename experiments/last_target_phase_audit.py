"""Numerical checks of phase formulas, not probability proofs.

The analytic criterion is in proofs/LAST_FOUR_POINT_PHASE_CLASSIFICATION.md.
"""
from math import log, sqrt

RHO_STAR = (3*sqrt(3)-5)/4

def H(t,s):
    if s>=1:
        return 2+2*log(t)-t-s
    return 3+2*log(t)+log(s)-t-2*s

def finite_phase_grid(rho,v):
    # A deliberately bounded numerical check, not an exact maximizer.
    return max((H(v*rho**i,v*rho**j),i,j)
               for i in range(-35,36) for j in range(-35,36))

def main():
    checks=0
    for rho in (1/3,.35,.4,.5,.6,.7,.8,.9,.95,.99):
        for i in range(1001):
            t=(1/rho)**(i/1000)
            assert H(t,rho*t)>0
            checks+=1
    for rho in (.0491,.05,.06,.07,.08,.09,.1,.12,.15,.18,.2):
        assert rho>RHO_STAR
        assert finite_phase_grid(rho,1)[0]<=1e-10
        checks+=1
    assert abs(finite_phase_grid(.1,1)[0])<1e-10
    assert abs(finite_phase_grid(.1,2.5)[0]-log(27*.1/(1+.2)**3))<1e-10
    assert checks==10021
    print(f"{checks} numerical phase checks passed; not an asymptotic proof.")

if __name__=="__main__":
    main()
