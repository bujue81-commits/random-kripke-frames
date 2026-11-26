"""Check numeric data in FourPointCensus.lean independently of Lean.

This is an executable finite regression, not a substitute for compiling Lean
or for the asymptotic probability arguments in the manuscript.
"""
import csv
import re
from itertools import permutations, product
from pathlib import Path
from verify_paper_certificate import matrix, morphism

ROOT = Path(__file__).resolve().parents[1]

def main():
    src = (ROOT / "RandomKripke/FourPointCensus.lean").read_text(encoding="utf8")
    rows = list(csv.DictReader((ROOT / "paper/four_point_classification.csv").open(
        newline="", encoding="utf8")))
    def lean_set(name):
        pattern = rf"def {name} : Finset \(Fin 512\) :=\s*\{{([^}}]+)\}}"
        return set(map(int, re.search(pattern, src).group(1).split(",")))

    minimal = lean_set("manuscriptMinimal4")
    positive = lean_set("manuscriptPositive4")
    assert minimal == {int(r["encoding"], 2) for r in rows if r["minimal_vanishing"] == "1"}
    assert positive == {int(r["encoding"], 2) for r in rows if r["limit_fair"] == "1"}
    certs = [tuple(map(int, groups)) for groups in re.findall(
        r"⟨(\d+), (\d+), (\d+)⟩", src)]
    targets = [matrix(code) for code in ("0", "0001", "1001")]

    def decode(n):
        return [[int(i == 0 or j == 0 or
                    n // 2**(8 - 3*(i-1) - (j-1)) % 2 == 1)
                 for j in range(4)] for i in range(4)]

    def encode(R):
        return sum(R[i][j]*2**(8 - 3*(i-1) - (j-1))
                   for i in range(1,4) for j in range(1,4))

    def recode(R,p):
        return encode([[R[i][j] for j in p] for i in p])

    perms = list(permutations(range(4)))
    marked = [p for p in perms if p[0] == 0]
    frames = [decode(n) for n in range(512)]
    canons = [min(recode(R,p) for p in marked) for R in frames]
    inherited = set()
    reps = set()
    checks = unmarked = 0
    target_maps = [(Q, list(product(range(len(Q)),repeat=4))) for Q in targets]
    for n,R in enumerate(frames):
        assert encode(R) == n
        c = canons[n]
        assert canons[c] == c
        assert any(frames[c] == [[R[i][j] for j in p] for i in p] for p in marked)
        for p in perms:
            if all(R[p[0]]) and all(row[p[0]] for row in R):
                unmarked += 1
                assert canons[recode(R,p)] == c
        found = False
        for Q,maps in target_maps:
            for f in maps:
                checks += 1
                if morphism(R,Q,f):
                    found = True
        if c == n:
            reps.add(n)
            if found:
                inherited.add(n)
            assert int(found) + int(n in minimal) + int(n in positive) == 1
        else:
            assert n not in minimal and n not in positive

    covered = set()
    for n,t,d in certs:
        Q = targets[t]
        k = len(Q)
        f = tuple(d // k**(3-i) % k for i in range(4))
        assert morphism(frames[n],Q,f)
        covered.add(n)
    assert covered == inherited
    assert (len(reps),len(inherited),len(minimal),len(positive),len(certs)) == (104,70,22,12,70)
    assert (checks,unmarked) == (91136,3360)
    print("Lean numeric data: 512 roundtrips; 91,136 map checks; "
          "3,360 central relabellings; all 70 certificates verified.")

if __name__ == "__main__":
    main()
