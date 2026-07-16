import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. EMA INDIKATORI (Računaju se iz Price_btc)
EMA_20 = Price_btc.ewm(span=20, adjust=False).mean()
EMA_50 = Price_btc.ewm(span=50, adjust=False).mean()

# 2. SIGNALI KRIŽANJA
Pozicija = (EMA_20 > EMA_50).astype(int)
Signal = Pozicija.diff()

# TOČAN NAČIN FILTRIRANJA: Izvlačimo točne cijene samo za dane kada je signal 1 ili -1
Cijene_Kupnja = Price_btc[Signal == 1]
Cijene_Prodaja = Price_btc[Signal == -1]

# ==========================================
# 3. GRAFIČKI PRIKAZ (Popravljene linije i scatter)
# ==========================================
plt.figure(figsize=(14, 7))

# Crtanje cijene i EMA linija (SADA CRTAMO TOČNE VARIJABLE!)
plt.plot(Price_btc.index, Price_btc, label="Cijena BTC", color="black", alpha=0.3)
plt.plot(EMA_20.index, EMA_20, label="EMA 20 (Brza)", color="blue", alpha=0.8)
plt.plot(EMA_50.index, EMA_50, label="EMA 50 (Spora)", color="orange", alpha=0.8)

# Označavanje signala na grafikonu (Koristimo indekse datuma i filtrirane cijene)
plt.scatter(
    Cijene_Kupnja.index,
    Cijene_Kupnja,
    label="Kupovni Signal (Buy)",
    marker="^",
    color="green",
    s=100,
    zorder=5,
)
plt.scatter(
    Cijene_Prodaja.index,
    Cijene_Prodaja,
    label="Prodajni Signal (Sell)",
    marker="v",
    color="red",
    s=100,
    zorder=5,
)

# Uređivanje i estetika
plt.title(
    "EMA Crossover Strategija (20/50) - BTC-USD",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Datum", fontsize=10)
plt.ylabel("Cijena (USD)", fontsize=10)
plt.grid(True, linestyle=":", alpha=0.5)
plt.legend(loc="upper left")

# Prikaz grafikona
plt.show()
