# Informatik 2 Übung02

## Aufgabe 1

| Prozesse | $P_1$ | $P_2$ | $P_3$ | $P_4$ | $P_5$ | $P_6$ |
| -------- | ----- | ----- | ----- | ----- | ----- | ---- |
| Ankunftszeit| 0 | 4000 | 5000 | 39000 | 42000 | 43000 |
| Rechenzeit   | 15000 | 20000 | 5000 | 50000 | 25000 | 10000 |

### Nicht-Unterbrechendes Sceduling

#### First Job First Served


| Laufzeit | Rechender Prozess | Bereiten Prozesse |
| ---- | ---- | ---- |
| 0 | $P_1$ | |
| 4000 | $P_1$ | $P_2$ |
| 5000 | $P_1$ | $P_2$, $P_3$ |
| 15000 | $P_2$ | $P_3$ |
| 25000 | $P_3$ | |
| 39000 | $P_3$ | $P_4$ |
| 40000 | $P_4$ | |
| 42000 | $P_4$ | $P_5$ |
| 43000 | $P_4$ | $P_5$, $P_6$ |
| 90000 | $P_5$ | $P_6$ |
| 115000 | $P_6$ | |
| 125000 | |

Durchschnittliche Wartezit pro Prozess: (0 + 11000 + 10000 + 1000  + 48000 + 73000) / 6 = 23833,333334

#### Shortest Job First

| Laufzeit | Rechender Prozess | Bereiten Prozesse |
| ---- | ---- | ---- |
| 0 | $P_1$ | |
| 4000 | $P_1$ | $P_2$ |
| 5000 | $P_1$ | $P_2$, $P_3$ |
| 15000 | $P_3$ | $P_2$ |
| 20000 | $P_2$ | |
| 39000 | $P_2$ | $P_4$ |
| 40000 | $P_4$ | |
| 42000 | $P_4$ | $P_5$ |
| 43000 | $P_4$ | $P_5$, $P_6$ |
| 90000 | $P_6$ | $P_5$ |
| 100000 | $P_5$ | |
| 125000 | |

Durchschnittliche Wartezeit pro Prozess: (0 + 16000 + 10000 + )



