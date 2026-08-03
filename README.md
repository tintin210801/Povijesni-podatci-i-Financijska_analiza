**Projekt 1:**
Analiza povijesnih podataka, uređenje podataka i osnovni tehnički indikatori

Ovaj projekt automatski preuzima povijesne podatke za odabrane financijske instrumente te podatke uređuje zatim provodi statističku i tehničku analizu.

**POKRETANJE SKRIPTE**
Samo pokrenite main.py skriptu i ona će automatski sve riješiti.

**MIJENJANJE IMOVINE**
S obzirom da su podatci preuzeti s Yahoo Finance-a, treba pronaći naziv tickera odnosno kratice imovine s Yahooa. Tickere možete mijenjati ručno u datoteci Nabava_podataka.py.
Izbrišite, ostavite ili nadodajte neke nove, ovisno o vašim željama.
Program će izbacivati grešku ili će preskočiti određeni ticker ako je krivo kratica napisana ili ako ga nema na Yahoo Finance-u

**Analizirane Imovine** (Tickeri) koje obrađuje su:
* **Kriptovalute:** BTC-USD, ETH-USD
* **Dionice / Indeksi:** SPY, GOOGL, ASML, TSM
  Primjeri još tickera: MSFT, TTWO, SOL-USD, AAPL, AMZN
**ZLATO** preko Yahoo financea koristi skraćenicu GC=F što označava terminske ugovore zlata, a **Srebro** je SI=F
  
**Mogućnosti Projekta**
* **Automatsko dohvaćanje podataka:** Preuzimanje najnovijih podataka (OHLCV) do današnjeg dana koristeći Yahoo Finance.
* **Statistička analiza:** Izračunavanje osnovnih statistika (Maksimum, Minimum, Prosjek, Medijan, Standardnu devijaciju), ispisuje ih u tablicu te analiza strukture podataka.
* **Izračun prinosa i volatilnosti:** Računa više vrsta prinosa (Jednostavni, logaritamski, kumulativni) i volatilnost (dnevnu, godišnju i rolling odnosno pokretnu).
* **Tehnički indikatori:** Izračun pokretnih prosjeka (SMA, EMA), RSI-ja, MACD-a, Bollingerovih traka, te njihova vizualizacija na grafikonima.
* **Analiza sezonalnosti:** Istraživanje povijesnih prinosa po mjesecima i danima u tjednu pomoću Boxplot vizualizacije.
* **Vizualizacija rizika:** Prikaz distribucije dnevnih prinosa (histogram) i rolling volatilnosti kroz vrijeme.
* **Korelacijska matrica:** Prikaz korelacijske matrice cijene i volumena odvojeno te spojenu matricu cijene i volumena

* **Cijeli izvještaj je generiran u Excel datoteci**

