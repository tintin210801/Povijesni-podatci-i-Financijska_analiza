import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Učitavanje podataka
Data = pd.read_csv("podaci.csv", header=[0, 1], index_col=0, parse_dates=True)
tickers = Data['Close'].columns.tolist()

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
        Prinosi = Data['Close'][ticker].pct_change(fill_method=None).dropna()
        Prinosi_u_postotcima = Prinosi * 100
        
        # Uklonjen problematični hue argument
        sns.histplot(
            data=Prinosi_u_postotcima, bins=50, kde=True, 
            color='royalblue', edgecolor='black', alpha=0.7, ax=axes[i]
        )
        
        prosjek = Prinosi_u_postotcima.mean()
        medijan = Prinosi_u_postotcima.median()
        axes[i].axvline(prosjek, color='red', linestyle='--', linewidth=1.5, label=f'Mean: {prosjek:.2f}%')
        axes[i].axvline(medijan, color='green', linestyle='-', linewidth=1.5, label=f'Median: {medijan:.2f}%')
        
        axes[i].set_title(ticker, fontsize=10, fontweight='bold')
        axes[i].set_xlabel('Dnevni prinos (%)', fontsize=8)
        axes[i].set_ylabel('Frekvencija', fontsize=8)
        axes[i].grid(True, linestyle=':', alpha=0.5)
        axes[i].legend(fontsize=7)

for j in range(i+1, len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.savefig("Svi_tickeri_histogrami.png", dpi=300, bbox_inches='tight')
print("Grafikon spremljen kao 'Svi_tickeri_histogrami.png'")