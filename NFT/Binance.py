import requests, json, time

url = 'https://api.binance.com/api/v3/ticker/price?symbol='
lst = ['SOLEUR', 'DIABUSD', 'WINGUSDT', 'FORTHUSDT']


for i in lst:
    data = requests.get(url+i).json()
    print(f"{data['symbol']} --> {data['price']}")
    time.sleep(1)    