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
