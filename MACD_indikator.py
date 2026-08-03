import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Učitavanje podataka
Data = pd.read_csv("podaci.csv", header=[0, 1], index_col=0, parse_dates=True)
Price = Data['Close'].ffill().bfill()
tickers = Price.columns.tolist()

# Podgrafovi za sve tickere
n = len(tickers)
cols = 2
rows = (n + cols - 1) // cols

fig, axes = plt.subplots(rows, cols, figsize=(15, 4*rows))
axes = axes.flatten() if n > 1 else [axes]

for i, ticker in enumerate(tickers):
    if i < n:
        Price_current = Price[ticker]
        
        # MACD izračuni
        ema25 = Price_current.ewm(span=25, adjust=False).mean()
        ema50 = Price_current.ewm(span=50, adjust=False).mean()
        MACD = ema25 - ema50
        Signal = MACD.ewm(span=9, adjust=False).mean()
        Hist = MACD - Signal
        
        # Crtanje
        axes[i].plot(MACD.index, MACD, color="blue", linewidth=1, label='MACD')
        axes[i].plot(Signal.index, Signal, color="orange", linewidth=1, label='Signal')
        
        # Histogram
        boje = ["green" if x >= 0 else "red" for x in Hist]
        axes[i].bar(Hist.index, Hist, color=boje, alpha=0.5, width=0.8)
        
        axes[i].axhline(0, color="black", linestyle="-", linewidth=0.5, alpha=0.5)
        axes[i].set_title(ticker, fontsize=10, fontweight='bold')
        axes[i].grid(True, linestyle=":", alpha=0.5)
        axes[i].legend(loc='upper left', fontsize=7)

# Sakrij prazne podgrafove
for j in range(i+1, len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.savefig("Svi_tickeri_MACD.png", dpi=300, bbox_inches='tight')
print("Grafikon spremljen kao 'Svi_tickeri_MACD.png'")
plt.show()