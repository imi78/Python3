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

currencies = ['RVNBUSD','LEVERBUSD', 'POLYXBUSD', 'GALBUSD', 'BURGERBUSD', 'DIABUSD', 'YFIEUR']
prices = [0.02423, 0.00207, 0.1471, 1.28380, 0.75000, 0.47600, 7199]
j = 0
for i,k in zip_longest(currencies,prices):
    url = key+currencies[j]
    data = requests.get(url).json()
    symbol, price = data['symbol'], float(data['price']) 
    j += 1
    if i != None and k != None:
        print(f"{symbol} bought - {k}")
        print(f"price is         {price:.5f}")
        diff = price - k
        print(f"Difference --> {round(diff, 5)}")
        print(f"In percentage --> {(diff/k)*100:.2f}\n")
    else:
        print(f"{symbol} -->  {price:.3f}\n")
        
currency = ['LINK-EUR', 'XYO-EUR', 'DIA-EUR', 'SHIB-EUR']
price = [28, 0.05, 0.38, 0.00001319]

for i, p in zip(currency,price):
    key1 = 'https://api.pro.coinbase.com/products/'+i+'/ticker'
    data = requests.get(key1).json()
    print(f"{i} bought - {p}")
    diff1 = float(data['price']) - p
    print(f"price    --> {data['price']}")
    print(f"Difference --> {round(diff1, 5)}")
    print(f"In percentage --> {(diff1/p)*100:.2f}\n")
    
