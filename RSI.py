# RSI indikator
# Izračun dnevne razlike u cijeni
delta = Price.diff()

# Dobitci i gubitci
gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)

# Eksponencijalni prosjek (EMA) za dobitke i gubitke
avg_gain = gain.ewm(com=13, adjust=False).mean()
avg_loss = loss.ewm(com=13, adjust=False).mean()

# Izračun relativne snage (RS) i RSI
rs = avg_gain / avg_loss
RSI = 100 - (100 / (1 + rs))

# Primjer dohvaćanja RSI-a za jednu imovinu i cjelokupnu imovinu
print(RSI['BTC-USD'].tail())
print(RSI.tail())
