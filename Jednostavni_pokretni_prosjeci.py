# Računanje jednostavnih pokretnih prosjeka pomoću 'Close' cijene
# Pokretni prosjeci od 10, 20, 50, 100, 200 SMA
SMA10 = Price_btc.rolling(10).mean()
SMA20 = Price_btc.rolling(20).mean()
SMA50 = Price_btc.rolling(50).mean()
SMA100 = Price_btc.rolling(100).mean()
SMA200 = Price_btc.rolling(200).mean() 
# Grafikon i veličina
plt.figure(figsize=(14, 7))

#Cijena (malo deblja i tamnija linija)
plt.plot(Price_btc, label='Stvarna cijena (Close)', color='black', linewidth=1.8, alpha=0.8)

# Svi pokretni prosjeci (različite boje i tanje linije)
plt.plot(SMA10, label='SMA 10', color='blue', linewidth=1, linestyle='--')
plt.plot(SMA20, label='SMA 20', color='orange', linewidth=1)
plt.plot(SMA50, label='SMA 50', color='green', linewidth=1)
plt.plot(SMA100, label='SMA 100', color='red', linewidth=1.2)
plt.plot(SMA200, label='SMA 200', color='purple', linewidth=1.5)

# Estetsko uređivanje grafikona
plt.title(f"Tehnička analiza za BTC, Pokretni prosjeci (SMA)", fontsize=14, fontweight='bold')
plt.xlabel("Datum", fontsize=12)
plt.ylabel("Cijena u USD", fontsize=12)

# Legenda da znaš koja je koja linija
plt.legend(loc='upper left', fontsize=10)

# Rešetka u pozadini radi lakšeg čitanja vrijednosti
plt.grid(True, linestyle=':', alpha=0.6)

# Prikaži grafikon
plt.show()
