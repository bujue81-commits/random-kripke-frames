# Forbidden-degree criterion for central frames

Internal hand proof, not Lean-verified, independently refereed or novelty-checked. Fix independent ordered-edge probability theta in (0,1) including loops; rho=1-theta, B=1/rho, L=log_B m, b=L-log_B L.

## Theorem

Let F have universal reflexive center c and r>=1 peripheral vertices. Write A_ij=1 for a missing ordered arrow i->j among peripherals and 0 otherwise; q=sum A_ij, d=q-r. Assume (i) every peripheral column of A has a 1 (c is the only universal incoming column), and (ii) each peripheral missing-edge incidence degree g_i=sum_j(A_ij+A_ji) is at least 2, counting missing loops twice. Then d>=0 and

    log_B P(G_m ->> F) = -d*b^2 + O_{F,theta}(L).

When d=0, additionally P(G_m ->> F)=O(L^(-r/2)), so all these targets have vanishing image probability. The logarithmic equality is for existence probability, not a claim about the unrestricted first moment (exceptional frames can have many maps). This extends the earlier loopless results to some looped targets. Conditions are sufficient, not necessary.

## 1. Exclude tiny peripheral fibres with a frame-level estimate

Choose a fixed C=8(r+1)^2 and h=ceil(C L). With probability at least 1-B^{2hL-h^2}, no ordered pair of h-element subsets has its entire rectangular edge block absent: there are at most m^{2h} pairs and each rectangle has h^2 independent coordinates, even when the subsets overlap. Thus in any successful partition the labels U of fibres of size >=h induce a complete reflexive relation. Let S be the other labels. U is nonempty for large m. There are at most 2^(r+1) * (h+1)^(r+1) * m^((r+1)h) possible choices of S and its disjoint small fibres (each nonempty, size <h); this is B^{O(L^2)}.

Put b0=L-3 log_B L. Suppose a peripheral label i has fibre size a_i<b0, so i is in S. For a fixed choice of small fibres, consider an outside vertex x with no outgoing edge to fibre i, at least one outgoing edge to every other S-fibre, and at least one incoming edge from every S-fibre. These tests use disjoint edge blocks, since x is outside the union of small fibres; their probability is >=rho^a_i * theta^(2|S|-1). Tests for distinct outside vertices use disjoint coordinates. Such an x would have to map to some u in U, with incoming arrows from all S labels by forth and from all U labels because U is complete. Therefore u=c by (i). But x misses i, impossible by back since c->i. Hence no outside vertex can pass the test. Its probability is <=exp(-c0*m*rho^a_i)<=exp(-c0*L^3), where c0>0 depends on theta,r (there are m-O(L) outside vertices). Union over small-fibre choices and i gives exp(-Omega(L^3)). Together with the rectangle failure probability this shows that existence via a tiny peripheral fibre has probability at most

    B^{2hL-h^2}+exp(-Omega(L^3)).

The first term has quadratic exponent more negative than -d L^2 by the choice of C. This argument does not assume adaptive partitions are independent.

## 2. Upper bound on the remaining existence event

For peripheral sizes a_i>=b0 and central size a_c=m-T>0, T=sum a_i, put Q(a)=sum A_ij a_i a_j. The full-map probability is rho^Q times required-hit factors; in particular at most rho^Q * prod_i(1-rho^a_i)^a_c. The multinomial count is at most m^T. Write a_i=b0+z_i, z_i>=0. Since A is nonnegative,

    Q >= q*b0^2 + b0*sum_i g_i z_i >= q*b0^2+2*b0*sum_i z_i.

Thus the log_B of the selected size-vector summand is <=

    -q*b0^2 + r*b0*L - (2*b0-L)*(T-r*b0).

For T>C L the last term is <=-L*(T-r*b0)/2; summing at most m^r vectors makes this tail B^{-d L^2-Omega(L^2)} (using b0=L-O(log L), C>r). This holds regardless of the size of the central fibre.

For T<=C L, a_c>=m/2 and ln(k!)>=k ln k-k imply log_B multinomial <= b*T+O(L). Define P(x)=sum A_ij x_i x_j-b sum x_i; at (b,...,b), P=d b^2. On x_i>=b0 its partial derivatives are >=g_i*b0-b>=2*b0-b>0. Clip each coordinate upwards to at least b; on these segments the derivatives are <=2(C+r)L. With delta_i=(b-a_i)_+ this gives

    P(a)>=d*b^2-2(C+r)L sum_i delta_i.

