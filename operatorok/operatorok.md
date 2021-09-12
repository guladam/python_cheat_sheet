## Operátorok

Az operátorokat műveletek végrehajtására használjuk.
A következő matematikai operátorokkal találkoztunk eddig:

| Jel | Példák |
| --- | --- |
| + | Összeadás: 5 + 5 -> 10<br>Összefűzés: "Mr." + " John" -> "Mr. John" |
| - | Kivonás: 10 - 5 -> 5 |
| / | Valós osztás:<br>10 / 2 -> 5.0<br>9 / 4 -> 2.25 |
| * | Szorzás: 5 * 5 -> 25<br>Szöveg ismétlése: "Helló" * 5 -> "HellóHellóHellóHellóHelló" |
| // | Egész osztás:<br>14 // 10 -> 1<br>10 // 3 -> 3 |
| % | Maradékos osztás:<br>5 % 2 -> 1<br>10 % 2 -> 0 |

Az **összehasonlító operátorokat** logikai kifejezések (eldöntendő kérdések) létrehozására használunk. Az ilyen kifejezések értéke mindig logikai (bool) típusú, azaz *True* vagy *False*. A következő összehasonlító operátorokkal találkoztunk eddig:

| Jel | Példák |
| --- | --- |
| == | Egyenlőség:<br>5 == 5 -> True<br>5 == 10 -> False |
| != | Nem egyenlő:<br>5 != 5 -> False<br>5 != 10 -> True |
| > | Nagyobb:<br>5 > 10 -> False<br>5 > 4 -> True |
| < | Kisebb:<br>5 < 10 -> True<br>5 < 4 -> False |
| >= | Nagyobb egyenlő:<br>5 >= 10 -> False<br>5 >= 5 -> True |
| <= | Kisebb egyenlő:<br>5 <= 4 -> False<br>5 <= 5 -> True |

> Megjegyzés: a változó értékadásra használt 1 egyenlőségjel (=) is egy operátor, de azt már taglaltuk a változók részben.

## Logikai műveletek

Összetett logikai kifejezések (eldöntendő kérdések) előállításához logikai műveleteket használunk:

### Logikai ÉS: **and** kulcsszó

| a | b | a and b |
| --- | --- | --- |
| True | True | True |
| False | True | False |
| True | False | False |
| False | False | False |

### Logikai VAGY: **or** kulcsszó

| a | b | a or b |
| --- | --- | --- |
| True | True | True |
| False | True | True |
| True | False | True |
| False | False | False |

### Logikai NEM: **not** kulcsszó

| a | not a |
| --- | --- |
| True | False |
| False | True |

> Próbáld ki a logikai műveleteket egy Python programban úgy, hogy *a* és *b* helyére logikai kifejezéseket (eldöntendő kérdéseket) írsz.

[Vissza a főoldalra](../README.md)