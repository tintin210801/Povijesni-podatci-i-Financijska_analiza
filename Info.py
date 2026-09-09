import yfinance as yf
import pandas as pd

def dohvati_info_imovine(ticker_symbol):
    """
    Dohvaća opće informacije, ključne pokazatelje i profil za zadanu dionicu ili kriptovalutu.
    """
    print(f"\n[INFO] Dohvaćam opće informacije za: {ticker_symbol.upper()}...")
    asset = yf.Ticker(ticker_symbol)
    
    # .info vraća veliki rječnik (dictionary) s podacima
    info = asset.info
    
    if not info or len(info) < 5:
        print(f"[GREŠKA] Nije moguće pronaći podatke za ticker '{ticker_symbol}'. Provjerite naziv.")
        return None

    # Izvlačenje ključnih podataka s provjerom ključeva (da ne pukne ako neki podatak ne postoji, npr. za kripto)
    podaci = {
        "Ticker": ticker_symbol.upper(),
        "Naziv": info.get("longName", info.get("shortName", "N/A")),
        "Tip imovine": info.get("quoteType", "N/A"),
        "Valuta": info.get("currency", "N/A"),
        "Burza": info.get("exchange", "N/A"),
        "Trenutna cijena": info.get("currentPrice", info.get("regularMarketPrice", "N/A")),
        "Tržišna kapitalizacija": info.get("marketCap", "N/A"),
        "52 tjedna visoko": info.get("fiftyTwoWeekHigh", "N/A"),
        "52 tjedna nisko": info.get("fiftyTwoWeekLow", "N/A"),
        "P/E omjer (Trailing)": info.get("trailingPE", "N/A"),
        "Dividendni prinos (%)": info.get("dividendYield", 0),
        "Sektor": info.get("sector", "N/A"),
        "Industrija": info.get("industry", "N/A"),
        "Web stranica": info.get("website", "N/A")
    }
    
    # Pretvorba dividendnog prinosa u postotak ako postoji
    if isinstance(podaci["Dividendni prinos (%)"], (int, float)):
        podaci["Dividendni prinos (%)"] = round(podaci["Dividendni prinos (%)"] * 100, 2)

    # Ispis u terminal u urednom obliku
    print("\n" + "="*50)
    print(f" OSNOVNE INFORMACIJE: {podaci['Naziv']} ({podaci['Ticker']})")
    print("="*50)
    for kljuc, vrijednost in podaci.items():
        print(f"{kljuc.ljust(25)}: {vrijednost}")
    print("="*50)

    
    
    return info

if __name__ == "__main__":
    # Automatsko čitanje tickera iz podaci.csv umjesto ručnog unosa
    import os
    if os.path.exists("podaci.csv"):
        df_temp = pd.read_csv("podaci.csv", header=[0, 1], index_col=0)
        tickers = df_temp['Close'].columns.tolist() if isinstance(df_temp.columns, pd.MultiIndex) else df_temp.columns.tolist()
        
        for t in tickers:
            dohvati_info_imovine(t)
    else:
        # Fallback ako csv ne postoji
        dohvati_info_imovine("NVDA")