# Theoretical background: \(ML^r\), \(ML^{as}\), and minimal characteristic frames

## Primary reference

Valentin Goranko, “The Modal Logic of Almost Sure Frame Validities in the Finite,” *Proceedings of the 13th Conference on Advances in Modal Logic* (AiML 2020), pp. 249–268.

- [Author-hosted final draft](https://titan.dcs.bbk.ac.uk/volumes/volume13/Goranko.pdf)
- [AiML volume page](https://www.aiml.net/volumes/volume13/)

The paper fixes the same labelled random-frame model used here: on an n-element labelled domain, every ordered pair is independently made an edge with probability 1/2 (pp. 250, 256–257).

## 1. Characteristic formulas and bounded morphisms

Goranko defines a surjective bounded morphism (p-morphism) by the forth and back conditions. For a finite frame F, the characteristic formula \(\chi_F\) is built using the universal modality. Lemma 2.3 states:

\[
G\twoheadrightarrow F
\quad\Longleftrightarrow\quad
G\not\models\chi_F.
\]

Thus, in the labelled random model,

\[
\mu_n(\chi_F)=1-\Pr(G_n\twoheadrightarrow F).
\]

This is the key bridge from our probability estimates to almost-sure modal validity. The exact language matters: the displayed characteristic formula uses the universal modality; the paper also discusses translation to the basic modal language.

## 2. Why central-point frames are the right targets

Proposition 3.5 states that, for a finite frame F, the following are equivalent:

- F validates \(ML^r\), the logic of the countable random frame;
- F has a central point, i.e. a point related in both directions to every point, including itself;
- F is a bounded-morphic image of the countable random frame.

Both F0001 and F1001 have central point c. Hence both validate \(ML^r\).

Corollary 3.6 and the surrounding discussion identify characteristic formulas of central-point frames as natural candidates for additional axioms of \(ML^{as}\), the logic of almost-sure frame validities in the finite.

## 3. The precise minimality criterion

In Section 4.2, Goranko defines the candidate set
\[
\Xi^{as}=\{\chi_F:F\text{ has a central point and }\chi_F\in ML^{as}\}.
\]

He then says it suffices to identify the *minimal* such frames F: there must be no proper bounded-morphic image F' which also has a central point and whose characteristic formula \(\chi_{F'}\) is in \(ML^{as}\). Equivalently, the preimage class of F must have asymptotic measure zero.

This is the notion relevant to our project. It is **not** minimality among all central-point frames. A target may have proper central-point images and still be minimal for \(\Xi^{as}\), provided those smaller images are almost-sure images of the random finite frame and therefore their characteristic formulas are not in \(ML^{as}\).

## 4. How F0001 and F1001 fit

The finite quotient audit gives:

| Target | Proper bounded-morphic images, up to isomorphism |
|---|---|
| F0001 | E1 only |
| F1001 | T2 and E1 |

The singleton E1 is an almost-sure image because
\[
\Pr(G_n\twoheadrightarrow E1)=(1-2^{-n})^n\to1.
\]

The complete reflexive two-point frame T2 is also an almost-sure image: fix a deterministic balanced partition of [n] into two fibres; with probability tending to one every source vertex has an outgoing edge into each fibre, which is exactly the back condition for the constant-on-fibres map.

Therefore \(\chi_{E1}\) and \(\chi_{T2}\) are not in \(ML^{as}\). If the two first-moment drafts establish
\[
\Pr(G_n\twoheadrightarrow F0001)\to0,
\qquad
\Pr(G_n\twoheadrightarrow F1001)\to0,
\]
then \(\chi_{F0001},\chi_{F1001}\in ML^{as}\). Together with centrality and the proper-image classification, this makes F0001 and F1001 candidates for minimal frames in Goranko's precise sense.

The probability limits are still hand-proof claims, not Lean-verified results. Bibliographic novelty also remains to be checked.

## 5. Independence over \(ML^r\)

The two targets are non-isomorphic three-point frames. A surjective bounded morphism between two three-point frames would be bijective and hence an isomorphism, so there is no such map in either direction.

By Lemma 2.3, each target validates the other's characteristic formula but fails its own. Since both targets validate \(ML^r\), they provide opposite countermodels to derivability:
\[
ML^r+\chi_{F0001}\nvdash\chi_{F1001},
\qquad
ML^r+\chi_{F1001}\nvdash\chi_{F0001}.
\]
This independence statement is conditional on the characteristic formulas being interpreted in the precise language of the theorem and on the target frames' membership in the base logic, which Proposition 3.5 supplies.

## 6. Existing benchmark examples

Goranko's paper discusses K2 and K3 (the single-kernel and double-kernel frames) and proves that the double-kernel characteristic formula is almost surely valid; the single-kernel case was subsequently proved by Le Bars. It also gives an infinite family of minimal candidate frames in Proposition 4.7. Our two matrices should be compared explicitly with those examples before making a novelty claim.

## Page guide

- pp. 254–255: bounded morphisms and Lemma 2.3 (characteristic formula).
- pp. 256–257: labelled random-frame probability model and almost-sure validity.
- pp. 261–262: Proposition 3.5 (finite frames of \(ML^r\) are exactly central-point frames); Corollary 3.6; Theorem 3.7.
- pp. 263–265: characterization of additional axioms and the minimality criterion in Section 4.2.
