# Bollingerove trake
# Srednja traka (Jednostavni pomični prosjek - SMA 20)
BB_middle_btc = Price_btc.rolling(window=50).mean()

# Standardna devijacija od 20 dana
BB_std_btc = Price_btc.rolling(window=50).std()

# Gornja i donja traka
BB_upper_btc = BB_middle_btc + (BB_std_btc * 2)
BB_lower_btc = BB_middle_btc - (BB_std_btc * 2)


# GRAFIČKI PRIKAZ

plt.figure(figsize=(12, 6))

# stvarne cijene Bitcoina
plt.plot(
    Price_btc.index, Price_btc, label="Cijena (BTC)", color="black", linewidth=1.5
)

# Bollingerove trake
plt.plot(
    BB_upper_btc.index,
    BB_upper_btc,
    label="Gornja traka (+2 std)",
    color="red",
    linestyle="--",
    alpha=0.7,
)
plt.plot(
    BB_middle_btc.index,
    BB_middle_btc,
    label="Srednja traka (SMA 50)",
    color="blue",
    alpha=0.7,
)
plt.plot(
    BB_lower_btc.index,
    BB_lower_btc,
    label="Donja traka (-2 std)",
    color="green",
    linestyle="--",
    alpha=0.7,
)

# 3. Osjenčavanje prostora između gornje i donje trake (vizualno najbitniji dio)
plt.fill_between(
    Price_btc.index,
    BB_lower_btc,
    BB_upper_btc,
    color="gray",
    alpha=0.1,
    label="Područje kanala",
)

# 4. Uređivanje i estetika grafikona
plt.title(
    "Bollingerove trake (Bollinger Bands) - BTC-USD",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Datum", fontsize=10)
plt.ylabel("Cijena (USD)", fontsize=10)
plt.grid(True, linestyle=":", alpha=0.5)
plt.legend(loc="upper left")

# Prikaz grafikona
plt.show()
