# Übung08

## Aufgabe 1

$\forall X : ((P(X) \Rightarrow (\forall S:(\exists R: ((Q(f(R), T) \wedge Q(S,R)) \lor O(T)))))) \Leftrightarrow$<br>
$\forall X : ((P(X) \Rightarrow (\forall S:(\exists R: ((Q(R-1, T) \wedge Q(S,R)) \lor O(T)))))) \Leftrightarrow$<br>
$\forall X : (X \leq 0 \Rightarrow (\forall S:(\exists R: ((Q(R-1, T) \wedge Q(S,R)) \lor O(T))))) \Leftrightarrow$<br>
$\forall X : (X \leq 0 \Rightarrow (\forall S:(\exists R: ((Q(R-1, T) \wedge Q(S,R)) \lor T = 9)))) \Leftrightarrow$<br>
$\forall X : (X \leq 0 \Rightarrow (\forall S:(\exists R: ((R-1 \geq T \wedge S \geq R) \lor T = 9)))) \Leftrightarrow$<br>
$\forall X : (X \leq 0) \Rightarrow (\forall S:(\exists R: ((R-1 \geq T \wedge S \geq R) \lor T = 9)))$

Implikation:

$wahr \Rightarrow wahr$<br>
$falsch \Rightarrow wahr$<br>
$falsch \Rightarrow falsch$<br>


$Fall\ 1: X > 0$


Damit die Formel richtig ist, muss der Zweite Part der Aussage wahr oder falsch sein. $\Rightarrow T \in \{-10, .. 10\}$

$Fall\ 2: X \leq 0$

Damit die Formel richtig ist, muss der Zweite Part der Aussage wahr sein.

1. $\forall S: \exists R: S \geq R \Longrightarrow R = -10$

2. $R - 1 \geq T \Longrightarrow T \leq -11 \notin D$ 

$\Longrightarrow \textbf{T = 9}$

## Aufgabe 2:

$\forall S : (\exists R: ((Q(T, f(R)) \lor Q(R,S)) \lor O(f(T))))$

$D=\{Alice, Bob, Charlie, Diane\}$

---

$Fall\ 1:\ O(f(T))\ ist\ wahr$


$O(f(T))$ ist genau dann wahr, wenn $f(T)$ = Charlie $\Longrightarrow O(f(T))$ ist immer falsch

$\Longrightarrow T = \empty \wedge T \neq Charlie$

$Fall\ 2:\ Q(R,S)\ ist\ wahr$

Nicht immer wahr, S = Charlie

$\Longrightarrow T = \empty$

$Fall\ 3:\ Q(T, f(R))\ ist\ wahr$

$\Rightarrow R \in \{Alice, Bob\}$

$\Longrightarrow T \in \{Bob\}$

$\Longrightarrow\textbf{T = Bob}$

