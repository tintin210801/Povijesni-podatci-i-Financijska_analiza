import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib as plt
# Linijski grafikon
Cum_return.plot(kind='line', figsize=(12, 6), linewidth=1.5)

plt.title("Kumulativni rast", fontsize=14, fontweight='bold')
plt.xlabel("Datum")
plt.ylabel("Rast (npr. 1.0 = 100% zarade)")
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(title="Tickeri")

plt.show()
