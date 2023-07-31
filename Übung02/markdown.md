# Informatik 2 Übung02

## Aufgabe 1a

| Prozesse | $P_1$ | $P_2$ | $P_3$ | $P_4$ | $P_5$ | $P_6$ |
| -------- | ----- | ----- | ----- | ----- | ----- | ---- |
| Ankunftszeit| 0 | 4000 | 5000 | 39000 | 42000 | 43000 |
| Rechenzeit   | 15000 | 20000 | 5000 | 50000 | 25000 | 10000 |

### Nicht-Unterbrechendes Sceduling

#### Short-Job-First

| Zeit | Prozess | Warteschlange |
| ---- | ------- | ------------- |
| 0 | $P_1$ | |
|4000 | $P_1$ | $P_2$ |
|5000 |$P_1$| $P_2$, $P_3$ |
|15000| $P_3$ | $P_2$ |
|20000| $P_2$ | |
|39000| $P_2$ | $P_4$ |
|40000| $P_4$ | |
|42000| $P_4$ | $P_5$ |
|43000| $P_4$ | $P_5$, $P_6$ |
|90000| $P_6$ | $P_5$ |
|100000| $P_5$ | |
|125000| | |

Durchschnittliche Wartezeit pro Prozess:

    (0 + 16000 + 10000 + 1000 + 58000 + 47000) / 6 = 22000


### Unterbrechendes Sceduling

#### Round-Robin

Schlitzlänge 10000

| Zeit | Prozess | Warteschlange |
| ---- | ------- | ------------- |
| 0 | $P_1$ | |
|4000 | $P_1$ | $P_2$ |
|5000 |$P_1$| $P_2$, $P_3$ |
|10000| $P_2$ | $P_3$, $P_1$ |
|20000| $P_3$ | $P_1$, $P_2$ |
|25000| $P_1$ | $P_2$ |
|30000| $P_2$ | |
|39000| $P_2$ | $P_4$ |
|40000| $P_4$ | |
|42000| $P_4$ | $P_5$ |
|43000| $P_4$ | $P_5$, $P_6$ |
|50000| $P_5$ | $P_6$, $P_4$ |
|60000|$P_6$ | $P_4$, $P_5$ |
|70000| $P_4$| $P_5$ |
|80000| $P_5$| $P_4$ |
|90000| $P_4$ | $P_5$ |
|100000| $P_5$ | $P_4$ |
|105000| $P_4$ | |
|115000 | $P_4$ | |
|125000 | |


Durchschnittliche Wartezeit:

    (15000 + 15000 + 15000 + 36000 + 38000 + 17000) / 6 = 22.666,667

## Aufgabe 1b.

Damit die durchschnittliche Wartezeit möglichst klein wird, sollten die Prozesse schnellstmöglich berechnet werden, dessen Rechenzeit die Kleinste ist.

Beim Nicht unterbrochenenen Sceduling sollte somit nach dem Short-Job-First gehandelt werden.

Beim Unterbrochenen Sceduling sollte immer der Prozess aus der Warteschlange herausgeholt werden, dessen übrige Rechenzeit am wenigsten ist.

## Aufgabe 2a.

Wenn Prozesse mehrfach in der Liste stehen, bedeutet, dass der Prozess in dem gegebenen Zeitschlitz, in dem er gerechnet hat, noch zu keinem Ergebnis gekommen ist (weil seine Rechenzeit den gegebenen Zeitschlitz überschreitet), weswegen er blockiert wird und somit erneut in die Warteschlange geschoben wird und dann bereit ist bis er wieder dran ist. Somit wenn Prozesse mhrfach in der Liste stehen, heißt das, dass die Prozesse in dem gegebenen Zeitschlitz nicht fertig geworden sind mit dem Rechnen und somit blockiert werden und erneut in die Warteschlange gelangen (bis sie wieder dran sind).

## Aufgabe 2b.

Das mehrfache Eintragen von Prozessen in die Liste könnte man erlauben, wenn sie einfach zu hohe Rechenzeit aufweisen im Vergleich zum gegebenen Zeitschlitz und somit nach einem Durchlauf nicht fertigwerden können. Oder wenn während des Durchlaufs plötzlich Systemwichtige Prozesse in den Weg kommen, die höhere Priorität haben und somit kurzzeitig laufende Prozesse blockieren (bis sie fertig sind).

## Aufgabe 2c.

Es mag sein, dass der Grund, weswegen ein Prozess nicht fertigwird, nicht an der Rechenzeit liegt, sondern, dass er auf Ergebnisse von anderen Prozessen wartet, die noch nicht fertiggerechnet wurden und somit in dem gegebenen Zeitschlitz, wo der Prozess eben rechnen soll einfach nicht rechnet, sondern auf die Ergebnisse der anderen Prozesse wartet, was die mittlere Wartezeit von allen Prozessen erhöht.