# Proper bounded-morphic images and minimality

This note records the elementary finite quotient analysis for
\[
F_0:\quad
\begin{pmatrix}1&1&1\\1&0&0\\1&0&1\end{pmatrix},
\qquad
F_1:\quad
\begin{pmatrix}1&1&1\\1&1&0\\1&0&1\end{pmatrix}.
\]
The vertex order is \((c,a,b)\).

## 1. The singleton frame

Let \(E_1\) be the one-point reflexive frame. A map from a nonempty frame \(G\) to \(E_1\) is the unique constant map. Its forth condition is automatic, and its back condition is exactly seriality:
\[
G\twoheadrightarrow E_1
\quad\Longleftrightarrow\quad
G\text{ is serial}.
\]

In the labelled random model, the \(n\) rows are independent and each row is empty with probability \(2^{-n}\). Hence
\[
\Pr(G_n\twoheadrightarrow E_1)=(1-2^{-n})^n\longrightarrow1.
\]

## 2. The complete reflexive two-point frame

Let \(T_2\) be the complete reflexive frame on two points. Fix a deterministic balanced partition
\[
[n]=P\sqcup Q,\qquad |P|=\lfloor n/2\rfloor,\quad |Q|=\lceil n/2\rceil,
\]
and map P,Q to the two target points.

The forth condition is automatic. The back condition holds exactly when every source vertex has at least one outgoing edge into P and at least one outgoing edge into Q. By a union bound,
\[
\Pr(\text{the fixed map fails})
\leq n(2^{-|P|}+2^{-|Q|})\longrightarrow0.
\]
Therefore
\[
\Pr(G_n\twoheadrightarrow T_2)\longrightarrow1.
\]

## 3. Proper images of F0 and F1

A surjective map from a three-point set to a three-point set is bijective; a bijective bounded morphism is an isomorphism. Thus every proper bounded-morphic image has one or two points.

For F0, no two-point bounded-morphic image exists. Its only proper image up to isomorphism is E1.

For F1, the only two-point fibre partition that works, up to target-label swap, is
\[
\{c\}\mid\{a,b\}.
\]
Its quotient is T2. The other two partitions fail the back condition. Its proper images up to isomorphism are T2 and E1.

## 4. Correct minimality statement

Assume the two asymptotic claims
\[
\Pr(G_n\twoheadrightarrow F_0)\to0,
\qquad
\Pr(G_n\twoheadrightarrow F_1)\to0
\]
are proved. Then the corresponding characteristic formulas are almost-surely frame valid.

Every proper bounded-morphic image of F0 or F1 is E1 or T2. But E1 and T2 are themselves almost-sure bounded-morphic images of G_n, so their characteristic formulas are not almost-surely frame valid.

Thus F0 and F1 are minimal, in the bounded-morphic image ordering, among finite frames whose characteristic formulas are almost-surely frame valid. This is not minimality among all central-point frames: E1 and T2 themselves have central points.

## 5. Conditional independence over ML^r

Assume the finite-frame characterization that a finite frame validates ML^r exactly when it has a central point, together with the appropriate Jankov–Fine correspondence.

Both F0 and F1 have central point c, so both validate ML^r. They are non-isomorphic and have the same finite cardinality, so there is no surjective bounded morphism in either direction. Hence
\[
F_0\models\chi_{F_1},\quad F_1\models\chi_{F_0},
\]
while
\[
F_0\not\models\chi_{F_0},\quad F_1\not\models\chi_{F_1}.
\]

Therefore F1 is a countermodel to deriving \(\chi_{F_1}\) from the ML^r axioms together with \(\chi_{F_0}\), and F0 is a countermodel in the reverse direction. The two characteristic formulas are independent over ML^r, conditional on the stated logic theorems.

The probability estimates remain hand-proof drafts and are not formalized in Lean.
