# Research handoff — durable project state

Updated 2026-11-25. This is the entry point for a new chat, agent or human collaborator. Use the GitHub branch and CI rather than relying on a previous conversation. Keep this file current when substantive progress is committed.

## Repository and working rules

- Repository: bujue81-commits/random-kripke-frames
- Working branch: research/three-point-central-frames; PR #1 (draft).
- Goal: rigorous results on the almost-sure modal logic of labelled random finite Kripke frames, with Lean 4 and reproducible Python experiments.
- Commit each coherent proof, code change or research note; record head SHA, CI result, remaining obligations and exact reproduction commands here. Never describe uncompiled Lean as verified or a numerical experiment as a proof.
- Do not merge the PR merely because CI is green. Confirm exact latest head, inspect logs, and distinguish mathematical, engineering and bibliographic review.
- Never overwrite unrelated collaborator changes. Prefer small commits.

## Verified baseline

Head e4c00634604859d3339758564e516ad7eb5965e8 passed PR CI run 45573227061 (job 139064736314; checkout was the PR merge commit). All four Python audits, default Lean build and four explicit module builds succeeded. Lean/Mathlib v4.36.0. There were nonfatal Mathlib module-system warnings. All five substantive Lean modules imported by RandomKripke.lean contain 24 theorem declarations in total.

- FiniteFrames: bounded morphisms, composition, centrality, seriality, finite quotient classification.
- ExactSmallN: 6 and 3 labelled source relations at n=3 for F0001 and F1001, respectively; uses native_decide.
- F1001Characterization: exact fibrewise iff.
- F0001Witness: necessary weaker witness condition.
- GorankoEtaCounterexample: explicit three-to-two-point counterexample to eta preservation, both frames having two-step reachability. It refutes a proof step, not the final proposition.

The n=4 counts are Python-only. The three asymptotic probability bounds are not formalized. See docs/PROOF_AUDIT.md and docs/RELATED_WORK.md for detailed history.

## New changes after that baseline

- e8e9818829473ac980443bc2653988ab9ff2869a: restored proofs/GORANKO_CHAIN_FRAMES_FIRST_MOMENT.md, including exact selected-event expectation, parity bound on forbidden edges, uniform two-range estimates and explicit final constant. This is a hand proof for the explicitly stated chain target, not a Lean theorem. Verify target identification against the primary source before external claims.
- 464cd4526ce7c14806caa9d06cf3538e1c0cce63: added a conservative proof-placeholder/explicit-axiom token guard, dynamic module builds and theorem axiom reporting in CI. The new checks have not yet been confirmed green. The current reporting assumes top-level theorem declarations in namespace RandomKripke with simple ASCII names; revise as the namespace structure evolves. It is not a general parser or full axiom allowlist.
- This handoff is a separate commit. Check its actual head and CI in GitHub, not from a stale PR description.

## Mathematical status and limits

For fixed target and independent fair ordered edge variables including loops:
- F0001: internal hand proof O(1/sqrt(ln n)); necessary witness lemma in Lean.
- F1001: internal hand proof O(1/ln n); exact partition condition in Lean.
- Chain target F_r, fixed r>=2: internal hand proof exp(-Omega_r((ln m)^2)); Python audit of selected event for r=2,3. No claim about r growing with m, no matching lower bound, no full classification of K^as.
- Other three-point cases 0101, 1011, 1111: not resolved here.
- Jankov-Fine correspondence, probability-space definitions, expectation and limiting estimates are not formalized. Verify whether generated subframes or global surjections enter the exact characteristic-formula convention.
- Schamm (2002) already searched the 16 central three-point frames and introduced the partition first-moment method. Do not claim novelty for that search. Priority of the quantitative results remains unchecked. The Sliusarev transfer theorem has an extra unverified limsup hypothesis.

## Next work, in order

1. Verify CI on the newest head, inspect axiom report (especially native_decide), correct any failed guard or build. Tighten the report to a deliberate allowlist after inspecting actual dependencies.
2. Define the chain family for arbitrary r and its necessary witness condition in Lean; prove the forward implication from IsBoundedMorphism. Add it to RandomKripke.lean, run its explicit build and commit the tested result.
3. Formalize the parity inequality sum of adjacent products <= (sum of sizes)^2 / 4, preferably separately from probability theory.
4. Formalize the labelled fair-edge sample space and finite partition count, then the necessary-event probability product and first-moment inequality.
5. Prove the asymptotic estimates, starting with the simpler chain argument and reusing probability infrastructure for the other targets.
6. Independently verify primary-source target definitions and characteristic formula conventions, novelty, and the open cases.

## Reproduce

    lake exe cache get
    lake build
    lake build RandomKripke.ExactSmallN
    lake build RandomKripke.F1001Characterization
    lake build RandomKripke.F0001Witness
    lake build RandomKripke.GorankoEtaCounterexample
    python3 experiments/finite_quotient_audit.py
    python3 experiments/exact_random_frames.py
    python3 experiments/expected_partition_sum.py
    python3 experiments/goranko_chain_first_moment.py

Optional: experiments/large_n_audit_numpy.py requires NumPy and SciPy. See .github/workflows/lean.yml for the newest proof-hygiene and axiom audit commands.

## Restart prompt

Read docs/RESEARCH_HANDOFF.md, inspect current PR #1 head, latest CI jobs and raw logs, and verify the current source tree. Continue the earliest unresolved milestone above. Work in small GitHub commits, update this handoff, and distinguish Lean-checked theorems from hand proofs and experiments. Do not merge without explicit approval.

## Incremental checkpoint: general chain-frame formalization

- Rechecked Proposition 4.7 of Goranko (2020), printed p. 264, at https://www.aiml.net/volumes/volume13/Goranko.pdf. Its target relation is exactly the union of all arrows into/out of 0 and the successive arrows from 1 to r. The extracted primary-source text confirms the target definition used in the hand proof. The PDF page-image retrieval timed out; the text was available. This confirms identification, not bibliographic novelty.
- ce53710d120c30b56f43db57f335697f6569f3b0: added RandomKripke/ChainFrames.lean, with the general target, necessary-event implication and six arithmetic lemmas. In particular, for an arbitrary list xs of noncentral fibre sizes, chainAdjacentWeight xs is the sum of successive products, and chain_forbidden_weight_lower states 3*(xs.sum)^2 <= 4*((xs.sum)^2-chainAdjacentWeight xs). The proof uses induction via odd/even position sums and a square inequality. This is the arithmetic part of Q >= 3S^2/4, not yet its identification with actual forbidden ordered-pair cardinalities.
- eba43d5edcb3bdadaf0b179a92859f468f74d64b: imported ChainFrames in the root module, so the dynamic CI module build and theorem report should include it.
- At the start of this checkpoint the connector reported no PR workflow runs or combined commit statuses for c226d57654d32afe6873cc5613c096594acca301. The prior verified baseline remains e4c0063. Neither the new CI guard nor the new seven theorem declarations is claimed compiled yet.
- Next: inspect CI for this checkpoint's actual latest head; resolve any compiler or audit failure first. Reproduce with lake build RandomKripke.ChainFrames. Then bridge the list arithmetic to a Finset of actual forbidden noncentral ordered pairs and establish the finite fair-edge probability space. Do not count the new theorem declarations as verified until logs confirm compilation.
