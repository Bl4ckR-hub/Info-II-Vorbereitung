# Übung06

## Aufgabe 1

### 1.

$FIRST(program) = FIRST(stmtList) = \{\epsilon,\ FIRST(stmt\ stmtList)\} = \{id\ :=,\ \epsilon\}$

$FIRST(stmtList) = \{id,\ \epsilon\}$

$FIRST(stmt) = \{id\}$

$FIRST(expr) = FIRST(term\ termTail) = \{FIRST(factor\ factorTail),\ FIRST(factor\ factorTail\ addOp\ term\ termTail)\}$  = $\{$\($, id\}$

$FIRST(termTail) = \{\epsilon,\ FIRST(addOP\ term\ termTail)\} = \{\epsilon,\ +,\ -\}$

$FIRST(term) = FIRST(factor factorTail) = \{$\($,\ id\}$

$FIRST(factorTail) = \{\epsilon,\ FIRST(multOp\ factor\ factorTail)\} = \{\epsilon,\ *,\ /\}$

$FIRST(factor) = \{$\($,\ id\}$

$FIRST(addOp) = \{+,\ -\}$

$FIRST(multOp) = \{*,\ /\}$

### 2.

$FOLLOW(program) = §§$

$FOLLOW(stmtList) = §§$

$FOLLOW(stmt) = \{id, §§\}$

$FOLLOW(expr) = \{id, $\), $§§\}$

$FOLLOW(termTail) = \{§§,\ +,\ -\}$

$FOLLOW(term) = \{§§,\ +,\ -\}$

$FOLLOW(factorTail) = \{§§,\ *,\ /\}$

$FOLLOW(factor) = \{§§,\ *,\ /\}$

$FOLLOW(addOp) = \{$\(, $id\}$

$FOLLOW(multOp) = \{$\(, $id\}$

### 3.

| | id | ( | ) | := | + | - | * | / | §§ |
|-|-|-|-|-|-|-|-|-|-|
|program| $program \rightarrow stmtList$ | | | | | | | $program \rightarrow stmtList$ |
|stmtList| $stmtList \rightarrow stmt\ stmtList$ | | | | | | | $stmtList \rightarrow \epsilon$ |
|stmt| $stmt \rightarrow id\ :=\ expr$ | | | | | | |
|expr| $expr \rightarrow term\ termTail$ | $expr \rightarrow term\ termTail$ |
|termTail| | | | | $termTail \rightarrow addOp\ term\ termTail$ | $termTail \rightarrow addOp\ term\ termTail$ | | | $termTail \rightarrow \epsilon$ | 
|term| $term \rightarrow factor\ factorTail$ | $term \rightarrow factor\ factorTail$ | 
|factorTail| | | | | | | $factorTail \rightarrow multOp\ factor\ factorTail$ | $factorTail \rightarrow multOp\ factor\ factorTail$ | $factorTail \rightarrow \epsilon$ | 
|factor| $factor \rightarrow id$ | $factor \rightarrow (\ expr\ )$ |
|addOp| | | | | $addOp \rightarrow +$ | $addOp \rightarrow -$ |
|multOp| | | | | | | $multOp \rightarrow *$ | $multOp \rightarrow /$ |


## Aufgabe 2

### 1.

$G = (N, T, P, S)$

$N = \{<1>,\ <2>,\ <3>,\ <4>\}$

$T = \{0,\ 1,\ \neg,\ \lor,\ \wedge\}$

$P = \{<1> \Rightarrow <2>;$<br>$<2> \Rightarrow <3>\ <4>;$<br>$<3> \Rightarrow 0\ |\ 1\ |\ \neg\ <2>;$<br>$<4> \Rightarrow \epsilon\ |\ \lor\ <3>\ <4>\ |\ \wedge\ <3>\ <4>\}$

$S = \{<1>\}$

### 2.

| Abgearbeitete Eingabe | Abarbeitungsstapel | Restliche Eingabe |
|-|-|-|
| |$<1>\ \gamma{_0}$| $\neg 0 \lor 0 \wedge 1 \lor \neg 1 §§$ |
| |$<2>\ \gamma{_0}$| $\neg 0 \lor 0 \wedge 1 \lor \neg 1 §§$ |
| |$<3>\ <4>\ \gamma{_0}$ | $\neg 0 \lor 0 \wedge 1 \lor \neg 1 §§$ |
| |$\neg\ <2>\ <4>\ \gamma{_0}$ | $\neg 0 \lor 0 \wedge 1 \lor \neg 1 §§$ |
|$\neg$|$<2>\ <4>\ \gamma{_0}$ | $0 \lor 0 \wedge 1 \lor \neg 1 §§$ |
|$\neg$|$<3>\ <4>\ <4>\ \gamma{_0}$ | $0 \lor 0 \wedge 1 \lor \neg 1 §§$ |
|$\neg$|$0\ <4>\ <4>\ \gamma{_0}$ | $0 \lor 0 \wedge 1 \lor \neg 1 §§$ |
|$\neg 0$|$<4>\ <4>\ \gamma{_0}$ | $\lor 0 \wedge 1 \lor \neg 1 §§$ |
|$\neg 0$|$\lor\ <3>\ <4>\ <4>\ \gamma{_0}$ | $\lor 0 \wedge 1 \lor \neg 1 §§$ |
|$\neg 0 \lor$|$<3>\ <4>\ <4>\ \gamma{_0}$ | $0 \wedge 1 \lor \neg 1 §§$ |
|$\neg 0 \lor$|$0\ <4>\ <4>\ \gamma{_0}$ | $0 \wedge 1 \lor \neg 1 §§$ |
|$\neg 0 \lor 0$|$<4>\ <4>\ \gamma{_0}$ | $\wedge 1 \lor \neg 1 §§$ |
|$\neg 0 \lor 0$|$\wedge\ <3>\ <4>\ <4>\ \gamma{_0}$ | $\wedge 1 \lor \neg 1 §§$ |
|$\neg 0 \lor 0 \wedge$|$<3>\ <4>\ <4>\ \gamma{_0}$ | $1 \lor \neg 1 §§$ |
|$\neg 0 \lor 0 \wedge$|$1\ <4>\ <4>\ \gamma{_0}$ | $1 \lor \neg 1 §§$ |
|$\neg 0 \lor 0 \wedge 1$|$<4>\ <4>\ \gamma{_0}$ | $\lor \neg 1 §§$ |
|$\neg 0 \lor 0 \wedge 1$|$\lor\ <3>\ <4>\ <4>\ \gamma{_0}$ | $\lor \neg 1 §§$ |
|$\neg 0 \lor 0 \wedge 1 \lor$|$<3>\ <4>\ <4>\ \gamma{_0}$ | $\neg 1 §§$ |
|$\neg 0 \lor 0 \wedge 1 \lor$|$\neg\ <2>\ <4>\ <4>\ \gamma{_0}$ | $\neg 1 §§$ |
|$\neg 0 \lor 0 \wedge 1 \lor \neg$|$<2>\ <4>\ <4>\ \gamma{_0}$ | $1 §§$ |
|$\neg 0 \lor 0 \wedge 1 \lor \neg$|$<3>\ <4>\ <4>\ <4>\ \gamma{_0}$ | $1 §§$ |
|$\neg 0 \lor 0 \wedge 1 \lor \neg$|$1\ <4>\ <4>\ <4>\ \gamma{_0}$ | $1 §§$ |
|$\neg 0 \lor 0 \wedge 1 \lor \neg 1$|$<4>\ <4>\ <4>\ \gamma{_0}$ | $§§$ |
|$\neg 0 \lor 0 \wedge 1 \lor \neg 1$|$\epsilon\ <4>\ <4>\ \gamma{_0}$ | $§§$ |
|$\neg 0 \lor 0 \wedge 1 \lor \neg 1$|$<4>\ <4>\ \gamma{_0}$ | $§§$ |
|$\neg 0 \lor 0 \wedge 1 \lor \neg 1$|$\epsilon\ <4>\ \gamma{_0}$ | $§§$ |
|$\neg 0 \lor 0 \wedge 1 \lor \neg 1$|$<4>\ \gamma{_0}$ | $§§$ |
|$\neg 0 \lor 0 \wedge 1 \lor \neg 1$|$\epsilon\ \gamma{_0}$ | $§§$ |
|$\neg 0 \lor 0 \wedge 1 \lor \neg 1$|$\gamma{_0}$ | $§§$ |

Match!


## Aufgabe 3

$P' = \{product \rightarrow factor;$<br>$factor \rightarrow id\ factorid;$<br>$factorid \rightarrow *\ factor\ |\ \epsilon;$<br>$sum \rightarrow id\ +\ sumList;$ <br> $sumList \rightarrow sum\ |\ (product) \}$