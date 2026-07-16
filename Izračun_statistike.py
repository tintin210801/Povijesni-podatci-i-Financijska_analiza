import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib as plt
# Učitavanje spremljenih podataka
Data = pd.read_csv("podaci.csv", header=[0, 1], index_col=0, parse_dates=True)
Data_max = Data.max()
Data_min = Data.min()
Data_mean = Data.mean()
Data_median = Data.median()
Data_std = Data.std()

# Spajanje u tablicu i dodavanje nazive (ključeve)
Data_statistics = pd.DataFrame({
    'Max': Data_max,
    'Min': Data_min,
    'Mean (Prosjek)': Data_mean,
    'Median': Data_median,
    'Std Dev (Devijacija)': Data_std
}).T  # .T transponira tablicu kako bi statistike bile u redovima, a tickeri u stupcima

# Ispis tablice
print("STATISTIČKI PREGLED PODATAKA")
print(Data_statistics)
