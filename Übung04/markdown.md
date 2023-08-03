# Übung04

## Aufgabe 1


Gelöscht:     

    hee
    hihoo
    ha
    hoooo
    hohi
    hehuuu
    haaaa
    huu
    hee

Nicht-gelöscht: 

    O
    a
    s
    e

Herausgefiltertes Wort: Oase

## Aufgabe 2

Die folgende Sprache ist regulär, denn ich kann den folgenden Automaten konstruieren, der die Sprache akzeptiert.

A = ($\Sigma$, $Q$, $q_0$, $F$, $\delta$)

$\Sigma$ = {0,1,2,3,4,5,6,7,8,9}

$Q$ = {start, zero, one, two}

$q_0$ = start

$F$ = {zero}

$\delta$ : $Q$ $\times$ $\Sigma$ $\rightarrow$ $Q$


| $p$ $\in$ $Q$ | $\delta(p, z_1)$ : $z_1 \in$ {0,3,6,9} | $\delta(p, z_2)$ : $z_2 \in$ {1,4,7} |  $\delta(p, z_3)$ : $z_3 \in$ {2,5,8} |
|:---|:---|:---|:---|
| start | zero | one | two |
| zero | zero | one | two |
| one | one | two | zero |
| two | two | zero | one |


## Aufgabe 3

### gegeben:

$A = \{\Sigma, Q, q_0, F, \Delta\}$

$\Sigma = $ {a,b}

$Q = \{q_0, q_1, q_2, q_3\}$

$q_0 = \{q_0\}$

$F = \{q_1\}$

$\Delta : Q \times \Sigma \rightarrow U | U \subseteq Q$

| $p \in Q$ | $\Delta(p, a)$ | $\Delta(p, b)$ |
|---|---|---|
| $q_0$ | ${q_0, q_1}$ | ${q_1}$ |
| $q_1$ | $\emptyset$ | ${q_2}$ |
| $q_2$ | $\emptyset$ | ${q_1, q_3}$ |
| $q_3$ | ${q_0}$ | $\emptyset$ |


### Deterministischer Endlicher Automat

$B = \{\Sigma, Q, q_0, F, \delta\}$

$\Sigma = $ {a,b} 

$Q = $ {$\{q_0\}$, $\{q_1\}$, $\{q_2\}$, $\{q_3\}$, $\{q_0, q_1\}$, $\{q_1, q_3\}$, $\{q_1, q_2\}$, $\{q_2, q_3\}$, $\{q_0, q_1, q_3\}$, $\{q_0, q_1, q_2\}$ , $\{q_1, q_2, q_3\}$, error }

$q_0 = \{\{q_0\}\}$

$F = $ {$\{q_1\}$, $\{q_0, q_1\}$, $\{q_1, q_3\}$, $\{q_1, q_2\}$, $\{q_0, q_1, q_3\}$, $\{q_0, q_1, q_2\}$, $\{q_1, q_2, q_3\}$ }


$\delta : Q \times \Sigma \rightarrow Q$

| $p \in Q$ | $\Delta(p, a)$ | $\Delta(p, b)$ |
|---|---|---|
| ${q_0}$ | ${q_0, q_1}$ | ${q_1}$ |
| ${q_1}$ | error | ${q_2}$ |
| ${q_2}$ | error | ${q_1, q_3}$ |
| ${q_3}$ | ${q_0}$ | error |
| ${q_0, q_1}$ | ${q_0, q_1}$ | ${q_1, q_2}$ |
| ${q_1, q_3}$ | ${q_0}$ | ${q_2}$ |
| ${q_1, q_2}$ | error | ${q_2, q_3}$ |
| ${q_2, q_3}$ | ${q_0}$ | ${q_0, q_1, q_3}$ |
| ${q_0, q_1, q_3}$ | ${q_0, q_1}$ | ${q_0, q_1, q_2}$ |
| ${q_0, q_1, q_2}$ | ${q_0, q_1}$ | ${q_1, q_2, q_3}$ |
| ${q_1, q_2, q_3}$ | ${q_0}$ | ${q_2, q_3}$ |
| error | error | error |


## Aufgabe 4

Automat, der $L_1 \cap L_2$ akzeptiert

$A = \{\Sigma, Q, q_0, F, \delta\}$

$\Sigma = \{\sigma \in \Sigma : \sigma \in \Sigma(L_1) \cup \Sigma(L_2)\}$

$Q = Q(L_1) \times Q(L_2)$

$q_0 = $ Vereine die Startzustände $q_1$ und $q_2$ zu einem Zustand

$\delta$ = $\delta1 \times \delta2$

$F = F(L_1) \times F(L_2)$


Beweis, den ich präferiere:

$L_1 \cap L_2$ = $\overline{\overline{L_1} \cup \overline{L_2}}$

Da Komplement und Vereinigung jeweils Reguläre Sprachen darstellen -> ist der Durchschnitt zweier Regulären Sprachen wiederum eine Reguläre Sprache.