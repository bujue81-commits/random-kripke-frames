# Research status and proof obligations

Date: 2026-11-25

## Probability model

For each n, G_n is a labelled directed graph on [n]. Every ordered pair (x,y), including loops, is independently an edge with probability 1/2.

For a fixed finite frame F, let p_n(F) be the probability that G_n admits a surjective bounded morphism onto F. If chi_F is the corresponding Jankov–Fine characteristic formula for the chosen language, then the frame-validity measure satisfies mu_n(chi_F)=1-p_n(F). The precise theorem and language convention still need a primary-source citation.

## Target frames

Vertex order is (c,a,b):

F0001 = [[1,1,1],[1,0,0],[1,0,1]]

F1001 = [[1,1,1],[1,1,0],[1,0,1]].

Both have central point c and are serial.

## Finite quotient facts

- F0001 has no surjective bounded morphism onto any two-point frame.
- F1001 has exactly one two-block fibre partition, up to swapping target labels, that gives a bounded morphism: {c}|{a,b}. Its quotient is T2, the complete reflexive two-point frame.
- Both targets map onto the reflexive singleton E1.
- The exhaustive Python quotient audit passes in CI.

The previous statement that all three two-block partitions of F1001 work was erroneous and has been corrected in the proof-audit note.

## Exact finite random-frame counts

Exhaustive enumeration gives:

| n | F0001 source relations | F1001 source relations | F0001 surjective maps | F1001 surjective maps | Total relations |
|---:|---:|---:|---:|---:|---:|
| 3 | 6 | 3 | 6 | 6 | 512 |
| 4 | 1,332 | 787 | 1,332 | 1,620 | 65,536 |

The map columns count all surjective bounded morphisms over all source relations, so dividing by the total relation count gives the exact first moment. The separate log-stable partition-sum script agrees with these exact n=3,4 counts. These are finite checks, not asymptotic evidence by themselves.

## Asymptotic probability arguments

Detailed hand proofs are in:
- `proofs/F0001_first_moment.md`
- `proofs/F1001_first_moment.md`

I have independently rechecked the combinatorial event definitions and the main summation estimates in both drafts. The F0001 argument counts a weaker necessary-condition event, so its first moment is a valid upper bound. The F1001 argument uses the exact fibre-partition event; its row constraints split by destination fibre, and its Poisson cross-sum has an explicit summable majorant.

These are still hand proofs. They have not been referee-checked by an independent mathematician and are not Lean-verified. They should be presented as proof drafts, not as established published results.

## Other three-point types

The proposed claims for types 0101 and 1011 remain open proof obligations. The independent-set and second-moment constructions need full conditional-independence checks, including whether the partition is selected using edge variables later assumed independent. The 1111 case has not been settled here.

## Logic and independence claims

The proposed independence of chi_F0001 and chi_F1001 over ML^r is conditional on:
1. the correct Jankov–Fine theorem for the exact language and frame-validity convention;
2. the precise finite-frame characterization of ML^r;
3. verification that both target frames validate ML^r;
4. the correct quotient direction.

The proper-image note now distinguishes minimality among frames whose characteristic formulas are almost-surely valid from minimality among all central-point frames.

## Lean status

- `RandomKripke/FiniteFrames.lean` and `RandomKripke/ExactSmallN.lean` both pass `lake build` together. The exact-count search uses a finite filter of all maps and `native_decide`.
- CI run [45566445869](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45566445869), on commit `72603e73e696f8fb5934a2363cd6f14e0b90b889`, passed all three Python audits and the Lean build.
- The finite Lean scope includes exact n=3 labelled counts: 6 source relations for F0001 and 3 for F1001. No asymptotic probability theorem is formalized in Lean.

## Next tasks

1. Confirm the current Lean exact-count module builds.
2. Keep the Python exact enumeration and quotient audit green.
3. Refine the two hand proofs into a referee-ready version with every uniform bound explicit.
4. Investigate 0101 and 1011 using carefully separated random edge blocks.
5. Complete the primary-source and novelty audit.


## Novelty update (2026-11-25)

