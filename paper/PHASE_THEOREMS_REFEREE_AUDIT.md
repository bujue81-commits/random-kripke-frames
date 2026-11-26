# Referee-style internal audit: Theorems 4 and 5

26 November 2026. Reviewed unified manuscript v0.4 and Appendix A–D at checkpoint 21f504f. This is an internal audit by the same research assistant, not independent refereeing or formal verification. No new asymptotic theorem is claimed. The purpose is to test the most fragile implications separately.

## 1. Deterministic witness reductions

For F011010111, the independent A-fibre forces Z to be exactly the outside rows missing A; M0 is the set of common nonneighbors of Z outside A union Z. A successful map requires every row to hit Z, and each non-Z row to hit M0. Conversely if these conditions hold and C0 is nonempty and hit by all rows, the exact M0 assignment supplies a map. The actual M may be a strict subset of M0, so the two counts must remain separate.

A concrete counterexample to treating the necessary witness as sufficient is the source on vertices 0,1,2,3 with row masks [1,7,3,1] (bit j corresponds to an arrow to vertex j). Its rows are 1000,1110,1100,1000 when printed in vertex order. Take A={2}, Z={0,3}, M0={1}, C0=empty. The necessary witness holds but the exhaustive 24 bijections yield no surjective bounded morphism. This is not a counterexample to the manuscript theorem: it demonstrates exactly why completion is necessary.

For F011011101, independent V determines A uniquely, and A determines Z outside V union A; requiring V and A rows to hit A and all rows to hit Z and C gives the exact successor statuses. The two-stage pair event deliberately does not yet require completion.

An actual independent JS computation exhausted all 65,536 four-point directed source relations and all 24 bijections to each target, checking the two implications for the first and exact equivalence for the second. Each target has 24 source relations admitting an image (trivial at equal cardinality but a useful check of labels). Counts of necessary witnesses, sufficient witnesses and two-stage preliminary pairs over all sources are respectively 1524, 24, 125504. The example above was found by enumeration, not postulated.

## 2. Exact integer audit of witness expectations

For rational theta=p/q, an individual present bit contributes numerator p and an absent bit q-p, with denominator q^(m^2). For a row-hit block of length l the integer numerator is q^l-(q-p)^l. Untested coordinates contribute q per bit. For the rectangular Z-to-C row-and-column nonempty event, inclusion-exclusion over j missed rows gives numerator

    sum_j (-1)^j binom(z,j) [ (q-p)^j (q^(z-j)-(q-p)^(z-j)) ]^c.

This verifies the exact conditional J factor without floating point. Independently weighted the exhaustive source counts by their edge count and compared to the formula products. Actual BigInt execution produced exact equality for all 18 comparisons (three expectations at six rational biases). For example at theta=1/2 the three numerators are 1524,24,125504, denominator 65536; at theta=24/25 the numerators are 24358642005823193088,21035720123168587776,429393004455567968750, denominator 23283064365386962890625. The full Python reproduction, experiments/phase_theorems_exact_audit.py, is committed but not yet run by Python or CI. It reproduces the JS algorithm rather than serving as evidence of independent peer review.

## 3. Uniform size and first-moment bounds

For A.1 the events excluding tiny fibres use unconditional tests and an implication on the no-empty-rectangle event; no independence conditional on that event is required. Both universally incoming labels of the three-fibre target have either zero or two missing outgoing edges. For the two-stage target neither universally incoming label misses V alone; z is lower bounded separately because Z is hit by every row. These facts justify the different size exclusions.

For both targets a forced next fibre has a binomial size *before* exposing its own columns or conditioning on further hit conditions. An oversized earlier fibre makes the next one too small with exponentially small tail probability on the relevant scale. The factor exp(400 L ln L) bounds the independent-set count uniformly: a,b <=129L and lambda<=L^3, so the displayed loose bound has ample margin. The K=1000 cutoff beats it. The main-size expansions allow O(log^2 L) error; they must not be used to settle zero exponents.

## 4. Overlap geometry and conditional independence

For the triple, restrict the first absent coordinates to S intersect S'. Its size is R=x^2+yx+yw; the pair has R=(x+y)x. Since I<=R<=Dh, the deficit inequalities follow exactly by subtraction. Within A intersect S', split into A',Z',M' parts of sizes u,v,r. The squares on the latter two parts and the rectangles out of the first part to those two parts belong to the first forbidden square but not the second forbidden set. They are disjoint; hence R-I>=v^2+r^2+u(v+r). The pair analogue omits r. In particular R-I<=Dh-I, the deficit. These inequalities apply to the unequal-size pair too; D is the larger prescribed size, eventually the independent V size because alpha<1.

