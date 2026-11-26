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

## Four-point finite Lean formalization (staged, not compiled)

- RandomKripke/FourPointCensus.lean at e8e85ad486d477b40f1ebff01186f607f3356d5c contains 20 theorem declarations, including direct proof of the successor-image characterization, bit encoding/decoding and marked permutation completeness, canonical count 104, exact proper minimal-image class count 70, disjoint explicit candidate lists of sizes 22 and 12, reflected certificate validity and exact certificate coverage, representative witnesses, and invariance under isomorphisms moving the distinguished center. The 22/12 list properties are finite structural statements; their asymptotic labels remain supplied by the hand probability theorems. No new probability formalization.
- Actual independent JS audit read the committed Lean numeric lists and checked all 512 roundtrips, all 91,136 candidate functions to the three fixed smaller minimal targets, 3,072 marked relabellings and 3,360 allowed central relabellings (including center-moving isomorphisms), all 70 explicit certificates and equality with the CSV. All checks passed. df2b6300317de977f6f2f15c393b9cf9942902b0 stores Python reproduction experiments/lean_census_data_audit.py, not yet executed in CI.
- 5393e11fa6ca3ef22493d034563b70cdf52e2b9f adds the module to the project root; c296aa356760f07a6dc77c00ddff16bee1202945 adds independent data check and explicit Lean module build to the existing workflow. New declarations have no proof-placeholder tokens, but this is not proof of compilation or of trusted theorem dependencies. The local runtime has no lean, lake or elan; no current verified workflow log. Next obtain actual compiler output, repair any elaboration or evaluation issues, and inspect theorem dependencies. The archival verified baseline is unchanged. No merge or submission.


## Unified fixed-bias manuscript v0.4 audit

Main text: paper/MANUSCRIPT_BIASED.md (21de413ff3c18d45f09769307e3bdcb259a23f48); companion numbered technical appendices: paper/BIASED_PROOF_APPENDICES.md (d4681689e9c31b5732c95ab9ffd17ab2c143bac4). Together approximately 14,000 words. The original fair Markdown and LaTeX are preserved. This is an integrated two-part Markdown draft, not a compiled submission. No new asymptotic classification is asserted beyond the preceding phase theorems.

Internal cross-audit:
- Verified dependency of the uniform small-fibre exclusion on the label-specific missing-signature hypothesis, not on the separate degree assumption; in the last target C,Z have missing signatures empty and {A,M}, whereas in the two-stage target neither universal-incoming label misses exactly V.
- Rechecked the forced fibre laws against the order of exposure. For 011010111 the M0 column tests use coordinates disjoint from A and Z columns, and its completion needs the separate C-hit event. Clarified that a specified row misses a hit-conditioned column with probability <=rho, and the probability of missing all c independent columns is <=rho^c; the earlier loose phrase "<=rho^c per column" was incorrect. The actual J bound is unchanged. Distinguish H0(a,z), the exact witness probability factor, from H(t,s), the exponent.
- Uniform negative exponent bounds use a,z=L+O(log L) or b=L+O(log L), with large next-fibre tails paying for the number of independent sets. Fixed-phase equalities use Stirling with j+i, not L, to retain polynomial decay. Full-sequence vanishing at rho_* needs the uniform boundary argument of Appendix A.4, not merely exact zero phases. Rechecked the lattice switch argument and exact rational root sign bracket.
- Positive-phase triple, pair and unequal-size pair second moments all count fixed witnesses. Low overlap uses disjoint retained hit blocks; high overlap with a large deficit is negligible; near alignment reduces to a conditional bound on other independent first fibres. Uniqueness of the forced sets makes the remaining diagonal contribution negligible. Completion failure is bounded for a fixed witness and then counted; no unjustified fresh-edge assumption for arbitrarily chosen successful witnesses. No new fatal gap found during internal review, but this is not an independent referee report.
- Recomputed all four regime counts directly from the committed 104-row CSV: canonical (zero,one,oscillatory) = (92,12,0),(92,11,1),(92,10,2),(93,10,1); labelled (454,58,0),(454,52,6),(454,46,12),(460,46,6); minimal vanishing four-point counts 22,22,22,23. This was an actual JS calculation; the probability labels are inputs from the hand proofs.
- The unified main text explicitly proves ML^r subset ML^as_theta by the fixed-bias extension-axiom bound and uses Goranko 2020 Props 3.2(ii), 3.5, 4.2(ii). Thus all noncentral finite frames are excluded, and positive limsup, not convergence to 1, is the correct model criterion.
- New bibliographic check: Le Bars, A Sharp Threshold for a Non-monotone Digraph Property, Mathematics and Computer Science II, 2002, pp. 197–211, author text https://lebarsj.users.greyc.fr/publications/3tournament.pdf, publisher volume https://link.springer.com/book/10.1007/978-3-0348-8211-8. Section 2 already uses integer logarithmic kernel-size phases, first/second moments and fixed edge density; related variants and zero-one failure are established prior art. The specific three threshold constants and target classifications have not been located in the targeted searches, which is insufficient to establish priority. Goranko primary text rechecked; attempted PDF screenshots of Goranko and Le Bars timed out. Schamm figure still unverified. No new Lean declarations; no new verified CI or compiled v0.4 PDF.
