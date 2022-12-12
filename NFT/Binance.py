# Import libraries
import json
import requests
from itertools import zip_longest
# Defining Binance API URL
url1 = "https://www.binance.com/api/v3/ticker/24hr"
data = requests.get(url1).json()

d = {}

for i in data:
    d[i['symbol']] = float(i['priceChangePercent'])

d = sorted(d.items(), key=lambda x:x[1], reverse=True)
x = [(k,v) for k,v in d if  v > 30]
print("\n".join([str(i) for i in x]))

print()

key = 'https://api.binance.com/api/v3/ticker/price?symbol='

currencies = ['RVNBUSD','TBUSD', 'POLYXBUSD', 'GALBUSD', 'DIABUSD', 'SOLBUSD', 'LINKEUR']
prices = [0.02423, 0.0196, 0.1471, 1.2838]
j = 0
for i,k in zip_longest(currencies,prices):
    url = key+currencies[j]
    data = requests.get(url).json()
    symbol, price = data['symbol'], float(data['price']) 
    j += 1
    if i != None and k != None:
        print(f"{symbol} bought - {k}")
        print(f"price is         {price:.5f}")
        print(f"Difference -->   {price - k:.5f}\n")
    else:
        print(f"{symbol} -->  {price:.3f}\n")
