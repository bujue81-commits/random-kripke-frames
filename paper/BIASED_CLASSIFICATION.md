# Fixed-bias central-frame classification: theorem summary

Working supplement to the fair-model manuscript, 26 November 2026. All asymptotic claims below are internal hand proofs; independent review, full priority checking and machine verification remain pending. No changes to the fair manuscript.

Fix a labelled random directed frame on m vertices, each ordered edge including loops present independently with probability theta in (0,1). For a finite central target F let p_m(F) be the probability of a full surjective bounded morphism onto F.

Define three constants in increasing order:

    theta_c = 1-r_c = 0.7485023647443824...,
    theta_0 = 1-1/(e T) = 0.9313234165433595...,
    theta_* = (9-3 sqrt(3))/4 = 0.950961894323342...,

where r_c is the unique root in (0.251,0.252) of

    D(r) = 3+3 ln u(r)+2 ln r-(1+2r^2)u(r),
    u(r)=2 ln(1/r)/(1-r),

and T>2 solves 2+2 ln T-T=0. The exact definitions, not the decimal approximations, specify the boundaries.

## Four-point classification

Of the 104 isomorphism classes of four-point central frames, 92 have p_m->0 at every fixed bias, and ten have p_m->1 at every fixed bias. The remaining two canonical encodings have the following exact behavior:

| target | p_m->1 | liminf 0, limsup 1 | p_m->0 |
|---|---|---|---|
| 011010111 | 0<theta<theta_c | theta_c<=theta<theta_* | theta_*<=theta<1 |
| 011011101 | 0<theta<theta_0 | theta_0<=theta<1 | never |

Therefore:

| edge probability | zero limit | one limit | oscillatory | total |
|---|---:|---:|---:|---:|
| 0<theta<theta_c | 92 | 12 | 0 | 104 |
| theta_c<=theta<theta_0 | 92 | 11 | 1 | 104 |
| theta_0<=theta<theta_* | 92 | 10 | 2 | 104 |
| theta_*<=theta<1 | 93 | 10 | 1 | 104 |

Both exceptional types have six labelled peripheral matrices each. The corresponding counts with the central label fixed are respectively (454,58,0), (454,52,6), (454,46,12), (460,46,6). These are marked-label counts, not counts with an unspecified center.

All smaller central frames retain the earlier bias-independent existence-limit classification.

## Logical interpretation

For a finite central frame F, F validates ML^as_theta iff limsup p_m(F)>0, by bounded-morphism preservation and the ordinary characteristic formula on frames with universal R^2. Consequently the four-point finite model counts are 12 below theta_* and 11 at or above theta_*. Oscillation alone does not remove a frame from this model class. The characterizing formula of 011010111 distinguishes the high-bias almost-sure logic from the fair one. There are 22 minimal vanishing four-point types below theta_*, and 23 at or above it.

The convergence threshold theta_c and theta_0 are thresholds for existence-probability convergence, not proved thresholds for changes in the full almost-sure logic.

## Proof dependency map

- Fair census and the 92 uniformly negative, ten uniformly positive types: MANUSCRIPT_FULL.md, the degree, complete-core, forced-fibre and dominating-reserve proofs.
- F011010111 exact threshold for positive limsup and boundary zero: ../proofs/LAST_FOUR_POINT_BIAS_THRESHOLD.md.
- F011010111 exact fixed phases, including boundary phases: ../proofs/LAST_FOUR_POINT_PHASE_CLASSIFICATION.md.
- F011010111 convergence threshold via two adjacent lattice switches: ../proofs/LAST_TARGET_SHARP_CONVERGENCE_THRESHOLD.md. Integer arithmetic sign certificates: ../experiments/sharp_convergence_sign_certificate.py.
- F011011101 positive-phase rare-fibre construction and endpoint upper bounds: ../proofs/TWO_STAGE_SHARP_PHASE_CLASSIFICATION.md.

No inference of probability limits from finite numerical experiments alone is used. For both exceptional targets the positive directions use full overlap second moments and conditioning on fixed witnesses, followed by counting failed completions. Zero phases at critical endpoints use fixed-offset Stirling prefactors rather than the leading exponent alone.

Remaining tasks: independent mathematical review of all biased proofs; primary-source literature priority checks (including known kernel and frame zero-one counterexamples); full LaTeX compilation; Lean verification; transition windows for varying phases approaching a boundary. The present summary is not a claim of general zero-one laws or complete axiomatization of ML^as_theta.
