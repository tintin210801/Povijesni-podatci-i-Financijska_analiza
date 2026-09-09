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

fig, axes = plt.subplots(rows, cols, figsize=(15, 5*rows))

if rows == 1 and cols == 1:
    axes = np.array([axes])
else:
    axes = np.array(axes).flatten()

for i, ticker in enumerate(tickers):
    if i < n:
        Price_current = Price[ticker]
        
        # EMA indikatori
        EMA_20 = Price_current.ewm(span=20, adjust=False).mean()
        EMA_50 = Price_current.ewm(span=50, adjust=False).mean()
        
        # Signali
        Pozicija = (EMA_20 > EMA_50).astype(int)
        Signal = Pozicija.diff()
        Cijene_Kupnja = Price_current[Signal == 1]
        Cijene_Prodaja = Price_current[Signal == -1]
        
        # Crtanje
        axes[i].plot(Price_current.index, Price_current, color="black", alpha=0.5, linewidth=1)
        axes[i].plot(EMA_20.index, EMA_20, color="blue", alpha=0.7, linewidth=1, label='EMA 20')
        axes[i].plot(EMA_50.index, EMA_50, color="orange", alpha=0.7, linewidth=1, label='EMA 50')
        
        if len(Cijene_Kupnja) > 0:
            axes[i].scatter(Cijene_Kupnja.index, Cijene_Kupnja, marker="^", color="green", s=30)
        if len(Cijene_Prodaja) > 0:
            axes[i].scatter(Cijene_Prodaja.index, Cijene_Prodaja, marker="v", color="red", s=30)
        
        axes[i].set_title(ticker, fontsize=10)
        axes[i].grid(True, linestyle=":", alpha=0.5)
        axes[i].legend(loc='upper left', fontsize=8)

# Sakrij prazne podgrafove
for j in range(i+1, len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.savefig("Svi_tickeri_EMA.png", dpi=300, bbox_inches='tight')
print("Grafikon spremljen kao 'Svi_tickeri_EMA.png'")