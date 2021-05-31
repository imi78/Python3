import requests
# import re

# currency_pattern = "^[a-zA-Z]{3}$"  # matches exactly thre chars

url = 'http://data.fixer.io/api/latest?access_key=c1bf0b4af0dd8939a2da6c80e10c5bbf'
data = requests.get(url).json()
# rates = {}
rates = data['rates']

def convert(from_currency, to_currency, amount):

  if from_currency in rates and to_currency in rates and amount.isdigit():
    print(from_currency)
    initial_amount = int(amount)
    amount = amount / rates[from_currency]  # calculates the base currency (EUR) rates
    amount = round(amount * rates[to_currency], 2)  # then re-calculates the rate to the given currency
    print(f'{initial_amount} {from_currency} = {amount:.2f} {to_currency}')
  else:
    if from_currency not in rates or to_currency not in rates:
      print('Enter a valid three letter currency')
    if amount.isdigit() == False:
      print('Enter a valid amount')

 

from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()
amount = input("Amount: ")


convert(from_currency, to_currency, amount)

