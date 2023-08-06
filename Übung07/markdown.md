# Übung07

## Aufgabe 1

$((C \wedge \neg D) \wedge \neg (\neg D \Rightarrow B)) \lor ((\neg A \lor \neg B) \wedge (\neg A \Rightarrow \neg C))$<br>
$\Rightarrow$<br>
$((C \wedge \neg D) \wedge (\neg D \wedge \neg B)) \lor ((\neg A \lor \neg B) \wedge (A \lor \neg C))$<br>
$\Rightarrow$<br>
$(C \wedge \neg D \wedge \neg B) \lor ((\neg A \lor \neg B) \wedge (A \lor \neg C))$<br>
$\Rightarrow$<br>
$(C \lor ((\neg A \lor \neg B) \wedge (A \lor \neg C))) \wedge (\neg D \lor ((\neg A \lor \neg B) \wedge (A \lor \neg C))) \wedge (\neg B \lor ((\neg A \lor \neg B) \wedge (A \lor \neg C)))$<br>
$\Rightarrow$<br>
$((C \lor \neg A \lor \neg B) \wedge (C \lor A \lor \neg C)) \wedge ((\neg D \lor \neg A \lor \neg B) \wedge (\neg D \lor A \lor \neg C)) \wedge ((\neg B \lor \neg A \lor \neg B) \wedge (\neg B \lor A \lor \neg C))$<br>
$\Rightarrow$<br>
$(C \lor \neg A \lor \neg B) \wedge (C \lor A \lor \neg C) \wedge (\neg D \lor \neg A \lor \neg B) \wedge (\neg D \lor A \lor \neg C) \wedge (\neg B \lor \neg A \lor \neg B) \wedge (\neg B \lor A \lor \neg C)$<br>
$\Rightarrow$<br>
$(C \lor \neg A \lor \neg B) \wedge A \wedge (\neg D \lor \neg A \lor \neg B) \wedge (\neg D \lor A \lor \neg C) \wedge (\neg A \lor \neg B) \wedge (\neg B \lor A \lor \neg C)$<br>
$\Rightarrow$<br>
$(C \lor \neg A \lor \neg B) \wedge A \wedge (\neg D \lor \neg A \lor \neg B) \wedge (\neg D \lor A \lor \neg C) \wedge (\neg A \lor \neg B)$<br>

Klauselmenge:

$\Kappa(F) = \{L_{1}, L_{2}, L_{3}, L_{4}, L_{5}\}$

$L_1 = \{C \lor \neg A \lor \neg B\}$<br>
$L_2 = \{A\}$<br>
$L_3 = \{\neg D \lor \neg A \lor \neg B\}$<br>
$L_4 = \{\neg D \lor \neg A \lor \neg C\}$<br>
$L_5 = \{\neg A \lor \neg B\}$<br>


## Aufgabe 2

### 1.

Klauselmenge $K_0$:

$K_0 = \{L_0, L_1, L_2, L_3, L_4\}$

$L_0 = \{X \lor \neg Y\}$<br>
$L_1 = \{\neg X \lor \neg Y \lor \neg Z\}$<br>
$L_2 = \{\neg X \lor Z\}$<br>
$L_3 = \{X \lor Y \lor Z\}$<br>
$L_4 = \{Y \lor \neg Z\}$<br>