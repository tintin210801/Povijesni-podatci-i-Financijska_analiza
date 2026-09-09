import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Učitavanje podataka
Data = pd.read_csv("podaci.csv", header=[0, 1], index_col=0, parse_dates=True)
Price = Data['Close'].ffill().bfill()
tickers = Price.columns.tolist()

# Podgrafovi za sve tickere (robusno rješenje za n=1 ili više tickera)
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
        Price_current = Price[ticker]
        
        # SMA izračuni
        SMA10 = Price_current.rolling(10).mean()
        SMA20 = Price_current.rolling(20).mean()
        SMA50 = Price_current.rolling(50).mean()
        SMA100 = Price_current.rolling(100).mean()
        SMA200 = Price_current.rolling(200).mean()
        
        # Crtanje
        axes[i].plot(Price_current.index, Price_current, color='black', linewidth=1, alpha=0.7, label='Cijena')
        axes[i].plot(SMA10.index, SMA10, color='blue', linewidth=0.8, linestyle='--', label='SMA10')
        axes[i].plot(SMA20.index, SMA20, color='orange', linewidth=0.8, label='SMA20')
        axes[i].plot(SMA50.index, SMA50, color='green', linewidth=0.8, label='SMA50')
        axes[i].plot(SMA100.index, SMA100, color='red', linewidth=0.8, label='SMA100')
        axes[i].plot(SMA200.index, SMA200, color='purple', linewidth=0.8, label='SMA200')
        
        axes[i].set_title(ticker, fontsize=10, fontweight='bold')
        axes[i].grid(True, linestyle=':', alpha=0.5)
        axes[i].legend(loc='upper left', fontsize=6)

# Sakrij prazne podgrafove
for j in range(i+1, len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.savefig("Svi_tickeri_SMA.png", dpi=300, bbox_inches='tight')
print("Grafikon spremljen kao 'Svi_tickeri_SMA.png'")