A direct precursor has been identified: Rainer Franz Schamm, *Zero-One Laws and Almost Sure Validities on Finite Structures* (M.Sc. dissertation, Rand Afrikaans University, January 2002; supervisor Valentin Goranko). Sections 3.3.5–3.3.6 already introduce the same F-partition first-moment formula and experimentally examine all 16 three-point frames with a central point. Figure 4.1 classifies their expected-partition behaviour; the appendix proves K4 analytically. Consequently, the 16-frame search and candidate selection are not new contributions of this repository.

The plausible new contribution is a rigorous asymptotic proof for particular cases that Schamm treated experimentally, plus Lean formalization of finite structural facts and reproducible computation. Under the thesis Java-code bit convention, F0001 has mask 8 and F1001 mask 9. The appendix's included Java code evaluates the full partition sum at n=50 for each mask; the genetic-algorithm code is mentioned but not included. The natural reading of Figure 4.1 appears to label mask 8 “No growth” and mask 9 “Slow growth”, but the visual ordering has not yet been independently confirmed. These labels are heuristic rather than proved limits. Our log-stable exact first-moment script gives a decreasing expectation for F1001 from about 0.128 at n=50 to 0.0405 at n=1000. The hand proof claims the limit is zero. This is a potentially useful refinement of the 2002 experiment, but must be reconciled with the original figure and code before claiming a correction.

The 2025/2026 Sliusarev thesis is also relevant adjacent work: it develops a general random-L-frame framework and a connected-frame transfer theorem, with main applications to KD5, KD45, K5B, S5, Grz.3, GL.3, SL and Horn closures. The unrestricted K case and our two target frames are not among its listed main results, but its publications still need checking.


## Current verification snapshot

The latest complete code-and-proof CI run is [45566445869](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45566445869), commit `72603e73e696f8fb5934a2363cd6f14e0b90b889`. It passed: (1) the six-surjection/sixteen-target finite quotient audit; (2) exhaustive source-frame and surjective-map counts for n=3,4; (3) the log-stable first-moment numerical audit, including exact n=3,4 cross-checks; and (4) `lake build`. The subsequent updates to the independent audit, numerical documentation, and Sliusarev relevance note are documentation-only; the CI workflow is running on the newest documentation head. No asymptotic theorem is formalized in Lean.


## Independent proof audit (2026-11-25)

A new detailed audit is recorded in [INDEPENDENT_PROOF_AUDIT_2026-11-25.md](../proofs/INDEPENDENT_PROOF_AUDIT_2026-11-25.md).

The current internal audit found no fatal gap in either first-moment argument:
- F0001's weaker witness event, disjoint-rectangle probability, binomial reduction, and Poisson point-mass estimate are valid.
- F1001's exact fibre-partition formula, small/large fibre bounds, Poisson cross-sum domination, and middle-tail Stirling estimate are valid. The proof now states a uniform relative error of 1 + O((ln n)^10/n) for the central Poisson approximation and an explicit Stirling constant for the remaining middle tail.

This is an internal proof audit, not independent peer review. The asymptotic arguments remain hand proofs and are not Lean-formalized.

The generic numerical script had a matrix/fibre ordering mismatch: target matrices are ordered (c,a,b), while the proof variables are (a,b,c). The total sum was unchanged by permutation invariance of the complete triple sum, but fixed-size terms were not aligned. This is corrected, with a new termwise F1001 formula assertion. An optional NumPy/SciPy large-n script now reproduces values through n=30,000 after checking exact n=3,4 counts.


## Sliusarev 2025/2026 theorem audit

The English thesis summary's Theorem 83 gives a transfer from all random L-frames to connected random L-frames, but only under the extra hypothesis that every formula outside the connected almost-sure logic has connected-validity limsup strictly below 1. For L=K, connected frames exist at every size, but that limsup hypothesis has not been proved here. The theorem therefore does not by itself classify K^as.

The same summary states that the unrestricted random frame has Ext_m properties a.a.s., implying the frame conditions characterizing ML^r and hence ML^r ⊆ K^as. This is background already present in Goranko's programme, not a new result of this repository. See docs/RELATED_WORK.md for the precise theorem statement and source.


The latest completed code-and-proof CI run is [45566445869](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45566445869), commit 72603e73e696f8fb5934a2363cd6f14e0b90b889. All three Python audits and lake build passed. Subsequent commits only update documentation and bibliography notes.