The central hit log is <=-L/(2 ln B) times sum of B^delta_i over a_i<b. Since K*delta-B^delta/(2 ln B) is bounded above for delta>=0 and fixed K, each main summand has log_B <=-d*b^2+O(L). There are O(L^r) such vectors. Markov restricted to these sizes, and the frame-level exceptional bound of section 1, prove the desired existence upper bound. No claim about unrestricted expectation is needed.

## 3. Balanced-map second moment

Take a=ceil(b) and balanced peripheral fibres of size a, total support t=ra. Number of maps N=(m)_t/(a!)^r has log_B N=r*b^2+O(L); Q=q*a^2=q*b^2+O(L). Full success for each map has probability >=c_m rho^Q with c_m=exp(-2(r+1)L), since every required hit block has size >=a, at most (r+1)m blocks exist, and rho^a<=L/m.

For two balanced maps f,g let k_i count vertices of f-fibre i outside g's peripheral support, k=sum k_i. Each forbidden rectangle i->j loses a^2-(a-k_i)(a-k_j)>=a*(k_i+k_j)/2 coordinates on restriction to g's support, including i=j (then this is a^2-(a-k_i)^2>=a*k_i). These rectangles are disjoint. The lost coordinates cannot be in g's forbidden set. Hence |H_f intersect H_g|<=Q-(a/2)sum_i g_i k_i<=Q-a*k. Joint success probability <=rho^{Q+a*k}. For fixed f there are at most binom(t,k)binom(m-t,k)r^t maps with that support difference. Retaining k! gives

    sum_g P(f,g both succeed) <=rho^Q (2r)^t exp(m*rho^a)
                               <=rho^Q (2r)^t exp(L).

For Y counting successful balanced maps, E[Y]>=c_m N rho^Q, E[Y^2]<=N rho^Q (2r)^t exp(L). Cauchy-Schwarz yields P(Y>0)>=c_m^2 N rho^Q (2r)^(-t) exp(-L). Its log_B is at least -d*b^2-O(L), as required.

## 4. Critical d=0

Each column has >=1 missing arrow and q=r, so every column has exactly one. Degree>=2 then forces exactly one missing arrow per row. A is a permutation matrix; write sigma(i) for the unique forbidden destination of row i. On main sizes b0<=a_i, T<=C L, let lambda_j=m rho^a_j. The selected first-moment summand is bounded by

    exp(T sum_j rho^a_j) * prod_i pi_{lambda_{sigma(i)}}(a_i),

where pi_lambda(k)=exp(-lambda) lambda^k/k!. The correction is 1+o(1) uniformly, because T=O(L) and rho^a_j<=L^3/m. This product uses that sigma is a permutation. Stirling gives pi_{t k}(k)<=K k^(-1/2) exp[-k(t-1-ln t)]. If any normalized mean lambda_sigma(i)/a_i is outside [1/2,2], its rate function is uniformly positive, so these O(L^r) vectors contribute exponentially little. Otherwise all a_i in [L/2,CL] imply lambda_j is between L/4 and 2CL, so a_j=b+O(1) for all j. Only O(1) integer vectors remain, each contributing O(L^(-r/2)). All exceptional and large-support bounds above are negligible. This proves the critical upper bound, not a matching lower bound of logarithmic-power order.

## 5. Four-point application

The previous census left 28 canonical peripheral matrices unresolved. Exactly 11 meet (i),(ii); list with d=q-3:

    000010100 4
    000010101 3
    000011100 3
    000011101 2
    001010010 3
    001010011 2
    001100011 2
    001110001 2
    001110011 1
    100011101 1
    101110011 0

The ten positive-d cases have matching first two logarithmic existence coefficients -d,+2d; the last has critical O(L^(-3/2)) upper bound. All eleven have no proper vanishing central quotient by the earlier census of all smaller targets, so they are minimal in Goranko's sense, conditional on the internal hand proofs. Together with C3 there are at least 12 minimal four-point types. Of 104 four-point types, 82 now have limit zero, 5 limit one, 17 remain unresolved. These counts use canonical simultaneous peripheral row/column permutations. No assertion that the 12 are all minimal four-point types, or that the whole almost-sure logic is axiomatized. Priority and independent review pending; CI remains unverified.
