import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Učitavanje spremljenih podataka
Data = pd.read_csv("podaci.csv", header=[0, 1], index_col=0, parse_dates=True)
Price = Data['Close'].ffill().bfill()
tickers = Price.columns.tolist()
print(f"Pronađeno {len(tickers)} imovina: {tickers}")

# ============================================
# 1. POJEDINAČNI GRAFIKONI
# ============================================
for ticker in tickers:
    try:   
        print(f"Obrađujem: {ticker}")
        Price_current = Price[ticker]

        # Bollingerove trake
        BB_middle = Price_current.rolling(window=50).mean()
        BB_std = Price_current.rolling(window=50).std()
        BB_upper = BB_middle + (BB_std * 2)
        BB_lower = BB_middle - (BB_std * 2)

        # GRAFIČKI PRIKAZ za pojedinačni ticker
        plt.figure(figsize=(12, 6))

        plt.plot(Price_current.index, Price_current, label=f"Cijena ({ticker})", color="black", linewidth=1.5)
        plt.plot(BB_upper.index, BB_upper, label="Gornja traka (+2 std)", color="red", linestyle="--", alpha=0.7)
        plt.plot(BB_middle.index, BB_middle, label="Srednja traka (SMA 50)", color="blue", alpha=0.7)
        plt.plot(BB_lower.index, BB_lower, label="Donja traka (-2 std)", color="green", linestyle="--", alpha=0.7)
        plt.fill_between(Price_current.index, BB_lower, BB_upper, color="gray", alpha=0.1, label="Područje kanala")

        plt.title(f"Bollingerove trake - {ticker}", fontsize=14, fontweight="bold")
        plt.xlabel("Datum", fontsize=10)
        plt.ylabel("Cijena (USD)", fontsize=10)
        plt.grid(True, linestyle=":", alpha=0.5)
        plt.legend(loc="upper left")
        
        plt.savefig(f"Bollingerove_trake_{ticker}.png", dpi=300, bbox_inches='tight')
        print(f"Grafikon za {ticker} spremljen")
        plt.close()
        
    except Exception as e:
        print(f"Greška pri obradi tickera {ticker}: {e}")
        continue

# ============================================
# 2. PODGRAFOVI - 6 GRAFOVA PO SLICI
# ============================================
print("\n" + "="*50)
print("Kreiram podgrafove (6 grafova po slici)...")
print("="*50)

def create_subplots(tickers_list, start_idx, fig_num):
    """Kreira podgrafove za 6 tickera po slici"""
    n = len(tickers_list)
    cols = 3
    rows = 2
    
    fig, axes = plt.subplots(rows, cols, figsize=(18, 10))
    fig.suptitle(f'Bollingerove trake - Svi tickeri (dio {fig_num})', 
                 fontsize=16, fontweight='bold')
    
    axes = axes.flatten()
    
    for i, ticker in enumerate(tickers_list):
        Price_current = Price[ticker]
        
        # Bollingerove trake
        BB_middle = Price_current.rolling(window=50).mean()
        BB_std = Price_current.rolling(window=50).std()
        BB_upper = BB_middle + (BB_std * 2)
        BB_lower = BB_middle - (BB_std * 2)
        
        # Crtanje
        axes[i].plot(Price_current.index, Price_current, 
                    color='black', linewidth=1, alpha=0.7, label='Cijena')
        axes[i].plot(BB_upper.index, BB_upper, 
                    color='red', linestyle='--', linewidth=0.8, alpha=0.5, label='Gornja')
        axes[i].plot(BB_middle.index, BB_middle, 
                    color='blue', linewidth=0.8, alpha=0.5, label='SMA 50')
        axes[i].plot(BB_lower.index, BB_lower, 
                    color='green', linestyle='--', linewidth=0.8, alpha=0.5, label='Donja')
        axes[i].fill_between(Price_current.index, BB_lower, BB_upper, 
                            color='gray', alpha=0.1)
        
        # Statusna poruka
        zadnja_cijena = Price_current.iloc[-1]
        zadnji_upper = BB_upper.iloc[-1]
        zadnji_lower = BB_lower.iloc[-1]
        
        if not np.isnan(zadnji_upper) and not np.isnan(zadnji_lower):
            if zadnja_cijena > zadnji_upper:
                status = "🔴 Iznad gornje"
                color_status = 'red'
            elif zadnja_cijena < zadnji_lower:
                status = "🟢 Ispod donje"
                color_status = 'green'
            else:
                status = "⚪ U kanalu"
                color_status = 'blue'
            
            axes[i].text(0.02, 0.95, status, transform=axes[i].transAxes, 
                        fontsize=8, verticalalignment='top', color=color_status,
                        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        axes[i].set_title(ticker, fontsize=10, fontweight='bold')
        axes[i].grid(True, linestyle=":", alpha=0.5)
        axes[i].legend(loc='upper left', fontsize=6)
    
    # Sakrij prazne podgrafove
    for j in range(len(tickers_list), len(axes)):
        axes[j].axis('off')
    
    plt.tight_layout()
    filename = f"Podgrafovi_Bollinger_{fig_num}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Podgrafovi spremljeni kao '{filename}'")
    plt.close()

