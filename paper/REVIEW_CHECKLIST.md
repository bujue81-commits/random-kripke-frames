# Manuscript review and release checklist — 2026-11-26

Scope: internal audit, not independent peer review. Main draft: MANUSCRIPT.md (commit 2e0973d37c22a61c4ef26a7b18467d66c646391c).

## First integrated audit

| component | status | audit finding |
|---|---|---|
| Source measure | internally checked | Independent ordered edges including loops; fair main theorem; all constants in biased lemmas depend on fixed theta. |
| Isomorphism | independently recomputed | All 24 permutations on 4 points give 104 classes, agreeing with 6 peripheral permutations. Central vertices are interchangeable twins. |
| Smaller quotient test | independently recomputed | 25,600 surjective functions checked across 512 peripheral matrices (14 maps to 2 labels and 36 maps to 3). Construct quotient by forth, explicitly test back. 70 types inherit vanishing. |
| Classification coverage | independently recomputed | 20 degree, 2 forced negative, 9 complete-core positive, 3 exceptional positive beyond the 70 inherited. Labelled counts 103,12,43,15,339. All sum to 512. |
| Degree theorem | internally rechecked | Tiny-fibre union uses unconditional tests, not conditioning on the empty-rectangle event. Large support and clipping bounds retain all constants needed at quadratic scale. Balanced lower bound keeps factorial in overlap sum. Critical case reorients only the quadratic form, not the actual target. |
| Complete-core theorem | internally rechecked | Fresh coordinates for nonselected rows ending outside reserve W are disjoint from the ACTUAL tuple/signature exposures. Conditioning on the larger sigma-field of all edges incident to W alone would not justify inside-W rows; proof explicitly uses finer history. |
| Forced-fibre negative cases | internally rechecked | Required A is uniquely determined by B. Additional edge blocks are fresh. Size tails and the narrower Poisson resonance window are explicitly separated. No matching lower bounds claimed. |
| Dominating reserve | internally rechecked | Second moment over reserve subsets; outside-W edges from selected D exposed only after D selected. Remaining outside-D rows are fresh. |
| Two-stage positive | internally rechecked | Independent-set concentration plus expected count of failed completions avoids adaptive selection bias. Requires rho>1/e. |
| Final positive first moment | internally rechecked | Exact forced-pair formula and all hit probabilities. Uniform growth exponent has endpoint values >0.48. |
| Final positive second moment | internally rechecked | Outside-support row and column constraints disjoint. Low-overlap Bonferroni correction is uniform; large-deficit tail uses crude ratio. Near-full overlap forces alignment of A. Condition on first witness's disjoint block constraints; sum conditional probabilities of other close independent A sets. Uniqueness of Z,M from A is essential. |
| Logic | internally checked against primary text | Goranko 2020 Prop 3.5, Prop 4.2 and appendix. Ordinary global translation on R^2 universal frames. Positive image limit implies validity of every almost-sure formula by preservation. 25 minimal types yield mutual independence, not general non-finite axiomatizability. |

No new fatal gap identified in these checks. This is a first-pass audit by the same assistant that drafted the arguments, not independent review. It does not certify every inequality or establish publication priority.

## Literature

- Goranko 2020 primary text fetched on mirror https://titan.dcs.bbk.ac.uk/volumes/volume13/Goranko.pdf ; Proposition 3.5 confirms central-point characterization; Theorem 3.7 and pp. 261–262 credit earlier double-kernel and single-kernel results. The PDF page screenshot request returned 404; original site timed out.
- Le Bars 2002 LICS record and DOI verified: https://lics.siglog.org/2002/LeBars-The01lawfailsforfra.html ; https://doi.org/10.1109/LICS.2002.1029831 . General zero-one law fails; not a novelty claim.
- Goranko–Kapron 2003 publication metadata and DOI verified. Schamm dissertation search records and supervisor's student list confirm title and author; no newly verified figure image. Prior Section 3.3.6 text audit recorded in RELATED_WORK.md.
- Sliusarev official thesis defence record https://www.hse.ru/sci/diss/1034821759 (15 January 2026), summary and related Horn/Euclidean/transitive papers located. Not a full reading of the Russian dissertation. No verified prior four-point central census located in the targeted searches; absence of a search hit is not proof of originality.
- Before submission verify Schamm Figure 4.1 against original scan; read relevant full papers/thesis, check citation trail, and distinguish known results from new candidate theorems.

## CI and Lean verification

As checked on 2e0973d37c22a61c4ef26a7b18467d66c646391c, combined commit statuses and pull-request workflow runs are empty. The connector's commit-workflow tool filters to PR-triggered runs, so this is NOT evidence that no push-triggered run exists. The base main branch returns 404 for .github/workflows/lean.yml; research branch contains push/PR/workflow_dispatch configuration. Old CI run 45573227061, job 139064736314, is still retrievable and successful. It does not verify subsequent commits. There is no exposed dispatch action. No new Lean verification claim, and do not change main or merge without approval.

User-assisted route: open https://github.com/bujue81-commits/random-kripke-frames/actions and inspect latest research-branch push runs; if available send actual run URL or logs. Otherwise run on local checkout of the research branch: python3 experiments/four_point_census.py ; lake build ; lake build RandomKripke.ChainFrames ; lake build RandomKripke.ChainEdgeCounting . Local output should identify commit and toolchain. A default-branch workflow or other CI changes require explicit approval.

