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

 $Res^0(K_0) = K_0 = \{\{X \lor \neg Y\}, \{\neg X \lor \neg Y \lor \neg Z\}, \{\neg X \lor Z\}, \{X \lor Y \lor Z\}, \{Y \lor \neg Z\}\}$<br>
 $Res^1(K_0) = \{\{X \lor \neg Y\}, \{\neg X \lor \neg Y \lor \neg Z\}, \{\neg X \lor Z\}, \{X \lor Y \lor Z\}, \{Y \lor \neg Z\}, \{\neg X \lor Y\}\}$<br>
 $Res^2(K_0) = \{\{X \lor \neg Y\}, \{\neg X \lor \neg Y \lor \neg Z\}, \{\neg X \lor Z\}, \{X \lor Y \lor Z\}, \{Y \lor \neg Z\}, \{\neg X \lor Y\}, \{Y \lor \neg Y\}\}$<br>
$Res^3(K_0) = \{\{X \lor \neg Y\}, \{\neg X \lor \neg Y \lor \neg Z\}, \{\neg X \lor Z\}, \{X \lor Y \lor Z\}, \{Y \lor \neg Z\}, \{\neg X \lor Y\}, \{Y \lor \neg Y\}, \{\neg Y \lor Z\}\}$<br>
$Res^4(K_0) = \{\{X \lor \neg Y\}, \{\neg X \lor \neg Y \lor \neg Z\}, \{\neg X \lor Z\}, \{X \lor Y \lor Z\}, \{Y \lor \neg Z\}, \{\neg X \lor Y\}, \{Y \lor \neg Y\}, \{\neg Y \lor Z\}, \{\neg Y \lor \neg Z\}\}$<br>
$Res^5(K_0) = \{\{X \lor \neg Y\}, \{\neg X \lor \neg Y \lor \neg Z\}, \{\neg X \lor Z\}, \{X \lor Y \lor Z\}, \{Y \lor \neg Z\}, \{\neg X \lor Y\}, \{Y \lor \neg Y\}, \{\neg Y \lor Z\}, \{\neg Y \lor \neg Z\}, \{\neg Y\}\}$<br>
$Res^6(K_0) = \{\{X \lor \neg Y\}, \{\neg X \lor \neg Y \lor \neg Z\}, \{\neg X \lor Z\}, \{X \lor Y \lor Z\}, \{Y \lor \neg Z\}, \{\neg X \lor Y\}, \{Y \lor \neg Y\}, \{\neg Y \lor Z\}, \{\neg Y \lor \neg Z\}, \{\neg Y\}, \{X \lor Y\}\}$<br>
$Res^7(K_0) = \{\{X \lor \neg Y\}, \{\neg X \lor \neg Y \lor \neg Z\}, \{\neg X \lor Z\}, \{X \lor Y \lor Z\}, \{Y \lor \neg Z\}, \{\neg X \lor Y\}, \{Y \lor \neg Y\}, \{\neg Y \lor Z\}, \{\neg Y \lor \neg Z\}, \{\neg Y\}, \{X \lor Y\}, \{Y\}\}$<br>
$Res^7(K_0) = \{\{X \lor \neg Y\}, \{\neg X \lor \neg Y \lor \neg Z\}, \{\neg X \lor Z\}, \{X \lor Y \lor Z\}, \{Y \lor \neg Z\}, \{\neg X \lor Y\}, \{Y \lor \neg Y\}, \{\neg Y \lor Z\}, \{\neg Y \lor \neg Z\}, \{\neg Y\}, \{X \lor Y\}, \{Y\}, \empty\}$<br>

$\Rightarrow$ F ist nicht erfüllbar.


## Aufgabe 3

1. $X + (-Y)$<br>
gehört nicht zur Sprache, da der Funktor - die Stelligkeit 2 erwartet.

2. $1 + 2 - X - Y<br>
gehört zur Sprache, ist ein Term. Es kann das zu bezeichnete Objekt angegeben werden, indem Werte für X und Y eingesetzt werden-

3. $2 < ((2 > 3) \lor (3 \geq 2))$<br>
gehört nicht zur Sprache wegen $\geq$

4. $1 > (\exists X : (X < 0))$<br>
gehört nicht zur Sprache, da > Prädikat eine ganze Zahl und keinen Wahrheitswert erwartet

5. $2 + 3 = 5$<br>
gehört nicht zur Sprache, da = kein Prädikat und kein Funktor ist.

6. $(X > 2) \wedge (X + 2)$<br>
gehört nicht zur Sprache, da Warheitswert mit einem Objekt verknüpft.

7. $(Z > 2) \lor ((Z - 1) < 0)$<br>
gehört zur Sprache und ist eine offene Formel. Liefert Wahr, wenn Z > 2 oder Z < 1
Liefert Falsch, wenn $Z \in \{1,2\}$

8. $\forall X : ( X \Rightarrow (X \cdot (2+3)))$<br>
gehört nicht zur Sprache $\cdot$.

9. $\exists X : (\exists Y : ((X > 2) \wedge (\neg(Y < 3))))$<br>
gehört zu Sprache und ist eine geschlossene Formel. Liefert Wahr.

10. $6 + 1 - 8$
gehört zur Sprache und ist ein Term. Es wird -1 dargestellt.

11. $\forall X : ((X \wedge (2 > 3)) \Rightarrow X)$<br>
gehört  nicht zur Sprache aufgrund der Verknüpfung eines Wahrheitswertes mit einem Objekt.

12. $\exists : ((Z < 2) \lor ((Z - 1) < 0))$<br>
gehört nicht zur Sprache, da dem Existenzquantor eine Variable folgen müsste, das tut es hier aber nicht.
