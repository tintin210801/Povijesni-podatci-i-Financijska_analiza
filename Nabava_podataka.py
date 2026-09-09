import yfinance as yf
import numpy as np
import pandas as pd
from datetime import datetime

# Omogućujemo korisniku unos tickera (odvojenih zarezom ili razmakom)
unos_korisnika = input("Unesite tickere odvojene zarezom (npr. BTC-USD, ETH-USD, SPY) ili pritisnite Enter za zadane: ").strip()

if unos_korisnika:
    # Pretvaramo unos u listu i mičemo eventualne suvišne razmake
    Tickers = [t.strip().upper() for t in unos_korisnika.split(",") if t.strip()]
else:
    # Zadana lista ako korisnik ništa ne upiše
    Tickers = ['BTC-USD', 'ETH-USD', 'SPY', 'GOOGL', 'ASML', 'TSM']

print(f"\n[INFO] Preuzimanje podataka za tickere: {Tickers}")

# Povijesni podatci i njihovo uređenje
Data = yf.download(Tickers, start='2020-01-01', end=datetime.now())

# Spremanje podataka u zajedničku datoteku
Data.to_csv("podaci.csv")
print("Podaci su uspješno spremljeni u podaci.csv!")