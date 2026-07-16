import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Učitavanje spremljenih podataka
Data = pd.read_csv("podaci.csv", header=[0, 1], index_col=0, parse_dates=True)
# Izvuci cijene zatvaranja i volumen za odabrane tickere
# (Radimo novu tablicu u kojoj su stupci jasno definirani)
cijene = Data['Close'].ffill().bfill()
volumeni = Data['Volume']

korelacijska_matrica_cijena = cijene.corr()
korelacijska_matrica_volumena = volumeni.corr()
# Toplinska mapa (Heatmap) korelacija cijena
plt.figure(figsize=(10, 6))

# 'annot=True' ispisuje točne brojeve korelacije u svakom kvadratiću
# 'cmap=coolwarm' koristi plavu boju za negativnu, a crvenu za pozitivnu korelaciju
sns.heatmap(
    korelacijska_matrica_cijena, 
    annot=True, 
    cmap='coolwarm', 
    fmt=".2f", 
    linewidths=0.5,
    vmin=-1, vmax=1  # Korelacija je uvijek u rasponu od -1 do 1
)

plt.title("Korelacijska matrica cijena", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
# Sprema grafikon kao sliku u tvoj projekt
plt.savefig("Korelacijska matrica cijene.png", dpi=300, bbox_inches='tight')
print("Grafikon je uspješno spremljen kao 'Korelacijska matrica cijene.png'!")
plt.close()

# Toplinska mapa (Heatmap) korelacija volumena
plt.figure(figsize=(10, 6))
sns.heatmap(
    korelacijska_matrica_volumena, 
    annot=True, 
    cmap='coolwarm', 
    fmt=".2f", 
    linewidths=0.5,
    vmin=-1, vmax=1  # Korelacija je uvijek u rasponu od -1 do 1
)
plt.title("Korelacijska matrica volumena", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
# Sprema grafikon kao sliku u tvoj projekt
plt.savefig("Korelacijska matrica volumena.png", dpi=300, bbox_inches='tight')
print("Grafikon je uspješno spremljen kao 'Korelacijska matrica volumena.png'!")
plt.close()


# Toplinska mapa (Heatmap) korelacija cijena i volumena kombinirano
# Spojit ćemo ih tako da preimenujemo stupce kako bismo znali što je što
# npr. 'BTC-USD_Price' i 'BTC-USD_Volume'
kombinirano = cijene.join(volumeni, lsuffix='_Price', rsuffix='_Volume')

# Izračun korelacijske matrice
korelacijska_matrica = kombinirano.corr()

# Vizualizacija toplinske mape (Heatmap)
plt.figure(figsize=(12, 10))

# 'annot=True' ispisuje točne brojeve korelacije u svakom kvadratiću
# 'cmap=coolwarm' koristi plavu boju za negativnu, a crvenu za pozitivnu korelaciju
sns.heatmap(
    korelacijska_matrica, 
    annot=True, 
    cmap='coolwarm', 
    fmt=".2f", 
    linewidths=0.5,
    vmin=-1, vmax=1  # Korelacija je uvijek u rasponu od -1 do 1
)

plt.title("Korelacijska matrica: Cijene i Volumen", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
# Sprema grafikon kao sliku u tvoj projekt
plt.savefig("Korelacijska matrica cijene i volumena.png", dpi=300, bbox_inches='tight')
print("Grafikon je uspješno spremljen kao 'Korelacijska matrica cijene i volumena.png'!")
plt.close()