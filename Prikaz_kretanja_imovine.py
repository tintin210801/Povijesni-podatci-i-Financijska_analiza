ticker_1 = 'ASML'
ticker_2 = 'ETH-USD'
ticker_3 = 'SPY'
#Kretanje cijena imovine kroz vrijeme
plt.figure(figsize=(12, 6))
plt.plot(Price[ticker_1], label=ticker_1, color='orange', linewidth=1.5, alpha=0.8)
plt.plot(Price[ticker_2], label=ticker_2, color='navy', linewidth=1.5, alpha=0.8)
plt.plot(Price[ticker_3], label=ticker_3, color='red', linewidth=1.5, alpha=0.8)
plt.title("Kretanje cijena imovine kroz vrijeme", fontsize=14, fontweight='bold')
plt.xlabel("Datum", fontsize=12)
plt.ylabel("Cijena (USD)", fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
