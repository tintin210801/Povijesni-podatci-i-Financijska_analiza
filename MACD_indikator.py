# IZDVAJANJE I ČIŠĆENJE POJEDINAČNE IMOVINE
Price_btc = Price["BTC-USD"].ffill().bfill()

# IZRAČUN MACD-A SAMO ZA BTC
# Izračun 25-dnevnog i 50-dnevnog EMA za BTC
ema25_btc = Price_btc.ewm(span=25, adjust=False).mean()
ema50_btc = Price_btc.ewm(span=50, adjust=False).mean()

# Komponente MACD-a za BTC
MACD_btc = ema25_btc - ema50_btc
Signal_btc = MACD_btc.ewm(span=9, adjust=False).mean()
Hist_btc = MACD_btc - Signal_btc


# GRAFIČKI PRIKAZ ZA BTC
plt.figure(figsize=(12, 5))

# MACD i Signalne linije za BTC
plt.plot(
    MACD_btc.index, MACD_btc, label="MACD (25, 50)", color="blue", linewidth=1.5
)
plt.plot(
    Signal_btc.index,
    Signal_btc,
    label="Signal (9)",
    color="orange",
    linewidth=1.5,
)

# Definiranje boja histograma (zeleno za rast, crveno za pad)
boje_btc = ["green" if x >= 0 else "red" for x in Hist_btc]
plt.bar(Hist_btc.index, Hist_btc, color=boje_btc, alpha=0.5, label="Histogram")

# Dodavanje nulte linije i estetike
plt.axhline(0, color="black", linestyle="-", linewidth=0.8, alpha=0.5)
plt.title(
    "MACD Indikator Zamaha - BTC-USD (Pojedinačno)",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Datum", fontsize=10)
plt.ylabel("Vrijednost", fontsize=10)
plt.grid(True, linestyle=":", alpha=0.5)
plt.legend(loc="upper left")

# Prikaz grafikona
plt.show()