## Lean CI coverage correction (2026-11-25)

A source-level audit found that the F1001 exact-count theorem had accidentally stated the F0001 source-set cardinality equals 3. This contradicted the preceding F0001 theorem and was a real source error. It is corrected to use SourcesOfF1001OnThreePoints.

More importantly, the previous CI log for run 45566445869 showed that the default lake build compiled RandomKripke.FiniteFrames but did not compile RandomKripke.ExactSmallN. Thus the earlier green CI did not verify the exact n=3 Lean enumeration module. The workflow now explicitly runs lake build RandomKripke.ExactSmallN after the standard Lean action. The explicit module build has now passed in CI run [45567277661](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45567277661), commit 9853990185486a656cd5f7adefb9a2e65f2b4353. The corrected F1001 theorem and both exact n=3 Lean counts are now actually compiled by the explicit target.


## Exact-count Lean verification confirmed

CI run [45567277661](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45567277661) completed successfully. Its log explicitly shows the command lake build RandomKripke.ExactSmallN and “Build completed successfully”. Thus the corrected exact_count_F0001_n3 and exact_count_F1001_n3 declarations are now genuinely checked by Lean. The preceding default build alone did not cover this module; the workflow now has the explicit target.


## Quantitative F1001 result (internal hand proof)

The F1001 first-moment draft has been strengthened beyond mere convergence: a quantitative refinement gives the Poisson cross-sum S_n=O(1/m_n), and the remaining middle-tail sum is O(1/ln n). Since the small- and large-fibre tails are o(1/m_n), the resulting bound is
[
\Pr(G_n\twoheadrightarrow F1001)=O(1/\ln n).
]
This is an internal hand proof, not Lean-formalized or externally refereed. It is an upper bound only; no matching lower bound or asymptotic equivalent is claimed. The full argument is in proofs/F1001_first_moment.md and the independent audit note.


## Lean characterization of F1001 (2026-11-25)

A new module RandomKripke/F1001Characterization.lean proves the exact equivalence between a surjective bounded morphism onto F1001 and the fibrewise conditions used in the probability proof:
- no edges from A to B or B to A;
- every source row hits C;
- rows in C∪A hit A;
- rows in C∪B hit B.

The module is imported by RandomKripke.lean and is explicitly built in CI. Run [45568777128](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45568777128), commit e868c7f1a7bf3bfe9fc3610a5a925c8e920fbfc1, passed the standard Lean build, the exact n=3 enumeration module, and the new F1001 characterization module, as well as all Python audits.

The asymptotic probability proof remains outside Lean.


## Quantitative F0001 result and Lean witness module (2026-11-25)

The F0001 first-moment argument has been sharpened to
\[
\Pr(G_n\twoheadrightarrow F_{0001})=O(1/\sqrt{\ln n}).
\]
The proof splits at \(A_n=\lfloor\frac12\log_2 n\rfloor\): small fibres are exponentially suppressed by \(e^{-\sqrt n/4}\) up to a subexponential prefactor, while large fibres are bounded by Poisson point masses. The at-most-two central indices contribute \(O(1/\sqrt{\ln n})\), and the off-central Chernoff tails are exponentially small.

RandomKripke/F0001Witness.lean formalizes the weaker necessary-condition event used in this argument and proves that every surjective bounded morphism onto F0001 satisfies it. The module is imported by RandomKripke.lean and explicitly compiled in CI.

Latest verified head: c1efeb9418e14505ee287e3093489aa0d5a18cfb. CI run [45569425119](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45569425119) passed all three Python audits, the standard Lean build, and explicit builds of ExactSmallN, F1001Characterization, and F0001Witness. The F0001 and F1001 asymptotic probability estimates remain hand proofs, not Lean theorems.


## Quantitative F0001 result

The F0001 proof has also been sharpened. Its central Poisson point-mass range has at most two indices and contributes O(1/sqrt(ln n)); the noncentral tail is exponentially small in A_n, while the small-fibre range is o(1/sqrt(ln n)). Thus the hand proof now claims
[
\Pr(G_n\twoheadrightarrow F0001)=O(1/\sqrt{\ln n}).
]
This is an upper bound only, not an asymptotic equivalent. See proofs/F0001_first_moment.md.