# Podijeli tickere u grupe po 6
batch_size = 6
for i in range(0, len(tickers), batch_size):
    batch = tickers[i:i+batch_size]
    fig_num = i // batch_size + 1
    create_subplots(batch, i, fig_num)

# ============================================
# 3. PODGRAFOVI - SVI TICKERI NA JEDNOJ SLICI
# ============================================
print("\n" + "="*50)
print("Kreiram podgrafove (svi tickeri na jednoj slici)...")
print("="*50)

try:
    n = len(tickers)
    cols = 3
    rows = (n + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(18, 6*rows))
    fig.suptitle('Bollingerove trake - Svi tickeri (kompletno)', 
                 fontsize=16, fontweight='bold')
    axes = axes.flatten() if n > 1 else [axes]

    for i, ticker in enumerate(tickers):
        if i < n:
            Price_current = Price[ticker]
            
            # Bollingerove trake
            BB_middle = Price_current.rolling(window=50).mean()
            BB_std = Price_current.rolling(window=50).std()
            BB_upper = BB_middle + (BB_std * 2)
            BB_lower = BB_middle - (BB_std * 2)
            
            # Crtanje
            axes[i].plot(Price_current.index, Price_current, 
                        color='black', linewidth=1, alpha=0.7)
            axes[i].plot(BB_upper.index, BB_upper, 
                        color='red', linestyle='--', linewidth=0.8, alpha=0.5)
            axes[i].plot(BB_middle.index, BB_middle, 
                        color='blue', linewidth=0.8, alpha=0.5)
            axes[i].plot(BB_lower.index, BB_lower, 
                        color='green', linestyle='--', linewidth=0.8, alpha=0.5)
            axes[i].fill_between(Price_current.index, BB_lower, BB_upper, 
                                color='gray', alpha=0.1)
            
            # Status
            zadnja_cijena = Price_current.iloc[-1]
            zadnji_upper = BB_upper.iloc[-1]
            zadnji_lower = BB_lower.iloc[-1]
            
            if not np.isnan(zadnji_upper) and not np.isnan(zadnji_lower):
                if zadnja_cijena > zadnji_upper:
                    status = "🔴 Iznad"
                elif zadnja_cijena < zadnji_lower:
                    status = "🟢 Ispod"
                else:
                    status = "⚪ U kanalu"
                
                axes[i].text(0.02, 0.95, status, transform=axes[i].transAxes, 
                            fontsize=7, verticalalignment='top',
                            bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
            
            axes[i].set_title(ticker, fontsize=8, fontweight='bold')
            axes[i].grid(True, linestyle=":", alpha=0.5)
            axes[i].tick_params(labelsize=6)

    # Sakrij prazne podgrafove
    for j in range(i+1, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.savefig("Svi_tickeri_Bollinger_kompletno.png", dpi=300, bbox_inches='tight')
    print("Podgrafovi spremljeni kao 'Svi_tickeri_Bollinger_kompletno.png'")
    plt.close()
    
except Exception as e:
    print(f"Greška pri kreiranju podgrafova: {e}")

# ============================================
# 4. DODATNA ANALIZA - SIGNALI
# ============================================
print("\n" + "="*50)
print("Analiza Bollinger Band signala...")
print("="*50)

try:
    signali = []
    
    for ticker in tickers:
        Price_current = Price[ticker]
        
        # Bollingerove trake
        BB_middle = Price_current.rolling(window=50).mean()
        BB_std = Price_current.rolling(window=50).std()
        BB_upper = BB_middle + (BB_std * 2)
        BB_lower = BB_middle - (BB_std * 2)
        
        if len(Price_current) > 0 and len(BB_upper) > 0:
            zadnja_cijena = Price_current.iloc[-1]
            zadnji_upper = BB_upper.iloc[-1]
            zadnji_lower = BB_lower.iloc[-1]
            zadnji_middle = BB_middle.iloc[-1]
            
            if not np.isnan(zadnji_upper) and not np.isnan(zadnji_lower):
                if zadnja_cijena > zadnji_upper:
                    signal = "🔴 PRODAJA"
                elif zadnja_cijena < zadnji_lower:
                    signal = "🟢 KUPNJA"
                elif zadnja_cijena > zadnji_middle:
                    signal = "🔵 BULL"
                else:
                    signal = "🟠 BEAR"
                
                width = (zadnji_upper - zadnji_lower) / zadnji_middle * 100
                
                signali.append({
                    'Ticker': ticker,
                    'Zadnja cijena': f"{zadnja_cijena:.2f}",
                    'Gornja': f"{zadnji_upper:.2f}",
                    'Srednja': f"{zadnji_middle:.2f}",
                    'Donja': f"{zadnji_lower:.2f}",
                    'Širina kanala (%)': f"{width:.2f}",
                    'Signal': signal
                })
    
    if signali:
        df_signali = pd.DataFrame(signali)
        
        print("\n=== BOLLINGER BAND SIGNALI ===")
        print(df_signali.to_string(index=False))
        
        df_signali.to_csv("Bollinger_signali.csv", index=False)
        print("\nSignali spremljeni u 'Bollinger_signali.csv'")
        
        # Grafikon širine kanala
        plt.figure(figsize=(12, 6))
        df_sorted = df_signali.sort_values('Širina kanala (%)', ascending=False)
        
        # Boje prema signalu
        color_map = {
            '🔴 PRODAJA': 'red',
            '🟢 KUPNJA': 'green',
            '🔵 BIKOVSKI': 'blue',
            '🟠 MEDVJEĐI': 'orange'
        }
        colors = [color_map.get(x.split()[0], 'gray') for x in df_sorted['Signal']]
        
        plt.barh(df_sorted['Ticker'], df_sorted['Širina kanala (%)'].astype(float), 
                color=colors, alpha=0.7)
        plt.axvline(df_sorted['Širina kanala (%)'].astype(float).mean(), 
                   color='black', linestyle='--', alpha=0.5, label='Prosjek')
        plt.title('Širina Bollinger kanala po tickerima', fontsize=14, fontweight='bold')
        plt.xlabel('Širina kanala (%)', fontsize=12)
        plt.grid(True, linestyle=':', alpha=0.5)
        plt.legend(['Prosjek', 'Signal'])
        plt.tight_layout()
        plt.savefig("Bollinger_sirina_kanala.png", dpi=300, bbox_inches='tight')
        print("Grafikon širine kanala spremljen kao 'Bollinger_sirina_kanala.png'")
        plt.close()
        
except Exception as e:
    print(f"Greška pri analizi: {e}")

print("\n" + "="*50)
print("SVI TICKERI SU OBRADJENI!")
print("="*50)