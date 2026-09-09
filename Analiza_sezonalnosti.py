import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Učitavanje podataka
Data = pd.read_csv("podaci.csv", header=[0, 1], index_col=0, parse_dates=True)
Price = Data['Close'].ffill().bfill()
tickers = Price.columns.tolist()

dani_redoslijed = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mjeseci_redoslijed = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

n = len(tickers)
cols = 2
rows = (n + cols - 1) // cols

# ----------------- Dani u tjednu -----------------
fig, axes = plt.subplots(rows, cols, figsize=(15, 5*rows))
if rows == 1 and cols == 1:
    axes = np.array([axes])
else:
    axes = np.array(axes).flatten()

for i, ticker in enumerate(tickers):
    if i < n:
        Prinosi = Data['Close'][ticker].pct_change(fill_method=None).dropna() * 100
        df_sezona = Prinosi.to_frame(name='Prinos')
        df_sezona['Dan_u_tjednu'] = df_sezona.index.day_name()
        
        sns.boxplot(
            ax=axes[i], data=df_sezona, x='Dan_u_tjednu', y='Prinos',
            hue='Dan_u_tjednu',
            order=[d for d in dani_redoslijed if d in df_sezona['Dan_u_tjednu'].unique()],
            palette='Set2', showfliers=False, legend=False
        )
        axes[i].axhline(0, color='red', linestyle='--', linewidth=0.5)
        axes[i].set_title(ticker, fontsize=9)
        axes[i].set_xlabel('', fontsize=8)
        axes[i].set_ylabel('Prinos (%)', fontsize=8)
        axes[i].grid(True, linestyle=':', alpha=0.5)
        axes[i].tick_params(axis='x', rotation=45)

for j in range(i+1, len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.savefig("Svi_tickeri_sezonalnost_dani.png", dpi=300, bbox_inches='tight')


# ----------------- Mjeseci -----------------
fig, axes = plt.subplots(rows, cols, figsize=(15, 5*rows))
if rows == 1 and cols == 1:
    axes = np.array([axes])
else:
    axes = np.array(axes).flatten()

for i, ticker in enumerate(tickers):
    if i < n:
        Prinosi = Data['Close'][ticker].pct_change(fill_method=None).dropna() * 100
        df_sezona = Prinosi.to_frame(name='Prinos')
        df_sezona['Mjesec'] = df_sezona.index.strftime('%b')
        
        sns.boxplot(
            ax=axes[i], data=df_sezona, x='Mjesec', y='Prinos',
            hue='Mjesec',
            order=mjeseci_redoslijed, palette='coolwarm', showfliers=False, legend=False
        )
        axes[i].axhline(0, color='red', linestyle='--', linewidth=0.5)
        axes[i].set_title(ticker, fontsize=9)
        axes[i].set_xlabel('', fontsize=8)
        axes[i].set_ylabel('Prinos (%)', fontsize=8)
        axes[i].grid(True, linestyle=':', alpha=0.5)

for j in range(i+1, len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.savefig("Svi_tickeri_sezonalnost_mjeseci.png", dpi=300, bbox_inches='tight')