## Lean witness-condition formalization

RandomKripke/F0001Witness.lean proves that every bounded morphism onto F0001 satisfies the weaker fibrewise witness conditions used in the F0001 first-moment upper bound. CI run [45569425119](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45569425119) explicitly built this module successfully, together with the F1001 characterization and exact n=3 module.

## Potential issue in Goranko Proposition 4.7

A finite counterexample has been added in RandomKripke/GorankoEtaCounterexample.lean to test the claimed preservation of eta = forall x exists y (Rxy and not Ryy) under bounded morphic images. The first CI attempts exposed a decidability issue; the proof was rewritten with explicit finite cases. CI run [45571076110](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45571076110) passed the explicit Lean module build. The counterexample is now Lean-verified. A Python cross-check has since been integrated into finite_quotient_audit.py; it passed the Python step on head 844dc5acdae4f4ded3a0530db9eba09f020cedbf, while the complete Lean workflow for that head is still running. It refutes the preservation step, not the final conclusion of Proposition 4.7. See docs/RELATED_WORK.md and proofs/GORANKO_2020_PROP_4_7_ETA_COUNTEREXAMPLE.md.


## Goranko Proposition 4.7: preservation counterexample

A separate finite counterexample has been identified to the preservation step used in the proof of Proposition 4.7. The paper asserts that \(\eta=\forall x\exists y(Rxy\land\neg Ryy)\) is preserved under surjective bounded morphic images. Let G be the complete irreflexive directed frame on three points, let F1 have edges (0,0),(0,1),(1,0), and map 0,1 to 0 and 2 to 1. Then G satisfies eta, G maps onto F1 by a surjective bounded morphism, but F1 fails eta at 1. Both frames have two-step reachability. Thus the stated preservation step is false under Definition 2.1 as printed.

The Lean theorem is in RandomKripke/GorankoEtaCounterexample.lean. The initial CI attempts failed because native_decide did not synthesize an executable Decidable instance for the whole proposition. The final proof now uses explicit finite cases and has passed the Lean build in run 45571076110. The Python cross-check was added after that run; the complete workflow for head 844dc5acdae4f4ded3a0530db9eba09f020cedbf is pending. The result invalidates the proof shortcut, not necessarily Proposition 4.7's final conclusion: those characteristic formulas may still be almost-surely valid by another argument. See docs/RELATED_WORK.md for the construction and caveats.


## Latest full CI verification

CI run [45571611756](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45571611756), commit 51ddeb975742cb52b9ba58a1ef463ffe77bd933d, passed all three Python audits and the standard Lean build plus all four explicit module builds: ExactSmallN, F1001Characterization, F0001Witness, and GorankoEtaCounterexample. This run includes the Python eta-preservation counterexample check.


## Alternative first-moment repair for Goranko's F_r family

A new hand proof draft, proofs/GORANKO_CHAIN_FRAMES_FIRST_MOMENT.md, gives for every fixed r >= 2
\[
\Pr(G_m\twoheadrightarrow F_r)\leq\exp(-\Omega_r((\ln m)^2)).
\]
It avoids the invalid eta-preservation step identified above. The argument splits on the total size S of the noncentral fibres. For S below (3r/4)log_2(m), some noncentral fibre is small and the central rows almost surely fail to hit it; for larger S, the chain structure forces at least 3S^2/4 forbidden ordered edges, which overwhelms the number of partitions.

This appears to repair the asymptotic-validity part of Proposition 4.7 for r >= 2, assuming the paper's characteristic-formula correspondence. The r=1 case K2 is already known by Le Bars. The proof is a hand argument, not Lean-formalized, and should not be described as a novel result until prior-work checking is done.

The new log-space audit script is experiments/goranko_chain_first_moment.py. Its small exact checks give E[Z_3]=6/32 for r=2 and E[Z_4]=24/1024 for r=3. At m=100 the selected-event expectations are approximately 4.5e-7 for r=2 and 2.1e-19 for r=3. The CI workflow has been updated to run this script; the latest run is pending.
