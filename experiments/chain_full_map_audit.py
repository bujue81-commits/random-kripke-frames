"""Exact rational fixed-map probability audit for the chain target."""
from fractions import Fraction


def audit():
    for labels in [(0,1,2),(0,0,1,2),(0,1,1,2),(0,1,2,2),(0,1,2,3)]:
        m,r=len(labels),max(labels)
        a=[labels.count(i) for i in range(r+1)]
        Q=sum(a[1:])**2-sum(a[i]*a[i+1] for i in range(1,r))
        selected=Fraction(1,2**Q)
        for i in range(1,r+1):
            selected *= (1-Fraction(1,2**a[i]))**a[0]
        full=selected*(1-Fraction(1,2**a[0]))**m
        for i in range(1,r):
            full *= (1-Fraction(1,2**a[i+1]))**a[i]
        target=[{j for j in range(r+1) if i==0 or j==0 or j==i+1} for i in labels]
        s=t=0
        for bits in range(1<<(m*m)):
            rows=[{labels[y] for y in range(m) if bits & (1<<(x*m+y))} for x in range(m)]
            s += all((set(range(1,r+1)) <= row) if i==0 else row <= allowed
                     for i,row,allowed in zip(labels,rows,target))
            t += all(row==allowed for row,allowed in zip(rows,target))
        assert Fraction(s,1<<(m*m))==selected
        assert Fraction(t,1<<(m*m))==full
        print(labels,s,t)


if __name__ == "__main__":
    audit()
