import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Učitavanje spremljenih podataka
Data = pd.read_csv("podaci.csv", header=[0, 1], index_col=0, parse_dates=True)

# Dobivanje cijena zatvaranja za sve dostupne tickere u DataFrame-u
Price = Data['Close'].ffill().bfill()

# Dinamičko dohvaćanje dostupnih tickera iz stupaca
available_tickers = Price.columns.tolist()
print("Dostupni tickeri:", available_tickers)

# Primjer pojedinačnog dohvaćanja za prvi dostupni ticker (ako postoji)
if len(available_tickers) > 0:
    first_ticker = available_tickers[0]
    Price_first = Price[first_ticker]
    print(f"Podaci za {first_ticker} uspješno učitani.")

# Računanje prinosa za sve tickere odjednom
Return = Price.pct_change()
Log_return = np.log(Price / Price.shift(1))

# Kumulativni prinosi
Cum_return = ((Price / Price.iloc[0]) - 1)
Kumulativni_povrat = (1 + Price.pct_change()).cumprod() - 1

# Ispis rezultata
print("\nLogaritamski prinos:")
print(Log_return.tail())

print("\nKumulativni prinos (prvih 5 redova):")
print(Cum_return.head())

print("\nKumulativni prinos (zadnjih 5 redova):")
print(Cum_return.tail())