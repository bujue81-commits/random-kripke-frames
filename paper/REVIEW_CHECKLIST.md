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
- [ ] Standalone typeset manuscript with full proofs.
- [ ] Verify primary-source priority; full external mathematical review.
- [ ] Obtain current CI and verify pending Lean modules.
- [ ] Formalize finite census and then selected asymptotic lemmas.
- [ ] Set author/affiliation with researcher and disclose AI assistance according to venue rules; never invent independent proof verification or attribution.
- [ ] Author approval before any public submission. No submission or merge performed.
