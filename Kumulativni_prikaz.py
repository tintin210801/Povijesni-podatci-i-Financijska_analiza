import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Linijski grafikon
Data = pd.read_csv("podaci.csv", header=[0, 1], index_col=0, parse_dates=True)
# Računanje metrika prinosa i ostalih vrsti prinosa
Price = Data['Close'].ffill().bfill()
Cum_return = (1 + Price.pct_change()).cumprod() - 1
Cum_return.plot(kind='line', figsize=(12, 6), linewidth=1.5)

plt.title("Kumulativni rast", fontsize=14, fontweight='bold')
plt.xlabel("Datum")
plt.ylabel("Rast (npr. 1.0 = 100% zarade)")
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(title="Tickeri")

# Sprema grafikon kao sliku u tvoj projekt
plt.savefig("Kumulativni prikaz.png", dpi=300, bbox_inches='tight')
print("Grafikon je uspješno spremljen kao 'Kumulativni prikaz.png'!")
plt.close()