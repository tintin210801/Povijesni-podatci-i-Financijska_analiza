import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib as plt
# Učitavanje spremljenih podataka
Data = pd.read_csv("podaci.csv", header=[0, 1], index_col=0, parse_dates=True)
# Izračun cijena za kasnije računanje volatilnosti
Price = Data['Close'].ffill().bfill()
Log_return = np.log(Price / Price.shift(1))
# Računanje volatilnosti
Dnevna_Stdev = Log_return.std()
God_std = Log_return.std() * np.sqrt(365) * 100
Std50 = Log_return.rolling(window=50).std()
print("Dnevna Volatilnost")
print(Dnevna_Stdev)
print("Godišnja volatilnost")
print(God_std)
print("Rolling vol 50")
print(Std50.tail(10))
