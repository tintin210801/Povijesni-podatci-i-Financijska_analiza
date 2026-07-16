#Histogram dnevnih prinosa na primjeru ASML-a
import matplotlib.pyplot as plt
import seaborn as sns  # Seaborn koristimo za ljepši izgled i krivulju gustoće (KDE)

# Izračun dnevnih povrat< i brisanje NaN vrijednosti
odabrani_ticker = 'ETH-USD'
Prinosi = Data['Close'][odabrani_ticker].pct_change().dropna()

# Pretvaranje u postotke 
Prinosi_u_postotcima = Prinosi * 100

# Pravljenje grafikona
plt.figure(figsize=(10, 6))

# Crtanje histograma s krivuljom gustoće (KDE - Kernel Density Estimate)
# bins=50 dijeli podatke u 50 stupaca za optimalnu detaljnost
sns.histplot(Prinosi_u_postotcima, bins=100, kde=True, color='royalblue', edgecolor='black', alpha=0.7)

# Dodavanje statističkih linija (Prosjek i Medijan)
prosjek = Prinosi_u_postotcima.mean()
medijan = Prinosi_u_postotcima.median()

# Vertikalna crvena linija za prosjek (mean)
plt.axvline(prosjek, color='red', linestyle='--', linewidth=1.5, 
            label=f'Prosjek (Mean): {prosjek:.2f}%')

# Vertikalna zelena linija za medijan (median)
plt.axvline(medijan, color='green', linestyle='-', linewidth=1.5, 
            label=f'Medijan (Median): {medijan:.2f}%')

# Estetsko uređivanje
plt.title(f"Distribucija dnevnih prinosa za {odabrani_ticker}", fontsize=14, fontweight='bold')
plt.xlabel("Dnevni prinos (%)", fontsize=12)
plt.ylabel("Broj dana (Frekvencija)", fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=10)

# Prikaz grafikona
plt.tight_layout()
plt.show()
