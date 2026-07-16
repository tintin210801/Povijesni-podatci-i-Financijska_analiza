#Povijesni podatci i njihovo uređenje
#Preuzimanje i obrada cijena nekoliko imovina te izrada čitljivih statističkih izvještaja
from datetime import datetime
Tickers = ['BTC-USD', 'ETH-USD', 'SPY', 'GOOGL', 'ASML', 'TSM']
Data = yf.download(Tickers, start='2020-01-01', end= datetime.now())
Price = Data["Close"].ffill()
Price = Price.bfill()
Volume =Data["Volume"]
High = Data["High"]
Low = Data["Low"]
Price_btc =  Price["BTC-USD"]
Price_eth = Price["ETH-USD"]
Price_spy = Price["SPY"]
Price_googl = Price["GOOGL"]
Price_asml = Price["ASML"]
Price_tsm = Price["TSM"]
