# Računanje metrika prinosa i ostalih vrsti prinosa
Return = Price.pct_change()
Return_btc = Price_btc.pct_change()
Log_return = np.log(Price / Price.shift(1))
#1. Formula za kum. prinos, jednostavnija i daje isti rezultat kao 2. kompleksnija ali mora imati uređene podatke
Cum_return = ((Price / Price.iloc[0]) - 1)
#2. Formula, kompleksnija ali ne mora imati uređene podatke
Kumulativni_povrat = (1 +Price.pct_change()).cumprod() - 1
print("Logaritamski prinos")
print(Log_return)
print("Kumulativni prinos")
print(Cum_return.head(10))
print(Cum_return.tail(10))
print("Kumulativni prinos")
print(Kumulativni_povrat)
