# Universal-column signature criterion

Internal hand proof, not Lean-verified or novelty-checked. Fix a finite nonempty target F and fixed edge probability theta in (0,1), with independent ordered edges (including loops) on m labelled vertices.

## Theorem (sufficient condition for exponentially high probability)

Partition target vertices into nonempty U and possibly empty S. Assume:

1. Every target vertex has an arrow to every vertex of U (universal incoming columns).
2. For every subset J of S, there is at least one u in U whose set of successors in S is exactly J.

Then for some c>0 and all sufficiently large m,

    P(G_m has no surjective bounded morphism onto F) <= exp(-c*m).

The constant may depend on F and theta. The condition is sufficient, not asserted necessary. No restriction on the induced relation on S is needed. If F is central, take U to include the designated center. Condition 2 implies |U|>=2^|S|.

## Proof

Write s=|S| and t=|U|. If s=0, F is complete reflexive. A fixed balanced t-block partition fails back with probability <=tm(1-theta)^floor(m/t), while forth is automatic.

If s>=1, reserve a deterministic set W of floor(m/2) source vertices. Split W into floor(|W|/s) disjoint ordered s-tuples, discarding leftovers. A tuple realizes exactly the induced relation on S when its s^2 ordered coordinates, including loops, match that relation. Each tuple succeeds with constant probability

    gamma=theta^e*(1-theta)^(s^2-e)>0,

where e is the number of arrows in S. The tests on disjoint tuples are independent. Select the first successful tuple, one vertex v_j per j in S. Failure probability <=(1-gamma)^floor(|W|/s)=exp(-Omega(m)). All information in this selection is measurable in the sigma-field H of edges ending in W.

Use v_j as the singleton fibre of j. For every vertex x not selected, define its signature J(x)={j in S: x->v_j}. For each J, the nonempty set U_J consists of those u in U with exactly this successor signature. Partition the vertices having signature J among the labels in U_J, as evenly as possible outside W; distribute inside-W vertices of that signature by any deterministic rule. On success of tuple selection, all vertices outside W have independent signatures, each with constant probability

    pi_J=theta^|J|*(1-theta)^(s-|J|)>0,

conditional on the tuple tests, since those tests use only coordinates inside W. A binomial Chernoff bound and finite union bound give, except with probability exp(-Omega(m)), at least (m-|W|)*pi_J/2 outside-W vertices of every signature. Therefore for some alpha>0 all U-fibres have at least alpha*m outside-W vertices for large m. All classification and size events are H-measurable (even though outside-W row signatures were exposed, their destinations lie inside W).

The edges ending outside W are mutually independent and independent of H. Conditional on any successful history with the size bounds, each source row misses the outside-W portion of any U-fibre with probability <=(1-theta)^(alpha*m). A union bound over mt row/fibre pairs gives exp(-Omega(m)) conditional failure probability. Hence every row hits every U-fibre. This matches all target arrows into U. Edges into singleton S-fibres match target successor signatures for unselected rows by construction, and for selected rows by the induced-relation test. Thus all row successor images are exactly the target rows, giving forth and back; every fibre is nonempty. Combine the three exponential failure bounds, decreasing c if needed.

## Four-point application

For central four-point targets, write the nine peripheral relation bits in row-major order, canonical under peripheral permutation. Applying the criterion to all 34 types not ruled out by earlier smaller vanishing quotients gives five successes:

    011011011, 011011111, 101111101, 101111111, 111111111.

The last is complete and already known. Each of the other four has one nonuniversal incoming column, put that vertex in S and the three other vertices in U. The U rows realize both signatures on S. These four new types have failure probability exponentially small in m.

The finite census: 104 isomorphism types; 70 vanish because of a smaller vanishing quotient, C3=001100010 vanishes by the loopless theorem, five types succeed exponentially by this criterion, and 28 remain unclassified by these arguments. Counts in labelled matrices are 339, 2, 19, 152 respectively. Distinguish the criterion from a necessary condition or a complete four-point classification.

## Research scope

The proof uses singleton rare fibres rather than the logarithmic reserve construction of the earlier three-point proof. It handles arbitrary fixed internal S relations, including loops. It strengthens the earlier four positive three-point cases to exponential failure bounds. For fixed targets satisfying the criterion, no almost-sure characteristic formula excludes them. The argument makes no claim about arbitrary modal formulas, varying theta or literature priority. No recent Lean CI results available.
