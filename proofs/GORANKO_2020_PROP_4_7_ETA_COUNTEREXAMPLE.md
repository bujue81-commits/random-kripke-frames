# Counterexample to the eta-preservation step in Goranko (2020), Proposition 4.7

Date: 2026-11-25

## Claim under examination

In the proof of Proposition 4.7 of Valentin Goranko, *The Modal Logic of Almost Sure Frame Validities in the Finite* (AiML 2020, pp. 264–265), the following first-order property is used:
\[
\eta := \forall x\,\exists y\,(Rxy\land\neg Ryy).
\]
The paper states that \(\eta\) is preserved in bounded-morphic images. Since \(\eta\) fails in each frame \(F_n\), the proof concludes that it fails in every \(G\) with \(G\twoheadrightarrow F_n\).

Under the paper's Definition 2.1 of a surjective bounded morphism, this preservation claim is false.

## Explicit finite counterexample

Let \(K_2\) be the two-point frame on \(\{0,1\}\) with
\[
R_{K_2}=\{(0,0),(0,1),(1,0)\}.
\]
This is exactly the frame \(F_1\) from Proposition 4.7.

Let \(G\) be the complete irreflexive directed frame on \(\{0,1,2\}\):
\[
iR_Gj \quad\Longleftrightarrow\quad i\ne j.
\]
Define the surjection
\[
h(0)=h(1)=0,\qquad h(2)=1.
\]

### Forth

If \(iR_Gj\), then \(i\ne j\). Since only the source point 2 maps to target point 1, two distinct source points cannot both map to 1. The only absent target edge is \(1R_{K_2}1\). Hence
\[
iR_Gj\Longrightarrow h(i)R_{K_2}h(j).
\]

### Back

- If \(h(i)=0\), the target successors are 0 and 1. Each of source points 0 and 1 has one successor in the fibre of 0 (the other point) and one successor in the fibre of 1 (point 2).
- If \(h(i)=1\), the only target successor is 0. Source point 2 has successors 0 and 1, both in the fibre of 0.

Thus the back condition holds. Therefore \(h:G\twoheadrightarrow K_2\) is a surjective bounded morphism.

### The property \(\eta\)

Every point of \(G\) has a distinct successor, and no point has a loop. Hence
\[
G\models\eta.
\]
In \(K_2\), point 1 has only successor 0, and \(0R_{K_2}0\). Thus
\[
K_2\not\models\eta.
\]
So \(\eta\) is not preserved under surjective bounded-morphic images.

### Diameter-two restriction

Both frames have a directed path of exactly two edges between every ordered pair:
- in \(G\), use a third point when the endpoints differ, and any other point when they coincide;
- in \(K_2\), use the central point 0 as the intermediate point.

Thus the counterexample lies inside the diameter-two class \(\mathcal F^{d2}\) used in Goranko's Section 3.1.

## General blow-up for the whole family \(F_n\)

The same phenomenon is not restricted to \(n=1\).

For any \(n\geq1\), replace every vertex \(x\) of \(F_n\) by three copies \((x,0),(x,1),(x,2)\). Let \(\pi\) map each copy to its original vertex, and define
\[
uR'v \quad\Longleftrightarrow\quad u\ne v\ \land\ \pi(u)R_n\pi(v).
\]

Then:

1. **Forth** is immediate from the definition.
2. **Back:** if \(\pi(u)R_n y\) and \(y\ne\pi(u)\), choose any copy of \(y\); if \(y=\pi(u)\), choose another copy of that vertex. Three copies ensure such a choice.
3. \(\pi\) is surjective, so it is a bounded morphism onto \(F_n\).
4. \(R'\) is irreflexive. Every vertex of \(F_n\) has a distinct successor: 0 has successor 1, and every \(k>0\) has successor 0. Therefore every source point has a non-loop successor, so the blow-up satisfies \(\eta\).
5. \(F_n\) fails \(\eta\) at its terminal vertex \(n\), whose only successor is the looped central point 0.
6. Since \(F_n\) has a central point and two-step reachability, the three-copy blow-up also has two-step reachability: for any source endpoints, choose an intermediate target point and then a copy in its fibre distinct from both endpoints.

Consequently, \(\eta\) fails to be preserved even on the diameter-two class for every \(F_n\), \(n\geq1\).

## Lean and Python verification

- Lean theorem: RandomKripke.goranko_eta_not_preserved_counterexample.
- Lean module: RandomKripke/GorankoEtaCounterexample.lean.
- Python check: audit_eta_preservation_counterexample() in experiments/finite_quotient_audit.py.
- CI run [45571076110](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45571076110), commit ef5fe04e2d3021a9884ad51591614f6291d14951, passed all Python audits, including the dedicated eta counterexample check, and the Lean build. The CI log explicitly built RandomKripke.GorankoEtaCounterexample.

## What this does and does not establish

It **does establish** that the preservation assertion used in the proof of Proposition 4.7 is false under the paper's stated bounded-morphism definition. Therefore the inference
\[
F_n\not\models\eta
\quad\Longrightarrow\quad
G\not\models\eta\text{ for every }G\twoheadrightarrow F_n
\]
is invalid.

It **does not establish** that Proposition 4.7's final conclusion is false. The fact that \(\eta\) does not exclude all preimages does not show that the preimage class has positive asymptotic measure. A different argument may still prove that \(\Pr(G_m\twoheadrightarrow F_n)\to0\). In particular, the \(n=1\) case \(K_2\) is known to be almost-surely valid by Le Bars' result; this counterexample only invalidates the stated shortcut.

## Follow-up research problem

For each fixed \(n\geq2\), determine whether
\[
\Pr(G_m\twoheadrightarrow F_n)\longrightarrow0
\qquad(m\to\infty),
\]
and, if so, obtain a quantitative upper bound. This would either repair the missing part of Proposition 4.7 by a different combinatorial-probabilistic argument or reveal a genuine failure of the claimed infinite family of additional axioms.

Primary source: [Goranko (2020), *The Modal Logic of Almost Sure Frame Validities in the Finite*](https://www.aiml.net/volumes/volume13/Goranko.pdf), Definition 2.1, Section 3.1, Proposition 4.7.
