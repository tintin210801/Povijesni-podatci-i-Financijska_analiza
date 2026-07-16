import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib as plt
# Učitavanje spremljenih podataka
Data = pd.read_csv("podaci.csv", header=[0, 1], index_col=0, parse_dates=True)
# Priprema podataka
Data_shape = Data.shape
Data_columns = Data.columns
Data_dtypes = Data.dtypes
Data_head = Data.head(5)
Data_tail = Data.tail(5) 
print("=" * 60)
print("                  PREGLED STRUKTURE PODATAKA")
print("=" * 60)

print(f"DIMENZIJE: {Data_shape[0]} redova, {Data_shape[1]} stupaca")
print("-" * 60)

print("STUPCI:")
print(list(Data_columns))
print("-" * 60)

print("TIPOVI PODATAKA (Dtypes):")
print(Data_dtypes)
print("-" * 60)

print("PRVIH 5 REDOVA:")
print(Data_head)
print("-" * 60)

print("ZADNJIH 5 REDOVA:")
print(Data_tail)
print("=" * 60)