For small overlap the retained outside rows end in S union S', and retained outside columns start in Z union Z'; the two coordinate families are disjoint and neither meets the forbidden coordinates. If q_i is an individual miss probability and q_ij is a simultaneous miss, Bonferroni bounds the joint all-hit probability by 1-sum q_i+sum q_ij. The independent product is at least 1-sum q_i, which is bounded away from zero. Thus their ratio is at most 1+O(max q_ij); q_ij<=rho^(2ell-h). Multiplying over O(m) blocks gives 1+o(1) uniformly. When deleting O(L) inside-support hit tests, each removed marginal factor is 1-O(L/m), so the ratio cost is 1+o(1). For the unequal-size pair only V-column hits are tested, so ell=b, not a.

For high overlap and small deficit, the geometric inequalities force near-identical independent fibres. Conditional on a fixed first witness, for any specified q coordinates in a block of size n conditioned nonempty, the probability they are all absent is

    rho^q (1-rho^(n-q))/(1-rho^n) <= rho^q.

Distinct blocks stay independent after conditioning on their separate events. Let U be the common independent part of size a-d (or b-d), G the added d vertices, e=|G intersect Z| (or |G intersect A| for the two-stage pair). Of the 2(a-d)d cross coordinates only the (a-d)e incoming coordinates from the already forced missing fibre are absent under the original witness. All the remaining coordinates are fresh or hit-conditioned; thus their joint absence has the claimed upper bound. Counting possible G and removed vertices gives the binomial sum bounded by [a rho^(a-d)(z+m rho^(a-d))]^d, or its pair analogue. Uniformly d=O(log L), rho^(a-d)=poly(L)/m; the geometric base is poly(L)/m. The original independent fibre determines every other counted fibre, so its conditional count is one, not a potentially exponential multiplicity.

Actual finite audit: fixed the first labelling and enumerated every second labelling at five six-vertex size profiles (two triples, one equal-size pair, two unequal-size pairs), 570 pairs total. Direct ordered-coordinate enumeration verified all the deficit, lost-coordinate, and newly required cross-coordinate counts. This tests the geometry, not the asymptotic probabilistic estimates.

## 5. Critical cases and compact phases

Full-sequence vanishing at rho=rho_* requires A.4, with uniform prefactors indexed by a and v=lambda_a/a. A fixed-phase result at a single limiting v does not suffice because the actual phase may approach a zero at an unknown rate. The critical upper bound sums O(log L) terms of order L^(-3/2). For exact fixed phases m_j=round(v j B^j) one instead uses lambda=t j+o(1) and fixed integer offsets. The O(j^-1), O(j^-3/2), and O(j^-1/2) bounds at zero exponent follow by Stirling and geometric binomial tail ratios. For the large-a tail in Appendix D.2 the cutoff K1 is fixed after choosing the fixed phase and offset; it can depend on both, because only finitely many offsets survive the compactness reduction. The tail exponent can exceed the fixed independent-set exponent.

Positive directions keep a fixed positive margin and apply second moments before selecting a witness. Failure probabilities are conditional on a deterministic witness's tested bits; Markov bounds the number of failed completions. No unproved independence is asserted after choosing an arbitrary successful pair. Compactness of the normalized phase in [1,B] then yields full-sequence convergence when all phases are strictly positive. Exact zero phases at the endpoints suffice to show oscillation at the convergence thresholds, not to classify arbitrary sequences approaching them.

## 6. Assessment and remaining gates

No new fatal gap was identified in the reviewed portions of Theorems 4 and 5. The audit is not a proof that no gap exists. The finite checks cannot validate any limit theorem. The two strongest remaining mathematical review tasks are a genuinely independent review of the general degree criterion (including its rate lower bound) and a referee's check of the uniform overlap estimates above.

Literature search reconfirmed the prior kernel variants and nonconvergence in Le Bars (LICS 2002, official abstract https://lics.siglog.org/2002/LeBars-The01lawfailsforfra.html), and the Goranko-Kapron double-kernel result (2003 bibliographic record https://philarchive.org/rec/GORTML, searchable author text at https://www.researchgate.net/publication/2395729_The_Modal_Logic_of_the_Countable_Random_Frame). This search did not establish priority for the exact two targets or the three constants. Schamm's original figure remains unverified. No new Lean or LaTeX compilation is claimed. No merge or submission.
