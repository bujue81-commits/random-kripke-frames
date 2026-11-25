# Three-point central existence limits (hand proof)

Fix theta in (0,1), rho=1-theta, L=log_{1/rho} m. Independent ordered edges include loops. Target c is reflexive and bidirectionally universal; peripheral bits in order aa,ab,ba,bb.

Limit one: 0101,1010,1011,1101,1111. Limit zero: 0000,0001,0010,0011,0100,0110,0111,1000,1001,1100,1110. No novelty or Lean verification claim.

Neither cross arrow: apply TWO_PERIPHERAL_RECIPROCAL_GAP.md. Both peripheral loops absent: apply LOOPLESS_CENTRAL_BIASED_RATE.md. Their union gives seven vanishing cases. In 0011,0111,1100,1110 a loopless vertex receives arrows from both other vertices. Collapse the other two to the reflexive central vertex of the two-point frame K (all edges except the peripheral loop). Successor images show this is a surjective bounded morphism. By composition p(F)<=p(K)=O(L^(-1/2)) from the r=1 critical loopless theorem.

For 1111 a fixed balanced partition succeeds with failure probability <=3m rho^floor(m/3).

For the other four positive cases, relabel peripherals A,B so A->B is the only missing cross arrow and A has a loop. B may or may not have a loop. Choose a deterministic reserve W of floor(sqrt(m)) vertices and h=floor(L/8). If B is looped, choose a fixed h-subset T of W; every row in T hits T except with probability <=h rho^h. If B is loopless, partition W into h groups of size >=floor(|W|/h). Sequentially choose a candidate from each group with absent loop and absent edges in both directions to previously chosen vertices. Conditional on past tests these coordinates are fresh, disjoint across candidates, and the success probability per candidate is >=rho^(2h)>=m^(-1/4). Union bound gives failure <=h exp(-floor(|W|/h)*m^(-1/4))=o(1).

Set B=T. Assign each x outside T to A iff x has no edge into T, otherwise C. Outside W, the size of A is Bin(m-|W|,rho^h) conditional on successful selection; rho^h is between m^(-1/8) and rho^(-1)m^(-1/8). Chebyshev and Markov give |A minus W|>=m^(7/8)/4 and |C minus W|>=m/2 with probability 1-o(1).

All selection and classification information is measurable with respect to edges ending in W. Edges ending outside W are independent of this sigma-field. Conditional on the size bounds, the probability that any row misses A minus W or C minus W is <=m(rho^(m^(7/8)/4)+rho^(m/2))=o(1). Therefore every row hits A,C, and its B-hit status is already exactly as required. This is a surjective bounded morphism by equality of successor images. Thus the four patterns with a single missing cross arrow whose source is looped have limit one.

All 16 are covered. This classifies existence limits only, not full almost-sure modal logic or sharp rates for every case. Schamm already examined the family; literature priority and independent review pending. Recent CI unavailable; no new Lean claim.
