# RSI indikator
# Izračun dnevne razlike u cijeni
delta = Price.diff()

# Dobitci i gubitci
gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)

# Eksponencijalni prosjek (EMA) za dobitke i gubitke
avg_gain = gain.ewm(com=13, adjust=False).mean()
avg_loss = loss.ewm(com=13, adjust=False).mean()

# Izračun relativne snage (RS) i RSI
rs = avg_gain / avg_loss
RSI = 100 - (100 / (1 + rs))

# Primjer dohvaćanja RSI-a za jednu imovinu i cjelokupnu imovinu
print(RSI['BTC-USD'].tail())
print(RSI.tail())

# Prolazimo kroz svaki stupac imovine pojedinačno
for ticker in RSI.columns:
    #Otvaramo novi, zasebni prozor za grafikon
    plt.figure(figsize=(12, 5))

    # Crtamo liniju samo za trenutnu imovinu
    plt.plot(RSI.index, RSI[ticker], label=ticker, color="blue", linewidth=1.5)

    # RSI granice (70 i 30)
    plt.axhline(70, color="red", linestyle="--", alpha=0.5, label="Overbought (70)")
    plt.axhline(30, color="green", linestyle="--", alpha=0.5, label="Oversold (30)")

    # Uređivanje izgleda grafikona
    plt.title(
        f"Indeks relativne snage (RSI) - {ticker}",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Datum", fontsize=10)
    plt.ylabel("RSI Vrijednost (0-100)", fontsize=10)
    plt.ylim(10, 90)  # Ograničavamo Y os radi bolje vidljivosti

    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="upper left")

    # 5. Prikaz
    plt.show()
