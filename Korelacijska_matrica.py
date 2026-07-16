# Izvuci cijene zatvaranja i volumen za odabrane tickere
# (Radimo novu tablicu u kojoj su stupci jasno definirani)
cijene = Data['Close']
volumeni = Data['Volume']

korelacijska_matrica_cijena = cijene.corr()
korelacijska_matrica_volumena = volumeni.corr()
# Toplinska mapa (Heatmap)
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
