import requests

# import re

# currency_pattern = "^[a-zA-Z]{3}$"  # matches exactly thre chars

url = 'https://free.currconv.com/api/v7/currencies?apiKey=fe444f880c2cb85b3f6a'
data = requests.get(url).json()['results']
currency = {}
lst = []
for k, v in data.items():
  currency[k] = v['currencyName']
  lst.append(f"{k} - {v['currencyName']}")
             
# currency = sorted(currency)  # sorted dict by keys
print(lst)

# def convert(from_currency, to_currency, amount):
#     if from_currency in rates and to_currency in rates and amount.isdigit():
#         initial_amount = int(amount)
#         amount = amount / rates[from_currency]  # calculates the base currency (EUR) rates
#         amount = round(amount * rates[to_currency], 2)  # then re-calculates the rate to the given currency
#         print(f'{initial_amount} {from_currency} = {amount:.2f} {to_currency}')
#     else:
#         if from_currency not in rates or to_currency not in rates:
#             print('Enter a valid three letter currency')
#         if amount.isdigit() == False:
#             print('Enter a valid amount')


# from_currency = input("From currency: ").upper()
# to_currency = input("To currency: ").upper()
# amount = input("Amount: ")

# convert(from_currency, to_currency, amount)
