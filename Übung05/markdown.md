# Übung05

## Aufgabe 1

Die Sprache $L = \{a^p | p \in \mathbb{N}$ ist eine Primzahl $\}$ ist nicht regulär.

Beweis mit Widerspruch:

Sei $L$ regulär $\Rightarrow$ $L$ erfüllt das Pumping-Lemma

$\Rightarrow \exists k \in \mathbb{N}\ s.d$<br>
$w = xyz : |xy| < k \wedge |y| \geq 1\  |\  w \in L$<br>
s.d.: $xy^iz \in L\ \ \ \ \forall i \in \mathbb{N} \cup \{0\}$

i = 0 $\Rightarrow |xz|$ ist prim

Für jedes $l \in \mathbb{N}$ gibt es eine Primzahl $p \geq l+2$

$\Rightarrow$ Setze y s.d |y| = 1<br>
$\Rightarrow xy^1z \notin L$, weil prim+1 ist nicht prim!

$\Rightarrow L\ erfüllt\ nicht\ das\ Pumping-Lemma \Rightarrow L\ ist\ nicht\ regulär!$

## Aufgabe 2

### 1.

$\epsilon,\ a,\ b,\ ab,\ ba,\ aba,\ bab$

### 2.

$G = \{N, T, P, S\}$

$T = \{a, b\}$

$N = \{start, A, B\}$

$P = \{start \rightarrow aA|bB|\epsilon,\ A \rightarrow bB|\epsilon,\ B \rightarrow aA|\epsilon \}$

$S = \{start\}$

### 3.

aba:

$start \rightarrow aA \rightarrow abB \rightarrow abaA \rightarrow aba\epsilon = aba$

bab:

$start \rightarrow bB \rightarrow baA \rightarrow babB \rightarrow bab\epsilon = bab$

### 4.

$L$ ist eine reguläre Sprache, denn es gibt eine reguläre (in dem Fall rechtslineare Grammatik aus Aufgabe 2) Grammatik, die diese Sprache beschreibt.

### 5.

Setze k = 1

y = ab, x = $\epsilon$, z = $\epsilon$

$\Rightarrow$ $xy^iz = (ab)^i \in L$


## Aufgabe 3

### 1.

Erstes Wort: 0 $\wedge$ 1 $\lor$ 0<br>
Zweites Wort: 1 $\wedge$ 0 $\lor$ 1

### 2.

$G' = \{N, T, P, S\}$

$N = \{START, BIN, NULL, OP\}$

$T = \{0, 1, \wedge, \lor\}$

$P = \{START \rightarrow BIN\ 1 | NULL\ 0 | 1 | 0;$ <br> $\ BIN \rightarrow BIN\ 1 | BIN\ 0 |OP\ \lor |OP\ \wedge| \epsilon;$<br>$ NULL \rightarrow OP\ \lor| OP\ \wedge | \epsilon;$<br>$ OP \rightarrow BIN\ 1 | NULL\ 0 \}$

$S = \{START\}$

### 3.

$START \rightarrow NULL\ 0 \rightarrow OP\ \lor 0 \rightarrow BIN\ 1 \lor 0 \rightarrow OP\ \wedge 1 \lor 0 \rightarrow BIN\ 0 \wedge 1 \lor 0 \rightarrow \epsilon\ 0 \wedge 1 \lor 0 \rightarrow 0 \wedge 1 \lor 0$

$START \rightarrow BIN\ 1 \rightarrow OP\ \lor 1 \rightarrow NULL\ 0 \lor 1 \rightarrow OP\ \wedge 0 \lor 1 \rightarrow BIN\ 1 \wedge 0 \lor 1 \rightarrow \epsilon\ 1\  \wedge 0\ \lor 1 \rightarrow 1\ \wedge 0\ \lor 1$

  
