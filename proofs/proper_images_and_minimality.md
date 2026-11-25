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

Let \(E_1\) be the one-point reflexive frame.

A map from any nonempty frame \(G\) to \(E_1\) is the unique constant map. Its forth condition is automatic, and its back condition is exactly seriality:
\[
\forall x\in W_G\;\exists y\;(xR_Gy).
\]
Thus
\[
G\twoheadrightarrow E_1
\quad\Longleftrightarrow\quad
G\text{ is serial}.
\]

In the labelled random model, the \(n\) rows are independent and each row is empty with probability \(2^{-n}\). Hence
\[
\Pr(G_n\twoheadrightarrow E_1)
=(1-2^{-n})^n\longrightarrow1.
\]

## 2. The complete reflexive two-point frame

Let \(T_2\) be the complete reflexive frame on two points.

Fix a deterministic balanced partition
\[
[n]=P\sqcup Q,\qquad
|P|=\lfloor n/2\rfloor,\quad |Q|=\lceil n/2\rceil,
\]
and map \(P,Q\) to the two target points.

The forth condition is automatic because every target edge is present. The back condition holds if and only if every source vertex has at least one outgoing edge into \(P\) and at least one outgoing edge into \(Q\).

For a fixed source vertex, the union bound gives failure probability at most
\[
2^{-|P|}+2^{-|Q|}.
\]
A further union bound over all \(n\) source vertices gives
\[
\Pr(\text{the fixed map is not a bounded morphism})
\leq n(2^{-|P|}+2^{-|Q|})\longrightarrow0.
\]
Therefore
\[
\Pr(G_n\twoheadrightarrow T_2)\longrightarrow1.
\]

## 3. Proper images of \(F_0\) and \(F_1\)

A surjective map from a three-point set to a three-point set is bijective. A bijective bounded morphism is a frame isomorphism. Thus every proper bounded-morphic image of either frame has one or two points.

For \(F_0\), exhaustive analysis of all six surjections onto a two-point set shows that no such bounded morphism exists. Hence its only proper image, up to isomorphism, is \(E_1\).

For \(F_1\), exactly one two-block fibre partition works, up to swapping the two target labels:
\[
\{c\}\mid\{a,b\}.
\]
The quotient target is \(T_2\). The other two two-block partitions fail the back condition. Its proper images, up to isomorphism, are therefore \(T_2\) and \(E_1\).

Since both \(E_1\) and \(T_2\) are almost-sure bounded-morphic images of \(G_n\), their characteristic formulas are not almost-sure frame validities.

Consequently, if the probability theorems
\[
\Pr(G_n\twoheadrightarrow F_0)\to0,
\qquad
\Pr(G_n\twoheadrightarrow F_1)\to0
\]
hold, then \(F_0,F_1\) are minimal among the central-point frames in the bounded-morphic image ordering, in the sense used by Goranko.

## 4. Independence over the countable random-frame logic

Assume the cited finite-frame characterization of the countable random-frame logic:
a finite frame validates \(\mathrm{ML}^r\) exactly when it has a central point.

Both \(F_0\) and \(F_1\) have central point \(c\), so both validate \(\mathrm{ML}^r\).

They are non-isomorphic. Since both have three points, there is no surjective bounded morphism in either direction. By the characteristic-formula correspondence:
\[
F_0\models\chi_{F_1},\quad F_1\models\chi_{F_0},
\]
while
\[
F_0\not\models\chi_{F_0},\quad F_1\not\models\chi_{F_1}.
\]

Thus, subject to the cited characterization and characteristic-formula theorem,
\[
\mathrm{Ax}(\mathrm{ML}^r)\cup\{\chi_{F_0}\}
\not\vdash\chi_{F_1},
\]
and
\[
\mathrm{Ax}(\mathrm{ML}^r)\cup\{\chi_{F_1}\}
\not\vdash\chi_{F_0}.
\]

The two independence claims are therefore reduced to explicit finite semantic facts plus the two asymptotic non-mappability theorems. The latter are not formalized in Lean yet.
