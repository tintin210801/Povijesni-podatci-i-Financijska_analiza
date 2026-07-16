import matplotlib.pyplot as plt
import seaborn as sns

# 1. Izračunaj dnevne prinose u postotcima za jedan ticker (npr. SPY ili BTC-USD)
odabrani_ticker = 'GOOGL'  # Promijeni u 'BTC-USD' ako analiziraš kripto
Prinosi = Data['Close'][odabrani_ticker].pct_change().dropna() * 100

# 2. Kreiramo privremeni DataFrame za analizu sezonalnosti
df_sezona = Prinosi.to_frame(name='Prinos')

# Izvlačimo naziv dana u tjednu i naziv mjeseca iz indexa (datuma)
df_sezona['Dan_u_tjednu'] = df_sezona.index.day_name()
df_sezona['Mjesec'] = df_sezona.index.strftime('%b')  # 'Jan', 'Feb', 'Mar'...

# Poredaj dane u tjednu kronološki (da ne idu abecedno)
dani_redoslijed = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# Ako analiziraš Bitcoin koji radi i vikendom, koristi ovaj redoslijed:
# dani_redoslijed = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Poredaj mjesece kronološki
mjeseci_redoslijed = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# 3. CRTANJE GRAFIKONA (2 grafa na jednoj slici)
fig, axes = plt.subplots(2, 1, figsize=(12, 12))

# GRAF 1: Sezonalnost po danima u tjednu
sns.boxplot(
    ax=axes[0], 
    data=df_sezona, 
    x='Dan_u_tjednu', 
    y='Prinos', 
    order=[d for d in dani_redoslijed if d in df_sezona['Dan_u_tjednu'].unique()],
    palette='Set2',
    showfliers=False  # Sakrivamo ekstremne outliere radi bolje preglednosti "kutija"
)
axes[0].set_title(f"Sezonalnost po danima u tjednu za {odabrani_ticker}", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Dan u tjednu", fontsize=11)
axes[0].set_ylabel("Dnevni prinos (%)", fontsize=11)
axes[0].axhline(0, color='red', linestyle='--', linewidth=0.8)
axes[0].grid(True, linestyle=':', alpha=0.6)

# GRAF 2: Sezonalnost po mjesecima
sns.boxplot(
    ax=axes[1], 
    data=df_sezona, 
    x='Mjesec', 
    y='Prinos', 
    order=mjeseci_redoslijed,
    palette='coolwarm',
    showfliers=False  # Sakrivamo ekstremne outliere radi bolje preglednosti
)
axes[1].set_title(f"Sezonalnost po mjesecima za {odabrani_ticker}", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Mjesec", fontsize=11)
axes[1].set_ylabel("Dnevni prinos (%)", fontsize=11)
axes[1].axhline(0, color='red', linestyle='--', linewidth=0.8)
axes[1].grid(True, linestyle=':', alpha=0.6)

# Prilagodba i prikaz
plt.tight_layout()
plt.show()
