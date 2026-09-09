**Projekt 1:**
Analiza povijesnih podataka, uređenje podataka i osnovni tehnički indikatori

Ovaj projekt automatski preuzima povijesne podatke za odabrane financijske instrumente te ih uređuje zatim provodi statističku i tehničku analizu.

**POKRETANJE SKRIPTE**
Samo pokrenite main.py skriptu i ona će automatski sve riješiti.

**ODABIRANJE IMOVINE**
S obzirom da su podatci preuzeti s Yahoo Finance-a, treba pronaći naziv tickera odnosno kratice imovine s Yahooa. Tickere ćete upisati prilikom pokretanja main.py skripte.
Program će izbacivati grešku ili će preskočiti određeni ticker ako je pogrešno napisana kratica ili ako ga nema na Yahoo Finance-u

* **NAPOMENA:** **ZLATO** preko Yahoo financea koristi skraćenicu GC=F što označava terminske ugovore zlata, a **Srebro** je SI=F
  
**Mogućnosti Projekta**
* **Automatsko dohvaćanje podataka:** Preuzimanje najnovijih podataka (OHLCV) do današnjeg dana koristeći Yahoo Finance.
* **Statistička analiza:** Izračunavanje osnovnih statistika (Maksimum, Minimum, Prosjek, Medijan, Standardnu devijaciju), ispisuje ih u tablicu te analiza strukture podataka.
* **Izračun prinosa i volatilnosti:** Računa više vrsta prinosa (Jednostavni, logaritamski, kumulativni) i volatilnost (dnevnu, godišnju i rolling odnosno pokretnu).
* **Tehnički indikatori:** Izračun pokretnih prosjeka (SMA, EMA), RSI-ja, MACD-a, Bollingerovih traka, te njihova vizualizacija na grafikonima.
* **Analiza sezonalnosti:** Istraživanje povijesnih prinosa po mjesecima i danima u tjednu pomoću Boxplot vizualizacije.
* **Vizualizacija rizika:** Prikaz distribucije dnevnih prinosa (histogram) i rolling volatilnosti kroz vrijeme.
* **Korelacijska matrica:** Prikaz korelacijske matrice cijene i volumena odvojeno te spojenu matricu cijene i volumena
* **Info:** Pruža osnovne informacije o određenom financijskom instrumentu

* **Cijeli izvještaj je generiran u Excel datoteci**

