# Related work and novelty audit

## Rainer Franz Schamm (2002): direct precursor

Rainer Franz Schamm, *Zero-One Laws and Almost Sure Validities on Finite Structures*, M.Sc. short dissertation, Rand Afrikaans University, January 2002; supervisor: Valentin Goranko.

The direct overlap is substantial:

1. Section 3.3.5 introduces \(F\)-partitions and gives the general first-moment formula for a fixed target frame and fixed fibre sizes.
2. Section 3.3.6 explicitly says that all 3-vertex frames with a central point were investigated experimentally. There are 16 such frames, corresponding to the 16 possible binary relations on the two non-central points.
3. Figure 4.1 classifies the 16 cases into “No growth”, “Very slow growth”, “Slow growth”, “Medium growth”, “Fast growth”, and “Very fast growth” categories.
4. The appendix gives an analytic first-moment proof for K4, the frame obtained from K3 by adding the arrow \(y_1\to y_2\).

This means the 16-frame candidate search and the use of the first-moment partition expectation are not new contributions of this repository. The current targets F0001 and F1001 are two members of that 16-frame family.

## Exact relation to the old enumeration

Schamm's Java code iterates the four non-central ordered pairs in this order:
\[
(y_1,y_1),\ (y_1,y_2),\ (y_2,y_1),\ (y_2,y_2).
\]
It uses successive binary bits to decide whether each arrow is present. Under that code convention:

- F0001 has bit mask 8 (only \(y_2\to y_2\));
- F1001 has bit mask 9 (both self-loops, no cross-arrows).

The text extraction of Figure 4.1 gives the 4×4 category labels but not the diagrams' full visual ordering. The appendix code iterates masks k=0,...,15 with the four bits in the order above, but the extracted figure does not expose the diagrams' precise arrangement. Under the natural row-by-row arrangement of the two adjacency rows, F0001 appears in a “No growth” cell and F1001 appears in a “Slow growth” cell; treat that cell assignment as provisional until the original figure is inspected visually.

The included Java program in the appendix sets n=50 and evaluates the partition sum for each of the 16 frames; the genetic-algorithm programs mentioned in the text are not included. Thus the labels are explicitly experimental/heuristic, not proved asymptotic classifications. Our exact first-moment sum for F1001 decreases over the tested range, and the current hand-proof draft claims that it tends to zero. If the old “Slow growth” label was intended to mean non-vanishing growth, the new proof would refine or correct that heuristic. The figure's encoding and the original numerical computation must be reconciled before claiming a correction.

## What remains potentially new

The plausible contribution is not discovering F0001/F1001 as candidates. It is:

- giving rigorous asymptotic first-moment proofs for these specific frames, rather than relying on the 2002 numerical/heuristic classification;
- checking whether the F1001 proof establishes a limit that the old figure classified differently;
- formalizing the finite quotient structure and exact small-n counts in Lean;
- providing reproducible, numerically stable calculations that can audit the earlier experiment.

Schamm's appendix proves K4 analytically, but the thesis does not provide analytic proofs for the two matrices studied here. A later-literature search is still required before making a priority or novelty claim.

## Later synthesis

Goranko's 2020 paper explicitly cites Schamm's empirical study and says that identifying which central-point frames have almost-surely valid characteristic formulas may require difficult combinatorial-probabilistic calculations. It then defines the minimality criterion used in this project: no proper bounded-morphic image F' may itself be a central-point frame with \(\chi_{F'}\in ML^{as}\).

See [THEORY_BACKGROUND.md](THEORY_BACKGROUND.md) for the theorem/page guide.


## Reproducible numerical cross-check

The new log-stable script `experiments/expected_partition_sum.py` evaluates the exact first-moment sum from the general formula in Schamm's Section 3.3.6. It counts all labelled surjective maps, not merely source frames that admit at least one map. Representative values are:

| n | E[X(F0001)] | E[X(F1001)] |
|---:|---:|---:|
| 3 | 0.01171875 | 0.01171875 |
| 50 | 0.000650884 | 0.127916528 |
| 100 | 0.000014376 | 0.092169675 |
| 200 | 0.000000119 | 0.069560675 |
| 500 | 6.30e-11 | 0.050743682 |
| 1,000 | 4.50e-14 | 0.040466991 |

This is a numerical audit only. In particular, F1001's expectation decreases much more slowly than F0001's over this range. It does not establish a limit. It does make the provisional “Slow growth” label for mask 9 in Figure 4.1 worth checking against the original figure ordering and the old Java computation. The asymptotic proof draft, if correct, would show that this expectation nevertheless tends to zero.


## Sliusarev (2025/2026): broader random-frame framework

