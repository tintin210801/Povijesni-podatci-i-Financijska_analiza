import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Učitavanje podataka
Data = pd.read_csv("podaci.csv", header=[0, 1], index_col=0, parse_dates=True)
Price = Data['Close'].ffill().bfill()
tickers = Price.columns.tolist()

# RSI izračun
delta = Price.diff()
gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)
avg_gain = gain.ewm(com=13, adjust=False).mean()
avg_loss = loss.ewm(com=13, adjust=False).mean()
rs = avg_gain / avg_loss
RSI = 100 - (100 / (1 + rs))

# Podgrafovi za sve tickere
n = len(tickers)
cols = 2
rows = (n + cols - 1) // cols

fig, axes = plt.subplots(rows, cols, figsize=(15, 4*rows))
axes = axes.flatten() if n > 1 else [axes]

for i, ticker in enumerate(tickers):
    if i < n:
        axes[i].plot(RSI.index, RSI[ticker], color="blue", linewidth=1)
        axes[i].axhline(70, color="red", linestyle="--", alpha=0.5, linewidth=0.8)
        axes[i].axhline(30, color="green", linestyle="--", alpha=0.5, linewidth=0.8)
        axes[i].axhline(50, color="gray", linestyle=":", alpha=0.3, linewidth=0.5)
        axes[i].set_ylim(10, 90)
        axes[i].set_title(ticker, fontsize=10, fontweight='bold')
        axes[i].grid(True, linestyle=":", alpha=0.5)
        axes[i].set_ylabel('RSI', fontsize=8)

# Sakrij prazne podgrafove
for j in range(i+1, len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.savefig("Svi_tickeri_RSI.png", dpi=300, bbox_inches='tight')
print("Grafikon spremljen kao 'Svi_tickeri_RSI.png'")
plt.show()