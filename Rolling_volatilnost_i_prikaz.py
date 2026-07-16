import matplotlib.pyplot as plt

# 1. Izračunaj dnevne povrate
Returns = Data['Close'].pct_change()

# 2. Izračunaj rolling volatilnost (standardnu devijaciju) za prozor od 21 dan
# Množimo s np.sqrt(252) kako bismo je "anualizirali" (prikazali na godišnjoj razini, što je standard u financijama)
import numpy as np
rolling_vol = Returns.rolling(window=25).std() * np.sqrt(252) * 100  # Prikaz u postotcima (%)

# 3. Odaberi imovine za prikaz (npr. visokorizični BTC i stabilniji SPY)
ticker_1 = 'BTC-USD'
ticker_2 = 'SPY'
ticker_3 = 'ETH-USD'
# 4. Nacrtaj grafikon
plt.figure(figsize=(12, 6))

# Koristimo laganu prozirnost (alpha=0.8) kako bi se linije ljepše preklapale
plt.plot(rolling_vol[ticker_1], label=f'{ticker_1} (25-day Rolling Volatility)', color='orange', linewidth=1.5, alpha=0.8)
plt.plot(rolling_vol[ticker_2], label=f'{ticker_2} (25-day Rolling Volatility)', color='navy', linewidth=1.5, alpha=0.8)
plt.plot(rolling_vol[ticker_3], label=f'{ticker_3} (25-day Rolling Volatility)', color='red', linewidth=1.5, alpha=0.8)

# 5. Estetika i označavanje turbulencija
plt.title("Rolling Volatilnost kroz vrijeme (Godišnja, 25-dnevni prozor)", fontsize=14, fontweight='bold')
plt.xlabel("Datum", fontsize=12)
plt.ylabel("Volatilnost (%)", fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left')

# Automatsko prilagođavanje i prikaz
plt.tight_layout()
plt.show()
