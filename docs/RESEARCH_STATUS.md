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
- CI run [45555290042](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45555290042), on commit `48128fc80a2b3b877012dab0628a4b3e3c4ffba6`, passed all three Python audits and the Lean build.
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

The latest complete code-and-proof CI run is [45555290042](https://github.com/bujue81-commits/random-kripke-frames/actions/runs/45555290042), commit `48128fc80a2b3b877012dab0628a4b3e3c4ffba6`. It passed: (1) the six-surjection/sixteen-target finite quotient audit; (2) exhaustive source-frame and surjective-map counts for n=3,4; (3) the log-stable first-moment numerical audit, including exact n=3,4 cross-checks; and (4) `lake build`. The subsequent change to the minimality note is documentation-only and has its own CI run pending. No asymptotic theorem is formalized in Lean.


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