Formalization plan (after actual Lean builds are confirmed):
1. Define Fin 4 frame from 9-bit peripheral relation, and executable quotient/partition predicate.
2. Prove successor-image characterization equivalent to existing IsBoundedMorphism, then reflect it to Boolean computation.
3. Prove permutation orbit equivalence and canonical representative soundness. Use native_decide only for explicit finite statements, not asymptotic claims.
4. Check 104 representatives and the 70 inherited-zero classes, and exact lists of 22 minimal candidates/12 positive candidates conditional on the probability classification. Keep finite combinatorics separate from the proof of asymptotic labels.
5. Build every module explicitly and print theorem axioms. Formalizing probability estimates will be a separate project.

## Release gates

- [x] Main manuscript draft with explicit proof dependency map.
- [x] Independent finite algorithm recomputation.
- [x] First-pass internal proof audit.
- [x] Integrated full-proof Markdown manuscript v0.2 (MANUSCRIPT_FULL.md).
- [x] Explicit finite classification certificates for all 104 four-point types and 70 quotient maps.
- [x] Convert integrated manuscript to standalone LaTeX source v0.3.
- [ ] Compile and visually review the complete LaTeX manuscript (representative smoke test only so far).
- [ ] Verify primary-source priority; full external mathematical review.
- [ ] Obtain current CI and verify pending Lean modules.
- [ ] Formalize finite census and then selected asymptotic lemmas.
- [ ] Set author/affiliation with researcher and disclose AI assistance according to venue rules; never invent independent proof verification or attribution.
- [ ] Author approval before any public submission. No submission or merge performed.

## v0.2 integration audit

The full Markdown text at 724fa1533f1ae80abc900134c5f1fcf1d3e4785c incorporates the five exceptional-target arguments, exact forced-pair formulas, full overlap second moment, finite enumeration pseudocode, explicit characteristic formula and prime-cycle quotient proof. The previous main text remains unchanged. The three-point catalogue was independently recomputed: 10 canonical classes, seven negative and three positive, with exactly two minimal negative classes. Burnside counts 10 and 104 were derived explicitly. No remaining external proof-file dependency; supplementary links concern reproducibility and bibliographic evidence. This is not yet a typeset/compiled submission.

The per-type CSV at 4ab0f876c10259d3631731b6b6a8b4259d34ea92 includes 70 explicit maps onto one of the smaller minimal targets; the JS generator checked direct successor-image equality for each and exhaustively checked no smaller minimal image for the other 34 canonical types. 9322960083eb675069d5930331d8c06ca8c2cbf1 provides a Python checker (execution not confirmed). 74b37abaf9ff324c35ff07091c292af368f58da6 integrates it into CI. These are finite certificates, not probability proofs.

Repeated literature search located Schamm's dissertation through indexed expiring signed PDF URLs and the University of Johannesburg output index, but the repository page returned 403; no figure image recovered. The Goranko 2020 mirror primary text was accessible, but page screenshot returned 404. No priority claim. No new Lean source or verified run.

## v0.3 LaTeX conversion and second internal audit

- 28c7ef3630e53099c8dbd1589cea8f049c703cba created paper/manuscript.tex from the complete v0.2 text with 42 typeset display formulas and two encoding-list blocks (44 mathematical/display blocks total), three tables and the finite-classifier pseudocode. a7746f546c0b130b47f70ca1d750f7ecc79ef93e improved inline mathematical typesetting. 8fb48d30de0950fea77c9f6aa87b89c4057ff835 added standard theorem/proof environments, corrected residual raw exponent notation, and passed static environment/brace/inline-delimiter checks. This editorial conversion is not a compiler or semantic proof of equivalence; further notation and visual review is required.
- Found a real statement-level omission in v0.2 Theorem 2: the degree and singleton-miss hypotheses must be restricted to r>=1 (at least one peripheral vertex). Without it, the hypotheses are vacuous for the complete singleton, and the final vanishing claim is false. The original NO_SINGLETON_MISS_DEGREE_CRITERION.md already explicitly assumed r>=1. Corrected integrated Markdown in 89c803bd8239c416c36e072acbacb2456e46d9a2 and LaTeX in 8fb48d30de0950fea77c9f6aa87b89c4057ff835. The probability classification of the singleton remains positive by the separate seriality argument; no other census counts change.
- Rechecked conditional block-law and overlap arguments in the final positive case: the necessary witness's forbidden rectangles, external hit blocks and Z-to-C column-hit blocks are disjoint; conditioning on a nonempty-hit block decreases the probability of specified absent coordinates. The large-deficit tail and near-aligned independent-fibre cases are separate; a successful triple is uniquely determined by A. Rechecked the fixed-size first-moment exponent and the critical Poisson permutation argument. No further fatal gap identified in this internal review; this is not independent peer review. The old v0.1 archival source still contains the abbreviated wording; use corrected integrated source for the current paper.
- Local runtime has latexmk and pdfTeX 1.40.26 (TeX Live 2025/dev/Debian). A representative one-page smoke test with identical preamble, theorem/proof environments, representative exact forced-pair and characteristic formula displays, table, and verbatim algorithm compiled to PDF with zero fatal errors. The complete repository source could not be downloaded into that runtime (DNS and URL-download restrictions). No complete manuscript PDF has been compiled or visually verified. 064ac69b0bad4613cdf54b0e83b31b40bb7e9d81 records the exact build command; 19e5f6771e4cba6431886b1961c336b2d8d70c7b adds a dedicated push/PR/manual manuscript workflow and PDF/log artifact. Current run not verified. The prior Lean CI blocker remains.
- Bibliographic recheck confirmed Goranko-Kapron 2003 DOI 10.1007/s001530100135 and AiML 2020 paper metadata, and located an additional author-hosted version https://www2.philosophy.su.se/goranko/papers/AiML2020_Goranko_paper_56_final.pdf . Schamm repository index again led to expired signed PDF links; Figure 4.1 visual ordering and novelty remain unverified. No submission, no merge, no invented author details.
