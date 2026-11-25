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

## Incremental checkpoint: actual forbidden ordered pairs

- d000817dd813750995d761874b855cccbf19a8b2: added RandomKripke/ChainEdgeCounting.lean, with seven theorem declarations. Defines actual finite sets of noncentral vertices, odd/even vertices, allowed and forbidden ordered pairs. The orientation map sends an allowed pair to its odd/even ordered endpoints, and is injective because two opposite directed chain arrows cannot both occur. Consequently the allowed cardinality is <= U*V, and the theorem chain_forbidden_pairs_card_lower gives 3*S^2 <= 4*Q. The theorem boundedMorphism_chain_forbidden_pairs_absent connects these actual pairs with absent source edges. This approach bypasses the need to identify the list expression with actual pair cardinality for the large-S bound; exact formula identification is still needed for the full selected-event first moment.
- 5290d55b0e109c5f6609f5fba642894c0384c90a: imported the edge-counting module in the root.
- af60e99c0856ee56f3548d85ed2805acfaa4ff12: explicit builds for both new chain modules and workflow_dispatch configuration. GitHub may require the workflow to exist on the default branch before manual dispatch; no dispatch was performed.
- 8e8b8379049702e04ddd5ce698e087df08a7a888: added experiments/chain_edge_counting_audit.py. Independently ran the same exhaustive assertions in Python here: all 5694 fibre maps for 1<=r<=4, 1<=m<=5 passed. Includes non-surjective maps, permitted-pair count, orientation injectivity, exact forbidden-pair count and lower bound. This does not prove the Lean source compiles.
- bf9f09a7401f8296701944dc8edd69ec55a33db9: integrated the finite audit into CI.
- At checkpoint start, PR head 73c4389f40a56f214e7eaeaaf1f3d6bce9d7fb68 still had no workflow runs or combined statuses returned by the connector. No local Lean or lake executable is installed in the chat runtime. Last confirmed CI remains e4c0063. Both new Lean modules (14 theorem declarations total) are unverified source drafts. Do not accumulate further unverified Lean code until CI access is resolved. Current attempt to reopen the Goranko PDF returned HTTP 502, so no new primary-source verification is claimed this turn.
- Next: obtain actual CI results for the latest head; fix any Lean elaboration or audit errors. Then define the finite uniform sample space of all Bool-valued edge relations, prove the fixed-absent-edge event has probability 2^(-Q) by counting functions on the complement, and establish the central-hit event and first-moment bound. Preserve all changes and log actual verification results here.

Reproduction additions:

    lake build RandomKripke.ChainFrames
    lake build RandomKripke.ChainEdgeCounting
    python3 experiments/chain_edge_counting_audit.py

## Incremental checkpoint: sharp logarithmic first moment

- 61c0ca83546109ee47d7e58b84b87d2d72b8add5: proofs/CHAIN_SHARP_FIRST_MOMENT.md. Derives exact fixed-surjection probabilities for both selected witnesses and complete bounded morphisms. For fixed r>=2 and L=log_2(m), proves by hand log_2 E[X_m] = log_2 E[Z_m] + O_r(L log L) = -(r-1)^2 L^2 + O_r(L log L), with both expectations separately satisfying that asymptotic. X counts full maps, Z counts the weaker witnesses. Markov gives the corresponding upper bound on existence; a single balanced map gives the weaker lower bound 2^{-(r^2-r+1)L^2-O_r(L)}. Do not claim the exact existence-probability exponent or priority. The proof is not Lean-formalized.
- 67847e41e8c8654e3223355faf7df0e491bd2352: experiments/chain_full_map_audit.py. Independently executed the exact rational formula and exhaustive row-image semantics for five fixed surjections, checking all 512 or 65536 source relations per map. All passed: selected/full counts 16/1, 512/81, 192/3, 192/9, 64/1 respectively. Reproduce with python3 experiments/chain_full_map_audit.py.
- 9e8fd554eaa97479f25c09e538178559d72548be: integrated this regression script into CI.
- CI investigation: the connector still returned no PR workflow runs or combined statuses for 9aeb1ba. Fetch of .github/workflows/lean.yml at base SHA 0c4cd30cee1bcf283c1da1c57fdb734e20da75af returned 404. This suggests the workflow may not be present on the base branch; does not establish why push/PR runs are missing. The accessible workflow-run query filters to PR runs; it cannot rule out push runs. The prior successful run on e4c0063 is still accessible. No manual dispatch capability was available through the connector; no dispatch was attempted. Check the Actions UI or use an authenticated local checkout. Do not merge or modify main merely to trigger CI. No further Lean modules added this turn.
- Next priorities: (1) get actual build and axiom audit results for the fourteen pending Lean declarations, repair failures; (2) prove the finite uniform sample-space coordinate-block counting lemma, the full fixed-map probability formula, and the expectation formula; (3) formalize the sharper asymptotic bound. For a new research direction, investigate overlap/second moment for a matching existence exponent, distinguishing this from the now-proved hand first-moment rate; independently audit novelty.
