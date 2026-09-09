import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Učitavanje podataka
Data = pd.read_csv("podaci.csv", header=[0, 1], index_col=0, parse_dates=True)
Data = Data['Close'].ffill().bfill()
tickers = Data.columns.tolist()

# Izračun rolling volatilnosti
Returns = Data.pct_change()
rolling_vol = Returns.rolling(window=25).std() * np.sqrt(252) * 100

# Podgrafovi za sve tickere
n = len(tickers)
cols = 2
rows = (n + cols - 1) // cols

fig, axes = plt.subplots(rows, cols, figsize=(15, 5*rows))

if rows == 1 and cols == 1:
    axes = np.array([axes])
else:
    axes = np.array(axes).flatten()
for i, ticker in enumerate(tickers):
    if i < n:
        axes[i].plot(rolling_vol[ticker], color='orange', linewidth=1.5)
        axes[i].axhline(rolling_vol[ticker].mean(), color='red', linestyle='--', linewidth=0.8, alpha=0.5)
        axes[i].set_title(ticker, fontsize=10, fontweight='bold')
        axes[i].grid(True, linestyle=':', alpha=0.5)
        axes[i].set_ylabel('Vol (%)', fontsize=8)

# Sakrij prazne podgrafove
for j in range(i+1, len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.savefig("rolling_volatilnost_podgrafovi.png", dpi=300, bbox_inches='tight')
print("Grafikon spremljen kao 'rolling_volatilnost_podgrafovi.png'")