Vladislav V. Sliusarev, *Modal Logic of Random Kripke Frames*, PhD thesis summary, National Research University Moscow Institute of Physics and Technology, Moscow, 2025; thesis defence at HSE University, 15 January 2026. [English summary](https://www.hse.ru/data/2025/10/24/1949835949/2resume_en.pdf).

This is important recent adjacent work. It defines the uniformly distributed random L-frame for an arbitrary modal logic L and develops a transfer theorem relating all L-frames to connected L-frames (Theorem 83). Its stated main applications are KD5, KD45, K5B, S5, Grz.3, GL.3, SL, and certain Horn closures; the unrestricted K case and the specific three-point targets F0001/F1001 are not listed among the thesis's main results. It is therefore a required source for the broader novelty review, but the summary does not show that it resolves the present target-frame problem.

The thesis also lists these related publications by Sliusarev:
- “Almost sure modal logic of the Kripke frames with a functional relation,” *Proceedings of Moscow Institute of Physics and Technology* 16(3(63)) (2024), 57–71.
- “Modal Logics of Almost Sure Validities and Zero-One Laws in Horn Classes,” *Doklady Mathematics* 110(2) (2024), 442–449.
- “Modal logics of almost-sure validities in some classes of Euclidean and transitive frames,” *Combinatorics and Number Theory* 14(1) (2025), 49–64.

The first two papers and the third paper should be checked for any lemmas that transfer to the unrestricted random relation model. Do not claim a complete literature survey on the basis of the thesis summary alone.


## Extended numerical audit through n=30,000

The optional vectorized script experiments/large_n_audit_numpy.py reproduces the exact first-moment sum in log space and cross-checks n=3,4 against exhaustive labelled-map enumeration.

| n | E[X(F1001)] |
|---:|---:|
| 1,000 | 0.040466991 |
| 2,000 | 0.032340597 |
| 5,000 | 0.026380675 |
| 10,000 | 0.021771903 |
| 20,000 | 0.017459042 |
| 30,000 | 0.016048503 |

The script requires NumPy and SciPy and is intentionally not part of the standard CI workflow. The values are finite numerical evidence only. The first-moment proof, not this table, is what would establish convergence to zero.


## Sliusarev thesis: the precise connection to the unrestricted K model

The official English thesis summary (2025 manuscript; defended 15 January 2026) contains two general results relevant to this project.

1. **Theorem 68 / Corollary 69 (summary pp. 8–9):** for any nonempty class of frames, its almost-sure logic is a normal modal logic extending the ordinary logic of that class. This applies to the class of all frames, so it gives the normality of \(K^{as}\), but it does not axiomatize \(K^{as}\).
2. **Theorem 83 (summary p. 9):** under a nonemptiness assumption for connected \(L\)-frames and the additional condition
   \[
   \varphi\notin\operatorname{Log}^{as}(\operatorname{ConFr}L)
   \Longrightarrow
   \limsup_n\Pr(\widehat F_n(\operatorname{ConFr}L)\models\varphi)<1,
   \]
   one obtains
   \[
   L^{as}\subseteq\operatorname{Log}^{as}(\operatorname{ConFr}L).
   \]
   The condition is stronger than merely saying that the probability does not converge to 1. For \(L=K\), connected frames exist at every size, but the displayed limsup condition has not been established here for all modal formulas. It must not be silently assumed.

In Section 3.2 (summary pp. 13–14), Sliusarev recalls the extension properties \(Ext_m\) of the unrestricted random frame and states that they hold asymptotically almost surely. These imply the frame properties characterizing \(\mathbf{ML}^r\), hence \(\mathbf{ML}^r\subseteq K^{as}\), as already established in Goranko's programme. The thesis generalizes the corresponding axioms to Horn closures. This does not determine the additional axioms in \(K^{as}\).

The thesis's main finite axiomatizations concern KD5, KD45, K5B, S5, Grz.3, GL.3 and SL, not the unrestricted K case. Its conclusion explicitly lists further classification work for extensions of K5 and additional Horn closures as future directions. Thus it is an important methodological source, but it does not appear to settle the F0001/F1001 image-probability questions.

Primary source: [Sliusarev, Modal Logic of Random Kripke Frames, English thesis summary](https://www.hse.ru/data/2025/10/24/1949835949/2resume_en.pdf), especially Theorems 68 and 83 and Section 3.2.


## Potential preservation gap in Goranko (2020), Proposition 4.7

A separate issue was found in the proof of Proposition 4.7, distinct from the F0001/F1001 estimates. The proof says that
\[
\eta:=\forall x\exists y\,(Rxy\land\neg Ryy)
\]
is preserved in bounded-morphic images, and uses this to infer that because \(\eta\) fails in \(F_n\), it must fail in every \(G\) with \(G\twoheadrightarrow F_n\).

Under Definition 2.1 of the same paper, this preservation assertion has a finite counterexample already for \(F_1\). The frame \(F_1\) in Proposition 4.7 is the two-point frame \(K_2\) with
\[
W=\{0,1\},\quad R=\{(0,0),(0,1),(1,0)\}.
\]
Let \(G\) be the three-point complete irreflexive directed frame, and define \(h(0)=h(1)=0\), \(h(2)=1\). Then:
- \(G\models\eta\), since every point has a distinct successor and no point has a loop;
- \(G\twoheadrightarrow K_2\): forth holds because all target edges except \(1\to1\) are present, and no two distinct source points both map to 1; back holds because each point over 0 has a successor over 0 and over 1, while the point over 1 has a successor over 0;
- \(K_2\not\models\eta\), since point 1 has only successor 0, and 0 has a loop.

Both frames also have two-step reachability between every ordered pair. Thus the counterexample persists inside the diameter-two class used in Section 3.1.

This is formalized in Lean in RandomKripke/GorankoEtaCounterexample.lean as goranko_eta_not_preserved_counterexample, and independently checked by the Python audit. CI run [45571076110](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45571076110) explicitly built the Lean module successfully. The dedicated Python cross-check also passed in CI run [45571611756](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45571611756).

There is also a general blow-up construction for every \(F_n\), \(n\geq1\). Replace each target vertex by three copies and define \(uR'v\) iff \(u\ne v\) and \(\pi(u)R_n\pi(v)\), where \(\pi\) is the projection to \(F_n\). The projection is a surjective bounded morphism: forth is immediate; for back, if the target successor is different, choose any point in its fibre, and if it is the same vertex, choose another copy in that fibre. Every source point has a non-loop successor because every vertex of \(F_n\) has a distinct successor (0 has successor 1, and each k>0 has successor 0). Hence the blow-up satisfies \(\eta\), while \(F_n\) fails \(\eta\) at its terminal point n. Since \(F_n\) has a central point and two-step reachability, the blow-up can also be chosen to have two-step reachability by using three copies per vertex.

**Interpretation:** this refutes the stated preservation claim and therefore leaves a gap in the proof of Proposition 4.7's assertion that every \(\chi_{F_n}\) is almost-surely valid. It does not, by itself, refute the proposition's final conclusion: those characteristic formulas might be almost-surely valid for other reasons. In particular, the \(n=1\) case \(K_2\) is known to be almost-surely valid by Le Bars' result, so the counterexample only invalidates the claimed shortcut, not that known conclusion. Any claim about the \(n\geq2\) cases requires a separate proof or further literature audit.

Primary source locations: Goranko (2020), Definition 2.1 (bounded morphisms), pp. 254–255; Proposition 4.7 and its proof, pp. 264–265.


A standalone write-up with the forth/back verification and the general three-copy blow-up construction is available in proofs/GORANKO_2020_PROP_4_7_ETA_COUNTEREXAMPLE.md.


## Alternative first-moment proof for the chain family F_r, r >= 2

A separate hand proof has now been added in proofs/GORANKO_CHAIN_FRAMES_FIRST_MOMENT.md. For every fixed r >= 2, it proves
\[
\Pr(G_m\twoheadrightarrow F_r)
\leq \exp(-\Omega_r((\ln m)^2)).
\]
The proof counts a weaker necessary event: all forbidden noncentral-to-noncentral rectangles must be empty, and every row in the central fibre must hit every noncentral fibre. If the total noncentral fibre size S is small, at least one noncentral fibre is smaller than (3/4)log_2(m), and the central-hit probability is at most exp(-m^(1/4)/2). If S is large, the forbidden-edge count is at least 3S^2/4 by splitting the chain fibres into odd and even indices; this beats the number of partitions once S >= (3r/4)log_2(m).

This supplies an alternative route to the asymptotic validity of chi_F_r for every fixed r >= 2, without using the false eta-preservation assertion. The r=1 case K2 is covered by Le Bars' known result. The proof is an internal hand argument, not Lean-formalized or externally refereed; bibliographic priority for this exact estimate has not been checked. The numerical script experiments/goranko_chain_first_moment.py sums the selected-event expectation in log space for r=2,3.


## Ikeda and Okamoto (2008): Japanese survey and double-kernel antecedent

K. Ikeda and K. Okamoto (池田宏一郎・岡本圭史), *On Random Kripke Frames*, RIMS Kokyuroku 1602 (2008), 74–84. [RIMS primary PDF](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1602-11.pdf). Title page visually inspected; text of Definitions 23–25, Propositions 27–28, Theorem 29 and Theorem 30 inspected. The survey defines double kernels and explicitly identifies the three-point central target with all four peripheral arrows missing (our 0000) as a bounded-morphic image under universal two-step reachability, attributing the result to Goranko–Kapron [9 in that survey]. Theorem 29 recalls fair-model almost-sure validity of NO-DKER, which gives vanishing probability of that target; the proof is omitted in the survey. Theorem 30 recalls Le Bars's nonconvergent frame-validity probability. This is established precedent, not a new three-point result. The paper is an introductory survey rather than a full central-frame census, and the inspected sections do not give the two particular four-point thresholds studied here. This is not sufficient to establish priority. The first page was visually verified; an attempted out-of-range screenshot returned an error. The Japanese author names are copied from the title page; romanizations beyond initials are not assumed.
